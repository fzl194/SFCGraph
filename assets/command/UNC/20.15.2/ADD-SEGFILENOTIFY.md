---
id: UNC@20.15.2@MMLCommand@ADD SEGFILENOTIFY
type: MMLCommand
name: ADD SEGFILENOTIFY（增加号段文件通知记录）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: SEGFILENOTIFY
command_category: 配置类
applicable_nf:
- NRF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- 对端NF管理
- 号段配置管理
- 号段导入通知管理
status: active
---

# ADD SEGFILENOTIFY（增加号段文件通知记录）

## 功能

![](增加号段文件通知记录（ADD SEGFILENOTIFY）_50738957.assets/notice_3.0-zh-cn_2.png)

该操作会触发订阅通知，导致后续号段导入通知记录与预期不符。

**适用NF：NRF**

该命令用于在NRF上通过手动新增NF对应的IMSI/MSISDN号段信息达到NF号段更新，触发订阅通知。

## 注意事项

- 该命令执行后立即生效。

- 主备或双活两个NRF上均需执行此命令，配置参数值参考实际规划。

- 最多可输入1024条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFTYPE | NF类型 | 可选必选说明：必选参数<br>参数含义：该参数用于表示支持IMSI/MSISDN号段支持的NF类型。<br>数据来源：本端规划<br>取值范围：<br>- AUSF（AUSF）<br>- PCF（PCF）<br>- UDM（UDM）<br>- UDR（UDR）<br>- CHF（CHF）<br>- CUSTOM_OCS（CUSTOM_OCS）<br>默认值：无<br>配置原则：<br>支持IMSI号段配置的NF类型仅包含AUSF、PCF、UDM、 UDR、CHF、CUSTOM_OCS。支持MSISDN号段配置的NF类型仅包含PCF、UDM、 UDR、CHF、CUSTOM_OCS。 |
| SEGTYPE | 号段类型 | 可选必选说明：必选参数<br>参数含义：该参数用于表示号段类型。<br>数据来源：本端规划<br>取值范围：<br>- IMSI（IMSI）<br>- MSISDN（MSISDN）<br>默认值：无<br>配置原则：无 |
| NFGROUPID | NF组标识 | 可选必选说明：必选参数<br>参数含义：该参数用于表示待配置IMSI/MSISDN号段的NF组标识。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~128。<br>默认值：无<br>配置原则：无 |
| SEGSTART | 号段起始字符串 | 可选必选说明：必选参数<br>参数含义：该参数用于表示号段的起始号码。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是5~15。当号段类型为IMSI时，号段起始字符串长度为15位，不足15位时系统自动在末尾补0。十进制数字，号段的起始号码数值必须小于或等于号段结束号码的数值，且号段的起始号码不能以0开始，全0除外。号段类型为MSISDN时，号段的起始号码必须与结束号码长度保持一致，数值必须小于或等于结束号码的数值，且号段的起始号码不能以0开始，全0除外。<br>默认值：无<br>配置原则：无 |
| SEGEND | 号段结束字符串 | 可选必选说明：必选参数<br>参数含义：该参数用于表示号段的结束号码。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是5~15。当号段类型为IMSI时，号段结束字符串长度为15位，不足15位时系统自动在末尾补9。十进制数字，号段的结束号码数值必须大于或等于起始号码的数值，且号段的结束号码不能为以0开始。号段类型为MSISDN时，号段的结束号码必须与起始号码长度保持一致，数值大于或等于起始号码的数值，且号段的结束号码不能以0开始。<br>默认值：无<br>配置原则：无 |
| ISFROMAUSFUDM | 是否来源于AUSFUDM表 | 可选必选说明：该参数在"NFTYPE"配置为"AUSF"、"UDM"时为条件可选参数。<br>参数含义：该参数表示数据是否来源于AUSFUDM表。<br>数据来源：本端规划<br>取值范围：<br>- TRUE(TRUE)<br>- FALSE(FALSE)<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SEGFILENOTIFY]] · 号段文件通知记录（SEGFILENOTIFY）

## 使用实例

在NRF上手动触发新增CHF类型NF组标识为nfgroup001的IMSI号段信息，起始号段为123456，结束号段为234567的订阅通知。

```
ADD SEGFILENOTIFY: SEGTYPE=IMSI, NFTYPE=CHF, NFGROUPID="nfgroup001", SEGSTART="123456", SEGEND="234567";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-SEGFILENOTIFY.md`
