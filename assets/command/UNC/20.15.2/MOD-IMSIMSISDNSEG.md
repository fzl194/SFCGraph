---
id: UNC@20.15.2@MMLCommand@MOD IMSIMSISDNSEG
type: MMLCommand
name: MOD IMSIMSISDNSEG（修改IMSI和MSISDN号段）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: IMSIMSISDNSEG
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费和策略的业务管理
- 业务公共
- IMSI MSISDN号段
status: active
---

# MOD IMSIMSISDNSEG（修改IMSI和MSISDN号段）

## 功能

**适用NF：PGW-C、SMF**

该命令用于修改配置IMSI/MSISDN号码段。

## 注意事项

- 该命令执行后立即生效。
- 如果记录已被ADD L2RULEGRPBIND命令引用，则不允许将SegmentType修改为MSISDN和MSISDNWILDCARD，否则修改失败。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SEGMENTNAME | IMSI/MSISDN号段名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定IMSI/MSISDN号段名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| SEGMENTTYPE | IMSI/MSISDN号段类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定IMSI/MSISDN号段类型。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- IMSI：单个IMSI。<br>- MSISDN：单个MSISDN。<br>- IMSIWILDCARD：IMSI含通配符，可匹配多个IMSI。<br>- MSISDNWILDCARD：MSISDN含通配符，可匹配多个MSISDN。<br>默认值：无<br>配置原则：无 |
| SEGSTART | 号段起始字符串 | 可选必选说明：条件必选参数<br>前提条件：该参数在“SEGMENTTYPE”配置为“IMSI” 或 “MSISDN”时为必选参数。<br>参数含义：该参数用于指定起始号段。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～17。<br>默认值：无<br>配置原则：<br>- SEGMENTTYPE等于IMSI时，SEGSTART取值范围为1~15位数字。不足15位，系统匹配时自动在末尾补0。<br>- SEGMENTTYPE等于MSISDN时，SEGSTART取值范围为1~15位数字，如果开头是19，则取值范围1~17位数字。在配置MSISDN时开头可以输入19，SEGSTART截取19之后的字符串存储。SEGSTART过滤开头19后不足15位，系统匹配时自动在末尾补0。如果使用19开头的号码段进行匹配，必须在输入时携带国家码，如号码段191900000000000。<br>- SEGSTART必须小于等于SEGEND。 |
| SEGEND | 号段结束字符串 | 可选必选说明：条件必选参数<br>前提条件：该参数在“SEGMENTTYPE”配置为“IMSI” 或 “MSISDN”时为必选参数。<br>参数含义：该参数用于指定结束号段。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～17。<br>默认值：无<br>配置原则：<br>- SEGMENTTYPE等于IMSI时，SEGEND取值范围为1~15位数字。不足15位，系统匹配时自动在末尾补9。<br>- SEGMENTTYPE等于MSISDN时，SEGEND取值范围为1~15位数字，如果开头是19，则取值范围1~17位数字。在配置MSISDN时开头可以输入19，SEGEND截取19之后的字符串存储。SEGEND过滤开头19后不足15位，系统匹配时自动在末尾补9。如果使用19开头的号码段进行匹配，必须在输入时携带国家码，如号码段191900000000000。<br>- SEGEND必须大于等于SEGSTART。 |
| WILDCARDSEG | 通配号段字符串 | 可选必选说明：条件必选参数<br>前提条件：该参数在“SEGMENTTYPE”配置为“IMSIWILDCARD” 或 “MSISDNWILDCARD”时为必选参数。<br>参数含义：该参数用于指定号段通配。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～47。仅支持“*”、“?”和数字。<br>默认值：无<br>配置原则：<br>- “?”可代替一个字符，“*”可代替零个或多个字符。<br>- SEGMENTTYPE等于IMSIWILDCARD时，WILDCARDSEG中最多只能携带一个“*”，其中“?”需要输入为%3f，IMSI的最大长度为15。<br>- SEGMENTTYPE等于MSISDNWILDCARD时，WILDCARDSEG中最多只能携带一个“*”，其中“?”需要输入为%3f，当MSISDN的开头两位为19时，MSISDN的最大长度为17，否则MSISDN的最大长度为15。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@IMSIMSISDNSEG]] · IMSI和MSISDN号段（IMSIMSISDNSEG）

## 使用实例

修改IMSI和MSISDN号段: SEGMENTNAME为huawei，SEGMENTTYPE为IMSI，SEGSTART为130，SEGEND为139：

```
MOD IMSIMSISDNSEG:SEGMENTNAME="huawei",SEGMENTTYPE=IMSI,SEGSTART="130",SEGEND="139";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-IMSIMSISDNSEG.md`
