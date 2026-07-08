---
id: UNC@20.15.2@MMLCommand@MOD SELCHFGBIMSISEG
type: MMLCommand
name: MOD SELCHFGBIMSISEG（修改IMSI号段与CHF组的绑定关系）
nf: UNC
version: 20.15.2
verb: MOD
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

# MOD SELCHFGBIMSISEG（修改IMSI号段与CHF组的绑定关系）

## 功能

**适用NF：PGW-C、SMF、GGSN**

该命令用于修改IMSI号段与CHF组的绑定关系。

## 注意事项

- 该命令执行后立即生效。

- SMF选择CHF的优先级从高到低依次是：基于IMSI选择CHF > 基于IMSI号段选择CHF > 基于PCF下发的信息选择CHF > 基于从UDM获取的签约CC选择CHF > 基于标准化服务发现选择CHF > 基于SMF本地配置的CC选择CHF。

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

- [[configobject/UNC/20.15.2/SELCHFGBIMSISEG]] · IMSI号段与CHF组的绑定关系（SELCHFGBIMSISEG）

## 使用实例

修改基于IMSI号段为12345678901~12345678905选择CHF处理，将主CHF组由CHF1改为CHF2，备CHF组由CHF2改为CHF1：

```
MOD SELCHFGBIMSISEG: SEGSTART="12345678901", SEGEND="12345678905", PRIMARYCHFGRP="CHF2", SECONDARYCHFGRP="CHF1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-SELCHFGBIMSISEG.md`
