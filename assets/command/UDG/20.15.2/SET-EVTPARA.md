---
id: UDG@20.15.2@MMLCommand@SET EVTPARA
type: MMLCommand
name: SET EVTPARA（设置策略参数值）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: EVTPARA
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 可靠性管理
- 微服务可靠性管理
status: active
---

# SET EVTPARA（设置策略参数值）

## 功能

该命令用于设置策略参数值。

> **说明**
> - 该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SERVICE | 服务名称 | 可选必选说明：必选参数<br>参数含义：该参数表示策略模型绑定的服务名称，可以通过<br>[**LST EVTPARA**](查询策略参数值（LST EVTPARA）_36260906.md)<br>命令获取参数。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~16。<br>默认值：无。<br>配置原则：无 |
| EVENTID | 事件ID | 可选必选说明：必选参数<br>参数含义：该参数表示服务名称对应的事件ID，可以通过<br>[**LST EVTPARA**](查询策略参数值（LST EVTPARA）_36260906.md)<br>命令获取参数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~4294967295。<br>默认值：无。<br>配置原则：<br>只支持配置LST EVTPARA命令获取到的服务实例。 |
| PARANAME | 策略参数 | 可选必选说明：必选参数<br>参数含义：该参数用于表示策略对应的参数名称。<br>数据来源：本端规划<br>取值范围：<br>- “AssStatic-Suspect（关联诊断嫌疑实例数）”：关联诊断配置的嫌疑实例数量。<br>- “AssStatic-Proportion（关联诊断嫌疑实例比例）”：关联诊断配置的嫌疑实例比例。<br>- “CellReset-Delay（进程复位延迟时间）”：进程复位延迟执行时间。<br>- “CellReset-Retry（进程复位重试次数）”：进程复位重试次数。<br>- “CellReset-Interval（进程复位间隔时间）”：进程复位重试间隔。<br>默认值：无。<br>配置原则：无 |
| PARAVALUE | 策略参数值 | 可选必选说明：必选参数<br>参数含义：该参数用于表示策略对应的参数数值。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~8。当策略参数为AssStatic-Suspect时，本参数取值范围为1-100；当策略参数为AssStatic-Proportion时，本参数取值范围为1-100；当策略参数为CellReset-Delay时，本参数取值范围为0-3600；当策略参数为CellReset-Retry时，本参数取值范围为0-10；当策略参数为CellReset-Interval时，本参数取值范围为1-3600。<br>默认值：无。<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/EVTPARA]] · 策略参数值（EVTPARA）

## 使用实例

设置事件1动作关联诊断里嫌疑实例数量为4。

```
%%SET EVTPARA: SERVICE="SDRS", EVENTID=1, PARANAME=AssStatic-Suspect, PARAVALUE="4";%%
RETCODE = 0  操作成功
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置策略参数值（SET-EVTPARA）_82500407.md`
