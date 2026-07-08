---
id: UNC@20.15.2@MMLCommand@SET SYSTIMER
type: MMLCommand
name: SET SYSTIMER（设置系统定时器）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: SYSTIMER
command_category: 配置类
applicable_nf:
- NCG
effect_mode: 立即生效
is_dangerous: false
max_records: 2
category_path:
- 业务服务管理
- NCG业务及策略管理
- 计费管理
- 业务系统管理
- 维护管理
- 设置系统定时器
status: active
---

# SET SYSTIMER（设置系统定时器）

## 功能

**适用NF：NCG**

该命令用于设置NCG的系统定时器时长。其中系统定时器包括统计2G/3G的PDP信息老化定时器、统计4G的Bearer信息老化定时器。对超过定时器时长的信息执行老化操作，防止无用数据对统计准确性的干扰。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为2。
- 定时器时长的单位为分钟。
- 该命令存在系统初始设置记录，参数的初始设置值如下表：

| TIMERNAME | OUTTIME |
| --- | --- |
| PDPs_Aging_Timer | 30 |
| Bearers_Aging_Timer | 75 |

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TIMERNAME | 定时器名称 | 可选必选说明：必选参数<br>参数含义：选择设置时长的定时器标识。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- PDPs_Aging_Timer：统计2G/3G的PDP信息老化定时器。<br>- Bearers_Aging_Timer：统计4G的Bearer信息老化定时器。<br>- 5G_Bearers_Aging_Timer：统计5G的Bearer信息老化定时器。<br>默认值：无<br>配置原则：无 |
| OUTTIME | 定时器时长(分钟) | 可选必选说明：条件可选参数<br>前提条件：该参数在“TIMERNAME”配置为“PDPs_Aging_Timer” 或 “Bearers_Aging_Timer”时为条件可选参数。<br>参数含义：系统定时器时长，单位为分钟。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～35790。<br>默认值：无<br>配置原则：<br>- 对于“PDPs_Aging_Timer(统计2G/3G的PDP信息老化定时器)”，默认的定时器时长为30分钟。<br>- 对于“Bearers_Aging_Timer(统计4G的Bearer信息老化定时器)”，默认的定时器时长为75分钟。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SYSTIMER]] · 系统定时器（SYSTIMER）

## 使用实例

设置NCG的“定时器名称”为“PDPs_Aging_Timer(统计2G/3G的PDP信息老化定时器)”，“定时器时长(分钟)”为“8888”：

```
SET SYSTIMER: TIMERNAME=PDPs_Aging_Timer, OUTTIME=8888;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-SYSTIMER.md`
