---
id: UNC@20.15.2@ConfigObject@RECOVERY
type: ConfigObject
name: RECOVERY（本端重启次数）
nf: UNC
version: 20.15.2
object_name: RECOVERY
object_kind: entity
applicable_nf:
- SGSN
- MME
- AMF
status: active
---

# RECOVERY（本端重启次数）

## 说明

![](修改本端重启次数(MOD RECOVERY)_72225609.assets/notice_3.0-zh-cn_2.png)

该命令可能导致对端网元无法正常处理GTPC消息。

**适用网元：SGSN、MME、AMF**

该命令用于修改本端Recovery值。本端Recovery值表示本端系统重启的次数。

## 操作本对象的命令

- [[command/UNC/20.15.2/DSP-RECOVERY]] · DSP RECOVERY
- [[command/UNC/20.15.2/MOD-RECOVERY]] · MOD RECOVERY

## 证据

- 原始手册：`evidence/UNC/20.15.2/RECOVERY.md`
- 原始手册：`evidence/UNC/20.15.2/RECOVERY.md`
