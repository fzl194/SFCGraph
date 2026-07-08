---
id: UDG@20.15.2@MMLCommand@SET ADDRESSATTR
type: MMLCommand
name: SET ADDRESSATTR（设置全局地址分配属性）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: ADDRESSATTR
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: true
max_records: 1
category_path:
- 用户面服务管理
- 会话管理
- 会话地址管理
- 全局地址分配属性配置
status: active
---

# SET ADDRESSATTR（设置全局地址分配属性）

## 功能

**适用NF：PGW-U、UPF**

![](设置全局地址分配属性（SET ADDRESSATTR）_06561538.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，参数的配置策略和AAA保持一致。否则可能导致无法分配地址，用户激活失败。

该命令用来设置全局地址分配属性。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 参数V4IPHOSTROUTE和参数V6IPHOSTROUTE设置为关闭的时候，可能导致用户的下行包不通。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | V4POOLWILDCARDSW | V6POOLWILDCARDSW | RELEASETIME | V4IPHOSTROUTE | V6IPHOSTROUTE |
| --- | --- | --- | --- | --- | --- |
| 初始值 | DISABLE | DISABLE | 0 | ENABLE | ENABLE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| V4POOLWILDCARDSW | IPv4地址池通配功能开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定IPv4地址池是否使能通配功能的开关。控制在AAA未下发IPv4地址池通配符的情况下是否开启通配功能。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：需要和AAA的地址池匹配策略保持一致，如果不一致，可能导致UPF无法分配地址，用户激活失败。 |
| V6POOLWILDCARDSW | IPv6地址池通配功能开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定IPv6地址池是否使能通配功能的开关。控制在AAA未下发IPv6地址池通配符的情况下是否开启通配功能。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：需要和AAA的地址池匹配策略保持一致，如果不一致，可能导致UPF无法分配地址，用户激活失败。 |
| RELEASETIME | 地址租期（秒） | 可选必选说明：可选参数<br>参数含义：用户因收到下行异常报文被去激活，用户释放之后，对应用户IP地址的等待释放时间。取值为0时，根据地址池配置的release-time延迟释放IP地址。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～86400，单位是秒。<br>默认值：无<br>配置原则：无 |
| V4IPHOSTROUTE | IPv4主机路由发布开关 | 可选必选说明：可选参数<br>参数含义：控制IPv4的UE外部地址主机路由是否对外发布。<br>数据来源：本端规划<br>取值范围：1、ENABLE：IPv4的UE外部地址主机路由对外发布。 2、DISABLE：IPv4的UE外部地址主机路由不对外发布。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：如果和AAA配置策略不一致，可能导致无法分配地址，用户激活失败。 |
| V6IPHOSTROUTE | IPv6主机路由发布开关 | 可选必选说明：可选参数<br>参数含义：控制IPv6的UE外部地址主机路由是否对外发布。<br>数据来源：本端规划<br>取值范围：1、ENABLE：IPv6的UE外部地址主机路由对外发布。 2、DISABLE：IPv6的UE外部地址主机路由不对外发布。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：如果和AAA配置策略不一致，可能导致无法分配地址，用户激活失败。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/ADDRESSATTR]] · AddressAttr配置（ADDRESSATTR）

## 使用实例

设置全局地址分配属性，打开IPv4地址池通配功能开关：

```
SET ADDRESSATTR: V4POOLWILDCARDSW=ENABLE;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置全局地址分配属性（SET-ADDRESSATTR）_06561538.md`
