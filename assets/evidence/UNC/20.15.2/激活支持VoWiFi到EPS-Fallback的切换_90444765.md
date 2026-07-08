# 激活支持VoWiFi到EPS Fallback的切换

- [操作场景](#ZH-CN_OPI_0000002090444765__1.3.1)
- [对系统的影响](#ZH-CN_OPI_0000002090444765__1.3.2)
- [必备事项](#ZH-CN_OPI_0000002090444765__1.3.3)
- [操作步骤](#ZH-CN_OPI_0000002090444765__1.3.4)
- [任务示例](#ZH-CN_OPI_0000002090444765__1.3.5)

## [操作场景](#ZH-CN_OPI_0000002090444765)

本操作指导介绍在运行网络中激活VoWiFi到VoNR切换支持EPS Fallback特性的操作过程。

> **说明**
> 适用于SMF。

## [对系统的影响](#ZH-CN_OPI_0000002090444765)

该操作对系统正常运行没有影响。

## [必备事项](#ZH-CN_OPI_0000002090444765)

前提条件

请仔细阅读 [WSFD-201305 支持VoWiFi到EPS Fallback的切换特性概述](WSFD-201305 支持VoWiFi到EPS Fallback的切换特性概述_90523317.md) 。

数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| **[SET SMFFUNC](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/会话协议参数管理/会话管理拓展功能/5GC会话管理拓展功能/设置SMF扩展功能（SET SMFFUNC）_09653731.md)** | WLAN切换NG-RAN失败转EPS FallBack功能开关（WLANHONREPSFBSW） | Support | 本端规划 | 支持WLAN切换NG-RAN失败转EPS FallBack功能。 |

## [操作步骤](#ZH-CN_OPI_0000002090444765)

1. 进入 “MML命令行-UNC” 窗口。
2. 配置支持WLAN切换NG-RAN失败转EPS FallBack功能。
  **[SET SMFFUNC](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/会话协议参数管理/会话管理拓展功能/5GC会话管理拓展功能/设置SMF扩展功能（SET SMFFUNC）_09653731.md)**

## [任务示例](#ZH-CN_OPI_0000002090444765)

任务描述

按照网络规划，配置SMF支持VoWifi到VoNR切换流程中支持收到基站指定原因值后，提供发起EPS Fallback流程的能力，使UE能回落到4G网络通过VoLTE进行通话，最大化利用现有LTE网络的覆盖和业务质量等资源。

脚本

//配置支持WLAN切换NG-RAN失败转EPS FallBack功能。

```
SET SMFFUNC: WLANHONREPSFBSW=Support;
```
