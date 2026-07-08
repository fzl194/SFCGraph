---
id: UNC@20.15.2@ConfigObject@QOSRDRVPN
type: ConfigObject
name: QOSRDRVPN（QoS重定向VPN）
nf: UNC
version: 20.15.2
object_name: QOSRDRVPN
object_kind: entity
status: active
---

# QOSRDRVPN（QoS重定向VPN）

## 说明

该命令用于配置非本地报文重定向到指定VPN。用户不需要配置复杂流分类，只需要将接口上收到的所有非本地的单播报文全部重定向到指定的VPN，在该VPN内再查路由表项进行转发。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-QOSRDRVPN]] · ADD QOSRDRVPN
- [[command/UNC/20.15.2/LST-QOSRDRVPN]] · LST QOSRDRVPN
- [[command/UNC/20.15.2/MOD-QOSRDRVPN]] · MOD QOSRDRVPN
- [[command/UNC/20.15.2/RMV-QOSRDRVPN]] · RMV QOSRDRVPN

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改QoS重定向VPN（MOD-QOSRDRVPN）_00441377.md`
- 原始手册：`evidence/UNC/20.15.2/删除QoS重定向VPN（RMV-QOSRDRVPN）_00600549.md`
- 原始手册：`evidence/UNC/20.15.2/增加QoS重定向VPN（ADD-QOSRDRVPN）_00441441.md`
- 原始手册：`evidence/UNC/20.15.2/查询QoS重定向VPN（LST-QOSRDRVPN）_49961018.md`
