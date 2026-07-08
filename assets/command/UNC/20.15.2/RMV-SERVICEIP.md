---
id: UNC@20.15.2@MMLCommand@RMV SERVICEIP
type: MMLCommand
name: RMV SERVICEIP（删除业务IP）
nf: UNC
version: 20.15.2
verb: RMV
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

# RMV SERVICEIP（删除业务IP）

## 功能

**适用NF：SGSN、MME、AMF**

该命令用于删除业务IP地址。

## 注意事项

- 该命令执行后立即生效。
- 如果要删除的业务IP地址已经被命令[**ADD S1APLE**](../../S1接口管理/S1AP本地实体/增加S1AP本地实体(ADD S1APLE)_26146254.md)、[**ADD DMLNK**](../../信令传输管理/Diameter管理/Diameter链路/增加Diameter链路配置(ADD DMLNK)_72225953.md)、[**ADD M3LNK**](../../信令传输管理/M3UA管理/M3UA链路/增加M3UA信令链路(ADD M3LNK)_72225983.md)、[**ADD GTPCLE**](../../GTP-C接口管理/Gtpc本端实体管理/增加GTP-C本地实体(ADD GTPCLE)_26145966.md)、[**ADD SGSLNK**](../../电路域联合业务/SGSAP/SGsAP链路管理/增加SGs链路(ADD SGSLNK)_72345031.md)、[**ADD GTPULE**](../../GTP-U接口管理/Gtpu本端实体管理/增加GTP-U本地实体(ADD GTPULE)_72345581.md)、[**ADD DNSLE**](../../GTP-C接口管理/DNS/DNS本端实体管理/增加DNS实体绑定DNS Client IP(ADD DNSLE)_72225567.md)、[**ADD GBEPPOOL**](../../Gb接口管理/Gb自动配置管理/Gb地址池管理/增加IP地址到地址池(ADD GBEPPOOL)_26145998.md)、[**ADD GBIPLOCENDPT**](../../Gb接口管理/Gb over IP管理/本端IP端点配置/增加本端端点配置(ADD GBIPLOCENDPT)_72225689.md)、[**ADD CHGCDPIP**](../../../计费管理/CDPIP 配置/增加计费相关的IP配置参数(ADD CHGCDPIP)_72344961.md)、[**ADD LCSAPLNK**](../../业务安全管理/LCS/LCSAP链路配置/增加LCSAP链路配置(ADD LCSAPLNK)_72345407.md)、[**ADD SBCAPLE**](../../SBc接口管理/SBCAP本地实体/增加SBCAP本地实体(ADD SBCAPLE)_72226055.md)、[**ADD SBCAPLNK**](../../SBc接口管理/SBc链路/增加SBc链路(ADD SBCAPLNK)_72345973.md)、 [**ADD SCTPLE**](../../S1接口管理/SCTP本地实体/增加SCTP本地实体(ADD SCTPLE)_11295747.md)引用，需要先通过[**RMV S1APLE**](../../S1接口管理/S1AP本地实体/删除S1AP本地实体(RMV S1APLE)_26306066.md)、[**RMV DMLNK**](../../信令传输管理/Diameter管理/Diameter链路/删除Diameter链路配置(RMV DMLNK)_26306086.md)、[**RMV M3LNK**](../../信令传输管理/M3UA管理/M3UA链路/删除M3UA信令链路(RMV M3LNK)_26306116.md)、[**RMV GTPCLE**](../../GTP-C接口管理/Gtpc本端实体管理/删除GTP-C本地实体(RMV GTPCLE)_72225645.md)、[**RMV SGSLNK**](../../电路域联合业务/SGSAP/SGsAP链路管理/删除SGs链路(RMV SGSLNK)_26145430.md)、[**RMV GTPULE**](../../GTP-U接口管理/Gtpu本端实体管理/删除GTP-U本地实体(RMV GTPULE)_26145982.md)、[**RMV DNSLE**](../../GTP-C接口管理/DNS/DNS本端实体管理/删除DNS Client IP与DNS实体的绑定关系(RMV DNSLE)_26305698.md)、[**RMV GBEPPOOL**](../../Gb接口管理/Gb自动配置管理/Gb地址池管理/删除地址池中IP地址(RMV GBEPPOOL)_72225677.md)、[**RMV GBIPLOCENDPT**](../../Gb接口管理/Gb over IP管理/本端IP端点配置/删除本端端点配置(RMV GBIPLOCENDPT)_26305820.md)、[**RMV CHGCDPIP**](../../../计费管理/CDPIP 配置/删除计费相关的IP配置参数(RMV CHGCDPIP)_26145360.md)、[**RMV LCSAPLNK**](../../业务安全管理/LCS/LCSAP链路配置/删除LCSAP链路配置(RMV LCSAPLNK)_26145808.md)、[**RMV SBCAPLE**](../../SBc接口管理/SBCAP本地实体/删除SBCAP本地实体(RMV SBCAPLE)_26306188.md)、[**RMV SBCAPLNK**](../../SBc接口管理/SBc链路/删除SBc链路(RMV SBCAPLNK)_26146374.md)、[**RMV SCTPLE**](../../S1接口管理/SCTP本地实体/删除SCTP本地实体(RMV SCTPLE)_11295837.md)命令删除业务，然后再执行此命令。
- 如果要删除的业务IP所属VPN实例已经被命令引用，且该VPN实例下仅有一条业务IP，需要先通过命令删除重定向配置记录，然后再执行此命令。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPVERSION | IP版本 | 可选必选说明：必选参数<br>参数含义：该参数用于指定需要删除的业务IP的IP版本。<br>数据来源：本端规划<br>取值范围：<br>- "IPv4(IPv4地址)"<br>- "IPv6(IPv6地址)"<br>默认值：IPv4(IPv4地址)<br>配置原则：<br>- 根据选择的IP版本，输入相应格式的IP地址。 |
| SERVICEIPV4 | 业务IPv4地址 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定需要删除的业务IPv4地址。<br>前提条件：该参数在<br>“IP版本”<br>配置为<br>“IPv4(IPv4地址)”<br>后生效。<br>数据来源：全网规划<br>取值范围：0.0.0.0~255.255.255.255<br>默认值：无<br>配置原则：<br>- 业务地址不能配置为0.0.0.0、255.255.255.255和环回地址(127.x.y.z)。<br>- 业务地址必须是A、B或者C类地址。<br>- 该参数的掩码缺省为255.255.255.255，不可更改。 |
| SERVICEIPV6 | 业务IPv6地址 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定需要删除的业务IPv6地址。<br>前提条件：该参数在<br>“IP版本”<br>配置为<br>“IPv6(IPv6地址)”<br>后生效。<br>数据来源：全网规划<br>取值范围：::~FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无<br>配置原则：<br>- IPv6地址必须是全球单播地址，不能为::、FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址(::1)、链路本地地址(FE80::/10)和组播地址(FF00::/8)。<br>- 该参数的掩码缺省为FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF，不可更改。 |
| VPNINSTNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定需要删除的业务IP所属的VPN实例名称。<br>数据来源：本端规划<br>取值范围：1~31位字符串<br>默认值：无<br>配置原则：<br>- 本参数需要与[**ADD L3VPNINST**](../../../../../平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例/增加L3VPN实例（ADD L3VPNINST）_49802446.md)命令中的**VPN实例名称**保持一致。<br>- 不指定VPN实例名称则默认业务IP所属的VPN为公网VPN"_public_"。<br>- 一个业务IP只能属于一个VPN实例。<br>- 若VPN非"_public_"必须输入实际VPNINSTNAME参数。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SERVICEIP]] · 业务IP（SERVICEIP）

## 使用实例

删除IP版本号为IPV4，业务IPv4地址为192.168.52.1，VPN实例名称为_abc_

RMV SERVICEIP: IPVERSION=IPv4, SERVICEIPV4="192.168.52.1", VPNINSTNAME="_abc_";

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除业务IP(RMV-SERVICEIP)_72345967.md`
