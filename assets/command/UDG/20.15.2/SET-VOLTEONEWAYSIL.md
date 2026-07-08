---
id: UDG@20.15.2@MMLCommand@SET VOLTEONEWAYSIL
type: MMLCommand
name: SET VOLTEONEWAYSIL（设置单通检测信息）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: VOLTEONEWAYSIL
command_category: 配置类
applicable_nf:
- PGW-U
effect_mode: 立即生效
is_dangerous: false
max_records: 1
category_path:
- 用户面服务管理
- VoLTE质量监控配置
- VoLTE单通检测
status: active
---

# SET VOLTEONEWAYSIL（设置单通检测信息）

## 功能

**适用NF：PGW-U**

该命令用于设置单通检测的开关、丢包率和MOS周期。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 不建议关闭，关闭后无法进行Volte单通检测。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | ONEWAYSILSW | ONEWAYSILTHD | ONEWAYSILPERIOD |
| --- | --- | --- | --- |
| 初始值 | ENABLE | 25 | 3 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ONEWAYSILSW | 单通检测开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定单通检测的开关。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能（关闭）。<br>- ENABLE：使能（开启）。<br>默认值：无<br>配置原则：无 |
| ONEWAYSILTHD | 单通检测丢包率阈值 | 可选必选说明：可选参数<br>参数含义：该参数用于指定单通检测的丢包率门限。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为5～50，单位是百分比。5到50之间的整数。<br>默认值：无<br>配置原则：配置过大或者过小，会导致语音质量MOS评价结果变化，建议参考实际的语音质量配置。 |
| ONEWAYSILPERIOD | 单通检测的连续MOS计算周期数 | 可选必选说明：可选参数<br>参数含义：该参数用于指定单通检测的连续MOS计算周期数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～10。1到10之间的整数。<br>默认值：无<br>配置原则：配置过大或者过小，会导致语音质量MOS评价结果变化，建议参考实际的语音质量配置。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/VOLTEONEWAYSIL]] · 单通检测的系统初始设置值（VOLTEONEWAYSIL）

## 使用实例

设置单通检测的开关、丢包率和MOS周期：

```
SET VOLTEONEWAYSIL: ONEWAYSILSW=ENABLE, ONEWAYSILTHD=5, ONEWAYSILPERIOD=2;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置单通检测信息（SET-VOLTEONEWAYSIL）_57738485.md`
