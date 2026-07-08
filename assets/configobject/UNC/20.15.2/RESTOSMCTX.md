---
id: UNC@20.15.2@ConfigObject@RESTOSMCTX
type: ConfigObject
name: RESTOSMCTX（容灾用户SM上下文信息）
nf: UNC
version: 20.15.2
object_name: RESTOSMCTX
object_kind: query_target
applicable_nf:
- MME
status: active
---

# RESTOSMCTX（容灾用户SM上下文信息）

## 说明

**适用网元：MME**

- 本命令用于查询系统内容灾用户的SM上下文信息。
- 输出结果分为SM User上下文、SM PDN上下文、SM PDP上下文等报表。
- 当某一字段显示“NULL”时，表示该字段没有备份。

## 操作本对象的命令

- [[command/UNC/20.15.2/DSP-RESTOSMCTX]] · DSP RESTOSMCTX

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示容灾用户SM上下文信息（DSP-RESTOSMCTX）_26307108.md`
