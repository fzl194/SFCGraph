---
id: UDG@20.15.2@ConfigObject@UPPFCPPATH
type: ConfigObject
name: UPPFCPPATH（路径相关属性）
nf: UDG
version: 20.15.2
object_name: UPPFCPPATH
object_kind: global_setting
applicable_nf:
- SGW-U
- PGW-U
- UPF
status: active
---

# UPPFCPPATH（路径相关属性）

## 说明

**适用NF：SGW-U、PGW-U、UPF**

![](设置PFCP路径相关属性（SET UPPFCPPATH）_82837240.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，配置不合理可能导致告警或者用户去活，建议根据现网规划设置。

该命令用来设置PFCP协议配置属性。包括当前系统支持主动发送PFCP消息重发时间间隔和最大尝试发送次数，心跳检测消息的发送次数。

## 操作本对象的命令

- [[command/UDG/20.15.2/LST-UPPFCPPATH]] · LST UPPFCPPATH
- [[command/UDG/20.15.2/SET-UPPFCPPATH]] · SET UPPFCPPATH

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询路径相关属性（LST-UPPFCPPATH）_82837241.md`
- 原始手册：`evidence/UDG/20.15.2/设置PFCP路径相关属性（SET-UPPFCPPATH）_82837240.md`
