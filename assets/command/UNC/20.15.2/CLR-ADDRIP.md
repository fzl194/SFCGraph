---
id: UNC@20.15.2@MMLCommand@CLR ADDRIP
type: MMLCommand
name: CLR ADDRIP（清除地址）
nf: UNC
version: 20.15.2
verb: CLR
object_keyword: ADDRIP
command_category: 动作类
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
- UE地址管理
- UE地址池管理
- 地址管理
status: active
---

# CLR ADDRIP（清除地址）

## 功能

**适用NF：GGSN、PGW-C、SMF**

该命令用于清除路由地址或静态地址缓存。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CLRTYPE | 清除方式 | 可选必选说明：必选参数<br>参数含义：该命令用于指定清除路由地址或静态地址缓存的方式。<br>数据来源：本端规划<br>取值范围：<br>- DELETEALL（清除所有地址）<br>- DELETEALLBYAPN（清除该APN下的所有地址）<br>- DELETESINGLE（清除单条地址）<br>默认值：无<br>配置原则：无 |
| ADDRIPTYPE | 本地地址类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定本地地址类型。<br>数据来源：本端规划<br>取值范围：<br>- ROUTEIP（路由IP地址）<br>- STATICIP（静态IP地址）<br>默认值：无<br>配置原则：无 |
| APN | APN名称 | 可选必选说明：该参数在"CLRTYPE"配置为"DELETEALLBYAPN"、"DELETESINGLE"时为条件必选参数。<br>参数含义：该参数用于指定APN实例名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。<br>默认值：无<br>配置原则：无 |
| IPVERSION | IP地址类型 | 可选必选说明：该参数在"CLRTYPE"配置为"DELETESINGLE"时为条件必选参数。<br>参数含义：该参数用于指定IP地址类型。<br>数据来源：本端规划<br>取值范围：<br>- “IPv4（IPv4）”：IPv4<br>- “IPv6（IPv6）”：IPv6<br>默认值：无<br>配置原则：无 |
| IPV4 | IPV4地址 | 可选必选说明：该参数在"IPVERSION"配置为"IPv4"时为条件必选参数。<br>参数含义：该参数用于指定IPv4地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| IPV4MASK | IPV4掩码 | 可选必选说明：该参数在"IPVERSION"配置为"IPv4"时为条件可选参数。<br>参数含义：该参数用于指定IPv4地址的网络掩码。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~4294967295。<br>默认值：无<br>配置原则：无 |
| IPV6 | IPV6地址 | 可选必选说明：该参数在"IPVERSION"配置为"IPv6"时为条件必选参数。<br>参数含义：该参数用于指定IPv6地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |
| IPV6PREFIX | IPV6前缀 | 可选必选说明：该参数在"IPVERSION"配置为"IPv6"时为条件可选参数。<br>参数含义：该参数用于指定IPv6地址的前缀。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~4294967295。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/ADDRIP]] · 地址缓存（ADDRIP）

## 使用实例

清除所有静态地址缓存。

```
CLR ADDRIP:CLRTYPE=DELETEALL,ADDRIPTYPE=STATICIP;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/清除地址（CLR-ADDRIP）_06775896.md`
