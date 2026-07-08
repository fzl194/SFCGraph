# 激活NB-IoT eDRX模式（SGW-C）

- [操作场景](#ZH-CN_OPI_0277194597__1.3.1)
- [必备事项](#ZH-CN_OPI_0277194597__1.3.2)
- [操作步骤](#ZH-CN_OPI_0277194597__1.3.3)
- [任务示例](#ZH-CN_OPI_0277194597__1.3.4)

## [操作场景](#ZH-CN_OPI_0277194597)

本操作指导介绍在运行网络中激活 NB-IoT eDRX模式 特性的操作过程。

> **说明**
> 适用于SGW-C。

## [必备事项](#ZH-CN_OPI_0277194597)

前提条件

- 请仔细阅读 [WSFD-215002 NB-IoT eDRX模式特性概述（SGW-C）](特性概述_77194596.md) 。
- 完成加载License。

数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| [**SET SMFGLBDLBUFTIME**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/会话协议参数管理/GTP会话协议参数管理/下行报文缓存时长/设置全局下行报文缓存时长（SET SMFGLBDLBUFTIME）_96805509.md) | NB-IoT用户下行数据缓存时长（NBIOTUSER） | 200 | 本端规划 | 全局的NB-IoT用户下行报文缓存时长。 |
| [**ADD SMFAPNDLBUFTIME**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/会话协议参数管理/GTP会话协议参数管理/下行报文缓存时长/增加APN的下行报文缓存时长配置（ADD SMFAPNDLBUFTIME）_96805378.md) | APN名称（APN） | test | 本端规划 | 指定APN下的NB-IoT用户下行报文缓存时长。 |
| [**ADD SMFAPNDLBUFTIME**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/会话协议参数管理/GTP会话协议参数管理/下行报文缓存时长/增加APN的下行报文缓存时长配置（ADD SMFAPNDLBUFTIME）_96805378.md) | NB-IoT用户下行报文缓存时长(秒)（NBIOTUSER） | 200 | 本端规划 | 指定APN下的NB-IoT用户下行报文缓存时长。 |
| **[SET PFCPCMPT](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/PFCP接口管理/PFCP接口兼容性/设置PFCP接口兼容性参数（SET PFCPCMPT）_96243192.md)** | 是否支持BAR信元（BAR） | SUPPORT（支持） | 全网规划 | 控制PFCP接口是否支持BAR（Buffering Action Rule）信元。 |

## [操作步骤](#ZH-CN_OPI_0277194597)

1. 进入 “MML命令行-UNC” 窗口。
2. 打开本特性的License配置开关。
  [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
3. **可选：**配置下行数据到达S-GW时，全局的NB-IoT用户下行报文缓存时长。
  [**SET SMFGLBDLBUFTIME**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/会话协议参数管理/GTP会话协议参数管理/下行报文缓存时长/设置全局下行报文缓存时长（SET SMFGLBDLBUFTIME）_96805509.md)
4. 配置下行数据到达S-GW时，指定APN下的NB-IoT用户下行报文缓存时长。
  [**ADD SMFAPNDLBUFTIME**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/会话协议参数管理/GTP会话协议参数管理/下行报文缓存时长/增加APN的下行报文缓存时长配置（ADD SMFAPNDLBUFTIME）_96805378.md)
5. 配置下行数据到达S-GW时，PFCP接口支持BAR（Buffering Action Rule）信元。
  **[**SET PFCPCMPT**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/PFCP接口管理/PFCP接口兼容性/设置PFCP接口兼容性参数（SET PFCPCMPT）_96243192.md)**

## [任务示例](#ZH-CN_OPI_0277194597)

任务描述

在 UNC 上配置 NB-IoT eDRX模式 功能。

脚本

//打开本特性的License配置开关。

```
SET LICENSESWITCH:LICITEM="LKV3WNBDRX11",SWITCH=ENABLE;
```

//配置下行数据到达S-GW时，S-GW缓存报文的缓存时长。

```
SET SMFGLBDLBUFTIME: NBIOTUSER=200;
ADD SMFAPNDLBUFTIME: APN="test", NBIOTUSER=200;
```

//配置下行数据到达S-GW时，PFCP接口支持BAR（Buffering Action Rule）信元。

```
SET PFCPCMPT:BAR=SUPPORT;
```
