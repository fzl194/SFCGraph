---
id: UNC@20.15.2@ConfigObject@DCNMEMBER
type: ConfigObject
name: DCNMEMBER（DCN成员）
nf: UNC
version: 20.15.2
object_name: DCNMEMBER
object_kind: entity
applicable_nf:
- MME
status: active
---

# DCNMEMBER（DCN成员）

## 说明

**适用网元：MME**

当运营商部署DCN时，此命令用于配置DCN所覆盖MME的网络范围。当专用核心网重选时，可通过该配置找到指定DCN下的MME组。执行此命令前需要通过 [**ADD DCN**](../DCN配置/增加DCN(ADD DCN)_72225505.md) 增加专用核心网。

## 操作本对象的命令

- [ADD DCNMEMBER](command/UNC/20.15.2/ADD-DCNMEMBER.md)
- [LST DCNMEMBER](command/UNC/20.15.2/LST-DCNMEMBER.md)
- [RMV DCNMEMBER](command/UNC/20.15.2/RMV-DCNMEMBER.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除DCN成员(RMV-DCNMEMBER)_72345431.md`
- 原始手册：`evidence/UNC/20.15.2/增加DCN成员(ADD-DCNMEMBER)_26305640.md`
- 原始手册：`evidence/UNC/20.15.2/查询DCN成员(LST-DCNMEMBER)_26145832.md`
