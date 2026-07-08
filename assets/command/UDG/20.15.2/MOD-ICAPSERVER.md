---
id: UDG@20.15.2@MMLCommand@MOD ICAPSERVER
type: MMLCommand
name: MOD ICAPSERVER（修改ICAP服务器）
nf: UDG
version: 20.15.2
verb: MOD
object_keyword: ICAPSERVER
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- ICAPC管理
- ICAP服务器
status: active
---

# MOD ICAPSERVER（修改ICAP服务器）

## 功能

**适用NF：PGW-U、UPF**

该命令用于修改一个ICAP Server相关的配置，包括ICAP Server的主机IP地址、PORT、TCP尝试建链间隔、OPTIONS消息重发间隔等。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ICAPSERVERNAME | ICAP服务器名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定ICAP Server的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格。不区分大小写。<br>默认值：无<br>配置原则：无 |
| ICAPSERVERTYPE | ICAP服务器类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定ICAP Server的服务器类型。<br>数据来源：本端规划<br>取值范围：<br>- URL_FILTERING：支持URL过滤的ICAP服务器。<br>默认值：无<br>配置原则：无 |
| ICAPSVRIPTYPE | ICAP 服务器IP地址类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定ICAP Server的IP地址类型。<br>数据来源：本端规划<br>取值范围：<br>- IPV4：IPv4地址类型。<br>- IPV6：IPv6地址类型。<br>默认值：无<br>配置原则：无 |
| ICAPSERVERIPV4 | ICAP服务器IPv4地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“ICAPSVRIPTYPE”配置为“IPV4”时为必选参数。<br>参数含义：该参数用于指定ICAP Server的IPv4地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。采用点分十进制格式。不支持0.0.0.0和255.255.255.255。<br>默认值：无<br>配置原则：无 |
| ICAPSERVERIPV6 | ICAP服务器IPv6地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“ICAPSVRIPTYPE”配置为“IPV6”时为必选参数。<br>参数含义：该参数用于指定ICAP Server的IPv6地址。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。采用冒号分十六进制X:X:X:X:X:X:X:X格式。不支持全F。<br>默认值：无<br>配置原则：无 |
| ICAPSERVERPORT | ICAP服务器端口 | 可选必选说明：可选参数<br>参数含义：该参数用于指定ICAP Server的通信TCP端口号。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为1~65534。<br>默认值：无<br>配置原则：无 |
| VPNINSTANCE | VPN实例 | 可选必选说明：可选参数<br>参数含义：该参数用于指定VPN的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格。不区分大小写。<br>默认值：无<br>配置原则：无 |
| TCPRETRYTIME | TCP尝试建链间隔（秒） | 可选必选说明：可选参数<br>参数含义：该参数用于指定TCP尝试建链间隔。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1~3600。<br>默认值：无<br>配置原则：无 |
| OPTIONINTERVAL | OPTIONS消息的间隔（秒） | 可选必选说明：可选参数<br>参数含义：该参数用于指定OPTIONS消息的间隔。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1~600。<br>默认值：无<br>配置原则：无 |
| CFGDOMAINNAME | 配置域名称 | 可选必选说明：可选参数<br>参数含义：该参数表示命令所属公共配置域的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@ICAPSERVER]] · ICAP服务器（ICAPSERVER）

## 使用实例

该命令用于修改指定名称的ICAP Server配置：

```
MOD ICAPSERVER: ICAPSERVERNAME="is1", ICAPSERVERTYPE=URL_FILTERING, ICAPSVRIPTYPE=IPV4, ICAPSERVERIPV4="172.16.39.140", ICAPSERVERPORT=1355, TCPRETRYTIME=20, OPTIONINTERVAL=100;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/MOD-ICAPSERVER.md`
