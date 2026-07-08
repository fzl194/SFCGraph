---
id: UNC@20.15.2@ConfigObject@ALMRPTMODE
type: ConfigObject
name: ALMRPTMODE（告警上报模式）
nf: UNC
version: 20.15.2
object_name: ALMRPTMODE
object_kind: global_setting
applicable_nf:
- SGSN
- MME
status: active
---

# ALMRPTMODE（告警上报模式）

## 说明

**适用网元：SGSN、MME**

该命令用于设置告警的上报模式。如果系统内某一个告警大量产生时，会对系统的性能和告警台产生冲击，此时可以根据实际的需求，配置告警的上报模式，可以有效降低大量告警对系统的影响。

## 操作本对象的命令

- [LST ALMRPTMODE](command/UNC/20.15.2/LST-ALMRPTMODE.md)
- [SET ALMRPTMODE](command/UNC/20.15.2/SET-ALMRPTMODE.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询告警上报模式(LST-ALMRPTMODE)_72225883.md`
- 原始手册：`evidence/UNC/20.15.2/设置告警上报模式(SET-ALMRPTMODE)_26146204.md`
