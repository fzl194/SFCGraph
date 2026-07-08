---
id: UDG@20.15.2@ConfigObject@UPDEFAULTQUOTA
type: ConfigObject
name: UPDEFAULTQUOTA（全局默认配额开关）
nf: UDG
version: 20.15.2
object_name: UPDEFAULTQUOTA
object_kind: global_setting
applicable_nf:
- PGW-U
- UPF
status: active
---

# UPDEFAULTQUOTA（全局默认配额开关）

## 说明

**适用NF：PGW-U、UPF**

![](设置全局默认配额开关（SET UPDEFAULTQUOTA）_82837623.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，修改默认配额使能开关会影响用户业务访问时延。

该命令用于设置指定漫游类型的用户在进行在线计费业务时，是否使用默认配额。主要应用场景是，当支持使用默认配额时，新业务请求的首个报文，在向SMF申请配额时，UPF不缓存这个报文，允许其通过；非新业务场景申请配额期间的报文，UPF不丢包，允许其通过。

## 操作本对象的命令

- [LST UPDEFAULTQUOTA](command/UDG/20.15.2/LST-UPDEFAULTQUOTA.md)
- [SET UPDEFAULTQUOTA](command/UDG/20.15.2/SET-UPDEFAULTQUOTA.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询全局默认配额开关（LST-UPDEFAULTQUOTA）_82837624.md`
- 原始手册：`evidence/UDG/20.15.2/设置全局默认配额开关（SET-UPDEFAULTQUOTA）_82837623.md`
