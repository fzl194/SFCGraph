---
id: UDG@20.15.2@ConfigObject@APNAFFUNC
type: ConfigObject
name: APNAFFUNC（APN防欺诈功能）
nf: UDG
version: 20.15.2
object_name: APNAFFUNC
object_kind: global_setting
applicable_nf:
- PGW-U
- UPF
status: active
---

# APNAFFUNC（APN防欺诈功能）

## 说明

**适用NF：PGW-U、UPF**

![](设置APN防欺诈功能（SET APNAFFUNC）_82837800.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，误配后会影响系统性能，和具体规则匹配到的用户数有关。执行命令前请评估对性能的影响，如果无法评估请联系华为技术支持。

此命令用于在指定APN下配置是否启用防欺诈功能。当用户需要开启或关闭指定APN下的防欺诈开关时配置。

## 操作本对象的命令

- [[command/UDG/20.15.2/LST-APNAFFUNC]] · LST APNAFFUNC
- [[command/UDG/20.15.2/SET-APNAFFUNC]] · SET APNAFFUNC

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询APN防欺诈功能（LST-APNAFFUNC）_82837801.md`
- 原始手册：`evidence/UDG/20.15.2/设置APN防欺诈功能（SET-APNAFFUNC）_82837800.md`
