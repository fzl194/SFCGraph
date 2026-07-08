# 激活支持Null-MSISDN（适用SMF/GGSN/SGW-C/PGW-C）

- [操作场景](#ZH-CN_OPI_0276486798__1.3.1)
- [必备事项](#ZH-CN_OPI_0276486798__1.3.2)
- [操作步骤](#ZH-CN_OPI_0276486798__1.3.3)
- [任务示例](#ZH-CN_OPI_0276486798__1.3.4)

## [操作场景](#ZH-CN_OPI_0276486798)

本操作指导介绍在运行网络中激活支持Null-MSISDN特性的操作过程。

支持Null-MSISDN特性是指 UNC 支持不携带MSISDN（Mobile Station International ISDN Number）的用户进行基本的移动性管理和会话管理业务，如附着、TAU/RAU、激活等。

> **说明**
> 适用于 GGSN、 SGW-C、PGW-C、SMF。

## [必备事项](#ZH-CN_OPI_0276486798)

前提条件

- 请仔细阅读[WSFD-106012 支持Null-MSISDN特性概述](WSFD-106012 支持Null-MSISDN特性概述_68358206.md)。
- 已完成加载License，对应的License项为“81202798 LKV3W9NUMD02 支持Null-MSISDN”。
- 移动网络中的相关网元（如GGSN/P-GW、HLR/HSS、CG等）打开Null MSISDN业务功能。

数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| [**SET APNACCESSCTRL**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/基于APN的接入属性控制/设置APN访问控制参数（SET APNACCESSCTRL）_09654434.md) | APN名称（APN） | apn-test | 已配置数据中获取 | 使能Null-MSISDN功能 |
| [**SET APNACCESSCTRL**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/基于APN的接入属性控制/设置APN访问控制参数（SET APNACCESSCTRL）_09654434.md) | 不携带MSISDN用户激活策略（NULLMSISDN） | ENABLE | 本端规划 | 使能Null-MSISDN功能 |

## [操作步骤](#ZH-CN_OPI_0276486798)

1. 以下命令在 “MML命令行-UNC” 窗口上执行。打开本特性的License配置开关。
  [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
2. 使能Null-MSISDN功能。
  > **说明**
  > 该命令对新接入用户生效，不影响已接入用户。
  [**SET APNACCESSCTRL**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/基于APN的接入属性控制/设置APN访问控制参数（SET APNACCESSCTRL）_09654434.md)

## [任务示例](#ZH-CN_OPI_0276486798)

任务描述

使能APN“apn-test”的Null-MSISDN功能。

脚本

//使能Null-MSISDN功能。

```
SET LICENSESWITCH:LICITEM="LKV3W9NUMD02",SWITCH=ENABLE;
```

```
SET APNACCESSCTRL:APN="apn-test",NULLMSISDN=ENABLE;
```
