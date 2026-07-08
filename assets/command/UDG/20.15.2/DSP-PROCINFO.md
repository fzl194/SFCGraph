---
id: UDG@20.15.2@MMLCommand@DSP PROCINFO
type: MMLCommand
name: DSP PROCINFO（查询进程部署信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: PROCINFO
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 设备管理
- 进程管理
status: active
---

# DSP PROCINFO（查询进程部署信息）

## 功能

该命令用于查询系统中的进程部署信息。

> **说明**
> 无。

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCINFO_MEID | 网元ID | 可选必选说明：可选参数。<br>参数含义：当前需要查询的网元ID；若不输入，则表示查询所有。<br>取值范围：整数类型，取值范围0~65535。<br>默认值：无。<br>配置原则：无。 |
| PROCINFO_QUERY_TYPE | 查询类型 | 可选必选说明：可选参数。<br>参数含义：用于指示系统当前的查询类型；若不输入，则表示查询所有。<br>取值范围：<br>- byProcessType(进程类型)<br>- byContainerType(容器类型)<br>- byNode(节点名称)<br>默认值：无。<br>配置原则：无。 |
| PROCINFO_PROC_TYPE | 进程类型 | 可选必选说明：该参数在<br>“查询类型”<br>取值为<br>“byProcessType(进程类型)”<br>时为必选参数。<br>参数含义：用于指示按照进程类型查询部署信息。<br>取值范围：字符串类型，字符串长度范围为2~256个字符。<br>默认值：无。<br>配置原则：可通过<br>**[DSP PROCINFO](查询进程部署信息（DSP PROCINFO）_08305928.md)**<br>命令查询进程类型。 |
| PROCINFO_CNT_TYPE | 容器类型 | 可选必选说明：该参数在<br>“查询类型”<br>取值为<br>“byContainerType(容器类型)”<br>时为必选参数。<br>参数含义：用于指示按照容器类型查询部署信息。<br>取值范围：字符串类型，字符串长度范围为2~256个字符。<br>默认值：无。<br>配置原则：可通过<br>**[DSP PROCINFO](查询进程部署信息（DSP PROCINFO）_08305928.md)**<br>命令查询容器类型。 |
| PROCINFO_NODE_NAME | 节点名称 | 可选必选说明：该参数在<br>“查询类型”<br>取值为<br>“byNode(节点名称)”<br>时为必选参数。<br>参数含义：用于指示按照节点名称查询部署信息。<br>取值范围：字符串类型，字符串长度范围为2~256个字符。<br>默认值：无。<br>配置原则：可通过<br>**[DSP PROCINFO](查询进程部署信息（DSP PROCINFO）_08305928.md)**<br>命令查询节点名称。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@PROCINFO]] · 进程部署信息（PROCINFO）

## 使用实例

1. 根据进程类型查询进程部署信息。
  ```
  %%DSP PROCINFO: PROCINFO_MEID=0, PROCINFO_QUERY_TYPE=byProcessType, PROCINFO_PROC_TYPE="CSPNetConfGW";%%
  RETCODE = 0  执行成功
  操作结果如下：
  -------------- 
  网元ID  进程类型      节点名称         Pod名称                          容器类型                进程编号   进程标识                           进程ID   
  0       CSPNetConfGW  172.16.0.1       cspnetconfgw-857ccfd9c5-cqqt7    cspnetconfgw-software   110        0_CSPNetConfGW_192.168.0.1_40333   nodeName:172.16.0.1/podName:cspnetconfgw-857ccfd9****
  0       CSPNetConfGW  172.16.0.2       cspnetconfgw-857ccfd9c5-pmmsk    cspnetconfgw-software   109        0_CSPNetConfGW_192.168.0.2_40293   nodeName:172.16.0.2/podName:cspnetconfgw-857ccfd9**** 
  (结果个数 = 2)  
  ---    END
  ```
2. 根据容器类型查询进程部署信息。
  ```
  %%DSP PROCINFO: PROCINFO_MEID=0, PROCINFO_QUERY_TYPE=byContainerType, PROCINFO_CNT_TYPE="cspnetconfgw-software";%% 
  RETCODE = 0  执行成功 
  操作结果如下：
  -------------- 
  网元ID  进程类型      节点名称         Pod名称                          容器类型                进程编号   进程标识                           进程ID
  0       CSPNetConfGW  172.16.0.1       cspnetconfgw-857ccfd9c5-cqqt7    cspnetconfgw-software   110        0_CSPNetConfGW_192.168.0.1_40333   nodeName:172.16.0.1/podName:cspnetconfgw-857ccfd9****
  0       CSPNetConfGW  172.16.0.2       cspnetconfgw-857ccfd9c5-pmmsk    cspnetconfgw-software   109        0_CSPNetConfGW_192.168.0.2_40293   nodeName:172.16.0.2/podName:cspnetconfgw-857ccfd9****
  (结果个数 = 2)  
  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-PROCINFO.md`
