---
id: UDG@20.15.2@ConfigObject@APNTRAFDFUNC
type: ConfigObject
name: APNTRAFDFUNC（APN流量转发配置）
nf: UDG
version: 20.15.2
object_name: APNTRAFDFUNC
object_kind: global_setting
applicable_nf:
- PGW-U
- UPF
status: active
---

# APNTRAFDFUNC（APN流量转发配置）

## 说明

**适用NF：PGW-U、UPF**

设置流量转发APN开关，当TRAFFICFDSW配置为ENABLE时，UPF支持通过VXLAN隧道转发数据流到MPF，否则不支持。

## 操作本对象的命令

- [LST APNTRAFDFUNC](command/UDG/20.15.2/LST-APNTRAFDFUNC.md)
- [SET APNTRAFDFUNC](command/UDG/20.15.2/SET-APNTRAFDFUNC.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询APN流量转发配置（LST-APNTRAFDFUNC）_92153143.md`
- 原始手册：`evidence/UDG/20.15.2/设置流量转发APN开关（SET-APNTRAFDFUNC）_92313447.md`
