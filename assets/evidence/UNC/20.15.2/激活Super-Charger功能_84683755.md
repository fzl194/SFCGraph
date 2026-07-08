# 激活Super-Charger功能

- [操作场景](#ZH-CN_OPI_0184683755__1.3.1)
- [必备事项](#ZH-CN_OPI_0184683755__1.3.2)
- [操作步骤](#ZH-CN_OPI_0184683755__1.3.3)
- [任务示例](#ZH-CN_OPI_0184683755__1.3.4)

## [操作场景](#ZH-CN_OPI_0184683755)

本操作指导介绍在运行网络中激活Super-Charger功能的操作过程。

Super-Charger功能是一种用户漫游出SGSN或长时间分离后，SGSN仍然保留该用户的签约数据而不删除的一种机制。Super-Charger特性可以减少SGSN与HLR之间的信令交互。

> **说明**
> 适用于 SGSN 。

## [必备事项](#ZH-CN_OPI_0184683755)

前提条件

- 请仔细阅读[WSFD-106304 Super-Charger功能特性概述](特性概述_85454305.md)。
- 完成对端网元HLR激活Super-Charger功能。
- 完成加载License。

数据

| 类别 | 参数名 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md) | License项（LICITEM） | LKV2SUPCHG02 | 全网规划 | 打开本特性的License配置开关。 |
| [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md) | 开关（SWITCH） | ENABLE | 全网规划 | 打开本特性的License配置开关。 |
| [**SET SDCFG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/签约数据管理/签约数据信息/设置签约数据配置(SET SDCFG)_72225433.md) | Super-Charger功能（SC） | YES | 全网规划 | 开启Super-Charger功能开关。 |

## [操作步骤](#ZH-CN_OPI_0184683755)

1. 进入 “MML命令行-UNC” 窗口。
2. 打开本特性的License配置开关。
  [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
3. 开启Super-Charger功能开关。
  [**SET SDCFG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/签约数据管理/签约数据信息/设置签约数据配置(SET SDCFG)_72225433.md)
  > **说明**
  > 参数 “SC” （Super-Charger功能）选择 “YES” 。

## [任务示例](#ZH-CN_OPI_0184683755)

任务描述

激活Super-Charger功能。

脚本

//打开License配置开关。

```
SET LICENSESWITCH: LICITEM="LKV2SUPCHG02", SWITCH=ENABLE;
```

//开启Super-Charger功能开关。

```
SET SDCFG: SC=YES;
```
