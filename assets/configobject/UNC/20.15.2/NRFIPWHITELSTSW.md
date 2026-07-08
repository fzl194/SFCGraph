---
id: UNC@20.15.2@ConfigObject@NRFIPWHITELSTSW
type: ConfigObject
name: NRFIPWHITELSTSW（NF IP白名单开关）
nf: UNC
version: 20.15.2
object_name: NRFIPWHITELSTSW
object_kind: global_setting
applicable_nf:
- NRF
status: active
---

# NRFIPWHITELSTSW（NF IP白名单开关）

## 说明

![](设置NF IP白名单开关（SET NRFIPWHITELSTSW）_29869622.assets/notice_3.0-zh-cn_2.png)

该命令与ADD NRFIPWHITELST配合使用，在NF IP白名单未设置完成时请勿打开此开关，否则客户端IP未加入到IP白名单中的NF将无法正常注册、去注册、更新及维持到NRF的心跳。

**适用NF：NRF**

该命令用于设置NF IP白名单功能开关，用于控制非预期NF接入。

该命令与ADD NRFIPWHITELST配合使用，在NF IP白名单未设置完成时请勿打开此开关，否则客户端IP未加入到IP白名单中的NF将无法正常注册、去注册、更新及维持到NRF的心跳。

该命令与SET NRFWHITELISTSW开关互斥，两者不能同时打开。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-NRFIPWHITELSTSW]] · LST NRFIPWHITELSTSW
- [[command/UNC/20.15.2/SET-NRFIPWHITELSTSW]] · SET NRFIPWHITELSTSW

## 证据

- 原始手册：`evidence/UNC/20.15.2/NRFIPWHITELSTSW.md`
- 原始手册：`evidence/UNC/20.15.2/NRFIPWHITELSTSW.md`
