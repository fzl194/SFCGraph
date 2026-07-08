---
id: UNC@20.15.2@MMLCommand@ADD BLACKLIST
type: MMLCommand
name: ADD BLACKLIST（增加黑名单地址列表）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: BLACKLIST
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
- GGSN
effect_mode: 对新用户生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- UE地址管理
- 静态地址黑名单管理
status: active
---

# ADD BLACKLIST（增加黑名单地址列表）

## 功能

**适用NF：PGW-C、SMF、GGSN**

该命令用于将指定的IP地址段设置为黑名单，禁止携带该地址段内IP地址的用户入网。

## 注意事项

- 该命令执行后只对新激活用户生效。

- 静态地址黑名单基于VPN实例配置，每个VPN实例最多可配置20个黑名单列表。
- 该命令不支持C面分地址。

- 最多可输入200条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NAME | 名称 | 可选必选说明：必选参数<br>参数含义：黑名单地址段名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~79。不支持空格及特殊字符“#”、“$”和“&”等，由“-”、“_”、数字、字母和“.”组成，不能以“.”开头或结尾，不区分大小写。<br>默认值：无<br>配置原则：无 |
| IPVERSION | IP地址类型 | 可选必选说明：可选参数<br>参数含义：用于指定IP地址类型。<br>数据来源：本端规划<br>取值范围：<br>- “IPv4（IPv4）”：IPv4<br>- “IPv6（IPv6）”：IPv6<br>默认值：IPv4<br>配置原则：无 |
| V4STARTIP | IPv4起始地址 | 可选必选说明：该参数在"IPVERSION"配置为"IPv4"时为条件必选参数。<br>参数含义：该参数用于指定IPv4地址段的起始地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：<br>- 取值范围：1.0.0.0~255.255.255.254。<br>- IPv4地址不能为组播地址（224.x.y.z）和环回地址（127.x.y.z）。<br>- IPv4地址必须是A、B或者C类地址。<br>- 起始IP地址必须小于或等于终止IP地址，每个IPv4地址段最多可以配置32768个地址，且同一VPN下，各个地址段里的地址不能相互重叠。 |
| V4ENDIP | IPv4结束地址 | 可选必选说明：该参数在"IPVERSION"配置为"IPv4"时为条件必选参数。<br>参数含义：该参数用于指定IPv4地址段的结束地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：<br>- 取值范围：1.0.0.0~255.255.255.254。<br>- IPv4地址不能为组播地址（224.x.y.z）和环回地址（127.x.y.z）。<br>- IPv4地址必须是A、B或者C类地址。<br>- 结束IP地址必须大于或等于起始IP地址，每个IPv4地址段最多可以配置32768个地址，且同一VPN下，各个地址段里的地址不能相互重叠。 |
| V6PREFIXSTART | IPv6前缀起始地址 | 可选必选说明：该参数在"IPVERSION"配置为"IPv6"时为条件必选参数。<br>参数含义：该参数用于指定IPv6地址段的起始前缀。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：<br>- 取值范围：::～FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF。<br>- IPv6地址必须是全球单播地址，不能为::、FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址（::1）、链路本地地址（FE80::/10）、组播地址（FF00::/8）和IPv4映射地址（::FFFF:XXXX:XXXX），若为IPv4兼容地址时，需判断是否符合IPv4地址要求。<br>- 前缀地址段的起始地址必须小于或等于结束地址，每个IPv6地址段最多可以配置1048576个地址，且同一VPN下，各个前缀地址段里的地址不能相互重叠，IPv6地址的前缀长度默认为64 bit。 |
| V6PREFIXEND | IPv6前缀结束地址 | 可选必选说明：该参数在"IPVERSION"配置为"IPv6"时为条件必选参数。<br>参数含义：该参数用于指定IPv6地址段的终止前缀。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：<br>- 取值范围：::～FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF。<br>- IPv6地址必须是全球单播地址，不能为::、FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址（::1）、链路本地地址（FE80::/10）、组播地址（FF00::/8）和IPv4映射地址（::FFFF:XXXX:XXXX），若为IPv4兼容地址时，需判断是否符合IPv4地址要求。<br>- 前缀地址段的起始地址必须小于或等于结束地址，每个IPv6地址段最多可以配置1048576个地址，且同一VPN下，各个前缀地址段里的地址不能相互重叠，IPv6地址的前缀长度默认为64 bit。 |
| HASVPN | 绑定VPN | 可选必选说明：可选参数<br>参数含义：该参数用于指定是否绑定VPN。<br>数据来源：本端规划<br>取值范围：<br>- Disable（去使能）<br>- Enable（使能）<br>默认值：Disable<br>配置原则：无 |
| VPNINSTANCE | VPN实例名 | 可选必选说明：该参数在"HASVPN"配置为"Enable"时为条件必选参数。<br>参数含义：该参数用于指定VPN实例名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~31。<br>默认值：无<br>配置原则：<br>该参数使用ADD VPNINST命令配置生成。 |

## 操作的配置对象

- [黑名单地址列表（BLACKLIST）](configobject/UNC/20.15.2/BLACKLIST.md)

## 使用实例

假设运营商希望增加实例为testvpn下的静态地址黑名单，起始地址为192.168.0.1，结束地址为192.168.0.255：

```
ADD BLACKLIST: NAME="testblacklist", IPVERSION=IPv4, V4STARTIP="192.168.0.1", V4ENDIP="192.168.0.255", HASVPN=Enable, VPNINSTANCE="testvpn";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加黑名单地址列表（ADD-BLACKLIST）_44006355.md`
