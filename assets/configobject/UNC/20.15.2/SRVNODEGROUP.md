---
id: UNC@20.15.2@ConfigObject@SRVNODEGROUP
type: ConfigObject
name: SRVNODEGROUP（服务节点组）
nf: UNC
version: 20.15.2
object_name: SRVNODEGROUP
object_kind: entity
applicable_nf:
- PGW-C
- GGSN
status: active
---

# SRVNODEGROUP（服务节点组）

## 说明

**适用NF：PGW-C、GGSN**

该命令用来添加一个新的服务节点组。当需要用SGSN IP、SGW IP、PCF IP进行虚拟APN映射时，在不同的场景下需要使用该命令添加SGSN/SGW/PCF新的服务节点组，可以在该服务节点组下绑定服务节点IP地址。

## 操作本对象的命令

- [ADD SRVNODEGROUP](command/UNC/20.15.2/ADD-SRVNODEGROUP.md)
- [LST SRVNODEGROUP](command/UNC/20.15.2/LST-SRVNODEGROUP.md)
- [RMV SRVNODEGROUP](command/UNC/20.15.2/RMV-SRVNODEGROUP.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除服务节点组（RMV-SRVNODEGROUP）_09653063.md`
- 原始手册：`evidence/UNC/20.15.2/增加服务节点组（ADD-SRVNODEGROUP）_09651376.md`
- 原始手册：`evidence/UNC/20.15.2/查询服务节点组（LST-SRVNODEGROUP）_09651531.md`
