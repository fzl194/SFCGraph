---
id: UDG@20.15.2@ConfigObject@VOLTEMOSALMTHD
type: ConfigObject
name: VOLTEMOSALMTHD（异常MOS告警阈值为系统初始设置值）
nf: UDG
version: 20.15.2
object_name: VOLTEMOSALMTHD
object_kind: global_setting
applicable_nf:
- PGW-U
status: active
---

# VOLTEMOSALMTHD（异常MOS告警阈值为系统初始设置值）

## 说明

**适用NF：PGW-U**

该命令用于设置MOS值异常的呼叫比例告警阈值和恢复告警阈值。当MOS值异常的呼叫比例连续10次超过告警阈值时产生“ALM-81152 VoLTE语音质量差”，当低于配置的恢复阈值时“ALM-81152 VoLTE语音质量差”恢复。

## 操作本对象的命令

- [LST VOLTEMOSALMTHD](command/UDG/20.15.2/LST-VOLTEMOSALMTHD.md)
- [RTR VOLTEMOSALMTHD](command/UDG/20.15.2/RTR-VOLTEMOSALMTHD.md)
- [SET VOLTEMOSALMTHD](command/UDG/20.15.2/SET-VOLTEMOSALMTHD.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/恢复异常MOS告警阈值为系统初始设置值（RTR-VOLTEMOSALMTHD）_69418600.md`
- 原始手册：`evidence/UDG/20.15.2/查询异常MOS告警阈值（LST-VOLTEMOSALMTHD）_57538681.md`
- 原始手册：`evidence/UDG/20.15.2/设置异常MOS告警阈值（SET-VOLTEMOSALMTHD）_69178840.md`
