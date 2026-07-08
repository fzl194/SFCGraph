# 查询容器部署信息（DSP CNTINFO）

- [命令功能](#ZH-CN_MMLREF_0000001360666141__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001360666141__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001360666141__1.3.3)
- [使用实例](#ZH-CN_MMLREF_0000001360666141__1.3.4)
- [输出结果说明](#ZH-CN_MMLREF_0000001360666141__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0000001360666141)

该命令用于查询系统中的容器部署信息。

> **说明**
> 无。

## [参数说明](#ZH-CN_MMLREF_0000001360666141)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CNTINFO_MEID | 网元ID | 可选必选说明：可选参数。<br>参数含义：当前需要查询的网元ID；若不输入，则表示查询所有。<br>取值范围：整数类型，取值范围0~65535。<br>默认值：无。<br>配置原则：无。 |
| CNTINFO_QUERY_TYPE | 查询类型 | 可选必选说明：可选参数。<br>参数含义：用于指示系统当前的查询类型；若不输入，则表示查询所有。<br>取值范围：<br>- byContainerType(容器类型)<br>- byNode(节点名称)<br>默认值：无。<br>配置原则：无。 |
| CNTINFO_CNT_TYPE | 容器类型 | 可选必选说明：该参数在<br>“查询类型”<br>取值为<br>“byContainerType(容器类型)”<br>时为必选参数。<br>参数含义：用于指示系统按照容器类型查询部署信息。<br>取值范围：字符串类型，字符串长度范围为2~256个字符。<br>默认值：无。<br>配置原则：通过<br>**[DSP CNTINFO](查询容器部署信息（DSP CNTINFO）_60666141.md)**<br>命令查询容器类型。 |
| CNTINFO_NODE_NAME | 节点名称 | 可选必选说明：该参数在<br>“查询类型”<br>取值为<br>“byNode(节点名称)”<br>时为必选参数。<br>参数含义：用于指示系统按照节点名称查询部署信息。<br>取值范围：字符串类型，字符串长度范围为2~256个字符。<br>默认值：无。<br>配置原则：通过<br>**[DSP CNTINFO](查询容器部署信息（DSP CNTINFO）_60666141.md)**<br>命令查询节点名称。 |

## [使用实例](#ZH-CN_MMLREF_0000001360666141)

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

## [输出结果说明](#ZH-CN_MMLREF_0000001360666141)

命令执行正常，会返回命令执行成功的提示信息。输出结果说明 [表1 输出项说明](#ZH-CN_MMLREF_0000001360666141__zh-cn_mmlref_0000001129863460_table721916042810) 所示。

命令执行失败则返回相应的错误，参见 [表2 错误码列表](#ZH-CN_MMLREF_0000001360666141__zh-cn_mmlref_0000001129863460_table1362814278591) ；命令执行异常，请联系技术支持处理。

*表1 输出项说明*

| 输出项名称 | 输出项解释 |
| --- | --- |
| 网元ID | 容器所在网元ID，即应用ID |
| 容器类型 | 容器的类型 |
| 节点名称 | 容器所在的节点名称 |
| Pod名称 | 容器所在的Pod名称 |
| 容器ID | 容器的唯一标识ID |

*表2 错误码列表*

| 错误码 | 消息解释 | 原因分析 | 处理建议 |
| --- | --- | --- | --- |
| 20002 | 查询mk失败 | ModuleKeeper服务故障或网络异常。 | 重试或联系华为技术支持处理。 |
| 20024 | 查不到相应数据或不支持该查询条件 | 没有符合条件的查询结果。 | 修改查询条件后重试。 |
