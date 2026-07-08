---
id: UDG@20.15.2@MMLCommand@SET USERROUTINGSW
type: MMLCommand
name: SET USERROUTINGSW（设置用户路由可靠性配置）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: USERROUTINGSW
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 1
category_path:
- 用户面服务管理
- 会话管理
- 会话地址管理
- 用户路由可靠性配置
status: active
---

# SET USERROUTINGSW（设置用户路由可靠性配置）

## 功能

**适用NF：PGW-U、UPF**

该命令用于配置用户路由下发失败时是否上报告警（ALM-81241）和告警上报阈值。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | ALARMSWITCH | ALARMTHRESHOLD |
| --- | --- | --- |
| 初始值 | ENABLE | 0 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ALARMSWITCH | 告警开关 | 可选必选说明：必选参数<br>参数含义：该参数用于指定系统是否开启用户路由下发失败的告警上报功能。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |
| ALARMTHRESHOLD | 告警上报阈值 | 可选必选说明：条件可选参数<br>前提条件：该参数在“ALARMSWITCH”配置为“ENABLE”时为可选参数。<br>参数含义：1、该参数为30分钟内用户路由下发失败次数极限值，超过此门限则会触发用户路由下发失败告警（ALM-81241）上报。2、该参数配置为0时，业务使用缺省阈值320处理。3、该参数配置过小，可能导致告警误报。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0~20000，单位是次数。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@USERROUTINGSW]] · 用户路由可靠性配置（USERROUTINGSW）

## 使用实例

运营商在需要使用用户路由下发失败时告警上报时， 需要配置用户路由下发失败告警开关和告警阈值：

```
SET USERROUTINGSW: ALARMSWITCH=ENABLE, ALARMTHRESHOLD=320;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-USERROUTINGSW.md`
