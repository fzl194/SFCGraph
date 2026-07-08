---
id: UNC@20.15.2@MMLCommand@RMV SGSNCHARACT
type: MMLCommand
name: RMV SGSNCHARACT（删除GnGp SGSN属性配置信息）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: SGSNCHARACT
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- GTP-C接口管理
- GnGp-SGSN_S10_S16_S3接口管理
- GnGp SGSN属性
status: active
---

# RMV SGSNCHARACT（删除GnGp SGSN属性配置信息）

## 功能

**适用网元：SGSN**

该命令用于删除对端SGSN的QoS属性信息记录。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPT | IP地址类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定对端SGSN的信令面IP地址类型。<br>数据来源：整网规划<br>取值范围：<br>“IPV4”<br>、<br>“IPV6”<br>默认值：无<br>配置原则：<br>- IPV4，表示对端SGSN的信令面IP地址为IPV4类型。<br>- IPV6，表示对端SGSN的信令面IP地址为IPV6类型。 |
| IPV4 | SGSN IPv4信令面地址 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定对端SGSN的信令面IPV4地址。<br>前提条件：当<br>“IPT（IP地址类型）”<br>为IPv4时显示。<br>数据来源：整网规划<br>取值范围：0.0.0.1~255.255.255.254<br>默认值： 无<br>配置原则：<br>- 有效的IPV4地址不能为环回地址(127.x.y.z)。<br>- 有效的IPV4地址必须是A、B或者C类地址。 |
| MASKV4 | 掩码 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定对端SGSN的信令面IPV4地址的掩码。<br>前提条件：当<br>“IPT（IP地址类型）”<br>为IPv4时显示。<br>数据来源：整网规划<br>取值范围：0.0.0.1~255.255.255.255<br>默认值： 无<br>说明：- 输入的掩码要求对应的二进制值1和1之间不允许存在0。例如：“255.255.0.0”是有效掩码；“123.123.123.123”是无效掩码。因为123对应的二进制为“1111011”，1之间存在0。 |
| IPV6 | SGSN IPv6信令面地址 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定SGSN配置的信令面IPV6地址。<br>前提条件：当<br>“IPT（IP地址类型）”<br>为IPv6时显示。<br>数据来源：整网规划<br>取值范围：::~FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值： 无<br>配置原则：IPV6地址必须是全球单播地址，不能为::、FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址(::1)、链路本地地址(FE80::/10)和组播地址(FF00::/8)。 |
| MASKV6 | 子网前缀长度 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定子网前缀的长度。<br>前提条件：当<br>“IPT（IP地址类型）”<br>为IPv6时显示。<br>数据来源：整网规划<br>取值范围：1~128（数值型）<br>默认值： 无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SGSNCHARACT]] · GnGp SGSN属性配置信息（SGSNCHARACT）

## 使用实例

删除信令面IP地址为"192.168.168.12"，掩码为"255.255.255.0"的SGSN的属性信息：

RMV SGSNCHARACT:IPT=IPV4, IPV4="192.168.168.12", MASKV4="255.255.255.0";

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-SGSNCHARACT.md`
