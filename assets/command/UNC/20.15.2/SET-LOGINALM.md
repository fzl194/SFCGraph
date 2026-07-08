---
id: UNC@20.15.2@MMLCommand@SET LOGINALM
type: MMLCommand
name: SET LOGINALM（设置登录告警策略）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: LOGINALM
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务平台功能管理
- 操作维护
- 用户管理
- 登录告警阈值
status: active
---

# SET LOGINALM（设置登录告警策略）

## 功能

该命令用于设置登录告警策略。

## 注意事项

- 该命令执行后立即生效。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| REPORTTIMES | RESUMETIMES | PERIOD |
| --- | --- | --- |
| 30 | 20 | 5 |

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| REPORTTIMES | 触发告警的失败次数 | 可选必选说明：可选参数<br>参数含义：达到该失败次数后上报告警。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～100。0表示对管理用户登录失败不上报告警。<br>默认值：无 |
| RESUMETIMES | 解除告警的失败次数 | 可选必选说明：可选参数<br>参数含义：解除告警的失败次数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～100。0表示无登录失败情况下告警取消。取值范围随触发告警的失败次数的变化而变化，如果触发告警的失败次数为12，则解除告警的失败次数的范围为0到12。<br>默认值：无 |
| PERIOD | 统计周期（分钟） | 可选必选说明：可选参数<br>参数含义：统计周期。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～120，单位是分钟。<br>默认值：无 |

## 操作的配置对象

- [登录告警策略（LOGINALM）](configobject/UNC/20.15.2/LOGINALM.md)

## 使用实例

设置登录失败告警策略，触发告警的失败次数为10，解除告警的失败次数为5，统计周期为10分钟：

```
SET LOGINALM:REPORTTIMES=10,RESUMETIMES=5,PERIOD=10;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置登录告警策略（SET-LOGINALM）_59036112.md`
