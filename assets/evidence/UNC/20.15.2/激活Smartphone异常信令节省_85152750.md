# 激活Smartphone异常信令节省

- [操作场景](#ZH-CN_OPI_0185152750__1.3.1)
- [必备事项](#ZH-CN_OPI_0185152750__1.3.2)
- [操作流程](#ZH-CN_OPI_0185152750__1.3.3)
- [操作步骤](#ZH-CN_OPI_0185152750__1.3.4)
- [任务示例](#ZH-CN_OPI_0185152750__1.3.5)

## [操作场景](#ZH-CN_OPI_0185152750)

本操作指导介绍在运行网络中激活Smartphone异常信令节省功能的操作过程。

异常信令节省是指当由于未签约APN、网络故障等原因导致UE激活失败时，UE反复进行激活，从而产生大量异常信令时。 UNC 可以根据事先配置的抑制策略对UE进行抑制此现象发生，消除由于UE的异常重复激活行为对网络侧的影响。

> **说明**
> 适用于 SGSN 。

## [必备事项](#ZH-CN_OPI_0185152750)

前提条件

- 请仔细阅读[WSFD-206006 Smartphone异常信令节省特性概述](特性概述_86930572.md)。
- 如果采用Parking APN假激活的抑制规则，需要UDG对Parking APN配置不进行数据业务和不生成话单。
- 如果采用Parking APN假激活的抑制规则，APN需要系统增加Parking的DNS解析配置，或增加DNS服务器的配置。
- 完成加载License。

数据

| 类别 | **参数名称** | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| [**ADD APNNILIB**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/Smartphone管理/终端类型识别/APNNI库管理/增加APNNI库记录（ADD APNNILIB）_26145736.md) | APNNI（APNNI） | huawei1 | 本端规划 | 配置APN NI库。 |
| [**ADD APNNILIB**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/Smartphone管理/终端类型识别/APNNI库管理/增加APNNI库记录（ADD APNNILIB）_26145736.md) | APN类型（APNTYPE） | REQUEST_APN | 本端规划 | 配置APN NI库。 |
| [**ADD APNNILIB**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/Smartphone管理/终端类型识别/APNNI库管理/增加APNNI库记录（ADD APNNILIB）_26145736.md) | 终端类型（UETYPE） | BLACKBERRY | 本端规划 | 配置APN NI库。 |
| [**SET SMARTACTPARA**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/Smartphone管理/异常信令节省/激活抑制参数管理/设置激活抑制参数（SET SMARTACTPARA）_26305550.md) | 识别异常激活行为的门限(times/h)（ABNORACTTHRESH） | 30 | 本端规划 | 开启Smartphone用户异常行为识别功能。 |
| [**ADD SMARTACT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/Smartphone管理/异常信令节省/激活抑制规则管理/增加激活抑制规则（ADD SMARTACT）_72225421.md) | 终端类型（UETYPE） | BLACKBERRY | 本端规划 | 配置激活抑制规则。 |
| [**ADD SMARTACT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/Smartphone管理/异常信令节省/激活抑制规则管理/增加激活抑制规则（ADD SMARTACT）_72225421.md) | 特定原因值拒绝激活功能开关（SPECCAUSESW） | ON | 本端规划 | 配置激活抑制规则。 |
| [**ADD SMARTACT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/Smartphone管理/异常信令节省/激活抑制规则管理/增加激活抑制规则（ADD SMARTACT）_72225421.md) | Parking APN假激活功能开关（PARKINGAPNSW） | ON | 本端规划 | 配置激活抑制规则。 |
| [**ADD SMARTACT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/Smartphone管理/异常信令节省/激活抑制规则管理/增加激活抑制规则（ADD SMARTACT）_72225421.md) | 主动分离用户功能开关（DETACHSW） | ON | 本端规划 | 配置激活抑制规则。 |
| [**ADD SMARTACT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/Smartphone管理/异常信令节省/激活抑制规则管理/增加激活抑制规则（ADD SMARTACT）_72225421.md) | 激活拒绝原因值（SMARTACTREJCAUSE） | OPERATOR_DETERMINED_BARRING_8 | 本端规划 | 配置激活抑制规则。 |
| [**ADD SMARTACT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/Smartphone管理/异常信令节省/激活抑制规则管理/增加激活抑制规则（ADD SMARTACT）_72225421.md) | 分离原因值（SMARTDETACHCAUSE） | GPRS_SERVICES_NOT_ALLOWED_7 | 本端规划 | 配置激活抑制规则。 |
| [**SET SMARTACTPARA**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/Smartphone管理/异常信令节省/激活抑制参数管理/设置激活抑制参数（SET SMARTACTPARA）_26305550.md) | Parking APN（PARKINGAPN） | huawei2.com | 本端规划 | 配置Parking APN参数。 |
| [**SET SMARTACTPARA**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/Smartphone管理/异常信令节省/激活抑制参数管理/设置激活抑制参数（SET SMARTACTPARA）_26305550.md) | 分离异常用户的SERVICE REQUEST门限(times/h)（DETACHSERVREQTHRESH） | 30 | 本端规划 | 配置Parking APN参数。 |
| [**SET SMARTACTPARA**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/Smartphone管理/异常信令节省/激活抑制参数管理/设置激活抑制参数（SET SMARTACTPARA）_26305550.md) | 抑制唤醒定时器(min)（WAKEUPTIMER） | 120 | 全网规划 | 配置抑制唤醒定时器。 |
| [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md) | License项（LICITEM） | LKV2DAPDP02 | 全网规划 | 打开本特性的License配置开关。 |
| [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md) | 开关（SWITCH） | ENABLE | 全网规划 | 打开本特性的License配置开关。 |

## [操作流程](#ZH-CN_OPI_0185152750)

激活Smartphone异常信令节省操作流程如 [图1](#ZH-CN_OPI_0185152750__zh-cn_opi_0130429035_fig_01) 所示。

**图1** 激活Smartphone异常信令节省操作流程

<br>

![](激活Smartphone异常信令节省_85152750.assets/zh-cn_image_0185156588_2.png)

<br>

## [操作步骤](#ZH-CN_OPI_0185152750)

1. 进入 “MML命令行-UNC” 窗口。
2. 配置识别终端类型的数据库。
    - 可选：配置IMEI库。
      [**ADD IMEILIB**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/Smartphone管理/终端类型识别/IMEI库管理/增加IMEI库记录（ADD IMEILIB）_26145734.md)
    - 可选：配置APN NI库。
      [**ADD APNNILIB**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/Smartphone管理/终端类型识别/APNNI库管理/增加APNNI库记录（ADD APNNILIB）_26145736.md)
  > **说明**
  > IMEI库和APN NI库两者可以同时配置，优先级从高到低依次为：签约APN，IMEI，请求APN。
3. 开启Smartphone用户异常行为识别功能。
  > **说明**
  > 如果不配置此参数，系统会根据默认值自动对Smartphone用户异常行为进行识别，默认值为30次/小时。
  [**SET SMARTACTPARA**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/Smartphone管理/异常信令节省/激活抑制参数管理/设置激活抑制参数（SET SMARTACTPARA）_26305550.md)
4. 配置激活抑制规则。
  [**ADD SMARTACT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/Smartphone管理/异常信令节省/激活抑制规则管理/增加激活抑制规则（ADD SMARTACT）_72225421.md)
  > **说明**
  > - 针对每一种终端类型，系统可以配置1～3个具体规则项，并会自动按照特定原因值拒绝激活、Parking APN假激活、主动分离用户的顺序依次执行，直到用户停止异常激活行为。
  > - 网络侧主动分离用户是抑制用户激活最有效的规则，一般最后采用此规则。
  > - 执行Parking APN假激活规则后，不允许用户使用Direct Tunnel功能。
  > - 当[**ADD SMARTACT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/Smartphone管理/异常信令节省/激活抑制规则管理/增加激活抑制规则（ADD SMARTACT）_72225421.md)命令中“BACKOFFSW”参数设置为“ON”时，建议将[**ADD SMARTACT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/Smartphone管理/异常信令节省/激活抑制规则管理/增加激活抑制规则（ADD SMARTACT）_72225421.md)命令中“SMARTACTREJCAUSE”参数设置为“INSUFFICENT_RESOURCES_26(INSUFFICENT_RESOURCES_26)”或“MISSING_OR_UNKNOWN_APN_27(MISSING_OR_UNKNOWN_APN_27)”，以实现对终端异常激活的有效控制。
5. **可选：**配置Parking APN参数。
  > **说明**
  > 如果命令 [**ADD SMARTACT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/Smartphone管理/异常信令节省/激活抑制规则管理/增加激活抑制规则（ADD SMARTACT）_72225421.md) 中的参数 “PARKINGAPNSW” （Parking APN假激活功能开关）取值为 “ON” ，则需要执行以下命令。
  [**SET SMARTACTPARA**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/Smartphone管理/异常信令节省/激活抑制参数管理/设置激活抑制参数（SET SMARTACTPARA）_26305550.md)
  > **说明**
  > - 执行Parking APN假激活规则后，如果用户的Service Request次数超过参数“DETACHSERVREQTHRESH”（分离异常用户的SERVICE REQUEST门限）的取值，则系统自动执行主动分离用户抑制规则，消除异常行为。如果不配置参数“DETACHSERVREQTHRESH”，系统会根据默认值判断用户行为是否异常，默认值为100次/小时。
  > - Parking APNNI参数的其他应用场景，请参考[Parking APNNI相关操作](Parking APNNI相关操作_85152753.md)。
6. 配置抑制唤醒定时器。
  > **说明**
  > 如果不配置此参数，系统会根据默认值执行相应流程，默认值为60min。
  [**SET SMARTACTPARA**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/Smartphone管理/异常信令节省/激活抑制参数管理/设置激活抑制参数（SET SMARTACTPARA）_26305550.md)
  > **说明**
  > “特定原因值拒绝激活唤醒开关” 及 “Parking APN假激活唤醒开关” 默认设置为打开。
7. 打开本特性的License配置开关。
  [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)

## [任务示例](#ZH-CN_OPI_0185152750)

任务描述

用户使用黑莓手机，产生大量激活失败的异常信令，需要对用户手机采用抑制激活规则并最终使其恢复正常业务。

> **说明**
> 针对黑莓手机的终端类型，系统建议配置执行三种抑制激活规则来消除用户异常行为。

脚本

//开启Smartphone用户异常行为识别功能。

```
SET SMARTACTPARA: ABNORACTTHRESH=30;
```

//配置APN NI库。

```
ADD APNNILIB: APNNI="huawei1", APNTYPE=REQUEST_APN, UETYPE=BLACKBERRY;
```

//配置激活抑制规则。

```
ADD SMARTACT: UETYPE=BLACKBERRY, SPECCAUSESW=ON, PARKINGAPNSW=ON, DETACHSW=ON, SMARTACTREJCAUSE=OPERATOR_DETERMINED_BARRING_8, SMARTDETACHCAUSE=GPRS_SERVICES_NOT_ALLOWED_7;
```

//配置Parking APNNI参数。

```
SET SMARTACTPARA: PARKINGAPN="huawei2.com", DETACHSERVREQTHRESH=30;
```

//配置抑制唤醒定时器。

```
SET SMARTACTPARA: WAKEUPTIMER=120;
```

//打开License配置开关。

```
SET LICENSESWITCH: LICITEM="LKV2SPAS02", SWITCH=ENABLE;
```
