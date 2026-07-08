---
id: UNC@20.15.2@MMLCommand@MOD HOMEPGWIP
type: MMLCommand
name: MOD HOMEPGWIP（修改归属地PGW-C IP地址）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: HOMEPGWIP
command_category: 配置类
applicable_nf:
- SGW-C
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- Proxy SGW_SMF管理
- 归属地PGW-C IP地址
status: active
---

# MOD HOMEPGWIP（修改归属地PGW-C IP地址）

## 功能

**适用NF：SGW-C**

该命令用于Proxy S-GW特性中修改归属地PGW-C IP地址记录的描述信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定用户范围。<br>数据来源：本端规划<br>取值范围：<br>- IMSI_PRE（IMSI前缀 ）<br>- MSISDN_PRE（MSISDN前缀）<br>默认值：无<br>配置原则：<br>IMSI_PRE和MSISDN_PRE记录的优先级受SET PROXYSGWFUNC命令中的QUERYTYPE参数控制。 |
| PREFIX | 前缀 | 可选必选说明：该参数在"SUBRANGE"配置为"IMSI_PRE"、"MSISDN_PRE"时为条件必选参数。<br>参数含义：该参数用于指定用户号码前缀。当参数SUBRANGE为"IMSI_PRE"时，本参数表示IMSI号码前缀，当参数SUBRANGE为"MSISDN_PRE"时，本参数表示MSISDN号码前缀。使用时按照最长匹配进行查询。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~15。<br>默认值：无<br>配置原则：<br>取值范围为1~15位数字。 |
| IPVERSION | IP地址版本类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定归属地PGW的IP地址类型。<br>数据来源：全网规划<br>取值范围：<br>- “IPV4（IPV4）”：表示地址类型为IPv4<br>- “IPV6（IPV6）”：表示地址类型为IPv6<br>默认值：无<br>配置原则：无 |
| HOMEIPV4 | IPv4地址 | 可选必选说明：该参数在"IPVERSION"配置为"IPV4"时为条件必选参数。<br>参数含义：该参数用于指定归属地PGW的IPv4地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：<br>IPv4地址不能配置为0.0.0.0、255.255.255.255和环回地址(127.x.y.z)。业务地址必须是A、B或者C类地址。 |
| HOMEIPV6 | IPv6地址 | 可选必选说明：该参数在"IPVERSION"配置为"IPV6"时为条件必选参数。<br>参数含义：该参数用于指定归属地PGW的IPv6地址。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：<br>IPv6地址必须是全球单播地址，不能为::、FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址(::1)、链路本地地址(FE80::/10)和组播地址(FF00::/8)。 |
| DESC | 描述信息 | 可选必选说明：可选参数<br>参数含义：该参数用于指定本记录的描述信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~32。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [归属地PGW-C IP地址（HOMEPGWIP）](configobject/UNC/20.15.2/HOMEPGWIP.md)

## 使用实例

修改用户范围为IMSI_PRE，前缀为27602，IP地址类型为IPV4，IPV4地址为10.0.0.0的配置的描述信息为Vodafone，执行如下命令：

```
MOD HOMEPGWIP: SUBRANGE=IMSI_PRE, PREFIX="27602", IPVERSION=IPV4, HOMEIPV4="10.0.0.0", DESC="Vodafone";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改归属地PGW-C-IP地址（MOD-HOMEPGWIP）_06399920.md`
