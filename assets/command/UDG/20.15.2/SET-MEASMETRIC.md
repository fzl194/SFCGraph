---
id: UDG@20.15.2@MMLCommand@SET MEASMETRIC
type: MMLCommand
name: SET MEASMETRIC（设置话统测量指标参数）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: MEASMETRIC
command_category: 配置类
effect_mode: ''
is_dangerous: true
category_path:
- 平台服务管理
- 操作维护
- 性能统计
status: active
---

# SET MEASMETRIC（设置话统测量指标参数）

## 功能

![](设置话统测量指标参数(SET MEASMETRIC)_46417865.assets/notice_3.0-zh-cn.png)

该命令为高危命令，执行将修改话统测量指标的参数，影响该话统指标的上报，请慎重执行。

该命令用于设置话统测量指标参数。

> **说明**
> 无。

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MEID | 网元ID | 可选必选说明：必选参数。<br>参数含义：标识网元ID，可以通过<br>[**LST ME**](../../系统管理/版本信息/查询网元配置信息（LST ME）_47084797.md)<br>命令查询获取。<br>取值范围：0~65535。<br>默认值：无。<br>配置原则：无。 |
| METRICID | 测量指标ID | 可选必选说明：必选参数。<br>参数含义：测量指标ID，可以通过<br>[**LST MEASUNIT**](查询测量指标模型(LST MEASUNIT)_47814449.md)<br>命令查询获取。<br>取值范围：整数类型，取值范围为0~4294967294。<br>默认值：无。<br>配置原则：仅支持配置微服务指标。 |
| TYPE | 类型 | 可选必选说明：必选参数。<br>参数含义：支持变更的指标参数。<br>取值范围：枚举项。<br>METRIC_TYPE (指标分类)<br>默认值：无。<br>配置原则：无。 |
| METRIC_TYPE | 指标分类 | 可选必选说明：当TYPE类型为METRIC_TYPE时为条件必选参数。<br>参数含义：指标的分类选项。<br>取值范围：位域项<br>- NORTH(北向指标)<br>- BASIC(基础指标)<br>- EXTEND(扩展指标)<br>- KPI(KPI指标)<br>默认值：无。<br>配置原则：<br>- 不输入或“全部灰化”，表示指标分类恢复默认类型。<br>- “全部清空”，表示配置指标不属于任何指标分类。<br>- “全部选中”，表示配置指标属于取值范围四种指标分类。<br>- 勾选取值范围中的多个，表示配置指标属于所勾选指标分类。<br>- 指标分类去勾选或者非全部灰化，都表示指标不属于该指标分类。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/MEASMETRIC]] · 话统测量指标参数（MEASMETRIC）

## 使用实例

设置话统测量指标参数：

```
%%SET MEASMETRIC: MEID=800, METRICID=4100153, TYPE=METRIC_TYPE, METRIC_TYPE=KPI-1;%% 
RETCODE = 0  操作成功    

 ---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-MEASMETRIC.md`
