# 修改非广播RAI配置信息(MOD NONRAI)

- [命令功能](#ZH-CN_MMLREF_0000001126146110__1.3.1.1)
- [注意事项](#ZH-CN_MMLREF_0000001126146110__1.3.2.1)
- [本地用户权限](#ZH-CN_MMLREF_0000001126146110__1.3.3.1)
- [网管用户权限](#ZH-CN_MMLREF_0000001126146110__1.3.4.1)
- [参数说明](#ZH-CN_MMLREF_0000001126146110__1.3.5.1)
- [使用实例](#ZH-CN_MMLREF_0000001126146110__1.3.6.1)

#### [命令功能](#ZH-CN_MMLREF_0000001126146110)

**适用网元：SGSN**

此命令用于修改本POOL区内非本SGSN的非广播RAI配置记录。

#### [注意事项](#ZH-CN_MMLREF_0000001126146110)

无。

#### [本地用户权限](#ZH-CN_MMLREF_0000001126146110)

manage-ug；system-ug

#### [网管用户权限](#ZH-CN_MMLREF_0000001126146110)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_MMLREF_0000001126146110)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NONRAI | 路由区标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定本POOL区内非本SGSN的非广播路由区标识。用于在迁移的时候，目的SGSN来识别MS是从哪个SGSN迁移过来的。一个非广播路由区标识可以唯一地标志一个SGSN。<br>数据来源：本端规划<br>取值范围：长度必须为11或者12位，前5或6位为十进制数，后6位为十六进制数的字符串<br>默认值：无<br>配置原则：NONRAI = LAI + RAC。LAI = MCC + MNC + LAC。MCC由3个阿拉伯数字组成，MNC由2到3个阿拉伯数字组成，LAC是十六进制数，占2个字节。RAC是十六进制数，占1个字节。 |
| IPTYPE | IP类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定IP类型。<br>数据来源：本端规划<br>取值范围：<br>- “IPV4(IPV4)”<br>- “IPV6(IPV6)”<br>- “IPV4V6(IPV4V6)”<br>默认值：无<br>配置原则：当没有设置IP类型时，SGSN信令面地址为无效值255.255.255.255。 |
| IPV4 | SGSN IPv4信令面地址 | 可选必选说明：条件必选参数<br>参数含义：该参数用于表示本POOL区内非本SGSN的信令面IPV4类型地址。<br>前提条件：当<br>“IP类型”<br>取值为<br>“IPV4(IPV4)”<br>或<br>“IPV4V6(IPV4V6)”<br>时，此参数有效。当<br>“IP类型”<br>取值为<br>“IPV4(IPV4)”<br>时，此参数为条件必选参数，<br>“IP类型”<br>取值为<br>“IPV4V6(IPV4V6)”<br>时，此参数为条件可选参数。<br>数据来源：本端规划<br>取值范围：0.0.0.0～255.255.255.255<br>默认值：无<br>配置原则：<br>当<br>“IP类型”<br>取值从<br>“IPV4(IPV4)”<br>或<br>“IPV6(IPV6)”<br>修改为<br>“IPV4V6(IPV4V6)”<br>时，此参数必须输入。 |
| IPV6 | SGSN IPv6信令面地址 | 可选必选说明：条件必选参数<br>参数含义：该参数用于表示本POOL区内非本SGSN的信令面IPV6类型地址。<br>前提条件：当<br>“IP类型”<br>取值为<br>“IPV6(IPV6)”<br>时，此参数有效。<br>数据来源：整网规划<br>取值范围：::～FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无<br>配置原则：<br>- IPv6地址必须是全球单播地址，不能为::、 FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址(::1)、链路本地地址(FE80::/10)和组播地址(FF00::/8)。 |
| ALTERNATIVE | SGSN IPv6信令面地址 | 可选必选说明：条件可选参数<br>参数含义：该参数用于表示本POOL区内非本SGSN的信令面IPV6类型地址。<br>前提条件：当<br>“IP类型”<br>取值为<br>“IPV4V6(IPV4V6)”<br>时，此参数有效。<br>数据来源：本端规划<br>取值范围：::～FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无<br>配置原则：<br>- IPv6地址必须是全球单播地址，不能为::、 FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址(::1)、链路本地地址(FE80::/10)和组播地址(FF00::/8)。<br>- 当“IP类型”取值从“IPV4(IPV4)”或“IPV6(IPV6)”修改为“IPV4V6(IPV4V6)”时，此参数必须输入。 |
| SGSNN | SGSN名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SGSN名称。<br>数据来源：本端规划<br>取值范围：长度不超过32的字符串<br>默认值：无 |

#### [使用实例](#ZH-CN_MMLREF_0000001126146110)

设置非广播RAI记录信息， “NONRAI” 为 “123000000000” ， “IP类型” 是 “IPV4” ， “IP地址” 是 “192.168.0.0” ， “SGSN名称” 是 “sgsn1” ：

MOD NONRAI: NONRAI="123000000000", IPTYPE=IPV4, IPV4="192.168.0.0", SGSNN="sgsn1";
