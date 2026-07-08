# 激活 基于VoLTE的优先语音服务 （适用于SGW-C/PGW-C）

- [操作场景](#ZH-CN_OPI_0251416105__1.3.1)
- [必备事项](#ZH-CN_OPI_0251416105__1.3.2)
- [操作步骤](#ZH-CN_OPI_0251416105__1.3.3)
- [任务示例](#ZH-CN_OPI_0251416105__1.3.4)

## [操作场景](#ZH-CN_OPI_0251416105)

在 UNC 上激活基于VoLTE的优先语音服务，支持异常情况下的通话场景。

> **说明**
> 适用于SGW-C、PGW-C。

## [必备事项](#ZH-CN_OPI_0251416105)

前提条件

- 已经加载支持该特性的License。
- 请仔细阅读[WSFD-102004 基于VoLTE的优先语音服务特性概述](特性概述_70010134.md)。
- 完成[激活IMS功能](../WSFD-201103 IMS功能/激活IMS功能_91473678.md)。

数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| [**SET DDNATTR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/DDN消息携带的属性/设置DDN消息参数以及Delay信元处理开关（SET DDNATTR）_09651485.md) | 携带ARP（ARP） | Enable | 全网规划 | 控制SGW-C/PGW-C在Downlink Data Notification消息中是否携带ARP信元。 |
| [**SET DDNATTR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/DDN消息携带的属性/设置DDN消息参数以及Delay信元处理开关（SET DDNATTR）_09651485.md) | ARP值（ARPVALUE） | TriDDNBearer | 本端规划 | 控制SGW-C/PGW-C在Downlink Data Notification消息中是否携带ARP信元。 |
| [**SET DDNATTR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/DDN消息携带的属性/设置DDN消息参数以及Delay信元处理开关（SET DDNATTR）_09651485.md) | 携带EBI（EBI） | Enable | 本端规划 | 控制SGW-C/PGW-C在Downlink Data Notification消息中是否携带EBI信元。 |
| [**SET DDNATTR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/DDN消息携带的属性/设置DDN消息参数以及Delay信元处理开关（SET DDNATTR）_09651485.md) | EBI值（EBIVALUE） | TriDDNBearer | 本端规划 | 控制SGW-C/PGW-C在Downlink Data Notification消息中是否携带EBI信元。 |
| [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md) | APN名称（APN） | ims | 已配置数据中获取 | - |
| [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md) | Ppd功能开关（PPDSWITCH） | ENABLE | 本端规划 | - |

## [操作步骤](#ZH-CN_OPI_0251416105)

1. 进入 “MML命令行-UNC” 窗口。
2. 配置ARP参数。
  [**SET DDNATTR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/DDN消息携带的属性/设置DDN消息参数以及Delay信元处理开关（SET DDNATTR）_09651485.md)
3. 打开PPD功能开关。
  [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)

## [任务示例](#ZH-CN_OPI_0251416105)

任务描述

激活基于VoLTE的优先语音服务。

脚本

// 进入 “MML命令行-UNC” 窗口。

//配置ARP参数。

```
SET DDNATTR: EBI=Enable, EBIVALUE=TriDDNBearer, ARP=Enable, ARPVALUE=TriDDNBearer;
```

//打开PPD功能开关。

```
ADD APN:APN="ims",PPDSWITCH=ENABLE;
```
