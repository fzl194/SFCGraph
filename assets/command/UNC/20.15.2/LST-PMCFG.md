---
id: UNC@20.15.2@MMLCommand@LST PMCFG
type: MMLCommand
name: LST PMCFG（查询性能统计配置参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PMCFG
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 性能统计
status: active
---

# LST PMCFG（查询性能统计配置参数）

## 功能

该命令用于查询性能统计的配置参数。

## 注意事项

无。

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TYPE | 类型 | 可选必选说明：可选参数。<br>参数含义：配置类型。若不输入，则表示该参数不作为查询的限制条件。<br>取值范围：<br>- MAX_METRIC_BEFORE_CALC(最大原始指标量)<br>- MAX_METRIC_AFTER_CALC(最大结果指标量)<br>- METRIC_SUSPECT_FLAG(话统不可信标识)：话统不可信标识对外呈现开关<br>- METRIC_INVALID_VALUE_DISPLAY_ZERO(指标无效值呈现为零)：指标无效值是否呈现为0<br>- PERF_STORAGE_DURATION(话统存储时长)<br>- STREAM_COLLECT_KPI(流式采集KPI的最大指标量)：流式采集KPI的最大指标量配置<br>- PERF_DELAY(话统北向上报时延)：话统北向上报时延<br>- PERF_COLLECT_CSV(话统信息收集(CSV))：对话统信息收集CSV文件的配置<br>默认值：无。<br>配置原则：无。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PMCFG]] · 性能统计配置参数（PMCFG）

## 使用实例

查询性能统计配置参数：

```
%%LST PMCFG:;%%
RETCODE = 0  操作成功

性能统计配置参数
----------------
类型                                                   参数名称             参数值    

MAX_METRIC_AFTER_CALC(最大结果指标量)                  开关                 开启      
MAX_METRIC_AFTER_CALC(最大结果指标量)                  告警阈值比例         100%      
MAX_METRIC_AFTER_CALC(最大结果指标量)                  单周期结果指标量     2500000   
MAX_METRIC_AFTER_CALC(最大结果指标量)                  多周期结果指标量     5000000   
MAX_METRIC_BEFORE_CALC(最大原始指标量)                 开关                 开启      
MAX_METRIC_BEFORE_CALC(最大原始指标量)                 告警阈值比例         90%       
MAX_METRIC_BEFORE_CALC(最大原始指标量)                 原始指标量/实例      8000000   
METRIC_INVALID_VALUE_DISPLAY_ZERO(指标无效值呈现为零)  开关                 关闭      
METRIC_SUSPECT_FLAG(话统不可信标识)                    开关                 开启
METRIC_SUSPECT_FLAG(话统不可信标识)                    指标缓存             开启
METRIC_SUSPECT_FLAG(话统不可信标识)                    范围                 全局
PERF_COLLECT_CSV(话统信息收集(CSV))                    开关                 开启       
PERF_COLLECT_CSV(话统信息收集(CSV))                    目录拆分方式         测量对象   
PERF_COLLECT_CSV(话统信息收集(CSV))                    文件行数             1000001    
PERF_COLLECT_CSV(话统信息收集(CSV))                    测量对象类时间配置   ALL:5:10   
PERF_COLLECT_CSV(话统信息收集(CSV))                    测量单元ID黑名单     456,789    
PERF_COLLECT_CSV(话统信息收集(CSV))                    测量单元ID白名单     123       
PERF_DELAY(话统北向上报时延)                           上报超时时长         199       
PERF_DELAY(话统北向上报时延)                           上报超时判断时长     199       
STREAM_COLLECT_KPI(流式采集KPI的最大指标量)            1分钟周期最大指标量  500       
STREAM_COLLECT_KPI(流式采集KPI的最大指标量)            5秒周期最大指标量    50        
PERF_STORAGE_DURATION(话统存储时长)                    5分钟周期            168小时   
PERF_STORAGE_DURATION(话统存储时长)                    15分钟周期           336小时   
PERF_STORAGE_DURATION(话统存储时长)                    30分钟周期           720小时   
PERF_STORAGE_DURATION(话统存储时长)                    60分钟周期           720小时   
PERF_STORAGE_DURATION(话统存储时长)                    1天周期              1440小时  
(结果个数 = 26)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询性能统计配置参数(LST-PMCFG)_11353212.md`
