package ResourcesControl

import (
	"dotcs/minecraft/protocol"
	"fmt"
	"sync/atomic"
)

// 提交物品请求 ID 为 key 的物品操作。
// howToChange 指代相应槽位的变动结果，这用于更新本地库存数据
func (i *itemStackRequestWithResponse) WriteRequest(
	key int32,
	howToChange map[ContainerID]StackRequestContainerInfo,
) error {
	_, exist := i.requestWithResponse.Load(key)
	if exist {
		return fmt.Errorf("WriteRequest: %v has already existed", key)
	}
	// if key has already exist
	i.requestWithResponse.Store(
		key,
		singleItemStackRequestWithResponse{
			resp:        make(chan protocol.ItemStackResponse, 1),
			howToChange: howToChange,
		},
	)
	// write request
	return nil
	// return
}

// 向请求 ID 为 key 的物品操作写入返回值 resp 。
// 当 key 不存在时，将会抛出程序 panic 。
// 属于私有实现。
func (i *itemStackRequestWithResponse) writeResponse(
	key int32,
	resp protocol.ItemStackResponse,
) {
	value, exist := i.requestWithResponse.Load(key)
	if !exist {
		panic("writeResponse: Attempt to send packet.ItemStackRequest without using ResourcesControlCenter")
	}
	// if key is not exist
	get, normal := value.(singleItemStackRequestWithResponse)
	if !normal {
		panic(fmt.Sprintf("writeResponse: Failed to convert value into singleItemStackRequestWithResponse; value = %#v", value))
	}
	// convert data
	get.resp <- resp
	// send response
}

// 读取请求 ID 为 key 的物品操作请求的返回值，
// 同时移除此物品操作请求
func (i *itemStackRequestWithResponse) LoadResponseAndDelete(key int32) (protocol.ItemStackResponse, error) {
	value, exist := i.requestWithResponse.Load(key)
	if !exist {
		return protocol.ItemStackResponse{}, fmt.Errorf("LoadResponseAndDelete: %v is not recorded", key)
	}
	// if key is not exist
	get, normal := value.(singleItemStackRequestWithResponse)
	if !normal {
		return protocol.ItemStackResponse{}, fmt.Errorf("tryToWriteResponse: Failed to convert value into singleItemStackRequestWithResponse; value = %#v", value)
	}
	// convert data
	ret := <-get.resp
	i.requestWithResponse.Delete(key)
	return ret, nil
	// return
}

// 以原子操作获取上一次的请求 ID ，即 RequestID 。
// 如果从未进行过物品操作，则将会返回 1
func (i *itemStackRequestWithResponse) GetCurrentRequestID() int32 {
	return atomic.LoadInt32(&i.currentRequestID)
}

// 以原子操作获取一个新的请求 ID ，即 RequestID
func (i *itemStackRequestWithResponse) GetNewRequestID() int32 {
	return atomic.AddInt32(&i.currentRequestID, -2)
}

// 利用 newItemName 更新 item 中存储的物品名称信息。
// 如果传入的 newItemName 为空字符串，则将会从 item 中移除物品名称信息
func (i *itemStackRequestWithResponse) SetItemName(
	item *protocol.ItemInstance,
	newItemName string,
) error {
	nbt := item.Stack.NBTData
	// get nbt datas
	defer func() {
		item.Stack.NBTData = nbt
	}()
	// while exit
	deleteDisplay := func() {
		delete(nbt, "display")
		newMap := map[string]interface{}{}
		for key, value := range nbt {
			newMap[key] = value
		}
		nbt = newMap
	}
	deleteName := func() {
		delete(nbt["display"].(map[string]interface{}), "Name")
		newMap := map[string]interface{}{}
		for key, value := range nbt["display"].(map[string]interface{}) {
			newMap[key] = value
		}
		nbt["display"] = newMap
	}
	// init func
	if newItemName != "" {
		_, ok := nbt["display"]
		if !ok {
			nbt["display"] = map[string]interface{}{}
		}
		_, normal := nbt["display"].(map[string]interface{})
		if !normal {
			return fmt.Errorf("SetItemName: Failed to convert nbt[\"display\"] into map[string]interface{}; nbt = %#v", nbt)
		}
		// display
		nbt["display"].(map[string]interface{})["Name"] = newItemName
		// name
		return nil
		// return
	} else {
		_, ok := nbt["display"]
		if !ok {
			return nil
		}
		_, normal := nbt["display"].(map[string]interface{})
		if !normal {
			return fmt.Errorf("SetItemName: Failed to convert nbt[\"display\"] into map[string]interface{}; nbt = %#v", nbt)
		}
		// display
		_, ok = nbt["display"].(map[string]interface{})["Name"]
		if ok {
			deleteName()
		}
		if len(nbt["display"].(map[string]interface{})) <= 0 {
			deleteDisplay()
		}
		// name
		return nil
		// return
	}
	// update names
}

// 根据 newItem 中预期的新数据和租赁服返回的 resp ，
// 返回完整的新物品数据。
func (i *itemStackRequestWithResponse) GetNewItemData(
	newItem protocol.ItemInstance,
	resp protocol.StackResponseSlotInfo,
) (protocol.ItemInstance, error) {
	nbt := newItem.Stack.NBTData
	// 获取物品的旧 NBT 数据
	newItem.Stack.NBTData = nbt
	newItem.Stack.Count = uint16(resp.Count)
	newItem.StackNetworkID = resp.StackNetworkID
	/*
		newItem.Stack.MetadataValue = uint32(resp.DurabilityCorrection) [This line of code has not been tested for validity]
	*/
	// update values
	return newItem, nil
	// return
}

/*
根据租赁服返回的 resp 字段更新对应库存中对应槽位的物品数据。
inventory 必须是一个指针，它指向了客户端库存数据在内存中存放的地址。
此函数属于私有实现。

由于返回的 resp 字段不完整，因此此函数内部使用 i.LoadRequest(resp.RequestID)
来加载原有的请求数据，并访问其中描述的物品变动的预期结果，
然后依此字段和 resp 字段更新本地库存数据。
*/
func (i *itemStackRequestWithResponse) updateItemData(
	resp protocol.ItemStackResponse,
	inventory *inventoryContents,
) error {
	value, exist := i.requestWithResponse.Load(resp.RequestID)
	if !exist {
		panic("updateItemData: Attempt to send packet.ItemStackRequest without using ResourcesControlCenter")
	}
	// if key is not exist
	get, normal := value.(singleItemStackRequestWithResponse)
	if !normal {
		panic(fmt.Sprintf("updateItemData: Failed to convert value into singleItemStackRequestWithResponse; value = %#v", value))
	}
	// convert data
	for _, val := range resp.ContainerInfo {
		if get.howToChange == nil {
			panic("updateItemData: Attempt to send packet.ItemStackRequest without using ResourcesControlCenter")
		}
		_, ok := get.howToChange[ContainerID(val.ContainerID)]
		if !ok {
			panic(fmt.Sprintf("updateItemData: item change result %v not found or not provided(packet.ItemStackRequest related); get.howToChange = %#v; val = %#v", ContainerID(val.ContainerID), get.howToChange, val))
		}
		// check pass
		currentChanges := get.howToChange[ContainerID(val.ContainerID)].ChangeResult
		windowID := get.howToChange[ContainerID(val.ContainerID)].WindowID
		// get currentChanges and windowID
		for _, v := range val.SlotInfo {
			newItem, err := i.GetNewItemData(
				currentChanges[v.Slot],
				v,
			)
			if err != nil {
				panic(fmt.Sprintf("updateItemData: Failed to get new item data; currentChanges[v.Slot] = %#v, v = %#v", currentChanges[v.Slot], v))
			}
			inventory.writeItemStackInfo(windowID, v.Slot, newItem)
		}
		// update item info
	}
	// set item data
	return nil
	// return
}
