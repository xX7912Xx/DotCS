//go:build !is_tweak
// +build !is_tweak

package interfaces

import "dotcs/minecraft/protocol/packet"

type GameInterface interface {
	SendSettingsCommand(string, bool) error                         // 发送有关设置的命令
	SendCommand(string) error                                       // 执行我的世界命令
	SendWSCommand(string) error                                     // 以ws的方式执行我的世界命令
	SendCommandWithResponse(string) (packet.CommandOutput, error)   // 发送的命令返回执行结果
	SendWSCommandWithResponse(string) (packet.CommandOutput, error) // 以ws的方式执行我的世界命令并返回执行结果

	SetBlock([3]int32, string, string) error      // 放置方块
	SetBlockAsync([3]int32, string, string) error // 异步放置方块

	SendChat(string) error // 聊天命令
	Output(string) error   // 输出结果
	Title(string) error    // 标题命令
}
