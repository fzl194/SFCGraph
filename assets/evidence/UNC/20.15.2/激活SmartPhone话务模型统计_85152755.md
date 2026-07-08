# 激活SmartPhone话务模型统计

- [操作场景](#ZH-CN_OPI_0185152755__1.3.1)
- [必备事项](#ZH-CN_OPI_0185152755__1.3.2)
- [操作步骤](#ZH-CN_OPI_0185152755__1.3.3)
- [任务示例](#ZH-CN_OPI_0185152755__1.3.4)

## [操作场景](#ZH-CN_OPI_0185152755)

本操作指导介绍在运行网络中激活Smartphone话务模型统计功能的操作过程。

Smartphone话务模型统计是指SGSN和网络优化工具协同工作，分析网络中Smartphone话务模型，从而进行准确的网络评估和规划的功能。

> **说明**
> 适用于 SGSN 。

## [必备事项](#ZH-CN_OPI_0185152755)

前提条件

- 请仔细阅读[WSFD-206007 Smartphone话务模型统计特性概述](特性概述_87065739.md)。
- 完成加载License。

数据

| 类别 | **参数名称** | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| [**ADD IMEILIB**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/Smartphone管理/终端类型识别/IMEI库管理/增加IMEI库记录（ADD IMEILIB）_26145734.md) | 设备型号核准号码（IMEITAC） | 46001111 | 本端规划 | 配置IMEI库。 |
| [**ADD IMEILIB**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/Smartphone管理/终端类型识别/IMEI库管理/增加IMEI库记录（ADD IMEILIB）_26145734.md) | 终端类型（UETYPE） | BLACKBERRY | 本端规划 | 配置IMEI库。 |
| [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md) | License项（LICITEM） | LKV2SPCB02 | 全网规划 | 打开Smartphone控制功能的License开关。 |
| [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md) | 开关（SWITCH） | ENABLE | 全网规划 | 打开Smartphone控制功能的License开关。 |

## [操作步骤](#ZH-CN_OPI_0185152755)

1. 进入 “MML命令行-UNC” 窗口。
2. 配置识别终端类型的数据库。
    - 可选：配置IMEI库。
      [**ADD IMEILIB**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/Smartphone管理/终端类型识别/IMEI库管理/增加IMEI库记录（ADD IMEILIB）_26145734.md)
    - 可选：配置APN NI库。
      [**ADD APNNILIB**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/Smartphone管理/终端类型识别/APNNI库管理/增加APNNI库记录（ADD APNNILIB）_26145736.md)
  > **说明**
  > IMEI库和APN NI库两者可以同时配置，优先级从高到低依次为：签约APN，IMEI，请求APN。
3. 打开本特性的License配置开关。
  [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)

## [任务示例](#ZH-CN_OPI_0185152755)

任务描述

激活对黑莓手机的话务模型统计功能。

> **说明**
> 以下脚本中设置IMEI号码为46001111的手机为黑莓手机，此设置仅为举例，现场配置时请根据实际情况选择参数值配置。

脚本

//配置IMEI库。

```
ADD IMEILIB: IMEITAC="46001111", UETYPE=BLACKBERRY;
```

//打开License配置开关。

```
SET LICENSESWITCH: LICITEM="LKV2SPTM02", SWITCH=ENABLE;
```
