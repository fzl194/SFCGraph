---
id: UDG@20.15.2@MMLCommand@SET RELAYSALMPARA
type: MMLCommand
name: SET RELAYSALMPARA（设置媒体中继业务告警参数配置）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: RELAYSALMPARA
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 1
category_path:
- 用户面服务管理
- 业务控制策略
- 媒体中继
- 媒体中继业务告警参数配置
status: active
---

# SET RELAYSALMPARA（设置媒体中继业务告警参数配置）

## 功能

**适用NF：PGW-U、UPF**

该命令用于配置媒体中继业务告警参数。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | ALAMCHECKTIME | URLAUTHALMSW | URLAUTHRPTTHD | URLAUTHRSTTHD | RFCHKALMSW | RFCHKRPTTHD | RFCHKRSTTHD | ORGFALMSW | ORGFALMRPTTHD | ORGFALMRSTTHD | UKWNALMSW | UKWNALMRPTTHD | UKWNALMRSTTHD | RESALARMSW | RESALMRPTTHD | RESALMRSTTHD | UESRVFALMSW | UESRVFALMRPTTHD | UESRVFALMRSTTHD | DNSFTALMSW | DNSFTALMTM | DNSFTRSTTM | ALMRPTOPTSW |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 初始值 | 5 | ENABLE | 100 | 10 | ENABLE | 100 | 10 | ENABLE | 100 | 10 | ENABLE | 100 | 10 | ENABLE | 80 | 75 | ENABLE | 100 | 10 | ENABLE | 5 | 1 | ENABLE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ALAMCHECKTIME | 告警检测时长（分钟） | 可选必选说明：可选参数<br>参数含义：该参数用来指定告警检测时长。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1~30，单位为分钟。<br>默认值：无<br>配置原则：无 |
| URLAUTHALMSW | URL鉴权失败告警开关 | 可选必选说明：可选参数<br>参数含义：该参数用于控制开启或关闭URL鉴权失败告警开关。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能URL鉴权失败告警。<br>- ENABLE：使能URL鉴权失败告警。<br>默认值：无<br>配置原则：无 |
| URLAUTHRPTTHD | URL鉴权告警上报阈值（万分比） | 可选必选说明：条件可选参数<br>前提条件：该参数在“URLAUTHALMSW”配置为“ENABLE”时为可选参数。<br>参数含义：该参数用来指定URL鉴权告警上报阈值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0~10000，单位为万分比。<br>默认值：无<br>配置原则：无 |
| URLAUTHRSTTHD | URL鉴权告警恢复阈值（万分比） | 可选必选说明：条件可选参数<br>前提条件：该参数在“URLAUTHALMSW”配置为“ENABLE”时为可选参数。<br>参数含义：该参数用来指定URL鉴权告警恢复阈值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0~10000，单位为万分比。<br>默认值：无<br>配置原则：无 |
| RFCHKALMSW | Referer校验失败告警开关 | 可选必选说明：可选参数<br>参数含义：该参数用于控制开启或关闭Referer校验失败告警开关。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能Referer校验失败告警。<br>- ENABLE：使能Referer校验失败告警。<br>默认值：无<br>配置原则：无 |
| RFCHKRPTTHD | Referer校验告警上报阈值（万分比） | 可选必选说明：条件可选参数<br>前提条件：该参数在“RFCHKALMSW”配置为“ENABLE”时为可选参数。<br>参数含义：该参数用来指定Referer校验告警上报阈值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0~10000，单位为万分比。<br>默认值：无<br>配置原则：无 |
| RFCHKRSTTHD | Referer校验告警恢复阈值（万分比） | 可选必选说明：条件可选参数<br>前提条件：该参数在“RFCHKALMSW”配置为“ENABLE”时为可选参数。<br>参数含义：该参数用来指定Referer校验告警恢复阈值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0~10000，单位为万分比。<br>默认值：无<br>配置原则：无 |
| ORGFALMSW | 回源失败告警开关 | 可选必选说明：可选参数<br>参数含义：该参数用于控制开启或关闭回源失败告警开关。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能媒体中继回源失败告警。<br>- ENABLE：使能媒体中继回源失败告警。<br>默认值：无<br>配置原则：无 |
| ORGFALMRPTTHD | 回源失败告警上报阈值（万分比） | 可选必选说明：条件可选参数<br>前提条件：该参数在“ORGFALMSW”配置为“ENABLE”时为可选参数。<br>参数含义：该参数用来指定回源失败告警上报阈值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0~10000，单位为万分比。<br>默认值：无<br>配置原则：无 |
| ORGFALMRSTTHD | 回源失败告警恢复阈值（万分比） | 可选必选说明：条件可选参数<br>前提条件：该参数在“ORGFALMSW”配置为“ENABLE”时为可选参数。<br>参数含义：该参数用来指定回源失败告警恢复阈值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0~10000，单位为万分比。<br>默认值：无<br>配置原则：无 |
| UKWNALMSW | 未知类型的媒体访问告警开关 | 可选必选说明：可选参数<br>参数含义：该参数用于控制开启或关闭未知类型的媒体访问告警开关。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能未知类型的媒体访问告警。<br>- ENABLE：使能未知类型的媒体访问告警。<br>默认值：无<br>配置原则：无 |
| UKWNALMRPTTHD | 未知媒体访问告警上报阈值（万分比） | 可选必选说明：条件可选参数<br>前提条件：该参数在“UKWNALMSW”配置为“ENABLE”时为可选参数。<br>参数含义：该参数用来指定未知媒体访问告警上报阈值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0~10000，单位为万分比。<br>默认值：无<br>配置原则：无 |
| UKWNALMRSTTHD | 未知媒体访问告警恢复阈值（万分比） | 可选必选说明：条件可选参数<br>前提条件：该参数在“UKWNALMSW”配置为“ENABLE”时为可选参数。<br>参数含义：该参数用来指定未知媒体访问告警恢复阈值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0~10000，单位为万分比。<br>默认值：无<br>配置原则：无 |
| RESALARMSW | Relay资源不足告警开关 | 可选必选说明：可选参数<br>参数含义：该参数用于控制开启或关闭Relay资源不足告警开关。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能Relay资源阈值告警告警。<br>- ENABLE：使能Relay资源阈值告警告警。<br>默认值：无<br>配置原则：无 |
| RESALMRPTTHD | Relay资源不足告警上报阈值（百分比） | 可选必选说明：条件可选参数<br>前提条件：该参数在“RESALARMSW”配置为“ENABLE”时为可选参数。<br>参数含义：该参数用来指定Relay资源不足告警上报阈值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0~100，单位为百分比。<br>默认值：无<br>配置原则：无 |
| RESALMRSTTHD | Relay资源不足告警恢复阈值（百分比） | 可选必选说明：条件可选参数<br>前提条件：该参数在“RESALARMSW”配置为“ENABLE”时为可选参数。<br>参数含义：该参数用来指定Relay资源不足告警恢复阈值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0~100，单位为百分比。<br>默认值：无<br>配置原则：无 |
| UESRVFALMSW | 媒体中继UE业务失败告警开关 | 可选必选说明：可选参数<br>参数含义：该参数用于控制开启或关闭媒体中继UE业务失败告警开关。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能媒体中继UE业务失败告警。<br>- ENABLE：使能媒体中继UE业务失败告警。<br>默认值：无<br>配置原则：无 |
| UESRVFALMRPTTHD | UE业务失败告警上报阈值（万分比） | 可选必选说明：条件可选参数<br>前提条件：该参数在“UESRVFALMSW”配置为“ENABLE”时为可选参数。<br>参数含义：该参数用来指定UE业务失败告警上报阈值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0~10000，单位为万分比。<br>默认值：无<br>配置原则：无 |
| UESRVFALMRSTTHD | UE业务失败告警恢复阈值（万分比） | 可选必选说明：条件可选参数<br>前提条件：该参数在“UESRVFALMSW”配置为“ENABLE”时为可选参数。<br>参数含义：该参数用来指定UE业务失败告警恢复阈值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0~10000，单位为万分比。<br>默认值：无<br>配置原则：无 |
| DNSFTALMSW | DNS故障告警开关 | 可选必选说明：可选参数<br>参数含义：该参数用于控制开启或关闭DNS故障告警开关。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能DNS故障告警开关。<br>- ENABLE：使能DNS故障告警开关。<br>默认值：无<br>配置原则：无 |
| DNSFTALMTM | DNS故障告警检测时长（分钟） | 可选必选说明：条件可选参数<br>前提条件：该参数在“DNSFTALMSW”配置为“ENABLE”时为可选参数。<br>参数含义：该参数用来指定DNS故障告警检测时长。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1~60，单位为分钟。<br>默认值：无<br>配置原则：无 |
| DNSFTRSTTM | DNS告警恢复检测时长（分钟） | 可选必选说明：条件可选参数<br>前提条件：该参数在“DNSFTALMSW”配置为“ENABLE”时为可选参数。<br>参数含义：该参数用来指定DNS告警恢复检测时长。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1~10，单位为分钟。<br>默认值：无<br>配置原则：无 |
| ALMRPTOPTSW | 告警上报优化开关 | 可选必选说明：可选参数<br>参数含义：该参数用于控制开启或关闭告警上报优化开关。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能告警上报优化开关。<br>- ENABLE：使能告警上报优化开关。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@RELAYSALMPARA]] · 媒体中继业务告警参数配置（RELAYSALMPARA）

## 使用实例

假如需要配置媒体中继业务告警参数，则命令如下：

```
SET RELAYSALMPARA:ALAMCHECKTIME=10;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-RELAYSALMPARA.md`
