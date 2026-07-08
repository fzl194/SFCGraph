# 激活PCC模式的本地QoS策略控制（适用于SGSN）

- [操作场景](#ZH-CN_OPI_0192954490__1.3.1)
- [必备事项](#ZH-CN_OPI_0192954490__1.3.2)
- [操作步骤](#ZH-CN_OPI_0192954490__1.3.3)
- [任务示例](#ZH-CN_OPI_0192954490__1.3.4)

## [操作场景](#ZH-CN_OPI_0192954490)

本操作指导介绍在运行网络中激活PCC模式的本地QoS策略控制特性的操作过程。

GPRS网络中， UNC 作为GnGp SGSN，为PCC（Policy and Charging Control）用户和非PCC用户提供灵活的QoS策略。

- 对于非PCC用户，GnGp SGSN作为QoS决策中心。
- 对于PCC用户，GnGp SGSN允许PCRF/PCEF根据PCC策略决策UE使用的QoS。

> **说明**
> 适用于 SGSN 。

## [必备事项](#ZH-CN_OPI_0192954490)

前提条件

- 请仔细阅读[PCC模式的本地QoS策略控制（适用于SGSN）](../PCC模式的本地QoS策略控制（适用于SGSN）_92954487.md)。
- 完成加载License。

数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| [**ADD IMSISMCHAR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/Pre-R8 QoS/QoS协商控制/QoS协商参数管理/增加QoS协商参数(ADD IMSISMCHAR)_26306040.md) | 用户范围（SUBRANGE） | IMSI_PREFIX | 全网规划 | QoS参数 |
| [**ADD IMSISMCHAR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/Pre-R8 QoS/QoS协商控制/QoS协商参数管理/增加QoS协商参数(ADD IMSISMCHAR)_26306040.md) | IMSI前缀（IMSIPRE） | 12300755 | 全网规划 | QoS参数 |
| [**ADD IMSISMCHAR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/Pre-R8 QoS/QoS协商控制/QoS协商参数管理/增加QoS协商参数(ADD IMSISMCHAR)_26306040.md) | 起始IMSI(BEGIMSI) | 123007550 | 全网规划 | QoS参数 |
| [**ADD IMSISMCHAR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/Pre-R8 QoS/QoS协商控制/QoS协商参数管理/增加QoS协商参数(ADD IMSISMCHAR)_26306040.md) | 终止IMSI(ENDIMSI) | 123007552 | 全网规划 | QoS参数 |
| [**ADD IMSISMCHAR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/Pre-R8 QoS/QoS协商控制/QoS协商参数管理/增加QoS协商参数(ADD IMSISMCHAR)_26306040.md) | 运营商标识（NOID） | 0 | 全网规划 | QoS参数 |
| [**ADD IMSISMCHAR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/Pre-R8 QoS/QoS协商控制/QoS协商参数管理/增加QoS协商参数(ADD IMSISMCHAR)_26306040.md) | 用户子类（USERSUBTYPE） | HOME_ALL_USER | 全网规划 | QoS参数 |
| [**ADD IMSISMCHAR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/Pre-R8 QoS/QoS协商控制/QoS协商参数管理/增加QoS协商参数(ADD IMSISMCHAR)_26306040.md) | APN网络标识（APNNI） | * | 全网规划 | QoS参数 |
| [**ADD IMSISMCHAR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/Pre-R8 QoS/QoS协商控制/QoS协商参数管理/增加QoS协商参数(ADD IMSISMCHAR)_26306040.md) | UE接入能力（UEACCCAP） | ALL_UE | 全网规划 | QoS参数 |
| [**ADD IMSISMCHAR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/Pre-R8 QoS/QoS协商控制/QoS协商参数管理/增加QoS协商参数(ADD IMSISMCHAR)_26306040.md) | 协商方式（NTYPE） | NET_MIX_QOS | 全网规划 | QoS参数 |
| [**ADD IMSISMCHAR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/Pre-R8 QoS/QoS协商控制/QoS协商参数管理/增加QoS协商参数(ADD IMSISMCHAR)_26306040.md) | 是否配置2G QoS（QoS2G） | YES | 全网规划 | QoS参数 |
| [**ADD IMSISMCHAR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/Pre-R8 QoS/QoS协商控制/QoS协商参数管理/增加QoS协商参数(ADD IMSISMCHAR)_26306040.md) | 是否配置3G QoS（QoS3G） | YES | 全网规划 | QoS参数 |

## [操作步骤](#ZH-CN_OPI_0192954490)

1. 进入 “MML命令行-UNC” 窗口。
2. 检查本特性的License配置开关。
    a. 查询本特性License配置开关状态。
      [**LST LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md)
          - “开关”=“打开”，执行[步骤 3](#ZH-CN_OPI_0192954490__step2)。
          - “开关”=“关闭”，执行[步骤 2.b](#ZH-CN_OPI_0192954490__SET_LICCTRL)。
    b. 打开本特性的License配置开关。
      [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
3. 增加IMSI前缀所在号段用户的SM属性配置。
  [**ADD IMSISMCHAR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/Pre-R8 QoS/QoS协商控制/QoS协商参数管理/增加QoS协商参数(ADD IMSISMCHAR)_26306040.md)

  > **说明**
  > - 当参数“SUBRANGE”（用户范围）选择“IMSI_PREFIX”（指定IMSI前缀）时，参数“IMSIPRE”（IMSI前缀）才会显示有效。
  > - 当参数“SUBRANGE”（用户范围）选择“IMSI_RANGE”（指定IMSI范围）时，参数“BEGIMSI”（起始IMSI）和“ENDIMSI”（终止IMSI）才会显示有效。

## [任务示例](#ZH-CN_OPI_0192954490)

任务描述

配置IMSI前缀为12300755的用户使用混合模式。

脚本

//打开License配置开关。

```
SET LICENSESWITCH: LICITEM="LKV2NQOS01", SWITCH=ENABLE;
```

//配置IMSI前缀为12300755的用户使用混合模式。

```
ADD IMSISMCHAR: SUBRANGE=IMSI_PREFIX, IMSIPRE="12300755", APNNI="*", UEACCCAP=ALL_UE, NTYPE=NET_MIX_QOS, QOS2G=YES, QOS3G=YES;
```
