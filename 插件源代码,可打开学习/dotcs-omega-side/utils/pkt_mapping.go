package utils

import "dotcs/minecraft/protocol/packet"

var PktIDMapping map[string]int
var PktIDInvMapping map[int]string
var PktIDNames []string

func init() {
	PktIDMapping = map[string]int{
		"IDLogin":                             packet.IDLogin,
		"IDPlayStatus":                        packet.IDPlayStatus,
		"IDServerToClientHandshake":           packet.IDServerToClientHandshake,
		"IDClientToServerHandshake":           packet.IDClientToServerHandshake,
		"IDDisconnect":                        packet.IDDisconnect,
		"IDResourcePacksInfo":                 packet.IDResourcePacksInfo,
		"IDResourcePackStack":                 packet.IDResourcePackStack,
		"IDResourcePackClientResponse":        packet.IDResourcePackClientResponse,
		"IDText":                              packet.IDText,
		"IDSetTime":                           packet.IDSetTime,
		"IDStartGame":                         packet.IDStartGame,
		"IDAddPlayer":                         packet.IDAddPlayer,
		"IDAddActor":                          packet.IDAddActor,
		"IDRemoveActor":                       packet.IDRemoveActor,
		"IDAddItemActor":                      packet.IDAddItemActor,
		"IDTakeItemActor":                     packet.IDTakeItemActor,
		"IDMoveActorAbsolute":                 packet.IDMoveActorAbsolute,
		"IDMovePlayer":                        packet.IDMovePlayer,
		"IDPassengerJump":                     packet.IDPassengerJump,
		"IDUpdateBlock":                       packet.IDUpdateBlock,
		"IDAddPainting":                       packet.IDAddPainting,
		"IDTickSync":                          packet.IDTickSync,
		"IDLevelEvent":                        packet.IDLevelEvent,
		"IDBlockEvent":                        packet.IDBlockEvent,
		"IDActorEvent":                        packet.IDActorEvent,
		"IDMobEffect":                         packet.IDMobEffect,
		"IDUpdateAttributes":                  packet.IDUpdateAttributes,
		"IDInventoryTransaction":              packet.IDInventoryTransaction,
		"IDMobEquipment":                      packet.IDMobEquipment,
		"IDMobArmourEquipment":                packet.IDMobArmourEquipment,
		"IDInteract":                          packet.IDInteract,
		"IDBlockPickRequest":                  packet.IDBlockPickRequest,
		"IDActorPickRequest":                  packet.IDActorPickRequest,
		"IDPlayerAction":                      packet.IDPlayerAction,
		"IDHurtArmour":                        packet.IDHurtArmour,
		"IDSetActorData":                      packet.IDSetActorData,
		"IDSetActorMotion":                    packet.IDSetActorMotion,
		"IDSetActorLink":                      packet.IDSetActorLink,
		"IDSetHealth":                         packet.IDSetHealth,
		"IDSetSpawnPosition":                  packet.IDSetSpawnPosition,
		"IDAnimate":                           packet.IDAnimate,
		"IDRespawn":                           packet.IDRespawn,
		"IDContainerOpen":                     packet.IDContainerOpen,
		"IDContainerClose":                    packet.IDContainerClose,
		"IDPlayerHotBar":                      packet.IDPlayerHotBar,
		"IDInventoryContent":                  packet.IDInventoryContent,
		"IDInventorySlot":                     packet.IDInventorySlot,
		"IDContainerSetData":                  packet.IDContainerSetData,
		"IDCraftingData":                      packet.IDCraftingData,
		"IDCraftingEvent":                     packet.IDCraftingEvent,
		"IDGUIDataPickItem":                   packet.IDGUIDataPickItem,
		"IDAdventureSettings":                 packet.IDAdventureSettings,
		"IDBlockActorData":                    packet.IDBlockActorData,
		"IDPlayerInput":                       packet.IDPlayerInput,
		"IDLevelChunk":                        packet.IDLevelChunk,
		"IDSetCommandsEnabled":                packet.IDSetCommandsEnabled,
		"IDSetDifficulty":                     packet.IDSetDifficulty,
		"IDChangeDimension":                   packet.IDChangeDimension,
		"IDSetPlayerGameType":                 packet.IDSetPlayerGameType,
		"IDPlayerList":                        packet.IDPlayerList,
		"IDSimpleEvent":                       packet.IDSimpleEvent,
		"IDEvent":                             packet.IDEvent,
		"IDSpawnExperienceOrb":                packet.IDSpawnExperienceOrb,
		"IDClientBoundMapItemData":            packet.IDClientBoundMapItemData,
		"IDMapInfoRequest":                    packet.IDMapInfoRequest,
		"IDRequestChunkRadius":                packet.IDRequestChunkRadius,
		"IDChunkRadiusUpdated":                packet.IDChunkRadiusUpdated,
		"IDItemFrameDropItem":                 packet.IDItemFrameDropItem,
		"IDGameRulesChanged":                  packet.IDGameRulesChanged,
		"IDCamera":                            packet.IDCamera,
		"IDBossEvent":                         packet.IDBossEvent,
		"IDShowCredits":                       packet.IDShowCredits,
		"IDAvailableCommands":                 packet.IDAvailableCommands,
		"IDCommandRequest":                    packet.IDCommandRequest,
		"IDCommandBlockUpdate":                packet.IDCommandBlockUpdate,
		"IDCommandOutput":                     packet.IDCommandOutput,
		"IDUpdateTrade":                       packet.IDUpdateTrade,
		"IDUpdateEquip":                       packet.IDUpdateEquip,
		"IDResourcePackDataInfo":              packet.IDResourcePackDataInfo,
		"IDResourcePackChunkData":             packet.IDResourcePackChunkData,
		"IDResourcePackChunkRequest":          packet.IDResourcePackChunkRequest,
		"IDTransfer":                          packet.IDTransfer,
		"IDPlaySound":                         packet.IDPlaySound,
		"IDStopSound":                         packet.IDStopSound,
		"IDSetTitle":                          packet.IDSetTitle,
		"IDAddBehaviourTree":                  packet.IDAddBehaviourTree,
		"IDStructureBlockUpdate":              packet.IDStructureBlockUpdate,
		"IDShowStoreOffer":                    packet.IDShowStoreOffer,
		"IDPurchaseReceipt":                   packet.IDPurchaseReceipt,
		"IDPlayerSkin":                        packet.IDPlayerSkin,
		"IDSubClientLogin":                    packet.IDSubClientLogin,
		"IDAutomationClientConnect":           packet.IDAutomationClientConnect,
		"IDSetLastHurtBy":                     packet.IDSetLastHurtBy,
		"IDBookEdit":                          packet.IDBookEdit,
		"IDNPCRequest":                        packet.IDNPCRequest,
		"IDPhotoTransfer":                     packet.IDPhotoTransfer,
		"IDModalFormRequest":                  packet.IDModalFormRequest,
		"IDModalFormResponse":                 packet.IDModalFormResponse,
		"IDServerSettingsRequest":             packet.IDServerSettingsRequest,
		"IDServerSettingsResponse":            packet.IDServerSettingsResponse,
		"IDShowProfile":                       packet.IDShowProfile,
		"IDSetDefaultGameType":                packet.IDSetDefaultGameType,
		"IDRemoveObjective":                   packet.IDRemoveObjective,
		"IDSetDisplayObjective":               packet.IDSetDisplayObjective,
		"IDSetScore":                          packet.IDSetScore,
		"IDLabTable":                          packet.IDLabTable,
		"IDUpdateBlockSynced":                 packet.IDUpdateBlockSynced,
		"IDMoveActorDelta":                    packet.IDMoveActorDelta,
		"IDSetScoreboardIdentity":             packet.IDSetScoreboardIdentity,
		"IDSetLocalPlayerAsInitialised":       packet.IDSetLocalPlayerAsInitialised,
		"IDUpdateSoftEnum":                    packet.IDUpdateSoftEnum,
		"IDNetworkStackLatency":               packet.IDNetworkStackLatency,
		"IDScriptCustomEvent":                 packet.IDScriptCustomEvent,
		"IDSpawnParticleEffect":               packet.IDSpawnParticleEffect,
		"IDAvailableActorIdentifiers":         packet.IDAvailableActorIdentifiers,
		"IDNetworkChunkPublisherUpdate":       packet.IDNetworkChunkPublisherUpdate,
		"IDBiomeDefinitionList":               packet.IDBiomeDefinitionList,
		"IDLevelSoundEvent":                   packet.IDLevelSoundEvent,
		"IDLevelEventGeneric":                 packet.IDLevelEventGeneric,
		"IDLecternUpdate":                     packet.IDLecternUpdate,
		"IDAddEntity":                         packet.IDAddEntity,
		"IDRemoveEntity":                      packet.IDRemoveEntity,
		"IDClientCacheStatus":                 packet.IDClientCacheStatus,
		"IDOnScreenTextureAnimation":          packet.IDOnScreenTextureAnimation,
		"IDMapCreateLockedCopy":               packet.IDMapCreateLockedCopy,
		"IDStructureTemplateDataRequest":      packet.IDStructureTemplateDataRequest,
		"IDStructureTemplateDataResponse":     packet.IDStructureTemplateDataResponse,
		"IDClientCacheBlobStatus":             packet.IDClientCacheBlobStatus,
		"IDClientCacheMissResponse":           packet.IDClientCacheMissResponse,
		"IDEducationSettings":                 packet.IDEducationSettings,
		"IDEmote":                             packet.IDEmote,
		"IDMultiPlayerSettings":               packet.IDMultiPlayerSettings,
		"IDSettingsCommand":                   packet.IDSettingsCommand,
		"IDAnvilDamage":                       packet.IDAnvilDamage,
		"IDCompletedUsingItem":                packet.IDCompletedUsingItem,
		"IDNetworkSettings":                   packet.IDNetworkSettings,
		"IDPlayerAuthInput":                   packet.IDPlayerAuthInput,
		"IDCreativeContent":                   packet.IDCreativeContent,
		"IDPlayerEnchantOptions":              packet.IDPlayerEnchantOptions,
		"IDItemStackRequest":                  packet.IDItemStackRequest,
		"IDItemStackResponse":                 packet.IDItemStackResponse,
		"IDPlayerArmourDamage":                packet.IDPlayerArmourDamage,
		"IDCodeBuilder":                       packet.IDCodeBuilder,
		"IDUpdatePlayerGameType":              packet.IDUpdatePlayerGameType,
		"IDEmoteList":                         packet.IDEmoteList,
		"IDPositionTrackingDBServerBroadcast": packet.IDPositionTrackingDBServerBroadcast,
		"IDPositionTrackingDBClientRequest":   packet.IDPositionTrackingDBClientRequest,
		"IDDebugInfo":                         packet.IDDebugInfo,
		"IDPacketViolationWarning":            packet.IDPacketViolationWarning,
		"IDMotionPredictionHints":             packet.IDMotionPredictionHints,
		"IDAnimateEntity":                     packet.IDAnimateEntity,
		"IDCameraShake":                       packet.IDCameraShake,
		"IDPlayerFog":                         packet.IDPlayerFog,
		"IDCorrectPlayerMovePrediction":       packet.IDCorrectPlayerMovePrediction,
		"IDItemComponent":                     packet.IDItemComponent,
		"IDFilterText":                        packet.IDFilterText,
		"IDClientBoundDebugRenderer":          packet.IDClientBoundDebugRenderer,
		"IDSyncActorProperty":                 packet.IDSyncActorProperty,
		"IDAddVolumeEntity":                   packet.IDAddVolumeEntity,
		"IDRemoveVolumeEntity":                packet.IDRemoveVolumeEntity,
		"IDSimulationType":                    packet.IDSimulationType,
		"IDNPCDialogue":                       packet.IDNPCDialogue,
		"IDEducationResourceURI":              packet.IDEducationResourceURI,
		"IDCreatePhoto":                       packet.IDCreatePhoto,
		"IDUpdateSubChunkBlocks":              packet.IDUpdateSubChunkBlocks,
		"IDPhotoInfoRequest":                  packet.IDPhotoInfoRequest,
		"IDSubChunk":                          packet.IDSubChunk,
		"IDSubChunkRequest":                   packet.IDSubChunkRequest,
		"IDClientStartItemCooldown":           packet.IDClientStartItemCooldown,
		"IDScriptMessage":                     packet.IDScriptMessage,
		"IDCodeBuilderSource":                 packet.IDCodeBuilderSource,
	}
	PktIDInvMapping = make(map[int]string)
	PktIDNames = make([]string, 0)
	for k, v := range PktIDMapping {
		PktIDInvMapping[v] = k
		PktIDNames = append(PktIDNames, k)
	}

}
