# 激活eNodeB SON信息传送功能

- [操作场景](#ZH-CN_OPI_0166313820__1.3.1)
- [必备事项](#ZH-CN_OPI_0166313820__1.3.2)
- [操作步骤](#ZH-CN_OPI_0166313820__1.3.3)

## [操作场景](#ZH-CN_OPI_0166313820)

本操作指导介绍在运行网络中激活eNodeB SON信息传送功能特性的操作过程。

> **说明**
> 适用于MME。

本场景应用于eNodeB全部支持SON流程自动发现X2地址的组网。

如 [图1](#ZH-CN_OPI_0166313820__fig1) 所示，eNodeB2和eNodeB3连接于同一个MME即MME2；eNodeB1连接于独立的MME1。eNodeB1与eNodeB2，eNodeB2与eNodeB3之间互为相邻，之间通过X2接口传递切换和eNodeB状态信息。

**图1** SON组网图

<br>

![](激活eNodeB SON信息传送功能_66313820.assets/zh-cn_image_0166482119_2.png)

## [必备事项](#ZH-CN_OPI_0166313820)

前提条件

- 请仔细阅读[WSFD-104402 eNodeB SON信息传送功能特性概述](../特性概述_66292211.md)。
- 完成加载License。
- MME、eNodeB网元上首先完成基本业务的数据配置。S1–MME、S10接口的数据配置，按网络规划配置数据进行，具体请参见[配置到eNodeB的数据](../../../../../初始配置/UNC初始配置与调测/组网对接配置/配置AMF&MME&SGSN/配置MME/配置到eNodeB的数据_82626680.md)、[配置到MME的数据](../../../../../初始配置/UNC初始配置与调测/组网对接配置/配置AMF&MME&SGSN/配置MME/配置到MME的数据_82626684.md)，本文不再赘述。

数据

该操作无需准备数据。

## [操作步骤](#ZH-CN_OPI_0166313820)

1. 打开本特性的License配置开关。
  进入 “MML命令行-UNC” 窗口。
  [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
