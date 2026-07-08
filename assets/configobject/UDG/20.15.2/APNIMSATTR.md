---
id: UDG@20.15.2@ConfigObject@APNIMSATTR
type: ConfigObject
name: APNIMSATTR（ApnImsAttr配置）
nf: UDG
version: 20.15.2
object_name: APNIMSATTR
object_kind: global_setting
applicable_nf:
- UPF
- PGW-U
status: active
---

# APNIMSATTR（ApnImsAttr配置）

## 说明

**适用NF：PGW-U、UPF**

![](设置ApnImsAttr配置（SET APNIMSATTR）_82837822.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，该操作会配置APN的IMS属性，可能会影响用户的VoLTE业务。

命令用来配置APN的IMS属性从而使得VoLTE语音业务可用。

## 操作本对象的命令

- [[command/UDG/20.15.2/LST-APNIMSATTR]] · LST APNIMSATTR
- [[command/UDG/20.15.2/SET-APNIMSATTR]] · SET APNIMSATTR

## 关联对象

- [[configobject/UDG/20.15.2/APN]] · APN

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询ApnImsAttr配置（LST-APNIMSATTR）_86527128.md`
- 原始手册：`evidence/UDG/20.15.2/设置ApnImsAttr配置（SET-APNIMSATTR）_82837822.md`
