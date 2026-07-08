---
id: UDG@20.15.2@MMLCommand@LST KPIMONRULE
type: MMLCommand
name: LST KPIMONRULE（查询KPI异常检测规则）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: KPIMONRULE
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 指标监控
status: active
---

# LST KPIMONRULE（查询KPI异常检测规则）

## 功能

该命令用于查询KPI异常检测规则。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| METRICTYPE | 指标类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定指标类型。<br>数据来源：本端规划<br>取值范围：<br>- KPI（KPI）<br>默认值：无<br>配置原则：无 |
| METRICID | 测量指标ID | 可选必选说明：可选参数<br>参数含义：该参数用于指定测量指标ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~4294967295。<br>默认值：无<br>配置原则：无 |
| MOIID | 对象实例ID | 可选必选说明：可选参数<br>参数含义：该参数用于指定对象实例ID。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [KPI异常检测规则（KPIMONRULE）](configobject/UDG/20.15.2/KPIMONRULE.md)

## 使用实例

查询当前配置的所有KPI异常检测规则。

```
%%LST KPIMONRULE:;%%
RETCODE = 0  操作成功

结果如下
--------
指标类型  测量指标ID  对象实例ID   测量周期  检测算法       阈值下限  阈值上限  告警开关  

KPI       2000000001  MOIID_1      5分钟     7天平均值同比  80        150       开启      
KPI       2000000002  MOIID_2      5分钟     7天平均值同比  70        160       开启      
KPI       2000000003  MOIID_3      5分钟     7天平均值同比  80        150       开启      
(结果个数 = 3)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询KPI异常检测规则（LST-KPIMONRULE）_87324058.md`
