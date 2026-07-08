# 修改POOL区NRI配置信息(MOD POOLNRI)

- [命令功能](#ZH-CN_MMLREF_0000001172345707__1.3.1.1)
- [注意事项](#ZH-CN_MMLREF_0000001172345707__1.3.2.1)
- [本地用户权限](#ZH-CN_MMLREF_0000001172345707__1.3.3.1)
- [网管用户权限](#ZH-CN_MMLREF_0000001172345707__1.3.4.1)
- [参数说明](#ZH-CN_MMLREF_0000001172345707__1.3.5.1)
- [使用实例](#ZH-CN_MMLREF_0000001172345707__1.3.6.1)

#### [命令功能](#ZH-CN_MMLREF_0000001172345707)

**适用网元：SGSN**

此命令用于修改本POOL区内非本SGSN的NRI属性配置信息。

#### [注意事项](#ZH-CN_MMLREF_0000001172345707)

- 输入的IP地址和本SGSN的信令面IP地址不能相同。
- 此命令执行后立即生效。

#### [本地用户权限](#ZH-CN_MMLREF_0000001172345707)

manage-ug；system-ug

#### [网管用户权限](#ZH-CN_MMLREF_0000001172345707)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_MMLREF_0000001172345707)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POOLID | POOL区标识 | 可选必选说明：必选参数<br>参数含义：该参数用于表示POOL区标识。<br>数据来源：整网规划<br>取值范围：0～4095<br>默认值：无 |
| NRIV | NRI值 | 可选必选说明：必选参数<br>参数含义：该参数用于表示本POOL区内非本SGSN的NRI的值，NRI（Net Resource Identify），网络资源标识，用于标识一个CN节点。RAN根据NRI将MS的消息路由到对应的SGSN。<br>数据来源：整网规划<br>取值范围：0～1023<br>默认值：无 |
| IPTYPE | IP类型 | 可选必选说明：可选参数<br>参数含义：该参数用于表示SGSN信令面IP地址类型。<br>数据来源：整网规划<br>取值范围：<br>- “IPV4(IPV4)”<br>- “IPV6(IPV6)”<br>- “IPV4V6(IPV4V6)”<br>默认值：无 |
| IPV4 | SGSN信令面地址 | 可选必选说明：条件必选参数<br>参数含义：该参数用于表示本POOL区内非本SGSN的信令面IPv4类型地址。<br>前提条件：当<br>“IP类型”<br>取值为<br>“IPV4(IPV4)”<br>或<br>“IPV4V6(IPV4V6)”<br>时，此参数有效。当<br>“IP类型”<br>取值为<br>“IPV4(IPV4)”<br>时，此参数为条件必选参数，<br>“IP类型”<br>取值为<br>“IPV4V6(IPV4V6)”<br>时，此参数为条件可选参数。<br>数据来源：整网规划<br>取值范围：0.0.0.0～255.255.255.255<br>默认值：无<br>配置原则：<br>- 当“IP类型”取值从“IPV4(IPV4)”或“IPV6(IPV6)”修改为“IPV4V6(IPV4V6)”时，此参数必须输入。 |
| IPV6 | SGSN信令面地址 | 可选必选说明：条件必选参数<br>参数含义：该参数用于表示本POOL区内非本SGSN的信令面IPv6类型地址。<br>前提条件：当<br>“IP类型”<br>取值为<br>“IPV6(IPV6)”<br>时，此参数有效。<br>数据来源：整网规划<br>取值范围：::～FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无<br>配置原则：<br>- IPv6地址必须是全球单播地址，不能为::、 FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址(::1)、链路本地地址(FE80::/10)和组播地址(FF00::/8)。 |
| ALTERNATIVE | SGSN信令面地址2 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定本POOL区内非本SGSN的信令面IPV6类型地址。<br>前提条件：当<br>“IP类型”<br>取值为<br>“IPV4V6(IPV4V6)”<br>时，该参数有效。<br>数据来源：整网规划<br>取值范围：::～FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无<br>配置原则：<br>- 输入的IP地址和本SGSN的信令面IP地址不能相同。<br>- IPv6地址必须是全球单播地址，不能为::、 FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址(::1)、链路本地地址(FE80::/10)和组播地址(FF00::/8)。<br>- 当“IP类型”取值从“IPV4(IPV4)”或“IPV6(IPV6)”修改为“IPV4V6(IPV4V6)”时，此参数必须输入。 |
| SGSNN | SGSN名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示SGSN的名称。<br>数据来源：整网规划<br>取值范围：长度不超过32的字符串<br>默认值：无 |

#### [使用实例](#ZH-CN_MMLREF_0000001172345707)

修改POOLID为1，NRI值为10的NRI属性：SGSN信令面地址类型为：IPv4，SGSN信令面地址为“10.161.251.233”，SGSNN名称为“SGSN50”：

MOD POOLNRI: POOLID=1, NRIV=10, IPTYPE=IPV4, IPV4="10.161.251.233", SGSNN="SGSN50";
