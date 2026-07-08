---
id: UDG@20.15.2@ConfigObject@SQOSRDRVPNGROUP
type: ConfigObject
name: SQOSRDRVPNGROUP（QoS重定向VPN组）
nf: UDG
version: 20.15.2
object_name: SQOSRDRVPNGROUP
object_kind: entity
status: active
---

# SQOSRDRVPNGROUP（QoS重定向VPN组）

## 说明

该命令用来配置重定向VPN。通过流策略将该动作应用于具体接口，对匹配类的流量进行重定向。在网络部署中，如果用户希望一部分流量不按照报文的正常路由路径转发而是由用户来指定这部分流量的转发VPN，这种情况下需要部署重定向特性。

## 操作本对象的命令

- [ADD SQOSRDRVPNGROUP](command/UDG/20.15.2/ADD-SQOSRDRVPNGROUP.md)
- [LST SQOSRDRVPNGROUP](command/UDG/20.15.2/LST-SQOSRDRVPNGROUP.md)
- [RMV SQOSRDRVPNGROUP](command/UDG/20.15.2/RMV-SQOSRDRVPNGROUP.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除QoS重定向VPN组（RMV-SQOSRDRVPNGROUP）_00865581.md`
- 原始手册：`evidence/UDG/20.15.2/增加QoS重定向VPN组（ADD-SQOSRDRVPNGROUP）_00441265.md`
- 原始手册：`evidence/UDG/20.15.2/查询QoS重定向VPN组（LST-SQOSRDRVPNGROUP）_00841137.md`
