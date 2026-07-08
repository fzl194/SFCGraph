---
id: UDG@20.15.2@ConfigObject@VIRTUALIP
type: ConfigObject
name: VIRTUALIP（浮动IP）
nf: UDG
version: 20.15.2
object_name: VIRTUALIP
object_kind: entity
status: active
---

# VIRTUALIP（浮动IP）

## 说明

![](修改浮动IP (MOD VIRTUALIP)_01259710.assets/notice_3.0-zh-cn.png)

该类命令执行之后 **可能会导致OM Portal断链** 、网管断链以及VNFM断链，需使用修改后IP重新登录OM Portal，并重新对接网管以及修改VNFM侧对应网元的IP。该命令若执行不当， **会导致所有业务中断** 。

用于修改登录OM Portal的浮动IP地址。

> **说明**
> - IPv4单栈环境下的浮动IP类型不支持修改为IPv6类型，IPv6单栈环境下的浮动IP类型不支持修改为IPv4类型。
> - IPv4或IPv6单栈环境可以通过此命令变更为双栈环境。
> - 修改浮动IP时，需和物理IP保持相同网段。
> - 执行该命令修改浮动IP时，请参考网元的改造OM网络方案改造OM网络。

## 操作本对象的命令

- [[command/UDG/20.15.2/LST-VIRTUALIP]] · LST VIRTUALIP
- [[command/UDG/20.15.2/MOD-VIRTUALIP]] · MOD VIRTUALIP

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改浮动IP-(MOD-VIRTUALIP)_01259710.md`
- 原始手册：`evidence/UDG/20.15.2/查询浮动IP-(LST-VIRTUALIP)_47819609.md`
