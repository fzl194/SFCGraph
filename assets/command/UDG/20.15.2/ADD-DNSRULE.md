---
id: UDG@20.15.2@MMLCommand@ADD DNSRULE
type: MMLCommand
name: ADD DNSRULE（添加DNS规则）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: DNSRULE
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 10000
category_path:
- 用户面服务管理
- 业务匹配策略
- 业务匹配公共配置
- 业务规则管理
- DNS规则
status: active
---

# ADD DNSRULE（添加DNS规则）

## 功能

**适用NF：PGW-U、UPF**

当系统为处于边缘节点的应用提供DNSLite业务时，该命令用于新增一条DNS规则，该DNS规则被称为静态DNS规则。

DNS规则是一种具有域名匹配功能的分流规则，包含了服务器域名和服务器 IP地址的对应关系。基于DNS规则分流可以实现以下功能：当数据流的报文中携带服务器的域名时，如果命中DNS Rule，则返回DNS响应，将服务器的IP地址返回给UE。当数据流的报文根据域名返回的IP地址发送数据报文时，支持基于服务器的IP地址命中DNS规则，将数据流本地分流到服务器。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为10000。
- APPLICATIONID与DNSRULENAME唯一标识一条记录。
- 当SET DNSLITEPARA中DNSLPOLICYSW使能后该规则才生效。
- 每个APPLICATIONID和DOMAIN下配置的IPADDRESS不可以重复。
- 每个APPLICATIONID下的DOMAIN配置的IPV4ADDRESS最大不超过16个。
- 每个APPLICATIONID下的DOMAIN配置的IPV6ADDRESS最大不超过16个。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APPLICATIONID | 应用标识 | 可选必选说明：必选参数<br>参数含义：该参数用于配置DNS列表所属的应用标识。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不区分大小写。<br>默认值：无<br>配置原则：该参数用于和SMF下发的PDR中携带的Application ID进行匹配。 |
| DNSRULENAME | DNS规则名称 | 可选必选说明：必选参数<br>参数含义：该参数用于配置DNS规则名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不区分大小写。<br>默认值：无<br>配置原则：无 |
| DOMAIN | 域名 | 可选必选说明：必选参数<br>参数含义：该参数用于设置DNS规则的服务器域名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不区分大小写。<br>默认值：无<br>配置原则：无 |
| IPVERSION | IP地址类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定DNS域名的IP地址类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- IPV4：IPv4地址类型。<br>- IPV6：IPv6地址类型。<br>默认值：无<br>配置原则：该DOMAIN对应的地址类型。 |
| IPV4ADDRESS | IPv4地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IPVERSION”配置为“IPV4”时为必选参数。<br>参数含义：该参数用于指定域名对应的IPv4类型的服务器地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| IPV6ADDRESS | IPv6地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IPVERSION”配置为“IPV6”时为必选参数。<br>参数含义：该参数用于指定域名对应的IPv6类型的服务器地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |
| DNSTTL | DNS TTL | 可选必选说明：可选参数<br>参数含义：该参数用于设置域名解析信息在DNS中的存在时间。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：86400<br>配置原则：无 |
| CFGDOMAINNAME | 配置域名称 | 可选必选说明：可选参数<br>参数含义：该参数表示命令所属公共配置域的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/DNSRULE]] · DNS规则（DNSRULE）

## 使用实例

在需要配置轻量DNS规则时，执行该命令设置新增规则：

```
ADD DNSRULE: APPLICATIONID="app1", DNSRULENAME="rule1", DOMAIN="www.huawei1.com", IPVERSION=IPV4, IPV4ADDRESS="10.0.0.1", DNSTTL=1;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/ADD-DNSRULE.md`
