---
id: UNC@20.15.2@MMLCommand@ADD SMFDIALTEST
type: MMLCommand
name: ADD SMFDIALTEST（增加SMF拨测用户配置）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: SMFDIALTEST
command_category: 配置类
applicable_nf:
- SGW-C
- PGW-C
- SMF
effect_mode: 对新用户生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 网络管理
- 灰度升级
- 拨测管理
status: active
---

# ADD SMFDIALTEST（增加SMF拨测用户配置）

## 功能

**适用NF：SGW-C、PGW-C、SMF**

该命令用于新增拨测用户列表，通过起始IMSI/MSISDN和终止IMSI/MSISDN的方式，配置一组拨测用户。

## 注意事项

- 该命令执行后只对新激活用户生效。

- 该命令的匹配拨测用户的方式为全匹配，不支持IMSI/MSISDN前缀匹配。
- 该命令每条记录配置的拨测用户数不大于100。
- 起始IMSI（MSISDN）和终止IMSI（MSISDN）必须等长。
- 终止IMSI（MSISDN）取值应大于等于起始IMSI（MSISDN）。
- 相同用户标识类型的两条记录的拨测用户范围不可以重叠。

- 最多可输入80条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TSTUSRRANGE | 用户标识类型 | 可选必选说明：必选参数<br>参数含义：该参数用于配置拨测用户类型。<br>数据来源：本端规划<br>取值范围：<br>- MSISDN（MSISDN）<br>- IMSI（IMSI）<br>默认值：无<br>配置原则：无 |
| BEGINMSISDN | 起始MSISDN | 可选必选说明：该参数在"TSTUSRRANGE"配置为"MSISDN"时为条件必选参数。<br>参数含义：该参数用于配置拨测用户的起始MSISDN。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~15。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：<br>该参数在“用户标识类型”参数配置为“MSISDN(MSISDN)”后生效。 |
| ENDMSISDN | 终止MSISDN | 可选必选说明：该参数在"TSTUSRRANGE"配置为"MSISDN"时为条件必选参数。<br>参数含义：该参数用于配置拨测用户的终止MSISDN。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~15。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：<br>该参数在“用户标识类型”参数配置为“MSISDN(MSISDN)”后生效。 |
| BEGINIMSI | 起始IMSI | 可选必选说明：该参数在"TSTUSRRANGE"配置为"IMSI"时为条件必选参数。<br>参数含义：该参数用于配置拨测用户的起始IMSI。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是14~15。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：<br>该参数在“用户标识类型”参数配置为“IMSI(IMSI)”后生效。 |
| ENDIMSI | 终止IMSI | 可选必选说明：该参数在"TSTUSRRANGE"配置为"IMSI"时为条件必选参数。<br>参数含义：该参数用于配置拨测用户的终止IMSI。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是14~15。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：<br>该参数在“用户标识类型”参数配置为“IMSI(IMSI)”后生效。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SMFDIALTEST]] · SMF拨测用户配置（SMFDIALTEST）

## 使用实例

增加一条拨测用户配置，用户标识类型为IMSI，待拨测用户IMSI长度为15位，用户范围为460001111111111~460001111111122。

```
ADD SMFDIALTEST: TSTUSRRANGE=IMSI, BEGINIMSI="460001111111111", ENDIMSI="460001111111122";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加SMF拨测用户配置（ADD-SMFDIALTEST）_23622922.md`
