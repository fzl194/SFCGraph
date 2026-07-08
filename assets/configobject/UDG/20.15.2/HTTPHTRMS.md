---
id: UDG@20.15.2@ConfigObject@HTTPHTRMS
type: ConfigObject
name: HTTPHTRMS（HTR流控安全边界配置）
nf: UDG
version: 20.15.2
object_name: HTTPHTRMS
object_kind: entity
status: active
---

# HTTPHTRMS（HTR流控安全边界配置）

## 说明

该命令用于增加HTR流控安全边界配置。

> **说明**
> - 该命令执行后立即生效。
>
> - 已经处于HTR过载状态的局向仍按照修改前安全边界值生效，解控后重新起控按照新增的安全边界值生效。
>
> - 最多可输入64条记录。
>
> - 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：
>
> | LOCALNFTYPE | PEERNFTYPE | MINTHD | MAXTHD |
> | --- | --- | --- | --- |
> | NFTypeAMF | NFTypeAUSF | 210 | 1500 |
> | NFTypeAMF | NFTypeUDM | 210 | 1500 |
> | NFTypeSMF | NFTypeUDM | 160 | 1200 |
> | NFTypeSMF | NFTypePCF | 160 | 1200 |
> | NFTypeCHF | NFTypeCUSTOM_OCS | 1000 | 3000 |

## 操作本对象的命令

- [ADD HTTPHTRMS](command/UDG/20.15.2/ADD-HTTPHTRMS.md)
- [LST HTTPHTRMS](command/UDG/20.15.2/LST-HTTPHTRMS.md)
- [MOD HTTPHTRMS](command/UDG/20.15.2/MOD-HTTPHTRMS.md)
- [RMV HTTPHTRMS](command/UDG/20.15.2/RMV-HTTPHTRMS.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改HTR流控安全边界配置（MOD-HTTPHTRMS）_35230486.md`
- 原始手册：`evidence/UDG/20.15.2/删除HTR流控安全边界配置（RMV-HTTPHTRMS）_86255393.md`
- 原始手册：`evidence/UDG/20.15.2/增加HTR流控安全边界配置（ADD-HTTPHTRMS）_85910089.md`
- 原始手册：`evidence/UDG/20.15.2/查询HTR流控安全边界配置（LST-HTTPHTRMS）_35070998.md`
