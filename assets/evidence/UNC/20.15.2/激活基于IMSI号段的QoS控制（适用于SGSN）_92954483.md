# 激活基于IMSI号段的QoS控制（适用于SGSN）

- [操作场景](#ZH-CN_OPI_0192954483__1.3.1)
- [必备事项](#ZH-CN_OPI_0192954483__1.3.2)
- [操作步骤](#ZH-CN_OPI_0192954483__1.3.3)
- [任务示例](#ZH-CN_OPI_0192954483__1.3.4)

## [操作场景](#ZH-CN_OPI_0192954483)

本操作指导介绍在运行网络中激活基于IMSI号段的QoS控制特性的操作过程。

基于IMSI号段的QoS控制是指SGSN能够按照IMSI号段对本网用户和漫游用户的QoS进行单独配置，实现灵活的QoS控制策略的功能。

本指导介绍指定IMSI号段用户的SM属性的激活过程，指定IMSI号段用户的QoS转换激活过程请参考 [激活QoS覆盖](../../WSFD-105001 QoS覆盖/激活QoS覆盖_93181073.md) 。

> **说明**
> 适用于 SGSN 。

## [必备事项](#ZH-CN_OPI_0192954483)

前提条件

- 请仔细阅读[WSFD-105104 基于IMSI号段的QoS控制（适用于SGSN）](../WSFD-105104 基于IMSI号段的QoS控制（适用于SGSN）_92954481.md)。
- 完成加载License。

数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| [**ADD IMSISMCHAR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/Pre-R8 QoS/QoS协商控制/QoS协商参数管理/增加QoS协商参数(ADD IMSISMCHAR)_26306040.md) | 用户范围（SUBRANGE） | IMSI_PREFIX | 全网规划 | 2G和3G网络共有的QoS参数 |
| [**ADD IMSISMCHAR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/Pre-R8 QoS/QoS协商控制/QoS协商参数管理/增加QoS协商参数(ADD IMSISMCHAR)_26306040.md) | IMSI前缀（IMSIPRE） | 12300755 | 全网规划 | 2G和3G网络共有的QoS参数 |
| [**ADD IMSISMCHAR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/Pre-R8 QoS/QoS协商控制/QoS协商参数管理/增加QoS协商参数(ADD IMSISMCHAR)_26306040.md) | 起始IMSI(BEGIMSI) | 123007550 | 全网规划 | 2G和3G网络共有的QoS参数 |
| [**ADD IMSISMCHAR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/Pre-R8 QoS/QoS协商控制/QoS协商参数管理/增加QoS协商参数(ADD IMSISMCHAR)_26306040.md) | 终止IMSI(ENDIMSI) | 123007552 | 全网规划 | 2G和3G网络共有的QoS参数 |
| [**ADD IMSISMCHAR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/Pre-R8 QoS/QoS协商控制/QoS协商参数管理/增加QoS协商参数(ADD IMSISMCHAR)_26306040.md) | APN网络标识（APNNI） | huawei | 全网规划 | 2G和3G网络共有的QoS参数 |
| [**ADD IMSISMCHAR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/Pre-R8 QoS/QoS协商控制/QoS协商参数管理/增加QoS协商参数(ADD IMSISMCHAR)_26306040.md) | UE接入能力（UEACCCAP） | ALL_UE | 全网规划 | 2G和3G网络共有的QoS参数 |
| [**ADD IMSISMCHAR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/Pre-R8 QoS/QoS协商控制/QoS协商参数管理/增加QoS协商参数(ADD IMSISMCHAR)_26306040.md) | 协商方式（NTYPE） | NET_NEGO_QOS | 全网规划 | 2G和3G网络共有的QoS参数 |
| [**ADD IMSISMCHAR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/Pre-R8 QoS/QoS协商控制/QoS协商参数管理/增加QoS协商参数(ADD IMSISMCHAR)_26306040.md) | Gb模式QoS协商（GBLOCCHANGE） | CN_NODE_CHGD-1 | 全网规划 | 2G和3G网络共有的QoS参数 |
| [**ADD IMSISMCHAR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/Pre-R8 QoS/QoS协商控制/QoS协商参数管理/增加QoS协商参数(ADD IMSISMCHAR)_26306040.md) | Iu模式QoS协商（IULOCCHANGE） | CN_NODE_CHGD-1 | 全网规划 | 2G和3G网络共有的QoS参数 |
| [**ADD IMSISMCHAR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/Pre-R8 QoS/QoS协商控制/QoS协商参数管理/增加QoS协商参数(ADD IMSISMCHAR)_26306040.md) | 覆盖签约QoS（SUBQOS） | NO | 全网规划 | 2G和3G网络共有的QoS参数 |
| [**ADD IMSISMCHAR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/Pre-R8 QoS/QoS协商控制/QoS协商参数管理/增加QoS协商参数(ADD IMSISMCHAR)_26306040.md) | 是否配置2G QoS（QoS2G） | YES | 全网规划 | 2G和3G网络共有的QoS参数 |
| [**ADD IMSISMCHAR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/Pre-R8 QoS/QoS协商控制/QoS协商参数管理/增加QoS协商参数(ADD IMSISMCHAR)_26306040.md) | 是否配置3G QoS（QoS3G） | YES | 全网规划 | 2G和3G网络共有的QoS参数 |
| [**ADD IMSISMCHAR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/Pre-R8 QoS/QoS协商控制/QoS协商参数管理/增加QoS协商参数(ADD IMSISMCHAR)_26306040.md) | 可靠性（RC） | NGTPLLC | 全网规划 | 2G和3G网络共有的QoS参数 |
| [**ADD IMSISMCHAR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/Pre-R8 QoS/QoS协商控制/QoS协商参数管理/增加QoS协商参数(ADD IMSISMCHAR)_26306040.md) | 优先级（PRI） | HPRI | 全网规划 | 2G和3G网络共有的QoS参数 |
| [**ADD IMSISMCHAR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/Pre-R8 QoS/QoS协商控制/QoS协商参数管理/增加QoS协商参数(ADD IMSISMCHAR)_26306040.md) | 延迟等级（DC） | DC1 | 全网规划 | 2G和3G网络共有的QoS参数 |
| [**ADD IMSISMCHAR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/Pre-R8 QoS/QoS协商控制/QoS协商参数管理/增加QoS协商参数(ADD IMSISMCHAR)_26306040.md) | 最大吞吐量(octet/s)（PT） | PT9 | 全网规划 | 2G和3G网络共有的QoS参数 |
| [**ADD IMSISMCHAR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/Pre-R8 QoS/QoS协商控制/QoS协商参数管理/增加QoS协商参数(ADD IMSISMCHAR)_26306040.md) | 平均吞吐量（octet/h）（MT） | MT18 | 全网规划 | 2G和3G网络共有的QoS参数 |
| [**ADD IMSISMCHAR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/Pre-R8 QoS/QoS协商控制/QoS协商参数管理/增加QoS协商参数(ADD IMSISMCHAR)_26306040.md) | 流量等级（TC） | CC | 全网规划 | 2G和3G网络共有的QoS参数 |
| [**ADD IMSISMCHAR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/Pre-R8 QoS/QoS协商控制/QoS协商参数管理/增加QoS协商参数(ADD IMSISMCHAR)_26306040.md) | 3G QoS最大SDU长度（MAXSDU3G） | 151 | 全网规划 | 2G和3G网络共有的QoS参数 |
| [**ADD IMSISMCHAR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/Pre-R8 QoS/QoS协商控制/QoS协商参数管理/增加QoS协商参数(ADD IMSISMCHAR)_26306040.md) | 3G QoS上行最大速率（MBRUPLK3G） | 126 | 全网规划 | 2G和3G网络共有的QoS参数 |
| [**ADD IMSISMCHAR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/Pre-R8 QoS/QoS协商控制/QoS协商参数管理/增加QoS协商参数(ADD IMSISMCHAR)_26306040.md) | 3G QoS上行保证速率（GBRUPLK3G） | 254 | 全网规划 | 2G和3G网络共有的QoS参数 |
| [**ADD IMSISMCHAR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/Pre-R8 QoS/QoS协商控制/QoS协商参数管理/增加QoS协商参数(ADD IMSISMCHAR)_26306040.md) | 3G QoS下行最大速率（MBRDNLK3G） | 126 | 全网规划 | 2G和3G网络共有的QoS参数 |
| [**ADD IMSISMCHAR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/Pre-R8 QoS/QoS协商控制/QoS协商参数管理/增加QoS协商参数(ADD IMSISMCHAR)_26306040.md) | 3G QoS下行保证速率<br>（GBRDNLK3G） | 254 | 全网规划 | 2G和3G网络共有的QoS参数 |
| [**ADD IMSISMCHAR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/Pre-R8 QoS/QoS协商控制/QoS协商参数管理/增加QoS协商参数(ADD IMSISMCHAR)_26306040.md) | 3G QoS发送次序（DO3G） | ORDER | 全网规划 | 2G和3G网络共有的QoS参数 |
| [**ADD IMSISMCHAR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/Pre-R8 QoS/QoS协商控制/QoS协商参数管理/增加QoS协商参数(ADD IMSISMCHAR)_26306040.md) | 3G QoS发送错误SDU（DESDU3G） | NODT | 全网规划 | 2G和3G网络共有的QoS参数 |
| [**ADD IMSISMCHAR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/Pre-R8 QoS/QoS协商控制/QoS协商参数管理/增加QoS协商参数(ADD IMSISMCHAR)_26306040.md) | 3G QoS保留BER（RBER3G） | RBER9 | 全网规划 | 2G和3G网络共有的QoS参数 |
| [**ADD IMSISMCHAR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/Pre-R8 QoS/QoS协商控制/QoS协商参数管理/增加QoS协商参数(ADD IMSISMCHAR)_26306040.md) | 3G QoSSDU误码率（SDUER3G） | SDUER4 | 全网规划 | 2G和3G网络共有的QoS参数 |
| [**ADD IMSISMCHAR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/Pre-R8 QoS/QoS协商控制/QoS协商参数管理/增加QoS协商参数(ADD IMSISMCHAR)_26306040.md) | 3G QoS发送控制优先级（THPRI3G） | THPRI1 | 全网规划 | 2G和3G网络共有的QoS参数 |
| [**ADD IMSISMCHAR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/Pre-R8 QoS/QoS协商控制/QoS协商参数管理/增加QoS协商参数(ADD IMSISMCHAR)_26306040.md) | 3G QoS传递时延（TD3G） | 10 | 全网规划 | 2G和3G网络共有的QoS参数 |
| [**ADD IMSISMCHAR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/Pre-R8 QoS/QoS协商控制/QoS协商参数管理/增加QoS协商参数(ADD IMSISMCHAR)_26306040.md) | 3G QoS分配保留优先级（ARPRI3G） | HIGHLEVELUSER | 全网规划 | 2G和3G网络共有的QoS参数 |
| [**ADD IMSISMCHAR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/Pre-R8 QoS/QoS协商控制/QoS协商参数管理/增加QoS协商参数(ADD IMSISMCHAR)_26306040.md) | 3G QoS无线优先级（RADIOPRI3G） | 2 | 全网规划 | 2G和3G网络共有的QoS参数 |
| [**ADD IMSISMCHAR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/Pre-R8 QoS/QoS协商控制/QoS协商参数管理/增加QoS协商参数(ADD IMSISMCHAR)_26306040.md) | 3G QoS扩展下行最大速率（MBRDNLKEX3G） | 0 | 全网规划 | 3G网络独有的QoS参数 |
| [**ADD IMSISMCHAR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/Pre-R8 QoS/QoS协商控制/QoS协商参数管理/增加QoS协商参数(ADD IMSISMCHAR)_26306040.md) | 3G QoS扩展下行保证速率（GBRDNLKEX3G） | 0 | 全网规划 | 3G网络独有的QoS参数 |
| [**ADD IMSISMCHAR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/Pre-R8 QoS/QoS协商控制/QoS协商参数管理/增加QoS协商参数(ADD IMSISMCHAR)_26306040.md) | 3G QoS扩展上行最大速率（MBRUPLKEX3G） | 0 | 全网规划 | 3G网络独有的QoS参数 |
| [**ADD IMSISMCHAR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/Pre-R8 QoS/QoS协商控制/QoS协商参数管理/增加QoS协商参数(ADD IMSISMCHAR)_26306040.md) | 3G QoS扩展上行保证速率（GBRUPLKEX3G） | 0 | 全网规划 | 3G网络独有的QoS参数 |

## [操作步骤](#ZH-CN_OPI_0192954483)

1. 进入 “MML命令行-UNC” 窗口。
2. 检查本特性的License配置开关。
    a. 查询本特性License配置开关状态。
      [**LST LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md)
          - “开关”=“打开”，执行[3](#ZH-CN_OPI_0192954483__cmd246869372180642)。
          - “开关”=“关闭”，执行[2.b](#ZH-CN_OPI_0192954483__SET_LICCTRL)。
    b. 打开本特性的License配置开关。
      [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
3. 增加IMSI前缀所在号段用户的SM属性配置。
  [**ADD IMSISMCHAR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/Pre-R8 QoS/QoS协商控制/QoS协商参数管理/增加QoS协商参数(ADD IMSISMCHAR)_26306040.md)
  > **说明**
  > 当参数 “SUBRANGE” （用户范围）选择 “IMSI_PREFIX” （指定IMSI前缀）时，参数 “IMSIPRE” （IMSI前缀）才会显示有效；当参数 “SUBRANGE” （用户范围）选择 “IMSI_RANGE” （指定IMSI范围）时，参数 “BEGIMSI” （起始IMSI）和 “ENDIMSI” （终止IMSI）才会显示有效。

## [任务示例](#ZH-CN_OPI_0192954483)

任务描述

- 任务1：对IMSI前缀为12300755，APNNI为huawei，UE接入能力为所有UE的用户，配置其2G SM属性。配置上下行最大速率均为560kbit/s，SGSN结合请求的QoS、签约的QoS和自身配置的QoS与其他网元共同进行QoS协商。
- 任务2：对IMSI前缀为12300755，APNNI为huawei1，UE接入能力为同时具备GUL能力的UE的用户，配置其3G SM属性。配置上下行最大速率均为560kbit/s，SGSN使用配置的QoS直接覆盖签约的QoS，并将此QoS发送给GGSN，最后使用GGSN响应消息中携带的QoS。

脚本

//打开License配置开关。

```
SET LICENSESWITCH: LICITEM="LKV2IMSIQOS02", SWITCH=ENABLE;
```

- 脚本1：对IMSI前缀为12300755，APNNI为huawei，UE接入能力为所有UE的用户，配置其2G SM属性。
  //配置2G上下行最大速率设置为126即为560kbit/s。
  ```
  ADD IMSISMCHAR: SUBRANGE=IMSI_PREFIX, IMSIPRE="12300755", APNNI="huawei", UEACCCAP=ALL_UE, NTYPE=NET_NEGO_QOS, QOS2G=YES, MBRUPLK2G=126, MBRDNLK2G=126, QOS3G=NO;
  ```
- 脚本2：对IMSI前缀为12300755，APNNI为huawei1，UE接入能力为同时具备GUL能力的UE的用户，配置其3G SM属性。
  //配置3G上下行最大速率设置为126即为560kbit/s。
  ```
  ADD IMSISMCHAR: SUBRANGE=IMSI_PREFIX, IMSIPRE="12300755", APNNI="huawei1", UEACCCAP=EUTRAN_CAPABLE_UE, NTYPE=NET_CTRL_QOS, SUBQOS=YES, QOS2G=NO, QOS3G=YES,  MBRUPLK3G=126, MBRDNLK3G=126;
  ```
