---
id: UNC@20.15.2@ConfigObject@GLBCHRFUNC
type: ConfigObject
name: GLBCHRFUNC（全局CHR功能配置）
nf: UNC
version: 20.15.2
object_name: GLBCHRFUNC
object_kind: global_setting
applicable_nf:
- SGW-C
- PGW-C
- GGSN
- SMF
status: active
---

# GLBCHRFUNC（全局CHR功能配置）

## 说明

![](设置全局CHR功能配置（SET GLBCHRFUNC）_36148217.assets/notice_3.0-zh-cn_2.png)

当小范围CHR存储在OMU时，SPECSESSIONNUM设置过大会导致OMU的CPU升高，且可能导致异常CHR丢失，建议值不超过5。

**适用NF：SGW-C、PGW-C、GGSN、SMF**

该命令用于设置全局CHR功能配置。

## 操作本对象的命令

- [LST GLBCHRFUNC](command/UNC/20.15.2/LST-GLBCHRFUNC.md)
- [SET GLBCHRFUNC](command/UNC/20.15.2/SET-GLBCHRFUNC.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询全局CHR功能配置（LST-GLBCHRFUNC）_89350516.md`
- 原始手册：`evidence/UNC/20.15.2/设置全局CHR功能配置（SET-GLBCHRFUNC）_36148217.md`
