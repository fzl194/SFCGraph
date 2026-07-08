# 激活 支持Category NB2接入 （S/PGW-C）

- [操作场景](#ZH-CN_OPI_0277673142__1.3.1)
- [必备事项](#ZH-CN_OPI_0277673142__1.3.2)
- [操作步骤](#ZH-CN_OPI_0277673142__1.3.3)
- [任务示例](#ZH-CN_OPI_0277673142__1.3.4)

## [操作场景](#ZH-CN_OPI_0277673142)

本操作指导介绍在运行网络中激活 支持Category NB2接入 特性的操作过程。

> **说明**
> SGW-C、PGW-C

## [必备事项](#ZH-CN_OPI_0277673142)

前提条件

- 请仔细阅读 [WSFD-215501 支持Category NB2接入特性概述（S/PGW-C）](特性概述_77673141.md) 。
- 完成加载License。

数据

该操作无需准备数据。

## [操作步骤](#ZH-CN_OPI_0277673142)

1. 进入 “MML命令行-UNC” 窗口。
2. 打开本特性的License配置开关。
  [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
3. 打开本特性的软参配置开关。
  [**SET SMFSOFTPARA**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/软件参数管理/设置SMF软参（SET SMFSOFTPARA）_09653002.md)

## [任务示例](#ZH-CN_OPI_0277673142)

任务描述

在 UNC 上配置 支持Category NB2接入 功能。

脚本

//打开本特性的License配置开关。

```
SET LICENSESWITCH:LICITEM="LKV3WSNBAC21",SWITCH=ENABLE;
```

//打开本特性的软参配置开关。

```
SET SMFSOFTPARA:DT=Bit,BITNUM=717,BITVALUE=1;
```
