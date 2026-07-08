---
id: UNC@20.15.2@ConfigObject@SCPFUNCSW
type: ConfigObject
name: SCPFUNCSW（间接路由功能）
nf: UNC
version: 20.15.2
object_name: SCPFUNCSW
object_kind: global_setting
applicable_nf:
- AMF
- SMF
- SMSF
- NCG
status: active
---

# SCPFUNCSW（间接路由功能）

## 说明

![](设置间接路由功能（SET SCPFUNCSW）_02870340.assets/notice_3.0-zh-cn_2.png)

指定网元之间网络部署未调整时，执行该命令会导致实际功能不生效。

间接路由和直连路由模式间切换，可能存在业务呼损。

**适用NF：AMF、SMF、SMSF、NCG**

该命令用于设置是否开启间接路由功能和服务发现代理功能。可通过指定本端和对端的NF类型进行设置。

- 当间接路由开关为ON且服务发现代理开关为ON，区域位置开关为OFF，且已经加载相关License时候，开启ModelD模式。
- 当间接路由开关为ON，服务发现代理开关为OFF，区域位置开关为OFF，已经加载相关License时候，开启ModelC模式（不判断是否同大区）。
- 当间接路由开关为ON，服务发现代理开关为OFF，区域位置开关为ON，已经加载相关License时候，需要判断是否同大区。跨大区则使用ModelC，否则使用直连模式。
- 当间接路由开关为OFF，发现代理为OFF，区域位置开关为OFF时，与NF对应的业务消息交互和服务发现均处于直连模式。
- 当拨测开关为ON，启动拨测阶段。反之则走正常流程。
- 直连不支持拨测。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-SCPFUNCSW]] · LST SCPFUNCSW
- [[command/UNC/20.15.2/SET-SCPFUNCSW]] · SET SCPFUNCSW

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询间接路由功能（LST-SCPFUNCSW）_02630398.md`
- 原始手册：`evidence/UNC/20.15.2/设置间接路由功能（SET-SCPFUNCSW）_02870340.md`
