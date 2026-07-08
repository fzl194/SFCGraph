---
id: UNC@20.15.2@ConfigObject@IMSIFORSMSC
type: ConfigObject
name: IMSIFORSMSC（融合短消息功能共部署SMSC支持的IMSI号段配置）
nf: UNC
version: 20.15.2
object_name: IMSIFORSMSC
object_kind: entity
applicable_nf:
- SMSF
status: active
---

# IMSIFORSMSC（融合短消息功能共部署SMSC支持的IMSI号段配置）

## 说明

**适用NF：SMSF**

该命令用于设置融合短消息功能共部署SMSC支持的IMSI号段或MSISDN号段（通过DWORD16 BIT9软参配置）。在MO短消息流程中，SET ROUTSMSCPARA的“按号段选择SMSC开关”设置为“打开”时，用户IMSI或MSISDN如果归属本大区，且属于当前配置号段则短消息发往融合短消息功能共部署的SMSC，否则发往本大区跨DC的SMSC。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-IMSIFORSMSC]] · ADD IMSIFORSMSC
- [[command/UNC/20.15.2/LST-IMSIFORSMSC]] · LST IMSIFORSMSC
- [[command/UNC/20.15.2/RMV-IMSIFORSMSC]] · RMV IMSIFORSMSC

## 证据

- 原始手册：`evidence/UNC/20.15.2/IMSIFORSMSC.md`
- 原始手册：`evidence/UNC/20.15.2/IMSIFORSMSC.md`
- 原始手册：`evidence/UNC/20.15.2/IMSIFORSMSC.md`
