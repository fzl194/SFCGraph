---
id: UNC@20.15.2@MMLCommand@ADD IFIPV6ADDRESSIPSEC
type: MMLCommand
name: ADD IFIPV6ADDRESSIPSEC（增加接口IPv6地址）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: IFIPV6ADDRESSIPSEC
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- IPSEC功能管理
- IP服务
- 接口管理
- IPv6地址
status: active
---

# ADD IFIPV6ADDRESSIPSEC（增加接口IPv6地址）

## 功能

该命令用于手工配置接口的IPv6地址。

## 注意事项

- 该命令执行后立即生效。

- 该命令可以在VNRS_VNFC的Ethernet接口，Ethernet子接口，Eth-Trunk接口，Eth-Trunk子接口以及Loopback口，Tunnel口上配置。

- 最多可输入65535条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IFNAME | 接口名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定需要配置IP地址的接口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。接口名称由接口类型+接口编号组成。<br>默认值：无<br>配置原则：<br>请使用<br>[**LST INTERFACEIPSEC**](../接口配置/查询接口（LST INTERFACEIPSEC）_80592504.md)<br>命令查看可用接口。 |
| IFIP6ADDR | IPv6地址 | 可选必选说明：必选参数<br>参数含义：该参数用于指定需要配置的接口IP地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |
| ADDRPREFIXLEN | IPv6地址前缀 | 可选必选说明：必选参数<br>参数含义：该参数用于指定需要配置的接口IPv6地址的网络掩码。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~128。<br>默认值：无<br>配置原则：无 |
| ADDRTYPE | IPv6地址类型 | 可选必选说明：可选参数<br>参数含义：地址类型。<br>数据来源：本端规划<br>取值范围：<br>- Global（Global地址）<br>- LinkLocal（链路本地地址）<br>- Anycast（任播地址）<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [接口IPv6地址（IFIPV6ADDRESSIPSEC）](configobject/UNC/20.15.2/IFIPV6ADDRESSIPSEC.md)

## 使用实例

配置LoopBack4的地址为fc00:0000:0000:0000:0000:0000:0000:0000，地址掩码为128，类型为主地址：

```
ADD IFIPV6ADDRESSIPSEC: IFNAME="LoopBack4", IFIP6ADDR="fc00:0000:0000:0000:0000:0000:0000:0000", ADDRPREFIXLEN=128;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加接口IPv6地址（ADD-IFIPV6ADDRESSIPSEC）_21521206.md`
