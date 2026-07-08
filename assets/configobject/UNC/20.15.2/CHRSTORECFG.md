---
id: UNC@20.15.2@ConfigObject@CHRSTORECFG
type: ConfigObject
name: CHRSTORECFG（CHR存盘配置）
nf: UNC
version: 20.15.2
object_name: CHRSTORECFG
object_kind: global_setting
applicable_nf:
- SGSN
- MME
status: active
---

# CHRSTORECFG（CHR存盘配置）

## 说明

**适用网元：SGSN、MME**

该命令用于控制系统在上报CHR单据时，配置CHR单据在 ucf 上的存储策略。 ucf 存储CHR单据功能主要应用于没有部署CloudUDN同时又想做本地单据分析的局点，或传输链路中断时将CHR单据本地保存的情况。存储功能打开时 UNC 采集订阅流程的CHR单据发送给 ucf ，并且通知 ucf 存储到本地硬盘中。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-CHRSTORECFG]] · LST CHRSTORECFG
- [[command/UNC/20.15.2/SET-CHRSTORECFG]] · SET CHRSTORECFG

## 证据

- 原始手册：`evidence/UNC/20.15.2/CHRSTORECFG.md`
- 原始手册：`evidence/UNC/20.15.2/CHRSTORECFG.md`
