---
id: UNC@20.15.2@MMLCommand@ADD SERVICEIP
type: MMLCommand
name: ADD SERVICEIP（增加业务IP）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: SERVICEIP
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
- 业务IP管理
- 业务IP
status: active
---

# ADD SERVICEIP（增加业务IP）

## 功能

**适用NF：SGSN、MME、AMF**

该命令用于配置业务IP地址。

- 命令[**ADD S1APLE**](../../S1接口管理/S1AP本地实体/增加S1AP本地实体(ADD S1APLE)_26146254.md)、[**ADD DMLNK**](../../信令传输管理/Diameter管理/Diameter链路/增加Diameter链路配置(ADD DMLNK)_72225953.md)、[**ADD M3LNK**](../../信令传输管理/M3UA管理/M3UA链路/增加M3UA信令链路(ADD M3LNK)_72225983.md)、[**ADD GTPCLE**](../../GTP-C接口管理/Gtpc本端实体管理/增加GTP-C本地实体(ADD GTPCLE)_26145966.md)、[**ADD SGSLNK**](../../电路域联合业务/SGSAP/SGsAP链路管理/增加SGs链路(ADD SGSLNK)_72345031.md)、[**ADD GTPULE**](../../GTP-U接口管理/Gtpu本端实体管理/增加GTP-U本地实体(ADD GTPULE)_72345581.md)、[**ADD DNSLE**](../../GTP-C接口管理/DNS/DNS本端实体管理/增加DNS实体绑定DNS Client IP(ADD DNSLE)_72225567.md)、[**ADD GBEPPOOL**](../../Gb接口管理/Gb自动配置管理/Gb地址池管理/增加IP地址到地址池(ADD GBEPPOOL)_26145998.md)、[**ADD GBIPLOCENDPT**](../../Gb接口管理/Gb over IP管理/本端IP端点配置/增加本端端点配置(ADD GBIPLOCENDPT)_72225689.md)、[**ADD CHGCDPIP**](../../../计费管理/CDPIP 配置/增加计费相关的IP配置参数(ADD CHGCDPIP)_72344961.md)、[**ADD LCSAPLNK**](../../业务安全管理/LCS/LCSAP链路配置/增加LCSAP链路配置(ADD LCSAPLNK)_72345407.md)、[**ADD SBCAPLE**](../../SBc接口管理/SBCAP本地实体/增加SBCAP本地实体(ADD SBCAPLE)_72226055.md)、[**ADD SBCAPLNK**](../../SBc接口管理/SBc链路/增加SBc链路(ADD SBCAPLNK)_72345973.md)、[**ADD SCTPLE**](../../S1接口管理/SCTP本地实体/增加SCTP本地实体(ADD SCTPLE)_11295747.md)中的使用的地址或本端地址都必须引用该业务IP地址。不同的业务允许使用同一个业务IP地址，也允许使用不同的业务IP地址。
- 命令使用的VPN必须引用业务IP所属VPN实例。

## 注意事项

- 该命令配置后立即生效。
- 整系统最大允许配置1024个业务IP地址。
- 整系统最大允许配置200个VPN实例。
- 一个业务IP地址，只能属于一个VPN实例。多个业务IP地址，可以同属于一个VPN实例。
- UNC不支持IPV6以下格式地址下发：0:0:0:0:0:FFFF:X.X.X.X和::FFFF:X.X.X.X/96、0:0:0:0:0:0:X.X.X.X和::X.X.X.X/96、2002:X.X.X.X:0:0:0:0:0和2002:X.X.X.X::/48。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPVERSION | IP版本 | 可选必选说明：必选参数<br>参数含义：IP版本。<br>数据来源：本端规划<br>取值范围：<br>- “IPv4(IPv4地址)”<br>- “IPv6(IPv6地址)”<br>默认值：“IPv4(IPv4地址)”<br>配置原则：根据选择的IP版本，输入相应格式的IP地址。 |
| SERVICEIPV4 | 业务IPv4地址 | 可选必选说明：条件必选参数<br>参数含义：该参数用于配置业务IPv4地址。<br>前提条件：该参数在<br>“IP版本”<br>配置为<br>“IPv4(IPv4地址)”<br>后生效。<br>数据来源：全网规划<br>取值范围：0.0.0.0～255.255.255.255<br>默认值：无<br>配置原则：<br>- 业务地址不能配置为0.0.0.0、255.255.255.255和环回地址(127.x.y.z)。<br>- 业务地址必须是A、B或者C类地址。<br>- 该参数的掩码缺省为255.255.255.255，不可更改。 |
| SERVICEIPV6 | 业务IPv6地址 | 可选必选说明：条件必选参数<br>参数含义：该参数用于配置业务IPv6地址。<br>前提条件：该参数在<br>“IP版本”<br>配置为<br>“IPv6(IPv6地址)”<br>后生效。<br>数据来源：全网规划<br>取值范围：::～FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无<br>配置原则：<br>- IPv6地址必须是全球单播地址，不能为::、FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址(::1)、链路本地地址(FE80::/10)和组播地址(FF00::/8)。<br>- 该参数的掩码缺省为FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF，不可更改。 |
| IPV6MTU | IPv6 MTU大小 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定IP层协议为IPv6时使用的MTU大小。<br>前提条件：该参数在<br>“IP版本”<br>参数配置为<br>“IPv6地址”<br>后生效。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1280～65534。<br>默认值：1500 |
| VPNINSTNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：业务IP所属的VPN实例名称。<br>数据来源：本端规划<br>取值范围：1～31位字符串<br>默认值：无<br>配置原则：<br>- 本参数需要与[**ADD L3VPNINST**](../../../../../平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例/增加L3VPN实例（ADD L3VPNINST）_49802446.md)命令中的**VPN实例名称**保持一致。<br>- 不指定VPN实例名称则默认业务IP所属的VPN为公网VPN“_public_”。<br>- 一个业务IP只能属于一个VPN实例。<br>- 最后一个字符不能配置为“\”。 |
| DESC | 描述 | 可选必选说明：可选参数<br>参数含义：该参数用于描述业务IP地址的其他信息。<br>数据来源：本端规划<br>取值范围：1～32位字符串<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SERVICEIP]] · 业务IP（SERVICEIP）

## 使用实例

1. 配置IP版本号为 “IPV4” ，业务IPv4地址为“192.168.52.1”，VPN实例名称为 “_abc_” ，描述为 “for command gtpule”
  ADD SERVICEIP: IPVERSION=IPv4, SERVICEIPV4="192.168.52.1", VPNINSTNAME="_abc_", DESC="for command gtpule";
2. 配置IP版本号为 “IPV6” ，业务IPv6地址为“2001:db8:10:19:44:55:10:12”，IPv6 MTU大小为 “1600” ，VPN实例名称为 “_abc_” ，描述为 “for command gtpule IPv6”
  ADD SERVICEIP: IPVERSION=IPv6, SERVICEIPV6="2001:db8:10:19:44:55:10:12", IPV6MTU=1600, VPNINSTNAME="_abc_", DESC="for command gtpule IPv6";

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-SERVICEIP.md`
