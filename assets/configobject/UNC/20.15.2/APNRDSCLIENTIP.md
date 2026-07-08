---
id: UNC@20.15.2@ConfigObject@APNRDSCLIENTIP
type: ConfigObject
name: APNRDSCLIENTIP（APN Radius Client IP接口）
nf: UNC
version: 20.15.2
object_name: APNRDSCLIENTIP
object_kind: entity
applicable_nf:
- PGW-C
- SMF
status: active
---

# APNRDSCLIENTIP（APN Radius Client IP接口）

## 说明

**适用NF：PGW-C、SMF**

该命令用于配置APN实例鉴权或计费请求消息的radius client ip，即鉴权或者计费请求消息的源IP地址。将Gi接口与APN实例进行绑定时将配置此命令。该命令为radius access request和radius accounting request消息指定Gi接口。当发送radius access request和radius accounting request消息时，消息中携带的源地址为指定的Gi接口IP。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-APNRDSCLIENTIP]] · ADD APNRDSCLIENTIP
- [[command/UNC/20.15.2/LST-APNRDSCLIENTIP]] · LST APNRDSCLIENTIP
- [[command/UNC/20.15.2/RMV-APNRDSCLIENTIP]] · RMV APNRDSCLIENTIP

## 证据

- 原始手册：`evidence/UNC/20.15.2/APNRDSCLIENTIP.md`
- 原始手册：`evidence/UNC/20.15.2/APNRDSCLIENTIP.md`
- 原始手册：`evidence/UNC/20.15.2/APNRDSCLIENTIP.md`
