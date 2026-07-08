---
id: UNC@20.15.2@ConfigObject@APNPROFILE
type: ConfigObject
name: APNPROFILE（APN配置）
nf: UNC
version: 20.15.2
object_name: APNPROFILE
object_kind: entity
applicable_nf:
- SGSN
status: active
---

# APNPROFILE（APN配置）

## 说明

**适用网元：SGSN**

该命令用于新增APN的APN的概要信息，如QOS，计费属性等。

当用户使用GPRS/UMTS接入网接入并进行PDP激活时，如果使用 [ADD SMACTCTRL](../激活过程管理/增加激活过程控制参数（ADD SMACTCTRL）_26305472.md) 命令纠正用户激活的APNNI为回落APNNI时，如果回落APNNI未签约，使用本配置指定该APN的概要信息。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-APNPROFILE]] · ADD APNPROFILE
- [[command/UNC/20.15.2/LST-APNPROFILE]] · LST APNPROFILE
- [[command/UNC/20.15.2/MOD-APNPROFILE]] · MOD APNPROFILE
- [[command/UNC/20.15.2/RMV-APNPROFILE]] · RMV APNPROFILE

## 证据

- 原始手册：`evidence/UNC/20.15.2/APNPROFILE.md`
- 原始手册：`evidence/UNC/20.15.2/APNPROFILE.md`
- 原始手册：`evidence/UNC/20.15.2/APNPROFILE.md`
- 原始手册：`evidence/UNC/20.15.2/APNPROFILE.md`
