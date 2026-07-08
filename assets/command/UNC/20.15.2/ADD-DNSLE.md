---
id: UNC@20.15.2@MMLCommand@ADD DNSLE
type: MMLCommand
name: ADD DNSLE（增加DNS实体绑定DNS Client IP）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: DNSLE
command_category: 配置类
applicable_nf:
- SGSN
- MME
- AMF
effect_mode: 立即生效
is_dangerous: false
max_records: 32
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- GTP-C接口管理
- DNS
- DNS本端实体管理
status: active
---

# ADD DNSLE（增加DNS实体绑定DNS Client IP）

## 功能

**适用网元：SGSN、MME** **、AMF**

该命令用于增加DNS本端实体，包括：IP地址、端口、VPN名称，以便和DNS服务器进行通信。

## 注意事项

- 该命令执行后立即生效。
- 本表最大记录数为32条。
- DNSLE配置不包含传输层协议类型，对应的传输层类型由[**ADD DNSS**](../DNS服务器管理/增加DNS服务器(ADD DNSS)_72345497.md)的参数“DNS服务器承载协议”配置。只有通过[**ADD DNSS**](../DNS服务器管理/增加DNS服务器(ADD DNSS)_72345497.md)添加了至少一个DNS服务器后，用[**ADD DNSLE**](增加DNS实体绑定DNS Client IP(ADD DNSLE)_72225567.md)增加的DNS本端实体才能起作用。
- IP地址和vpn名称必须在SERVICEIP表中已经配置，可以用[**LST SERVICEIP**](../../../业务IP管理/业务IP/查询业务IP(LST SERVICEIP)_72226047.md)查询。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPT | IP地址类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定IP地址类型。<br>数据来源：整网规划<br>取值范围：<br>- “IPV4(IPV4)”<br>- “IPV6(IPV6)”<br>默认值：无 |
| IPV4 | IPv4地址 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定IPv4地址。<br>前提条件：当<br>“IP地址类型”<br>设置为<br>“IPV4(IPV4)”<br>时，该参数有效。<br>数据来源：整网规划<br>取值范围：0.0.0.0～255.255.255.255<br>默认值：无<br>配置原则：<br>- IPv4地址不能为组播地址（224.x.y.z）和环回地址(127.x.y.z)。<br>- IPv4地址必须是A、B或者C类地址。<br>- 该参数不能配置为如下IP地址：- xxx.xxx.xxx.0<br>- xxx.xxx.xxx.255 |
| IPV6 | IPv6地址 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定IPv6地址。<br>前提条件：当<br>“IP地址类型”<br>设置为<br>“IPV6(IPV6)”<br>时，该参数有效。<br>数据来源：整网规划<br>取值范围：::～FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无<br>配置原则：IPv6地址必须是全球单播地址，不能为::、FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址(::1)、链路本地地址(FE80::/10)和组播地址(FF00::/8)。 |
| LOCPORT | 本地端口号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定本端端口号。<br>数据来源：整网规划<br>取值范围：15000~65535<br>默认值：无 |
| VPNNAME | VPN名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定DNS本端实体到DNS服务器间的链路所用的VPN名称。<br>数据来源：整网规划<br>取值范围：0~31个字符。<br>默认值：无 |
| LENAME | DNS本端实体名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定DNS本端实体的名称。<br>数据来源：整网规划<br>取值范围：0~32个字符。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/DNSLE]] · DNS Client IP与DNS实体的绑定关系（DNSLE）

## 使用实例

添加DNS本端实体：IP地址 192.168.97.26；端口15001；VPN名称 _abc_；DNS本端实体名称Dnsle26。

ADD DNSLE:IPT=IPV4,IPV4="192.168.97.26",LOCPORT=15001,VPNNAME="_abc_",LENAME="Dnsle26";

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加DNS实体绑定DNS-Client-IP(ADD-DNSLE)_72225567.md`
