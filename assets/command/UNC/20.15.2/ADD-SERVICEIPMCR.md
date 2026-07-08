---
id: UNC@20.15.2@MMLCommand@ADD SERVICEIPMCR
type: MMLCommand
name: ADD SERVICEIPMCR（增加业务IP）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: SERVICEIPMCR
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- MME链式备份管理
- 业务IP管理
- 业务IP
status: active
---

# ADD SERVICEIPMCR（增加业务IP）

## 功能

**适用网元：MME**

该命令用于配置业务IP地址。

- 命令[**ADD SDAPLE**](../../Sdup接口管理/Sdup接口业务地址管理/增加SDAP本地实体(ADD SDAPLE)_26147290.md)中的使用的地址或本端地址都必须引用该业务IP地址。不同的业务允许使用同一个业务IP地址，也允许使用不同的业务IP地址。
- 命令使用的VPN必须引用业务IP所属VPN实例。

## 注意事项

- 该命令配置后立即生效。
- 整系统最大允许配置100个业务IP地址。
- 整系统最大允许配置20个VPN实例。
- 一个业务IP地址，只能属于一个VPN实例。多个业务IP地址，可以同属于一个VPN实例。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPVERSION | IP版本 | 可选必选说明：必选参数<br>参数含义：IP版本。<br>数据来源：本端规划<br>取值范围：<br>- "IPv4(IPv4地址)"<br>- "IPv6(IPv6地址)"<br>默认值：IPv4<br>配置原则：<br>- 根据选择的IP版本，输入相应格式的IP地址。 |
| SERVICEIPV4 | 业务IPv4地址 | 可选必选说明：条件必选参数<br>参数含义：该参数用于配置业务IPv4地址。<br>前提条件：该参数在<br>“IP版本”<br>配置为<br>“IPv4(IPv4地址)”<br>后生效。<br>数据来源：全网规划<br>取值范围：0.0.0.0~255.255.255.255<br>默认值：无<br>配置原则：<br>- 业务地址不能配置为0.0.0.0、255.255.255.255和环回地址(127.x.y.z)。<br>- 业务地址必须是A、B或者C类地址。<br>- 该参数的掩码缺省为255.255.255.255，不可更改。 |
| SERVICEIPV6 | 业务IPv6地址 | 可选必选说明：条件必选参数<br>参数含义：该参数用于配置业务IPv6地址。<br>前提条件：该参数在<br>“IP版本”<br>配置为<br>“IPv6(IPv6地址)”<br>后生效。<br>数据来源：全网规划<br>取值范围：::~FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无<br>配置原则：<br>- IPv6地址必须是全球单播地址，不能为::、FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址(::1/128)、链路本地地址(FE80::/10)和组播地址(FF00::/8)。<br>- 该参数的掩码缺省为FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF，不可更改。 |
| IPV6MTU | IPv6 MTU大小 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定IP层协议为IPv6时使用的MTU大小。<br>前提条件：该参数在“IP版本”参数配置为“IPv6地址”后生效。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1280～65534。<br>默认值：1500 |
| VPNINSTNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：业务IP所属的VPN实例名称。<br>数据来源：本端规划<br>取值范围：1~31位字符串<br>默认值：无<br>配置原则：<br>- 此VPN实例名称需要与VNRS的VPN实例名称统一规划。<br>- 一个业务IP只能属于一个VPN实例。<br>- 最后一个字符不能配置为“\”。 |
| DESC | 描述 | 可选必选说明：可选参数<br>参数含义：该参数用于描述业务IP地址的其他信息。<br>数据来源：本端规划<br>取值范围：1~32位字符串<br>默认值：无 |

## 操作的配置对象

- [业务IP（SERVICEIPMCR）](configobject/UNC/20.15.2/SERVICEIPMCR.md)

## 使用实例

1. 配置IP版本号为 “IPV4” ，业务IPv4地址为“192.168.52.1”，VPN实例名称为 “_abc_” ，描述为 “for command sdaple”
  ADD SERVICEIPMCR: IPVERSION=IPv4, SERVICEIPV4="192.168.52.1", VPNINSTNAME="_abc_", DESC="for command sdaple";
2. 配置IP版本号为 “IPV6” ，业务IPv6地址为“2001:db8:10:19:44:55:10:12”，IPv6 MTU大小为 “1600” ，VPN实例名称为 “_abc_” ，描述为 “for command sdaple IPv6”
  ADD SERVICEIPMCR: IPVERSION=IPv6, SERVICEIPV6="2001:db8:10:19:44:55:10:12", IPV6MTU=1600, VPNINSTNAME="_abc_", DESC="for command sdaple IPv6";

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加业务IP(ADD-SERVICEIPMCR)_71731081.md`
