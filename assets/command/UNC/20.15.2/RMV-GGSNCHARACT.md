---
id: UNC@20.15.2@MMLCommand@RMV GGSNCHARACT
type: MMLCommand
name: RMV GGSNCHARACT（删除GGSN属性配置信息）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: GGSNCHARACT
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
- GnGp-GGSN_S5_S8接口管理
- GGSN属性
status: active
---

# RMV GGSNCHARACT（删除GGSN属性配置信息）

## 功能

**适用网元：SGSN**

该命令用于删除GGSN属性配置信息表中GGSN属性的记录。

## 注意事项

- 该命令执行后立即生效。
- 删除记录后，系统会继续查找最匹配的记录，采用最匹配的记录的配置值。
- 删除记录前需要确认指定GGSN网元的功能，以免因与实际设备不兼容而导致流程失败。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RANGE | 对端设备范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定需要设置属性信息的对端GGSN范围。<br>取值范围：<br>- “Gn_GGSN（Gn接口GGSN）”<br>- “Gp_GGSN（Gp接口GGSN）”、<br>- “SPECIAL_GGSN（指定GGSN）”<br>默认值： 无 |
| IPT | IP地址类型 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定GGSN信令面IP地址类型。<br>前提条件：只有在<br>“RANGE”<br>配置为<br>“SPECIAL_GGSN（指定GGSN）”<br>时，该参数生效。<br>取值范围：<br>- “IPV4(IPV4)”<br>- “IPV6(IPV6)”<br>默认值：无 |
| GGSNIPV4 | GGSN的信令面IP地址 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定GGSN信令面IPv4地址。<br>前提条件：只有在<br>“IPT”<br>配置为<br>“IPV4”<br>时，才需要配置该类型的IP地址。<br>取值范围：0.0.0.1～255.255.255.254<br>默认值：无<br>配置原则：<br>- 有效的IPv4地址不能为环回地址（127.x.y.z）。<br>- 有效的IPv4地址必须是A、B或者C类地址。 |
| MASKV4 | 掩码 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定对端GGSN的信令面IPv4地址的掩码。<br>前提条件：只有在<br>“IPT”<br>配置为<br>“IPV4”<br>时，才需要配置该参数。<br>取值范围：0.0.0.1～255.255.255.255<br>默认值： 无<br>说明：- 输入的掩码要求对应的二进制值1和1之间不允许存在0。例如：“255.255.0.0”是有效掩码；“123.123.123.123”是无效掩码。因为123对应的二进制为“1111011”，1之间存在0。 |
| GGSNIPV6 | GGSN的信令面IP地址 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定GGSN信令面IPv6地址。<br>前提条件：只有在<br>“IPT”<br>配置为<br>“IPV6”<br>时，才需要配置该类型的IP地址。<br>取值范围：::～FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无<br>配置原则：IPV6地址必须是全球单播地址，不能为::、FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址（::1）、链路本地地址（FE80::/10）和组播地址（FF00::/8）。 |
| MASKV6 | 子网前缀长度 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定子网前缀的长度。<br>前提条件：只有在<br>“IPT”<br>配置为<br>“IPV6”<br>时，才需要配置该参数。<br>取值范围：1～128（数值型）<br>默认值： 无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/GGSNCHARACT]] · GGSN属性配置信息（GGSNCHARACT）

## 使用实例

数据配置错误或者指定的GGSN已经不存在，需要删除IP地址类型为“IPv4”，IP地址为"192.168.168.12"，掩码为"255.255.255.255"的GGSN的数据：

RMV GGSNCHARACT: RANGE=SPECIAL_GGSN, IPT=IPV4, GGSNIPV4="192.168.168.12", MASKV4="255.255.255.255";

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除GGSN属性配置信息(RMV-GGSNCHARACT)_26305744.md`
