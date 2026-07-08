---
id: UDG@20.15.2@ConfigObject@DRSEPINTERFACE
type: ConfigObject
name: DRSEPINTERFACE（故障隔离接口）
nf: UDG
version: 20.15.2
object_name: DRSEPINTERFACE
object_kind: entity
status: active
---

# DRSEPINTERFACE（故障隔离接口）

## 说明

该命令用于在免交换组网下组成热备容灾关系的网元间DCI通道变化时，添加需要关闭/开启的逻辑接口。

> **说明**
> - 该命令执行后立即生效。
>
> - 该命令只用于在UEG-M/UEG网元采用主备（热备）容灾模式下执行。
> - 该命令执行时，请确保配置接口名称正确。如果配置错误，请先执行[**RMV DRSEPINTERFACE**](删除故障隔离接口（RMV DRSEPINTERFACE）_35390226.md)命令，再执行此命令添加正确的接口。
>
> - 最多可输入65535条记录。

## 操作本对象的命令

- [[command/UDG/20.15.2/ADD-DRSEPINTERFACE]] · ADD DRSEPINTERFACE
- [[command/UDG/20.15.2/DSP-DRSEPINTERFACE]] · DSP DRSEPINTERFACE
- [[command/UDG/20.15.2/LST-DRSEPINTERFACE]] · LST DRSEPINTERFACE
- [[command/UDG/20.15.2/RMV-DRSEPINTERFACE]] · RMV DRSEPINTERFACE

## 证据

- 原始手册：`evidence/UDG/20.15.2/DRSEPINTERFACE.md`
- 原始手册：`evidence/UDG/20.15.2/DRSEPINTERFACE.md`
- 原始手册：`evidence/UDG/20.15.2/DRSEPINTERFACE.md`
- 原始手册：`evidence/UDG/20.15.2/DRSEPINTERFACE.md`
