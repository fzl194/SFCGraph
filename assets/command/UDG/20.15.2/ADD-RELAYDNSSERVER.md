---
id: UDG@20.15.2@MMLCommand@ADD RELAYDNSSERVER
type: MMLCommand
name: ADD RELAYDNSSERVER（增加媒体中继的DNS属性）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: RELAYDNSSERVER
command_category: 配置类
applicable_nf:
- UPF
- PGW-U
effect_mode: 立即生效
is_dangerous: false
max_records: 2
category_path:
- 用户面服务管理
- 业务控制策略
- 媒体中继
- 媒体中继DNS服务器配置
status: active
---

# ADD RELAYDNSSERVER（增加媒体中继的DNS属性）

## 功能

**适用NF：UPF、PGW-U**

该命令用于增加媒体中继的DNS属性。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为2。
- DNS服务器IP需至少配置其中一个。
- DNS服务器IP地址配置全零为无效地址。
- IPv6地址目前不支持配置。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DNSSERVERNAME | DNS服务器名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定DNS服务器名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| VPNNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。区分大小写。<br>默认值：无<br>配置原则：<br>- 输入单空格将删除该参数已有配置项。<br>- 绑定VPN时需要确保该VPN已经配置（ADD VPNINST）。 |
| MDNSSRVIPV4 | IPv4主DNS服务器IP | 可选必选说明：可选参数<br>参数含义：该参数用于配置IPv4主DNS服务器地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。采用点分十进制格式。不支持255.255.255.255。<br>默认值：无<br>配置原则：无 |
| SDNSSRVIPV4 | IPv4备DNS服务器IP | 可选必选说明：可选参数<br>参数含义：该参数用于配置IPv4备DNS服务器地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。采用点分十进制格式。不支持255.255.255.255。<br>默认值：无<br>配置原则：无 |
| MDNSSRVIPV6 | IPv6主DNS服务器IP | 可选必选说明：可选参数<br>参数含义：该参数用于配置IPv6主DNS服务器地址。<br>数据来源：本端规划<br>取值范围：冒号十六进制。<br>默认值：无<br>配置原则：无 |
| SDNSSRVIPV6 | IPv6备DNS服务器IP | 可选必选说明：可选参数<br>参数含义：该参数用于配置IPv6备DNS服务器地址。<br>数据来源：本端规划<br>取值范围：冒号十六进制。<br>默认值：无<br>配置原则：无 |
| TIMEOUT | 超时时间间隔（秒） | 可选必选说明：可选参数<br>参数含义：该参数用于指定DNS请求等待响应超时时间。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~3，单位是秒。<br>默认值：1<br>配置原则：无 |
| RESENDTIMES | 重发次数（次数） | 可选必选说明：可选参数<br>参数含义：该参数用于指定DNS请求消息超时重发次数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~3，单位是次数。<br>默认值：1<br>配置原则：无 |
| WALVALUE | WAL-Value流控 | 可选必选说明：可选参数<br>参数含义：该参数用于表示每个Pod最多发送的DNS请求数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0或者50~10000。<br>默认值：1000<br>配置原则：无 |
| CFGDOMAINNAME | 配置域名称 | 可选必选说明：可选参数<br>参数含义：该参数表示命令所属公共配置域的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：输入单空格将删除该参数已有配置项。 |
| DNSDETECTSW | DNS探测功能开关 | 可选必选说明：可选参数<br>参数含义：该参数用于控制开启或关闭DNS探测功能。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能媒体中继DNS探测功能开关。<br>- ENABLE：使能媒体中继DNS探测功能开关。<br>默认值：无<br>配置原则：无 |
| DETECTDOMAINNM | 探测域名 | 可选必选说明：条件必选参数<br>前提条件：该参数在“DNSDETECTSW”配置为“ENABLE”时为必选参数。<br>参数含义：该参数表示需要探测的域名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为0～63。不支持空格，不区分大小写。仅支持数字、字母和'-'和'.'进行组合，'-'和'.'不能出现在开头或结尾。<br>默认值：无<br>配置原则：无 |
| DETECTTIMER | 探测功能定时器（秒） | 可选必选说明：条件可选参数<br>前提条件：该参数在“DNSDETECTSW”配置为“ENABLE”时为可选参数。<br>参数含义：该参数用于设置探测功能定时器间隔。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围1~1440，单位是秒。<br>默认值：300<br>配置原则：无 |

## 操作的配置对象

- [媒体中继的DNS属性（RELAYDNSSERVER）](configobject/UDG/20.15.2/RELAYDNSSERVER.md)

## 使用实例

假设需要新增媒体中继DNS属性，则命令如下：

```
ADD RELAYDNSSERVER: DNSSERVERNAME="dns01", MDNSSRVIPV4="10.0.0.1", SDNSSRVIPV4="10.0.0.2";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/增加媒体中继的DNS属性（ADD-RELAYDNSSERVER）_17630205.md`
