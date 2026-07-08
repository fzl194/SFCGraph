---
id: UDG@20.15.2@ConfigObject@AUTHSOAP
type: ConfigObject
name: AUTHSOAP（网管登录认证策略）
nf: UDG
version: 20.15.2
object_name: AUTHSOAP
object_kind: global_setting
status: active
---

# AUTHSOAP（网管登录认证策略）

## 说明

![](设置网管登录认证策略（SET AUTHSOAP）_97634436.assets/notice_3.0-zh-cn.png)

- “ALL(普通认证和增强认证)”采用的认证算法强度较低，系统可能会受到安全风险。
- “ENHANCED(增强认证)”会导致系统禁止普通认证登录UDG，网管以普通认证的方式无法登录UDG。

本命令用于设置网管登录 UDG 的认证策略。

## 操作本对象的命令

- [[command/UDG/20.15.2/LST-AUTHSOAP]] · LST AUTHSOAP
- [[command/UDG/20.15.2/SET-AUTHSOAP]] · SET AUTHSOAP

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询网管登录认证策略（LST-AUTHSOAP）_97635699.md`
- 原始手册：`evidence/UDG/20.15.2/设置网管登录认证策略（SET-AUTHSOAP）_97634436.md`
