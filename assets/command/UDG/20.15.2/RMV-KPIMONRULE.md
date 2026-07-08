---
id: UDG@20.15.2@MMLCommand@RMV KPIMONRULE
type: MMLCommand
name: RMV KPIMONRULE（删除KPI异常检测规则）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: KPIMONRULE
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 指标监控
status: active
---

# RMV KPIMONRULE（删除KPI异常检测规则）

## 功能

该命令用于删除KPI异常检测规则。

> **说明**
> 该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| METRICTYPE | 指标类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定指标类型。<br>数据来源：本端规划<br>取值范围：<br>- KPI（KPI）<br>默认值：无<br>配置原则：无 |
| METRICID | 测量指标ID | 可选必选说明：必选参数<br>参数含义：该参数用于指定测量指标ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~4294967295。<br>默认值：无<br>配置原则：无 |
| MOIID | 对象实例ID | 可选必选说明：必选参数<br>参数含义：该参数用于指定对象实例ID。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [KPI异常检测规则（KPIMONRULE）](configobject/UDG/20.15.2/KPIMONRULE.md)

## 使用实例

删除测量指标ID为2000000001，对象实例ID为MOIID_1的KPI异常检测规则。

```
RMV KPIMONRULE: METRICTYPE=KPI, METRICID=2000000001, MOIID="MOIID_1";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除KPI异常检测规则（RMV-KPIMONRULE）_87483786.md`
