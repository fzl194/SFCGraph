---
id: UNC@20.15.2@ConfigObject@MDTCTX
type: ConfigObject
name: MDTCTX（MDT上下文）
nf: UNC
version: 20.15.2
object_name: MDTCTX
object_kind: entity
applicable_nf:
- MME
status: active
---

# MDTCTX（MDT上下文）

## 说明

![](删除MDT上下文(RMV MDTCTX)_26305646.assets/notice_3.0-zh-cn_2.png)

MDT任务正常运行时，删除本地的MDT配置参数会导致该任务异常。正常场景下请慎用本功能。

**适用网元：MME**

用于在异常场景下本地残留MDT配置参数时需要删除用户在MME上的MDT信息的情况下使用。

## 操作本对象的命令

- [[command/UNC/20.15.2/DSP-MDTCTX]] · DSP MDTCTX
- [[command/UNC/20.15.2/RMV-MDTCTX]] · RMV MDTCTX

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除MDT上下文(RMV-MDTCTX)_26305646.md`
- 原始手册：`evidence/UNC/20.15.2/显示MDT上下文(DSP-MDTCTX)_72225515.md`
