# 激活基于HeNB GW的HeNB接入

- [操作场景](#ZH-CN_OPI_0166313832__1.3.1)
- [必备事项](#ZH-CN_OPI_0166313832__1.3.2)
- [操作步骤](#ZH-CN_OPI_0166313832__1.3.3)
- [任务示例](#ZH-CN_OPI_0166313832__1.3.4)

## [操作场景](#ZH-CN_OPI_0166313832)

本操作指导介绍在运行网络中激活基于HeNB GW的HeNB接入的操作过程。

本特性支持HeNB通过HeNB GW接入MME，从而避免大规模HeNB与MME直连造成MME S1连接资源紧张。

> **说明**
> - HeNB（Home evolved NodeB，家庭演进基站）是指在一个局部的区域里（例如居民住宅、商业写字楼等）部署的小型基站，用来解决宏基站覆盖死角的问题。
> - 根据3GPP协议，eNodeB分为Macro eNodeB和HeNB，前者的网元ID为20 位，后者一般为28 位，但是有个别厂家的HeNB也使用20位长的ID。Macro eNodeB即通常所指的eNodeB，通常用于覆盖较大的范围，HeNB一般用于覆盖部分楼宇、地下场所等Macro eNodeB不容易覆盖到的区域。

> **说明**
> 适用于MME。

## [必备事项](#ZH-CN_OPI_0166313832)

前提条件

- 请仔细阅读[WSFD-205009 基于HeNB GW的HeNB接入特性概述](特性概述_66292247.md)。
- 完成加载License。

数据

该操作无需准备数据。

## [操作步骤](#ZH-CN_OPI_0166313832)

1. **可选：**打开支持对20bit长HeNB的TAI寻址开关。
  进入 “MML命令行-UNC” 窗口。
  [**SET MMFUNC**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/移动性管理/MM扩展功能管理/设置移动性管理扩展功能(SET MMFUNC)_26145512.md)
2. 打开本特性的License配置开关。
  [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)

## [任务示例](#ZH-CN_OPI_0166313832)

任务描述

启用基于HeNB GW的HeNB接入特性。

脚本

//打开支持对20bit长HeNB的TAI寻址开关。

```
SET MMFUNC: TAIFOR20BITHENB=YES;
```

//打开本特性的License配置开关。

```
SET LICENSESWITCH: LICITEM="LKV2SHNA01", SWITCH=ENABLE;
```
