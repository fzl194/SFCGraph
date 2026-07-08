# 增加IMSI和MSISDN号段（ADD PCSCFIMSISDNSEG）

- [命令功能](#ZH-CN_MMLREF_0209652488__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0209652488__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0209652488__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0209652488__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0209652488)

**适用NF：SMF、PGW-C、GGSN**

该命令用于配置IMSI/MSISDN号码段，号码段供P-CSCF选择。

## [注意事项](#ZH-CN_MMLREF_0209652488)

- 该命令执行后立即生效。

- 最多可输入4096条记录。

#### [操作用户权限](#ZH-CN_MMLREF_0209652488)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0209652488)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SEGMENTNAME | IMSI/MSISDN号段名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定IMSI/MSISDN号段名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~31。只允许输入字母、数字、“.”、“_”和“-”。字母会被转换为小写字母进行存储和处理。<br>默认值：无<br>配置原则：无 |
| SEGMENTTYPE | IMSI/MSISDN号段类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定IMSI/MSISDN号段类型。<br>数据来源：本端规划<br>取值范围：<br>- IMSI（IMSI）<br>- MSISDN（MSISDN）<br>- IMSIWILDCARD（IMSI通配）<br>- MSISDNWILDCARD（MSISDN通配）<br>默认值：无<br>配置原则：无 |
| SEGSTART | 号段起始字符串 | 可选必选说明：该参数在"SEGMENTTYPE"配置为"IMSI"、"MSISDN"时为条件必选参数。<br>参数含义：该参数用于指定起始号段。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~17。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：<br>SEGMENTTYPE等于IMSI时，SEGSTART取值范围为1~15位数字。不足15位，系统匹配时自动在末尾补0。<br>SEGMENTTYPE等于MSISDN时，SEGSTART取值范围为1~15位数字，如果开头是19，则取值范围1~17位数字。按照3GPP协议的规定，MSISDN号码的第一个字节应该是0x19，在配置MSISDN时开头可以输入19，SEGSTART截取19之后的字符串存储。SEGSTART过滤开头19后不足15位，系统匹配时自动在末尾补0。如果使用19开头的号码段进行匹配，必须在输入时携带国家码，如号码段191900000000000。<br>号段起始字符串必须小于等于号段结束字符串。 |
| SEGEND | 号段结束字符串 | 可选必选说明：该参数在"SEGMENTTYPE"配置为"IMSI"、"MSISDN"时为条件必选参数。<br>参数含义：该参数用于指定结束号段。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~17。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：<br>SEGMENTTYPE等于IMSI时，SEGEND取值范围为1~15位数字。不足15位，系统匹配时自动在末尾补9。<br>SEGMENTTYPE等于MSISDN时，SEGEND取值范围为1~15位数字，如果SEGEND的开头是19，则取值范围1~17位数字。按照3GPP协议的规定，MSISDN号码的第一个字节应该是0x19，在配置MSISDN时开头可以输入19，SEGEND截取19之后的字符串存储。SEGEND过滤开头19后不足15位，系统匹配时自动在末尾补9。如果使用19开头的号码段进行匹配，必须在输入时携带国家码，如号码段191999999999999。<br>号段起始字符串必须小于等于号段结束字符串。 |
| WILDCARDSEG | 通配号段字符串 | 可选必选说明：该参数在"SEGMENTTYPE"配置为"IMSIWILDCARD"、"MSISDNWILDCARD"时为条件必选参数。<br>参数含义：该参数用于指定号段通配。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~47。仅支持“*”、“?”和数字。<br>默认值：无<br>配置原则：<br>“?”可代替一个字符，“*”可代替零个或多个字符。<br>SEGMENTTYPE等于IMSIWILDCARD时，WILDCARDSEG中最多只能携带一个“*”，如存在“?”，则“?”会在生成系统配置时被逐一替换为“%3f”，IMSIWILDCARD的最大长度为15。<br>SEGMENTTYPE等于MSISDNWILDCARD时，WILDCARDSEG中最多只能携带一个“*”，如存在“?”，则“?”会在生成系统配置时被逐一替换为“%3f”，当MSISDNWILDCARD的开头两位为19时，MSISDN的最大长度为17，否则MSISDN的最大长度为15。 |

## [使用实例](#ZH-CN_MMLREF_0209652488)

增加IMSI和MSISDN号段：IMSI/MSISDN号段名称为“huawei”，IMSI/MSISDN号段类型为“IMSI”， 号段起始值是“130”，号段结束值为“139”：

```
ADD PCSCFIMSISDNSEG: SEGMENTNAME="huawei", SEGMENTTYPE=IMSI, SEGSTART="130", SEGEND="139";
```
