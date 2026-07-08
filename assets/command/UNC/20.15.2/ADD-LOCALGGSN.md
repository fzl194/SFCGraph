---
id: UNC@20.15.2@MMLCommand@ADD LOCALGGSN
type: MMLCommand
name: ADD LOCALGGSN（增加本地GGSN列表）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: LOCALGGSN
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
max_records: 120
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- GTP-C接口管理
- GTP-C协议管理
- 本地GGSN功能
status: active
---

# ADD LOCALGGSN（增加本地GGSN列表）

## 功能

**适用网元：SGSN**

该命令用于新增一个本地GGSN的网段。

## 注意事项

- 当开启“异地GGSN容灾”功能时，需要利用此命令来配置本地GGSN信息。
- 该命令执行后立即生效。
- 该命令可以多次执行。
- 配置本地GGSN地址的IP地址网段不能重复或交叉。
- 本表的最大记录数为120。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CFGTP | 配置类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定配置本地GGSN的类型。<br>取值范围：<br>- “IPMASK(IP+掩码)”<br>- “SENDIP(起始IP+终止IP)”<br>- “IPV6MASK(IPv6+前缀)”<br>- “SENDIPV6(起始IPv6+终止IPv6)”<br>默认值：无<br>配置原则：可以配置多条记录，但是IP网段区间不可以重叠和交叉。 |
| SIP | 起始IPv4地址 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定本地GGSN的起始IPv4地址。<br>取值范围：0.0.0.0～255.255.255.255<br>默认值：无<br>配置原则：<br>- 有效的IPv4地址不能为 0.0.0.0,255.255.255.255，或0.x.y.z。<br>- 有效的IPv4地址不能为环回地址(127.x.y.z)，或组播地址(224.x.y.z)。<br>- 有效的IPv4地址必须是A、B或者C类地址。 |
| EIP | 终止IPv4地址 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定本地GGSN的终止IPv4地址。<br>取值范围：0.0.0.0～255.255.255.255<br>默认值：无<br>配置原则：<br>- 有效的IPv4地址不能为 0.0.0.0,255.255.255.255，或0.x.y.z。<br>- 有效的IPv4地址不能为环回地址(127.x.y.z)，或组播地址(224.x.y.z)。<br>- 有效的IPv4地址必须是A、B或者C类地址。<br>说明：- 本参数的取值应该大于等于“起始IPv4地址”的取值。 |
| MASK | 掩码 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定网段的IPv4地址掩码。<br>取值范围：0.0.0.1～255.255.255.255<br>默认值：无 |
| SIPV6 | 起始IPv6地址 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定本地GGSN的起始IPv6地址。<br>取值范围：::～FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无<br>配置原则：<br>- IPv6地址必须是全球单播地址，不能为FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址(::1)、链路本地地址(FE80::/10)和组播地址(FF00::/8)。 |
| EIPV6 | 终止IPv6地址 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定本地GGSN的终止IPv6地址。<br>取值范围：::～FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无<br>配置原则：<br>- IPv6地址必须是全球单播地址，不能为FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址(::1)、链路本地地址(FE80::/10)和组播地址(FF00::/8)。<br>说明：- 本参数的取值应该大于等于“起始IPv6地址”的取值。 |
| PRELEN | 前缀长度 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定网段的IPv6地址前缀长度。<br>取值范围：0~128<br>默认值：无<br>配置原则：<br>- “0”表示全网段。 |
| DESC | 描述 | 可选必选说明：可选参数<br>参数含义：该参数用于描述该命令的文字说明，目的是在配置的时候可以将对象属性、配置原因、背景等进行描述，以便在查询时能够在大量配置数据中清晰的掌握配置的原因。<br>数据来源：整网规划<br>取值范围：0~32位字符串<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/LOCALGGSN]] · 本地GGSN列表（LOCALGGSN）

## 使用实例

添加一个本地GGSN网段，网段为192.168.41.x，掩码为255.255.255.0：

ADD LOCALGGSN: CFGTP=IPMASK, SIP="192.168.41.0", MASK="255.255.255.0";

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加本地GGSN列表(ADD-LOCALGGSN)_72345527.md`
