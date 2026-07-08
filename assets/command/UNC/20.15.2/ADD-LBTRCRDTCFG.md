---
id: UNC@20.15.2@MMLCommand@ADD LBTRCRDTCFG
type: MMLCommand
name: ADD LBTRCRDTCFG（增加跟踪重定向）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: LBTRCRDTCFG
command_category: 配置类
effect_mode: ''
is_dangerous: false
max_records: 32
category_path:
- 平台服务管理
- CSLB功能管理
- 操作维护
- 跟踪管理
status: active
---

# ADD LBTRCRDTCFG（增加跟踪重定向）

## 功能

该命令用于增加跟踪重定向参数的配置。因为跟踪报文数量过多，导致报文无法在跟踪界面完整显示，建议使用跟踪重定向功能将报文重定向到外部设备。

## 注意事项

- 相同索引的重定向参数配置需要和业务VNFC保持一致。
- 本表最大记录数为32。
- 该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INDEX | 重定向索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定跟踪重定向参数配置的索引。<br>数据来源：本端规划<br>取值范围：1~32<br>默认值：无 |
| VPN | VPN | 可选必选说明：可选参数<br>参数含义：该参用于数指定跟踪重定向源设备的VPN名称。<br>数据来源：本端规划<br>取值范围：1~32位字符串<br>默认值：无<br>配置原则：<br>- 不输入VPN，默认使用公网VPN“_public_”。建议使用用户面VPN。 |
| IPTYPE | IP地址类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定跟踪重定向报文的IP地址类型。<br>数据来源：本端规划<br>取值范围：<br>- “IPV4(IPv4) ”<br>- “IPV6(IPv6) ”<br>默认值：无 |
| SRCIP | 源IPv4地址 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定跟踪重定向源设备的IPv4地址。<br>前提条件：该参数在<br>“IP地址类型”<br>配置为<br>“IPV4(IPv4)”<br>后生效。<br>数据来源：本端规划<br>取值范围：0.0.0.0~255.255.255.255<br>默认值：无<br>配置原则：<br>- 业务地址必须是A、B或者C类地址。 |
| SRCIPV6 | 源IPv6地址 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定跟踪重定向源设备的IPv6址。<br>前提条件：该参数在<br>“IP地址类型”<br>配置为<br>“IPV6(IPv6)”<br>后生效。<br>数据来源：本端规划<br>取值范围：::~FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无<br>配置原则：<br>- IPv6地址必须是全球单播地址，不能为::、FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址(::1)、链路本地地址(FE80::/10)和组播地址(FF00::/8)。 |
| SRCPORT | 源端口号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定跟踪重定向源设备的端口号。<br>数据来源：本端规划<br>取值范围：5000~65535<br>默认值：10000 |
| DSTIP | 目的IPv4地址 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定跟踪重定向目的设备的IPv4地址。<br>前提条件：该参数在<br>“IP地址类型”<br>配置为<br>“IPV4(IPv4)”<br>后生效。<br>数据来源：对端协商<br>取值范围：0.0.0.0~255.255.255.255<br>默认值：无<br>配置原则：<br>- 业务地址必须是A、B或者C类地址。 |
| DSTIPV6 | 目的IPv6地址 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定跟踪重定向目的设备的IPv6址。<br>前提条件：该参数在<br>“IP地址类型”<br>配置为<br>“IPV6(IPv6)”<br>后生效。<br>数据来源：对端协商<br>取值范围：::~FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无<br>配置原则：<br>- IPv6地址必须是全球单播地址，不能为::、FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址(::1)、链路本地地址(FE80::/10)和组播地址(FF00::/8)。 |
| DSTPORT | 目的端口号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定跟踪重定向目的设备的端口号。<br>数据来源：对端协商<br>取值范围：5000~65535<br>默认值：10000 |
| DSCRPT | 描述 | 可选必选说明：可选参数<br>参数含义：该参数用于描述当前跟踪重定向用途。<br>数据来源：本端规划<br>取值范围：1~64位字符串<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/LBTRCRDTCFG]] · 跟踪重定向（LBTRCRDTCFG）

## 使用实例

将跟踪报文重定向到外部设备，外部设备的IP地址为192.168.0.2，配置如下：

ADD LBTRCRDTCFG: INDEX=1, VPN="trcrdt", IPTYPE=IPV4, SRCIP="192.168.0.1", SRCPORT=32676, DSTIP="192.168.0.2", DSTPORT=32678, DSCRPT="Redirection";

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-LBTRCRDTCFG.md`
