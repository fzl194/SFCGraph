---
id: UDG@20.15.2@ConfigObject@DHCP6CLIENT
type: ConfigObject
name: DHCP6CLIENT（DHCPv6客户端）
nf: UDG
version: 20.15.2
object_name: DHCP6CLIENT
object_kind: entity
status: active
---

# DHCP6CLIENT（DHCPv6客户端）

## 说明

该命令用于添加DHCPv6客户端。设备作为DHCPv6客户端，在接口上配置该命令后，设备将通过DHCPv6有状态方式从DHCPv6服务器自动获取IPv6地址。接口上使能DHCPv6客户端，需保证接口上有link-local地址，否则无法正常申请到地址。

## 操作本对象的命令

- [[command/UDG/20.15.2/ADD-DHCP6CLIENT]] · ADD DHCP6CLIENT
- [[command/UDG/20.15.2/LST-DHCP6CLIENT]] · LST DHCP6CLIENT
- [[command/UDG/20.15.2/MOD-DHCP6CLIENT]] · MOD DHCP6CLIENT
- [[command/UDG/20.15.2/RMV-DHCP6CLIENT]] · RMV DHCP6CLIENT

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改DHCPv6客户端（MOD-DHCP6CLIENT）_00865673.md`
- 原始手册：`evidence/UDG/20.15.2/删除DHCPv6客户端（RMV-DHCP6CLIENT）_50281534.md`
- 原始手册：`evidence/UDG/20.15.2/增加DHCPv6客户端（ADD-DHCP6CLIENT）_50120726.md`
- 原始手册：`evidence/UDG/20.15.2/查询DHCPv6客户端配置（LST-DHCP6CLIENT）_00866313.md`
