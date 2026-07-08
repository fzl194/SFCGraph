# 激活基于CSFB的Multi PLMN

- [操作场景](#ZH-CN_OPI_0164009927__1.3.1)
- [必备事项](#ZH-CN_OPI_0164009927__1.3.2)
- [操作步骤](#ZH-CN_OPI_0164009927__1.3.3)
- [任务示例](#ZH-CN_OPI_0164009927__1.3.4)

## [操作场景](#ZH-CN_OPI_0164009927)

本操作指导介绍在运行网络中激活基于CSFB的Multi PLMN的操作过程。

> **说明**
> 适用于MME。

## [必备事项](#ZH-CN_OPI_0164009927)

前提条件

已经加载支持该特性的License。

数据

该操作无需准备数据。

## [操作步骤](#ZH-CN_OPI_0164009927)

1. 进入 “MML命令行-UNC” 窗口。
2. 打开本特性的License配置开关。
  [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
3. 配置基于CSFB的Multi PLMN特性参数。
  **[ADD TAILAI](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/电路域联合业务/TAI与LAI对应关系/增加TAI与LAI对应关系(ADD TAILAI)_72345017.md)**

## [任务示例](#ZH-CN_OPI_0164009927)

任务描述

启用基于CSFB的Multi PLMN。

脚本

//打开License配置开关

```
SET LICENSESWITCH: LICITEM="LKV2CSFB04", SWITCH=ENABLE;
```

//配置基于CSFB的Multi PLMN特性参数。

```
ADD TAILAI: BGNTAI="308015101", SUBRANGE=IMSI_PREFIX, IMSIPRE="12345", LAI="308010002";
```
