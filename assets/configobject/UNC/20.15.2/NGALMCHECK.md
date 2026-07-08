---
id: UNC@20.15.2@ConfigObject@NGALMCHECK
type: ConfigObject
name: NGALMCHECK（5G告警核查）
nf: UNC
version: 20.15.2
object_name: NGALMCHECK
object_kind: action
applicable_nf:
- AMF
- SMF
status: active
---

# NGALMCHECK（5G告警核查）

## 说明

**适用NF：AMF、SMF**

当发现系统存在未恢复的故障告警时，可通过该命令启动告警核查功能，若系统识别出该故障已经恢复，则自动恢复该故障告警。

当前支持核查的告警包括ALM-100058 NG-RAN 链路故障告警、ALM-100059 NG-RAN 节点不可达告警。

## 操作本对象的命令

- [[command/UNC/20.15.2/DSP-NGALMCHECK]] · DSP NGALMCHECK
- [[command/UNC/20.15.2/STR-NGALMCHECK]] · STR NGALMCHECK

## 证据

- 原始手册：`evidence/UNC/20.15.2/NGALMCHECK.md`
- 原始手册：`evidence/UNC/20.15.2/NGALMCHECK.md`
