# 激活支持Null-MSISDN（适用于SGSN/MME）

- [操作场景](#ZH-CN_OPI_0168358209__1.3.1)
- [必备事项](#ZH-CN_OPI_0168358209__1.3.2)
- [操作步骤](#ZH-CN_OPI_0168358209__1.3.3)
- [任务示例](#ZH-CN_OPI_0168358209__1.3.4)

## [操作场景](#ZH-CN_OPI_0168358209)

本操作指导介绍在运行网络中激活支持Null-MSISDN特性的操作过程。

支持Null-MSISDN特性是指 UNC 支持不携带MSISDN（Mobile Station International ISDN Number）的用户进行基本的移动性管理和会话管理业务，如附着、TAU/RAU、激活等。

> **说明**
> 适用于 SGSN、 MME。

## [必备事项](#ZH-CN_OPI_0168358209)

前提条件

- 请仔细阅读[WSFD-106012 支持Null-MSISDN特性概述](WSFD-106012 支持Null-MSISDN特性概述_68358206.md)。
- 已完成加载License，对应的License项为“82207024 LKV2NOISDN02 支持Null-MSISDN”。
- 移动网络中的相关网元（如GGSN/P-GW、HLR/HSS、CG等）打开Null MSISDN业务功能。

数据

该操作无需准备数据。

## [操作步骤](#ZH-CN_OPI_0168358209)

1. 打开本特性的License配置开关。
  进入 “MML命令行-UNC” 窗口。
  [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)

## [任务示例](#ZH-CN_OPI_0168358209)

任务描述

启用支持Null-MSISDN业务。

脚本

//打开License配置开关。

```
SET LICENSESWITCH: LICITEM="LKV2NOISDN02", SWITCH=ENABLE;
```
