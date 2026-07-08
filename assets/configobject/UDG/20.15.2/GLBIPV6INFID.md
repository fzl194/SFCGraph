---
id: UDG@20.15.2@ConfigObject@GLBIPV6INFID
type: ConfigObject
name: GLBIPV6INFID（整机IPv6接口ID配置）
nf: UDG
version: 20.15.2
object_name: GLBIPV6INFID
object_kind: global_setting
applicable_nf:
- PGW-U
- UPF
status: active
---

# GLBIPV6INFID（整机IPv6接口ID配置）

## 说明

**适用NF：PGW-U、UPF**

![](设置整机IPv6接口ID配置（SET GLBIPV6INFID）_71074283.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，开启本功能后IPv6地址interface ID将会包含用户标识信息IMSI，请关注个人隐私保护。

该命令用于控制全局为用户分配IPv6地址时，是否开启IMSI作为用户的IPv6地址interface ID(IPv6地址的后64位)功能。

## 操作本对象的命令

- [[command/UDG/20.15.2/LST-GLBIPV6INFID]] · LST GLBIPV6INFID
- [[command/UDG/20.15.2/SET-GLBIPV6INFID]] · SET GLBIPV6INFID

## 证据

- 原始手册：`evidence/UDG/20.15.2/GLBIPV6INFID.md`
- 原始手册：`evidence/UDG/20.15.2/GLBIPV6INFID.md`
