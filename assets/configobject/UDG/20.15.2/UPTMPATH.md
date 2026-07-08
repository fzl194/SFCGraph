---
id: UDG@20.15.2@ConfigObject@UPTMPATH
type: ConfigObject
name: UPTMPATH（TM路径相关属性）
nf: UDG
version: 20.15.2
object_name: UPTMPATH
object_kind: global_setting
applicable_nf:
- SGW-U
- PGW-U
status: active
---

# UPTMPATH（TM路径相关属性）

## 说明

**适用NF：SGW-U、PGW-U**

![](设置TM路径相关属性（SET UPTMPATH）_68602067.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，配置不合理可能导致告警或者用户去活，建议根据现网规划设置。

该命令用来设置TM协议配置属性。包括当前系统支持主动发送TM消息重发时间间隔和最大尝试发送次数，Echo消息重发时间间隔和路径断后发送次数，NE状态空闲检查开关和NE空闲状态超时时间。

## 操作本对象的命令

- [[command/UDG/20.15.2/LST-UPTMPATH]] · LST UPTMPATH
- [[command/UDG/20.15.2/SET-UPTMPATH]] · SET UPTMPATH

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询TM路径相关属性（LST-UPTMPATH）_70762236.md`
- 原始手册：`evidence/UDG/20.15.2/设置TM路径相关属性（SET-UPTMPATH）_68602067.md`
