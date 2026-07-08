# 激活基于UDM的VoNR语音故障恢复（适用于AMF）

- [操作场景](#ZH-CN_OPI_0228824215__1.3.1)
- [必备事项](#ZH-CN_OPI_0228824215__1.3.2)
- [操作步骤](#ZH-CN_OPI_0228824215__1.3.3)
- [任务示例](#ZH-CN_OPI_0228824215__1.3.4)

## [操作场景](#ZH-CN_OPI_0228824215)

本操作指导介绍在运行网络中激活基于UDM的VoNR语音故障恢复的操作过程。

> **说明**
> 适用于AMF。

## [必备事项](#ZH-CN_OPI_0228824215)

前提条件

- 请仔细阅读[WSFD-221002 基于UDM的VoNR语音故障恢复特性概述](WSFD-221002 基于UDM的VoNR语音故障恢复特性概述_11685434.md)。
- 已完成加载License“82200BNL LKV2FRPH02 基于HSS/UDM的P-CSCF故障恢复”。

数据

| 类别 | 参数 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| **[SET NGMMFUNC](../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/MM协议参数管理/5G移动性管理/设置5G移动性管理功能（SET NGMMFUNC）_09653748.md)** | UDMPCSCFRESTOR | YES | 全网规划 | 打开AMF支持基于UDM的VoNR语音故障恢复的功能开关。 |

## [操作步骤](#ZH-CN_OPI_0228824215)

1. 进入 “MML命令行-UNC” 窗口。
2. 配置支持基于UDM的VoNR语音故障恢复特性。
  **[SET NGMMFUNC](../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/MM协议参数管理/5G移动性管理/设置5G移动性管理功能（SET NGMMFUNC）_09653748.md)**
3. 打开本特性的License配置开关。
  [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)

## [任务示例](#ZH-CN_OPI_0228824215)

任务描述

激活基于UDM的VoNR语音故障恢复特性。

脚本

// 进入 “MML命令行-UNC” 窗口。

//配置支持AMF基于UDM的VoNR语音故障恢复特性。

```
SET NGMMFUNC: UDMPCSCFRESTOR=YES;
```

//打开License配置开关。

```
SET LICENSESWITCH: LICITEM="LKV2FRPH02", SWITCH=ENABLE;
```
