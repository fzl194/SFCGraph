---
id: UDG@20.15.2@ConfigObject@LICENSESWITCH
type: ConfigObject
name: LICENSESWITCH（License配置项开关）
nf: UDG
version: 20.15.2
object_name: LICENSESWITCH
object_kind: global_setting
status: active
---

# LICENSESWITCH（License配置项开关）

## 说明

该命令用于设置License项的配置开关。当License文件中含有某功能的许可时，通过此命令可以设置该功能是否开通。

> **说明**
> - 该命令执行后立即生效。
>
> - 当License文件未激活时，无法设置任何License项，激活后只能设置已购买且支持配置开关的License项。
>
> - 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：
>
> > **说明**
> > 此处仅展示前20条初始记录值，您可以通过相关查询命令查看全部记录值。
>
> | LICITEM | SWITCH |
> | --- | --- |
> | LKV2MSCMG02 | ENABLE |
> | LKV2C2AF01 | ENABLE |
> | LKV2C6AF01 | ENABLE |
> | LKV2C9AF01 | ENABLE |
> | LKV2C11AF01 | ENABLE |
> | LKV2E2ETRACE02 | ENABLE |
> | LKV2BFD02 | ENABLE |
> | LKV2C15AF01 | ENABLE |
> | LKV2PPTF01 | ENABLE |
> | LKV2V6IF01 | ENABLE |
> | LKV3W9CAT411 | ENABLE |
> | LKV3W9CAT611 | ENABLE |
> | LKV3W9CT9A11 | ENABLE |
> | LKV3W9CTBC11 | DISABLE |
> | LKV3W9CA1611 | ENABLE |
> | LKV2C17AF01 | ENABLE |
> | LKV2C19AF01 | ENABLE |
> | LKV2NFBAM01 | ENABLE |
> | LKV2NFBSM01 | ENABLE |
> | LKV2NFAAM01 | ENABLE |

## 操作本对象的命令

- [[command/UDG/20.15.2/LST-LICENSESWITCH]] · LST LICENSESWITCH
- [[command/UDG/20.15.2/SET-LICENSESWITCH]] · SET LICENSESWITCH

## 证据

- 原始手册：`evidence/UDG/20.15.2/LICENSESWITCH.md`
- 原始手册：`evidence/UDG/20.15.2/LICENSESWITCH.md`
