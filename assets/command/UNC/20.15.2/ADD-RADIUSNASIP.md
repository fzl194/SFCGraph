---
id: UNC@20.15.2@MMLCommand@ADD RADIUSNASIP
type: MMLCommand
name: ADD RADIUSNASIP（增加RADIUS NAS IP）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: RADIUSNASIP
command_category: 配置类
applicable_nf:
- SGW-C
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
max_records: 6000
category_path:
- 业务服务管理
- 会话管理
- RADIUS管理
- 连接管理
- NAS IP
status: active
---

# ADD RADIUSNASIP（增加RADIUS NAS IP）

## 功能

**适用NF：SGW-C、PGW-C、SMF**

该命令用来基于APN实例增加RADIUS NAS IP配置。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为6000。
- 如果APN下配置了RADIUS NAS IP，则该APN的用户激活时使用配置的RADIUS NAS IP地址。
- 在一个group里，基于APN+UP可以配置1条RADIUS NAS IP，一个基础APN+多个UP可以配置多个UPF的RADIUS NAS IP。
- NasIp地址和NasIpv6地址这两个参数，必须配置其中一个。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：必选参数<br>参数含义：该参数用来指定APN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：无 |
| UPINSTANCEID | UP实例标识 | 可选必选说明：可选参数<br>参数含义：UP实例标识。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～36。字符串类型，输入长度范围是1~36。UpfInstanceId参数必须满足以下约束规则：1.如果输入为uuid格式（格式例如：a6a61c6f-0d3a-4221-b1da-424eda3ccf67）只能为A-F、a-f、0-9的字符。2.如果输入不为uuid格式，长度不能超过18且不允许输入只包含0-9和“.”的字符串，例如：1.2.3.4、不允许输入只包含十六进制数（A-F、a-f、0-9）和“:”的字符串，例如：1::2、FBFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF。<br>默认值：无<br>配置原则：无 |
| NASIP | NAS IP地址 | 可选必选说明：可选参数<br>参数含义：该参数用来指定RADIUS NAS IP地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。有效的IPv4地址，不允许配置为0.0.0.0或255.255.255.255。<br>默认值：无<br>配置原则：不配置此参数时值默认为0.0.0.0。 |
| NASIPV6 | NAS IPv6地址 | 可选必选说明：可选参数<br>参数含义：该参数用来指定RADIUS NAS IPv6地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。采用冒号分十六进制X:X:X:X:X:X:X:X格式。<br>默认值：无<br>配置原则：不配置此参数时值默认为::。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@RADIUSNASIP]] · RADIUS NAS IP（RADIUSNASIP）

## 使用实例

配置APN实例为huawei.com的用户激活时，使用的RADIUS NAS IP为192.168.10.1：

```
ADD RADIUSNASIP:APN="huawei.com",NASIP="192.168.10.1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-RADIUSNASIP.md`
