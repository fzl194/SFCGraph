---
id: UNC@20.15.2@ConfigObject@NRFSMSFWHITELST
type: ConfigObject
name: NRFSMSFWHITELST（SMSF白名单）
nf: UNC
version: 20.15.2
object_name: NRFSMSFWHITELST
object_kind: entity
applicable_nf:
- NRF
status: active
---

# NRFSMSFWHITELST（SMSF白名单）

## 说明

![](增加SMSF白名单（ADD NRFSMSFWHITELST）_71623458.assets/notice_3.0-zh-cn_2.png)

该命令与SET NRFSMSFWHLISTSW配合使用，在白名单未设置完成时请勿打开SMSFWHLISTSW，否则未加入到白名单中的SMSF在发现参数仅携带TargetNftype时将无法被发现。

**适用NF：NRF**

该命令用于增加SMSF白名单内的SMSF实例。白名单用于配置现网存量SMSF，确保存量SMSF可以为存量用户提供业务，避免错误业务导流。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-NRFSMSFWHITELST]] · ADD NRFSMSFWHITELST
- [[command/UNC/20.15.2/LST-NRFSMSFWHITELST]] · LST NRFSMSFWHITELST
- [[command/UNC/20.15.2/RMV-NRFSMSFWHITELST]] · RMV NRFSMSFWHITELST

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除SMSF白名单（RMV-NRFSMSFWHITELST）_21823529.md`
- 原始手册：`evidence/UNC/20.15.2/增加SMSF白名单（ADD-NRFSMSFWHITELST）_71623458.md`
- 原始手册：`evidence/UNC/20.15.2/查询SMSF白名单（LST-NRFSMSFWHITELST）_22103389.md`
