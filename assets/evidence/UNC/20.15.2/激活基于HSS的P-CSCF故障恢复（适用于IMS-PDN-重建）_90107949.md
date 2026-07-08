# 激活基于HSS的P-CSCF故障恢复（适用于IMS PDN 重建）

- [操作场景](#ZH-CN_OPI_0000001190107949__1.3.1)
- [必备事项](#ZH-CN_OPI_0000001190107949__1.3.2)
- [操作步骤](#ZH-CN_OPI_0000001190107949__1.3.3)
- [任务示例](#ZH-CN_OPI_0000001190107949__1.3.4)

## [操作场景](#ZH-CN_OPI_0000001190107949)

本操作指导介绍在运行网络中激活基于HSS的P-CSCF故障恢复的操作过程。

> **说明**
> 适用于MME。

## [必备事项](#ZH-CN_OPI_0000001190107949)

前提条件

- 请仔细阅读[WSFD-201205 基于HSS的P-CSCF故障恢复（IMS PDN 重建）特性概述](特性概述（适用于IMS PDN 重建）_89987789.md)。
- 已完成加载License。

数据

| 类别 | 参数 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| [**ADD DMCMPTBYIMSI**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/信令传输管理/Diameter管理/Diameter协议接口兼容性IMSI号段配置/增加IMSI对应的Diameter兼容性(ADD DMCMPTBYIMSI)_72225977.md) | 用户范围（SUBRANGE） | IMSI_PREFIX | 全网规划 | 配置基于HSS的P-CSCF故障恢复特性。 |
| [**ADD DMCMPTBYIMSI**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/信令传输管理/Diameter管理/Diameter协议接口兼容性IMSI号段配置/增加IMSI对应的Diameter兼容性(ADD DMCMPTBYIMSI)_72225977.md) | IMSI前缀（IMSIPRE） | 123123 | 全网规划 | 配置基于HSS的P-CSCF故障恢复特性。 |
| [**ADD DMCMPTBYIMSI**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/信令传输管理/Diameter管理/Diameter协议接口兼容性IMSI号段配置/增加IMSI对应的Diameter兼容性(ADD DMCMPTBYIMSI)_72225977.md) | 特性列表2（SF2） | FLSTID2_BIT16-1 | 全网规划 | 配置基于HSS的P-CSCF故障恢复特性。 |
| [**SET DMCMPT**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/信令传输管理/Diameter管理/Diameter协议接口兼容性配置/设置Diameter兼容性(SET DMCMPT)_26306080.md) | 特性列表2（SF2） | FLSTID2_BIT16-1 | 全网规划 | 配置基于HSS的P-CSCF故障恢复特性。 |

## [操作步骤](#ZH-CN_OPI_0000001190107949)

1. 进入 “MML命令行-UNC” 窗口。
2. 配置支持基于HSS的P-CSCF故障恢复特性。
  [**SET DMCMPT**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/信令传输管理/Diameter管理/Diameter协议接口兼容性配置/设置Diameter兼容性(SET DMCMPT)_26306080.md)
  [**ADD DMCMPTBYIMSI**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/信令传输管理/Diameter管理/Diameter协议接口兼容性IMSI号段配置/增加IMSI对应的Diameter兼容性(ADD DMCMPTBYIMSI)_72225977.md)
  [**LST DMCMPT**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/信令传输管理/Diameter管理/Diameter协议接口兼容性配置/查询Diameter兼容配置(LST DMCMPT)_72345869.md)

  ![](激活基于HSS的P-CSCF故障恢复（适用于IMS PDN 重建）_90107949.assets/notice_3.0-zh-cn_2.png)

  命令 [**SET DMCMPT**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/信令传输管理/Diameter管理/Diameter协议接口兼容性配置/设置Diameter兼容性(SET DMCMPT)_26306080.md) 和 [**ADD DMCMPTBYIMSI**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/信令传输管理/Diameter管理/Diameter协议接口兼容性IMSI号段配置/增加IMSI对应的Diameter兼容性(ADD DMCMPTBYIMSI)_72225977.md) 中除 “用户范围” 、 “运营商标识” 以及 “IMSI前缀” 外的其余参数功能均相同，且若系统中同时存在这两条命令的配置，系统会优先匹配命令 [**ADD DMCMPTBYIMSI**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/信令传输管理/Diameter管理/Diameter协议接口兼容性IMSI号段配置/增加IMSI对应的Diameter兼容性(ADD DMCMPTBYIMSI)_72225977.md) 的配置。因此在配置 [**ADD DMCMPTBYIMSI**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/信令传输管理/Diameter管理/Diameter协议接口兼容性IMSI号段配置/增加IMSI对应的Diameter兼容性(ADD DMCMPTBYIMSI)_72225977.md) 前需先执行 [**LST DMCMPT**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/信令传输管理/Diameter管理/Diameter协议接口兼容性配置/查询Diameter兼容配置(LST DMCMPT)_72345869.md) 查询系统中 [**SET DMCMPT**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/信令传输管理/Diameter管理/Diameter协议接口兼容性配置/设置Diameter兼容性(SET DMCMPT)_26306080.md) 的配置记录，确保命令 [**ADD DMCMPTBYIMSI**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/信令传输管理/Diameter管理/Diameter协议接口兼容性IMSI号段配置/增加IMSI对应的Diameter兼容性(ADD DMCMPTBYIMSI)_72225977.md) 的配置记录中所携带的参数默认值不影响系统已有配置。
3. 打开本特性的License配置开关。
  [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
4. **可选：**清除HSS信息。
  [**CLR HSSINFO**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/Diameter应用协议/HSS管理/清除HSS信息(CLR HSSINFO)_72225137.md)
  > **说明**
  > 根据3GPP 23.380定义，只要有一个用户通过Update Location Request消息通知HSS MME支持P-CSCF Restoration特性，HSS即认为整个MME支持此特性。如果HSS实现符合协议定义，则无需执行本步骤。

## [任务示例](#ZH-CN_OPI_0000001190107949)

任务描述

激活基于HSS的P-CSCF故障恢复特性，假设仅本网HSS支持本特性，其他用户的归属HSS都不支持本特性。

脚本

// 进入 “MML命令行-UNC” 窗口。

//配置支持基于HSS的P-CSCF故障恢复特性。（实际部署时，需要根据HSS是否支持本特性，组合如下命令进行配置）

- 所有HSS都支持此特性：
  ```
  SET DMCMPT: SF2=FLSTID2_BIT16-1;
  ```
- 本网所有的HSS支持此特性，外网所有HSS不支持此特性：
  ```
  ADD DMCMPTBYIMSI: SUBRANGE=HOME_USER, NOID=0, SF2=FLSTID2_BIT16-1;
  ```
- 仅46123和46321为IMSI前缀的用户注册的HSS支持此特性：
  ```
  ADD DMCMPTBYIMSI: SUBRANGE=IMSI_PREFIX, IMSIPRE="46123", SF2=FLSTID2_BIT16-1;
  ADD DMCMPTBYIMSI: SUBRANGE=IMSI_PREFIX, IMSIPRE="46321", SF2=FLSTID2_BIT16-1;
  ```

//打开License配置开关。

```
SET LICENSESWITCH: LICITEM="LKV2FRPH02", SWITCH=ENABLE;
```

//清除HSS信息。

```
CLR HSSINFO: HSSHTNAME="hss.epc.mnc456.mcc123.3gppnetwork.org";
```
