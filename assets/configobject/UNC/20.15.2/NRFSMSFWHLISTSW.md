---
id: UNC@20.15.2@ConfigObject@NRFSMSFWHLISTSW
type: ConfigObject
name: NRFSMSFWHLISTSW（SMSF白名单开关）
nf: UNC
version: 20.15.2
object_name: NRFSMSFWHLISTSW
object_kind: global_setting
applicable_nf:
- NRF
status: active
---

# NRFSMSFWHLISTSW（SMSF白名单开关）

## 说明

![](设置SMSF白名单开关（SET NRFSMSFWHLISTSW）_22223361.assets/notice_3.0-zh-cn_2.png)

该命令与ADD NRFSMSFWHITELST配合使用，在白名单未设置完成时请勿打开SMSFWHLISTSW，否则未加入到白名单中的SMSF在发现参数仅携带TargetNftype时将无法被发现。

**适用NF：NRF**

该命令用于设置SMSF白名单功能是否打开。白名单用于配置现网存量SMSF，避免新升级的SMSF不能为存量用户提供业务，导致错误业务导流。

## 操作本对象的命令

- [LST NRFSMSFWHLISTSW](command/UNC/20.15.2/LST-NRFSMSFWHLISTSW.md)
- [SET NRFSMSFWHLISTSW](command/UNC/20.15.2/SET-NRFSMSFWHLISTSW.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询SMSF白名单开关（LST-NRFSMSFWHLISTSW）_71463514.md`
- 原始手册：`evidence/UNC/20.15.2/设置SMSF白名单开关（SET-NRFSMSFWHLISTSW）_22223361.md`
