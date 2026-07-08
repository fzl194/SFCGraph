---
id: UNC@20.15.2@ConfigObject@APNIDLETIME
type: ConfigObject
name: APNIDLETIME（APN空闲上下文定时器配置）
nf: UNC
version: 20.15.2
object_name: APNIDLETIME
object_kind: global_setting
applicable_nf:
- SGW-C
- PGW-C
- SMF
- GGSN
status: active
---

# APNIDLETIME（APN空闲上下文定时器配置）

## 说明

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用于配置指定APN空闲上下文时长。在运营商网络中存在长时间在线的用户，为防止出现垃圾上下文和浪费无线侧资源可以配置该功能。其功能包括空闲上下文定时器时长和不活动上下文定时器时长。

- 空闲上下文定时器：会话无数据传输的时长超过定时器时长后，删除会话、承载或Qos Flow。对2G、3G、4G和5G用户都生效。
- 不活动上下文定时器：会话无数据传输的时长超过定时器时长后，释放会话的用户面资源。仅对5G用户生效。

## 操作本对象的命令

- [LST APNIDLETIME](command/UNC/20.15.2/LST-APNIDLETIME.md)
- [SET APNIDLETIME](command/UNC/20.15.2/SET-APNIDLETIME.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询APN空闲上下文定时器配置（LST-APNIDLETIME）_09653829.md`
- 原始手册：`evidence/UNC/20.15.2/设置APN空闲上下文定时器配置（SET-APNIDLETIME）_09653122.md`
