---
id: UNC@20.15.2@MMLCommand@MOD IFIPV6ADDRPOLICY
type: MMLCommand
name: MOD IFIPV6ADDRPOLICY（修改IPv6地址策略）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: IFIPV6ADDRPOLICY
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 接口管理
- IPv6地址策略
status: active
---

# MOD IFIPV6ADDRPOLICY（修改IPv6地址策略）

## 功能

该命令用于修改IPv6地址策略。

## 注意事项

该命令执行后立即生效。

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

- [IPv6地址策略（IFIPV6ADDRPOLICY）](configobject/UNC/20.15.2/IFIPV6ADDRPOLICY.md)

## 使用实例

修改IPv6地址策略：

```
MOD IFIPV6ADDRPOLICY:VPNNAME="vrf1",IPV6ADDRPREFIX="2001:db8::2",PRIFIXLEN=64,DSTPRECEDENCE=10,SRCPRECEDENCE=10;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改IPv6地址策略（MOD-IFIPV6ADDRPOLICY）_49802314.md`
