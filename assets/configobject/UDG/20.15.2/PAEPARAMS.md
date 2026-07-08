---
id: UDG@20.15.2@ConfigObject@PAEPARAMS
type: ConfigObject
name: PAEPARAMS（PAE参数）
nf: UDG
version: 20.15.2
object_name: PAEPARAMS
object_kind: global_setting
status: active
---

# PAEPARAMS（PAE参数）

## 说明

![](设置PAE参数（SET PAEPARAMS）_05415160.assets/notice_3.0-zh-cn.png)

该命令是高危命令，操作不当可能会导致业务受损，请谨慎使用并联系华为技术支持协助操作。

该命令用于设置PAE服务的相关参数。PAE主要功能是为微服务通信提供报文高速转发及适配。

> **说明**
> - 该命令执行后立即生效。
>
> - 参数"PARAVALUE2"仅作为保留域，暂未启用。
>
> - 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：
>
> | PARAID | PARAVALUE1 | PARAVALUE2 |
> | --- | --- | --- |
> | 0 | 1 | - |
> | 1 | 1 | - |
> | 2 | 1 | - |

## 操作本对象的命令

- [LST PAEPARAMS](command/UDG/20.15.2/LST-PAEPARAMS.md)
- [SET PAEPARAMS](command/UDG/20.15.2/SET-PAEPARAMS.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询PAE参数（LST-PAEPARAMS）_52213925.md`
- 原始手册：`evidence/UDG/20.15.2/设置PAE参数（SET-PAEPARAMS）_05415160.md`
