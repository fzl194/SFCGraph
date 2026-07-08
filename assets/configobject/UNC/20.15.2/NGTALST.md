---
id: UNC@20.15.2@ConfigObject@NGTALST
type: ConfigObject
name: NGTALST（5G跟踪区列表）
nf: UNC
version: 20.15.2
object_name: NGTALST
object_kind: entity
applicable_nf:
- AMF
status: active
---

# NGTALST（5G跟踪区列表）

## 说明

**适用NF：AMF**

该命令用于增加跟踪区列表。在初始注册或移动性注册更新流程中，如果UE当前驻留的跟踪区已经配置在系统的某个跟踪区列表中，那么AMF将在Registration Accept消息中将该跟踪区列表下发给UE。

## 操作本对象的命令

- [ADD NGTALST](command/UNC/20.15.2/ADD-NGTALST.md)
- [LST NGTALST](command/UNC/20.15.2/LST-NGTALST.md)
- [MOD NGTALST](command/UNC/20.15.2/MOD-NGTALST.md)
- [RMV NGTALST](command/UNC/20.15.2/RMV-NGTALST.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改5G跟踪区列表（MOD-NGTALST）_09652580.md`
- 原始手册：`evidence/UNC/20.15.2/删除5G跟踪区列表（RMV-NGTALST）_09652473.md`
- 原始手册：`evidence/UNC/20.15.2/增加5G跟踪区列表（ADD-NGTALST）_09651355.md`
- 原始手册：`evidence/UNC/20.15.2/查询5G跟踪区列表（LST-NGTALST）_09651772.md`
