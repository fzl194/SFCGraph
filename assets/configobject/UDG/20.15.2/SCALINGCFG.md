---
id: UDG@20.15.2@ConfigObject@SCALINGCFG
type: ConfigObject
name: SCALINGCFG（自动扩缩容配置）
nf: UDG
version: 20.15.2
object_name: SCALINGCFG
object_kind: global_setting
status: active
---

# SCALINGCFG（自动扩缩容配置）

## 说明

此命令用于设置扩缩容的各项参数，扩缩容方式、以及扩缩容步长、设置扩缩容阈值上下限，超过阈值上限，进行扩容，低于阈值下限进行缩容。扩缩容触发方式依赖 [**SET SCALINGSWITCH**](设置扩缩容开关（SET SCALINGSWITCH）_09587379.md) 命令。

> **说明**
> - 该命令执行后立即生效。
>
> - 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：
>
> | SCALEOUTTHD | SCALEINTHD | STEPCLASS | SCALINGSTEP |
> | --- | --- | --- | --- |
> | 80 | 20 | Percentage | 50 |

## 操作本对象的命令

- [[command/UDG/20.15.2/LST-SCALINGCFG]] · LST SCALINGCFG
- [[command/UDG/20.15.2/SET-SCALINGCFG]] · SET SCALINGCFG

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询自动扩缩容配置（LST-SCALINGCFG）_09587906.md`
- 原始手册：`evidence/UDG/20.15.2/设置自动扩缩容配置（SET-SCALINGCFG）_09587850.md`
