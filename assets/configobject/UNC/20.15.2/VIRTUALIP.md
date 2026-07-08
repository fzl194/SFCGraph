---
id: UNC@20.15.2@ConfigObject@VIRTUALIP
type: ConfigObject
name: VIRTUALIP（浮动IP）
nf: UNC
version: 20.15.2
object_name: VIRTUALIP
object_kind: entity
status: active
---

# VIRTUALIP（浮动IP）

## 说明

![](修改浮动IP (MOD VIRTUALIP)_01259710.assets/notice_3.0-zh-cn_2.png)

该类命令执行之后 **可能会导致OM Portal断链** 、网管断链以及VNFM断链，需使用修改后IP重新登录OM Portal，并重新对接网管以及修改VNFM侧对应网元的IP。该命令若执行不当， **会导致所有业务中断** 。

用于修改登录OM Portal的浮动IP地址。

## 操作本对象的命令

- [LST VIRTUALIP](command/UNC/20.15.2/LST-VIRTUALIP.md)
- [MOD VIRTUALIP](command/UNC/20.15.2/MOD-VIRTUALIP.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改浮动IP-(MOD-VIRTUALIP)_01259710.md`
- 原始手册：`evidence/UNC/20.15.2/查询浮动IP-(LST-VIRTUALIP)_47819609.md`
