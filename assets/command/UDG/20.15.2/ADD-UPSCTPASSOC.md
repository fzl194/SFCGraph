---
id: UDG@20.15.2@MMLCommand@ADD UPSCTPASSOC
type: MMLCommand
name: ADD UPSCTPASSOC（增加SCTP耦联测量对象）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: UPSCTPASSOC
command_category: 配置类
applicable_nf:
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 200
category_path:
- 用户面服务管理
- SCTP管理
- SCTP测量对象
status: active
---

# ADD UPSCTPASSOC（增加SCTP耦联测量对象）

## 功能

**适用NF：UPF**

此命令用于增加SCTP耦联测量对象。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为200。
- 该命令相关的功能当前版本暂不支持。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| OBJECTID | SCTP偶联测量对象实例标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定SCTP耦联测量对象实例标识。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～200。<br>默认值：无<br>配置原则：无 |
| IPVERSION | IP版本 | 可选必选说明：必选参数<br>参数含义：该参数用于指定SCTP耦联测量对象的IP地址类型。<br>数据来源：对端协商<br>取值范围：枚举类型。<br>- IPV4：IPv4地址类型。<br>- IPV6：IPv6地址类型。<br>默认值：无<br>配置原则：无 |
| LOCALADDRIPV4 | 本端主IPv4地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IPVERSION”配置为“IPV4”时为必选参数。<br>参数含义：该参数用于指定SCTP耦联本端主IP地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| LOCALSUBADDRIPV4 | 本端子IPv4地址 | 可选必选说明：条件可选参数<br>前提条件：该参数在“IPVERSION”配置为“IPV4”时为可选参数。<br>参数含义：该参数用于指定SCTP耦联本端子IP地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：本端存在子IP地址时需要配置。不配置此参数时值默认为0.0.0.0。 |
| PEERADDRIPV4 | 对端主IPv4地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IPVERSION”配置为“IPV4”时为必选参数。<br>参数含义：该参数用于指定SCTP耦联对端主IP地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| PEERSUBADDRIPV4 | 对端子IPv4地址 | 可选必选说明：条件可选参数<br>前提条件：该参数在“IPVERSION”配置为“IPV4”时为可选参数。<br>参数含义：该参数用于指定SCTP耦联对端子IP地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：对端存在子IP地址时需要配置。不配置此参数时值默认为0.0.0.0。 |
| LOCALADDRIPV6 | 本端主IPv6地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IPVERSION”配置为“IPV6”时为必选参数。<br>参数含义：该参数用于指定SCTP耦联本端主IP地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |
| LOCALSUBADDRIPV6 | 本端子IPv6地址 | 可选必选说明：条件可选参数<br>前提条件：该参数在“IPVERSION”配置为“IPV6”时为可选参数。<br>参数含义：该参数用于指定SCTP耦联本端子IP地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：本端存在子IP地址时需要配置。不配置此参数时值默认为0.0.0.0。 |
| PEERADDRIPV6 | 对端主IPv6地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IPVERSION”配置为“IPV6”时为必选参数。<br>参数含义：该参数用于指定SCTP耦联对端主IP地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |
| PEERSUBADDRIPV6 | 对端子IPv6地址 | 可选必选说明：条件可选参数<br>前提条件：该参数在“IPVERSION”配置为“IPV6”时为可选参数。<br>参数含义：该参数用于指定SCTP耦联对端子IP地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：对端存在子IP地址时需要配置。不配置此参数时值默认为0.0.0.0。 |
| LOCALPORT | 本端端口号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SCTP耦联本端端口号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65534。<br>默认值：无<br>配置原则：无 |
| PEERPORT | 对端端口号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定SCTP耦联对端端口号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～65534。<br>默认值：无<br>配置原则：无 |
| VPNINSTANCE | VPN实例 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SCTP耦联VPN的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：该参数使用ADD VPNINST命令配置生成。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@UPSCTPASSOC]] · SCTP耦联信息（UPSCTPASSOC）

## 使用实例

根据网络规划，需要新增一个SCTP耦联测量对象，则可以按如下配置：

```
ADD UPSCTPASSOC: OBJECTID=1, IPVERSION=IPV4, LOCALADDRIPV4="192.168.1.23", LOCALSUBADDRIPV4="192.168.1.24", PEERADDRIPV4="192.168.2.23", PEERSUBADDRIPV4="192.168.2.24", PEERPORT=3868;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/ADD-UPSCTPASSOC.md`
