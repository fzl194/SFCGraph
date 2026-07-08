---
id: UNC@20.15.2@MMLCommand@ADD PRIMSIMSISDNSEG
type: MMLCommand
name: ADD PRIMSIMSISDNSEG（增加代理IMSI/MSISDN号段）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: PRIMSIMSISDNSEG
command_category: 配置类
applicable_nf:
- PGW-C
- GGSN
- SGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- GGSN和P-GW Proxy
- 代理选择的IMSI_MSISDN号段
status: active
---

# ADD PRIMSIMSISDNSEG（增加代理IMSI/MSISDN号段）

## 功能

**适用NF：PGW-C、GGSN、SGW-C、SMF**

该命令用于增加代理IMSI/MSISDN号段。

## 注意事项

- 该命令执行后立即生效。

- 最多可输入12000条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SEGMENTNAME | IMSI/MSISDN号段名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定信令代理特性所使用的IMSI/MSISDN号码段名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~31。只允许输入字母、数字、“.”、“_”和“-”。字母会被转换为小写字母进行存储和处理。<br>默认值：无<br>配置原则：无 |
| SEGMENTTYPE | IMSI/MSISDN号段类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定IMSI/MSISDN号段类型。<br>数据来源：本端规划<br>取值范围：IMSI（IMSI），MSISDN（MSISDN），IMSIWILDCARD（IMSI通配），MSISDNWILDCARD（MSISDN通配）。<br>- IMSI（IMSI类型）<br>- MSISDN（MSISDN类型）<br>- IMSIWILDCARD（IMSI通配）<br>- MSISDNWILDCARD（MSISDN通配）<br>默认值：无<br>配置原则：无 |
| SEGSTART | 号段起始字符串 | 可选必选说明：该参数在"SEGMENTTYPE"配置为"IMSI"、"MSISDN"时为条件必选参数。<br>参数含义：该参数用于指定起始号段。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~17。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：<br>SEGMENTTYPE等于IMSI时，SEGSTART取值范围为1~15位数字。不足15位，系统匹配时自动在末尾补0。<br>SEGMENTTYPE等于MSISDN时，SEGSTART取值范围为1~15位数字，如果开头是19，则取值范围1~17位数字。按照3GPP协议的规定，MSISDN号码的第一个字节应该是0x19，在配置MSISDN时开头可以输入19，SEGSTART截取19之后的字符串存储。SEGSTART过滤开头19后不足15位，系统匹配时自动在末尾补0。如果使用19开头的号码段进行匹配，必须在输入时携带国家码，如号码段191900000000000。<br>号段起始字符串必须小于等于号段结束字符串。 |
| SEGEND | 号段结束字符串 | 可选必选说明：该参数在"SEGMENTTYPE"配置为"IMSI"、"MSISDN"时为条件必选参数。<br>参数含义：该参数用于指定结束号段。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~17。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：<br>SEGMENTTYPE等于IMSI时，SEGEND取值范围为1~15位数字。不足15位，系统匹配时自动在末尾补9。<br>SEGMENTTYPE等于MSISDN时，SEGEND取值范围为1~15位数字，如果SEGEND的开头是19，则取值范围1~17位数字。按照3GPP协议的规定，MSISDN号码的第一个字节应该是0x19，在配置MSISDN时开头可以输入19，SEGEND截取19之后的字符串存储。SEGEND过滤开头19后不足15位，系统匹配时自动在末尾补9。如果使用19开头的号码段进行匹配，必须在输入时携带国家码，如号码段191999999999999。<br>号段起始字符串必须小于等于号段结束字符串。 |
| WILDCARDSEG | 通配号段字符串 | 可选必选说明：该参数在"SEGMENTTYPE"配置为"IMSIWILDCARD"、"MSISDNWILDCARD"时为条件必选参数。<br>参数含义：该参数用于指定号段通配。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~47。仅支持“*”、“?”和数字。<br>默认值：无<br>配置原则：<br>“?”可代替一个字符，“*”可代替零个或多个字符。<br>SEGMENTTYPE等于IMSIWILDCARD时，WILDCARDSEG中最多只能携带一个“*”，“?”替换为%3f，IMSIWILDCARD的最大长度为15。<br>SEGMENTTYPE等于MSISDNWILDCARD时，WILDCARDSEG中最多只能携带一个“*”，“?”替换为%3f，当MSISDNWILDCARD的开头两位为19时，MSISDN的最大长度为17，否则MSISDN的最大长度为15。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PRIMSIMSISDNSEG]] · 代理IMSI/MSISDN号段（PRIMSIMSISDNSEG）

## 使用实例

增加“IMSI/MSISDN号段名称”为“imsi1”，“IMSI/MSISDN号段类型”为“IMSI”，“号段起始字符串”为“460000000000000”，“号段结束字符串”为“469999999999999”的代理IMSI/MSISDN号段配置：

```
ADD PRIMSIMSISDNSEG: SEGMENTNAME="imsi1", SEGMENTTYPE=IMSI, SEGSTART="460000000000000", SEGEND="469999999999999";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-PRIMSIMSISDNSEG.md`
