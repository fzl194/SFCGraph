---
id: UNC@20.15.2@ConfigObject@SCCPNGT
type: ConfigObject
name: SCCPNGT（SCCP新全局翻译码）
nf: UNC
version: 20.15.2
object_name: SCCPNGT
object_kind: entity
applicable_nf:
- SGSN
- MME
- SMSF
status: active
---

# SCCPNGT（SCCP新全局翻译码）

## 说明

**适用网元：SGSN、MME、SMSF**

此命令用于增加SCCP新全局码表指定记录的信息。此项配置命令关联SCCPGT中的翻译结果类型一项。当“翻译结果类型”为“DPCNEWGT（DPC + 新GT）”，这里的新GT是用于远端GT翻译的，如果本端发出的消息到达远端例如HLR、VLR后，希望将消息中的GT进行替换为更为合理的新GT，则需要先配置此项，然后在SCCPGT的GT翻译表中对新GT的索引进行关联即可。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-SCCPNGT]] · ADD SCCPNGT
- [[command/UNC/20.15.2/LST-SCCPNGT]] · LST SCCPNGT
- [[command/UNC/20.15.2/MOD-SCCPNGT]] · MOD SCCPNGT
- [[command/UNC/20.15.2/RMV-SCCPNGT]] · RMV SCCPNGT

## 证据

- 原始手册：`evidence/UNC/20.15.2/SCCPNGT.md`
- 原始手册：`evidence/UNC/20.15.2/SCCPNGT.md`
- 原始手册：`evidence/UNC/20.15.2/SCCPNGT.md`
- 原始手册：`evidence/UNC/20.15.2/SCCPNGT.md`
