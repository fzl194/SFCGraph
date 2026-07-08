---
id: UNC@20.15.2@ConfigObject@HSSBPFAULTCODE
type: ConfigObject
name: HSSBPFAULTCODE（HSS BYPASS故障状态码）
nf: UNC
version: 20.15.2
object_name: HSSBPFAULTCODE
object_kind: entity
applicable_nf:
- MME
status: active
---

# HSSBPFAULTCODE（HSS BYPASS故障状态码）

## 说明

**适用网元：MME**

本命令用于添加HSS BYPASS故障状态码配置。当HSS全故障后，系统收到HSS/DRA返回某个特定原因值时，希望用户进入HSS BYPASS状态，可通过此命令配置该原因值为HSS BYPASS原因值。

## 操作本对象的命令

- [ADD HSSBPFAULTCODE](command/UNC/20.15.2/ADD-HSSBPFAULTCODE.md)
- [LST HSSBPFAULTCODE](command/UNC/20.15.2/LST-HSSBPFAULTCODE.md)
- [RMV HSSBPFAULTCODE](command/UNC/20.15.2/RMV-HSSBPFAULTCODE.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除HSS-BYPASS故障状态码(RMV-HSSBPFAULTCODE)_10494885.md`
- 原始手册：`evidence/UNC/20.15.2/增加HSS-BYPASS故障状态码(ADD-HSSBPFAULTCODE)_62774744.md`
- 原始手册：`evidence/UNC/20.15.2/查询HSS-BYPASS故障状态码(LST-HSSBPFAULTCODE)_62934708.md`
