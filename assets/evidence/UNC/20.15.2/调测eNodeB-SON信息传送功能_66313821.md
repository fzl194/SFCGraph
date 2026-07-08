# 调测eNodeB SON信息传送功能

- [操作场景](#ZH-CN_OPI_0166313821__1.3.1)
- [必备事项](#ZH-CN_OPI_0166313821__1.3.2)
- [操作步骤](#ZH-CN_OPI_0166313821__1.3.3)

## [操作场景](#ZH-CN_OPI_0166313821)

当运营商部署eNodeB SON信息传送功能时，需对UNC的eNodeB SON信息传送功能进行调测，确保本功能可以正常使用。

> **说明**
> 适用于MME。

## [必备事项](#ZH-CN_OPI_0166313821)

前提条件

- 请仔细阅读[WSFD-104402 eNodeB SON信息传送功能特性概述](../特性概述_66292211.md)。
- 完成[激活eNodeB SON信息传送功能](../激活信息传送功能/激活eNodeB SON信息传送功能_66313820.md)。

数据

该操作无需准备数据。

工具

测试终端

## [操作步骤](#ZH-CN_OPI_0166313821)

1. 进入 “MML命令行-UNC” 窗口。
2. 执行 [**LST LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md) 命令查询License配置开关是否已打开。
    - 如果“SWITCH”为“ENABLE”，请执行[3](#ZH-CN_OPI_0166313821__cmd19480755172748)。
    - 如果“SWITCH”为“DISABLE”，请执行[**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)命令打开本特性对应的License配置开关。
3. Intra MME场景：
    a. 确认eNodeB2、eNodeB3配置在MME2下（使用[**DSP S1APLNK**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/S1接口管理/S1AP链路/显示S1AP连接状态(DSP S1APLNK)_26146252.md)命令确认），并且未配置X2接口；在MME2上打开eNodeB2、eNodeB3的接口跟踪。
    b. 无线侧触发eNodeB2进行X2地址学习流程。
    c. 观察MME2上eNodeB2的接口跟踪出现eNB Configuration Transfer消息，以及消息中的Target eNodeB ID是否标示为eNodeB3。
    d. 观察MME2上eNodeB3的接口跟踪出现MME Configuration Transfer消息，其中的SON Configuration Transfer信元与之前eNB Configuration Transfer消息中的信元一致。
4. Inter MME场景：
    a. 确认eNodeB1配置在MME1下，eNodeB2配置在MME2下（使用[**DSP S1APLNK**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/S1接口管理/S1AP链路/显示S1AP连接状态(DSP S1APLNK)_26146252.md)命令确认），并且未配置X2接口；在MME1上打开eNodeB1，在MME2上打开eNodeB2的接口跟踪。
    b. 打开该S10接口的GTPC跟踪（在MME1或MME2上打开都可）。
    c. 无线侧触发eNodeB1进行X2地址学习流程。
    d. 观察MME1上eNodeB1的接口跟踪出现eNB Configuration Transfer消息，以及消息中的Target eNodeB ID是否标示为eNodeB2。
    e. 观察MME1与MME2的S10接口跟踪出现Configuration Transfer Tunnel消息，其中的Target ID信元是否与eNB Configuration Transfer消息中信元一致。
    f. 观察MME2上eNodeB2的接口跟踪上出现MME Configuration Transfer消息，其中的SON Configuration Transfer信元与之前eNB Configuration Transfer消息中的信元一致。
