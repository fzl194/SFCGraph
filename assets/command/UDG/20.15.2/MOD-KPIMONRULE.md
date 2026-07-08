---
id: UDG@20.15.2@MMLCommand@MOD KPIMONRULE
type: MMLCommand
name: MOD KPIMONRULE（修改KPI异常检测规则）
nf: UDG
version: 20.15.2
verb: MOD
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

# MOD KPIMONRULE（修改KPI异常检测规则）

## 功能

该命令用于修改KPI异常检测规则。

> **说明**
> - 该命令执行后立即生效。
>
> - 修改规则时，测量指标ID必须在产品文档的KPI异常检测白名单中存在，当白名单中对应的规则配置了对象实例ID时，MML输入的对象实例ID要保持一致。
> - 修改规则时，若历史KPI符合该异常检测规则将不会立即触发“ALM-100624 业务指标异常”告警上报，若修改该规则后的KPI符合该异常检测规则，将触发“ALM-100624 业务指标异常”告警上报。
> - 修改后的阈值上限和阈值下限至少存在一个有效值。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| METRICTYPE | 指标类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定指标类型。<br>数据来源：本端规划<br>取值范围：<br>- KPI（KPI）<br>默认值：无<br>配置原则：无 |
| METRICID | 测量指标ID | 可选必选说明：必选参数<br>参数含义：该参数用于指定测量指标ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~4294967295。<br>默认值：无<br>配置原则：无 |
| MOIID | 对象实例ID | 可选必选说明：必选参数<br>参数含义：该参数用于指定对象实例ID。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：无 |
| PRD | 测量周期 | 可选必选说明：可选参数<br>参数含义：该参数用于指定指标的测量周期。<br>数据来源：本端规划<br>取值范围：<br>- FIVE（5分钟）<br>默认值：无<br>配置原则：无 |
| ALGORITHM | 检测算法 | 可选必选说明：可选参数<br>参数含义：该参数用于指定检测算法。<br>数据来源：本端规划<br>取值范围：<br>- AVERAGE（7天平均值同比）<br>默认值：无<br>配置原则：无 |
| LOWERTHRESHOLD | 阈值下限 | 可选必选说明：可选参数<br>参数含义：该参数用于指定阈值下限。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~100，单位是百分比。<br>默认值：无<br>配置原则：<br>参数配置为0（无效值）时，表示取消阈值下限。 |
| UPPERTHRESHOLD | 阈值上限 | 可选必选说明：可选参数<br>参数含义：该参数用于指定阈值上限。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0，100~10000，单位是百分比。<br>默认值：无<br>配置原则：<br>参数配置为0（无效值）时，表示取消阈值上限。 |
| ALARMSWITCH | 告警开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定告警开关。<br>数据来源：本端规划<br>取值范围：<br>- ON（开启）<br>- OFF（关闭）<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [KPI异常检测规则（KPIMONRULE）](configobject/UDG/20.15.2/KPIMONRULE.md)

## 使用实例

修改测量指标ID为2000000001，对象实例ID为MOIID_1的KPI异常检测规则：修改阈值下限为50%，修改阈值上限为200%，修改告警开关为关闭。

```
MOD KPIMONRULE: METRICTYPE=KPI, METRICID=2000000001, MOIID="MOIID_1", LOWERTHRESHOLD=50, UPPERTHRESHOLD=200, ALARMSWITCH=OFF;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改KPI异常检测规则（MOD-KPIMONRULE）_35322749.md`
