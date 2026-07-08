---
id: UDG@20.15.2@ConfigObject@ADDRESSATTR
type: ConfigObject
name: ADDRESSATTR（AddressAttr配置）
nf: UDG
version: 20.15.2
object_name: ADDRESSATTR
object_kind: global_setting
applicable_nf:
- PGW-U
- UPF
status: active
---

# ADDRESSATTR（AddressAttr配置）

## 说明

**适用NF：PGW-U、UPF**

![](设置全局地址分配属性（SET ADDRESSATTR）_06561538.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，参数的配置策略和AAA保持一致。否则可能导致无法分配地址，用户激活失败。

该命令用来设置全局地址分配属性。

## 操作本对象的命令

- [[command/UDG/20.15.2/LST-ADDRESSATTR]] · LST ADDRESSATTR
- [[command/UDG/20.15.2/SET-ADDRESSATTR]] · SET ADDRESSATTR

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询AddressAttr配置（LST-ADDRESSATTR）_05977154.md`
- 原始手册：`evidence/UDG/20.15.2/设置全局地址分配属性（SET-ADDRESSATTR）_06561538.md`
