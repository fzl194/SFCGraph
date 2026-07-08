---
id: UDG@20.15.2@ConfigObject@MASALMRPTMODE
type: ConfigObject
name: MASALMRPTMODE（5G告警上报模式）
nf: UDG
version: 20.15.2
object_name: MASALMRPTMODE
object_kind: global_setting
status: active
---

# MASALMRPTMODE（5G告警上报模式）

## 说明

该命令用于设置5G告警的上报模式。如果系统内某一个告警大量产生时，会对系统的性能和告警台产生冲击，此时可以根据实际的需求，配置告警的上报模式，可以有效降低大量告警对系统的影响。

> **说明**
> - 该命令执行后立即生效。
>
> - 批量告警上报开关从开启到关闭属于高危操作，请操作人员谨慎处理。如果单条告警数量过多，可能导致单条告警被丢弃。
>
> - 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：
>
> | ALMTYPE | BATCHEDALMSW | PERIOD | THRESHOLD | CLEARTHRESHOLD |
> | --- | --- | --- | --- | --- |
> | HTTP_LINKDOWN | ON | 60 | 100 | 10 |

## 操作本对象的命令

- [[command/UDG/20.15.2/LST-MASALMRPTMODE]] · LST MASALMRPTMODE
- [[command/UDG/20.15.2/SET-MASALMRPTMODE]] · SET MASALMRPTMODE

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询5G告警上报模式（LST-MASALMRPTMODE）_80432530.md`
- 原始手册：`evidence/UDG/20.15.2/设置5G告警上报模式（SET-MASALMRPTMODE）_26150765.md`
