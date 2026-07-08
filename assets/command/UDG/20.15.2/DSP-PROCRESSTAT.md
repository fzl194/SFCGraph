---
id: UDG@20.15.2@MMLCommand@DSP PROCRESSTAT
type: MMLCommand
name: DSP PROCRESSTAT（查询进程资源信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: PROCRESSTAT
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 设备管理
- 进程管理
status: active
---

# DSP PROCRESSTAT（查询进程资源信息）

## 功能

该命令用于查询进程的资源信息。

> **说明**
> 无。

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DSPPROCSTAT_MEID | 网元ID | 可选必选说明：必选参数。<br>参数含义：当前需要查询的网元ID，即应用ID。<br>取值范围：整数类型，取值范围0~65535。<br>默认值：无。<br>配置原则：无。 |
| DSPPROCSTAT_RES_NAME | 资源名称 | 可选必选说明：必选参数。<br>参数含义：用于指示系统当前查询的资源名称。<br>取值范围：<br>- cpu(CPU)<br>- memory(内存)<br>- thread(线程)<br>- fd(文件句柄)<br>默认值：无。<br>配置原则：当<br>“资源名称”<br>为<br>“memory(内存)”<br>时，该命令查询的内存信息不包含静态大页内存。 |
| DSPPROCSTAT_QUERY_TYPE | 查询类型 | 可选必选说明：可选参数。<br>参数含义：用于指示系统当前的查询类型；若不输入，则表示查询所有。<br>取值范围：<br>- byProcessID(进程ID)<br>- byProcessType(进程类型)<br>- byContainerType(容器类型)<br>- byNode(节点名称)<br>默认值：无。<br>配置原则：无。 |
| DSPPROCSTAT_PROC_ID | 进程ID | 可选必选说明：该参数在<br>“查询类型”<br>取值为<br>“byProcessID(进程ID)”<br>时为必选参数。<br>参数含义：用于指示系统按照进程ID查询资源信息。<br>取值范围：字符串类型，字符串长度范围为2~256个字符。<br>默认值：无。<br>配置原则：通过<br>**[DSP PROCINFO](查询进程部署信息（DSP PROCINFO）_08305928.md)**<br>命令查询进程ID。 |
| DSPPROCSTAT_PROC_TYPE | 进程类型 | 可选必选说明：该参数在<br>“查询类型”<br>取值为<br>“byProcessType(进程类型)”<br>时为必选参数。<br>参数含义：用于指示系统按照进程类型查询资源信息。<br>取值范围：字符串类型，字符串长度范围为2~256个字符。<br>默认值：无。<br>配置原则：通过<br>**[DSP PROCINFO](查询进程部署信息（DSP PROCINFO）_08305928.md)**<br>命令查询进程类型。 |
| DSPPROCSTAT_CNT_TYPE | 容器类型 | 可选必选说明：该参数在<br>“查询类型”<br>取值为<br>“byContainerType(容器类型)”<br>时为必选参数。<br>参数含义：用于指示系统按照容器类型查询资源信息。<br>取值范围：字符串类型，字符串长度范围为2~256个字符。<br>默认值：无。<br>配置原则：通过<br>**[DSP PROCINFO](查询进程部署信息（DSP PROCINFO）_08305928.md)**<br>命令查询容器类型。 |
| DSPPROCSTAT_NODE_NAME | 节点名称 | 可选必选说明：该参数在<br>“查询类型”<br>取值为<br>“byNode(节点名称)”<br>时为必选参数。<br>参数含义：用于指示系统按照节点名称查询资源信息。<br>取值范围：字符串类型，字符串长度范围为2~256个字符。<br>默认值：无。<br>配置原则：通过<br>**[DSP PROCINFO](查询进程部署信息（DSP PROCINFO）_08305928.md)**<br>命令查询节点名称。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/PROCRESSTAT]] · 进程资源信息（PROCRESSTAT）

## 使用实例

1. 根据资源名称查询所有进程的资源信息。
  ```
  %%DSP PROCRESSTAT: DSPPROCSTAT_MEID=0, DSPPROCSTAT_RES_NAME=cpu;%%
  RETCODE = 0  执行成功
  操作结果如下：
  --------------
  网元ID  进程类型      配额     使用量  使用率  告警开关  告警上报阈值(%)  告警清除阈值(%)  进程ID
  0       PatchMgr      200.00%  0.40%   0.20%    on       90.00%           85.00%           nodeName:x.x.x.x/podName:patchmgr-78cd4964bf-phr75/containerType:patchmgr-software****
  0       CSPMTCenter   200.00%  0.00%   0.00%    on       90.00%           85.00%           nodeName:x.x.x.x/podName:cspmtcenter-6ff5c59b6c-2qcqx/containerType:cspmtcenter****
  0       CSPNetConfGW  60.00%   0.20%   0.33%    on       90.00%           85.00%           nodeName:x.x.x.x/podName:cspnetconfgw-5b74fbfdf9-6hhxf/containerType:cspnetconf****
  0       CSPMTCenter   60.00%   0.20%   0.34%    on       90.00%           85.00%           nodeName:x.x.x.x/podName:cspmtcenter-6ff5c59b6c-6pfvn/containerType:cspmtcenter****
  0       CSPNetConfGW  150.00%  0.40%   0.27%    on       90.00%           85.00%           nodeName:x.x.x.x/podName:cspnetconfgw-5b74fbfdf9-vtz9z/containerType:cspnetconf****
  0       PatchMgr      150.00%  0.40%   0.27%    on       90.00%           85.00%           nodeName:x.x.x.x/podName:patchmgr-78cd4964bf-59kwj/containerType:patchmgr-softw****
  (结果个数 = 6)
  ---    END
  ```

2. 根据进程类型查询进程资源信息。
  ```
  %%DSP PROCRESSTAT: DSPPROCSTAT_MEID=0, DSPPROCSTAT_RES_NAME=cpu, DSPPROCSTAT_QUERY_TYPE=byProcessType, DSPPROCSTAT_PROC_TYPE="PatchMgr";%%
  RETCODE = 0  执行成功
  操作结果如下：
  --------------
  网元ID  进程类型       配额      使用量  使用率   告警开关  告警上报阈值(%)  告警清除阈值(%)  进程ID
  0       PatchMgr       200.00%   0.40%   0.20%    on        90.00%           85.00%           nodeName:x.x.x.x/podName:patchmgr-78cd4964bf-phr75/containerType:patchmgr-software/process:****   
  0       PatchMgr       150.00%   0.40%   0.27%    on        90.00%           85.00%           nodeName:x.x.x.x/podName:patchmgr-78cd4964bf-59kwj/containerType:patchmgr-software/process:****  
  (结果个数 = 2)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-PROCRESSTAT.md`
