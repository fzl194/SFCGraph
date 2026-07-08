# 激活IPv6承载上下文特性（SGSN/GGSN）

- [操作场景](#ZH-CN_OPI_0248043366__1.3.1)
- [必备事项](#ZH-CN_OPI_0248043366__1.3.2)
- [操作步骤](#ZH-CN_OPI_0248043366__1.3.3)
- [任务示例](#ZH-CN_OPI_0248043366__1.3.4)

## [操作场景](#ZH-CN_OPI_0248043366)

本操作指导介绍在运行网络中激活IPv6承载上下文的操作过程。

> **说明**
> 适用于SGSN、GGSN。

## [必备事项](#ZH-CN_OPI_0248043366)

前提条件

- 请仔细阅读[WSFD-104001 IPv6承载上下文特性概述（SGSN/GGSN）](特性概述_48043355.md)。
- 完成加载License。

数据

该操作无需准备数据。

## [操作步骤](#ZH-CN_OPI_0248043366)

1. 进入 “MML命令行-UNC” 窗口。
2. 打开IPv6承载上下文特性的License配置开关。
  [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)

## [任务示例](#ZH-CN_OPI_0248043366)

任务描述

启用IPv6承载上下文特性。

脚本

```
SET LICENSESWITCH: LICITEM="LKV2IPV601", SWITCH=ENABLE;
SET LICENSESWITCH: LICITEM="LKV2IPV6SM01", SWITCH=ENABLE;
```
