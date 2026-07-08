# 激活基于UDM的VoNR语音故障恢复（适用于SMF）

- [操作场景](#ZH-CN_OPI_0000001111685436__1.3.1)
- [必备事项](#ZH-CN_OPI_0000001111685436__1.3.2)
- [操作步骤](#ZH-CN_OPI_0000001111685436__1.3.3)
- [任务示例](#ZH-CN_OPI_0000001111685436__1.3.4)

## [操作场景](#ZH-CN_OPI_0000001111685436)

本操作指导介绍在运行网络中激活基于UDM的VoNR语音故障恢复的操作过程。

> **说明**
> 适用于SMF。

## [必备事项](#ZH-CN_OPI_0000001111685436)

前提条件

- 请仔细阅读[WSFD-221002 基于UDM的VoNR语音故障恢复特性概述](WSFD-221002 基于UDM的VoNR语音故障恢复特性概述_11685434.md)。
- 已完成加载License“82200DHD LKV2UDMVTR01 基于UDM的VoNR语音故障恢复”。

数据

| 类别 | 参数 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| **[SET GLOBALIMS](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/IMS管理/IMS业务功能/全局IMS配置/设置全局IMS互通配置信息（SET GLOBALIMS）_09653684.md)** | UDMPCSCF（基于UDM的P-CSCF Restoration功能开关） | ENABLE | 本端规划 | 打开SMF支持基于UDM进行P-CSCF故障恢复的功能开关。 |
| **[SET GLOBALIMS](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/IMS管理/IMS业务功能/全局IMS配置/设置全局IMS互通配置信息（SET GLOBALIMS）_09653684.md)** | UDMPCSCFMODE（基于UDM的P-CSCF Restoration功能模式） | PCSCFADDRUPDATE | 本端规划 | 打开SMF支持基于UDM进行P-CSCF故障恢复的功能开关。 |

## [操作步骤](#ZH-CN_OPI_0000001111685436)

1. 进入 “MML命令行-UNC” 窗口。
2. 配置支持SMF基于UDM的VoNR语音故障恢复特性。
  **[SET GLOBALIMS](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/IMS管理/IMS业务功能/全局IMS配置/设置全局IMS互通配置信息（SET GLOBALIMS）_09653684.md)**

## [任务示例](#ZH-CN_OPI_0000001111685436)

任务描述

激活基于UDM的VoNR语音故障恢复特性。

脚本

// 进入 “MML命令行-UNC” 窗口。

//配置支持SMF基于UDM的VoNR语音故障恢复特性。

```
SET GLOBALIMS: UDMPCSCF=ENABLE,UDMPCSCFMODE=PCSCFADDRUPDATE;
```
