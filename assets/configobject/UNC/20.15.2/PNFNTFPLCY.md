---
id: UNC@20.15.2@ConfigObject@PNFNTFPLCY
type: ConfigObject
name: PNFNTFPLCY（对端网元的通知抑制时间）
nf: UNC
version: 20.15.2
object_name: PNFNTFPLCY
object_kind: global_setting
applicable_nf:
- AMF
- SMF
- SMSF
status: active
---

# PNFNTFPLCY（对端网元的通知抑制时间）

## 说明

**适用NF：AMF、SMF、SMSF**

对端NF状态频繁变更时，本端NF不需要频繁感知并处理，本命令用于抑制向本端NF通知对端NF状态变化的频率，配置通知对端NF状态变化的抑制时间。

## 操作本对象的命令

- [LST PNFNTFPLCY](command/UNC/20.15.2/LST-PNFNTFPLCY.md)
- [SET PNFNTFPLCY](command/UNC/20.15.2/SET-PNFNTFPLCY.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询对端网元的通知抑制时间（LST-PNFNTFPLCY）_96242392.md`
- 原始手册：`evidence/UNC/20.15.2/设置对端网元的通知抑制时间（SET-PNFNTFPLCY）_96243197.md`
