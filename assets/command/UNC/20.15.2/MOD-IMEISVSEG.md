---
id: UNC@20.15.2@MMLCommand@MOD IMEISVSEG
type: MMLCommand
name: MOD IMEISVSEG（修改IMEISV号段）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: IMEISVSEG
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
- IMEISV号段
status: active
---

# MOD IMEISVSEG（修改IMEISV号段）

## 功能

**适用NF：PGW-C、SMF**

该命令用于修改指定号段名称的IMEISVSEG号码段，修改之后原来的绑定关系继续存在。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SEGMENTNAME | IMEISV号段名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定IMEISV号段名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| SEGMENTTYPE | IMEISV号段类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定IMEISV号段类型。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- IMEI<br>- SV<br>- IMEISV<br>默认值：无<br>配置原则：<br>- IMEI：指定IMEI号段时，将SEGMENTTYPE设定为IMEI。<br>- SV：指定SV号段时，将SEGMENTTYPE设定为SV。<br>- IMEISV：同时设定IMEI号段、SV号段时，将SEGMENTTYPE设定为IMEISV。 |
| IMEISEGSTART | IMEI号段起始字符串 | 可选必选说明：条件必选参数<br>前提条件：该参数在“SEGMENTTYPE”配置为“IMEI” 或 “IMEISV”时为必选参数。<br>参数含义：该参数用于配置IMEI起始号段。<br>数据来源：全网规划<br>取值范围：字符串类型，1～14位数字。<br>默认值：无<br>配置原则：当运营商需要修改Imei号段时配置，该参数用于配置Imei号段起始字符串。不足14位，系统匹配时自动在末尾补0。 |
| IMEISEGEND | IMEI号段结束字符串 | 可选必选说明：条件必选参数<br>前提条件：该参数在“SEGMENTTYPE”配置为“IMEI” 或 “IMEISV”时为必选参数。<br>参数含义：该参数用于配置IMEI结束号段。<br>数据来源：全网规划<br>取值范围：字符串类型，1～14位数字。<br>默认值：无<br>配置原则：当运营商需要修改Imei号段时配置，该参数用于配置Imei号段结束字符串。不足14位，系统匹配时自动在末尾补9。 |
| SVSEGSTART | SV号段起始字符串 | 可选必选说明：条件必选参数<br>前提条件：该参数在“SEGMENTTYPE”配置为“SV” 或 “IMEISV”时为必选参数。<br>参数含义：该参数用于配置SV起始号段。<br>数据来源：全网规划<br>取值范围：字符串类型，2位数字。<br>默认值：无<br>配置原则：当运营商需要修改Sv号段时配置，该参数用于配置Sv号段起始字符串。 |
| SVSEGEND | SV号段结束字符串 | 可选必选说明：条件必选参数<br>前提条件：该参数在“SEGMENTTYPE”配置为“SV” 或 “IMEISV”时为必选参数。<br>参数含义：该参数用于配置SV结束号段。<br>数据来源：全网规划<br>取值范围：字符串类型，2位数字。<br>默认值：无<br>配置原则：当运营商需要修改Sv号段时配置，该参数用于配置Sv号段结束字符串。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/IMEISVSEG]] · IMEISV号段（IMEISVSEG）

## 使用实例

修改IMEISV号段: SEGMENTNAME为TestSegmentName；SEGMENTTYPE为IMEI；IMEISEGSTART为T22222222；IMEISEGEND为22222222：

```
MOD IMEISVSEG:SEGMENTNAME="TestSegmentName",SEGMENTTYPE=IMEI,IMEISEGSTART="22222222",IMEISEGEND="22222222";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改IMEISV号段（MOD-IMEISVSEG）_09897139.md`
