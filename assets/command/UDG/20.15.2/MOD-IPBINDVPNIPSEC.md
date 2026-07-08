---
id: UDG@20.15.2@MMLCommand@MOD IPBINDVPNIPSEC
type: MMLCommand
name: MOD IPBINDVPNIPSEC（修改接口绑定VPN）
nf: UDG
version: 20.15.2
verb: MOD
object_keyword: IPBINDVPNIPSEC
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- IPSEC功能管理
- IP服务
- 接口管理
- 绑定VPN
status: active
---

# MOD IPBINDVPNIPSEC（修改接口绑定VPN）

## 功能

![](修改接口绑定VPN（MOD IPBINDVPNIPSEC）_26150759.assets/notice_3.0-zh-cn.png)

修改配置，影响该隧道下的地址信息，有业务影响。

该命令用于修改接口已绑定的VPN。

> **说明**
> - 该命令执行后立即生效。
>
> - 执行该命令将清除该接口下所有的IP配置。
> - 需要在执行[**ADD IPSECINTFCFGIPSEC**](../../IP安全管理/互联网密钥交换/IPsec接口配置/增加IPsec隧道接口（ADD IPSECINTFCFGIPSEC）_80910986.md)之前执行该命令，来使绑定的VPN生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IFNAME | 接口名 | 可选必选说明：必选参数<br>参数含义：用于设置绑定VPN的接口名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。接口名称由接口类型+接口编号组成。<br>默认值：无<br>配置原则：无 |
| IFIPADDR | IPv4地址 | 可选必选说明：该参数在"IPTYPECHECK"配置为"Ipv4"时为条件可选参数。<br>参数含义：该参数用于指定需要配置的IPv4地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。0.0.0.0～255.255.255.255。<br>默认值：无<br>配置原则：无 |
| SUBNETMASK | IPv4地址掩码 | 可选必选说明：该参数在"IPTYPECHECK"配置为"Ipv4"时为条件可选参数。<br>参数含义：该参数用于指定需要配置的接口IPv4地址的网络掩码。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。0.0.0.0～255.255.255.255。<br>默认值：无<br>配置原则：无 |
| VRFNAME | VPN实例名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定接口绑定的VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~31。<br>默认值：无<br>配置原则：无 |
| IPTYPECHECK | 校验为V4还是V6 | 可选必选说明：可选参数<br>参数含义：校验为IPv4还是IPv6。<br>数据来源：本端规划<br>取值范围：<br>- “Ipv4（IPv4）”：IPv4<br>- “Ipv6（IPv6）”：IPv6<br>默认值：Ipv4<br>配置原则：无 |
| IPV6ADDR | IPv6地址 | 可选必选说明：该参数在"IPTYPECHECK"配置为"Ipv6"时为条件可选参数。<br>参数含义：该参数用于指定需要配置的IPv6地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |
| SUBNETMASKIPV6 | IPv6地址掩码 | 可选必选说明：该参数在"IPTYPECHECK"配置为"Ipv6"时为条件可选参数。<br>参数含义：该参数用于指定需要配置的接口IPv6地址的网络掩码。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [接口绑定VPN（IPBINDVPNIPSEC）](configobject/UDG/20.15.2/IPBINDVPNIPSEC.md)

## 使用实例

修改接口绑定VPN：

```
MOD IPBINDVPNIPSEC:IFNAME="Loopback1",VRFNAME="vrf1",IPTYPECHECK=Ipv4;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改接口绑定VPN（MOD-IPBINDVPNIPSEC）_26150759.md`
