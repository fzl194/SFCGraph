---
id: UNC@20.15.2@MMLCommand@MOD PAEPORTGATEWAY
type: MMLCommand
name: MOD PAEPORTGATEWAY（修改网关转发地址）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: PAEPORTGATEWAY
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 系统调测
- PAE 调测命令
- 配置
status: active
---

# MOD PAEPORTGATEWAY（修改网关转发地址）

## 功能

![](修改网关转发地址（MOD PAEPORTGATEWAY）_98683661.assets/notice_3.0-zh-cn_2.png)

内联口网关IP配置错误，或者网关MAC地址学习失败，将会导致内联口报文无法跨子网通信，业务会出现呼损，同时会产生告警“ALM-100338 Fabric平面状态为Down”。请联系华为技术支持协助操作。

该命令用于修改指定网段索引下的内联口的网关地址信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NETWORKINDEX | 网段索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定网段索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~4294967295。<br>默认值：无<br>配置原则：无 |
| PLANEID | 平面ID | 可选必选说明：必选参数<br>参数含义：该参数用于指定平面ID。可以通过<br>[**DSP PAEPORTGROUPINFO**](../端口/显示PAE端口组信息（DSP PAEPORTGROUPINFO）_44950521.md)<br>指令查询。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~1，3~6。<br>默认值：无<br>配置原则：无 |
| IPVERSION | IP地址类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定IP地址的类型。<br>数据来源：全网规划<br>取值范围：<br>- IPv4（IPv4）<br>- IPv6（IPv6）<br>默认值：无<br>配置原则：<br>参考当前环境使用的IP类型。 |
| GATEWAYIPV4 | 网关IPv4地址 | 可选必选说明：该参数在"IPVERSION"配置为"IPv4"时为条件必选参数。<br>参数含义：该参数用于指定网关IPv4地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：<br>网关地址必须与平面内的端口IP地址同网段。可通过<br>[**DSP PAEPORTINFO**](../端口/显示PAE端口基本信息（DSP PAEPORTINFO）_92520040.md)<br>命令查看。 |
| IPV4MASK | IPv4地址掩码 | 可选必选说明：该参数在"IPVERSION"配置为"IPv4"时为条件必选参数。<br>参数含义：该参数用于指定网关IPv4地址的网络掩码。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。0.0.0.0～255.255.255.254。<br>默认值：无<br>配置原则：<br>使用网络规划的接口IP所属网段的掩码。 |
| GATEWAYIPV6 | 网关IPv6地址 | 可选必选说明：该参数在"IPVERSION"配置为"IPv6"时为条件必选参数。<br>参数含义：该参数用于指定网关IPv6地址。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：<br>网关地址必须与平面内的端口IP同网段。可以通过<br>[**DSP PAEPORTINFO**](../端口/显示PAE端口基本信息（DSP PAEPORTINFO）_92520040.md)<br>命令查看。 |
| IPV6PREFIXLEN | IPv6地址前缀 | 可选必选说明：该参数在"IPVERSION"配置为"IPv6"时为条件必选参数。<br>参数含义：该参数用于指定网关IPv6地址前缀。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~127。<br>默认值：无<br>配置原则：无 |
| DESC | 描述 | 可选必选说明：可选参数<br>参数含义：该参数用于描述逻辑IP地址的其他信息。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PAEPORTGATEWAY]] · PAE端口网关信息（PAEPORTGATEWAY）

## 使用实例

修改网段索引为1，平面ID为0的内联口的IPv4网关地址为192.168.1.1，且该网关地址的掩码为255.255.0.0：

```
MOD PAEPORTGATEWAY: NETWORKINDEX=1, PLANEID=0, IPVERSION=IPv4, GATEWAYIPV4="192.168.1.1", IPV4MASK="255.255.0.0";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改网关转发地址（MOD-PAEPORTGATEWAY）_98683661.md`
