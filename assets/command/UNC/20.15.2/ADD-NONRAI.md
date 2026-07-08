---
id: UNC@20.15.2@MMLCommand@ADD NONRAI
type: MMLCommand
name: ADD NONRAI（增加非广播RAI配置信息）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: NONRAI
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
- POOL区非广播RAI配置
status: active
---

# ADD NONRAI（增加非广播RAI配置信息）

## 功能

**适用网元：SGSN**

当使用Gb-flex或Iu-flex功能时，此命令用于增加一个本POOL区内非本SGSN的非广播RAI配置记录。

## 注意事项

- 此命令执行立即生效。
- 此命令最大记录数为1024条。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NONRAI | 路由区标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定POOL区内其他SGSN的非广播路由区标识。用于在迁移的时候，目的SGSN来识别MS是从哪个SGSN迁移过来的。一个非广播路由区标识可以唯一地标志一个SGSN。<br>数据来源：本端规划<br>取值范围：长度必须为11或者12位，前5或6位为十进制数，后6位为十六进制数的字符串<br>默认值：无<br>配置原则：NONRAI = LAI + RAC。LAI = MCC + MNC + LAC。MCC由3个阿拉伯数字组成，MNC由2到3个阿拉伯数字组成，LAC是十六进制数，占2个字节。RAC是十六进制数，占1个字节。 |
| IPTYPE | IP类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定IP类型。<br>数据来源：本端规划<br>取值范围：<br>- “IPV4(IPV4)”<br>- “IPV6(IPV6)”<br>- “IPV4V6(IPV4V6)”<br>默认值：无<br>配置原则：当没有设置IP类型时，SGSN信令面地址为无效值255.255.255.255。 |
| IPV4 | SGSN IPv4信令面地址 | 可选必选说明：条件必选参数<br>参数含义：该参数用于表示本POOL区内非本SGSN的信令面IPV4类型地址。<br>前提条件：当<br>“IP类型”<br>取值为<br>“IPV4(IPV4)”<br>或<br>“IPV4V6(IPV4V6)”<br>时，此参数有效。<br>数据来源：本端规划<br>取值范围：0.0.0.0～255.255.255.255<br>默认值：无 |
| IPV6 | SGSN IPv6信令面地址 | 可选必选说明：条件必选参数<br>参数含义：该参数用于表示本POOL区内非本SGSN的信令面IPV6类型地址。<br>前提条件：当<br>“IP类型”<br>取值为<br>“IPV6(IPV6)”<br>时，此参数有效。<br>数据来源：本端规划<br>取值范围：::～FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无<br>配置原则：<br>- IPv6地址必须是全球单播地址，不能为::、 FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址(::1)、链路本地地址(FE80::/10)和组播地址(FF00::/8)。 |
| ALTERNATIVE | SGSN IPv6信令面地址 | 可选必选说明：条件必选参数<br>参数含义：该参数用于表示本POOL区内非本SGSN的信令面IPV6类型地址。<br>前提条件：当<br>“IP类型”<br>取值为<br>“IPV4V6(IPV4V6)”<br>时，此参数有效。<br>数据来源：本端规划<br>取值范围：::～FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无<br>配置原则：<br>- IPv6地址必须是全球单播地址，不能为::、 FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址(::1)、链路本地地址(FE80::/10)和组播地址(FF00::/8)。 |
| SGSNN | SGSN名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SGSN名称。<br>数据来源：本端规划<br>取值范围：长度不超过32的字符串<br>默认值：noname |

## 操作的配置对象

- [非广播RAI配置信息（NONRAI）](configobject/UNC/20.15.2/NONRAI.md)

## 使用实例

增加一个非广播RAI记录， “NONRAI” 为 “123000000000” ， “IP类型” 是 “IPV4” ， “IP地址” 是 “192.168.0.0” “SGSN名称” 是 “sgsn1” ：

ADD NONRAI: NONRAI="123000000000", IPTYPE=IPV4, IPV4="192.168.0.0", SGSNN="sgsn1";

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加非广播RAI配置信息(ADD-NONRAI)_26305918.md`
