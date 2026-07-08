---
id: UDG@20.15.2@MMLCommand@SET APPTRAFFICPARA
type: MMLCommand
name: SET APPTRAFFICPARA（设置应用流量参数）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: APPTRAFFICPARA
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: true
max_records: 1
category_path:
- 用户面服务管理
- 业务匹配策略
- 业务匹配公共配置
- 业务公共参数管理
- 应用流量参数
status: active
---

# SET APPTRAFFICPARA（设置应用流量参数）

## 功能

**适用NF：PGW-U、UPF**

![](设置应用流量参数（SET APPTRAFFICPARA）_49101653.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，1、修改TrafficRuleSw为Disable会导致当前动态流量规则或者DNS衍生规则失效； 2、修改RuleSource为DYNAMIC_TRAFFIC_RULE会导致当前DNS衍生规则失效，动态流量规则开始生效； 3、修改RuleSource为DNS_RULE_EXTENDED会导致当前动态流量规则失效，DNS衍生规则开始生效；

该命令用于动态分流规则匹配时设置应用流量参数。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | TRAFFICRULESW | RULESOURCE |
| --- | --- | --- |
| 初始值 | ENABLE | DYNAMIC_TRAFFIC_RULE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TRAFFICRULESW | 应用流量规则开关 | 可选必选说明：必选参数<br>参数含义：该参数用于设置是否使用Traffic Rule进行匹配。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能（关闭）。<br>- ENABLE：使能（开启）。<br>默认值：无<br>配置原则：无 |
| RULESOURCE | 规则来源 | 可选必选说明：可选参数<br>参数含义：该参数用于设置应用流量规则的来源。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DNS_RULE_EXTENDED：DNS规则衍生。<br>- DYNAMIC_TRAFFIC_RULE：动态流量规则。<br>默认值：无<br>配置原则：<br>- 该参数配置为DNS规则衍生时，表示DNS Rule衍生的基于目的IP的本地分流功能。<br>- 动态流量规则包含了源IP地址、目的IP地址、源端口、目的端口、协议的五元组信息，当数据流的报文中携带五元组中的一个或多个信息，命中Traffic Rule时，则根据Traffic Rule中定义的动作放通或丢弃数据流。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/APPTRAFFICPARA]] · 应用流量参数（APPTRAFFICPARA）

## 使用实例

在需要配置应用流量规则使能并设置来源为DNS规则衍生时，执行该命令设置应用流量规则及规则来源：

```
SET APPTRAFFICPARA: TRAFFICRULESW=ENABLE, RULESOURCE=DNS_RULE_EXTENDED;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-APPTRAFFICPARA.md`
