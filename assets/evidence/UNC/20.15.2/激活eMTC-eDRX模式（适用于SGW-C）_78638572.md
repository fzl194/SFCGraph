# 激活 eMTC eDRX模式 （适用于SGW-C）

- [操作场景](#ZH-CN_OPI_0278638572__1.3.1)
- [必备事项](#ZH-CN_OPI_0278638572__1.3.2)
- [操作步骤](#ZH-CN_OPI_0278638572__1.3.3)
- [任务示例](#ZH-CN_OPI_0278638572__1.3.4)

## [操作场景](#ZH-CN_OPI_0278638572)

本操作指导介绍在运行网络中激活 eMTC eDRX模式 特性的操作过程。

> **说明**
> 适用于SGW-C。

## [必备事项](#ZH-CN_OPI_0278638572)

前提条件

- 请仔细阅读 [WSFD-216002 eMTC eDRX模式特性概述（适用于SGW-C）](特性概述_78638571.md) 。
- 已完成加载License。

数据

该操作无需准备数据。

## [操作步骤](#ZH-CN_OPI_0278638572)

1. 进入 “MML命令行-UNC” 窗口。
2. 打开本特性的License配置开关。
  [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)

## [任务示例](#ZH-CN_OPI_0278638572)

任务描述

在 UNC 上配置 eMTC eDRX模式 功能。

脚本

//打开本特性的License配置开关。

```
SET LICENSESWITCH:LICITEM="LKV3WMTDRX11",SWITCH=ENABLE;
```
