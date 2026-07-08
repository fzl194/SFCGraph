---
id: UNC@20.15.2@MMLCommand@ADD SCTPENDPOINT
type: MMLCommand
name: ADD SCTPENDPOINT（增加SCTP端点）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: SCTPENDPOINT
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
max_records: 60
category_path:
- 业务服务管理
- 接口管理
- 计费和策略接口管理
- SCTP管理
- SCTP端点
status: active
---

# ADD SCTPENDPOINT（增加SCTP端点）

## 功能

**适用NF：PGW-C、SMF**

此命令用于增加SCTP端点信息。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为60。
- 同一个Port下不能配置相同IP。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ENDPOINTNAME | 端点名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定SCTP端点名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| IPVERSION | IP版本 | 可选必选说明：必选参数<br>参数含义：该参数用于指定SCTP端点的IP地址类型。<br>数据来源：对端协商<br>取值范围：枚举类型。<br>- IPV4：IPv4地址类型。<br>- IPV6：IPv6地址类型。<br>默认值：无<br>配置原则：无 |
| IPV4ADDRESS1 | IPv4地址1 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IPVERSION”配置为“IPV4”时为必选参数。<br>参数含义：该参数用于指定SCTP端点的IPv4地址1。<br>数据来源：对端协商<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| IPV4ADDRESS2 | IPv4地址2 | 可选必选说明：条件可选参数<br>前提条件：该参数在“IPVERSION”配置为“IPV4”时为可选参数。<br>参数含义：该参数用于指定SCTP端点的IPv4地址2。<br>数据来源：对端协商<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：不配置此参数时值默认为0.0.0.0。 |
| PORT | 端口号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SCTP端点端口号。<br>数据来源：对端协商<br>取值范围：整数类型，取值范围为1～65534。<br>默认值：3868<br>配置原则：无 |
| SCTPTEMPLNAME | SCTP模板名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SCTP模板名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：该参数使用ADD SCTPTEMPLATE命令配置生成。 |
| IPV6ADDRESS1 | IPv6地址1 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IPVERSION”配置为“IPV6”时为必选参数。<br>参数含义：该参数用于指定SCTP端点的IPv6地址1。<br>数据来源：对端协商<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |
| IPV6ADDRESS2 | IPv6地址2 | 可选必选说明：条件可选参数<br>前提条件：该参数在“IPVERSION”配置为“IPV6”时为可选参数。<br>参数含义：该参数用于指定SCTP端点的IPv6地址2。<br>数据来源：对端协商<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：不配置此参数时值默认为::。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SCTPENDPOINT]] · SCTP端点（SCTPENDPOINT）

## 使用实例

根据网络规划，需要新增一个SCTP端点，则可以按如下配置：

```
ADD SCTPENDPOINT: ENDPOINTNAME="sctp_ep1",IPVERSION=IPV4,IPV4ADDRESS1="10.1.1.1",IPV4ADDRESS2="10.1.1.2",SCTPTEMPLNAME="sctp_tp1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-SCTPENDPOINT.md`
