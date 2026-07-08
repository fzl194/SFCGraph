# 激活SRVCC特性（适用于SGW-C/PGW-C）

- [操作场景](#ZH-CN_OPI_0230364774__1.3.1)
- [必备事项](#ZH-CN_OPI_0230364774__1.3.2)
- [操作步骤](#ZH-CN_OPI_0230364774__1.3.3)
- [任务示例](#ZH-CN_OPI_0230364774__1.3.4)

## [操作场景](#ZH-CN_OPI_0230364774)

本操作指导介绍在运行网络中部署SGW-C/PGW-C的SRVCC功能。

## [必备事项](#ZH-CN_OPI_0230364774)

前提条件

- 已完成加载License。
- MME、MSC Server、eNodeB等网元基本业务的数据配置已完成。

数据

该操作无需准备数据。

## [操作步骤](#ZH-CN_OPI_0230364774)

1. 进入 “MML命令行-UNC” 窗口。
2. 打开License配置开关。
  [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)

## [任务示例](#ZH-CN_OPI_0230364774)

任务描述

使能SRVCC切换功能。

脚本

//打开本特性的License配置开关。

```
SET LICENSESWITCH:LICITEM="LKV3WPRVCC11",SWITCH=ENABLE;
```
