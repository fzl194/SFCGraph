---
id: UNC@20.15.2@MMLCommand@MOD SERVICEIPMCR
type: MMLCommand
name: MOD SERVICEIPMCR（修改业务IP）
nf: UNC
version: 20.15.2
verb: MOD
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

# MOD SERVICEIPMCR（修改业务IP）

## 功能

**适用网元：MME**

该命令用于修改用户配置的业务IP的描述信息。

## 注意事项

- 该命令执行后立即生效。
- 该命令不能修改业务IP与VPN实例的所属关系。当IP版本选择为IPv4时，只能修改业务IP的描述信息，当IP版本选择为IPv6时，只能修改业务IP的描述信息和IPv6 MTU大小。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPVERSION | IP版本 | 可选必选说明：必选参数<br>参数含义：该参数用于指定需要修改描述信息的业务IP的IP版本。<br>数据来源：本端规划<br>取值范围：<br>- “IPv4(IPv4地址)”<br>- “IPv6(IPv6地址)”<br>默认值：无<br>配置原则：<br>- 根据选择的IP版本，输入相应格式的IP地址。 |
| SERVICEIPV4 | 业务IPv4地址 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定需要修改描述信息的业务IPv4地址。<br>前提条件：该参数在<br>“IP版本”<br>配置为<br>“IPv4(IPv4地址)”<br>后生效。<br>数据来源：全网规划<br>取值范围：0.0.0.0~255.255.255.255<br>默认值：无<br>配置原则：<br>- 业务地址不能配置为0.0.0.0、255.255.255.255和环回地址(127.x.y.z)。<br>- 业务地址必须是A、B或者C类地址。<br>- 该参数的掩码缺省为255.255.255.255，不可更改。 |
| SERVICEIPV6 | 业务IPv6地址 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定需要修改描述信息的业务IPv6地址。<br>前提条件：该参数在<br>“IP版本”<br>配置为<br>“IPv6(IPv6地址)”<br>后生效。<br>数据来源：全网规划<br>取值范围：::~FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无<br>配置原则：<br>- IPv6地址必须是全球单播地址，不能为::、FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址(::1/128)、链路本地地址(FE80::/10)和组播地址(FF00::/8)。<br>- 该参数的掩码缺省为FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF，不可更改。 |
| IPV6MTU | IPv6 MTU大小 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定IP层协议为IPv6时使用的MTU大小。<br>前提条件：该参数在“IP版本”参数配置为“IPv6地址”后生效。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1280～65534。<br>默认值：无 |
| VPNINSTNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定需要修改描述信息的业务IP所属的VPN实例名称。<br>数据来源：本端规划<br>取值范围：1~31位字符串<br>默认值：无<br>配置原则：<br>- 此VPN实例名称需要与VNRS的VPN实例名称统一规划。<br>- 一个业务IP只能属于一个VPN实例。 |
| DESC | 描述 | 可选必选说明：可选参数<br>参数含义：该参数用于修改业务IP的描述信息。<br>数据来源：本端规划<br>取值范围：1~32位字符串<br>默认值：无 |

## 操作的配置对象

- [业务IP（SERVICEIPMCR）](configobject/UNC/20.15.2/SERVICEIPMCR.md)

## 使用实例

1. 修改IP版本号为IPV4，业务IPv4地址为192.168.52.1，VPN实例名称为_abc_，描述为for command sdaple
  MOD SERVICEIPMCR: IPVERSION=IPv4, SERVICEIPV4="192.168.52.1", VPNINSTNAME="_abc_", DESC="for command sdaple";
2. 将IP版本号为“IPV6”，业务IPv6地址为"2001:db8:10:19:44:55:10:12"，IPv6 MTU大小为“1800”，VPN实例名称为“_abc_”的记录中描述修改为“new for command sdaple IPv6”
  MOD SERVICEIPMCR: IPVERSION=IPv6, SERVICEIPV6="2001:db8:10:19:44:55:10:12", IPV6MTU=1800, VPNINSTNAME="_abc_", DESC="new for command sdaple IPv6";

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改业务IP(MOD-SERVICEIPMCR)_71850997.md`
