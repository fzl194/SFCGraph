---
id: UDG@20.15.2@ConfigObject@CERTESCAPESWITCH
type: ConfigObject
name: CERTESCAPESWITCH（证书过期逃生开关状态）
nf: UDG
version: 20.15.2
object_name: CERTESCAPESWITCH
object_kind: global_setting
status: active
---

# CERTESCAPESWITCH（证书过期逃生开关状态）

## 说明

![](设置证书过期逃生开关状态（SET CERTESCAPESWITCH）_55469701.assets/notice_3.0-zh-cn.png)

执行此命令将修改证书过期逃生开关状态，开关关闭后证书过期业务可能会中断。

设置证书过期逃生开关状态。此命令用于设置证书管理页面所有证书在过期情况下是否仍可以正常使用。开关打开情况下证书过期后仍然能正常使用，业务无中断。

> **说明**
> - 本命令需要在稳态环境下执行。
> - 目前不支持证书开关状态为关时打开证书过期逃生开关。
> - 该命令存在系统初始记录，证书过期逃生开关的初始状态和证书开关的初始状态保持一致。
> - 关闭证书开关时，会自动关闭证书过期逃生开关。打开证书开关时，会自动打开证书过期逃生开关。
> - 本命令设置完成后建议间隔至少10秒后再次设置。
> - 初始部署场景下开关默认为开启状态。

## 操作本对象的命令

- [[command/UDG/20.15.2/LST-CERTESCAPESWITCH]] · LST CERTESCAPESWITCH
- [[command/UDG/20.15.2/SET-CERTESCAPESWITCH]] · SET CERTESCAPESWITCH

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询证书过期逃生开关状态（LST-CERTESCAPESWITCH）_06110022.md`
- 原始手册：`evidence/UDG/20.15.2/设置证书过期逃生开关状态（SET-CERTESCAPESWITCH）_55469701.md`
