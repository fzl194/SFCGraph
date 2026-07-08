---
id: UNC@20.15.2@MMLCommand@MOD M2MSERVER
type: MMLCommand
name: MOD M2MSERVER（修改M2M服务器）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: M2MSERVER
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- M2M
- M2M服务器
status: active
---

# MOD M2MSERVER（修改M2M服务器）

## 功能

**适用NF：PGW-C、SMF**

该命令用来修改M2M服务器组下的M2M服务器的相关属性。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GROUPNAME | M2M服务器组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定M2M服务器所属M2M服务器组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~31。不区分大小写，不支持空格。<br>默认值：无<br>配置原则：<br>GROUPNAME参数依赖M2MSERVERGRP命令的GROUPNAME参数。 |
| SERVERINDEX | M2M服务器索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定M2M服务器索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1。<br>默认值：无<br>配置原则：无 |
| SERVERIPTYPE | M2M服务器IP地址类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定M2M服务器IP地址类型。<br>数据来源：本端规划<br>取值范围：<br>- IPV4（IPv4）<br>- IPV6（IPv6）<br>默认值：无<br>配置原则：<br>SERVERIPTYPE参数依赖M2MSERVERGRP命令的SERVERIPTYPE参数。 |
| SERVERIPV4ADDR | M2M服务器IPv4地址 | 可选必选说明：该参数在"SERVERIPTYPE"配置为"IPV4"时为条件必选参数。<br>参数含义：该参数用于指定M2M服务器IPv4地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。必须是合法的单播地址。<br>默认值：无<br>配置原则：无 |
| SERVERIPV6ADDR | M2M服务器IPv6地址 | 可选必选说明：该参数在"SERVERIPTYPE"配置为"IPV6"时为条件必选参数。<br>参数含义：该参数用于指定M2M服务器IPv6地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。必须是合法的单播地址。<br>默认值：无<br>配置原则：无 |
| SERVERPORT | 服务器端口号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定M2M服务器的端口号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~65535。该端口号应与M2M服务器的端口一致。<br>默认值：无<br>配置原则：无 |
| REALMSWITCH | 域名配置开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定是否配置域名。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE（不使能）<br>- ENABLE（使能）<br>默认值：无<br>配置原则：无 |
| SERVERREALM | M2M服务器域名 | 可选必选说明：该参数在"REALMSWITCH"配置为"ENABLE"时为条件必选参数。<br>参数含义：该参数用于指定M2M Server的域名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~63。不区分大小写，不支持空格。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@M2MSERVER]] · M2M服务器（M2MSERVER）

## 使用实例

修改配置"m2msrvgroup01"M2M服务器组下的M2M服务器的相关属性：

```
MOD M2MSERVER: GROUPNAME="m2msrvgroup01", SERVERINDEX=1, SERVERIPTYPE=IPV4, SERVERIPV4ADDR="10.107.242.17", SERVERPORT=5859;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-M2MSERVER.md`
