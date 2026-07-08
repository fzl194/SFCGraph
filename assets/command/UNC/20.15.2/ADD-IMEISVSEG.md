---
id: UNC@20.15.2@MMLCommand@ADD IMEISVSEG
type: MMLCommand
name: ADD IMEISVSEG（增加IMEISV号段）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: IMEISVSEG
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
max_records: 12000
category_path:
- 业务服务管理
- 会话管理
- 计费和策略的业务管理
- 业务公共
- IMEISV号段
status: active
---

# ADD IMEISVSEG（增加IMEISV号段）

## 功能

**适用NF：PGW-C、SMF**

该命令用于配置IMEISVSEG号码段。设置号段后，可以通过ADD SUBSCRIBERIDSEGGRP命令配置到号段组。最终可以达到通过号段组选择USERPROFILE作为本地策略、根据号段选择OCS、用户根据号段选择OCS组以及在线计费模板、根据号段选择CG组、根据号段选择SGW离线计费方式等业务功能。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为12000。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SEGMENTNAME | IMEISV号段名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定IMEISV号段名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| SEGMENTTYPE | IMEISV号段类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定IMEISV号段类型。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- IMEI<br>- SV<br>- IMEISV<br>默认值：无<br>配置原则：<br>- IMEI：指定IMEI号段时，将SEGMENTTYPE设定为IMEI。<br>- SV：指定SV号段时，将SEGMENTTYPE设定为SV。<br>- IMEISV：同时设定IMEI号段、SV号段时，将SEGMENTTYPE设定为IMEISV。 |
| IMEISEGSTART | IMEI号段起始字符串 | 可选必选说明：条件必选参数<br>前提条件：该参数在“SEGMENTTYPE”配置为“IMEI” 或 “IMEISV”时为必选参数。<br>参数含义：该参数用于配置IMEI起始号段。<br>数据来源：全网规划<br>取值范围：字符串类型，1～14位数字。<br>默认值：无<br>配置原则：当运营商需要配置Imei号段时配置，该参数用于配置Imei号段起始字符串。不足14位，系统匹配时自动在末尾补0。 |
| IMEISEGEND | IMEI号段结束字符串 | 可选必选说明：条件必选参数<br>前提条件：该参数在“SEGMENTTYPE”配置为“IMEI” 或 “IMEISV”时为必选参数。<br>参数含义：该参数用于配置IMEI结束号段。<br>数据来源：全网规划<br>取值范围：字符串类型，1～14位数字。<br>默认值：无<br>配置原则：当运营商需要配置Imei号段时配置，该参数用于配置Imei号段结束字符串。不足14位，系统匹配时自动在末尾补9。 |
| SVSEGSTART | SV号段起始字符串 | 可选必选说明：条件必选参数<br>前提条件：该参数在“SEGMENTTYPE”配置为“SV” 或 “IMEISV”时为必选参数。<br>参数含义：该参数用于配置SV起始号段。<br>数据来源：全网规划<br>取值范围：字符串类型，2位数字。<br>默认值：无<br>配置原则：当运营商需要配置Sv号段时配置，该参数用于配置Sv号段起始字符串。 |
| SVSEGEND | SV号段结束字符串 | 可选必选说明：条件必选参数<br>前提条件：该参数在“SEGMENTTYPE”配置为“SV” 或 “IMEISV”时为必选参数。<br>参数含义：该参数用于配置SV结束号段。<br>数据来源：全网规划<br>取值范围：字符串类型，2位数字。<br>默认值：无<br>配置原则：当运营商需要配置Sv号段时配置，该参数用于配置Sv号段结束字符串。 |

## 操作的配置对象

- [IMEISV号段（IMEISVSEG）](configobject/UNC/20.15.2/IMEISVSEG.md)

## 使用实例

增加IMEISV号段: SEGMENTNAME为TestSegmentName；SEGMENTTYPE为IMEI；IMEISEGSTART为11111111；IMEISEGEND为11111111：

```
ADD IMEISVSEG:SEGMENTNAME="TestSegmentName",SEGMENTTYPE=IMEI,IMEISEGSTART="11111111",IMEISEGEND="11111111";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加IMEISV号段（ADD-IMEISVSEG）_09897138.md`
