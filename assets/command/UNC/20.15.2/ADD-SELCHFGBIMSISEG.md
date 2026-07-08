---
id: UNC@20.15.2@MMLCommand@ADD SELCHFGBIMSISEG
type: MMLCommand
name: ADD SELCHFGBIMSISEG（增加IMSI号段与CHF组的绑定关系）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: SELCHFGBIMSISEG
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 融合计费
- CHF选择
status: active
---

# ADD SELCHFGBIMSISEG（增加IMSI号段与CHF组的绑定关系）

## 功能

**适用NF：PGW-C、SMF、GGSN**

该命令用于增加IMSI号段与CHF组的绑定关系。SMF选择NCG/CHF时，可基于指定的IMSI号段选择CHF组，将不同IMSI号段的用户的计费信息送到不同NCG/CHF组。

## 注意事项

- 该命令执行后立即生效。

- 该命令仅支持本地配置SMF选择CHF组场景。
- SMF选择CHF的优先级从高到低依次是：基于IMSI选择CHF > 基于IMSI号段选择CHF > 基于PCF下发的信息选择CHF > 基于从UDM获取的签约CC选择CHF > 基于标准化服务发现选择CHF > 基于SMF本地配置的CC选择CHF。

- 最多可输入1024条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SEGSTART | 号段起始字符串 | 可选必选说明：必选参数<br>参数含义：该参数用于设置绑定的IMSI号段的起始字符串。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是5~15。号段起始字符串长度为15位，不足15位时系统自动在末尾补0。十进制数字，号段的起始号码数值必须小于或等于号段结束号码的数值，且号段的起始号码不能以0开始，全0除外。<br>默认值：无<br>配置原则：无 |
| SEGEND | 号段结束字符串 | 可选必选说明：必选参数<br>参数含义：该参数用于设置绑定的IMSI号段的结束字符串。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是5~15。号段结束字符串长度为15位，不足15位时系统自动在末尾补9。十进制数字，号段的结束号码数值必须大于或等于起始号码的数值，且号段的结束号码不能以0开始。<br>默认值：无<br>配置原则：无 |
| PRIMARYCHFGRP | 主CHF组 | 可选必选说明：可选参数<br>参数含义：该参数用于设置主CHF组。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~63。<br>默认值：无<br>配置原则：<br>该参数使用ADD TNFGRP命令配置生成。 |
| SECONDARYCHFGRP | 备CHF组 | 可选必选说明：可选参数<br>参数含义：该参数用于设置备CHF组。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~63。<br>默认值：无<br>配置原则：<br>该参数使用ADD TNFGRP命令配置生成。 |

## 操作的配置对象

- [IMSI号段与CHF组的绑定关系（SELCHFGBIMSISEG）](configobject/UNC/20.15.2/SELCHFGBIMSISEG.md)

## 使用实例

增加基于IMSI号段12345678901~12345678905选择主CHF组CHF1和备CHF组CHF2的处理：

```
ADD SELCHFGBIMSISEG: SEGSTART="12345678901", SEGEND="12345678905", PRIMARYCHFGRP="CHF1", SECONDARYCHFGRP="CHF2";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加IMSI号段与CHF组的绑定关系（ADD-SELCHFGBIMSISEG）_05630193.md`
