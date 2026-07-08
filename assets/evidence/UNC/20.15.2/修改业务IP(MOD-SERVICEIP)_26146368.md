# 修改业务IP(MOD SERVICEIP)

- [命令功能](#ZH-CN_MMLREF_0000001126146368__1.3.1.1)
- [注意事项](#ZH-CN_MMLREF_0000001126146368__1.3.2.1)
- [本地用户权限](#ZH-CN_MMLREF_0000001126146368__1.3.3.1)
- [网管用户权限](#ZH-CN_MMLREF_0000001126146368__1.3.4.1)
- [参数说明](#ZH-CN_MMLREF_0000001126146368__1.3.5.1)
- [使用实例](#ZH-CN_MMLREF_0000001126146368__1.3.6.1)

#### [命令功能](#ZH-CN_MMLREF_0000001126146368)

**适用NF：SGSN、MME、AMF**

该命令用于修改已配置业务IP地址的相关参数。

#### [注意事项](#ZH-CN_MMLREF_0000001126146368)

- 该命令执行后立即生效。
- 该命令不能修改业务IP与VPN实例的所属关系。当IP版本选择为IPv4时，只能修改业务IP的描述信息，当IP版本选择为IPv6时，只能修改业务IP的描述信息和IPv6 MTU大小。

#### [本地用户权限](#ZH-CN_MMLREF_0000001126146368)

manage-ug；system-ug

#### [网管用户权限](#ZH-CN_MMLREF_0000001126146368)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_MMLREF_0000001126146368)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPVERSION | IP版本 | 可选必选说明：必选参数<br>参数含义：该参数用于指定需要修改描述信息的业务IP的IP版本。<br>数据来源：本端规划<br>取值范围：<br>- “IPv4(IPv4地址)”<br>- “IPv6(IPv6地址)”<br>默认值：无<br>配置原则：根据选择的IP版本，输入相应格式的IP地址。 |
| SERVICEIPV4 | 业务IPv4地址 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定需要修改描述信息的业务IPv4地址。<br>前提条件：该参数在<br>“IP版本”<br>配置为<br>“IPv4(IPv4地址)”<br>后生效。<br>数据来源：全网规划<br>取值范围：0.0.0.0～255.255.255.255<br>默认值：无<br>配置原则：<br>- 业务地址不能配置为0.0.0.0、255.255.255.255和环回地址(127.x.y.z)。<br>- 业务地址必须是A、B或者C类地址。<br>- 该参数的掩码缺省为255.255.255.255，不可更改。 |
| SERVICEIPV6 | 业务IPv6地址 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定需要修改描述信息的业务IPv6地址。<br>前提条件：该参数在<br>“IP版本”<br>配置为<br>“IPv6(IPv6地址)”<br>后生效。<br>数据来源：全网规划<br>取值范围：::～FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无<br>配置原则：<br>- IPv6地址必须是全球单播地址，不能为::、FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址(::1)、链路本地地址(FE80::/10)和组播地址(FF00::/8)。<br>- 该参数的掩码缺省为FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF，不可更改。 |
| IPV6MTU | IPv6 MTU大小 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定IP层协议为IPv6时使用的MTU大小。<br>前提条件：该参数在<br>“IP版本”<br>参数配置为<br>“IPv6地址”<br>后生效。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1280～65534。<br>默认值：无 |
| VPNINSTNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定需要修改描述信息的业务IP所属的VPN实例名称。<br>数据来源：本端规划<br>取值范围：1～31位字符串<br>默认值：无<br>配置原则：<br>- 本参数需要与[**ADD L3VPNINST**](../../../../../平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例/增加L3VPN实例（ADD L3VPNINST）_49802446.md)命令中的**VPN实例名称**保持一致。<br>- 不指定VPN实例名称则默认业务IP所属的VPN为公网VPN“_public_”。<br>- 一个业务IP只能属于一个VPN实例。<br>说明：使用<br>[**MOD SERVICEIP**](修改业务IP(MOD SERVICEIP)_26146368.md)<br>命令修改一条记录时，如果使用<br>[**LST SERVICEIP**](查询业务IP(LST SERVICEIP)_72226047.md)<br>查询该条记录的<br>“VPN实例名称”<br>不为NULL，则必须同时<br>“输入VPN实例名称”<br>才能对该条记录进行修改。 |
| DESC | 描述 | 可选必选说明：可选参数<br>参数含义：该参数用于修改业务IP的描述信息。<br>数据来源：本端规划<br>取值范围：1～32位字符串<br>默认值：无 |

#### [使用实例](#ZH-CN_MMLREF_0000001126146368)

1. 将IP版本号为 “IPV4” ，业务IPv4地址为"192.168.52.1"，VPN实例名称为 “_abc_” 的记录中描述修改为 “for command gtpule”
  MOD SERVICEIP: IPVERSION=IPv4, SERVICEIPV4="192.168.52.1", VPNINSTNAME="_abc_", DESC="for command gtpule";
2. 将IP版本号为 “IPV6” ，业务IPv6地址为"2001:db8:10:19:44:55:10:12"，IPv6 MTU大小为 “1800” ，VPN实例名称为 “_abc_” 的记录中描述修改为 “new for command gtpule IPv6”
  MOD SERVICEIP: IPVERSION=IPv6, SERVICEIPV6="2001:db8:10:19:44:55:10:12", IPV6MTU=1800, VPNINSTNAME="_abc_", DESC="new for command gtpule IPv6";
