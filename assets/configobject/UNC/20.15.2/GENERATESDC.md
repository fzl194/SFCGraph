---
id: UNC@20.15.2@ConfigObject@GENERATESDC
type: ConfigObject
name: GENERATESDC（强制产生业务数据容器）
nf: UNC
version: 20.15.2
object_name: GENERATESDC
object_kind: action
applicable_nf:
- SGW-C
- PGW-C
- SMF
status: active
---

# GENERATESDC（强制产生业务数据容器）

## 说明

**适用NF：SGW-C、PGW-C、SMF**

该命令执行后，满足条件的在线计费用户会立即发送CCR-U消息，满足条件的离线计费用户会立即产生业务数据容器（SDC）。

## 操作本对象的命令

- [[command/UNC/20.15.2/DSP-GENERATESDC]] · DSP GENERATESDC
- [[command/UNC/20.15.2/FOC-GENERATESDC]] · FOC GENERATESDC

## 证据

- 原始手册：`evidence/UNC/20.15.2/强制产生业务数据容器（FOC-GENERATESDC）_09897028.md`
- 原始手册：`evidence/UNC/20.15.2/查询强制产生业务数据容器结果（DSP-GENERATESDC）_09897026.md`
