---
id: UNC@20.15.2@MMLCommand@TST AAA
type: MMLCommand
name: TST AAA（测试AAA服务器）
nf: UNC
version: 20.15.2
verb: TST
object_keyword: AAA
command_category: 调测类
applicable_nf:
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- RADIUS管理
- RADIUS维护
- 服务器检测
status: active
---

# TST AAA（测试AAA服务器）

## 功能

**适用NF：PGW-C、SMF**

该命令用于向AAA服务器发送探测消息，根据回显来推断UNC和AAA服务器之间的连接是否正常。

## 注意事项

- 该命令执行后立即生效。
- 在执行该命令前需要先使用ADD RDSSVR命令配置要探测的鉴权服务器或者计费服务器，否则探测命令会执行失败。
- 该命令执行的过程中不能执行其他命令，等待该命令执行完成后才能执行其他命令。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SERVERTYPE | 服务器类型 | 可选必选说明：必选参数<br>参数含义：该参数表示被探测的AAA服务器的服务器类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- AUTHENTICATION：鉴权服务器。<br>- ACCOUNTING：计费服务器。<br>默认值：无<br>配置原则：无 |
| VPNINSTANCE | VPN实例 | 可选必选说明：可选参数<br>参数含义：该参数表示被探测的AAA服务器组所属的VPN实例名。其中，VPN实例名可通过ADD RDSSVR进行配置。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：无 |
| USERNAME | 用户名 | 可选必选说明：条件可选参数<br>前提条件：该参数在“SERVERTYPE”配置为“ACCOUNTING” 或 “AUTHENTICATION”时为可选参数。<br>参数含义：该参数用于设置发送探测消息中携带的用户名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：AAAtester<br>配置原则：无 |
| PASSWORD | 密码 | 可选必选说明：条件可选参数<br>前提条件：该参数在“SERVERTYPE”配置为“AUTHENTICATION”时为可选参数。<br>参数含义：该参数用于设置发送探测鉴权请求消息中携带的密码。<br>数据来源：本端规划<br>取值范围：密码类型，输入长度范围为1～128。<br>默认值：AAAtester<br>配置原则：无 |
| PWDCONFM | 确认密码 | 可选必选说明：条件可选参数<br>前提条件：该参数在“SERVERTYPE”配置为“AUTHENTICATION”时为可选参数。<br>参数含义：确认指定的鉴权请求消息中携带的密码。<br>数据来源：本端规划<br>取值范围：密码类型，输入长度范围为1～128。<br>默认值：AAAtester<br>配置原则：无 |
| IPVERSION | IP Address Version | 可选必选说明：必选参数<br>参数含义：用于指定IP地址类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- IPV4：表示地址类型为IPv4。<br>- IPV6：表示地址类型为IPv6。<br>默认值：无<br>配置原则：无 |
| IPADDRESS | 服务器IP地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IPVERSION”配置为“IPV4”时为必选参数。<br>参数含义：该参数表示被探测的AAA服务器的IP地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| IPV6ADDRESS | 服务器IPv6地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IPVERSION”配置为“IPV6”时为必选参数。<br>参数含义：指定IPv6类型的地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。采用冒号分十六进制X:X:X:X:X:X:X:X格式。<br>默认值：无<br>配置原则：无 |
| PORT | 端口 | 可选必选说明：可选参数<br>参数含义：指定RADIUS服务器的端口号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～65535。该端口应于RADIUS服务器的端口一致。<br>默认值：无<br>配置原则：<br>- RADIUS鉴权服务器使用的鉴权服务器的端口一般为1812。<br>- RADIUS计费服务器使用的计费服务器的端口一般为1813。 |
| IMSI | IMSI | 可选必选说明：可选参数<br>参数含义：该参数用于设置发送探测消息中携带的IMSI。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1~15。<br>默认值：无<br>配置原则：无 |
| MSISDN | MSISDN | 可选必选说明：可选参数<br>参数含义：该参数用于设置发送探测消息中携带的MSISDN。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1~15。<br>默认值：无<br>配置原则：无 |
| IMEI | IMEI | 可选必选说明：可选参数<br>参数含义：该参数用于设置发送探测消息中携带的IMEI。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1~16。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/AAA]] · 测试AAA服务器（AAA）

## 使用实例

假设运营商需要向AAA服务器发送探测消息，根据回显来推断UNC和AAA服务器之间的连接是否正常，则执行如下命令：

```
TST AAA: SERVERTYPE=ACCOUNTING, IPVERSION=IPV4, IPADDRESS="192.168.1.1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/测试AAA服务器（TST-AAA）_09896762.md`
