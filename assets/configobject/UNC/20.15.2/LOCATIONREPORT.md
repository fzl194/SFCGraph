---
id: UNC@20.15.2@ConfigObject@LOCATIONREPORT
type: ConfigObject
name: LOCATIONREPORT（用户位置信息）
nf: UNC
version: 20.15.2
object_name: LOCATIONREPORT
object_kind: global_setting
applicable_nf:
- PGW-C
- GGSN
- SMF
status: active
---

# LOCATIONREPORT（用户位置信息）

## 说明

**适用NF：PGW-C、GGSN、SMF**

实时位置上报特性可以采用PCF/PCRF下发位置trigger的方式来触发，也可以采用SMF/PGW-C/GGSN本地配置位置trigger的方式来触发。SMF/PGW-C/GGSN可以通过本命令来配置本地位置trigger。要开启基于本地位置trigger的实时位置上报特性，除本配置外，还受到全局位置上报功能（SET SMCOMMFUNC）和APN位置上报功能（ADD APN）的控制。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-LOCATIONREPORT]] · LST LOCATIONREPORT
- [[command/UNC/20.15.2/SET-LOCATIONREPORT]] · SET LOCATIONREPORT

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询用户位置信息（LST-LOCATIONREPORT）_04484293.md`
- 原始手册：`evidence/UNC/20.15.2/设置用户位置信息（SET-LOCATIONREPORT）_04484294.md`
