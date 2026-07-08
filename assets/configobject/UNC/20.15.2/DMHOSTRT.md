---
id: UNC@20.15.2@ConfigObject@DMHOSTRT
type: ConfigObject
name: DMHOSTRT（Diameter主机路由）
nf: UNC
version: 20.15.2
object_name: DMHOSTRT
object_kind: entity
applicable_nf:
- SGSN
- MME
status: active
---

# DMHOSTRT（Diameter主机路由）

## 说明

**适用网元：SGSN、MME**

该命令用于新增一条Diameter主机路由。主机路由是指通过请求消息中的destination-host信元来选择对端。

## 操作本对象的命令

- [ADD DMHOSTRT](command/UNC/20.15.2/ADD-DMHOSTRT.md)
- [LST DMHOSTRT](command/UNC/20.15.2/LST-DMHOSTRT.md)
- [MOD DMHOSTRT](command/UNC/20.15.2/MOD-DMHOSTRT.md)
- [RMV DMHOSTRT](command/UNC/20.15.2/RMV-DMHOSTRT.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改Diameter主机路由(MOD-DMHOSTRT)_26306084.md`
- 原始手册：`evidence/UNC/20.15.2/删除Diameter主机路由(RMV-DMHOSTRT)_72225951.md`
- 原始手册：`evidence/UNC/20.15.2/增加Diameter主机路由(ADD-DMHOSTRT)_26146272.md`
- 原始手册：`evidence/UNC/20.15.2/查询Diameter主机路由(LST-DMHOSTRT)_72345873.md`
