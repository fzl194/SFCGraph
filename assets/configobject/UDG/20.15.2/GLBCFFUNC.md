---
id: UDG@20.15.2@ConfigObject@GLBCFFUNC
type: ConfigObject
name: GLBCFFUNC（内容过滤全局开关）
nf: UDG
version: 20.15.2
object_name: GLBCFFUNC
object_kind: global_setting
applicable_nf:
- PGW-U
- UPF
status: active
---

# GLBCFFUNC（内容过滤全局开关）

## 说明

**适用NF：PGW-U、UPF**

![](设置内容过滤全局开关（SET GLBCFFUNC）_54628145.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，该命令会导致用户匹配范围发生变化，可能导致性能下降。执行命令前请评估对性能的影响，如果无法评估请联系华为技术支持。

该命令用来配置全局是否启用内容过滤功能。

## 操作本对象的命令

- [LST GLBCFFUNC](command/UDG/20.15.2/LST-GLBCFFUNC.md)
- [SET GLBCFFUNC](command/UDG/20.15.2/SET-GLBCFFUNC.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询内容过滤全局开关（LST-GLBCFFUNC）_50710734.md`
- 原始手册：`evidence/UDG/20.15.2/设置内容过滤全局开关（SET-GLBCFFUNC）_54628145.md`
