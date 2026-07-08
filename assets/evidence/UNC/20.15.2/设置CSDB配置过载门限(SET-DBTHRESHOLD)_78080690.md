# 设置CSDB配置过载门限(SET DBTHRESHOLD)

- [命令功能](#ZH-CN_CONCEPT_0278080690__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0278080690__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0278080690__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0278080690__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0278080690__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0278080690)

![](设置CSDB配置过载门限(SET DBTHRESHOLD)_78080690.assets/notice_3.0-zh-cn_2.png)

该操作将修改CSDB的过载门限，会影响CSDB的运行。如需修改过载门限，请联系华为技术支持。

该命令用于设置CSDB门限参数，包括CPU过载门限、存储过载门限以及队列过载门限。

过载级别分3级，级别越高，过载控制越严格。

#### [注意事项](#ZH-CN_CONCEPT_0278080690)

- 同一个级别，上报门限要大于恢复门限。
- 级别高的门限要大于级别低的门限。
- 本命令的系统初始设置值已经比较科学，不建议操作员使用本命令。

#### [操作用户权限](#ZH-CN_CONCEPT_0278080690)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0278080690)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CLUSTERID | 子集群标识 | 可选必选说明：必选参数。<br>参数含义：该参数用于指定唯一一个子集群，可以通过<br>**[DSP DBCLUSTER](../集群管理/查询CSDB子集群信息（DSP DBCLUSTER）_29626985.md)**<br>命令查询获取。<br>数据来源：本端规划<br>取值范围：1～10。<br>默认值：无。 |
| THRESHOLDTYPE | 门限类型 | 可选必选说明：必选参数。<br>参数含义：该参数用于指定过载门限类型。<br>数据来源：本端规划<br>取值范围：<br>- “CPU_OVERLOAD_THRESHOLD”：CPU过载门限<br>- “STORE_OVERLOAD_THRESHOLD”：存储过载门限<br>- “QUEUE_OVERLOAD_THRESHOLD”：队列过载门限<br>默认值：无。 |
| L1UPP | 1级过载上门限 | 可选必选说明：条件必选参数。<br>参数含义：该参数用于指定1级过载上报门限。<br>数据来源：本端规划<br>前提条件：该参数在门限类型选择后生效。<br>取值范围：整数类型，取值范围为0～100，单位为%。<br>若选择<br>“CPU_OVERLOAD_THRESHOLD”<br>，则默认值为80；<br>若选择<br>“STORE_OVERLOAD_THRESHOLD”<br>，则默认值为80；<br>若选择<br>“QUEUE_OVERLOAD_THRESHOLD”<br>，则默认值为55。 |
| L1LOW | 1级过载下门限 | 可选必选说明：条件必选参数。<br>参数含义：该参数用于指定1级过载恢复门限。<br>数据来源：本端规划<br>前提条件：该参数在门限类型选择后生效。<br>取值范围：整数类型，取值范围为0～100，单位为%。<br>若选择<br>“CPU_OVERLOAD_THRESHOLD”<br>，则默认值为75；<br>若选择<br>“STORE_OVERLOAD_THRESHOLD”<br>，则默认值为70；<br>若选择<br>“QUEUE_OVERLOAD_THRESHOLD”<br>，则默认值为50。 |
| L2UPP | 2级过载上门限 | 可选必选说明：条件必选参数。<br>参数含义：该参数用于指定2级过载上报门限。<br>数据来源：本端规划<br>前提条件：该参数在门限类型选择后生效。<br>取值范围：整数类型，取值范围为0～100，单位为%。<br>若选择<br>“CPU_OVERLOAD_THRESHOLD”<br>，则默认值为85；<br>若选择<br>“STORE_OVERLOAD_THRESHOLD”<br>，则默认值为90；<br>若选择<br>“QUEUE_OVERLOAD_THRESHOLD”<br>，则默认值为60。 |
| L2LOW | 2级过载下门限 | 可选必选说明：条件必选参数。<br>参数含义：该参数用于指定2级过载恢复门限。<br>数据来源：本端规划<br>前提条件：该参数在门限类型选择后生效。<br>取值范围：整数类型，取值范围为0～100，单位为%。<br>若选择<br>“CPU_OVERLOAD_THRESHOLD”<br>，则默认值为80；<br>若选择<br>“STORE_OVERLOAD_THRESHOLD”<br>，则默认值为80；<br>若选择<br>“QUEUE_OVERLOAD_THRESHOLD”<br>，则默认值为55。 |
| L3UPP | 3级过载上门限 | 可选必选说明：条件必选参数。<br>参数含义：该参数用于指定3级过载上报门限。<br>数据来源：本端规划<br>前提条件：该参数在门限类型选择后生效。<br>取值范围：整数类型，取值范围为0～100，单位为%。<br>若选择<br>“CPU_OVERLOAD_THRESHOLD”<br>，则默认值为90；<br>若选择<br>“STORE_OVERLOAD_THRESHOLD”<br>，则默认值为95；<br>若选择<br>“QUEUE_OVERLOAD_THRESHOLD”<br>，则默认值为65。 |
| L3LOW | 3级过载下门限 | 可选必选说明：条件必选参数。<br>参数含义：该参数用于指定3级过载恢复门限。<br>数据来源：本端规划<br>前提条件：该参数在门限类型选择后生效。<br>取值范围：整数类型，取值范围为0～100，单位为%。<br>若选择<br>“CPU_OVERLOAD_THRESHOLD”<br>，则默认值为85；<br>若选择<br>“STORE_OVERLOAD_THRESHOLD”<br>，则默认值为90；<br>若选择<br>“QUEUE_OVERLOAD_THRESHOLD”<br>，则默认值为60。 |

#### [使用实例](#ZH-CN_CONCEPT_0278080690)

设置 “子集群标识” 为 “1” 的过载门限参数：

```
SET DBTHRESHOLD:CLUSTERID=1, THRESHOLDTYPE=CPU_OVERLOAD_THRESHOLD, L1LOW=75, L1UPP=80, L2LOW=80, L2UPP=85, L3LOW=85, L3UPP=90;
SET DBTHRESHOLD:CLUSTERID=1, THRESHOLDTYPE=STORE_OVERLOAD_THRESHOLD, L1LOW=70, L1UPP=80, L2LOW=80, L2UPP=90, L3LOW=90, L3UPP=95;
SET DBTHRESHOLD:CLUSTERID=1, THRESHOLDTYPE=QUEUE_OVERLOAD_THRESHOLD, L1LOW=50, L1UPP=55, L2LOW=55, L2UPP=60, L3LOW=60, L3UPP=65。
```
