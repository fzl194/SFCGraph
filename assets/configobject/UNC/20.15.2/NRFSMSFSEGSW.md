---
id: UNC@20.15.2@ConfigObject@NRFSMSFSEGSW
type: ConfigObject
name: NRFSMSFSEGSW（SMSF号段白名单功能开关）
nf: UNC
version: 20.15.2
object_name: NRFSMSFSEGSW
object_kind: global_setting
applicable_nf:
- NRF
status: active
---

# NRFSMSFSEGSW（SMSF号段白名单功能开关）

## 说明

![](设置SMSF号段白名单功能开关 （SET NRFSMSFSEGSW）_71303606.assets/notice_3.0-zh-cn_2.png)

该命令与ADD NRFSMSFSEGLIST配合使用，在白名单未设置完成时请勿打开此开关，否则携带非白名单中的号段来发现SMSF时，该号段发现参数在匹配时将会被NRF忽略。

**适用NF：NRF**

该命令用于设置SMSF号段白名单功能开关。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-NRFSMSFSEGSW]] · LST NRFSMSFSEGSW
- [[command/UNC/20.15.2/SET-NRFSMSFSEGSW]] · SET NRFSMSFSEGSW

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询SMSF号段白名单功能开关-（LST-NRFSMSFSEGSW）_21943405.md`
- 原始手册：`evidence/UNC/20.15.2/设置SMSF号段白名单功能开关-（SET-NRFSMSFSEGSW）_71303606.md`
