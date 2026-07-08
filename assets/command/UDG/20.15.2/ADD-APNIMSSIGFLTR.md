---
id: UDG@20.15.2@MMLCommand@ADD APNIMSSIGFLTR
type: MMLCommand
name: ADD APNIMSSIGFLTR（添加APN的IMS分类器）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: APNIMSSIGFLTR
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 对新用户生效
is_dangerous: true
max_records: 64000
category_path:
- 用户面服务管理
- VOLTE管理
- APN的IMS信令分类器
status: active
---

# ADD APNIMSSIGFLTR（添加APN的IMS分类器）

## 功能

**适用NF：PGW-U、UPF**

![](添加APN的IMS分类器（ADD APNIMSSIGFLTR）_82837825.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，请确认添加规则后合法的IMS信令报文都能命中其中一条规则。

该命令用于配置APN下的IMS信令专用上下文的Filter。使用VoLTE语音业务时，需要使用该命令配置IMS信令专用上下文的Filter来设置包的过滤规则。

## 注意事项

- 该命令执行后只对新激活用户生效。
- 该命令最大记录数为64000。
- 执行该命令时，APN参数只能配置为做IMS业务的APN，且配置的规则保证所有合法IMS业务能够命中。如果配置不当，将会影响IMS语音信令的转发，造成语音不通。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN实例名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格以及特殊字符：“_”、“#”、“$”、“&”等。<br>默认值：无<br>配置原则：无 |
| PRIORITY | 优先级 | 可选必选说明：必选参数<br>参数含义：该参数用于指定静态分组过滤优先级。值越小优先级越高。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～64。同一个APN内唯一。<br>默认值：无<br>配置原则：相同APN下的该值唯一。 |
| IPVERSION | IP地址版本 | 可选必选说明：必选参数<br>参数含义：该参数用于指定过滤规则是IPv4类型还是IPv6类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- IPV4：IPv4地址类型。<br>- IPV6：IPv6地址类型。<br>默认值：无<br>配置原则：无 |
| SRCIPV4SPECTYPE | 源IPv4地址指定方式 | 可选必选说明：条件可选参数<br>前提条件：该参数在“IPVERSION”配置为“IPV4”时为可选参数。<br>参数含义：该参数用于指定P-CSCF数据包服务器的IPv4地址是使用特定地址还是使用任意地址。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- SPECIFY：指定IP地址。<br>- ANY：任意IP地址。<br>默认值：无<br>配置原则：无 |
| SRCIPV4ADDR | 源IPv4地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“SRCIPV4SPECTYPE”配置为“SPECIFY”时为必选参数。<br>参数含义：该参数用于指定P-CSCF数据包服务器的IPv4地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。点分十进制格式。<br>默认值：无<br>配置原则：无 |
| SRCIPV4MASKLEN | 源IPv4地址掩码长度 | 可选必选说明：条件必选参数<br>前提条件：该参数在“SRCIPV4SPECTYPE”配置为“SPECIFY”时为必选参数。<br>参数含义：该参数用于指定P-CSCF数据包服务器IPv4地址的地址掩码长度。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～32。<br>默认值：无<br>配置原则：无 |
| SRCIPV6SPECTYPE | 源IPv6地址指定方式 | 可选必选说明：条件可选参数<br>前提条件：该参数在“IPVERSION”配置为“IPV6”时为可选参数。<br>参数含义：该参数用于指定P-CSCF数据包服务器的IPv6地址是使用特定地址还是使用任意地址。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- SPECIFY：指定IP地址。<br>- ANY：任意IP地址。<br>默认值：无<br>配置原则：无 |
| SRCIPV6ADDR | 源IPv6地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“SRCIPV6SPECTYPE”配置为“SPECIFY”时为必选参数。<br>参数含义：该参数用于指定P-CSCF数据包服务器的IPv6地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。冒号分隔十六进制格式，格式为X:X:X:X:X:X:X:X。取值范围为2001:0db8:0:0::～2001:0db8:FFFF:FFFF::。<br>默认值：无<br>配置原则：无 |
| SRCIPV6PREFLEN | 源IPv6地址前缀长度 | 可选必选说明：条件必选参数<br>前提条件：该参数在“SRCIPV6SPECTYPE”配置为“SPECIFY”时为必选参数。<br>参数含义：该参数用于指定P-CSCF数据包服务器IPv6地址的地址前缀长度。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～128。<br>默认值：无<br>配置原则：无 |
| SRCPORTSPECTYPE | 源端口指定方式 | 可选必选说明：可选参数<br>参数含义：该参数用于指定P-CSCF服务器端口是使用特定端口还是使用任意端口。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- SPECIFY：指定端口。<br>- ANY：任意端口。<br>默认值：无<br>配置原则：无 |
| SRCPORTSTART | 源端口号开始 | 可选必选说明：条件必选参数<br>前提条件：该参数在“SRCPORTSPECTYPE”配置为“SPECIFY”时为必选参数。<br>参数含义：该参数用于指定服务器端口起始值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～65535。<br>默认值：无<br>配置原则：无 |
| SRCPORTEND | 源端口号结束 | 可选必选说明：条件必选参数<br>前提条件：该参数在“SRCPORTSPECTYPE”配置为“SPECIFY”时为必选参数。<br>参数含义：该参数用于指定服务器端口终止值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～65535。<br>默认值：无<br>配置原则：无 |
| DSTIPV4SPECTYPE | 目的IPv4地址指定方式 | 可选必选说明：条件可选参数<br>前提条件：该参数在“IPVERSION”配置为“IPV4”时为可选参数。<br>参数含义：该参数用于指定数据包手机的IPv4地址是使用特定地址还是使用任意地址。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- SPECIFY：指定IP地址。<br>- ANY：任意IP地址。<br>默认值：无<br>配置原则：无 |
| DSTIPV4ADDR | 目的IPv4地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“DSTIPV4SPECTYPE”配置为“SPECIFY”时为必选参数。<br>参数含义：该参数用于指定数据包手机的IPv4地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。点分十进制格式。<br>默认值：无<br>配置原则：无 |
| DSTIPV4MASKLEN | 目的IPv4地址掩码长度 | 可选必选说明：条件必选参数<br>前提条件：该参数在“DSTIPV4SPECTYPE”配置为“SPECIFY”时为必选参数。<br>参数含义：该参数用于指定数据包手机IPv4地址的地址掩码长度。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～32。<br>默认值：无<br>配置原则：无 |
| DSTIPV6SPECTYPE | 目的IPv6地址指定方式 | 可选必选说明：条件可选参数<br>前提条件：该参数在“IPVERSION”配置为“IPV6”时为可选参数。<br>参数含义：该参数用于指定数据包手机的IPv6地址是使用特定地址还是使用任意地址。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- SPECIFY：指定IP地址。<br>- ANY：任意IP地址。<br>默认值：无<br>配置原则：无 |
| DSTIPV6ADDR | 目的IPv6地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“DSTIPV6SPECTYPE”配置为“SPECIFY”时为必选参数。<br>参数含义：该参数用于指定数据包手机的IPv6地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。冒号分隔十六进制格式，格式为X:X:X:X:X:X:X:X。取值范围为2000:0:0:0::～3FFF:FFFF:FFFF:FFFF:: 或 FEC0:0:0:0:: ～ FEFF:FFFF:FFFF:FFFF::。<br>默认值：无<br>配置原则：无 |
| DSTIPV6PREFLEN | 目的IPv6地址前缀长度 | 可选必选说明：条件必选参数<br>前提条件：该参数在“DSTIPV6SPECTYPE”配置为“SPECIFY”时为必选参数。<br>参数含义：该参数用于指定数据包手机IPv6地址的地址前缀长度。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～128。<br>默认值：无<br>配置原则：无 |
| DSTPORTSPECTYPE | 目的端口指定方式 | 可选必选说明：可选参数<br>参数含义：该参数用于指定手机端口是使用特定端口还是使用任意端口。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- SPECIFY：指定端口。<br>- ANY：任意端口。<br>默认值：无<br>配置原则：无 |
| DSTPORTSTART | 目的端口号开始 | 可选必选说明：条件必选参数<br>前提条件：该参数在“DSTPORTSPECTYPE”配置为“SPECIFY”时为必选参数。<br>参数含义：该参数用于指定手机端口起始值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～65535。<br>默认值：无<br>配置原则：无 |
| DSTPORTEND | 目的端口号结束 | 可选必选说明：条件必选参数<br>前提条件：该参数在“DSTPORTSPECTYPE”配置为“SPECIFY”时为必选参数。<br>参数含义：该参数用于指定手机端口终止值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～65535。<br>默认值：无<br>配置原则：无 |
| PROSPECTYPE | 协议指定方式 | 可选必选说明：可选参数<br>参数含义：该参数用于指定协议号是使用特定协议号还是使用任意协议号。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- SPECIFY：指定协议。<br>- ANY：任意协议。<br>默认值：无<br>配置原则：无 |
| PROTOCOL | 协议类型 | 可选必选说明：条件必选参数<br>前提条件：该参数在“PROSPECTYPE”配置为“SPECIFY”时为必选参数。<br>参数含义：该参数用于指定协议号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～255。协议类型tcp、udp，对应的协议号为6、17。<br>默认值：无<br>配置原则：常见协议类型ICMP、TCP、UDP、GRE，对应的协议号为1、6、17、47。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/APNIMSSIGFLTR]] · APN的IMS分类器（APNIMSSIGFLTR）

## 关联任务

- [[UDG@20.15.2@Task@0-00155]]

## 使用实例

根据网络规划，需要在APN下新增一个Filter：

```
ADD APNIMSSIGFLTR:APN="huawei.com",PRIORITY=8,IPVERSION=IPV4,SRCIPV4SPECTYPE=SPECIFY,SRCIPV4ADDR="10.3.3.3",SRCIPV4MASKLEN=32,SRCPORTSPECTYPE=SPECIFY,SRCPORTSTART=1,SRCPORTEND=65535,DSTIPV4SPECTYPE=SPECIFY,DSTIPV4ADDR="10.5.5.5",DSTIPV4MASKLEN=1,DSTPORTSPECTYPE=SPECIFY,DSTPORTSTART=50,DSTPORTEND=80,PROSPECTYPE=SPECIFY,PROTOCOL=6;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/添加APN的IMS分类器（ADD-APNIMSSIGFLTR）_82837825.md`
