---
id: UDG@20.15.2@ConfigObject@SECALG
type: ConfigObject
name: SECALG（安全算法）
nf: UDG
version: 20.15.2
object_name: SECALG
object_kind: global_setting
status: active
---

# SECALG（安全算法）

## 说明

![](设置安全算法（SET SECALG）_01666249.assets/notice_3.0-zh-cn.png)

执行此命令将修改安全算法开关状态，开关开启后会导致环境启用不安全配置。

该命令用于设置建链时使用的安全算法的开关状态。开关打开时该算法可以使用，关闭时该算法被禁用。

> **说明**
> - 执行此命令关闭不安全配置时，请确认是否存在第三方设备对接场景。如果存在上述场景，关闭后可能会影响对接，请谨慎处理。
> - 执行完本命令修改安全算法状态后请在“ 应用配置 > 服务治理 ”界面查询是否存在OMBrokerSvc服务，如果有则需要对该服务进行“批量复位”操作。
> - 初始部署场景下开关默认为关闭状态，升级场景下开关状态保持不变。

## 操作本对象的命令

- [[command/UDG/20.15.2/LST-SECALG]] · LST SECALG
- [[command/UDG/20.15.2/SET-SECALG]] · SET SECALG

## 证据

- 原始手册：`evidence/UDG/20.15.2/SECALG.md`
- 原始手册：`evidence/UDG/20.15.2/SECALG.md`
