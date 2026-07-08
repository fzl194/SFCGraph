---
id: UNC@20.15.2@MMLCommand@DSP SMSFUDMBYPASSTAT
type: MMLCommand
name: DSP SMSFUDMBYPASSTAT（显示SMSF用户UDM Bypass状态信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: SMSFUDMBYPASSTAT
command_category: 查询类
applicable_nf:
- SMSF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- SMSF业务管理
- UDM Bypass管理
status: active
---

# DSP SMSFUDMBYPASSTAT（显示SMSF用户UDM Bypass状态信息）

## 功能

**适用NF：SMSF**

该命令用于显示SMSF用户UDM Bypass状态信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QUERYOPT | 查询方式 | 可选必选说明：必选参数<br>参数含义：该参数用于表示查询SMSF用户UDM Bypass状态信息的方式。<br>数据来源：本端规划<br>取值范围：<br>- “SUPI（SUPI）”：用户的SUPI信息<br>- “GPSI（GPSI）”：用户的GPSI信息<br>默认值：无<br>配置原则：无 |
| SUPI | SUPI | 可选必选说明：该参数在"QUERYOPT"配置为"SUPI"时为条件可选参数。<br>参数含义：该参数用于指定用户的SUPI信息。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是5~15。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |
| GPSI | GPSI | 可选必选说明：该参数在"QUERYOPT"配置为"GPSI"时为条件可选参数。<br>参数含义：该参数用于指定用户的GPSI信息。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~15。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SMSFUDMBYPASSTAT]] · SMSF用户UDM Bypass状态信息（SMSFUDMBYPASSTAT）

## 使用实例

当运营商希望查询SMSF用户UDM Bypass状态信息，执行如下命令：

```
DSP SMSFUDMBYPASSTAT: QUERYOPT=SUPI, SUPI="460023500100001";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示SMSF用户UDM-Bypass状态信息（DSP-SMSFUDMBYPASSTAT）_54655102.md`
