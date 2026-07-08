# 查询容器资源信息（DSP CNTRESSTAT）

- [命令功能](#ZH-CN_MMLREF_0000001360785913__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001360785913__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001360785913__1.3.3)
- [使用实例](#ZH-CN_MMLREF_0000001360785913__1.3.4)
- [输出结果说明](#ZH-CN_MMLREF_0000001360785913__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0000001360785913)

该命令用于查询容器的资源信息。

> **说明**
> 无。

## [参数说明](#ZH-CN_MMLREF_0000001360785913)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DSPCNTSTAT_RES_NAME | 资源名称 | 可选必选说明：必选参数。<br>参数含义：用于指示系统当前查询的资源名称。<br>取值范围：<br>- cpu(CPU)<br>- memory(内存)<br>- net(网络)<br>- disk(磁盘)<br>默认值：无。<br>配置原则：无。 |
| DSPCNTTHD_RES_CPU | CPU阈值类型 | 可选必选说明：该参数在<br>“资源名称”<br>取值为<br>“cpu(CPU)”<br>时为必选参数。<br>参数含义：用于指示系统当前查询的CPU阈值类型。<br>取值范围：<br>- cpu_usage(cpu告警阈值)<br>- cpu_change(cpu突变阈值)<br>默认值：无。<br>配置原则：无。 |
| DSPCNTTHD_RES_DISK | DISK阈值类型 | 可选必选说明：该参数在<br>“资源名称”<br>取值为<br>“disk(磁盘)”<br>时为必选参数。<br>参数含义：用于指示系统当前查询的disk阈值类型。<br>取值范围：<br>- disk_usage(disk告警阈值)<br>- inode_usage(inode告警阈值)<br>默认值：无。<br>配置原则：无。 |
| DSPCNTSTAT_MEID | 网元ID | 可选必选说明：该参数在<br>“资源名称”<br>取值为<br>“memory(内存)”<br>时为必选参数，在<br>**“CPU阈值类型”**<br>取值为<br>“cpu_usage(cpu告警阈值)”<br>时为必选参数；或在<br>“资源名称”<br>取值为<br>“disk(磁盘)”<br>且在<br>“DISK阈值类型”<br>取值为<br>“disk_usage(disk告警阈值)”<br>或<br>“inode_usage(inode告警阈值)”<br>时为必选参数。<br>参数含义：当前需要查询的网元ID，即应用ID。<br>取值范围：整数类型，取值范围0~65535。<br>默认值：无。<br>配置原则：无。 |
| DSPCNTSTAT_QUERY_TYPE | 查询类型 | 可选必选说明：该参数在<br>“资源名称”<br>取值为<br>“memory(内存)”<br>时为可选参数，在<br>**“CPU阈值类型”**<br>取值为<br>“cpu_usage(cpu告警阈值)”<br>时为可选参数；或在<br>“资源名称”<br>取值为<br>“disk(磁盘)”<br>且在<br>“DISK阈值类型”<br>取值为<br>“disk_usage(disk告警阈值)”<br>或<br>“inode_usage(inode告警阈值)”<br>时为可选参数。<br>参数含义：用于指示系统当前的查询类型；若不输入，则表示查询所有。<br>取值范围：<br>- byContainerId(容器ID)<br>- byContainerType(容器类型)<br>- byNode(节点名称)<br>默认值：无。<br>配置原则：无。 |
| DSPCNTSTAT_CNT_ID | 容器ID | 可选必选说明：该参数在<br>“查询类型”<br>取值为<br>“byContainerId(容器ID)”<br>时为必选参数。<br>参数含义：用于指示系统按照容器ID查询资源信息。<br>取值范围：字符串类型，字符串长度范围为2~256个字符。<br>默认值：无。<br>配置原则：通过<br>[**DSP CNTINFO**](查询容器部署信息（DSP CNTINFO）_60666141.md)<br>命令查询容器ID。 |
| DSPCNTSTAT_CNT_TYPE | 容器类型 | 可选必选说明：该参数在<br>“查询类型”<br>取值为<br>“byContainerType(容器类型)”<br>时为必选参数。<br>参数含义：用于指示系统按照容器类型查询资源信息。<br>取值范围：字符串类型，字符串长度范围为2~256个字符。<br>默认值：无。<br>配置原则：通过<br>[**DSP CNTINFO**](查询容器部署信息（DSP CNTINFO）_60666141.md)<br>命令查询容器类型。 |
| DSPCNTSTAT_NODE_NAME | 节点名称 | 可选必选说明：该参数在<br>“查询类型”<br>取值为<br>“byNode(节点名称)”<br>时为必选参数。<br>参数含义：用于指示系统按照节点名称查询资源信息。<br>取值范围：字符串类型，字符串长度范围为2~256个字符。<br>默认值：无。<br>配置原则：通过<br>[**DSP CNTINFO**](查询容器部署信息（DSP CNTINFO）_60666141.md)<br>命令查询节点名称。 |
| DSPCNTSTAT_RES_NETSUBHEALTH | 网络亚健康资源检测 | 可选必选说明：该参数在<br>“资源名称”<br>取值为<br>“net(网络)”<br>时为必选参数。<br>参数含义：用于指示系统当前查询的网络亚健康信息。<br>取值范围：<br>- netsubhealth(网络亚健康)。<br>默认值：无。<br>配置原则：无。 |

## [使用实例](#ZH-CN_MMLREF_0000001360785913)

1. 根据节点名称查询容器CPU资源信息

```
%%DSP CNTRESSTAT: DSPCNTSTAT_RES_NAME=cpu, DSPCNTTHD_RES_CPU=cpu_usage, DSPCNTSTAT_MEID=0, DSPCNTSTAT_QUERY_TYPE=byNode, DSPCNTSTAT_NODE_NAME="x.x.x.x";%%
 RETCODE = 0  操作成功  
操作结果如下：
 -------------- 
网元ID  容器类型                  配额     使用量  使用率  告警开关  告警上报阈值(%)  告警清除阈值(%)  容器ID                                                                                                      
0       auditlog-software         80.00%   0.47%   0.59%   on        90.00%           85.00%           nodeName:x.x.x.x/podName:auditlog-55758468f6-nj4n2/containerType:auditlog-software
(结果个数 = 1)
---    END
```

2. 根据容器类型查询容器的内存资源信息

```
%%DSP CNTRESSTAT: DSPCNTSTAT_MEID=0, DSPCNTSTAT_RES_NAME=memory, DSPCNTSTAT_QUERY_TYPE=byContainerType, DSPCNTSTAT_CNT_TYPE="servicegovernance-soft";%%
RETCODE = 0  执行成功
网元ID  容器类型                配额   使用量  使用率  告警开关  告警上报阈值(%)  告警清除阈值(%)  容器ID                                                                                                  
0       servicegovernance-soft  1024M  397M    38.77%  on        80.00%           75.00%           nodeName:x.x.x.x/podName:servicegovernance-7f755f9f96-wcqmx/containerType:servicegovernance-soft  
0       servicegovernance-soft  1024M  388M    37.89%  on        80.00%           75.00%           nodeName:x.x.x.x/podName:servicegovernance-7f755f9f96-4dlkb/containerType:servicegovernance-soft  
(结果个数 = 2)
---    END
```

3. 查询CPU突变阈值信息

```
%%DSP CNTRESSTAT: DSPCNTSTAT_RES_NAME=cpu, DSPCNTTHD_RES_CPU=cpu_change;%% 
RETCODE = 0  操作成功  
操作结果如下：
 -------------- 
节点名称 开关  CPU突变阈值(%)  CPU突变检测间隔(s)    
x.x.x.x  ON    70              28                
x.x.x.x  ON    70              28                
x.x.x.x  ON    70              28                
x.x.x.x  ON    70              28                
x.x.x.x  ON    70              28                
x.x.x.x  ON    70              28                
(结果个数 = 6)  
---    END
```

4. 查询网络亚健康资源信息

```
%%DSP CNTRESSTAT: DSPCNTSTAT_RES_NAME=net, DSPCNTSTAT_RES_NETSUBHEALTH=netsubhealth;%%
RETCODE = 0  操作成功
操作结果如下：
--------------
节点名称       开关  单链路丢包率阈值 (%)  网络亚健康告警上报阈值 (%)  网络亚健康告警清除阈值 (%)  网络亚健康响应阈值 (ms)  
x.x.x.x        ON    2.0                    70                           30                           200                      
x.x.x.x        ON    2.0                    70                           30                           200                      
x.x.x.x        ON    2.0                    70                           30                           200                      
(结果个数 = 3)
---    END
```

5. 根据容器类型查询磁盘disk_usage的使用信息

```
%%DSP CNTRESSTAT: DSPCNTSTAT_RES_NAME=disk, DSPCNTTHD_RES_DISK=disk_usage, DSPCNTSTAT_MEID=0, DSPCNTSTAT_QUERY_TYPE=byContainerType, DSPCNTSTAT_CNT_TYPE="cspmtcenter-software";%%
RETCODE = 0  操作成功

操作结果如下：
--------------
网元ID  容器类型              分区  挂载目录  配额    使用量  使用率  告警开关  告警上报阈值(%)  告警清除阈值(%)  容器ID

0       cspmtcenter-software  shm   /dev/shm  64.00M  0.00M   0.00%   on        90.00%           85.00%           nodeName:x.x.x.x/podName:cspmtcenter-54584744cb-49rqx/containerType:cspmtcenter-software  
0       cspmtcenter-software  shm   /dev/shm  64.00M  0.00M   0.00%   on        90.00%           85.00%           nodeName:x.x.x.x/podName:cspmtcenter-54584744cb-2xgm6/containerType:cspmtcenter-software  
(结果个数 = 2)

---    END
```

6. 根据容器类型查询磁盘inode_usage的使用信息

```
%%DSP CNTRESSTAT: DSPCNTSTAT_RES_NAME=disk, DSPCNTTHD_RES_DISK=inode_usage, DSPCNTSTAT_MEID=0, DSPCNTSTAT_QUERY_TYPE=byContainerType, DSPCNTSTAT_CNT_TYPE="cspmtcenter-software";%%
RETCODE = 0  操作成功

操作结果如下：
--------------
网元ID  容器类型              分区  挂载目录  配额     使用量  使用率  告警开关  告警上报阈值(%)  告警清除阈值(%)  容器ID

0       cspmtcenter-software  shm   /dev/shm  5644008  1       0.00%   on        90.00%           85.00%           nodeName:x.x.x.x/podName:cspmtcenter-54584744cb-2xgm6/containerType:cspmtcenter-software  
0       cspmtcenter-software  shm   /dev/shm  5644008  1       0.00%   on        90.00%           85.00%           nodeName:x.x.x.x/podName:cspmtcenter-54584744cb-49rqx/containerType:cspmtcenter-software  
(结果个数 = 2)

---    END
```

## [输出结果说明](#ZH-CN_MMLREF_0000001360785913)

命令执行正常，会返回命令执行成功的提示信息。输出结果说明 [表1 输出项说明](#ZH-CN_MMLREF_0000001360785913__zh-cn_mmlref_0000001129703664_table721916042810) 所示。

命令执行失败则返回相应的错误，参见 [表2 错误码列表](#ZH-CN_MMLREF_0000001360785913__zh-cn_mmlref_0000001129703664_table1932420572464) ；命令执行异常，请联系技术支持处理。

*表1 输出项说明*

| 输出项名称 | 输出项解释 |
| --- | --- |
| 网元ID | 容器所在网元ID，即应用ID。 |
| 容器类型 | 容器的名称。 |
| 配额 | 容器资源使用限额。 |
| 使用量 | 容器资源使用总量。 |
| 使用率 | 容器资源使用率。 |
| 告警开关 | 容器资源阈值告警开关。<br>- on：表示超过阈值后上报告警。<br>- off：表示超过阈值后不上报告警。 |
| 告警上报阈值(%) | 容器资源上报告警阈值，显示方式为百分比。 |
| 告警清除阈值(%) | 容器资源清除告警阈值，显示方式为百分比。 |
| 容器ID | 容器的唯一标识ID。 |
| 节点名称 | 节点名称。 |
| 开关 | CPU突变检测开关。<br>- ON：表示开启CPU突变检测开关。<br>- OFF：表示不开启CPU突变检测开关。 |
| CPU突变阈值 | CPU突变检测阈值，显示方式为百分比。 |
| CPU突变检测间隔 | CPU突变检测间隔，显示方式为秒。 |
| 开关 | 网络亚健康告警上报开关。<br>- ON：表示网络亚健康告警上报开启。<br>- OFF：表示网络亚健康告警上报关闭。 |
| 单链路丢包率阈值 (%) | 单链路丢包阈值，显示方式为百分比。 |
| 网络亚健康告警上报阈值 (%) | 网络亚健康告警上报阈值，显示方式为百分比。 |
| 网络亚健康告警清除阈值 (%) | 网络亚健康告警清除阈值，显示方式为百分比。 |
| 网络亚健康响应阈值 (ms) | 网络亚健康响应阈值。 |
| 分区 | 磁盘检测的分区路径。 |
| 挂载目录 | 磁盘检测分区路径的挂载路径。 |

*表2 错误码列表*

| 错误码 | 消息解释 | 原因分析 | 处理建议 |
| --- | --- | --- | --- |
| 20002 | 查询mk失败 | ModuleKeeper服务故障或网络异常。 | 重试或联系华为技术支持处理。 |
| 20005 | 查询OpsAgent失败 | OpsAgent服务故障或网络异常。 | 重试或联系华为技术支持处理。 |
| 20024 | 查不到相应数据或不支持该查询条件 | 没有符合条件的查询结果。 | 修改查询条件后重试。 |
| 102200 | 此场景不支持 | 当前场景不支持此命令。 | 无。 |
