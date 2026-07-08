# 删除业务IP(RMV SERVICEIPMCR)

- [命令功能](#ZH-CN_MMLREF_0000001125291194__1.3.1.1)
- [注意事项](#ZH-CN_MMLREF_0000001125291194__1.3.2.1)
- [本地用户权限](#ZH-CN_MMLREF_0000001125291194__1.3.3.1)
- [网管用户权限](#ZH-CN_MMLREF_0000001125291194__1.3.4.1)
- [参数说明](#ZH-CN_MMLREF_0000001125291194__1.3.5.1)
- [使用实例](#ZH-CN_MMLREF_0000001125291194__1.3.6.1)

#### [命令功能](#ZH-CN_MMLREF_0000001125291194)

**适用网元：MME**

该命令用于删除业务IP地址。

#### [注意事项](#ZH-CN_MMLREF_0000001125291194)

- 该命令执行后立即生效。
- 如果要删除的业务IP地址已经被命令[**ADD SDAPLE**](../../Sdup接口管理/Sdup接口业务地址管理/增加SDAP本地实体(ADD SDAPLE)_26147290.md)引用，需要先通过[**RMV SDAPLE**](../../Sdup接口管理/Sdup接口业务地址管理/删除SDAP本地实体(RMV SDAPLE)_72226967.md)命令删除业务，然后再执行此命令。

#### [本地用户权限](#ZH-CN_MMLREF_0000001125291194)

manage-ug；system-ug

#### [网管用户权限](#ZH-CN_MMLREF_0000001125291194)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_MMLREF_0000001125291194)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPVERSION | IP版本 | 可选必选说明：必选参数<br>参数含义：该参数用于指定需要删除的业务IP的IP版本。<br>数据来源：本端规划<br>取值范围：<br>- “IPv4(IPv4地址)”<br>- “IPv6(IPv6地址)”<br>默认值：IPv4<br>配置原则：<br>- 根据选择的IP版本，输入相应格式的IP地址。 |
| SERVICEIPV4 | 业务IPv4地址 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定需要删除的业务IPv4地址。<br>前提条件：该参数在<br>“IP版本”<br>配置为<br>“IPv4(IPv4地址)”<br>后生效。<br>数据来源：全网规划<br>取值范围：0.0.0.0~255.255.255.255<br>默认值：无<br>配置原则：<br>- 业务地址不能配置为0.0.0.0、255.255.255.255和环回地址(127.x.y.z)。<br>- 业务地址必须是A、B或者C类地址。<br>- 该参数的掩码缺省为255.255.255.255，不可更改。 |
| SERVICEIPV6 | 业务IPv6地址 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定需要删除的业务IPv6地址。<br>前提条件：该参数在<br>“IP版本”<br>配置为<br>“IPv6(IPv6地址)”<br>后生效。<br>数据来源：全网规划<br>取值范围：::~FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无<br>配置原则：<br>- IPv6地址必须是全球单播地址，不能为::、FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址(::1/128)、链路本地地址(FE80::/10)和组播地址(FF00::/8)。<br>- 该参数的掩码缺省为FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF，不可更改。 |
| VPNINSTNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定需要删除的业务IP所属的VPN实例名称。<br>数据来源：本端规划<br>取值范围：1~31位字符串<br>默认值：无<br>配置原则：<br>- 此VPN实例名称需要与VNRS的VPN实例名称统一规划。<br>- 不指定VPN实例名称则默认业务IP所属的VPN为公网VPN"_public_"<br>- 一个业务IP只能属于一个VPN实例。<br>- 若VPN非"_public_"必须输入实际VPNINSTNAME参数。 |

#### [使用实例](#ZH-CN_MMLREF_0000001125291194)

删除IP版本号为IPV4，业务IPv4地址为192.168.52.1，VPN实例名称为_abc_

RMV SERVICEIPMCR: IPVERSION=IPv4, SERVICEIPV4="192.168.52.1", VPNINSTNAME="_abc_";
