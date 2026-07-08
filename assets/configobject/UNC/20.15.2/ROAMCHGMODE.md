---
id: UNC@20.15.2@ConfigObject@ROAMCHGMODE
type: ConfigObject
name: ROAMCHGMODE（基于漫游属性的计费接口选择方式）
nf: UNC
version: 20.15.2
object_name: ROAMCHGMODE
object_kind: entity
applicable_nf:
- PGW-C
- GGSN
- SMF
- SGW-C
status: active
---

# ROAMCHGMODE（基于漫游属性的计费接口选择方式）

## 说明

![](增加基于漫游属性的计费接口选择方式（ADD ROAMCHGMODE）_23622918.assets/notice_3.0-zh-cn_2.png)

配置基于漫游属性选择计费接口选择方式不当可能选错计费策略接口，相应计费策略接口未配置时会导致计费相关流程失败，影响用户使用业务，进而影响用户使用业务，比如用户无法正常激活。

**适用NF：PGW-C、GGSN、SMF、SGW-C**

该命令用于添加不同APN、不同漫游属性、不同类型终端接入不同网络时所选择的计费接口。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-ROAMCHGMODE]] · ADD ROAMCHGMODE
- [[command/UNC/20.15.2/LST-ROAMCHGMODE]] · LST ROAMCHGMODE
- [[command/UNC/20.15.2/MOD-ROAMCHGMODE]] · MOD ROAMCHGMODE
- [[command/UNC/20.15.2/RMV-ROAMCHGMODE]] · RMV ROAMCHGMODE

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改基于漫游属性的计费接口选择方式（MOD-ROAMCHGMODE）_23622982.md`
- 原始手册：`evidence/UNC/20.15.2/删除基于漫游属性的计费接口选择方式（RMV-ROAMCHGMODE）_70462609.md`
- 原始手册：`evidence/UNC/20.15.2/增加基于漫游属性的计费接口选择方式（ADD-ROAMCHGMODE）_23622918.md`
- 原始手册：`evidence/UNC/20.15.2/查询基于漫游属性的计费接口选择方式（LST-ROAMCHGMODE）_23782774.md`
