---
id: UNC@20.15.2@MMLCommand@ADD NRFSMSFSEGLIST
type: MMLCommand
name: ADD NRFSMSFSEGLIST（增加SMSF号段白名单）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: NRFSMSFSEGLIST
command_category: 配置类
applicable_nf:
- NRF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- NRF业务参数
- SMSF割接场景NRF处理策略
status: active
---

# ADD NRFSMSFSEGLIST（增加SMSF号段白名单）

## 功能

![](增加SMSF号段白名单（ADD NRFSMSFSEGLIST）_21823525.assets/notice_3.0-zh-cn_2.png)

该命令与SET NRFSMSFSEGSW配合使用，在白名单未设置完成时请勿打开此开关，否则携带非白名单中的号段来发现SMSF时，该号段发现参数在匹配时将会被NRF忽略。

**适用NF：NRF**

该命令用于向SMSF号段白名单内增加号段。 若希望使用号段来匹配选择SMSF时，需要将这些号段加入到白名单中，否则未加入的号段请求参数将会被忽略。

## 注意事项

- 该命令执行后立即生效。

- 最多可输入1024条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SEGTYPE | 号段类型 | 可选必选说明：必选参数<br>参数含义：该参数用于表示配置SMSF号段白名单的号段类型。<br>数据来源：本端规划<br>取值范围：<br>- IMSI（IMSI）<br>- MSISDN（MSISDN）<br>默认值：无<br>配置原则：无 |
| IMSISTART | IMSI起始号段 | 可选必选说明：该参数在"SEGTYPE"配置为"IMSI"时为条件必选参数。<br>参数含义：该参数用于表示配置SMSF号段白名单中IMSI号段的起始号码。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是5~15。<br>默认值：无<br>配置原则：<br>号段起始字符串长度为15位，不足15位时系统自动在末尾补0。十进制数字，号段的起始号码数值必须小于或等于号段结束号码的数值，且号段的起始号码不能以0开始，全0除外。 |
| IMSIEND | IMSI结束号段 | 可选必选说明：该参数在"SEGTYPE"配置为"IMSI"时为条件必选参数。<br>参数含义：该参数用于表示配置SMSF号段白名单中IMSI号段的结束号码。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是5~15。<br>默认值：无<br>配置原则：<br>号段结束字符串长度为15位，不足15位时系统自动在末尾补9。十进制数字，号段的结束号码数值必须大于或等于起始号码的数值，且号段的结束号码不能为以0开始。 |
| MSISDNSTART | MSISDN开始号段 | 可选必选说明：该参数在"SEGTYPE"配置为"MSISDN"时为条件必选参数。<br>参数含义：该参数用于表示配置SMSF号段白名单中MSISDN号段的起始号码。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是5~15。<br>默认值：无<br>配置原则：<br>十进制数字，号段的起始号码必须与结束号码长度保持一致，数值必须小于或等于结束号码的数值，且号段的起始号码不能以0开始，全0除外。 |
| MSISDNEND | MSISDN结束号段 | 可选必选说明：该参数在"SEGTYPE"配置为"MSISDN"时为条件必选参数。<br>参数含义：该参数用于表示配置SMSF号段白名单中MSISDN号段的结束号码。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是5~15。<br>默认值：无<br>配置原则：<br>十进制数字，号段的结束号码必须与起始号码长度保持一致，数值大于或等于起始号码的数值，且号段的结束号码不能以0开始。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NRFSMSFSEGLIST]] · SMSF号段白名单（NRFSMSFSEGLIST）

## 使用实例

增加起始号码为12346704，结束号码为12346705的IMSI号段。

```
ADD NRFSMSFSEGLIST: SEGTYPE=IMSI, IMSISTART="12346704", IMSIEND="12346705";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加SMSF号段白名单（ADD-NRFSMSFSEGLIST）_21823525.md`
