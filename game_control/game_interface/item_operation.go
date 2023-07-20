package GameInterface

import (
	ResourcesControl "dotcs/game_control/resources_control"
	"dotcs/minecraft/protocol"
	"dotcs/minecraft/protocol/packet"
	"fmt"
)

// 描述单个物品所在的位置
type ItemLocation struct {
	WindowID    int16 // 物品所在库存的窗口 ID
	ContainerID uint8 // 物品所在库存的库存类型 ID
	Slot        uint8 // 物品所在的槽位
}

// 将库存编号为 source 所指代的物品移动到 destination 所指代的槽位
// 且只移动 moveCount 个物品。
// details 指代相应槽位的预期变动结果，它将作为更新本地库存数据的依据。
// 当且仅当物品操作得到租赁服的响应后，此函数才会返回物品操作结果。
func (g *GameInterface) MoveItem(
	source ItemLocation,
	destination ItemLocation,
	details ItemChangingDetails,
	moveCount uint8,
) ([]protocol.ItemStackResponse, error) {
	placeStackRequestAction := protocol.PlaceStackRequestAction{}
	// 初始化
	itemOnSource, err := g.Resources.Inventory.GetItemStackInfo(uint32(source.WindowID), source.Slot)
	if err != nil {
		return []protocol.ItemStackResponse{}, fmt.Errorf("MoveItem: %v", err)
	}
	itemOnDestination, _ := g.Resources.Inventory.GetItemStackInfo(uint32(destination.WindowID), destination.Slot)
	// 取得 source 和 destination 处的物品信息
	if moveCount <= uint8(itemOnSource.Stack.Count) || source.WindowID == -1 {
		placeStackRequestAction.Count = moveCount
	} else {
		placeStackRequestAction.Count = uint8(itemOnSource.Stack.Count)
	}
	// 得到欲移动的物品数量
	placeStackRequestAction.Source = protocol.StackRequestSlotInfo{
		ContainerID:    source.ContainerID,
		Slot:           source.Slot,
		StackNetworkID: itemOnSource.StackNetworkID,
	}
	placeStackRequestAction.Destination = protocol.StackRequestSlotInfo{
		ContainerID:    destination.ContainerID,
		Slot:           destination.Slot,
		StackNetworkID: itemOnDestination.StackNetworkID,
	}
	// 构造 placeStackRequestAction 结构体
	ans, err := g.SendItemStackRequestWithResponse(
		&packet.ItemStackRequest{
			Requests: []protocol.ItemStackRequest{
				{
					Actions: []protocol.StackRequestAction{
						&placeStackRequestAction,
					},
				},
			},
		},
		[]ItemChangingDetails{details},
	)
	if err != nil {
		return []protocol.ItemStackResponse{}, fmt.Errorf("MoveItem: %v", err)
	}
	// 发送物品操作请求
	return ans, nil
	// 返回值
}

// 将 source 所指代的槽位中的全部物品丢出。
// windowID 指代被丢出物品所在库存的窗口 ID 。
// 返回值第一项代表丢出结果，
// 为真时代表成功丢出，否则反之
func (g *GameInterface) DropItemAll(
	source protocol.StackRequestSlotInfo,
	windowID uint32,
) (bool, error) {
	ans, err := g.SendItemStackRequestWithResponse(
		&packet.ItemStackRequest{
			Requests: []protocol.ItemStackRequest{
				{
					Actions: []protocol.StackRequestAction{
						&protocol.DropStackRequestAction{
							Count:    64,
							Source:   source,
							Randomly: false,
						},
					},
				},
			},
		},
		[]ItemChangingDetails{
			{
				map[ResourcesControl.ContainerID]ResourcesControl.StackRequestContainerInfo{
					ResourcesControl.ContainerID(source.ContainerID): {
						WindowID: windowID,
						ChangeResult: map[uint8]protocol.ItemInstance{
							source.Slot: AirItem,
						},
					},
				},
			},
		},
	)
	if err != nil {
		return false, fmt.Errorf("DropItemAll: %v", err)
	}
	if ans[0].Status != protocol.ItemStackResponseStatusOK {
		return false, nil
	}
	// 发送物品丢掷请求
	return true, nil
	// 返回值
}
