---
id: UDG@20.15.2@MMLCommand@MOD PDNROUTETSTPATH
type: MMLCommand
name: MOD PDNROUTETSTPATH（修改UPF向PDN服务器发送探测消息的探测路径配置）
nf: UDG
version: 20.15.2
verb: MOD
object_keyword: PDNROUTETSTPATH
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 会话管理
- 会话连通性检测
- 网络侧连通性检测
- PDN侧路由探测
status: active
---

# MOD PDNROUTETSTPATH（修改UPF向PDN服务器发送探测消息的探测路径配置）

## 功能

**适用NF：PGW-U、UPF**

该命令用来修改UPF向PDN服务器自动发送探测消息的路径配置。

## 注意事项

- 该命令执行后立即生效。
- 域名字段DOMAINVALUE，MOD时不支持清除，如需修改，请使用RMV命令删除此配置后重新配置。
- MOD修改探测路径配置后，将启动一次该路径的探测。
- 对于DOMAINVALUE，特殊字符的输入要求可以参考STR PDNROUTETST注意事项部分。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PATHNAME | 路径名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定用于连通性探测的路径名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：配置的路径名称应满足路径名称的取值范围。 |
| PATHTYPE | 路径类型 | 可选必选说明：必选参数<br>参数含义：用于指定路径类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DNS：DNS探测方式。<br>默认值：DNS<br>配置原则：无 |
| IPPOOL | 地址池名称 | 可选必选说明：必选参数<br>参数含义：地址池的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～79，单位是字节。由“_”、“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”，不区分大小写。<br>默认值：无<br>配置原则：无 |
| IPVERSION | IP地址类型 | 可选必选说明：必选参数<br>参数含义：用于指定IP地址类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- IPV4：IPv4地址类型。<br>- IPV6：IPv6地址类型。<br>默认值：无<br>配置原则：无 |
| DSTIPV4ADDR | 目的IPv4地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IPVERSION”配置为“IPV4”时为必选参数。<br>参数含义：指定探测目的PDN Server的IP地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。点分十进制形式，不可为广播地址或者全0地址，必须是有效地址。<br>默认值：无<br>配置原则：探测命令中DstIPaddr不允许配置为UE地址或者UPF设备上已经配置的地址，否则会导致无效探测。 |
| DSTIPV6PREFIX | 目的IPv6前缀地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IPVERSION”配置为“IPV6”时为必选参数。<br>参数含义：该参数用于指定探测目的PDN Server的IPv6前缀地址。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。采用冒号分十六进制X:X:X:X:X:X:X:X格式。<br>默认值：无<br>配置原则：无 |
| DSCPV | DSCP值 | 可选必选说明：条件可选参数<br>前提条件：该参数在“IPVERSION”配置为“IPV4”时为可选参数。<br>参数含义：指定探测报文的DSCP值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～63。<br>默认值：无<br>配置原则：无 |
| TESTMETHOD | 路由探测方式 | 可选必选说明：必选参数<br>参数含义：指定探测方式。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- PING：PING探测方式。<br>- DNS：DNS探测方式。<br>- TRACERT：TRACERT探测方式。<br>默认值：无<br>配置原则：无 |
| LENGTH | 报文净荷长度 | 可选必选说明：条件可选参数<br>前提条件：该参数在“TESTMETHOD”配置为“PING”时为可选参数。<br>参数含义：指定探测报文长度。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为20～1800。<br>默认值：无<br>配置原则：无 |
| TCV | Traffic-Class值 | 可选必选说明：条件可选参数<br>前提条件：该参数在“IPVERSION”配置为“IPV6”时为可选参数。<br>参数含义：指定探测报文的traffic-class值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～63。<br>默认值：无<br>配置原则：无 |
| DOMAINVALUE | 域名 | 可选必选说明：条件必选参数<br>前提条件：该参数在“TESTMETHOD”配置为“DNS”时为必选参数。<br>参数含义：当TESTMETHOD为DNS方式时，配置该参数用于指定域名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不区分大小写，转义后的长度不超过120。<br>默认值：无<br>配置原则：建议使用存在的域名。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/PDNROUTETSTPATH]] · UPF向PDN服务器发送探测消息的探测路径配置（PDNROUTETSTPATH）

## 使用实例

修改探测路径名称为test，用于检查地址池名称为pool-test中发布路由网段和PDN服务器10.1.1.1之间的路由是否正常，向PDN服务器发送PING探测消息：

```
MOD PDNROUTETSTPATH: PATHNAME="test1", PATHTYPE=DNS, IPPOOL="pool-test", IPVERSION=IPV4, DSTIPV4ADDR="10.1.1.1", TESTMETHOD=PING;
RETCODE = 0  Operation succeeded
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改UPF向PDN服务器发送探测消息的探测路径配置（MOD-PDNROUTETSTPATH）_64073333.md`
