---
id: UNC@20.15.2@MMLCommand@SET NOCDRALM
type: MMLCommand
name: SET NOCDRALM（设置未接收到话单告警参数）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: NOCDRALM
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
- 维护管理
- 未接收到话单告警参数
status: active
---

# SET NOCDRALM（设置未接收到话单告警参数）

## 功能

**适用NF：NCG**

该命令用于设置 [**ALM-82021 NCG长时间未接收到话单**](../../../../../../../../../网络运维/故障处理/UNC告警处理/业务告警/NCG/ALM-82021 vCG长时间未接收到话单_51174216.md) 告警的管理参数。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 该命令存在系统初始设置记录，参数的初始设置值如下表：

| SWITCHSTATE | TIMEOUT |
| --- | --- |
| OFF | 5 |

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SWITCHSTATE | 告警开关 | 可选必选说明：必选参数<br>参数含义：该参数用于设置是否支持<br>[**ALM-82021 NCG长时间未接收到话单**](../../../../../../../../../网络运维/故障处理/UNC告警处理/业务告警/NCG/ALM-82021 vCG长时间未接收到话单_51174216.md)<br>告警上报，“OFF(关闭)”为禁止上报此告警，“ON(开启)”为支持上报此告警。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- OFF：关闭。<br>- ON：开启。<br>默认值：无<br>配置原则：无 |
| TIMEOUT | 告警检测周期（分钟） | 可选必选说明：条件可选参数<br>前提条件：该参数在“SWITCHSTATE”配置为“ON”时为条件可选参数。<br>参数含义：该参数用于设置NCG的<br>[**ALM-82021 NCG长时间未接收到话单**](../../../../../../../../../网络运维/故障处理/UNC告警处理/业务告警/NCG/ALM-82021 vCG长时间未接收到话单_51174216.md)<br>告警的检测周期。超过这个时间，NCG未接收到链路上的话单时，则发送此告警。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为1～1440。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [未接收到话单告警参数（NOCDRALM）](configobject/UNC/20.15.2/NOCDRALM.md)

## 使用实例

设置 [**ALM-82021 NCG长时间未接收到话单**](../../../../../../../../../网络运维/故障处理/UNC告警处理/业务告警/NCG/ALM-82021 vCG长时间未接收到话单_51174216.md) 的“告警开关”为“ON(开启)”，“告警检测周期（分钟）”为默认值“5”：

```
SET NOCDRALM: SWITCHSTATE=ON, TIMEOUT=5;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置未接收到话单告警参数（SET-NOCDRALM）_51174320.md`
