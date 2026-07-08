---
id: UNC@20.15.2@ConfigObject@SRVNODEIP
type: ConfigObject
name: SRVNODEIP（服务节点IP）
nf: UNC
version: 20.15.2
object_name: SRVNODEIP
object_kind: entity
applicable_nf:
- PGW-C
- GGSN
status: active
---

# SRVNODEIP（服务节点IP）

## 说明

**适用NF：PGW-C、GGSN**

该命令用来增加一个新的服务节点IP。当需要用SGSN IP、SGW IP、PCF IP进行虚拟APN映射时，在不同的场景下需要使用该命令增加SGSN/SGW/PCF的服务节点组绑定的服务节点IP地址段。

## 操作本对象的命令

- [ADD SRVNODEIP](command/UNC/20.15.2/ADD-SRVNODEIP.md)
- [LST SRVNODEIP](command/UNC/20.15.2/LST-SRVNODEIP.md)
- [RMV SRVNODEIP](command/UNC/20.15.2/RMV-SRVNODEIP.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除服务节点IP（RMV-SRVNODEIP）_09651417.md`
- 原始手册：`evidence/UNC/20.15.2/增加服务节点IP（ADD-SRVNODEIP）_09654166.md`
- 原始手册：`evidence/UNC/20.15.2/查询服务节点IP（LST-SRVNODEIP）_09651392.md`
