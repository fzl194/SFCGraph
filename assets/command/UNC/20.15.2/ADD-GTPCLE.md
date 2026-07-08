---
id: UNC@20.15.2@MMLCommand@ADD GTPCLE
type: MMLCommand
name: ADD GTPCLE（增加GTP-C本地实体）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: GTPCLE
command_category: 配置类
applicable_nf:
- SGSN
- MME
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- GTP-C接口管理
- Gtpc本端实体管理
status: active
---

# ADD GTPCLE（增加GTP-C本地实体）

## 功能

**适用网元：SGSN、MME、AMF**

本命令用于增加GTPC本端实体。

本命令与 [**ADD GTPCINTFATTR**](../GTP-C接口类型属性/增加GTP-C IP地址接口属性(ADD GTPCINTFATTR)_72225579.md) 命令组合，满足各种GTPC接口的组网部署。

## 注意事项

- 本命令执行后立即生效。
- 系统最多支持256个GTPC本端实体记录。
- GTPC本端实体最多支持32个不同的IPv4，以及32个不同的IPv6地址。
- 不同组号内的IP地址允许相同，同一个组号内的IP地址不允许相同。
- 一个组号下最多支持8个IPv4地址，以及8个IPv6地址。
- IP地址和vpn名称必须在SERVICEIP表中已经配置，可以用[**LST SERVICEIP**](../../业务IP管理/业务IP/查询业务IP(LST SERVICEIP)_72226047.md)查询。
- IP地址不能与GTPCLEGRPMEM中已配置的IP地址相同。
- 当AMF的N26接口部署模式为融合部署模式时，该命令适用于AMF。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GROUPID | 组号 | 可选必选说明：可选参数<br>参数含义：本参数用于指定GTPC本端实体对应的组号。组号用于组网规划时不同接口，或者不同用户范围使用独立的GTPC本端实体。<br>数据来源：本端规划<br>取值范围：0~32<br>默认值：0<br>说明：- 如果添加非0组号GTPC本端实体，则需要同步增加[**ADD GTPCINTFATTR**](../GTP-C接口类型属性/增加GTP-C IP地址接口属性(ADD GTPCINTFATTR)_72225579.md)配置。<br>- 组号的应用参考[**ADD GTPCINTFATTR**](../GTP-C接口类型属性/增加GTP-C IP地址接口属性(ADD GTPCINTFATTR)_72225579.md)命令帮助。 |
| IPTYPE | IP地址类型 | 可选必选说明：必选参数<br>参数含义：本参数用于指定GTPC本端实体的IP地址类型。<br>数据来源：全网规划<br>取值范围：<br>- “TPTADDR_TYPE_IPV4(IPv4)”<br>- “TPTADDR_TYPE_IPV6(IPv6)”<br>默认值：无 |
| LEIPV4 | IPv4地址 | 可选必选说明：条件必选参数<br>参数含义：本参数用于指定GTPC本端实体的IPv4地址。<br>前提条件：该参数在<br>“IP地址类型”<br>参数配置为<br>“TPTADDR_TYPE_IPV4(IPv4)”<br>后生效。<br>数据来源：全网规划<br>取值范围：0.0.0.0~255.255.255.255<br>默认值：无<br>配置原则：<br>- 业务地址不能配置为0.0.0.0、255.255.255.255和环回地址(127.x.y.z)。<br>- 业务地址必须是A、B或者C类地址。<br>- 如果添加的地址和CHGCDPIP对象的IP地址相同，且IP地址对应的CHGCDPIP对象记录中端口范围包含3386，则不允许添加，可以用[**LST CHGCDPIP**](../../../计费管理/CDPIP 配置/查询计费相关的IP配置参数(LST CHGCDPIP)_72225041.md)查询。<br>- IP地址不能与GTPCLEGRPMEM中已配置的IP地址相同。 |
| LEIPV6 | IPv6地址 | 可选必选说明：条件必选参数<br>参数含义：本参数用于指定GTPC本端实体的IPv6地址。<br>前提条件：该参数在<br>“IP地址类型”<br>参数配置为<br>“TPTADDR_TYPE_IPV6(IPv6)”<br>后生效。<br>数据来源：全网规划<br>取值范围：::~FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无<br>配置原则：<br>- IPv6地址必须是全球单播地址，不能为::、FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址(::1)、链路本地地址(FE80::/10)和组播地址(FF00::/8)。<br>- IP地址不能与GTPCLEGRPMEM中已配置的IP地址相同。 |
| VPNNAME | VPN名称 | 可选必选说明：可选参数<br>参数含义：本参数用于指定GTPC本端实体对应的VPN名称。<br>数据来源：全网规划<br>取值范围：0~31位字符串<br>默认值：无 |
| DESC | 描述信息 | 可选必选说明：可选参数<br>参数含义：本参数用于指定描述信息。<br>数据来源：本端规划<br>取值范围：0~32位字符串<br>默认值：无 |

## 操作的配置对象

- [GTP-C本地实体（GTPCLE）](configobject/UNC/20.15.2/GTPCLE.md)

## 使用实例

增加IP为192.168.1.1的本地实体：

ADD GTPCLE: GROUPID=0, IPTYPE=TPTADDR_TYPE_IPV4, LEIPV4="192.168.1.1";

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加GTP-C本地实体(ADD-GTPCLE)_26145966.md`
