---
id: UNC@20.15.2@ConfigObject@POLICYMODE
type: ConfigObject
name: POLICYMODE（策略接口的选择方式）
nf: UNC
version: 20.15.2
object_name: POLICYMODE
object_kind: global_setting
applicable_nf:
- PGW-C
- SMF
- GGSN
status: active
---

# POLICYMODE（策略接口的选择方式）

## 说明

![](设置策略接口的选择方式（SET POLICYMODE）_09653658.assets/notice_3.0-zh-cn_2.png)

配置策略接口的选择方式不当可能导致PCC用户选择错误接口的PCRF/PCF服务器，进而影响用户使用业务，比如用户无法正常激活。

**适用NF：PGW-C、SMF、GGSN**

该命令用于配置策略接口的选择方式。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-POLICYMODE]] · LST POLICYMODE
- [[command/UNC/20.15.2/SET-POLICYMODE]] · SET POLICYMODE

## 证据

- 原始手册：`evidence/UNC/20.15.2/POLICYMODE.md`
- 原始手册：`evidence/UNC/20.15.2/POLICYMODE.md`
