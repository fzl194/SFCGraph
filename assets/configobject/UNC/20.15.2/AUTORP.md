---
id: UNC@20.15.2@ConfigObject@AUTORP
type: ConfigObject
name: AUTORP（Auto-RP配置）
nf: UNC
version: 20.15.2
object_name: AUTORP
object_kind: entity
status: active
---

# AUTORP（Auto-RP配置）

## 说明

该命令用于添加Auto-RP的配置。

当路由器与支持Auto-RP的设备互通时，需要配置此命令来使能Auto-RP侦听功能，即接收Auto-RP宣告和发现报文，并从发现报文中学习RP信息。

路由器在接收到Auto-RP宣告报文或发现报文之后，解析报文的源地址，根据源地址进行RPF检查。

如果RPF检查失败，则路由器丢弃该报文；如果RPF检查通过，则路由器向其他PIM邻居转发该报文。

## 操作本对象的命令

- [ADD AUTORP](command/UNC/20.15.2/ADD-AUTORP.md)
- [LST AUTORP](command/UNC/20.15.2/LST-AUTORP.md)
- [RMV AUTORP](command/UNC/20.15.2/RMV-AUTORP.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除Auto-RP配置（RMV-AUTORP）_49961958.md`
- 原始手册：`evidence/UNC/20.15.2/查询Auto-RP配置（LST-AUTORP）_00866725.md`
- 原始手册：`evidence/UNC/20.15.2/添加Auto-RP配置（ADD-AUTORP）_49961218.md`
