---
id: UNC@20.15.2@MMLCommand@SET ERRCDRALM
type: MMLCommand
name: SET ERRCDRALM（设置错误话单告警参数）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: ERRCDRALM
command_category: 配置类
applicable_nf:
- NCG
effect_mode: 立即生效
is_dangerous: false
max_records: 1
category_path:
- 业务服务管理
- NCG业务及策略管理
- 计费管理
- 业务系统管理
- 错误话单告警管理
status: active
---

# SET ERRCDRALM（设置错误话单告警参数）

## 功能

**适用NF：NCG**

该命令用于设置NCG在话单处理过程中对错误话单的监控模式，根据不同的监控模式上报不同的错误话单告警。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 该命令存在系统初始设置记录，参数的初始设置值如下表：

| MONITORMODE |
| --- |
| PERIOD |

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MONITORMODE | 监控模式 | 可选必选说明：必选参数<br>参数含义：用于选择NCG对错误话单的监控模式。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- PERIOD：周期性。<br>- REAL-TIME：实时性。<br>默认值：无<br>配置原则：<br>- “PERIOD(周期性)”：表示NCG每隔5分钟监控一次异常话单的张数，如果5分钟之内异常话单张数超过100张，上报告警“[**ALM-82019 收到异常话单**](../../../../../../../../网络运维/故障处理/UNC告警处理/业务告警/NCG/ALM-82019 收到异常话单_51174214.md)”。<br>- “REAL-TIME(实时性)”：表示NCG实时监控异常话单文件，当产生一个异常的最终话单文件时，上报告警“[**ALM-82020 发现异常话单文件**](../../../../../../../../网络运维/故障处理/UNC告警处理/业务告警/NCG/ALM-82020 发现异常话单文件_51174215.md)”。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/ERRCDRALM]] · 错误话单告警参数（ERRCDRALM）

## 使用实例

设置NCG对错误话单的“监控模式”为“PERIOD(周期性)”：

```
SET ERRCDRALM: MONITORMODE=PERIOD;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置错误话单告警参数（SET-ERRCDRALM）_51174331.md`
