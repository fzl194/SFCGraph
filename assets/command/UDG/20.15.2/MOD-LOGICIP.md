---
id: UDG@20.15.2@MMLCommand@MOD LOGICIP
type: MMLCommand
name: MOD LOGICIP（修改逻辑IP地址信息）
nf: UDG
version: 20.15.2
verb: MOD
object_keyword: LOGICIP
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- IP管理
- IP配置
status: active
---

# MOD LOGICIP（修改逻辑IP地址信息）

## 功能

该命令用于修改逻辑IP配置。

> **说明**
> 该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPVERSION | IP地址类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定配置的IP地址的版本，用于区别配置的是IPv4地址还是IPv6地址。<br>数据来源：全网规划<br>取值范围：<br>- “IPv4（IPv4）”：IPv4地址<br>- “IPv6（IPv6）”：IPv6地址<br>默认值：无<br>配置原则：无 |
| LOGICIPV4 | IPv4地址 | 可选必选说明：该参数在"IPVERSION"配置为"IPv4"时为条件必选参数。<br>参数含义：该参数用于指定逻辑IPv4地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。业务地址不能配置为0.0.0.0、255.255.255.255和环回地址(127.x.y.z)。业务地址必须是A、B或者C类地址。<br>默认值：无<br>配置原则：<br>业务地址不能配置为0.0.0.0、255.255.255.255和环回地址(127.x.y.z)。业务地址必须是A、B或者C类地址。 |
| LOGICIPV6 | IPv6地址 | 可选必选说明：该参数在"IPVERSION"配置为"IPv6"时为条件必选参数。<br>参数含义：该参数用于指定逻辑IPv6地址。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。IPv6地址必须是全球单播地址，不能为::、FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址(::1)、链路本地地址(FE80::/10)和组播地址(FF00::/8)。<br>默认值：无<br>配置原则：<br>IPv6地址必须是全球单播地址，不能为::、FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址(::1)、链路本地地址(FE80::/10)和组播地址(FF00::/8)。 |
| IPV4MTU | IPv4 MTU | 可选必选说明：该参数在"IPVERSION"配置为"IPv4"时为条件必选参数。<br>参数含义：该参数用于指定IP层协议版本为IPv4时使用的MTU大小。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是328~9600。<br>默认值：无<br>配置原则：<br>当环境上存在“NP121”NP卡时该参数取值范围为328~3600，当不存在“NP121”NP卡时该参数取值范围为328~9600。环境中是否存在“NP121”NP卡可以使用DSP NPNODE命令查询，具体参考回显结果中是否存在“NP卡名称”为“NP121”的NP节点。 |
| IPV6MTU | IPv6 MTU值 | 可选必选说明：该参数在"IPVERSION"配置为"IPv6"时为条件必选参数。<br>参数含义：该参数用于指定IP层协议版本为IPv6时使用的MTU大小。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1280~9600。<br>默认值：无<br>配置原则：<br>当环境上存在“NP121”NP卡时该参数取值范围为1280~3600，当不存在“NP121”NP卡时该参数取值范围为1280~9600。环境中是否存在“NP121”NP卡可以使用DSP NPNODE命令查询，具体参考回显结果中是否存在“NP卡名称”为“NP121”的NP节点。 |
| DESC | 描述 | 可选必选说明：可选参数<br>参数含义：该参数用于描述逻辑IP地址的其他信息。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/LOGICIP]] · 逻辑IP地址信息（LOGICIP）

## 使用实例

将地址为"192.168.1.1"逻辑地址的允许发包大小值修改为1400。

```
MOD LOGICIP: IPVERSION=IPv4, LOGICIPV4="192.168.1.1", IPV4MTU=1400, DESC="test";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/MOD-LOGICIP.md`
