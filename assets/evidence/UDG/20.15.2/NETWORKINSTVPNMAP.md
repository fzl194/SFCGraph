# 添加网络实例配置（ADD NETWORKINSTVPNMAP）

- [命令功能](#ZH-CN_CONCEPT_0000201478764775__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000201478764775__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000201478764775__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000201478764775__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000201478764775__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0000201478764775)

**适用NF：UPF**

该命令用于添加一个新的网络实例。在运营商需要在UPF上规划和DN侧连通域，配置NetworkInstance并绑定VPN时使用此命令进行配置。

#### [注意事项](#ZH-CN_CONCEPT_0000201478764775)

- 该命令执行后立即生效。
- 该命令最大记录数为1000。当配置记录数大于规格的98%时，会上报“ALM-135602215 配置数量超阈值”告警。当配置记录数小于等于配置规格95%时，恢复“ALM-135602215 配置数量超阈值”告警。阈值可以通过MOD CFGTHRESHOLD命令修改。
- 该配置可作为APN或者VPN使用，优先级低于APN和DNAI绑定的VPN。

#### [操作用户权限](#ZH-CN_CONCEPT_0000201478764775)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000201478764775)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NETWORKINSTANCE | 网络实例名称 | 可选必选说明：必选参数<br>参数含义：网络实例标识。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～100，单位是字节。由“_”、“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”，不区分大小写。<br>默认值：无<br>配置原则：无 |
| HASVPN | 绑定VPN | 可选必选说明：可选参数<br>参数含义：该参数用于指定是否绑定IPv4 VPN。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：DISABLE<br>配置原则：无 |
| VPNINSTANCE | VPN实例名 | 可选必选说明：条件必选参数<br>前提条件：该参数在“HASVPN”配置为“ENABLE”时为必选参数。<br>参数含义：该参数用于指定IPv4 VPN实例名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：无 |
| HASVPNIPV6 | 绑定IPv6 VPN | 可选必选说明：可选参数<br>参数含义：该参数用于指定是否绑定IPv6 VPN。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：DISABLE<br>配置原则：无 |
| VPNINSTANCEIPV6 | IPv6 VPN实例名 | 可选必选说明：条件必选参数<br>前提条件：该参数在“HASVPNIPV6”配置为“ENABLE”时为必选参数。<br>参数含义：该参数用于指定IPv6 VPN实例名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0000201478764775)

添加一个新的网络实例"net1"，配置networkInst和绑定VPN:"VPN2auto"：

```
ADD NETWORKINSTVPNMAP: NETWORKINSTANCE="net1", HASVPN=ENABLE, VPNINSTANCE="VPN2auto", HASVPNIPV6=DISABLE;
```
