---
id: UDG@20.15.2@ConfigObject@CLTVFYSWITCH
type: ConfigObject
name: CLTVFYSWITCH（双向认证开关）
nf: UDG
version: 20.15.2
object_name: CLTVFYSWITCH
object_kind: global_setting
status: active
---

# CLTVFYSWITCH（双向认证开关）

## 说明

![](设置双向认证开关（SET CLTVFYSWITCH）_84238196.assets/notice_3.0-zh-cn.png)

执行该命令打开 “双向认证开关” 后可能会导致网管、三方平台断链，请谨慎操作。

此命令用于设置双向认证开关的开关状态。

> **说明**
> - 该命令仅限角色为Administrators的用户执行。
> - 打开双向认证开关可能会导致网管、三方平台断链。需要在网管、三方平台上完成对接证书的上传。
> - 双向认证开关默认关闭。
> - 仅支持设置6443和9000端口的双向认证开关。

## 操作本对象的命令

- [[command/UDG/20.15.2/LST-CLTVFYSWITCH]] · LST CLTVFYSWITCH
- [[command/UDG/20.15.2/SET-CLTVFYSWITCH]] · SET CLTVFYSWITCH

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询双向认证开关（LST-CLTVFYSWITCH）_19797985.md`
- 原始手册：`evidence/UDG/20.15.2/设置双向认证开关（SET-CLTVFYSWITCH）_84238196.md`
