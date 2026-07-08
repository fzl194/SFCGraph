---
id: UDG@20.15.2@ConfigObject@MSSCOMMMATCH
type: ConfigObject
name: MSSCOMMMATCH（通信模块规则匹配开关）
nf: UDG
version: 20.15.2
object_name: MSSCOMMMATCH
object_kind: global_setting
status: active
---

# MSSCOMMMATCH（通信模块规则匹配开关）

## 说明

![](设置通信模块规则匹配开关（SET MSSCOMMMATCH）_49961350.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，操作不当会导致性能下降，请谨慎使用并联系华为技术支持协助操作。

该命令用于设置通信模块规则匹配开关，即诊断开关命令；通过开关打开规则匹配，协助问题定位。

当规则列表输入格式有误时，有错误信息“绑定的规则无效。”。

当输入的规则ID有不存在的，有错误信息“绑定的规则不存在。”。

当设置的服务类型和规则ID的类型不一致，有错误信息“绑定的规则类型有冲突。”。

## 操作本对象的命令

- [[command/UDG/20.15.2/SET-MSSCOMMMATCH]] · SET MSSCOMMMATCH

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置通信模块规则匹配开关（SET-MSSCOMMMATCH）_49961350.md`
