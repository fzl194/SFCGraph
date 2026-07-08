---
id: UDG@20.15.2@ConfigObject@DRSWAPREC
type: ConfigObject
name: DRSWAPREC（容灾倒换记录）
nf: UDG
version: 20.15.2
object_name: DRSWAPREC
object_kind: query_target
status: active
---

# DRSWAPREC（容灾倒换记录）

## 说明

该命令用于查询容灾倒换记录。

在主容灾实例上执行，查询的结果是主容灾实例发起倒换复位的记录，包含手工命令倒换。

在备容灾实例上执行，查询的结果是备容灾实例升主倒换的记录，包含手工命令倒换。

主备容灾实例记录配合查看，可以观测容灾实例倒换的完整过程。

> **说明**
> - 该命令只用于在UEG-L/UEN网元采用主备（冷备）容灾模式下执行。
> - 该命令只用于在UEG-M/UEG网元采用主备（热备）容灾模式下执行。

## 操作本对象的命令

- [[command/UDG/20.15.2/LST-DRSWAPREC]] · LST DRSWAPREC

## 证据

- 原始手册：`evidence/UDG/20.15.2/DRSWAPREC.md`
