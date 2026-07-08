---
id: UNC@20.15.2@MMLCommand@LST DBSTARTPARAS
type: MMLCommand
name: LST DBSTARTPARAS（查询DB启动参数值）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: DBSTARTPARAS
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- CSDB功能管理
- CSDB管理
- 参数管理
status: active
---

# LST DBSTARTPARAS（查询DB启动参数值）

## 功能

该命令用于查询当前配置的CSDB启动参数值。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| **参数标识** | **参数名称** | **参数说明** |
| --- | --- | --- |
| CLUSTERTYPE | 集群类型 | 可选必选说明：可选参数<br>参数含义: 该参数用于指定集群类型，分为普通集群和XSF集群。<br>数据来源：本端规划<br>取值范围：<br>- “COMMON_CLUSTER”：普通集群。<br>- “XSF_CLUSTER”：XSF集群。<br>默认值：无 |
| PARA | 参数 | 可选必选说明：可选参数<br>参数含义: 该参数用于指定需要查询的CSDB启动参数。<br>数据来源：本端规划<br>取值范围：<br>- “AGING_SCAN_INTERVAL(对象老化扫描间隔)”：数据老化扫描的时间间隔。<br>- “AGING_TIME_THRESHOLD(老化时间阈值)”：数据老化时间阈值。如果数据在设定时间内没有更新，则会被推送至对应的订阅者。<br>- “CLUSTER_AGING_THRESHOLD(集群间老化时间阈值)”：集群间老化时间阈值。老化阈值需要大于集群间核查周期“CLUSTER_CHECK_PERIOD”，否则未核查到的数据会被当成老化数据删除。一般大于2个周期。<br>- “CLUSTER_CHECK_INTERVAL(集群核查间隔)”：集群间核查间隔。<br>- “CLUSTER_CHECK_PERIOD(集群间核查周期)”：集群间核查周期，1个周期包括多个间隔。<br>- “CLUSTER_INCONSIS_RATIO(集群数据不一致比例)”：集群数据不一致比例。当取值为x时，表示当前节点核查数据的不一致数量超过扫描总数量的x%时，就会上报“ALM-82615” 容灾实例间数据不一致告警。<br>- “CLUSTER_INCONSIS_COUNT(集群数据不一致个数)”：集群数据不一致个数。当取值为x时，表示当前节点核查数据的不一致总数超过x时，就会上报“ALM-82615” 容灾实例间数据不一致告警。<br>- “FORCE_AGING_DURATION(强制老化时长)”：强制老化时长，强制老化长时间未更新且无法删除的所有数据。默认不开启，如果开启需要为数据老化时间阈值“AGING_TIME_THRESHOLD”的2倍。<br>- “INDEX_CHECK_PERIOD(索引核查周期)”：集群内主本和副本的核查周期。<br>- “TABLE_COMPRESSION_SWITCH(表压缩开关)”：是否开启表压缩。<br>- “BANDWIDTH_COMPRESSION_SWITCH(带宽压缩开关)”：是否开启带宽压缩。<br>- “NWAY_REP_PARTITION_SWITCH(nway副本分区分布开关)”：是否开启nway副本分区分布。<br>默认值：无 |

## 操作的配置对象

- [DB启动参数值（DBSTARTPARAS）](configobject/UNC/20.15.2/DBSTARTPARAS.md)

## 使用实例

查询当前普通集群的CSDB启动参数配置：

```
LST DBSTARTPARAS: CLUSTERTYPE=COMMON_CLUSTER;
RETCODE = 0  操作成功

操作结果如下：
--------------
集群类型  参数                 参数值      

普通集群  老化时间阈值         2100        
普通集群  对象老化扫描间隔     10000       
普通集群  强制老化时长         4294967295  
普通集群  索引核查周期         600         
普通集群  集群间核查周期       600         
普通集群  集群间老化时间阈值   1200        
普通集群  集群核查间隔         100         
普通集群  集群数据不一致比例   2           
普通集群  集群数据不一致个数   2000
普通集群  表压缩开关           0
普通集群  带宽压缩开关         0
普通集群  nway副本分区分布开关 0        
(结果个数 = 12)
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询DB启动参数值(LST-DBSTARTPARAS)_01330005.md`
