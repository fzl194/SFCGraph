---
id: UDG@20.15.2@MMLCommand@SET VOLTESWALBRK
type: MMLCommand
name: SET VOLTESWALBRK（设置VoLTE滑窗相关的参数）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: VOLTESWALBRK
command_category: 配置类
applicable_nf:
- PGW-U
effect_mode: 立即生效
is_dangerous: false
max_records: 1
category_path:
- 用户面服务管理
- VoLTE质量监控配置
- VoLTE吞字断续配置
status: active
---

# SET VOLTESWALBRK（设置VoLTE滑窗相关的参数）

## 功能

**适用NF：PGW-U**

该命令用于配置VoLTE吞字断续检测的相关参数。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | SWITCH | SWALLOWWIN | SWALLOWWINTHD | BREAKWIN | BREAKWINTHD |
| --- | --- | --- | --- | --- | --- |
| 初始值 | DISABLE | 20 | 12 | 50 | 30 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SWITCH | 功能开关 | 可选必选说明：必选参数<br>参数含义：该参数用于配置VoLTE吞字断续检测开关。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能（关闭）。<br>- ENABLE：使能（开启）。<br>默认值：无<br>配置原则：无 |
| SWALLOWWIN | 吞字滑窗大小 | 可选必选说明：条件可选参数<br>前提条件：该参数在“SWITCH”配置为“ENABLE”时为可选参数。<br>参数含义：该参数用于配置VoLTE吞字滑窗大小。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为5～64。必须小于断续滑窗大小。<br>默认值：无<br>配置原则：配置过大或者过小，影响语音质量统计和报表呈现, 建议参考现网语音吞字断续配置。 |
| SWALLOWWINTHD | 吞字的滑窗阈值 | 可选必选说明：条件可选参数<br>前提条件：该参数在“SWITCH”配置为“ENABLE”时为可选参数。<br>参数含义：该参数用于配置吞字的滑窗阈值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为5～64。必须小于等于吞字滑窗大小且小于断续的滑窗阈值。<br>默认值：无<br>配置原则：配置过大或者过小，影响语音质量统计和报表呈现, 建议参考现网语音吞字断续配置。 |
| BREAKWIN | 断续滑窗大小 | 可选必选说明：条件可选参数<br>前提条件：该参数在“SWITCH”配置为“ENABLE”时为可选参数。<br>参数含义：该参数用于配置VoLTE断续滑窗大小。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为6～128。必须大于吞字滑窗大小。<br>默认值：无<br>配置原则：配置过大或者过小，影响语音质量统计和报表呈现, 建议参考现网语音吞字断续配置。 |
| BREAKWINTHD | 断续的滑窗阈值 | 可选必选说明：条件可选参数<br>前提条件：该参数在“SWITCH”配置为“ENABLE”时为可选参数。<br>参数含义：该参数用于配置断续的滑窗阈值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为6～128。必须小于等于断续滑窗大小且大于吞字的滑窗阈值。<br>默认值：无<br>配置原则：配置过大或者过小，影响语音质量统计和报表呈现, 建议参考现网语音吞字断续配置。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@VOLTESWALBRK]] · VoLTE滑窗相关的参数（VOLTESWALBRK）

## 使用实例

开启VoLTE吞字断续检测上报开关：

```
SET VOLTESWALBRK: SWITCH=ENABLE, SWALLOWWIN=20, SWALLOWWINTHD=12, BREAKWIN=50, BREAKWINTHD=30;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-VOLTESWALBRK.md`
