# 激活 eMTC基于eNodeB覆盖等级的寻呼

- [操作场景](#ZH-CN_OPI_0277396885__1.3.1)
- [必备事项](#ZH-CN_OPI_0277396885__1.3.2)
- [操作步骤](#ZH-CN_OPI_0277396885__1.3.3)
- [任务示例](#ZH-CN_OPI_0277396885__1.3.4)

## [操作场景](#ZH-CN_OPI_0277396885)

本操作指导介绍在运行网络中激活 eMTC基于eNodeB覆盖等级的寻呼 的操作过程。

基于eNodeB覆盖等级的寻呼，指MME根据eNodeB上报的推荐寻呼的eNodeB进行寻呼优化，并在寻呼消息中将eNodeB上报的推荐寻呼的小区和小区覆盖等级通过寻呼辅助信息传给eNodeB，用以支持eNodeB覆盖等级的寻呼。

> **说明**
> 适用于MME。

## [必备事项](#ZH-CN_OPI_0277396885)

前提条件

- 请仔细阅读[WSFD-216102 eMTC基于eNodeB覆盖等级的寻呼特性概述](特性概述_75993415.md)。
- 已完成加载License。
- MME上已经部署[WSFD-206001 精准寻呼](../../流控功能/WSFD-206001 精准寻呼_64557971.md)特性，且[**ADD S1PAGINGRULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/S1接口管理/S1寻呼规则管理/增加S1寻呼规则(ADD S1PAGINGRULE)_26306058.md)的参数“ACTGRP”配置包含“NEIGH_ENODEB（邻接eNodeB）”。

数据

该操作无需准备数据。

## [操作步骤](#ZH-CN_OPI_0277396885)

1. 进入 “MML命令行-UNC” 窗口。
2. **可选：**配置 “eNodeB覆盖增强检查开关” 为 “打开” 。
  [**SET M2MCTRL**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/M2M管理/M2M控制参数/设置M2M控制参数(SET M2MCTRL)_72345369.md)
  > **说明**
  > 当 “eNodeB覆盖增强检查开关” 为 “打开” 时，MME只向支持覆盖增强寻呼的eNodeB下发携带寻呼辅助信息（Assistance Data for Paging）信元的寻呼请求。关于此参数的详细说明请参考 [**SET M2MCTRL**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/M2M管理/M2M控制参数/设置M2M控制参数(SET M2MCTRL)_72345369.md) 。
3. **可选：**配置 “Next Paging Area Scope开关” 为 “YES” 。
  [**SET S1CMPT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/S1接口管理/S1接口兼容性/设置S1接口兼容性(SET S1CMPT)_72345837.md)
4. 打开本功能的License配置开关。
  [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)

## [任务示例](#ZH-CN_OPI_0277396885)

任务描述

启用 eMTC基于eNodeB覆盖等级的寻呼 。

脚本

//配置eNodeB覆盖增强检查开关为打开。

```
SET M2MCTRL: CHK_ENB_CE_SW=ON;
```

//配置“Next Paging Area Scope开关”为 “YES” 。

```
SET S1CMPT: NPAS=YES;
```

//打开本特性的License配置开关。

```
SET LICENSESWITCH: LICITEM="LKV2CELP02", SWITCH=ENABLE;
```
