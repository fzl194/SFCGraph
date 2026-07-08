# 设置DB启动参数值(SET DBSTARTPARAS)

- [命令功能](#ZH-CN_TOPIC_0000001451449964__1.3.1.1)
- [注意事项](#ZH-CN_TOPIC_0000001451449964__1.3.2.1)
- [操作用户权限](#ZH-CN_TOPIC_0000001451449964__1.3.3.1)
- [参数说明](#ZH-CN_TOPIC_0000001451449964__1.3.4.1)
- [使用实例](#ZH-CN_TOPIC_0000001451449964__1.3.5.1)

#### [命令功能](#ZH-CN_TOPIC_0000001451449964)

![](设置DB启动参数值(SET DBSTARTPARAS)_51449964.assets/notice_3.0-zh-cn_2.png)

该操作将修改 CSDB启动参数 ，会影响 CSDB 的运行。如需修改启动参数， 请联系华为技术支持。

该命令用于设置单个集群范围内的CSDB启动参数。主要参数包括容灾核查周期、核查定时器触发周期、不一致告警条件、对象强制老化等。

#### [注意事项](#ZH-CN_TOPIC_0000001451449964)

- 该命令执行后30秒内生效。
- 该命令存在系统初始记录，参数的初始设置值如下表：
  | 集群类型 | 参数 | 参数值 |
  | --- | --- | --- |
  | 普通集群 | 老化时间阈值 | 2100 |
  | 普通集群 | 对象老化扫描间隔 | 1200 |
  | 普通集群 | 强制老化时长 | 4294967295 |
  | 普通集群 | 索引核查周期 | 600 |
  | 普通集群 | 集群间核查周期 | 600 |
  | 普通集群 | 集群间老化时间阈值 | 1200 |
  | 普通集群 | 集群核查间隔 | 100 |
  | 普通集群 | 集群数据不一致比例 | 2 |
  | 普通集群 | 集群数据不一致个数 | 2000 |
  | 普通集群 | 表压缩开关 | 0 |
  | 普通集群 | 带宽压缩开关 | 0 |
  | 普通集群 | nway副本分区分布开关 | 0 |
  | XSF集群 | 老化时间阈值 | 2100 |
  | XSF集群 | 对象老化扫描间隔 | 1200 |
  | XSF集群 | 强制老化时长 | 4294967295 |
  | XSF集群 | 索引核查周期 | 600 |
  | XSF集群 | 集群间核查周期 | 600 |
  | XSF集群 | 集群间老化时间阈值 | 1200 |
  | XSF集群 | 集群核查间隔 | 100 |
  | XSF集群 | 集群数据不一致比例 | 2 |
  | XSF集群 | 集群数据不一致个数 | 2000 |
  | XSF集群 | 表压缩开关 | 0 |
  | XSF集群 | 带宽压缩开关 | 0 |
  | XSF集群 | nway副本分区分布开关 | 0 |

#### [操作用户权限](#ZH-CN_TOPIC_0000001451449964)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_TOPIC_0000001451449964)

| **参数标识** | **参数名称** | **参数说明** |
| --- | --- | --- |
| CLUSTERTYPE | 集群类型 | 可选必选说明：必选参数<br>参数含义: 该参数用于指定集群类型，分为普通集群和XSF集群。<br>数据来源：本端规划<br>取值范围：<br>- “COMMON_CLUSTER”：普通集群<br>- “XSF_CLUSTER”：XSF集群<br>默认值：无。 |
| PARA | 参数 | 可选必选说明：必选参数<br>参数含义：该参数用于指定需要设置的CSDB启动参数。<br>数据来源：本端规划<br>取值范围：<br>- “AGING_SCAN_INTERVAL(对象老化扫描间隔)”：数据老化扫描的时间间隔。<br>- “AGING_TIME_THRESHOLD(老化时间阈值)”：数据老化时间阈值。如果数据在设定时间内没有更新，则会被推送至对应的订阅者。<br>- “CLUSTER_AGING_THRESHOLD(集群间老化时间阈值)”：集群间老化时间阈值。老化阈值需要大于集群间核查周期“CLUSTER_CHECK_PERIOD”，否则未核查到的数据会被当成老化数据删除。一般大于2个周期。<br>- “CLUSTER_CHECK_INTERVAL(集群核查间隔)”：集群间核查间隔。<br>- “CLUSTER_CHECK_PERIOD(集群间核查周期)”：集群间核查周期，1个周期包括多个间隔。<br>- “CLUSTER_INCONSIS_RATIO(集群数据不一致比例)”：集群数据不一致比例。当取值为x时，表示当前节点核查数据的不一致数量超过扫描总数量的x%时，就会上报“ALM-82615” 容灾实例间数据不一致告警。<br>- “CLUSTER_INCONSIS_COUNT(集群数据不一致个数)”：集群数据不一致个数。当取值为x时，表示当前节点核查数据的不一致总数超过x时，就会上报“ALM-82615” 容灾实例间数据不一致告警。<br>- “FORCE_AGING_DURATION(强制老化时长)”：强制老化时长，强制老化长时间未更新且无法删除的所有数据。默认不开启，如果开启需要为数据老化时间阈值“AGING_TIME_THRESHOLD”的2倍。<br>- “INDEX_CHECK_PERIOD(索引核查周期)”：集群内主本和副本的核查周期。<br>- “TABLE_COMPRESSION_SWITCH(表压缩开关)”：是否开启表压缩。<br>- “BANDWIDTH_COMPRESSION_SWITCH(带宽压缩开关)”：是否开启带宽压缩。<br>- “NWAY_REP_PARTITION_SWITCH(nway副本分区分布开关)”：是否开启nway副本分区分布。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过相关查询命令获取当前参数配置值。 |
| PARAVALUE | 参数值 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定CSDB启动参数的取值。<br>数据来源：本端规划<br>取值范围：<br>- “AGING_SCAN_INTERVAL”：1200~864000和0，0表示关闭该功能。单位：秒。<br>- “AGING_TIME_THRESHOLD”：2100~31536000，单位：秒。<br>- “CLUSTER_AGING_THRESHOLD”：1200~31536000，单位：秒。<br>- “CLUSTER_CHECK_INTERVAL”：100~100000，单位：毫秒。<br>- “CLUSTER_CHECK_PERIOD”：600~86400，单位：秒。<br>- “CLUSTER_INCONSIS_RATIO”：1~100， 单位：%。<br>- “CLUSTER_INCONSIS_COUNT”：1~2147483647，单位：个。<br>- “FORCE_AGING_DURATION”：4200~4294967295，4294967295表示关闭该功能。单位：秒。<br>- “INDEX_CHECK_PERIOD”：600~86400，单位：秒。<br>- “TABLE_COMPRESSION_SWITCH”：0~2，0表示默认值，默认开启该功能，1表示开启该功能，2表示关闭该功能。<br>- “BANDWIDTH_COMPRESSION_SWITCH”：0~3，0表示默认值，根据环境变量判断是否开启压缩功能，1表示使用lz4压缩算法压缩，2表示使用zstd压缩算法压缩，3表示关闭该功能。<br>- “NWAY_REP_PARTITION_SWITCH”：0~2，0表示默认值，默认开启该功能，1表示开启该功能，2表示关闭该功能。<br>默认值：<br>- “AGING_SCAN_INTERVAL”：1200<br>- “AGING_TIME_THRESHOLD”：2100<br>- “CLUSTER_AGING_THRESHOLD”：1200<br>- “CLUSTER_CHECK_INTERVAL”：100<br>- “CLUSTER_CHECK_PERIOD”：600<br>- “CLUSTER_INCONSIS_RATIO”：2<br>- “CLUSTER_INCONSIS_COUNT”：2000<br>- “FORCE_AGING_DURATION”：4294967295<br>- “INDEX_CHECK_PERIOD”：600<br>- “TABLE_COMPRESSION_SWITCH”：0<br>- “BANDWIDTH_COMPRESSION_SWITCH”：0<br>- “NWAY_REP_PARTITION_SWITCH”：0 |

#### [使用实例](#ZH-CN_TOPIC_0000001451449964)

设置普通集群的数据老化时间阈值为21205：

```
SET DBSTARTPARAS: CLUSTERTYPE=COMMON_CLUSTER, PARA=AGING_TIME_THRESHOLD, PARAVALUE="21205";
```
