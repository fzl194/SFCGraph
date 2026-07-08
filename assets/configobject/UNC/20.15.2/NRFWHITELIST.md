---
id: UNC@20.15.2@ConfigObject@NRFWHITELIST
type: ConfigObject
name: NRFWHITELIST（NF白名单）
nf: UNC
version: 20.15.2
object_name: NRFWHITELIST
object_kind: entity
applicable_nf:
- NRF
status: active
---

# NRFWHITELIST（NF白名单）

## 说明

![](增加NF白名单（ADD NRFWHITELIST）_35519265.assets/notice_3.0-zh-cn_2.png)

该命令与SET NRFWHITELISTSW配合使用，在白名单未设置完成时请勿打开NF白名单开关，否则未加入到白名单中的NF将无法正常注册、去注册、更新及维持到NRF的心跳功能。

**适用NF：NRF**

该命令用于增加NF白名单内的NF实例。白名单设置用于支撑NRF可以对不同NF进行区别处理，避免新升级NRF未经功能验证完善后就接入业务，导致错误业务导流。

该命令与NF白名单开关SET NRFWHITELISTSW配合使用，在白名单未设置完成时请勿打开NF白名单开关，否则影响未加入到白名单中NF的正常注册、去注册、更新及心跳功能。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-NRFWHITELIST]] · ADD NRFWHITELIST
- [[command/UNC/20.15.2/LST-NRFWHITELIST]] · LST NRFWHITELIST
- [[command/UNC/20.15.2/RMV-NRFWHITELIST]] · RMV NRFWHITELIST

## 证据

- 原始手册：`evidence/UNC/20.15.2/NRFWHITELIST.md`
- 原始手册：`evidence/UNC/20.15.2/NRFWHITELIST.md`
- 原始手册：`evidence/UNC/20.15.2/NRFWHITELIST.md`
