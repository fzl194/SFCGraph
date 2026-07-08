---
id: UNC@20.15.2@ConfigObject@GLBCDRFLDCFG
type: ConfigObject
name: GLBCDRFLDCFG（全局生效CDR字段配置）
nf: UNC
version: 20.15.2
object_name: GLBCDRFLDCFG
object_kind: query_target
applicable_nf:
- SGW-C
- PGW-C
- SMF
status: active
---

# GLBCDRFLDCFG（全局生效CDR字段配置）

## 说明

**适用NF：SGW-C、PGW-C、SMF**

该命令用来显示全局生效的各类型的话单字段的具体配置。

如果全局模板下某话单类型未绑定模板，则显示该话单类型的缺省配置信息。显示信息中如果模板名字为NULL，则表示是缺省配置信息。

## 操作本对象的命令

- [[command/UNC/20.15.2/DSP-GLBCDRFLDCFG]] · DSP GLBCDRFLDCFG

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询全局生效CDR字段配置（DSP-GLBCDRFLDCFG）_09897014.md`
