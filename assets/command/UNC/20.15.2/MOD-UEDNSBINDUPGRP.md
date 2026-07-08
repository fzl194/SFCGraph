---
id: UNC@20.15.2@MMLCommand@MOD UEDNSBINDUPGRP
type: MMLCommand
name: MOD UEDNSBINDUPGRP（修改UPF组的DNS属性）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: UEDNSBINDUPGRP
command_category: 配置类
applicable_nf:
- GGSN
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 接入控制
- DN网络DNS_NBNS选择管理
- DNS选择管理
- UPF组DNS域名策略
status: active
---

# MOD UEDNSBINDUPGRP（修改UPF组的DNS属性）

## 功能

**适用NF：GGSN、PGW-C、SMF**

该命令用于修改指定UPF组的DNS属性和DNS64属性。

## 注意事项

- 该命令执行后立即生效。

- 每个UPF组支持一条DNS属性配置。
- 配置的主、备DNS服务器地址不能相同。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| UPFGRPNAME | UPF组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定UPF组的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~32。不区分大小写。<br>默认值：无<br>配置原则：<br>该参数使用ADD UEDNSUPGROUP命令生成。 |
| APNTYPE | APN类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN类型。<br>数据来源：本端规划<br>取值范围：<br>- ALL_APN（所有APN）<br>- APN_GROUP（APN组）<br>- SPECIAL_APN（指定APN）<br>默认值：无<br>配置原则：<br>优先级从高到低：“SPECIAL_APN”、“APN_GROUP”、“ALL_APN”。 |
| APNGRPNAME | APN组名 | 可选必选说明：该参数在"APNTYPE"配置为"APN_GROUP"时为条件必选参数。<br>参数含义：该参数用于指定APN组名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~31。<br>默认值：无<br>配置原则：<br>该参数使用ADD SMFAPNGRP命令配置生成。<br>该参数在“APNTYPE”参数配置为“APN_GROUP”后生效。 |
| APN | APN名称 | 可选必选说明：该参数在"APNTYPE"配置为"SPECIAL_APN"时为条件必选参数。<br>参数含义：该参数用于指定APN实例名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”特殊字符，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数使用ADD APN命令配置生成。<br>该参数在“APNTYPE”参数配置为“SPECIAL_APN”后生效。 |
| MDNSSERVERV4 | IPv4主DNS服务器IP | 可选必选说明：可选参数<br>参数含义：该参数用于配置IPv4主DNS服务器地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。点分十进制。只允许配置A、B、C类地址。<br>默认值：无<br>配置原则：无 |
| BDNSSERVERV4 | IPv4备DNS服务器IP | 可选必选说明：可选参数<br>参数含义：该参数用于配置IPv4备DNS服务器地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。点分十进制。只允许配置A、B、C类地址。<br>默认值：无<br>配置原则：无 |
| MDNSSERVERV6 | IPv6主DNS服务器IP | 可选必选说明：可选参数<br>参数含义：该参数用于配置IPv6主DNS服务器地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。冒号十六进制。<br>默认值：无<br>配置原则：无 |
| BDNSSERVERV6 | IPv6备DNS服务器IP | 可选必选说明：可选参数<br>参数含义：该参数用于配置IPv6备DNS服务器地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。冒号十六进制。<br>默认值：无<br>配置原则：无 |
| MDNSSERVER64 | IPv6主DNS64服务器IP | 可选必选说明：可选参数<br>参数含义：该参数用于PDP类型为IPv6时配置主DNS64地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |
| BDNSSERVER64 | IPv6备DNS64服务器IP | 可选必选说明：可选参数<br>参数含义：该参数用于PDP类型为IPv6时配置备DNS64地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |
| FIRMODEV4 | IPv4 第一优先级服务器属性 | 可选必选说明：可选参数<br>参数含义：该参数用于指定IPv4第一优先级选择模式。<br>数据来源：本端规划<br>取值范围：<br>- “LOCAL（local）”：指定本地配置优先。即本命令配置的DNS地址。<br>- “RADIUS（radius）”：指定RADIUS服务器返回的DNS属性优先。<br>- “DHCP（dhcp）”：指定DHCP服务器返回的DNS属性优先。<br>- “PCRF（pcrf）”：指定PCRF返回的DNS属性优先。<br>默认值：无<br>配置原则：无 |
| SECMODEV4 | IPv4 第二优先级服务器属性 | 可选必选说明：可选参数<br>参数含义：该参数用于指定IPv4第二优先级选择模式。<br>数据来源：本端规划<br>取值范围：<br>- “LOCAL（local）”：指定本地配置优先。即本命令配置的DNS地址。<br>- “RADIUS（radius）”：指定RADIUS服务器返回的DNS属性优先。<br>- “DHCP（dhcp）”：指定DHCP服务器返回的DNS属性优先。<br>- “PCRF（pcrf）”：指定PCRF返回的DNS属性优先。<br>默认值：无<br>配置原则：无 |
| THIRDMODEV4 | IPv4第三优先级服务器属性 | 可选必选说明：可选参数<br>参数含义：该参数用于指定IPv4第三优先级选择模式。<br>数据来源：本端规划<br>取值范围：<br>- “LOCAL（local）”：指定本地配置优先。即本命令配置的DNS地址。<br>- “RADIUS（radius）”：指定RADIUS服务器返回的DNS属性优先。<br>- “DHCP（dhcp）”：指定DHCP服务器返回的DNS属性优先。<br>- “PCRF（pcrf）”：指定PCRF返回的DNS属性优先。<br>默认值：无<br>配置原则：无 |
| FOURTHMODEV4 | IPv4第四优先级服务器属性 | 可选必选说明：可选参数<br>参数含义：该参数用于指定IPv4第四优先级选择模式。<br>数据来源：本端规划<br>取值范围：<br>- “LOCAL（local）”：指定本地配置优先。即本命令配置的DNS地址。<br>- “RADIUS（radius）”：指定RADIUS服务器返回的DNS属性优先。<br>- “DHCP（dhcp）”：指定DHCP服务器返回的DNS属性优先。<br>- “PCRF（pcrf）”：指定PCRF返回的DNS属性优先。<br>默认值：无<br>配置原则：无 |
| FIRMODEV6 | IPv6 第一优先级服务器属性 | 可选必选说明：可选参数<br>参数含义：该参数用于指定IPv6第一优先级选择模式。<br>数据来源：本端规划<br>取值范围：<br>- “LOCAL（local）”：指定本地配置优先。即本命令配置的DNS地址。<br>- “RADIUS（radius）”：指定RADIUS服务器返回的DNS属性优先。<br>- “DHCP（dhcp）”：指定DHCP服务器返回的DNS属性优先。<br>- “PCRF（pcrf）”：指定PCRF返回的DNS属性优先。<br>默认值：无<br>配置原则：无 |
| SECMODEV6 | IPv6 第二优先级服务器属性 | 可选必选说明：可选参数<br>参数含义：该参数用于指定IPv6第二优先级选择模式。<br>数据来源：本端规划<br>取值范围：<br>- “LOCAL（local）”：指定本地配置优先。即本命令配置的DNS地址。<br>- “RADIUS（radius）”：指定RADIUS服务器返回的DNS属性优先。<br>- “DHCP（dhcp）”：指定DHCP服务器返回的DNS属性优先。<br>- “PCRF（pcrf）”：指定PCRF返回的DNS属性优先。<br>默认值：无<br>配置原则：无 |
| THIRDMODEV6 | IPv6第三优先级服务器属性 | 可选必选说明：可选参数<br>参数含义：该参数用于指定IPv6第三优先级选择模式。<br>数据来源：本端规划<br>取值范围：<br>- “LOCAL（local）”：指定本地配置优先。即本命令配置的DNS地址。<br>- “RADIUS（radius）”：指定RADIUS服务器返回的DNS属性优先。<br>- “DHCP（dhcp）”：指定DHCP服务器返回的DNS属性优先。<br>- “PCRF（pcrf）”：指定PCRF返回的DNS属性优先。<br>默认值：无<br>配置原则：无 |
| FOURTHMODEV6 | IPv6第四优先级服务器属性 | 可选必选说明：可选参数<br>参数含义：该参数用于指定IPv6第四优先级选择模式。<br>数据来源：本端规划<br>取值范围：<br>- “LOCAL（local）”：指定本地配置优先。即本命令配置的DNS地址。<br>- “RADIUS（radius）”：指定RADIUS服务器返回的DNS属性优先。<br>- “DHCP（dhcp）”：指定DHCP服务器返回的DNS属性优先。<br>- “PCRF（pcrf）”：指定PCRF返回的DNS属性优先。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [UPF组的DNS属性（UEDNSBINDUPGRP）](configobject/UNC/20.15.2/UEDNSBINDUPGRP.md)

## 使用实例

当APNTYPE为ALL_APN时，修改UPF组upfgrp1的DNS属性和DNS64属性：

```
MOD UEDNSBINDUPGRP: UPFGRPNAME="upfgrp1", APNTYPE=ALL_APN, MDNSSERVERV4="10.1.1.1", BDNSSERVERV4="10.2.2.2", MDNSSERVERV6="2001:0DB8:0:1::", BDNSSERVERV6="2001:0DB8:0:2::", MDNSSERVER64="2001:0DB8:0:3::", BDNSSERVER64="2001:0DB8:0:4::";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改UPF组的DNS属性（MOD-UEDNSBINDUPGRP）_73321241.md`
