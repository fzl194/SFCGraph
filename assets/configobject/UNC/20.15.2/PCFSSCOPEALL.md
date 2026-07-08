---
id: UNC@20.15.2@ConfigObject@PCFSSCOPEALL
type: ConfigObject
name: PCFSSCOPEALL（所有的PCF的业务服务区）
nf: UNC
version: 20.15.2
object_name: PCFSSCOPEALL
object_kind: entity
applicable_nf:
- PGW-C
- SMF
- GGSN
status: active
---

# PCFSSCOPEALL（所有的PCF的业务服务区）

## 说明

![](删除所有的PCF的业务服务区（RMV PCFSSCOPEALL）_38449589.assets/notice_3.0-zh-cn_2.png)

删除PCF的业务服务区不当可能导致动态PCC用户无法基于业务服务区选择PCF，进而影响用户使用业务。

**适用NF：PGW-C、SMF、GGSN**

该命令用于删除所有的PCF的业务服务区。

## 操作本对象的命令

- [[command/UNC/20.15.2/RMV-PCFSSCOPEALL]] · RMV PCFSSCOPEALL

## 证据

- 原始手册：`evidence/UNC/20.15.2/PCFSSCOPEALL.md`
