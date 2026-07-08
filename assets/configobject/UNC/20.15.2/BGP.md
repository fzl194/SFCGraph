---
id: UNC@20.15.2@ConfigObject@BGP
type: ConfigObject
name: BGP
nf: UNC
version: 20.15.2
object_name: BGP
object_kind: global_setting
status: active
---

# BGP

## 说明

![](设置BGP（SET BGP）_00866001.assets/notice_3.0-zh-cn_2.png)

操作不当会去使能BGP，导致BGP功能不可用，并且所有历史BGP配置全部删除，请谨慎使用并联系华为技术支持协助操作。

该命令用于创建BGP协议并设置BGP协议参数。BGP是一种外部网关协议（EGP），与OSPF等内部网关协议（IGP）不同，其着眼点不在于发现和计算路由，而在于在AS之间选择最佳路由和控制路由的传播。BGP协议默认不开启认证，认证需要手动开启，否则会有风险。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-BGP]] · LST BGP
- [[command/UNC/20.15.2/SET-BGP]] · SET BGP

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询BGP（LST-BGP）_00840665.md`
- 原始手册：`evidence/UNC/20.15.2/设置BGP（SET-BGP）_00866001.md`
