---
id: UNC@20.15.2@ConfigObject@SCCPGT
type: ConfigObject
name: SCCPGT（SCCP全局翻译码）
nf: UNC
version: 20.15.2
object_name: SCCPGT
object_kind: entity
applicable_nf:
- SGSN
- MME
- SMSF
status: active
---

# SCCPGT（SCCP全局翻译码）

## 说明

**适用网元：SGSN、MME、SMSF**

此命令用于增加SCCP全局码翻译表中指定记录的信息，用于将GT码翻译成由DPC、SSN、GT或NEWGT等不同组合而组成的新地址。

## 操作本对象的命令

- [ADD SCCPGT](command/UNC/20.15.2/ADD-SCCPGT.md)
- [LST SCCPGT](command/UNC/20.15.2/LST-SCCPGT.md)
- [MOD SCCPGT](command/UNC/20.15.2/MOD-SCCPGT.md)
- [RMV SCCPGT](command/UNC/20.15.2/RMV-SCCPGT.md)
- [TST SCCPGT](command/UNC/20.15.2/TST-SCCPGT.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改SCCP全局翻译码(MOD-SCCPGT)_26146326.md`
- 原始手册：`evidence/UNC/20.15.2/删除SCCP全局翻译码(RMV-SCCPGT)_72345925.md`
- 原始手册：`evidence/UNC/20.15.2/增加SCCP全局翻译码(ADD-SCCPGT)_26306136.md`
- 原始手册：`evidence/UNC/20.15.2/查询SCCP全局翻译码(LST-SCCPGT)_72226005.md`
- 原始手册：`evidence/UNC/20.15.2/测试SCCP全局翻译码(TST-SCCPGT)_26306138.md`
