---
id: UNC@20.15.2@ConfigObject@POOLALMPARA
type: ConfigObject
name: POOLALMPARA（本地地址池使用率告警参数）
nf: UNC
version: 20.15.2
object_name: POOLALMPARA
object_kind: global_setting
applicable_nf:
- PGW-C
- SMF
- GGSN
status: active
---

# POOLALMPARA（本地地址池使用率告警参数）

## 说明

**适用NF：PGW-C、SMF、GGSN**

为了即时监控地址池使用率，UNC提供了“地址池使用率超阈值”告警。该命令用于设置地址池使用率告警的产生阈值和恢复阈值。

## 操作本对象的命令

- [LST POOLALMPARA](command/UNC/20.15.2/LST-POOLALMPARA.md)
- [SET POOLALMPARA](command/UNC/20.15.2/SET-POOLALMPARA.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询本地地址池使用率告警参数（LST-POOLALMPARA）_37497449.md`
- 原始手册：`evidence/UNC/20.15.2/设置本地地址池使用率告警参数（SET-POOLALMPARA）_92057522.md`
