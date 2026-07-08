---
id: UDG@20.15.2@ConfigObject@PODCPUTHD
type: ConfigObject
name: PODCPUTHD（POD CPU阈值）
nf: UDG
version: 20.15.2
object_name: PODCPUTHD
object_kind: global_setting
status: active
---

# PODCPUTHD（POD CPU阈值）

## 说明

该命令用于设置POD CPU告警阈值。

> **说明**
> - 该命令执行后立即生效。
>
> - 该命令仅在FusionStage裸机场景下生效。
> - 当某种POD类型通过[**ADD PODALMTH**](增加POD资源告警阈值（ADD PODALMTH）_87483778.md)命令或模板配置过CPU类型阈值时，本命令配置的全局阈值对其不生效。
>
> - 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：
>
> | WARNTHD | RECVTHD |
> | --- | --- |
> | 80 | 70 |

## 操作本对象的命令

- [LST PODCPUTHD](command/UDG/20.15.2/LST-PODCPUTHD.md)
- [SET PODCPUTHD](command/UDG/20.15.2/SET-PODCPUTHD.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询POD-CPU阈值（LST-PODCPUTHD）_92620570.md`
- 原始手册：`evidence/UDG/20.15.2/设置POD-CPU告警阈值（SET-PODCPUTHD）_37900461.md`
