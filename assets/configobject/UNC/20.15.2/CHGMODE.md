---
id: UNC@20.15.2@ConfigObject@CHGMODE
type: ConfigObject
name: CHGMODE（计费接口选择方式）
nf: UNC
version: 20.15.2
object_name: CHGMODE
object_kind: global_setting
applicable_nf:
- SGW-C
- PGW-C
- SMF
- GGSN
status: active
---

# CHGMODE（计费接口选择方式）

## 说明

![](设置计费接口选择方式（SET CHGMODE）_09651465.assets/notice_3.0-zh-cn_2.png)

配置计费接口选择方式不当可能选错计费策略接口，相应计费策略接口未配置时会导致计费相关流程失败，进而影响用户使用业务，比如用户无法正常激活。

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用于配置在不同类型终端接入不同网络时所选择的计费接口。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-CHGMODE]] · LST CHGMODE
- [[command/UNC/20.15.2/SET-CHGMODE]] · SET CHGMODE

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询计费接口选择方式（LST-CHGMODE）_09652191.md`
- 原始手册：`evidence/UNC/20.15.2/设置计费接口选择方式（SET-CHGMODE）_09651465.md`
