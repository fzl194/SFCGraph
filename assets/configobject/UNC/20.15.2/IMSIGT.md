---
id: UNC@20.15.2@ConfigObject@IMSIGT
type: ConfigObject
name: IMSIGT（IMSI-GT对应关系）
nf: UNC
version: 20.15.2
object_name: IMSIGT
object_kind: entity
applicable_nf:
- SGSN
- SMSF
status: active
---

# IMSIGT（IMSI-GT对应关系）

## 说明

**适用网元：SGSN、SMSF**

- 本命令用于增加IMSI前缀与国家代码_网络接入号的对应关系。本网的IMSI以及允许漫游到本网的IMSI都需要增加对应的记录。
- 根据IMSI寻址HLR时，系统需要查询本表，分为以下两种情况:
  1.将IMSI号转换成E.214编码的GT码，条件是在本命令中配置的IMSI前缀与国家代码_网络接入号不同，转换原则是将IMSI中与IMSI前缀相等的部分，转换成国家代码_网络接入号，IMSI的剩余部分不变。一般情况下都采用E.214。
  2.将IMSI号转换成E.212编码的GT码，条件是在本命令中配置的IMSI前缀与国家代码_网络接入号相同，转换原则是将IMSI中与IMSI前缀相等的部分，转换成国家代码_网络接入号(实际两者是相同的)，IMSI的剩余部分不变。此时 [**ADD SCCPGT**](../../信令传输管理/SCCP管理/SCCP全局翻译码/增加SCCP全局翻译码(ADD SCCPGT)_26306136.md) 中对应GT的编号计划必须为 “陆地移动编号计划” 。
- 相关命令：[**ADD SCCPGT**](../../信令传输管理/SCCP管理/SCCP全局翻译码/增加SCCP全局翻译码(ADD SCCPGT)_26306136.md)--增加SCCP全局翻译码。该命令的作用是将经过[**ADD IMSIGT**](增加IMSI-GT对应关系(ADD IMSIGT)_72345061.md)命令翻译后的GT码再翻译成由DPC、SSN、GT或NEWGT等不同组合而组成的新地址。经过IMSIGT和SCCPGT的两次翻译，最终得到不同寻址方式下的目的地址。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-IMSIGT]] · ADD IMSIGT
- [[command/UNC/20.15.2/LST-IMSIGT]] · LST IMSIGT
- [[command/UNC/20.15.2/MOD-IMSIGT]] · MOD IMSIGT
- [[command/UNC/20.15.2/RMV-IMSIGT]] · RMV IMSIGT

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改IMSI-GT对应关系(MOD-IMSIGT)_72225145.md`
- 原始手册：`evidence/UNC/20.15.2/删除IMSI-GT对应关系(RMV-IMSIGT)_26145464.md`
- 原始手册：`evidence/UNC/20.15.2/增加IMSI-GT对应关系(ADD-IMSIGT)_72345061.md`
- 原始手册：`evidence/UNC/20.15.2/查询IMSI-GT对应关系(LST-IMSIGT)_26305276.md`
