---
id: UNC@20.15.2@ConfigObject@DFTIDLETIME
type: ConfigObject
name: DFTIDLETIME（默认空闲上下文定时器配置）
nf: UNC
version: 20.15.2
object_name: DFTIDLETIME
object_kind: global_setting
applicable_nf:
- SGW-C
- PGW-C
- SMF
- GGSN
status: active
---

# DFTIDLETIME（默认空闲上下文定时器配置）

## 说明

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用于设置全局的默认空闲上下文定时器和不活动上下文定时器开关和时长。

- 空闲上下文定时器：会话无数据传输的时长超过定时器时长后，删除会话、承载或Qos Flow。对2G、3G、4G和5G用户都生效。
- 不活动上下文定时器：会话无数据传输的时长超过定时器时长后，释放会话的用户面资源。仅对5G用户生效。

## 操作本对象的命令

- [LST DFTIDLETIME](command/UNC/20.15.2/LST-DFTIDLETIME.md)
- [SET DFTIDLETIME](command/UNC/20.15.2/SET-DFTIDLETIME.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询默认空闲上下文定时器配置（LST-DFTIDLETIME）_09653130.md`
- 原始手册：`evidence/UNC/20.15.2/设置默认空闲上下文定时器配置（SET-DFTIDLETIME）_09654414.md`
