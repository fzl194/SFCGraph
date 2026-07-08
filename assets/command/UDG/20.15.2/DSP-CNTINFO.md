---
id: UDG@20.15.2@MMLCommand@DSP CNTINFO
type: MMLCommand
name: DSP CNTINFO（查询容器部署信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: CNTINFO
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 设备管理
- 容器管理
status: active
---

# DSP CNTINFO（查询容器部署信息）

## 功能

该命令用于查询系统中的容器部署信息。

> **说明**
> 无。

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CNTINFO_MEID | 网元ID | 可选必选说明：可选参数。<br>参数含义：当前需要查询的网元ID；若不输入，则表示查询所有。<br>取值范围：整数类型，取值范围0~65535。<br>默认值：无。<br>配置原则：无。 |
| CNTINFO_QUERY_TYPE | 查询类型 | 可选必选说明：可选参数。<br>参数含义：用于指示系统当前的查询类型；若不输入，则表示查询所有。<br>取值范围：<br>- byContainerType(容器类型)<br>- byNode(节点名称)<br>默认值：无。<br>配置原则：无。 |
| CNTINFO_CNT_TYPE | 容器类型 | 可选必选说明：该参数在<br>“查询类型”<br>取值为<br>“byContainerType(容器类型)”<br>时为必选参数。<br>参数含义：用于指示系统按照容器类型查询部署信息。<br>取值范围：字符串类型，字符串长度范围为2~256个字符。<br>默认值：无。<br>配置原则：通过<br>**[DSP CNTINFO](查询容器部署信息（DSP CNTINFO）_60666141.md)**<br>命令查询容器类型。 |
| CNTINFO_NODE_NAME | 节点名称 | 可选必选说明：该参数在<br>“查询类型”<br>取值为<br>“byNode(节点名称)”<br>时为必选参数。<br>参数含义：用于指示系统按照节点名称查询部署信息。<br>取值范围：字符串类型，字符串长度范围为2~256个字符。<br>默认值：无。<br>配置原则：通过<br>**[DSP CNTINFO](查询容器部署信息（DSP CNTINFO）_60666141.md)**<br>命令查询节点名称。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/CNTINFO]] · 容器部署信息（CNTINFO）

## 使用实例

1. 按照节点名称查询容器部署信息

```
%%DSP CNTINFO: CNTINFO_MEID=0, CNTINFO_QUERY_TYPE=byNode, CNTINFO_NODE_NAME="xxxx";%% 
RETCODE = 0  执行成功    
网元ID  容器类型              节点名称         Pod名称                           容器ID                                                                                  
0       cspopsagent-software  xxxx             cspopsagent-jtfnh                 nodeName:xxxx/podName:cspopsagent-jtfnh/containerType:cspopsagent-software   
0       NULL                  xxxx             cspagentmanager-74bcd589f4-czs72  nodeName:xxxx/podName:cspagentmanager-74bcd589f4-czs72/containerType:        
0       kafka-software        xxxx             kafka-30074789-1                  nodeName:xxxx/podName:kafka-30074789-1/containerType:kafka-software          
(结果个数 = 3)  
---    END 
```

2. 按照容器类型查询容器部署信息

```
%%DSP CNTINFO: CNTINFO_MEID=0, CNTINFO_QUERY_TYPE=byContainerType, CNTINFO_CNT_TYPE="cspopsagent-software";%% 
RETCODE = 0  执行成功      
网元ID    =  0 
容器类型  =  cspopsagent-software 
节点名称  =  xxxx  
Pod名称   =  cspopsagent-jtfnh   
容器ID    =  nodeName:xxxx/podName:cspopsagent-jtfnh/containerType:cspopsagent-software 
(结果个数 = 1)  
---    END 
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询容器部署信息（DSP-CNTINFO）_60666141.md`
