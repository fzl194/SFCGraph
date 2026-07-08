# 激活 NB-IoT终端标准接入 （适用于S/PGW-C）

- [操作场景](#ZH-CN_OPI_0000001257752888__1.3.1)
- [必备事项](#ZH-CN_OPI_0000001257752888__1.3.2)
- [操作步骤](#ZH-CN_OPI_0000001257752888__1.3.3)
- [任务示例](#ZH-CN_OPI_0000001257752888__1.3.4)

## [操作场景](#ZH-CN_OPI_0000001257752888)

本操作指导介绍在运行网络中激活NB-IoT终端标准接入的操作过程。

> **说明**
> 适用于SGW-C、PGW-C。

## [必备事项](#ZH-CN_OPI_0000001257752888)

前提条件

- 请仔细阅读[WSFD-011601 NB-IoT终端标准接入特性概述（适用于S/PGW-C）](特性概述_76669507.md)。
- 完成[激活基于信令面的数据传输（SGW-C）](../../WSFD-215101 基于信令面的数据传输/WSFD-215101 基于信令面的数据传输（SGW-C）/激活基于信令面的数据传输（SGW-C）_77260996.md)。

数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md) | License项（LICITEM） | LKV3WPNBPS11 | 本端规划 | 用于配置License控制项开关。 |
| [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md) | 开关（SWITCH） | ENABLE | 本端规划 | 用于配置License控制项开关。 |

## [操作步骤](#ZH-CN_OPI_0000001257752888)

1. 进入 “MML命令行-UNC” 窗口。
2. 打开本特性的License配置开关。
  [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)

## [任务示例](#ZH-CN_OPI_0000001257752888)

任务描述

启用NB-IoT终端标准接入（S/PGW-C）特性，并配置用户为NB-IoT第一档用户。

脚本

//打开本特性的License配置开关。

```
SET LICENSESWITCH: LICITEM="LKV3WPNBPS11", SWITCH=ENABLE;
```

//配置用户为NB-IoT第一档用户。

```
SET LICENSESWITCH: LICITEM="LKV3WNBSL111", SWITCH=ENABLE;
```
