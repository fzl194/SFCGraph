---
id: UNC@20.15.2@MMLCommand@MOD SMSFSELPLCY
type: MMLCommand
name: MOD SMSFSELPLCY（修改SMSF选择策略）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: SMSFSELPLCY
command_category: 配置类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- NF发现和选择管理
- SMSF选择策略管理
status: active
---

# MOD SMSFSELPLCY（修改SMSF选择策略）

## 功能

**适用NF：AMF**

该命令用于对指定的用户（群）修改SMSF的选择策略。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定应用SMSF选择策略的用户范围。<br>数据来源：全网规划<br>取值范围：<br>- “ALL_USER（ 所有用户）”：所有用户<br>- “HOME_USER（本网用户）”：本网用户<br>- “FOREIGN_USER（外网用户）”：外网用户<br>- “IMSI_RANGE（IMSI范围）”：IMSI范围<br>- “MSISDN_RANGE（MSISDN范围）”：MSISDN范围<br>默认值：无<br>配置原则：<br>对于指定的用户（群），SMSF选择策略的匹配优先级从高到低依次为：“IMSI_RANGE(IMSI范围)”，“MSISDN_RANGE(。<br>MSISDN范围)”，“FOREIGN_USER(外网用户)”或“HOME_USER(本网用户)”，“ALL_USER(所有用户)”。 |
| STARTIMSI | 起始IMSI | 可选必选说明：该参数在"SUBRANGE"配置为"IMSI_RANGE"时为条件必选参数。<br>参数含义：该参数用于表示起始IMSI。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是5~15。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |
| ENDIMSI | 结束IMSI | 可选必选说明：该参数在"SUBRANGE"配置为"IMSI_RANGE"时为条件可选参数。<br>参数含义：该参数用于表示结束IMSI。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是5~15。只允许输入十进制数字（0-9）。当本参数不输入时，取值默认为起始IMSI的值。IMSI的终止号段需要不小于IMSI的起始号段，且终止号段和起始号段长度需相等。<br>默认值：无<br>配置原则：无 |
| STARTMSISDN | 起始MSISDN | 可选必选说明：该参数在"SUBRANGE"配置为"MSISDN_RANGE"时为条件必选参数。<br>参数含义：该参数用于表示起始MSISDN。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是5~15。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |
| ENDMSISDN | 结束MSISDN | 可选必选说明：该参数在"SUBRANGE"配置为"MSISDN_RANGE"时为条件可选参数。<br>参数含义：该参数用于表示结束MSISDN。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是5~15。只允许输入十进制数字（0-9）。当本参数不输入时，取值默认为起始MSISDN的值。MSISDN的终止号段需要不小于MSISDN的起始号段，且终止号段和起始号段长度需相等。<br>默认值：无<br>配置原则：无 |
| SUPISW | 是否使用SUPI | 可选必选说明：可选参数<br>参数含义：该参数用于指定是否使用用户的SUPI作为目标SMSF的选择条件。<br>数据来源：全网规划<br>取值范围：<br>- “OFF（关闭）”：关闭<br>- “ON（开启）”：开启<br>默认值：无<br>配置原则：无 |
| GPSISW | 是否使用GPSI | 可选必选说明：可选参数<br>参数含义：该参数用于指定是否使用用户的GPSI作为目标SMSF的选择条件。<br>数据来源：全网规划<br>取值范围：<br>- “OFF（关闭）”：关闭<br>- “ON（开启）”：开启<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [SMSF选择策略（SMSFSELPLCY）](configobject/UNC/20.15.2/SMSFSELPLCY.md)

## 使用实例

修改本网用户SMSF选择策略且GPSI作为SMSF服务发现参数，执行如下命令：

```
MOD SMSFSELPLCY:SUBRANGE=HOME_USER,SUPISW=OFF,GPSISW=ON;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改SMSF选择策略（MOD-SMSFSELPLCY）_91819425.md`
