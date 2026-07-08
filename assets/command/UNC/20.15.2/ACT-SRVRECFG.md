---
id: UNC@20.15.2@MMLCommand@ACT SRVRECFG
type: MMLCommand
name: ACT SRVRECFG（重配置业务数据）
nf: UNC
version: 20.15.2
verb: ACT
object_keyword: SRVRECFG
command_category: 动作类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- CSLB功能管理
- 业务管理
- 业务重配置
status: active
---

# ACT SRVRECFG（重配置业务数据）

## 功能

![](重配置业务数据（ACT SRVRECFG）_29627078.assets/notice_3.0-zh-cn_2.png)

可能会影响正常服务实例地址下发，请谨慎使用并联系华为技术支持协助操作。

当业务VNFC和CSLB的业务数据不一致时，需要触发业务数据重配置，保证业务数据完整性。

## 注意事项

- 请在业务负载较低的情况下执行本命令。

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SRVTYPE | 业务数据类型 | 可选必选说明：必选参数<br>参数含义：指定重配置的业务数据类型。<br>数据来源：本端规划<br>取值范围：<br>- SRVADDR：服务实例地址。<br>- VPN：虚拟专用网络。<br>- LBPLY：通用负载均衡策略。<br>- NEXTHOP：下一跳。<br>- LBPLYEX：扩展负载均衡策略。<br>- NEXTHOPEX：扩展下一跳。<br>- EXCHANGE：交换表。<br>- MISSACT：默认动作。当负载均衡策略匹配失败时，按照缺省动作执行。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SRVRECFG]] · 重配置业务数据（SRVRECFG）

## 使用实例

业务VNFC和CSLB服务实例地址数量不一致，需要重新配置服务实例地址。

```
ACT SRVRECFG: SRVTYPE=SRVADDR;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ACT-SRVRECFG.md`
