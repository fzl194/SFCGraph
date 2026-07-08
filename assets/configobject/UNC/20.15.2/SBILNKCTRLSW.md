---
id: UNC@20.15.2@ConfigObject@SBILNKCTRLSW
type: ConfigObject
name: SBILNKCTRLSW（服务化接口链路自动控制功能开关）
nf: UNC
version: 20.15.2
object_name: SBILNKCTRLSW
object_kind: global_setting
status: active
---

# SBILNKCTRLSW（服务化接口链路自动控制功能开关）

## 说明

![](设置服务化接口链路自动控制功能开关（SET SBILNKCTRLSW）_28971851.assets/notice_3.0-zh-cn_2.png)

如果设置服务化接口链路自动控制功能，可能导致链路数量变化，触发拆链或者新建链路。链路数变多可能会超过对端链路规格限制，导致建链失败；链路数变少可能会导致单链路负载增高，存在单链路过载风险，而且可能会导致对端负载不均衡。

该命令用于设置服务化接口链路自动控制功能。当用户配置功能打开时，按系统默认的复杂链路控制原则建立HTTP链路；当用户配置功能关闭时，按系统默认的简单链路控制原则建立HTTP链路。

## 操作本对象的命令

- [LST SBILNKCTRLSW](command/UNC/20.15.2/LST-SBILNKCTRLSW.md)
- [SET SBILNKCTRLSW](command/UNC/20.15.2/SET-SBILNKCTRLSW.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询服务化接口链路自动控制功能开关（LST-SBILNKCTRLSW）_83813636.md`
- 原始手册：`evidence/UNC/20.15.2/设置服务化接口链路自动控制功能开关（SET-SBILNKCTRLSW）_28971851.md`
