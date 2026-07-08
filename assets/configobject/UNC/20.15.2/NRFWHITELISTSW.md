---
id: UNC@20.15.2@ConfigObject@NRFWHITELISTSW
type: ConfigObject
name: NRFWHITELISTSW（NF白名单开关）
nf: UNC
version: 20.15.2
object_name: NRFWHITELISTSW
object_kind: global_setting
applicable_nf:
- NRF
status: active
---

# NRFWHITELISTSW（NF白名单开关）

## 说明

![](设置NF白名单开关（SET NRFWHITELISTSW）_35374753.assets/notice_3.0-zh-cn_2.png)

该命令与ADD NRFWHITELIST配合使用，在白名单未设置完成时请勿打开此开关，否则未加入到白名单中的NF将无法正常注册、去注册、更新及维持到NRF的心跳功能。

**适用NF：NRF**

该命令用于设置NF白名单功能开关，用于避免新升级NRF未经功能验证完善后就接入业务，导致错误业务导流。

该命令与NF白名单命令ADD NRFWHITELIST配合使用，在白名单未设置完成时请勿打开此开关，否则影响未加入到白名单中NF的正常注册、去注册、更新及心跳功能。

该命令与SET NRFIPWHITELSTSW开关互斥，两者不能同时打开。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-NRFWHITELISTSW]] · LST NRFWHITELISTSW
- [[command/UNC/20.15.2/SET-NRFWHITELISTSW]] · SET NRFWHITELISTSW

## 证据

- 原始手册：`evidence/UNC/20.15.2/NRFWHITELISTSW.md`
- 原始手册：`evidence/UNC/20.15.2/NRFWHITELISTSW.md`
