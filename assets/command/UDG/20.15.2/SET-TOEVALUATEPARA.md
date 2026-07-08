---
id: UDG@20.15.2@MMLCommand@SET TOEVALUATEPARA
type: MMLCommand
name: SET TOEVALUATEPARA（设置TCP优化评估配置信息）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: TOEVALUATEPARA
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 1
category_path:
- TCP优化服务管理
- TCP优化评估配置
status: active
---

# SET TOEVALUATEPARA（设置TCP优化评估配置信息）

## 功能

**适用NF：PGW-U、UPF**

该命令用于设置TCP优化评估配置信息。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | TOEVASWITCH | TOEVASAMPRATIO |
| --- | --- | --- |
| 初始值 | DISABLE | 100 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TOEVASWITCH | TCP优化评估开关 | 可选必选说明：可选参数<br>参数含义：该参数用于设置TCP优化评估开关。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |
| TOEVASAMPRATIO | TCP优化评估抽样比率 | 可选必选说明：条件可选参数<br>前提条件：该参数在“TOEVASWITCH”配置为“ENABLE”时为可选参数。<br>参数含义：该参数用于设置TCP优化评估抽样比率。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～100。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@TOEVALUATEPARA]] · TCP优化评估配置信息（TOEVALUATEPARA）

## 使用实例

开启TCP优化评估开关，设置TCP优化评估抽样比率为50%：

```
SET TOEVALUATEPARA:TOEVASWITCH=ENABLE,TOEVASAMPRATIO=50;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-TOEVALUATEPARA.md`
