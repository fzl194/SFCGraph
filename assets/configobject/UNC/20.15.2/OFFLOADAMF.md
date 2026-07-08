---
id: UNC@20.15.2@ConfigObject@OFFLOADAMF
type: ConfigObject
name: OFFLOADAMF（AMF迁移任务）
nf: UNC
version: 20.15.2
object_name: OFFLOADAMF
object_kind: action
applicable_nf:
- AMF
status: active
---

# OFFLOADAMF（AMF迁移任务）

## 说明

**适用NF：AMF**

此命令用于停止当前正在进行的迁移任务。

当需要发起新的迁移任务，执行“DSP OFFLOADAMF”命令查询是否有正在迁移的任务，如果有正在迁移的任务，执行此命令停止当前正在进行的迁移任务，再执行“STR OFFLOADAMF”发起新任务。

## 操作本对象的命令

- [[command/UNC/20.15.2/DSP-OFFLOADAMF]] · DSP OFFLOADAMF
- [[command/UNC/20.15.2/STP-OFFLOADAMF]] · STP OFFLOADAMF
- [[command/UNC/20.15.2/STR-OFFLOADAMF]] · STR OFFLOADAMF

## 证据

- 原始手册：`evidence/UNC/20.15.2/OFFLOADAMF.md`
- 原始手册：`evidence/UNC/20.15.2/OFFLOADAMF.md`
- 原始手册：`evidence/UNC/20.15.2/OFFLOADAMF.md`
