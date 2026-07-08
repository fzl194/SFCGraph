# 激活 WSFD-102601 LTE一键通基础功能 （适用于PGW-C/SGW-C）

- [操作场景](#ZH-CN_OPI_0000001339305629__1.3.1)
- [必备事项](#ZH-CN_OPI_0000001339305629__1.3.2)
- [操作步骤](#ZH-CN_OPI_0000001339305629__1.3.3)
- [任务示例](#ZH-CN_OPI_0000001339305629__1.3.4)

## [操作场景](#ZH-CN_OPI_0000001339305629)

本操作指导介绍在运行网络中激活 LTE一键通基础功能 特性的操作过程。

> **说明**
> 适用于SGW-C、PGW-C。

## [必备事项](#ZH-CN_OPI_0000001339305629)

前提条件

- 请仔细阅读[WSFD-102601 LTE一键通基础功能（适用于PGW-C/SGW-C）](特性概述_10980736.md)。

- 已完成加载License。

数据

无。

## [操作步骤](#ZH-CN_OPI_0000001339305629)

1. 进入 “MML命令行-UNC” 窗口。
2. 打开 LTE一键通基础功能 的License配置开关。
  [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)

## [任务示例](#ZH-CN_OPI_0000001339305629)

任务描述

激活 LTE一键通基础功能 特性。

脚本

// 进入 “MML命令行-UNC” 窗口。

//打开 LTE一键通基础功能 特性的License配置开关。

```
SET LICENSESWITCH: LICITEM="LKV3WNPLTE11", SWITCH=ENABLE;
```
