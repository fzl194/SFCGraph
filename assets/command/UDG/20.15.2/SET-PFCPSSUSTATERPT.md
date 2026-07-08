---
id: UDG@20.15.2@MMLCommand@SET PFCPSSUSTATERPT
type: MMLCommand
name: SET PFCPSSUSTATERPT（设置智能单元状态上报开关相关属性）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: PFCPSSUSTATERPT
command_category: 配置类
applicable_nf:
- UPF
- PGW-U
- SGW-U
effect_mode: 立即生效
is_dangerous: false
max_records: 1
category_path:
- 用户面服务管理
- 路径管理
- PFCP路径管理
- PFCP负荷上报管理
- SSU负荷上报
status: active
---

# SET PFCPSSUSTATERPT（设置智能单元状态上报开关相关属性）

## 功能

**适用NF：UPF、PGW-U、SGW-U**

该命令用于设置智能单元状态上报开关相关属性。包括过载上报阈值，过载停止上报阈值和定时器值。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SWITCH | 配置智能单元状态上报的开关 | 可选必选说明：必选参数<br>参数含义：该参数是配置智能单元状态上报的开关。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：<br>- ENABLE：使能智能单元状态上报功能。<br>- DISABLE：不使能智能单元状态上报功能。 |
| OVERLOADRPTTHD | 过载上报阈值 | 可选必选说明：条件可选参数<br>前提条件：该参数在“SWITCH”配置为“ENABLE”时为可选参数。<br>参数含义：过载上报阈值，过载达到阈值后，通知SMF过载状态。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～100。<br>默认值：无<br>配置原则：无 |
| OVERLOADSTOPTHD | 过载停止上报阈值 | 可选必选说明：条件可选参数<br>前提条件：该参数在“SWITCH”配置为“ENABLE”时为可选参数。<br>参数含义：过载停止上报阈值，过载上报后，低于过载停止上报阈值时，通知SMF正常状态；负载低于停止上报阈值后，后续若负载未达到上报阈值，则不再通知SMF。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～100。<br>默认值：无<br>配置原则：无 |
| TIMERVALUE | 指定定时器值 | 可选必选说明：条件可选参数<br>前提条件：该参数在“SWITCH”配置为“ENABLE”时为可选参数。<br>参数含义：指定定时器值，定期通知SMF智能单元状态，取值为0时表示关闭定期通知。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～60，单位为分钟。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@PFCPSSUSTATERPT]] · 智能单元状态上报相关属性（PFCPSSUSTATERPT）

## 使用实例

设置智能单元状态上报开关为ENABLE时，设置过载上报阈值为90：

```
SET PFCPSSUSTATERPT:SWITCH=ENABLE,OVERLOADRPTTHD=90;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-PFCPSSUSTATERPT.md`
