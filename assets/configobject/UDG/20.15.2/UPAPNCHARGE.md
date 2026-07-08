---
id: UDG@20.15.2@ConfigObject@UPAPNCHARGE
type: ConfigObject
name: UPAPNCHARGE（APN计费配置）
nf: UDG
version: 20.15.2
object_name: UPAPNCHARGE
object_kind: global_setting
applicable_nf:
- PGW-U
- UPF
status: active
---

# UPAPNCHARGE（APN计费配置）

## 说明

**适用NF：PGW-U、UPF**

![](设置APN的计费配置（SET UPAPNCHARGE）_29940708.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，修改默认配额使能开关会影响用户业务访问时延。

该命令用于设置指定APN的用户在进行在线计费业务时，是否使用默认配额。主要应用场景是，当支持使用默认配额时，新业务请求的首个报文，在向SMF申请配额时，UPF不缓存这个报文，允许其通过；非新业务场景申请配额期间的报文，UPF不丢包，允许其通过。

## 操作本对象的命令

- [[command/UDG/20.15.2/LST-UPAPNCHARGE]] · LST UPAPNCHARGE
- [[command/UDG/20.15.2/SET-UPAPNCHARGE]] · SET UPAPNCHARGE

## 证据

- 原始手册：`evidence/UDG/20.15.2/UPAPNCHARGE.md`
- 原始手册：`evidence/UDG/20.15.2/UPAPNCHARGE.md`
