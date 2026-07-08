---
id: UNC@20.15.2@MMLCommand@ADD MONVPN
type: MMLCommand
name: ADD MONVPN（增加监控VPN实例）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: MONVPN
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 可靠性管理
- 微服务可靠性管理
status: active
---

# ADD MONVPN（增加监控VPN实例）

## 功能

该命令用于增加监控VPN实例。

## 注意事项

- 该命令执行后立即生效。

- 该命令只用于在UEG-M/UEG网元采用主备（热备）容灾模式下执行。
- 添加监控VPN实例后，如果监控中的单个VPN实例的邻居全部异常则上报告警ALM-100545容灾组中监控VPN邻居状态异常。
- 在运行状态为主的容灾实例中，如果任意一个VPN组内所有监控的VPN实例内邻居全部异常，则自动发起容灾实例的主备倒换。
- 在运行状态为备的容灾实例中，如果任意一个VPN组内所有监控的VPN实例内邻居全部异常，则收到运行主容灾实例的倒换请求后将回应不允许倒换。
- 该命令执行前，请确保ISLINKED设置正确，否则可能造成误隔离。

- 最多可输入160条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DRGROUPID | 容灾组标识 | 可选必选说明：必选参数<br>参数含义：该参数用于配置容灾组标识。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~8。<br>默认值：无<br>配置原则：无 |
| VPNGRPID | VPN组标识 | 可选必选说明：必选参数<br>参数含义：该参数用于配置VPN组标识。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~10。<br>默认值：无<br>配置原则：无 |
| VPNINSTANCE | VPN实例名称 | 可选必选说明：必选参数<br>参数含义：该参数用于配置VPN实例名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~31。VPN实例名称禁止相同。<br>默认值：无<br>配置原则：无 |
| ISLINKED | 是否联动隔离 | 可选必选说明：可选参数<br>参数含义：该参数用于配置VPN实例是否联动隔离。<br>数据来源：本端规划<br>取值范围：<br>- “YES（是）”：此VPN故障会联动隔离ADD DRSEPINTERFACE命令添加的接口。<br>- “NO（否）”：此VPN故障不会联动隔离ADD DRSEPINTERFACE命令添加的接口。<br>默认值：无<br>配置原则：<br>在免交换组网下组成热备容灾关系的网元间DCI通道相关的VPN实例需要设置为是。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/MONVPN]] · 监控VPN实例（MONVPN）

## 使用实例

增加监控VPN实例:

```
%%ADD MONVPN:DRGROUPID=1,VPNGRPID=1,VPNINSTANCE="1";%%
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加监控VPN实例（ADD-MONVPN）_00921390.md`
