---
id: UNC@20.15.2@ConfigObject@GBARD
type: ConfigObject
name: GBARD（Gb模式接入限制参数）
nf: UNC
version: 20.15.2
object_name: GBARD
object_kind: entity
applicable_nf:
- SGSN
status: active
---

# GBARD（Gb模式接入限制参数）

## 说明

**适用网元：SGSN**

该命令用于增加Gb模式接入限制参数。该命令先根据IMSI号段将用户进行分类，再对每一类用户按照用户使用的卡类型（SIM/USIM）、签约的ARD信息、签约的APN信息进行区分而控制用户接入GERAN网络。

此命令适用于以下场景。若运营商希望拒绝某个号段接入GERAN系统，则可以启用根据签约ARD控制用户接入特性；若运营商希望控制某类用户是否允许接入GERAN，但HLR/HSS不支持ARD时，则可以启用根据签约APN控制用户接入特性；若运营商已经强制要求对GERAN用户使用SIM卡，UTRAN用户使用USIM卡，并希望对不同卡进行灵活的接入控制，就需要启用按SIM卡/USIM卡控制用户接入特性。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-GBARD]] · ADD GBARD
- [[command/UNC/20.15.2/LST-GBARD]] · LST GBARD
- [[command/UNC/20.15.2/MOD-GBARD]] · MOD GBARD
- [[command/UNC/20.15.2/RMV-GBARD]] · RMV GBARD

## 证据

- 原始手册：`evidence/UNC/20.15.2/GBARD.md`
- 原始手册：`evidence/UNC/20.15.2/GBARD.md`
- 原始手册：`evidence/UNC/20.15.2/GBARD.md`
- 原始手册：`evidence/UNC/20.15.2/GBARD.md`
