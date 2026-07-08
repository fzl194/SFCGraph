# 激活PCC模式的本地QoS策略控制（适用于MME）

- [操作场景](#ZH-CN_OPI_0170933939__1.3.1)
- [对系统的影响](#ZH-CN_OPI_0170933939__1.3.2)
- [必备事项](#ZH-CN_OPI_0170933939__1.3.3)
- [操作步骤](#ZH-CN_OPI_0170933939__1.3.4)
- [任务示例](#ZH-CN_OPI_0170933939__1.3.5)

## [操作场景](#ZH-CN_OPI_0170933939)

本操作指导介绍在运行网络中激活PCC模式的本地QoS策略控制特性的操作过程。

EPS网络中， UNC 作为MME，支持PCC模式下对专有承载的QoS控制。

> **说明**
> 适用于MME。

## [对系统的影响](#ZH-CN_OPI_0170933939)

该操作对系统正常运行无影响。

## [必备事项](#ZH-CN_OPI_0170933939)

前提条件

- 请仔细阅读[PCC模式的本地QoS策略控制（适用于MME）](../PCC模式的本地QoS策略控制（适用于MME）_62745887.md)。
- 完成加载License。

数据

需要准备全网规划的数据，无需准备与对端网元协商的数据， 如 [表1](#ZH-CN_OPI_0170933939__tab1) 所示。

*表1 需要准备的数据*

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| [**ADD QOSCAP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/EPS QoS/QoS限制配置/Non-GBR承载QoS限制/增加Non-GBR承载QoS限制配置(ADD QOSCAP)_72225897.md) | IMSI前缀（IMSIPRE） | 46123 | 全网规划 | 增加Non-GBR专有承载的QoS限制参数。 |
| [**ADD QOSCAP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/EPS QoS/QoS限制配置/Non-GBR承载QoS限制/增加Non-GBR承载QoS限制配置(ADD QOSCAP)_72225897.md) | 上行UE AMBR (kbps)（UEAMBRULK） | 15000 | 全网规划 | 增加Non-GBR专有承载的QoS限制参数。 |
| [**ADD QOSCAP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/EPS QoS/QoS限制配置/Non-GBR承载QoS限制/增加Non-GBR承载QoS限制配置(ADD QOSCAP)_72225897.md) | 下行UE AMBR (kbps)(UEAMBRDLK) | 15000 | 全网规划 | 增加Non-GBR专有承载的QoS限制参数。 |
| [**ADD QOSCAP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/EPS QoS/QoS限制配置/Non-GBR承载QoS限制/增加Non-GBR承载QoS限制配置(ADD QOSCAP)_72225897.md) | 上行APN AMBR (kbps)(APNAMBRULK) | 10000 | 全网规划 | 增加Non-GBR专有承载的QoS限制参数。 |
| [**ADD QOSCAP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/EPS QoS/QoS限制配置/Non-GBR承载QoS限制/增加Non-GBR承载QoS限制配置(ADD QOSCAP)_72225897.md) | 下行APN AMBR (kbps)（APNAMBRDLK） | 10000 | 全网规划 | 增加Non-GBR专有承载的QoS限制参数。 |
| [**ADD QOSCAP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/EPS QoS/QoS限制配置/Non-GBR承载QoS限制/增加Non-GBR承载QoS限制配置(ADD QOSCAP)_72225897.md) | QCI(Non-GBR承载) （QCI） | 8 | 全网规划 | 增加Non-GBR专有承载的QoS限制参数。 |
| [**ADD QOSCAP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/EPS QoS/QoS限制配置/Non-GBR承载QoS限制/增加Non-GBR承载QoS限制配置(ADD QOSCAP)_72225897.md) | ARP的优先级别(Non-GBR承载)（ARPPRL） | 10 | 全网规划 | 增加Non-GBR专有承载的QoS限制参数。 |
| [**ADD QOSCAP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/EPS QoS/QoS限制配置/Non-GBR承载QoS限制/增加Non-GBR承载QoS限制配置(ADD QOSCAP)_72225897.md) | ARP的抢占能力(Non-GBR承载)（ARPPCI） | ENABLE | 全网规划 | 增加Non-GBR专有承载的QoS限制参数。 |
| [**ADD QOSCAP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/EPS QoS/QoS限制配置/Non-GBR承载QoS限制/增加Non-GBR承载QoS限制配置(ADD QOSCAP)_72225897.md) | ARP的被抢占能力(Non-GBR承载)（ARPPVI） | ENABLE | 全网规划 | 增加Non-GBR专有承载的QoS限制参数。 |
| [**ADD QOSCAP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/EPS QoS/QoS限制配置/Non-GBR承载QoS限制/增加Non-GBR承载QoS限制配置(ADD QOSCAP)_72225897.md) | 网络提升Non-GBR承载QoS（CTRLNWQOS） | RESTRICT | 全网规划 | 增加Non-GBR专有承载的QoS限制参数。 |
| [**ADD QOSCAP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/EPS QoS/QoS限制配置/Non-GBR承载QoS限制/增加Non-GBR承载QoS限制配置(ADD QOSCAP)_72225897.md) | PDN连接建立拒绝原因值（PDNREJCAUSE） | 32 | 全网规划 | 增加Non-GBR专有承载的QoS限制参数。 |
| [**ADD QOSCAP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/EPS QoS/QoS限制配置/Non-GBR承载QoS限制/增加Non-GBR承载QoS限制配置(ADD QOSCAP)_72225897.md) | Non-GBR专有承载控制策略（DEDBEARER） | DEFAULT | 全网规划 | 增加Non-GBR专有承载的QoS限制参数。 |
| [**ADD QOSCAPBYQCI**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/EPS QoS/QoS限制配置/基于QCI的承载级QoS限制/增加基于QCI的Non-GBR承载QoS限制配置(ADD QOSCAPBYQCI)_26306032.md) | 用户范围（SUBRANGE） | IMSI_PREFIX | 全网规划 | 添加基于IMSI号段和QCI的QoS控制记录。当需要基于QCI粒度进一步限制QoS时可执行此步骤。 |
| [**ADD QOSCAPBYQCI**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/EPS QoS/QoS限制配置/基于QCI的承载级QoS限制/增加基于QCI的Non-GBR承载QoS限制配置(ADD QOSCAPBYQCI)_26306032.md) | IMSI前缀（IMSIPRE） | 46123 | 全网规划 | 添加基于IMSI号段和QCI的QoS控制记录。当需要基于QCI粒度进一步限制QoS时可执行此步骤。 |
| [**ADD QOSCAPBYQCI**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/EPS QoS/QoS限制配置/基于QCI的承载级QoS限制/增加基于QCI的Non-GBR承载QoS限制配置(ADD QOSCAPBYQCI)_26306032.md) | QCI（QCI） | 5 | 全网规划 | 添加基于IMSI号段和QCI的QoS控制记录。当需要基于QCI粒度进一步限制QoS时可执行此步骤。 |
| [**ADD QOSCAPBYQCI**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/EPS QoS/QoS限制配置/基于QCI的承载级QoS限制/增加基于QCI的Non-GBR承载QoS限制配置(ADD QOSCAPBYQCI)_26306032.md) | ARP的优先级别 （ARPPRL） | 1 | 全网规划 | 添加基于IMSI号段和QCI的QoS控制记录。当需要基于QCI粒度进一步限制QoS时可执行此步骤。 |
| [**ADD QOSCAPBYQCI**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/EPS QoS/QoS限制配置/基于QCI的承载级QoS限制/增加基于QCI的Non-GBR承载QoS限制配置(ADD QOSCAPBYQCI)_26306032.md) | ARP的抢占能力（ARPPCI） | ENABLE | 全网规划 | 添加基于IMSI号段和QCI的QoS控制记录。当需要基于QCI粒度进一步限制QoS时可执行此步骤。 |
| [**ADD QOSCAPBYQCI**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/EPS QoS/QoS限制配置/基于QCI的承载级QoS限制/增加基于QCI的Non-GBR承载QoS限制配置(ADD QOSCAPBYQCI)_26306032.md) | 描述信息（DESC） | For MobileNet1 | 全网规划 | 添加基于IMSI号段和QCI的QoS控制记录。当需要基于QCI粒度进一步限制QoS时可执行此步骤。 |
| [**ADD QOSCAPGBR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/EPS QoS/QoS限制配置/GBR承载QoS限制/增加GBR承载QoS限制配置(ADD QOSCAPGBR)_26146216.md) | IMSI前缀(IMSIPRE) | 46123 | 全网规划 | 配置GBR专有承载的QoS限制参数。 |
| [**ADD QOSCAPGBR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/EPS QoS/QoS限制配置/GBR承载QoS限制/增加GBR承载QoS限制配置(ADD QOSCAPGBR)_26146216.md) | QCI(GBR承载)(GBRQCI) | 4 | 全网规划 | 配置GBR专有承载的QoS限制参数。 |
| [**ADD QOSCAPGBR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/EPS QoS/QoS限制配置/GBR承载QoS限制/增加GBR承载QoS限制配置(ADD QOSCAPGBR)_26146216.md) | 上行最大速率 (kbps)(GBRMBRULK) | 15000 | 全网规划 | 配置GBR专有承载的QoS限制参数。 |
| [**ADD QOSCAPGBR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/EPS QoS/QoS限制配置/GBR承载QoS限制/增加GBR承载QoS限制配置(ADD QOSCAPGBR)_26146216.md) | 下行最大速率 (kbps)(GBRMBRDLK) | 15000 | 全网规划 | 配置GBR专有承载的QoS限制参数。 |
| [**ADD QOSCAPGBR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/EPS QoS/QoS限制配置/GBR承载QoS限制/增加GBR承载QoS限制配置(ADD QOSCAPGBR)_26146216.md) | 上行保证速率 (kbps)(GBRGBRULK) | 10000 | 全网规划 | 配置GBR专有承载的QoS限制参数。 |
| [**ADD QOSCAPGBR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/EPS QoS/QoS限制配置/GBR承载QoS限制/增加GBR承载QoS限制配置(ADD QOSCAPGBR)_26146216.md) | 下行保证速率 (kbps)(GBRGBRDLK) | 10000 | 全网规划 | 配置GBR专有承载的QoS限制参数。 |
| [**ADD QOSCAPGBR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/EPS QoS/QoS限制配置/GBR承载QoS限制/增加GBR承载QoS限制配置(ADD QOSCAPGBR)_26146216.md) | ARP的优先级别(GBR承载)(GBRARPPRL) | 1 | 全网规划 | 配置GBR专有承载的QoS限制参数。 |
| [**ADD QOSCAPGBR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/EPS QoS/QoS限制配置/GBR承载QoS限制/增加GBR承载QoS限制配置(ADD QOSCAPGBR)_26146216.md) | ARP的抢占能力(GBR承载)(GBRARPPCI) | DISABLE | 全网规划 | 配置GBR专有承载的QoS限制参数。 |
| [**ADD QOSCAPGBR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/EPS QoS/QoS限制配置/GBR承载QoS限制/增加GBR承载QoS限制配置(ADD QOSCAPGBR)_26146216.md) | ARP的被抢占能力(GBR承载)(GBRARPPVI) | DISABLE | 全网规划 | 配置GBR专有承载的QoS限制参数。 |
| [**ADD QOSCAPGBR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/EPS QoS/QoS限制配置/GBR承载QoS限制/增加GBR承载QoS限制配置(ADD QOSCAPGBR)_26146216.md) | 网络提升GBR承载QoS(GBRCTRLNWQOS) | RESTRICT | 全网规划 | 配置GBR专有承载的QoS限制参数。 |

## [操作步骤](#ZH-CN_OPI_0170933939)

1. 进入 “MML命令行-UNC” 窗口。
2. 检查本特性的License配置开关。
    a. 查询本特性License配置开关状态。
      **[**LST LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md)**
          - “开关”=“打开”，执行[步骤 3](#ZH-CN_OPI_0170933939__step2)。
          - “开关”=“关闭”，执行[步骤 2.b](#ZH-CN_OPI_0170933939__SET_LICCTRL)。
    b. 打开本特性的License配置开关。
      **[**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)**
3. 检查Non-GBR承载的配置。
    a. 查询Non-GBR承载的配置记录。
      **[**LST QOSCAP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/EPS QoS/QoS限制配置/Non-GBR承载QoS限制/查询Non-GBR承载QoS限制配置(LST QOSCAP)_26146220.md)**
          - 存在配置记录，执行[步骤 3.b](#ZH-CN_OPI_0170933939__step2b)。
          - 不存在配置记录，执行[步骤 3.c](#ZH-CN_OPI_0170933939__step2c)。
    b. 修改Non-GBR承载的配置，增加专有承载的QoS限制参数。然后执行 [步骤 4](#ZH-CN_OPI_0170933939__step3) 。
      **[**MOD QOSCAP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/EPS QoS/QoS限制配置/Non-GBR承载QoS限制/修改Non-GBR承载QoS限制配置(MOD QOSCAP)_72345819.md)**
    c. 增加Non-GBR专有承载的QoS限制参数。
      [**ADD QOSCAP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/EPS QoS/QoS限制配置/Non-GBR承载QoS限制/增加Non-GBR承载QoS限制配置(ADD QOSCAP)_72225897.md)
    d. **可选：**添加基于IMSI号段和QCI的QoS控制记录。当需要基于QCI粒度进一步限制QoS时可执行此步骤。
      [**ADD QOSCAPBYQCI**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/EPS QoS/QoS限制配置/基于QCI的承载级QoS限制/增加基于QCI的Non-GBR承载QoS限制配置(ADD QOSCAPBYQCI)_26306032.md)
4. 配置GBR专有承载的QoS限制参数。
  [**ADD QOSCAPGBR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/EPS QoS/QoS限制配置/GBR承载QoS限制/增加GBR承载QoS限制配置(ADD QOSCAPGBR)_26146216.md)

## [任务示例](#ZH-CN_OPI_0170933939)

任务描述

运营商A对漫游用户的缺省承载QoS进行限制，增加对专有承载QoS的限制。用户前缀为46123，QCI为8，上下行最大速率为15000kbps，上下行保证速率为10000kbps，ARP等级为10。当网络侧提升QoS时，MME上对QoS进行限制。

脚本

//打开License配置开关。

```
LST LICENSESWITCH: LICITEM="LKV2NQOS01";
SET LICENSESWITCH: LICITEM="LKV2NQOS01", SWITCH=ENABLE;
```

//配置Non-GBR专有承载的QoS限制参数。

```
LST QOSCAP: SUBRANGE=IMSI_PREFIX, IMSIPRE="46123";
MOD QOSCAP: 
RATTYPE=ALL,SUBRANGE=IMSI_PREFIX,
IMSIPRE="46123", QCI=8, ARPPRL=10, ARPPCI=DISABLE, ARPPVI=DISABLE, CTRLNWQOS=RESTRICT, DEDBEARER=DEFAULT;
```

///添加基于IMSI号段和QCI的QoS控制记录。

```
ADD QOSCAPBYQCI: SUBRANGE=IMSI_PREFIX, IMSIPRE="46123", QCI=5, ARPPRL=1, ARPPCI=ENABLE, DESC="For MobileNet1";
```

//配置GBR专有承载的QoS限制参数。

```
ADD QOSCAPGBR: IMSIPRE="46123", GBRQCI=4, GBRMBRULK=15000, GBRMBRDLK=15000, GBRGBRULK=10000, GBRGBRDLK=10000, GBRARPPRL=10, GBRARPPCI=DISABLE, GBRARPPVI=DISABLE, GBRCTRLNWQOS=RESTRICT;
```
