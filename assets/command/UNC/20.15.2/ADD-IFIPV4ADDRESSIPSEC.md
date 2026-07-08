---
id: UNC@20.15.2@MMLCommand@ADD IFIPV4ADDRESSIPSEC
type: MMLCommand
name: ADD IFIPV4ADDRESSIPSEC（增加接口IPv4地址）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: IFIPV4ADDRESSIPSEC
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- IPSEC功能管理
- IP服务
- 接口管理
- IPv4地址
status: active
---

# ADD IFIPV4ADDRESSIPSEC（增加接口IPv4地址）

## 功能

该命令用于配置接口的IP地址，包括逻辑接口及物理接口。物理接口是真实存在的接口。逻辑接口是指能够实现数据交换功能但物理上不存在、需要通过配置建立的接口。

## 注意事项

- 该命令执行后立即生效。

- 该接口需要支持配置IP地址。
- 该命令在版本升级过程中禁止执行。
- 每个主用接口最大允许配置256个接口IP地址：1个主IP地址和255个从IP地址。
- 该命令的必选参数IFNAME可通过[**LST INTERFACEIPSEC**](../接口配置/查询接口（LST INTERFACEIPSEC）_80592504.md)命令查询到。

- 最多可输入65535条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ADDRTYPE | IPv4地址类型 | 可选必选说明：可选参数<br>参数含义：地址类型。<br>数据来源：本端规划<br>取值范围：<br>- “Main（主地址）”：主地址<br>- “Sub（从地址）”：从地址<br>- “Brwd（被借用地址）”：被借用地址<br>- “Brw（借用地址）”：借用地址<br>默认值：Main<br>配置原则：无 |
| IFNAME | 接口名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定需要配置IP地址的接口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。接口名称由接口类型+接口编号组成。<br>默认值：无<br>配置原则：<br>请使用<br>[**LST INTERFACEIPSEC**](../接口配置/查询接口（LST INTERFACEIPSEC）_80592504.md)<br>命令查看可用接口。 |
| SUBNETMASK | IPv4地址掩码 | 可选必选说明：必选参数<br>参数含义：该参数用于指定需要配置的接口IPv4地址的网络掩码。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。0.0.0.0～255.255.255.255。<br>默认值：无<br>配置原则：<br>使用网络规划的接口IP所属网段的掩码。<br>除Loopback接口外，其它接口不能配置255.255.255.255的掩码。 |
| IFIPADDR | IPv4地址 | 可选必选说明：必选参数<br>参数含义：该参数用于指定需要配置的接口IP地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。0.0.0.0～255.255.255.255。<br>默认值：无<br>配置原则：<br>IPv4地址不能配置为0.0.0.0、255.255.255.255和环回地址(127.0.0.1)。<br>IPv4地址必须是A、B或者C类地址。<br>IPv4地址在系统内必须唯一。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@IFIPV4ADDRESSIPSEC]] · 接口IPv4地址（IFIPV4ADDRESSIPSEC）

## 使用实例

配置LoopBack4的地址为192.168.1.1，地址掩码为255.255.255.0，类型为主地址：

```
ADD IFIPV4ADDRESSIPSEC: ADDRTYPE=Main, IFNAME="LoopBack4", SUBNETMASK="255.255.255.0", IFIPADDR="192.168.1.1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-IFIPV4ADDRESSIPSEC.md`
