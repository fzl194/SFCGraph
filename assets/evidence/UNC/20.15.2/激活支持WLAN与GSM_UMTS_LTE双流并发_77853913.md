# 激活支持WLAN与GSM/UMTS/LTE双流并发

- [操作场景](#ZH-CN_OPI_0277853913__1.3.1)
- [必备事项](#ZH-CN_OPI_0277853913__1.3.2)
- [操作步骤](#ZH-CN_OPI_0277853913__1.3.3)
- [任务示例](#ZH-CN_OPI_0277853913__1.3.4)

## [操作场景](#ZH-CN_OPI_0277853913)

本操作指导介绍在运行网络中激活支持WLAN与GSM/UMTS/LTE双流并发特性的操作过程。

华为 UNC 支持标准定义的WLAN AN/GERAN/UTRAN/E-UTRAN无线网络接入，实现WLAN与GSM/UMTS/LTE网络用户同时接入 UNC 。

> **说明**
> 适用于SGW-C、PGW-C。

## [必备事项](#ZH-CN_OPI_0277853913)

前提条件

- 请仔细阅读[WSFD-201302 支持WLAN与GSM/UMTS/LTE双流并发特性概述](特性概述_76948719.md)。
- 完成加载License。

数据

该操作无需准备数据。

## [操作步骤](#ZH-CN_OPI_0277853913)

1. 进入 “MML命令行-UNC” 窗口。
2. 打开本特性的License配置开关。
  [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)

## [任务示例](#ZH-CN_OPI_0277853913)

任务描述

开启支持WLAN与GSM/UMTS/LTE双流并发功能。

脚本

//打开本特性的License配置开关。

```
SET LICENSESWITCH:LICITEM="LKV3WPWLAN11",SWITCH=ENABLE;
```
