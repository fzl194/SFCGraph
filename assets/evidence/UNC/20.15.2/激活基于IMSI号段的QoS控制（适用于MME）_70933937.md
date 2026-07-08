# 激活基于IMSI号段的QoS控制（适用于MME）

- [操作场景](#ZH-CN_OPI_0170933937__1.3.1)
- [对系统的影响](#ZH-CN_OPI_0170933937__1.3.2)
- [必备事项](#ZH-CN_OPI_0170933937__1.3.3)
- [操作步骤](#ZH-CN_OPI_0170933937__1.3.4)
- [任务示例](#ZH-CN_OPI_0170933937__1.3.5)

## [操作场景](#ZH-CN_OPI_0170933937)

本操作指导介绍在运行网络中激活基于IMSI号段的QoS控制特性的操作过程。

MME能够按IMSI号段对特定用户群的QoS进行单独配置，从而实现灵活的QoS控制策略。

当UE需要进行会话管理流程时，MME可以根据运营商基于用户群配置的QoS控制策略，改变用户签约的QoS。划分用户群的最大粒度为PLMN，最小粒度为特定IMSI，运营商可以根据自身的经营策略划分用户群，如：本网用户、漫游用户、指定PLMN用户、特定IMSI号段用户等。

> **说明**
> 适用于MME。

## [对系统的影响](#ZH-CN_OPI_0170933937)

该操作对系统正常运行无影响。

## [必备事项](#ZH-CN_OPI_0170933937)

前提条件

- 请仔细阅读[WSFD-105104 基于IMSI号段的QoS控制（适用于MME）](../WSFD-105104 基于IMSI号段的QoS控制（适用于MME）_62745886.md)。
- 完成加载License。

数据

需要准备全网规划的数据，无需准备与对端网元协商的数据， 如 [表1](#ZH-CN_OPI_0170933937__tbl_01) 所示。

*表1 需要准备的数据*

| 类别 | 参数 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| [**ADD QOSCAP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/EPS QoS/QoS限制配置/Non-GBR承载QoS限制/增加Non-GBR承载QoS限制配置(ADD QOSCAP)_72225897.md) | IMSI前缀（IMSIPRE） | 123001 | 全网规划 | 添加基于IMSI号段的QoS控制记录。 |
| [**ADD QOSCAP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/EPS QoS/QoS限制配置/Non-GBR承载QoS限制/增加Non-GBR承载QoS限制配置(ADD QOSCAP)_72225897.md) | 上行UE AMBR (kbps)（UEAMBRULK） | 15000kbps | 全网规划 | 添加基于IMSI号段的QoS控制记录。 |
| [**ADD QOSCAP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/EPS QoS/QoS限制配置/Non-GBR承载QoS限制/增加Non-GBR承载QoS限制配置(ADD QOSCAP)_72225897.md) | 下行UE AMBR (kbps)（UEAMBRDLK） | 15000kbps | 全网规划 | 添加基于IMSI号段的QoS控制记录。 |
| [**ADD QOSCAP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/EPS QoS/QoS限制配置/Non-GBR承载QoS限制/增加Non-GBR承载QoS限制配置(ADD QOSCAP)_72225897.md) | 上行APN AMBR (kbps)（APNAMBRULK） | 10000kbps | 全网规划 | 添加基于IMSI号段的QoS控制记录。 |
| [**ADD QOSCAP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/EPS QoS/QoS限制配置/Non-GBR承载QoS限制/增加Non-GBR承载QoS限制配置(ADD QOSCAP)_72225897.md) | 下行APN AMBR (kbps)（APNAMBRDLK） | 10000kbps | 全网规划 | 添加基于IMSI号段的QoS控制记录。 |
| [**ADD QOSCAP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/EPS QoS/QoS限制配置/Non-GBR承载QoS限制/增加Non-GBR承载QoS限制配置(ADD QOSCAP)_72225897.md) | QCI(Non-GBR承载)（QCI） | 8 | 全网规划 | 添加基于IMSI号段的QoS控制记录。 |
| [**ADD QOSCAP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/EPS QoS/QoS限制配置/Non-GBR承载QoS限制/增加Non-GBR承载QoS限制配置(ADD QOSCAP)_72225897.md) | ARP的优先级别(Non-GBR承载)（ARPPRL） | 10 | 全网规划 | 添加基于IMSI号段的QoS控制记录。 |
| [**ADD QOSCAP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/EPS QoS/QoS限制配置/Non-GBR承载QoS限制/增加Non-GBR承载QoS限制配置(ADD QOSCAP)_72225897.md) | ARP的抢占能力(Non-GBR承载)（ARPPCI） | ENABLE | 全网规划 | 添加基于IMSI号段的QoS控制记录。 |
| [**ADD QOSCAP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/EPS QoS/QoS限制配置/Non-GBR承载QoS限制/增加Non-GBR承载QoS限制配置(ADD QOSCAP)_72225897.md) | ARP的被抢占能力(Non-GBR承载)（ARPPVI） | ENABLE | 全网规划 | 添加基于IMSI号段的QoS控制记录。 |
| [**ADD QOSCAP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/EPS QoS/QoS限制配置/Non-GBR承载QoS限制/增加Non-GBR承载QoS限制配置(ADD QOSCAP)_72225897.md) | 仅使用配置QoS限制（SUBQOS） | YES | 全网规划 | 添加基于IMSI号段的QoS控制记录。 |
| [**ADD QOSCAP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/EPS QoS/QoS限制配置/Non-GBR承载QoS限制/增加Non-GBR承载QoS限制配置(ADD QOSCAP)_72225897.md) | 网络提升Non-GBR承载QoS（CTRLNWQOS） | ACCEPT | 全网规划 | 添加基于IMSI号段的QoS控制记录。 |
| [**ADD QOSCAP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/EPS QoS/QoS限制配置/Non-GBR承载QoS限制/增加Non-GBR承载QoS限制配置(ADD QOSCAP)_72225897.md) | Non-GBR专有承载控制策略（DEDBEARER） | DEFAULT | 全网规划 | 添加基于IMSI号段的QoS控制记录。 |
| [**ADD QOSCAPBYQCI**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/EPS QoS/QoS限制配置/基于QCI的承载级QoS限制/增加基于QCI的Non-GBR承载QoS限制配置(ADD QOSCAPBYQCI)_26306032.md) | 用户范围（SUBRANGE） | IMSI_PREFIX | 全网规划 | 添加基于IMSI号段和QCI的QoS控制记录。当需要基于QCI粒度进一步限制QoS时可执行此步骤。 |
| [**ADD QOSCAPBYQCI**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/EPS QoS/QoS限制配置/基于QCI的承载级QoS限制/增加基于QCI的Non-GBR承载QoS限制配置(ADD QOSCAPBYQCI)_26306032.md) | IMSI前缀（IMSIPRE） | 123001 | 全网规划 | 添加基于IMSI号段和QCI的QoS控制记录。当需要基于QCI粒度进一步限制QoS时可执行此步骤。 |
| [**ADD QOSCAPBYQCI**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/EPS QoS/QoS限制配置/基于QCI的承载级QoS限制/增加基于QCI的Non-GBR承载QoS限制配置(ADD QOSCAPBYQCI)_26306032.md) | QCI（QCI） | 5 | 全网规划 | 添加基于IMSI号段和QCI的QoS控制记录。当需要基于QCI粒度进一步限制QoS时可执行此步骤。 |
| [**ADD QOSCAPBYQCI**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/EPS QoS/QoS限制配置/基于QCI的承载级QoS限制/增加基于QCI的Non-GBR承载QoS限制配置(ADD QOSCAPBYQCI)_26306032.md) | ARP的优先级别 （ARPPRL） | 1 | 全网规划 | 添加基于IMSI号段和QCI的QoS控制记录。当需要基于QCI粒度进一步限制QoS时可执行此步骤。 |
| [**ADD QOSCAPBYQCI**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/EPS QoS/QoS限制配置/基于QCI的承载级QoS限制/增加基于QCI的Non-GBR承载QoS限制配置(ADD QOSCAPBYQCI)_26306032.md) | ARP的抢占能力（ARPPCI） | ENABLE | 全网规划 | 添加基于IMSI号段和QCI的QoS控制记录。当需要基于QCI粒度进一步限制QoS时可执行此步骤。 |
| [**ADD QOSCAPBYQCI**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/EPS QoS/QoS限制配置/基于QCI的承载级QoS限制/增加基于QCI的Non-GBR承载QoS限制配置(ADD QOSCAPBYQCI)_26306032.md) | 描述信息（DESC） | For MobileNet1 | 本端规划 | 添加基于IMSI号段和QCI的QoS控制记录。当需要基于QCI粒度进一步限制QoS时可执行此步骤。 |

## [操作步骤](#ZH-CN_OPI_0170933937)

1. 进入 “MML命令行-UNC” 窗口。
2. 检查本特性的License配置开关。
    a. 查询本特性License配置开关状态。
      **[**LST LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md)**
          - “开关”=“打开”，执行[步骤 3](#ZH-CN_OPI_0170933937__step_1)。
          - “开关”=“关闭”，执行[步骤 2.b](#ZH-CN_OPI_0170933937__SET_LICCTRL)。
    b. 打开本特性的License配置开关。
      **[**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)**
3. 添加基于IMSI号段的QoS控制记录。
  [**ADD QOSCAP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/EPS QoS/QoS限制配置/Non-GBR承载QoS限制/增加Non-GBR承载QoS限制配置(ADD QOSCAP)_72225897.md)
4. **可选：**添加基于IMSI号段和QCI的QoS控制记录。当需要基于QCI粒度进一步限制QoS时可执行此步骤。
  [**ADD QOSCAPBYQCI**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/EPS QoS/QoS限制配置/基于QCI的承载级QoS限制/增加基于QCI的Non-GBR承载QoS限制配置(ADD QOSCAPBYQCI)_26306032.md)

## [任务示例](#ZH-CN_OPI_0170933937)

任务描述

增加一条QoS限制配置，对于IMSI前缀为123001（即IMSI号范围在12300100000~12300199999内）的用户，将上行UE AMBR限制为20000kbps，下行UE AMBR限制为20000kbps，上行APN AMBR限制为10000kbps，下行APN AMBR限制为10000kbps。

为MobileNet1增加一条QoS限制配置，对于IMSI前缀为123001，QCI为5的用户，设置其ARP的优先级别为1，允许该范围内的用户在网络资源受限的情况下抢占其他低ARP优先级承载的资源。

脚本

//打开License配置开关。

```
SET LICENSESWITCH: LICITEM="LKV2IMSIQOS02", SWITCH=ENABLE;
```

//添加基于IMSI号段的QoS控制记录。

```
ADD QOSCAP:RATTYPE=ALL,SUBRANGE=IMSI_PREFIX, IMSIPRE="123001", UEAMBRULK=15000, UEAMBRDLK=15000, APNAMBRULK=10000, APNAMBRDLK=10000;
```

//添加基于IMSI号段和QCI的QoS控制记录。

```
ADD QOSCAPBYQCI: SUBRANGE=IMSI_PREFIX, IMSIPRE="123001", QCI=5, ARPPRL=1, ARPPCI=ENABLE, DESC="For MobileNet1";
```
