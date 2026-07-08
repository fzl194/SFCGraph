---
id: UNC@20.15.2@ConfigObject@MASALMCHECK
type: ConfigObject
name: MASALMCHECK（5G告警核查）
nf: UNC
version: 20.15.2
object_name: MASALMCHECK
object_kind: action
status: active
---

# MASALMCHECK（5G告警核查）

## 说明

当发现系统存在未恢复的故障告警时，可通过该命令启动告警核查功能，若系统识别出该故障已经恢复，则自动恢复该故障告警。

当前支持核查的告警包括ALM-100155 HTTP链路故障告警。

## 操作本对象的命令

- [[command/UNC/20.15.2/DSP-MASALMCHECK]] · DSP MASALMCHECK
- [[command/UNC/20.15.2/STR-MASALMCHECK]] · STR MASALMCHECK

## 证据

- 原始手册：`evidence/UNC/20.15.2/启动5G告警核查（STR-MASALMCHECK）_80751076.md`
- 原始手册：`evidence/UNC/20.15.2/显示5G告警核查状态（DSP-MASALMCHECK）_32103567.md`
