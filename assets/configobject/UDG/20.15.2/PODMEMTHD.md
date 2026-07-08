---
id: UDG@20.15.2@ConfigObject@PODMEMTHD
type: ConfigObject
name: PODMEMTHD（POD内存阈值）
nf: UDG
version: 20.15.2
object_name: PODMEMTHD
object_kind: global_setting
status: active
---

# PODMEMTHD（POD内存阈值）

## 说明

该命令用于设置POD内存告警阈值。

> **说明**
> - 该命令执行后立即生效。
>
> - 该命令仅在FusionStage裸机场景下生效。
> - 当某种POD类型通过[**ADD PODALMTH**](增加POD资源告警阈值（ADD PODALMTH）_87483778.md)命令或模板配置过内存类型阈值时，本命令配置的全局阈值对其不生效。
>
> - 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：
>
> | WARNTHD | RECVTHD |
> | --- | --- |
> | 95 | 90 |

## 操作本对象的命令

- [[command/UDG/20.15.2/LST-PODMEMTHD]] · LST PODMEMTHD
- [[command/UDG/20.15.2/SET-PODMEMTHD]] · SET PODMEMTHD

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询POD内存阈值（LST-PODMEMTHD）_92780526.md`
- 原始手册：`evidence/UDG/20.15.2/设置POD内存告警阈值（SET-PODMEMTHD）_37740493.md`
