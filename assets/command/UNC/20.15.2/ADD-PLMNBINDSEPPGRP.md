---
id: UNC@20.15.2@MMLCommand@ADD PLMNBINDSEPPGRP
type: MMLCommand
name: ADD PLMNBINDSEPPGRP（增加PLMN与SEPP组的绑定关系）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: PLMNBINDSEPPGRP
command_category: 配置类
applicable_nf:
- AMF
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 服务化接口管理
- SEPP管理
- SEPP组PLMN管理
status: active
---

# ADD PLMNBINDSEPPGRP（增加PLMN与SEPP组的绑定关系）

## 功能

**适用NF：AMF、SMF**

该命令用于增加PLMN与SEPP组的绑定关系。

## 注意事项

- 该命令执行后立即生效。

- 当MCC与MNC均配置为“*”时，代表该组SEPP支持所有PLMN。
- 优先使用关联目标PLMN的SEPP组，当没有关联目标PLMN的SEPP组时，使用支持所有PLMN的SEPP组。

- 最多可输入1000条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MCC | 移动国家码 | 可选必选说明：必选参数<br>参数含义：该参数用于指定移动国家码。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~3。<br>默认值：无<br>配置原则：<br>本参数只能由3个十进制数字组成或者配置为“*”。 |
| MNC | 移动网号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定移动网号。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~3。<br>默认值：无<br>配置原则：<br>本参数只能由2~3个十进制数字组成或者配置为“*”。 |
| GROUPID | 组号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定SEPP组号。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是2~65。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [PLMN与SEPP组的绑定关系（PLMNBINDSEPPGRP）](configobject/UNC/20.15.2/PLMNBINDSEPPGRP.md)

## 使用实例

规划目标PLMN为12303的异网漫游，需要使用组号为3的SEPP组间接通信。

```
ADD PLMNBINDSEPPGRP: MCC="123", MNC="03", GROUPID=3;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加PLMN与SEPP组的绑定关系（ADD-PLMNBINDSEPPGRP）_30680370.md`
