---
id: UNC@20.15.2@MMLCommand@MOD PCSCFIP
type: MMLCommand
name: MOD PCSCFIP（修改P-CSCF地址配置）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: PCSCFIP
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
- IMS管理
- P-CSCF管理
- P-CSCF的IP地址
status: active
---

# MOD PCSCFIP（修改P-CSCF地址配置）

## 功能

**适用NF：PGW-C、SMF、GGSN**

该命令用于修改P-CSCF IP地址配置。

## 注意事项

该命令执行后只对新激活用户生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GROUPNAME | P-CSCF组名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定P-CSCF组的名字，在系统内唯一。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。只允许输入字母、数字、“.”、“_”和“-”。字母会被转换为小写字母进行存储和处理。<br>默认值：无<br>配置原则：<br>该参数使用ADD PCSCFGROUP命令配置生成。 |
| IPVERSION | IP地址版本 | 可选必选说明：必选参数<br>参数含义：该参数用于指定P-CSCF地址类型。<br>数据来源：本端规划<br>取值范围：<br>- “IPV4（IPV4）”：IPv4地址类型<br>- “IPV6（IPV6）”：IPv6地址类型<br>默认值：无<br>配置原则：无 |
| PCSCFIPV4 | IPv4地址 | 可选必选说明：该参数在"IPVERSION"配置为"IPV4"时为条件必选参数。<br>参数含义：该参数用于指定IPv4类型的P-CSCF地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。点分十进制格式。有效的IPv4地址必须是A、B或者C类地址，且不能为环回地址（127.x.y.z）。<br>默认值：无<br>配置原则：无 |
| PCSCFIPV6 | IPv6地址 | 可选必选说明：该参数在"IPVERSION"配置为"IPV6"时为条件必选参数。<br>参数含义：该参数用于指定IPv6类型的P-CSCF地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。冒号分十六进制，格式为X:X:X:X:X:X:X:X。除了组播地址、链路本地地址、环回地址或未指定的地址为非法地址外，其他都为合法地址。<br>默认值：无<br>配置原则：无 |
| ALLOCTYPE | P-CSCF获取方式 | 可选必选说明：可选参数<br>参数含义：该参数用于指定p-cscf服务器地址分配方式。<br>数据来源：全网规划<br>取值范围：<br>- “LOCAL（本地分配）”：在网络规划p-cscf服务器地址由UNC本地配置的时，配置分组类型为LOCAL。<br>- “DHCP（DHCP分配）”：在网络规划p-cscf服务器地址由DHCP服务器分配时，配置分组类型为DHCP。<br>默认值：无<br>配置原则：无 |
| WEIGHT | 权重 | 可选必选说明：该参数在"ALLOCTYPE"配置为"LOCAL"时为条件必选参数。<br>参数含义：该参数用于指定该P-CSCF的能力，权重越大说明性能越高，被选中的概率就越大。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~100。<br>默认值：无<br>配置原则：无 |
| PAIRID | 结对ID | 可选必选说明：可选参数<br>参数含义：该参数用于指定P-CSCF IP的结对ID，结对ID相同的P-CSCF互为容灾。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~255。<br>默认值：无<br>配置原则：<br>UNC下发一对P-CSCF IP给UE时，第二个IP优先选择和第一个IP相同Pair ID的地址，建议互为容灾的两个P-CSCF IP配置相同的Pair ID，当相同Pair ID的地址存在多个时，按照权重来选择。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PCSCFIP]] · P-CSCF地址配置（PCSCFIP）

## 使用实例

当配置信息需要变更，需要修改指定P-CSCF组的P-CSCF IP地址的配置，使用该命令。举例:P-CSCF组名为mygrp，IPVERSION为IPV4，PCSCFIPV4为192.168.1.70，修改WEIGHT为5，PAIRID为1：

```
MOD PCSCFIP: GROUPNAME="mygroup", IPVERSION=IPV4, PCSCFIPV4="192.168.1.70", ALLOCTYPE=LOCAL, WEIGHT=5, PAIRID=1;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-PCSCFIP.md`
