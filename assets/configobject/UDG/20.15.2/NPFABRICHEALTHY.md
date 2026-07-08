---
id: UDG@20.15.2@ConfigObject@NPFABRICHEALTHY
type: ConfigObject
name: NPFABRICHEALTHY（全局亚健康相关配置）
nf: UDG
version: 20.15.2
object_name: NPFABRICHEALTHY
object_kind: global_setting
status: active
---

# NPFABRICHEALTHY（全局亚健康相关配置）

## 说明

该命令用来设置全局亚健康相关配置：包括亚健康阈值和亚健康检测周期。

> **说明**
> - 该命令执行后立即生效。
>
> - 如果修改阈值，需要注意：阈值过小，链路切换敏感，选路频繁变化，在网络负荷很大的场景下，频繁切换会导致网络传输质量下降。
> - 该命令仅适用于NP卡加速模式场景。
>
> - 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：
>
> | THRESHOLD | INTERVAL |
> | --- | --- |
> | 50 | 100 |

## 操作本对象的命令

- [[command/UDG/20.15.2/LST-NPFABRICHEALTHY]] · LST NPFABRICHEALTHY
- [[command/UDG/20.15.2/SET-NPFABRICHEALTHY]] · SET NPFABRICHEALTHY

## 证据

- 原始手册：`evidence/UDG/20.15.2/NPFABRICHEALTHY.md`
- 原始手册：`evidence/UDG/20.15.2/NPFABRICHEALTHY.md`
