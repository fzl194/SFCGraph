# 激活RedCap eDRX功能（AMF支持eDRX能力协商：AMF使用UE请求值）

- [操作场景](#ZH-CN_OPI_0000001550533852__1.3.1)
- [必备事项](#ZH-CN_OPI_0000001550533852__1.3.2)
- [操作步骤](#ZH-CN_OPI_0000001550533852__1.3.3)
- [任务示例](#ZH-CN_OPI_0000001550533852__1.3.4)

## [操作场景](#ZH-CN_OPI_0000001550533852)

本操作指导介绍在运行网络中激活5G eDRX模式的过程。

> **说明**
> 适用于AMF。

## [必备事项](#ZH-CN_OPI_0000001550533852)

前提条件

- 请仔细阅读[WSFD-990005 支持5G eDRX功能特性概述](WSFD-990005 支持RedCap eDRX功能特性概述_50693596.md)。
- 已完成加载License。

数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| [**SET HSFNTIME**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/M2M管理/H-SFN参考时间配置/设置H-SFN参考时间(SET HSFNTIME)_26305580.md) | 时间类型（TIMETYPE） | GPS | 对端协商 | AMF上使用的时间类型需要与gNodeB保持一致。若大部分gNodeB使用GPS时间类型，则此参数需要配置为GPS。 |
| [**SET HSFNTIME**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/M2M管理/H-SFN参考时间配置/设置H-SFN参考时间(SET HSFNTIME)_26305580.md) | 使用GPS起始时间（GPSBEGIN） | YES | 全网规划 | 当时间类型选为GPS时，此参数固定配置为”YES”。 |
| [**SET HSFNTIME**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/M2M管理/H-SFN参考时间配置/设置H-SFN参考时间(SET HSFNTIME)_26305580.md) | 当前时间与参考时间闰秒差（GPSLEAPSEC） | 18 | 全网规划 | 18仅为参考值。此参数设置值=最新公布的闰秒数-设置的参考时间之前最近一次公布的闰秒数。闰秒数请到IERS官方网站查询：http://hpiers.obspm.fr/eoppc/bul/bulc/UTC-TAI.history。 |
| [**SET HSFNTIME**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/M2M管理/H-SFN参考时间配置/设置H-SFN参考时间(SET HSFNTIME)_26305580.md) | 时间类型（TIMETYPE） | UTC（UTC） | 对端协商 | AMF上使用的时间类型需要与gNodeB保持一致。若大部分gNodeB使用UTC时间类型，则此参数需要配置为UTC。 |
| [**SET HSFNTIME**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/M2M管理/H-SFN参考时间配置/设置H-SFN参考时间(SET HSFNTIME)_26305580.md) | H-SFN参考日期（DATE） | 2010/01/01 | 固定取值 | 设置的日期为已经过去的某一日期，不能配置未来的日期。建议保持系统初始值。 |
| [**SET HSFNTIME**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/M2M管理/H-SFN参考时间配置/设置H-SFN参考时间(SET HSFNTIME)_26305580.md) | H-SFN参考时间（TIME） | 00：00：00 | 固定取值 | 建议保持系统初始值。 |
| [**SET NGM2MCTRL**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G M2M管理/M2M控制参数/设置5G M2M控制参数（SET NGM2MCTRL）_84932189.md) | EDRX参数校正开关（UEEDRXCOSW） | YES | 固定取值 | - |
| [**SET NGM2MCTRL**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G M2M管理/M2M控制参数/设置5G M2M控制参数（SET NGM2MCTRL）_84932189.md) | NR模式寻呼窗口差值（NREDRXPAGDIFF） | MAX_DIFF_3_SECOND | 固定取值 | - |
| [**SET NGM2MCTRL**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G M2M管理/M2M控制参数/设置5G M2M控制参数（SET NGM2MCTRL）_84932189.md) | 可达性事件上报非标开关（REACHEVENTNSSW） | YES | 全网规划 | eDRX用户建议设置此参数为”YES”，非标方案，只有连接态才认为可达，这样可以提高eDRX用户下行数据传输成功率。 |
| [**SET NGM2MCTRL**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G M2M管理/M2M控制参数/设置5G M2M控制参数（SET NGM2MCTRL）_84932189.md) | AMF内移动性流程用户面建立优化（INTRAUSRPLANOPT） | YES | 固定取值 | - |
| [**SET NGM2MCTRL**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G M2M管理/M2M控制参数/设置5G M2M控制参数（SET NGM2MCTRL）_84932189.md) | AMF间移动性流程用户面建立优化（INTRAUSRPLANOPT） | YES | 固定取值 | - |
| [**ADD NGM2MPLCY**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G M2M管理/5G M2M策略参数配置/增加5G M2M策略参数（ADD NGM2MPLCY）_85251937.md) | 用户范围（SUBRANGE） | HOME_USER（本网用户） | 全网规划 | 这三个参数需根据实际业务范围和用户范围进行规划。此处以本网用户根据DNN配置策略为例。 |
| [**ADD NGM2MPLCY**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G M2M管理/5G M2M策略参数配置/增加5G M2M策略参数（ADD NGM2MPLCY）_85251937.md) | 特征条件组合（FEATURECOND） | DNN | 全网规划 | 这三个参数需根据实际业务范围和用户范围进行规划。此处以本网用户根据DNN配置策略为例。 |
| [**ADD NGM2MPLCY**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G M2M管理/5G M2M策略参数配置/增加5G M2M策略参数（ADD NGM2MPLCY）_85251937.md) | 数据网络名称（DNNNI） | huawei.com | 根据业务场景的DNNNI配置 | 这三个参数需根据实际业务范围和用户范围进行规划。此处以本网用户根据DNN配置策略为例。 |
| [**ADD NGM2MPLCY**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G M2M管理/5G M2M策略参数配置/增加5G M2M策略参数（ADD NGM2MPLCY）_85251937.md) | eDRX开关（EDRXSW） | ON | 固定取值 | - |
| [**ADD NGM2MPLCY**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G M2M管理/5G M2M策略参数配置/增加5G M2M策略参数（ADD NGM2MPLCY）_85251937.md) | NR模式EDRX寻呼周期签约优先（NREDRXSUBPRI） | NO | 全网规划 | 当UDM没有签约eDRX参数时，AMF优先使用参数“NRECL“和“NRPTW“的值。 |
| [**ADD NGM2MPLCY**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G M2M管理/5G M2M策略参数配置/增加5G M2M策略参数（ADD NGM2MPLCY）_85251937.md) | NR模式寻呼周期（NRECL） | USE_UE_REQUEST | 固定取值 | 取默认值即可。 |
| [**ADD NGM2MPLCY**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G M2M管理/5G M2M策略参数配置/增加5G M2M策略参数（ADD NGM2MPLCY）_85251937.md) | NR模式寻呼时间窗口时长（NRPTW） | USE_UE_REQUEST | 固定取值 | 取默认值即可。 |
| [**SET AMFSBICMPT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/MM协议参数管理/AMF服务化接口兼容性参数管理/设置AMF服务化接口兼容性参数（SET AMFSBICMPT）_98011756.md) | SNDPRVEDRXINFO（是否给对端AMF携带EDRX私有信元） | NO | 全网规划 | 当AMF Pool中存在异厂商AMF时，此开关需配置为“NO”，反之配置为“YES”。 |

## [操作步骤](#ZH-CN_OPI_0000001550533852)

1. 进入 “MML命令行-UNC” 窗口。
2. 设置H-SFN参考时间（时间类型GPS或者UTC请与gNodeB对齐）：
  [**SET HSFNTIME**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/M2M管理/H-SFN参考时间配置/设置H-SFN参考时间(SET HSFNTIME)_26305580.md)
3. 配置5G M2M策略参数：
  [**ADD NGM2MPLCY**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G M2M管理/5G M2M策略参数配置/增加5G M2M策略参数（ADD NGM2MPLCY）_85251937.md)
4. 配置5G M2M控制参数：
  [**SET NGM2MCTRL**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G M2M管理/M2M控制参数/设置5G M2M控制参数（SET NGM2MCTRL）_84932189.md)

## [任务示例](#ZH-CN_OPI_0000001550533852)

任务描述

支持eDRX功能的UE接入核心网时，AMF与gNodeB协商使用同一时间类型GPS，并且AMF比基站提前3s发起寻呼。AMF优先使用UE下发的eDRX参数，并且打开eDRX参数校正开关。

脚本

//配置AMF和gNodeB使用同一时间类型GPS。

```
SET HSFNTIME: TIMETYPE=GPS, GPSBEGIN=YES, GPSLEAPSEC=18;
```

//打开eDRX参数校正开关，关闭eDRX短周期使能开关，NR模式寻呼窗口差值配置初始值为3s。

```
SET NGM2MCTRL: UEEDRXCOSW=YES, SHORTECLSW=NO, REACHEVENTNSSW=YES, INTRAUSRPLANOPT=YES, INTRAUSRPLANOPT=YES;
```

//配置5G M2M终端省电策略：配置本网用户根据DNN选择用户请求的eDRX周期和PTW参数。

```
ADD NGM2MPLCY: SUBRANGE=HOME_USER, FEATURECOND=DNN, DNNNI=huawei.com, EDRXSW=ON, NRECL=USE_UE_REQUEST, NRPTW=USE_UE_REQUEST, NBPTWSUBPRI=NO;
```
