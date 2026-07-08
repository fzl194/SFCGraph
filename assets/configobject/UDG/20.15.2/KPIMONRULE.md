---
id: UDG@20.15.2@ConfigObject@KPIMONRULE
type: ConfigObject
name: KPIMONRULE（KPI异常检测规则）
nf: UDG
version: 20.15.2
object_name: KPIMONRULE
object_kind: entity
status: active
---

# KPIMONRULE（KPI异常检测规则）

## 说明

该命令用于增加KPI异常检测规则。

> **说明**
> - 该命令执行后立即生效。
>
> - 添加规则时，测量指标ID必须在产品文档的KPI异常检测白名单中存在，当白名单中对应的规则配置了对象实例ID时，MML添加时输入的对象实例ID要保持一致。
> - 添加规则时，阈值上限和阈值下限至少存在一个有效值。
> - 添加规则时，若历史KPI符合该异常检测规则将不会立即触发“ALM-100624 业务指标异常”告警上报，若添加该规则后的KPI符合该异常检测规则，将触发“ALM-100624 业务指标异常”告警上报。
> - 本命令限制最多可以添加100条KPI规则，其中包含系统初始存在的规则和人工执行本命令下发的规则。
> - 执行[**DSP KPIMONSTATE**](显示系统中正在监控的KPI信息（DSP KPIMONSTATE）_35442885.md)可以查询到所有的KPI规则，执行[**LST KPIMONRULE**](查询KPI异常检测规则（LST KPIMONRULE）_87324058.md)可以查询到人工执行本命令已下发的规则。
>
> - 最多可输入100条记录。

## 操作本对象的命令

- [[command/UDG/20.15.2/ADD-KPIMONRULE]] · ADD KPIMONRULE
- [[command/UDG/20.15.2/LST-KPIMONRULE]] · LST KPIMONRULE
- [[command/UDG/20.15.2/MOD-KPIMONRULE]] · MOD KPIMONRULE
- [[command/UDG/20.15.2/RMV-KPIMONRULE]] · RMV KPIMONRULE

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改KPI异常检测规则（MOD-KPIMONRULE）_35322749.md`
- 原始手册：`evidence/UDG/20.15.2/删除KPI异常检测规则（RMV-KPIMONRULE）_87483786.md`
- 原始手册：`evidence/UDG/20.15.2/增加KPI异常检测规则（ADD-KPIMONRULE）_87324054.md`
- 原始手册：`evidence/UDG/20.15.2/查询KPI异常检测规则（LST-KPIMONRULE）_87324058.md`
