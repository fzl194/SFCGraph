---
id: UNC@20.15.2@ConfigObject@PEERPLMN
type: ConfigObject
name: PEERPLMN（对等PLMN配置）
nf: UNC
version: 20.15.2
object_name: PEERPLMN
object_kind: entity
applicable_nf:
- SGSN
- MME
status: active
---

# PEERPLMN（对等PLMN配置）

## 说明

**适用网元：SGSN、MME**

此命令用于增加一条对等PLMN配置记录。对等PLMN是指向UE提供和本网相同服务的PLMN，以便UE选择不同的PLMN网络。在Attach Accept或者TAU Accept消息中携带给UE，由UE保存。当UE发生PLMN重选时，优先从这个列表中选择。

## 操作本对象的命令

- [ADD PEERPLMN](command/UNC/20.15.2/ADD-PEERPLMN.md)
- [LST PEERPLMN](command/UNC/20.15.2/LST-PEERPLMN.md)
- [RMV PEERPLMN](command/UNC/20.15.2/RMV-PEERPLMN.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除对等PLMN配置(RMV-PEERPLMN)_72345697.md`
- 原始手册：`evidence/UNC/20.15.2/增加对等PLMN配置(ADD-PEERPLMN)_26305906.md`
- 原始手册：`evidence/UNC/20.15.2/查询对等PLMN配置(LST-PEERPLMN)_26146098.md`
