---
id: UDG@20.15.2@ConfigObject@PMCFG
type: ConfigObject
name: PMCFG（性能统计配置参数）
nf: UDG
version: 20.15.2
object_name: PMCFG
object_kind: global_setting
status: active
---

# PMCFG（性能统计配置参数）

## 说明

![](设置性能统计配置参数(SET PMCFG)_11513104.assets/notice_3.0-zh-cn.png)

执行该命令会改变性能统计的配置，会对性能统计造成影响，请慎重执行。

执行该命令配置过性能统计参数，会优先使用配置参数，如需使默认参数生效，请使用此命令清除配置参数。

该命令用于设置性能统计的配置参数。

> **说明**
> 该命令存在系统初始值，系统初始值如下 [表1](#ZH-CN_MMLREF_0000001111513104__table712075721115) 。
>
> *表1 系统指标量初始值列表*
>
> | 类型 | 开关 | 单周期结果指标量 | 多周期结果指标量 | 原始指标量/实例 | 告警阈值比例(%) |
> | --- | --- | --- | --- | --- | --- |
> | MAX_METRIC_BEFORE_CALC(最大原始指标量) | ON(开启) | 无 | 无 | 50000000/40000000/56000000<br>注：默认规格随部署资源(PMSCalc CPU/实例数)变动<br>PMSCalc CPU限额低于2.5 vCPUs，2个OMU：50000000<br>PMSCalc CPU限额大于等于2.5 vCPUs，2个OMU： 56000000<br>PMSCalc 4个OMU： 40000000<br>修改过原始指标量的配置值，则默认规格不随环境扩缩容自适应。 | 100 |
> | MAX_METRIC_AFTER_CALC(最大结果指标量) | ON(开启) | 2500000 | 5000000 | 无 | 100 |
>
> *表2 话统不可信标识开关初始值列表*
>
> | 参数 | 值 |
> | --- | --- |
> | METRIC_SUSPECT_FLAG(话统不可信标识) | ON(开启) |
> | RANGE | ALL(全局) |
> | ME_CACHE | OFF(关闭) |
>
> *表3 指标无效值呈现为零开关初始值列表*
>
> | 类型 | 开关 |
> | --- | --- |
> | METRIC_INVALID_VALUE_DISPLAY_ZERO(指标无效值呈现为零) | OFF(关闭) |
>
> *表4 话统存储时长初始值列表*
>
> | 类型 | 测量周期 | 存储时长(小时) |
> | --- | --- | --- |
> | PERF_STORAGE_DURATION(话统存储时长) | FIVE(5分钟) | 168 |
> | PERF_STORAGE_DURATION(话统存储时长) | FIFTEEN(15分钟) | 336 |
> | PERF_STORAGE_DURATION(话统存储时长) | THIRTY(30分钟) | 720 |
> | PERF_STORAGE_DURATION(话统存储时长) | SIXTY(1小时) | 720 |
> | PERF_STORAGE_DURATION(话统存储时长) | ONE_DAY(一天) | 1440 |
>
> *表5 流式采集KPI的最大指标量初始值列表*
>
> | 类型 | 5秒周期最大指标量 | 1分钟周期最大指标量 |
> | --- | --- | --- |
> | STREAM_COLLECT_KPI(流式采集KPI的最大指标量) | 50 | 500 |
>
> *表6 话统北向上报时延初始值列表*
>
> | 类型 | 上报超时时长 | 上报超时判断时长 |
> | --- | --- | --- |
> | PERF_DELAY(话统北向上报时延) | 290 | 60 |
>
> *表7 话统信息收集(CSV)初始值列表*
>
> | 类型 | 开关 | 文件行数 | 目录拆分方式 |
> | --- | --- | --- | --- |
> | PERF_COLLECT_CSV(话统信息收集(CSV)) | OFF(关闭) | 100000 | NO_DIRECTORY(无目录) |

## 操作本对象的命令

- [LST PMCFG](command/UDG/20.15.2/LST-PMCFG.md)
- [SET PMCFG](command/UDG/20.15.2/SET-PMCFG.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询性能统计配置参数(LST-PMCFG)_11353212.md`
- 原始手册：`evidence/UDG/20.15.2/设置性能统计配置参数(SET-PMCFG)_11513104.md`
