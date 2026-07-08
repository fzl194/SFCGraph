---
id: UDG@20.15.2@MMLCommand@ADD IFIPV6ADDRPOLICY
type: MMLCommand
name: ADD IFIPV6ADDRPOLICY（添加IPv6地址策略）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: IFIPV6ADDRPOLICY
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
max_records: 819200
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 接口管理
- IPv6地址策略
status: active
---

# ADD IFIPV6ADDRPOLICY（添加IPv6地址策略）

## 功能

该命令用于添加IPv6地址策略。当网络管理者需要指定和预知系统发送报文的源/目的地址时，可以通过该命令定义一组地址选择规则，这些规则构成地址选择策略表。该表类似于路由表，使用最长匹配原则查找规则。地址选择的结果是由源地址和目的地址共同决定的。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为819200。
- 系统存在缺省策略表项，即::1、::、2002::、FC00::、::FFFF:0.0.0.0。如果系统中的VPN配置了IPv6地址族，则系统自动会将缺省策略表项::1、::、2002::、FC00::、::FFFF:0.0.0.0加入VPN中。每个VPN最多配置50条表项。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPV6ADDRPREFIX | IPv6地址 | 可选必选说明：必选参数<br>参数含义：该参数用于指定IPv6前缀地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。<br>默认值：无 |
| PRIFIXLEN | IPv6前缀长度 | 可选必选说明：必选参数<br>参数含义：该参数用于指定接口IPv6地址前缀长度。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～128。<br>默认值：无 |
| DSTPRECEDENCE | 目的地址优先级 | 可选必选说明：必选参数<br>参数含义：该参数用于指定IPv6前缀地址作为目的地址的优先级。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无 |
| SRCPRECEDENCE | 源地址优先级 | 可选必选说明：必选参数<br>参数含义：该参数用于指定IPv6前缀地址作为源地址的优先级。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无 |
| VPNNAME | VPN实例名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定IPv6地址策略的VPN实例名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/IFIPV6ADDRPOLICY]] · IPv6地址策略（IFIPV6ADDRPOLICY）

## 使用实例

添加IPv6地址策略：

```
ADD IFIPV6ADDRPOLICY:VPNNAME="vrf1",IPV6ADDRPREFIX="2001:db8::2",PRIFIXLEN=64,DSTPRECEDENCE=10,SRCPRECEDENCE=10;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/ADD-IFIPV6ADDRPOLICY.md`
