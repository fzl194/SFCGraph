# 激活EPS Fallback紧急呼叫

- [操作场景](#ZH-CN_OPI_0226162693__1.3.1)
- [必备事项](#ZH-CN_OPI_0226162693__1.3.2)
- [操作步骤](#ZH-CN_OPI_0226162693__1.3.3)
- [任务示例](#ZH-CN_OPI_0226162693__1.3.4)

## [操作场景](#ZH-CN_OPI_0226162693)

本特性是指在UE从5G网络接入时，允许其在IMS域注册，但是当UE要进行紧急通话时，会回落到4G网络通过VoLTE进行紧急通话。在不部署VoNR的情况下提供紧急呼叫语音解决方案。

> **说明**
> 适用于AMF。

## [必备事项](#ZH-CN_OPI_0226162693)

前提条件

- 请仔细阅读[WSFD-102703 EPS Fallback紧急呼叫特性概述](特性概述_26162692.md)和[WSFD-102702 EPS Fallback特性概述](../WSFD-102702 EPS Fallback/特性概述_60374917.md)。
- 已完成[激活EPS Fallback](../WSFD-102702 EPS Fallback/激活EPS Fallback_76175590.md)。

数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| **[SET NGMMFUNC](../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/MM协议参数管理/5G移动性管理/设置5G移动性管理功能（SET NGMMFUNC）_09653748.md)** | 是否允许紧急呼叫业务（EMG） | EMFNR-1 | 全网规划 | 配置AMF支持紧急呼叫业务。 |
| [**SET NGEMGSRVFUNC**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/5G 语音业务管理/紧急呼叫业务管理/紧急服务功能配置/设置5G紧急服务功能（SET NGEMGSRVFUNC）_11421225.md) | 本网用户是否允许紧急呼叫业务（HOMEEMG） | EMFNR-1 | 全网规划 | 配置本网用户5G紧急呼叫业务。 |
| [**SET NGEMGSRVFUNC**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/5G 语音业务管理/紧急呼叫业务管理/紧急服务功能配置/设置5G紧急服务功能（SET NGEMGSRVFUNC）_11421225.md) | 本网用户紧急号码列表下发开关（HOMEEMGCNUMSW） | YES | 全网规划 | 配置本网用户5G紧急呼叫业务。 |
| **[ADD NGCONNECTPLMN](../../../../../OM参考/命令/UNC MML命令/业务服务管理/运营商管理/互联PLMN管理/增加5G Connect PLMN（ADD NGCONNECTPLMN）_09651402.md)** | 是否允许紧急呼叫业务（EMG） | EMFNR-1 | 全网规划 | 配置互联PLMN紧急呼叫业务。 |
| **[ADD NGEMGCNUM](../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/5G 语音业务管理/紧急呼叫业务管理/紧急呼叫号码配置/增加紧急号码配置信息（ADD NGEMGCNUM）_09652453.md)** | 移动国家码（MCC） | 123 | 全网规划 | 添加紧急呼叫号码。 |
| **[ADD NGEMGCNUM](../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/5G 语音业务管理/紧急呼叫业务管理/紧急呼叫号码配置/增加紧急号码配置信息（ADD NGEMGCNUM）_09652453.md)** | 紧急服务分类（ESC） | FIREBRIGADE | 全网规划 | 添加紧急呼叫号码。 |
| **[ADD NGEMGCNUM](../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/5G 语音业务管理/紧急呼叫业务管理/紧急呼叫号码配置/增加紧急号码配置信息（ADD NGEMGCNUM）_09652453.md)** | 紧急呼叫号码（NUM） | 119 | 全网规划 | 添加紧急呼叫号码。 |

## [操作步骤](#ZH-CN_OPI_0226162693)

1. 进入 “MML命令行-UNC” 窗口。
2. 打开该功能的License配置开关。
  [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
3. 配置是否允许紧急呼叫业务。
  **[SET NGMMFUNC](../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/MM协议参数管理/5G移动性管理/设置5G移动性管理功能（SET NGMMFUNC）_09653748.md)**
4. 配置本网用户5G紧急呼叫业务。
  [**SET NGEMGSRVFUNC**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/5G 语音业务管理/紧急呼叫业务管理/紧急服务功能配置/设置5G紧急服务功能（SET NGEMGSRVFUNC）_11421225.md)
5. **可选：** 配置互联PLMN的用户使用EPS Fallback紧急呼叫业务。
  如果系统中已有互联PLMN的配置，通过 [**LST NGCONNECTPLMN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/运营商管理/互联PLMN管理/查询5G Connect PLMN（LST NGCONNECTPLMN）_09653790.md) 确认 “EMG” 参数配置是否符合预期，如果不符合预期，通过 **[MOD NGCONNECTPLMN](../../../../../OM参考/命令/UNC MML命令/业务服务管理/运营商管理/互联PLMN管理/修改5G Connect PLMN（MOD NGCONNECTPLMN）_09651707.md)** 调整。
  **[MOD NGCONNECTPLMN](../../../../../OM参考/命令/UNC MML命令/业务服务管理/运营商管理/互联PLMN管理/修改5G Connect PLMN（MOD NGCONNECTPLMN）_09651707.md)**

  > **说明**
  > 该紧急呼叫业务受 **[SET NGMMFUNC](../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/MM协议参数管理/5G移动性管理/设置5G移动性管理功能（SET NGMMFUNC）_09653748.md)** 参数 “EMG” 和 **[ADD NGCONNECTPLMN](../../../../../OM参考/命令/UNC MML命令/业务服务管理/运营商管理/互联PLMN管理/增加5G Connect PLMN（ADD NGCONNECTPLMN）_09651402.md)** 参数 “EMG” 控制，且同时开启才能生效。
6. 添加紧急呼叫号码。
  **[ADD NGEMGCNUM](../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/5G 语音业务管理/紧急呼叫业务管理/紧急呼叫号码配置/增加紧急号码配置信息（ADD NGEMGCNUM）_09652453.md)**

## [任务示例](#ZH-CN_OPI_0226162693)

任务描述

激活EPS Fallback紧急呼叫特性。

脚本

// 进入 “MML命令行-UNC” 窗口。

//开启该功能的License配置开关。

```
SET LICENSESWITCH: LICITEM="LKV2EFEC01", SWITCH=ENABLE;
```

//配置允许紧急呼叫业务，并回落到LTE网络紧急呼叫。

```
SET NGMMFUNC: EMG=EMFNR-1;
```

//配置本网用户5G紧急呼叫业务。

```
SET NGEMGSRVFUNC: HOMEEMG=EMFNR-1,HOMEEMGCNUMSW=YES;
```

//配置联合PLMN的用户回落到LTE网络紧急呼叫。

```
MOD NGCONNECTPLMN: NOID=0, MCC="123", MNC="45", EMG=EMFNR-1;
```

//添加紧急呼叫号码。

```
ADD NGEMGCNUM: MCC="123", ESC=FIREBRIGADE, NUM="119";
```
