---
id: UDG@20.15.2@MMLCommand@ADD UPIMSIMSSEG
type: MMLCommand
name: ADD UPIMSIMSSEG（增加IMSI和MSISDN号段）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: UPIMSIMSSEG
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 12000
category_path:
- 用户面服务管理
- 业务匹配策略
- 业务匹配公共配置
- 业务公共参数管理
- IMSI MSISDN号段
status: active
---

# ADD UPIMSIMSSEG（增加IMSI和MSISDN号段）

## 功能

**适用NF：PGW-U、UPF**

该命令用于配置IMSI/MSISDN号码段。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为12000。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SEGMENTNAME | IMSI/MSISDN号段名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定IMSI/MSISDN号段名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| SEGMENTTYPE | IMSI/MSISDN号段类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定IMSI/MSISDN号段类型。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- IMSI：IMSI。<br>- MSISDN：MSISDN。<br>默认值：无<br>配置原则：无 |
| SEGSTART | 号段起始字符串 | 可选必选说明：条件必选参数<br>前提条件：该参数在“SEGMENTTYPE”配置为“IMSI” 或 “MSISDN”时为必选参数。<br>参数含义：该参数用于指定起始号段。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～17。<br>默认值：无<br>配置原则：<br>- SEGMENTTYPE等于IMSI时，SEGSTART取值范围为1~15位数字。不足15位，系统匹配时自动在末尾补0。<br>- SEGMENTTYPE等于MSISDN时，SEGSTART取值范围为1~15位数字，如果开头是19，则取值范围1~17位数字。按照3GPP协议的规定，MSISDN号码的第一个字节应该是0x91，在配置MSISDN时开头可以输入19，SEGSTART截取19之后的字符串存储。SEGSTART过滤开头19后不足15位，系统匹配时自动在末尾补0。<br>- SEGSTART必须小于等于SEGEND。 |
| SEGEND | 号段结束字符串 | 可选必选说明：条件必选参数<br>前提条件：该参数在“SEGMENTTYPE”配置为“IMSI” 或 “MSISDN”时为必选参数。<br>参数含义：该参数用于指定结束号段。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～17。<br>默认值：无<br>配置原则：<br>- SEGMENTTYPE等于IMSI时，SEGEND取值范围为1~15位数字。不足15位，系统匹配时自动在末尾补9。<br>- SEGMENTTYPE等于MSISDN时，SEGEND取值范围为1~15位数字，如果开头是19，则取值范围1~17位数字。按照3GPP协议的规定，MSISDN号码的第一个字节应该是0x91，在配置MSISDN时开头可以输入19，SEGEND截取19之后的字符串存储。SEGEND过滤开头19后不足15位，系统匹配时自动在末尾补9。<br>- SEGEND必须大于等于SEGSTART。 |
| CFGDOMAINNAME | 配置域名称 | 可选必选说明：可选参数<br>参数含义：该参数表示命令所属公共配置域的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/UPIMSIMSSEG]] · IMSI和MSISDN号段（UPIMSIMSSEG）

## 使用实例

增加IMSI和MSISDN号段: SEGMENTNAME为huawei; SEGSTART为IMSI; SEGSTART为130; SEGEND为139：

```
ADD UPIMSIMSSEG:SEGMENTNAME="huawei",SEGMENTTYPE=IMSI,SEGSTART="130",SEGEND="139";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/增加IMSI和MSISDN号段（ADD-UPIMSIMSSEG）_86322306.md`
