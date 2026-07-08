---
id: UNC@20.15.2@ConfigObject@APNCHGMODE
type: ConfigObject
name: APNCHGMODE（基于APN的计费接口选择方式）
nf: UNC
version: 20.15.2
object_name: APNCHGMODE
object_kind: entity
applicable_nf:
- SGW-C
- PGW-C
- SMF
- GGSN
status: active
---

# APNCHGMODE（基于APN的计费接口选择方式）

## 说明

![](增加基于APN的计费接口选择方式（ADD APNCHGMODE）_72001540.assets/notice_3.0-zh-cn_2.png)

配置基于APN的计费接口选择方式不当可能选错计费策略接口，相应计费策略接口未配置时会导致计费相关流程失败，进而影响用户使用业务，比如用户无法正常激活。

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用于添加在不同APN不同类型终端接入不同网络时所选择的计费接口。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-APNCHGMODE]] · ADD APNCHGMODE
- [[command/UNC/20.15.2/LST-APNCHGMODE]] · LST APNCHGMODE
- [[command/UNC/20.15.2/MOD-APNCHGMODE]] · MOD APNCHGMODE
- [[command/UNC/20.15.2/RMV-APNCHGMODE]] · RMV APNCHGMODE

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改基于APN的计费接口选择方式（MOD-APNCHGMODE）_72001549.md`
- 原始手册：`evidence/UNC/20.15.2/删除基于APN的计费接口选择方式（RMV-APNCHGMODE）_96242742.md`
- 原始手册：`evidence/UNC/20.15.2/增加基于APN的计费接口选择方式（ADD-APNCHGMODE）_72001540.md`
- 原始手册：`evidence/UNC/20.15.2/查询基于APN的计费接口选择方式（LST-APNCHGMODE）_72001543.md`
