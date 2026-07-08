---
id: UDG@20.15.2@MMLCommand@MOD SFIPSRVIP
type: MMLCommand
name: MOD SFIPSRVIP（修改SFIP业务IP）
nf: UDG
version: 20.15.2
verb: MOD
object_keyword: SFIPSRVIP
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- SFIP管理
- 网络管理
- SFIP业务IP
status: active
---

# MOD SFIPSRVIP（修改SFIP业务IP）

## 功能

该命令用于修改指定SFIP业务IP地址。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SERVICETYPENAME | 业务类型名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定SFIP业务类型名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：无 |
| IPVERSION | IP版本 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SFIP业务IP的版本信息。<br>数据来源：本端规划<br>取值范围：<br>- IPV4：表示地址类型为IPv4。<br>- IPV6：表示地址类型为IPv6。<br>- IPV4_IPV6：同时支持IPv4和IPv6地址。<br>默认值：无<br>配置原则：无 |
| IPV4ADDR | IPv4 地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IPVERSION”配置为“IPV4” 或 “IPV4_IPV6”时为必选参数。<br>参数含义：该参数用于指定SFIP业务的IPv4地址。当SFIP用于DNS业务场景时，该IP为提供DNS查询业务的服务器IPv4地址。<br>数据来源：全网规划<br>取值范围：有效的IPv4地址。<br>默认值：无<br>配置原则：无 |
| IPV6ADDR | IPv6 地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IPVERSION”配置为“IPV6” 或 “IPV4_IPV6”时为必选参数。<br>参数含义：该参数用于指定SFIP业务的IPv6地址。当SFIP用于DNS业务场景时，该IP为提供DNS查询业务的服务器IPv6地址。<br>数据来源：全网规划<br>取值范围：有效的IPv6地址。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/SFIPSRVIP]] · SFIP业务IP（SFIPSRVIP）

## 使用实例

修改SFIP业务IP地址，业务类型名称为dns，IP地址类型为IPv4，IPv4地址为192.168.1.1：

```
MOD SFIPSRVIP: SERVICETYPENAME="dns", IPVERSION=IPV4, IPV4ADDR="192.168.1.1";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改SFIP业务IP（MOD-SFIPSRVIP）_91652972.md`
