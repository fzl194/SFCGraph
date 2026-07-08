---
id: UDG@20.15.2@ConfigObject@URRGRPBINDING
type: ConfigObject
name: URRGRPBINDING（用户模板的URR组绑定关系）
nf: UDG
version: 20.15.2
object_name: URRGRPBINDING
object_kind: binding
applicable_nf:
- PGW-U
- UPF
status: active
---

# URRGRPBINDING（用户模板的URR组绑定关系）

## 说明

**适用NF：PGW-U、UPF**

![](设置用户模板的URR组绑定关系（SET URRGRPBINDING）_82837281.assets/notice_3.0-zh-cn.png)

建议用户模板下的同时配置缺省URR组和缺省信令URR组，否则可能导致使用该用户模板的用户的部分流量无法计费。

该命令用于设置用户模板的使用量上报规则组绑定关系。用于指定用户模板默认的计费策略，包括业务使用量上报规则组，信令使用量上报规则组，重定向使用量上报规则组和TCP重传使用量上报规则组。

## 操作本对象的命令

- [[command/UDG/20.15.2/RMV-URRGRPBINDING]] · RMV URRGRPBINDING
- [[command/UDG/20.15.2/SET-URRGRPBINDING]] · SET URRGRPBINDING

## 证据

- 原始手册：`evidence/UDG/20.15.2/URRGRPBINDING.md`
- 原始手册：`evidence/UDG/20.15.2/URRGRPBINDING.md`
