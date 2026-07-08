---
id: UNC@20.15.2@ConfigObject@IUARD
type: ConfigObject
name: IUARD（Iu模式接入限制参数）
nf: UNC
version: 20.15.2
object_name: IUARD
object_kind: entity
applicable_nf:
- SGSN
status: active
---

# IUARD（Iu模式接入限制参数）

## 说明

**适用网元：SGSN**

该命令用于增加Iu模式接入限制参数。该命令先根据IMSI号段将用户进行分类，再对每一类用户按照用户使用的卡类型（SIM/USIM）、签约的ARD信息、签约的APN信息进行区分而控制用户接入UTRAN网络。

该命令适用于以下场景。若运营商希望拒绝某个号段接入UTRAN系统，则可以启用根据签约ARD控制用户接入特性。若运营商希望控制某类用户是否允许接入UTRAN，但HLR/HSS不支持ARD时，则可以启用根据签约APN控制用户接入特性。若运营商已经强制要求对GERAN用户使用SIM卡，UTRAN用户使用USIM卡，并希望对不同卡进行灵活的接入控制，就需要启用按SIM卡/USIM卡控制用户接入特性。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-IUARD]] · ADD IUARD
- [[command/UNC/20.15.2/LST-IUARD]] · LST IUARD
- [[command/UNC/20.15.2/MOD-IUARD]] · MOD IUARD
- [[command/UNC/20.15.2/RMV-IUARD]] · RMV IUARD

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改Iu模式接入限制参数(MOD-IUARD)_72225157.md`
- 原始手册：`evidence/UNC/20.15.2/删除Iu模式接入限制参数(RMV-IUARD)_26145476.md`
- 原始手册：`evidence/UNC/20.15.2/增加Iu模式接入限制参数(ADD-IUARD)_72345073.md`
- 原始手册：`evidence/UNC/20.15.2/查询Iu模式接入限制参数(LST-IUARD)_26305288.md`
