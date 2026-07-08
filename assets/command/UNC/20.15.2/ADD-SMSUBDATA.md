---
id: UNC@20.15.2@MMLCommand@ADD SMSUBDATA
type: MMLCommand
name: ADD SMSUBDATA（增加签约数据纠正参数）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: SMSUBDATA
command_category: 配置类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
max_records: 1024
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- 会话管理
- 签约数据纠正
status: active
---

# ADD SMSUBDATA（增加签约数据纠正参数）

## 功能

**适用网元：SGSN、MME**

该命令用于增加一条签约数据修改的记录，修改IMSI号段、PDP TYPE、APN匹配的用户群的签约数据类型。使用该命令时建议设置软参DWORD_EX26 BIT13的值为1。

## 注意事项

- 该命令执行后立即生效。
- 该表最大记录数为1024。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定签约数据纠正参数所包含的用户范围，用来设定该命令的作用范围。<br>数据来源：整网规划<br>取值范围：<br>- “ALL_USER(所有用户)”：表示所有用户，增加全局约束的时候添加。<br>- “SPECIAL_USER(指定用户)”：表示指定的用户，增加指定用户配置的时候添加。<br>默认值：无<br>配置原则：相同APNNI，PDPTYPE时，只能配置一条<br>“SUBRANGE(用户范围)”<br>为<br>“所有用户”<br>的记录。 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定用户的IMSIPRE(IMSI前缀)，用来确定命令的作用范围，即当为选择SPECIAL USER时，才可以配置IMSIPRE。<br>前提条件：该参数在<br>“SUBRANGE(用户范围)”<br>参数设置为<br>“SPECIAL_USER(指定用户)”<br>时，才需要配置。<br>数据来源：整网规划<br>取值范围：5～15位数字<br>默认值：无<br>说明：- “IMSIPRE(IMSI前缀)”为全局唯一。 |
| TYPE | 匹配条件 | 可选必选说明：必选参数<br>参数含义：该参数用于指定合适的匹配条件。<br>数据来源：本端规划<br>取值范围：<br>- “SUBSCRIBED_PARAMETER(签约参数)”：指定使用签约的参数来作为匹配条件。<br>- “Context_ID(Context ID)”：指定使用上下文标识来作为匹配条件。<br>默认值：无 |
| CTXID | 上下文标识 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定PDP上下文标识。<br>前提条件：该参数在<br>“TYPE(匹配条件)”<br>参数设置为<br>“Context_ID(Context ID)”<br>时，才需要配置。<br>数据来源：整网规划<br>取值范围：0～255<br>默认值：无 |
| APNNIRANGE | 签约APNNI范围 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定合适的签约APNNI范围。<br>前提条件：该参数在<br>“TYPE(匹配条件)”<br>参数设置为<br>“SUBSCRIBED_PARAMETER(签约参数)”<br>时，才需要配置。<br>数据来源：本端规划<br>取值范围：<br>- “APNNI_ALL(所有签约APNNI)”：用于增加一条修改所有的APNNI的记录。<br>- “APNNI_SPECIAL(指定签约APNNI)”：用于增加一条修改指定APNNI的记录。<br>默认值：无 |
| APNNI | 签约APNNI | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定APN网络标识。<br>前提条件：该参数在<br>“APNNIRANGE(签约APNNI范围)”<br>参数设置为<br>“APNNI_SPECIAL(指定签约APNNI)”<br>时，才需要配置。<br>数据来源：本端规划<br>取值范围：1～62位字符串<br>默认值：无<br>配置原则：<br>- APN网络标识地址由一个或多个LABEL构成，各LABEL间用“.”间隔。每个LABEL的构成字符只能是字母A～Z或a～z、数字0～9和中划线“-”，字母不区分大小写。<br>- APN网络标识地址不能以“rac”、“lac”、“sgsn”或“rnc”开头，不能以“.gprs”结尾，不能取值为“*”。<br>- 输入的APNNI参数应为类似于XXX.XXX的形式，如“123.net”。如果配置的APNNI不正确，可能因DNS解析失败而导致激活流程失败。 |
| PDPTYPE | 签约PDP/PDN类型 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定PDP类型。<br>前提条件：该参数在<br>“TYPE(匹配条件)”<br>参数设置为<br>“SUBSCRIBED_PARAMETER(签约参数)”<br>时，才需要配置。<br>数据来源：整网规划<br>取值范围：<br>- “IPV4(IPv4地址)”：表示IPv4协议，为UE分配IPv4地址。<br>- “IPV6(IPv6地址)”：表示IPv6协议，为UE分配IPv6地址。<br>- “PPP(PPP)”：表示点对点通信协议，和UE之间使用PPP协议通信。<br>- “IPV4V6(IPv4v6)”：表示IPV4V6双栈协议，同时为UE分配IPv4地址和IPv6地址。<br>- “IPV4/IPV6(IPv4/IPv6)”：表示支持IPv4协议或者IPv6协议，由系统自动选择支持哪种协议，优先选择IPv4协议。<br>- “ALL_PDP_TYPE(ALL PDP Type)”：表示支持所有PDP协议类型，不包含Non-IP类型，当指定IMSEPRE的PDP类型不存在之前类型时，选择所有协议类型。<br>默认值：无 |
| IPV4PDPADDRTYPE | 签约IPv4 PDP/PDN地址分配类型 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定签约IPv4 PDP/PDN地址分配类型。<br>前提条件：该参数在<br>“PDPTYPE(签约PDP/PDN类型)”<br>参数设置为<br>“IPV4(IPv4地址)”<br>或<br>“IPV4V6(IPv4v6)”<br>或<br>“IPV4/IPV6(IPv4/IPv6)”<br>时，才需要配置。<br>数据来源：整网规划<br>取值范围：<br>- “ALLOCATION_IPV4PDP_DYNAMIC(动态分配)”<br>- “ALL_STATIC_IPV4PDP_ADDR(所有静态分配的PDP地址)”<br>- “SPECIAL_STATIC_IPV4PDP_ADDR(指定静态分配的PDP地址)”<br>默认值：无 |
| IPV4 | 签约IPv4 PDP/PDN地址 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定UE的IPv4地址。<br>前提条件：该参数在<br>“IPV4PDPADDRTYPE（签约IPv4 PDP/PDN地址分配类型）”<br>参数设置为<br>“SPECIAL_STATIC_IPV4PDP_ADDR(指定静态分配的PDP地址)”<br>时，才需要配置。<br>数据来源：整网规划<br>取值范围：0.0.0.0～255.255.255.255<br>默认值：无 |
| IPV6PDPADDRTYPE | 签约IPv6 PDP/PDN地址分配类型 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定签约IPv6 PDP/PDN地址分配类型。<br>前提条件：该参数在<br>“PDPTYPE(签约PDP/PDN类型)”<br>参数设置为<br>“IPV6(IPv6地址)”<br>或<br>“IPv4v6(IPv4v6)”<br>或<br>“IPv4/IPv6(IPv4/IPv6)”<br>时，才需要配置。<br>数据来源：整网规划<br>取值范围：<br>- “DYNAMIC(动态分配)”<br>- “ALL_STATIC_IPV6PDP_ADDR(所有静态分配的PDP地址)”<br>- “SPECIAL_STATIC_IPV6PDP_ADDR(指定静态分配的PDP地址)”<br>默认值：无 |
| IPV6 | 签约IPv6 PDP/PDN地址 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定UE的IPv6地址。<br>前提条件：该参数在<br>“IPV6PDPADDRTYPE（签约IPv6 PDP/PDN地址分配类型）”<br>参数设置为<br>“SPECIAL_STATIC_IPV6PDP_ADDR(指定静态分配的PDP地址)”<br>时显示。<br>数据来源：整网规划<br>取值范围：0:0:0:0:0:0:0:0～FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无 |
| CORRECTAPNNI | 修改签约APNNI | 可选必选说明：可选参数<br>参数含义：该参数用于标识是否要修改签约的APNNI。<br>数据来源：本端规划<br>取值范围：<br>- “YES(是)”：用于增加一条修改签约的APNNI记录。<br>- “NO(否)”<br>默认值：<br>“NO(否)”<br>。 |
| NEWAPNNI | 新的签约APNNI | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定新的APN网络标识。<br>前提条件：该参数在<br>“CORRECTAPNNI(修改签约APNNI)”<br>参数设置为<br>“YES(是)”<br>时，才需要配置。<br>数据来源：本端规划<br>取值范围：1～62位字符串<br>默认值：无<br>配置原则：<br>- APN网络标识地址由一个或多个LABEL构成，各LABEL间用“.”间隔。每个LABEL的构成字符只能是字母A～Z或a～z、数字0～9和中划线“-”。<br>- APN网络标识地址不能以“rac”、“lac”、“sgsn”或“rnc”开头，不能以“.gprs”结尾，不能取值为“*”。<br>- 输入的APN NI参数应为类似于XXX.XXX的形式，如“123.net”。如果配置的APN NI不正确，可能因DNS解析失败而导致激活流程失败。 |
| NEWPDPTYPE | 新的签约PDP类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定新的PDP类型，如果签约的PDP类型为Non-IP类型，本参数不生效。<br>数据来源：整网规划<br>取值范围：<br>- “IPV4(IPv4地址)”<br>- “IPV6(IPv6地址)”<br>- “PPP(PPP)”<br>- “IPV4V6(IPv4v6)”<br>- “IPV4/IPV6(IPv4/IPv6)”<br>- “NOT_MODIFY(不修改)”<br>默认值：无<br>说明：注意<br>“NEWPDPTYPE(新的签约PDP类型)”<br>参数不输入时，<br>“NEWPDPTYPE(新的签约PDP类型)”<br>参数取值为<br>“IPV4(IPv4地址)”<br>，<br>“NEWIPV4PDPADDRTYPE(新的签约IPv4 PDP地址分配类型)”<br>取值为<br>“DYNAMIC(动态分配)”<br>。 |
| NEWIPV4PDPADDRTYPE | 新的签约IPv4 PDP地址分配类型 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定新的签约IPv4 PDP地址分配类型。<br>前提条件：该参数在<br>“NEWPDPTYPE(新的签约PDP类型)”<br>参数设置为<br>“IPV4(IPV4地址)”<br>或<br>“IPV4V6(IPv4v6)”<br>或<br>“IPV4/IPV6(IPv4/IPv6)”<br>时，才需要配置。<br>数据来源：整网规划<br>取值范围：<br>- “DYNAMIC(动态分配)”<br>- “STATIC(静态分配)”<br>默认值：无 |
| NEWIPV4 | 新的IPv4 PDP/PDN地址 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定新的IPv4地址。<br>前提条件：该参数在<br>“NEWIPV4PDPADDRTYPE（新的签约IPv4 PDP/PDN地址分配类型）”<br>参数设置为<br>“STATIC(静态分配)”<br>时，才需要配置。<br>数据来源：整网规划<br>取值范围：0.0.0.0～255.255.255.255<br>默认值：无 |
| NEWIPV6PDPADDRTYPE | 新的签约IPv6 PDP地址分配类型 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定新的签约IPv6 PDP地址分配类型。<br>前提条件：该参数在<br>“NEWPDPTYPE(新的签约PDP/PDN类型)”<br>参数设置为<br>“IPV6(IPv6地址)”<br>或<br>“IPV4V6(IPv4v6)”<br>或<br>“IPV4/IPV6(IPv4/IPv6)”<br>时，才需要配置。<br>数据来源：整网规划<br>取值范围：<br>- “DYNAMIC(动态分配)”<br>- “STATIC(静态分配)”<br>默认值：无 |
| NEWIPV6 | 新的IPv6 PDP/PDN地址 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定新的IPv6地址。<br>前提条件：该参数在<br>“NEWIPV6PDPADDRTYPE（新的签约IPv6 PDP/PDN地址分配类型）”<br>参数设置为<br>“STATIC(静态分配)”<br>时显示。<br>数据来源：整网规划<br>取值范围：0:0:0:0:0:0:0:0～FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SMSUBDATA]] · 签约数据纠正参数（SMSUBDATA）

## 使用实例

增加一条签约数据纠正参数信息，其用户范围为所有用户，匹配条件为签约数据，签约APNNI范围为所有APNNI，PDP协议类型为PPP协议，不修改签约APNNI，不修改新的PDP类型：

ADD SMSUBDATA: SUBRANGE=ALL_USER, TYPE=SUBSCRIBED_PARAMETER, APNNIRANGE=APNNI_ALL, PDPTYPE=PPP, CORRECTAPNNI=NO, NEWPDPTYPE=NOT_MODIFY;

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-SMSUBDATA.md`
