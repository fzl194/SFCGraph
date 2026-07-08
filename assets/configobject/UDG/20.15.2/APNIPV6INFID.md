---
id: UDG@20.15.2@ConfigObject@APNIPV6INFID
type: ConfigObject
name: APNIPV6INFID（APN IPv6接口ID配置）
nf: UDG
version: 20.15.2
object_name: APNIPV6INFID
object_kind: global_setting
applicable_nf:
- PGW-U
- UPF
status: active
---

# APNIPV6INFID（APN IPv6接口ID配置）

## 说明

**适用NF：PGW-U、UPF**

![](设置APN IPv6接口ID配置（SET APNIPV6INFID）_71074281.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，开启本功能后，对应APN下的IPv6地址interface ID将会包含用户标识信息IMSI，请关注个人隐私保护。

该命令用于控制为用户分配IPv6地址时，APN下是否开启IMSI作为用户的IPv6地址interface ID(IPv6地址的后64位)功能。

## 操作本对象的命令

- [[command/UDG/20.15.2/LST-APNIPV6INFID]] · LST APNIPV6INFID
- [[command/UDG/20.15.2/SET-APNIPV6INFID]] · SET APNIPV6INFID

## 证据

- 原始手册：`evidence/UDG/20.15.2/APNIPV6INFID.md`
- 原始手册：`evidence/UDG/20.15.2/APNIPV6INFID.md`
