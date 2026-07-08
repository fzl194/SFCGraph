---
id: UDG@20.15.2@MMLCommand@SET CUSTATECHK
type: MMLCommand
name: SET CUSTATECHK（设置SMF和UPF的时间一致性校验）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: CUSTATECHK
command_category: 配置类
applicable_nf:
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 1
category_path:
- 用户面服务管理
- 业务控制策略
- 配置校验控制
- CP和UP关键配置不一致策略
status: active
---

# SET CUSTATECHK（设置SMF和UPF的时间一致性校验）

## 功能

**适用NF：UPF**

设置SMF和UPF时间不一致告警的参数。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- UTCDETECTMS参数配置范围过大时，可能会导致话单中时间戳上报不准确。建议误差配置取值不大于5000（5秒）。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | UTCTIMECHK | UTCDETECTMS | UTCALMRPTTHD | UTCALMCLRTHD |
| --- | --- | --- | --- | --- |
| 初始值 | DISABLE | 1000 | 10 | 5 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| UTCTIMECHK | UTC时间一致性校验开关 | 可选必选说明：必选参数<br>参数含义：该参数控制是否开启SMF和UPF之间的时间一致性校验。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |
| UTCDETECTMS | 检测误差阈值 | 可选必选说明：条件可选参数<br>前提条件：该参数在“UTCTIMECHK”配置为“ENABLE”时为可选参数。<br>参数含义：该参数用于指定SMF和UPF之间的UTC时间偏移阈值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～1800000，单位是毫秒。<br>默认值：无<br>配置原则：无 |
| UTCALMRPTTHD | 告警上报阈值 | 可选必选说明：条件可选参数<br>前提条件：该参数在“UTCTIMECHK”配置为“ENABLE”时为可选参数。<br>参数含义：该参数用于指定SMF和UPF网元时间不一致告警产生时的心跳检查周期。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～10000，单位是次数。<br>默认值：无<br>配置原则：无 |
| UTCALMCLRTHD | 告警恢复阈值 | 可选必选说明：条件可选参数<br>前提条件：该参数在“UTCTIMECHK”配置为“ENABLE”时为可选参数。<br>参数含义：该参数用于指定SMF和UPF网元时间不一致告警恢复时的心跳检查周期。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～10000，单位是次数。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/CUSTATECHK]] · SMF和UPF时间一致性检测（CUSTATECHK）

## 使用实例

通过命令配置SMF和UPF时间不一致告警的参数：

```
SET CUSTATECHK: UTCTIMECHK=ENABLE, UTCDETECTMS=1000, UTCALMRPTTHD=10, UTCALMCLRTHD=5;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-CUSTATECHK.md`
