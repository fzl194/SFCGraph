---
id: UDG@20.15.2@ConfigObject@IFIPV6ENABLEIPSEC
type: ConfigObject
name: IFIPV6ENABLEIPSEC（接口IPv6使能）
nf: UDG
version: 20.15.2
object_name: IFIPV6ENABLEIPSEC
object_kind: global_setting
status: active
---

# IFIPV6ENABLEIPSEC（接口IPv6使能）

## 说明

该命令用于修改接口的IPv6使能情况，用户可通过该命令修改接口的IPv6 MTU和Autolinklocal标志。

> **说明**
> - 该命令执行后立即生效。
>
> - 该命令在VNRS_VNFC上的Ethernet接口，Ethernet子接口，Eth-Trunk接口，Eth-Trunk子接口以及Loopback口，Tunnel口上配置执行。
> - 缺省情况下，接口上不使能IPv6。
> - 若IPv4 MTU与IPv6 MTU都配置的时候，实际取两者之间的较大值配置至vNic。

## 操作本对象的命令

- [[command/UDG/20.15.2/LST-IFIPV6ENABLEIPSEC]] · LST IFIPV6ENABLEIPSEC
- [[command/UDG/20.15.2/SET-IFIPV6ENABLEIPSEC]] · SET IFIPV6ENABLEIPSEC

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询接口IPv6使能（LST-IFIPV6ENABLEIPSEC）_68320999.md`
- 原始手册：`evidence/UDG/20.15.2/设置接口IPv6使能（SET-IFIPV6ENABLEIPSEC）_68201005.md`
