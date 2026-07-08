---
id: UNC@20.15.2@MMLCommand@ADD POOLNRI
type: MMLCommand
name: ADD POOLNRI（增加POOL区NRI配置信息）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: POOLNRI
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
max_records: 1024
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 网络管理
- SGSN POOL区管理
- POOL区NRI配置
status: active
---

# ADD POOLNRI（增加POOL区NRI配置信息）

## 功能

**适用网元：SGSN**

当使用Iu-flex/Gb-flex功能时，此命令用于配置本POOL区内非本SGSN的NRI属性配置信息。Iu-flex/Gb-flex指一个RAN连接同一个功能域（CS或者PS）的多个CN节点的功能。Iu-flex/Gb-flex新增的功能包括：RAN节点的消息路由功能；各个CN节点的负载平衡功能；缺省SGSN功能；后向兼容的功能等。POOL区指一个由多个路由区组成的区域，有一组（多个）SGSN为这个区域的MS服务，需要为每个SGSN配置一个或多个不同的NRI，用来标识每个SGSN。

系统开启Iu-flex/Gb-flex功能，当发生Inter SGSN的附着或者路由区更新流程时，本SGSN可以根据P-TMSI中的NRI在本表中查找OLD SGSN的信令面IP地址。关于flex功能描述，请参考3GPP规范23.236。

## 注意事项

- 此命令执行立即生效。
- 此命令最大记录数为1024条。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数ID | 参数名称 | 参数说明 |
| --- | --- | --- |
| POOLID | POOL区标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定POOL区标识。<br>数据来源：整网规划<br>取值范围：0～4095<br>默认值：无<br>配置原则：<br>“POOL区标识”<br>、<br>“NRI值”<br>唯一确定一条记录。 |
| NRIV | NRI值 | 可选必选说明：必选参数<br>参数含义：该参数用于指定本POOL区内非本SGSN的NRI的值，NRI（Net Resource Identify），网络资源标识，用于标识一个CN节点。RAN根据NRI将MS的消息路由到对应的SGSN。<br>数据来源：整网规划<br>取值范围：0～1023<br>默认值：无<br>配置原则：<br>- NRI值的取值范围应该与NRI的长度一致，不能超过或者等于2NRI长度。<br>- “POOL区标识”、“NRI值”唯一确定一条记录。 |
| IPTYPE | IP类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定SGSN信令面IP地址类型。<br>数据来源：整网规划<br>取值范围：<br>- “IPV4(IPV4)”<br>- “IPV6(IPV6)”<br>- “IPV4V6(IPV4V6)”<br>默认值：无 |
| IPV4 | SGSN信令面地址 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定本POOL区内非本SGSN的信令面IPV4类型地址。<br>前提条件：当<br>“IP类型”<br>取值为<br>“IPV4(IPV4)”<br>或<br>“IPV4V6(IPV4V6)”<br>时，该参数有效。<br>数据来源：整网规划<br>取值范围：0.0.0.0～255.255.255.255<br>默认值：无<br>配置原则：<br>- 输入的IP地址和本SGSN的信令面IP地址不能相同。<br>- 输入的IP地址不能是组播地址（224.x.y.z）或是回环地址（127.x.y.z）。<br>- 输入的IP地址必须是A类、B类或是C类地址。 |
| IPV6 | SGSN信令面地址 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定本POOL区内非本SGSN的信令面IPV6类型地址。<br>前提条件：当<br>“IP类型”<br>取值为<br>“IPV6(IPV6)”<br>时，该参数有效。<br>数据来源：整网规划<br>取值范围：::～FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无<br>配置原则：<br>- 输入的IP地址和本SGSN的信令面IP地址不能相同。<br>- IPv6地址必须是全球单播地址，不能为::、 FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址(::1)、链路本地地址(FE80::/10)和组播地址(FF00::/8)。 |
| ALTERNATIVE | SGSN信令面地址2 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定本POOL区内非本SGSN的信令面IPV6类型地址。<br>前提条件：当<br>“IP类型”<br>取值为<br>“IPV4V6(IPV4V6)”<br>时，该参数有效。<br>数据来源：整网规划<br>取值范围：::～FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无<br>配置原则：<br>- 输入的IP地址和本SGSN的信令面IP地址不能相同。<br>- IPv6地址必须是全球单播地址，不能为::、 FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址(::1)、链路本地地址(FE80::/10)和组播地址(FF00::/8)。 |
| SGSNN | SGSN名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SGSN的名称。<br>数据来源：整网规划<br>取值范围：长度不超过32的字符串<br>默认值：noname |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@POOLNRI]] · POOL区NRI配置信息（POOLNRI）

## 使用实例

增加一个POOLNRI记录，POOLID为1，NRI值为10，SGSN信令面地址类型为IPV4，SGSN信令面地址为“10.161.251.233”，SGSNN名称为“SGSN50”：

ADD POOLNRI: POOLID=1, NRIV=10, IPTYPE=IPV4, IPV4="10.161.251.233",SGSNN="SGSN50";

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-POOLNRI.md`
