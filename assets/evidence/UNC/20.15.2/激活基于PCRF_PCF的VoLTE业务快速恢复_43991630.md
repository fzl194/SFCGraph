# 激活 基于PCRF/PCF的VoLTE业务快速恢复

- [操作场景](#ZH-CN_OPI_0000001143991630__1.3.1)
- [必备事项](#ZH-CN_OPI_0000001143991630__1.3.2)
- [操作步骤](#ZH-CN_OPI_0000001143991630__1.3.3)
- [任务示例](#ZH-CN_OPI_0000001143991630__1.3.4)

## [操作场景](#ZH-CN_OPI_0000001143991630)

在 UNC 上激活基于PCRF/PCF的VoLTE业务快速恢复功能，降低P-CSCF服务器故障时，对用户业务的影响。

> **说明**
> 适用于 PGW-C 。

## [必备事项](#ZH-CN_OPI_0000001143991630)

前提条件

- 请仔细阅读[WSFD-102203 基于PCRF/PCF的VoLTE业务快速恢复特性概述](特性概述_89991353.md)。
- 完成[激活P-CSCF故障时IMS业务恢复](../WSFD-102202 P-CSCF故障时IMS业务恢复/激活P-CSCF故障时IMS业务恢复_26216211.md)。
- 已完成加载License。

数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| **[SET APNREPORTATTR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/周边接口呈现APN策略管理/基于APN的上报APN策略控制/设置APN的上报属性（SET APNREPORTATTR）_33845578.md)** | APN名称（APN） | ims.real | 本端规划 | 将真实使用的APN与终端上报的APN配置映射关系。 |
| **[SET APNREPORTATTR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/周边接口呈现APN策略管理/基于APN的上报APN策略控制/设置APN的上报属性（SET APNREPORTATTR）_33845578.md)** | 上报给PCRF的APN名<br>（PCRF） | REQUESTED | 本端规划 | 将真实使用的APN与终端上报的APN配置映射关系。 |
| **[SET SMFSOFTPARAOFBIT](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/软件参数管理/设置SMF软件参数比特位（SET SMFSOFTPARAOFBIT）_09652696.md)** | DT（数据类型） | Dw | 本端规划 | 设置SMF软件参数比特位，配置PGW-C基于PCRF/PCF的P-CSCF故障恢复会重新激活会话。 |
| **[SET SMFSOFTPARAOFBIT](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/软件参数管理/设置SMF软件参数比特位（SET SMFSOFTPARAOFBIT）_09652696.md)** | DWORDNUM（Dword索引） | 1017 | 本端规划 | 设置SMF软件参数比特位，配置PGW-C基于PCRF/PCF的P-CSCF故障恢复会重新激活会话。 |
| **[SET SMFSOFTPARAOFBIT](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/软件参数管理/设置SMF软件参数比特位（SET SMFSOFTPARAOFBIT）_09652696.md)** | VALUE（软参记录值） | VALUE_1 | 本端规划 | 设置SMF软件参数比特位，配置PGW-C基于PCRF/PCF的P-CSCF故障恢复会重新激活会话。 |
| **[SET SMFSOFTPARAOFBIT](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/软件参数管理/设置SMF软件参数比特位（SET SMFSOFTPARAOFBIT）_09652696.md)** | POSITION（比特位） | 30 | 本端规划 | 设置SMF软件参数比特位，配置PGW-C基于PCRF/PCF的P-CSCF故障恢复会重新激活会话。 |

## [操作步骤](#ZH-CN_OPI_0000001143991630)

1. 进入 “MML命令行-UNC” 窗口。
2. 将真实使用的APN与终端上报的APN配置映射关系。
  **[SET APNREPORTATTR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/周边接口呈现APN策略管理/基于APN的上报APN策略控制/设置APN的上报属性（SET APNREPORTATTR）_33845578.md)**
3. 配置PGW-C基于PCRF/PCF的P-CSCF故障恢复会重新激活会话。
  **[SET SMFSOFTPARAOFBIT](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/软件参数管理/设置SMF软件参数比特位（SET SMFSOFTPARAOFBIT）_09652696.md)**

## [任务示例](#ZH-CN_OPI_0000001143991630)

任务描述

开启基于PCRF/PCF的VoLTE业务快速恢复功能开关。

脚本

// 进入 “MML命令行-UNC” 窗口。

//将真实使用的APN与终端上报的APN配置映射关系。 参数 APN使用 **[**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)** 命令配置生成。执行该命令前请先通过 **[**LST APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/查询APN配置（LST APN）_09652599.md)** 查询当前是否已添加该APN配置。 根据查询结果，选择是否配置该参数。

```
SET APNREPORTATTR: APN="ims.real", PCRF=REQUESTED;
```

//配置PGW-C基于PCRF/PCF的P-CSCF故障恢复会重新激活会话。

```
SET SMFSOFTPARAOFBIT: DT=Dw, DWORDNUM=1017, VALUE=VALUE_1, POSITION=30;
```
