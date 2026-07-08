# 激活VoLTE紧急呼叫的定位(NI-LR)

- [操作场景](#ZH-CN_OPI_0170014699__1.3.1)
- [必备事项](#ZH-CN_OPI_0170014699__1.3.2)
- [操作步骤](#ZH-CN_OPI_0170014699__1.3.3)
- [任务示例](#ZH-CN_OPI_0170014699__1.3.4)

## [操作场景](#ZH-CN_OPI_0170014699)

本操作指导介绍在运行网络中激活VoLTE紧急呼叫的定位(NI-LR)的操作过程。

> **说明**
> 适用于MME。

## [必备事项](#ZH-CN_OPI_0170014699)

前提条件

- 已完成加载License。
- 在标准LCS组网中，已经完成SLg和SLs接口数据配置，详细请参见[SLg接口配置指导](../../../../初始配置/UNC初始配置与调测/组网对接配置/配置AMF&MME&SGSN/配置MME/配置到E-SMLC的数据_29346481.md)和[SLs接口配置指导](../../../../初始配置/UNC初始配置与调测/组网对接配置/配置AMF&MME&SGSN/配置MME/配置到E-SMLC的数据_29346481.md)。

数据

| 类别 | 参数 | 取值样例 | 获取方法 | 相关命令 |
| --- | --- | --- | --- | --- |
| [**ADD DMHOSTRT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/信令传输管理/Diameter管理/Diameter主机路由/增加Diameter主机路由(ADD DMHOSTRT)_26146272.md) | 路由索引 | 2 | 全网规划 | 增加Diameter主机路由。 |
| [**ADD DMHOSTRT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/信令传输管理/Diameter管理/Diameter主机路由/增加Diameter主机路由(ADD DMHOSTRT)_26146272.md) | 应用名称 | SLG(SLg) | 全网规划 | 增加Diameter主机路由。 |
| [**ADD DMHOSTRT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/信令传输管理/Diameter管理/Diameter主机路由/增加Diameter主机路由(ADD DMHOSTRT)_26146272.md) | 选路模式 | SELMODE_MASTER_SLAVE(主从) | 全网规划 | 增加Diameter主机路由。 |
| [**ADD DMHOSTRT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/信令传输管理/Diameter管理/Diameter主机路由/增加Diameter主机路由(ADD DMHOSTRT)_26146272.md) | 目的实体选择方式 | PEER_INDEX(对端索引) | 全网规划 | 增加Diameter主机路由。 |
| [**ADD DMHOSTRT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/信令传输管理/Diameter管理/Diameter主机路由/增加Diameter主机路由(ADD DMHOSTRT)_26146272.md) | 对端实体索引 | 1 | 全网规划 | 增加Diameter主机路由。 |
| [**ADD DMRTGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/信令传输管理/Diameter管理/Diameter路由组/增加Diameter路由组(ADD DMRTGRP)_26146292.md) | 路由组索引 | 1 | 全网规划 | 增加Diameter路由组。 |
| [**ADD DMRTGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/信令传输管理/Diameter管理/Diameter路由组/增加Diameter路由组(ADD DMRTGRP)_26146292.md) | 路由模式 | HOST_ROUTE(主机路由) | 全网规划 | 增加Diameter路由组。 |
| [**ADD DMRTGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/信令传输管理/Diameter管理/Diameter路由组/增加Diameter路由组(ADD DMRTGRP)_26146292.md) | 路由优选模式 | HOST_ROUTE_PREFER(优选主机路由) | 全网规划 | 增加Diameter路由组。 |
| [**ADD DMRTGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/信令传输管理/Diameter管理/Diameter路由组/增加Diameter路由组(ADD DMRTGRP)_26146292.md) | 对端实体索引 | 2 | 全网规划 | 增加Diameter路由组。 |
| [**ADD DMRTGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/信令传输管理/Diameter管理/Diameter路由组/增加Diameter路由组(ADD DMRTGRP)_26146292.md) | 路由组名称 | GMLC | 全网规划 | 增加Diameter路由组。 |
| [**ADD GMLCSELGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/LCS/GMLC选择策略组/增加GMLC选择策略组(ADD GMLCSELGRP)_26145810.md) | GMLC选择策略组索引 | 6 | 全网规划 | 增加GMLC选择策略组。 |
| [**ADD GMLCSELPLCY**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/LCS/GMLC选择策略/增加GMLC选择策略(ADD GMLCSELPLCY)_72225491.md) | GMLC选择策略组索引 | 6 | 全网规划 | 增加GMLC选择策略。 |
| [**ADD GMLCSELPLCY**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/LCS/GMLC选择策略/增加GMLC选择策略(ADD GMLCSELPLCY)_72225491.md) | LCS客户端类型 | EMERGENCY_SERVICES(紧急业务) | 全网规划 | 增加GMLC选择策略。 |
| [**ADD GMLCSELPLCY**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/LCS/GMLC选择策略/增加GMLC选择策略(ADD GMLCSELPLCY)_72225491.md) | 位置区标识类型 | ECI(小区标识) | 全网规划 | 增加GMLC选择策略。 |
| [**ADD GMLCSELPLCY**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/LCS/GMLC选择策略/增加GMLC选择策略(ADD GMLCSELPLCY)_72225491.md) | 小区起始标识 | 3 | 全网规划 | 增加GMLC选择策略。 |
| [**ADD GMLCSELPLCY**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/LCS/GMLC选择策略/增加GMLC选择策略(ADD GMLCSELPLCY)_72225491.md) | 小区结束标识 | 16 | 全网规划 | 增加GMLC选择策略。 |
| [**ADD GMLCSELPLCY**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/LCS/GMLC选择策略/增加GMLC选择策略(ADD GMLCSELPLCY)_72225491.md) | GMLC域名 | gmlc.epc.mnc456.mcc123.3gppnetwork.org | 全网规划 | 增加GMLC选择策略。 |
| [**ADD GMLCSELPLCY**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/LCS/GMLC选择策略/增加GMLC选择策略(ADD GMLCSELPLCY)_72225491.md) | Diameter路由组索引 | 1 | 全网规划 | 增加GMLC选择策略。 |
| [**ADD LCSPARAEX**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/LCS/LCS扩展参数/增加LCS扩展参数(ADD LCSPARAEX)_26305624.md) | 运营商标识 | 46 | 全网规划 | 增加LCS扩展参数。 |
| [**ADD LCSPARAEX**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/LCS/LCS扩展参数/增加LCS扩展参数(ADD LCSPARAEX)_26305624.md) | 紧急呼叫NI-LR支持开关 | ON(开) | 全网规划 | 增加LCS扩展参数。 |
| [**ADD LCSPARAEX**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/LCS/LCS扩展参数/增加LCS扩展参数(ADD LCSPARAEX)_26305624.md) | GMLC选择策略组索引 | 1 | 全网规划 | 增加LCS扩展参数。 |
| [**ADD LCSPARAEX**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/LCS/LCS扩展参数/增加LCS扩展参数(ADD LCSPARAEX)_26305624.md) | 上报类型 | LOCATE（经过定位再上报） | 全网规划 | 增加LCS扩展参数。 |
| [**ADD LCSPARAEX**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/LCS/LCS扩展参数/增加LCS扩展参数(ADD LCSPARAEX)_26305624.md) | 是否支持缺省承载呼叫 | NO（不支持） | 全网规划 | 增加LCS扩展参数。 |
| [**ADD LCSPARAEX**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/LCS/LCS扩展参数/增加LCS扩展参数(ADD LCSPARAEX)_26305624.md) | HO上报类型（HORPTTYPE） | SOURCE（由源侧上报） | 全网规划 | 增加LCS扩展参数。 |
| [**SET LCSPARA**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/LCS/LCS软件参数表/设置LCS参数表记录(SET LCSPARA)_72225477.md) | ECM-IDLE态触发Paging | YES（是） | 全网规划 | 设置LCS参数表记录。 |
| [**MOD MMECHARACT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/GTP-C接口管理/GnGp-SGSN_S10_S16_S3接口管理/MME属性/修改MME属性配置信息（MOD MMECHARACT）_26145958.md) | 对端设备范围 | ALL_MME（所有MME） | 全网规划 | 配置为携带MME Identifier信元。 |
| [**MOD MMECHARACT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/GTP-C接口管理/GnGp-SGSN_S10_S16_S3接口管理/MME属性/修改MME属性配置信息（MOD MMECHARACT）_26145958.md) | 是否携带MME Identifier信元 | YES（是） | 全网规划 | 配置为携带MME Identifier信元。 |
| [**ADD MSCPARA**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/GTP-C接口管理/Sv接口管理/MSC参数/增加MSC参数(ADD MSCPARA)_72225657.md) | IP地址类型 | IPV4 | 全网规划 | 配置MSC IP地址和MSC-Number之间的映射关系。 |
| [**ADD MSCPARA**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/GTP-C接口管理/Sv接口管理/MSC参数/增加MSC参数(ADD MSCPARA)_72225657.md) | MSC IPv4地址 | 10.65.39.80 | 全网规划 | 配置MSC IP地址和MSC-Number之间的映射关系。 |
| [**ADD MSCPARA**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/GTP-C接口管理/Sv接口管理/MSC参数/增加MSC参数(ADD MSCPARA)_72225657.md) | MSC-Number | 123456789 | 全网规划 | 配置MSC IP地址和MSC-Number之间的映射关系。 |
| [**SET DMCMPT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/信令传输管理/Diameter管理/Diameter协议接口兼容性配置/设置Diameter兼容性(SET DMCMPT)_26306080.md) | 是否支持AMF Instance ID信元（AMFID） | SUPPORT（支持） | 本端规划 | 配置Diameter兼容性参数，携带AMF Instance ID信元。<br>说明：系统会首先匹配<br>[**ADD DMCMPTBYIMSI**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/信令传输管理/Diameter管理/Diameter协议接口兼容性IMSI号段配置/增加IMSI对应的Diameter兼容性(ADD DMCMPTBYIMSI)_72225977.md)<br>命令的配置记录，若发现系统中不存在或不匹配<br>[**ADD DMCMPTBYIMSI**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/信令传输管理/Diameter管理/Diameter协议接口兼容性IMSI号段配置/增加IMSI对应的Diameter兼容性(ADD DMCMPTBYIMSI)_72225977.md)<br>命令的配置记录，才会匹配<br>[**SET DMCMPT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/信令传输管理/Diameter管理/Diameter协议接口兼容性配置/设置Diameter兼容性(SET DMCMPT)_26306080.md)<br>命令的配置记录。 |
| [**ADD DMCMPTBYIMSI**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/信令传输管理/Diameter管理/Diameter协议接口兼容性IMSI号段配置/增加IMSI对应的Diameter兼容性(ADD DMCMPTBYIMSI)_72225977.md) | SUBRANGE | IMSI_PREFIX（指定IMSI前缀） | 全网规划 | 配置Diameter兼容性参数，携带AMF Instance ID信元。<br>说明：系统会首先匹配<br>[**ADD DMCMPTBYIMSI**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/信令传输管理/Diameter管理/Diameter协议接口兼容性IMSI号段配置/增加IMSI对应的Diameter兼容性(ADD DMCMPTBYIMSI)_72225977.md)<br>命令的配置记录，若发现系统中不存在或不匹配<br>[**ADD DMCMPTBYIMSI**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/信令传输管理/Diameter管理/Diameter协议接口兼容性IMSI号段配置/增加IMSI对应的Diameter兼容性(ADD DMCMPTBYIMSI)_72225977.md)<br>命令的配置记录，才会匹配<br>[**SET DMCMPT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/信令传输管理/Diameter管理/Diameter协议接口兼容性配置/设置Diameter兼容性(SET DMCMPT)_26306080.md)<br>命令的配置记录。 |
| [**ADD DMCMPTBYIMSI**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/信令传输管理/Diameter管理/Diameter协议接口兼容性IMSI号段配置/增加IMSI对应的Diameter兼容性(ADD DMCMPTBYIMSI)_72225977.md) | IMSIPRE | 123456 | 全网规划 | 配置Diameter兼容性参数，携带AMF Instance ID信元。<br>说明：系统会首先匹配<br>[**ADD DMCMPTBYIMSI**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/信令传输管理/Diameter管理/Diameter协议接口兼容性IMSI号段配置/增加IMSI对应的Diameter兼容性(ADD DMCMPTBYIMSI)_72225977.md)<br>命令的配置记录，若发现系统中不存在或不匹配<br>[**ADD DMCMPTBYIMSI**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/信令传输管理/Diameter管理/Diameter协议接口兼容性IMSI号段配置/增加IMSI对应的Diameter兼容性(ADD DMCMPTBYIMSI)_72225977.md)<br>命令的配置记录，才会匹配<br>[**SET DMCMPT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/信令传输管理/Diameter管理/Diameter协议接口兼容性配置/设置Diameter兼容性(SET DMCMPT)_26306080.md)<br>命令的配置记录。 |
| [**ADD DMCMPTBYIMSI**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/信令传输管理/Diameter管理/Diameter协议接口兼容性IMSI号段配置/增加IMSI对应的Diameter兼容性(ADD DMCMPTBYIMSI)_72225977.md) | AMFID | SUPPORT（支持） | 本端规划 | 配置Diameter兼容性参数，携带AMF Instance ID信元。<br>说明：系统会首先匹配<br>[**ADD DMCMPTBYIMSI**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/信令传输管理/Diameter管理/Diameter协议接口兼容性IMSI号段配置/增加IMSI对应的Diameter兼容性(ADD DMCMPTBYIMSI)_72225977.md)<br>命令的配置记录，若发现系统中不存在或不匹配<br>[**ADD DMCMPTBYIMSI**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/信令传输管理/Diameter管理/Diameter协议接口兼容性IMSI号段配置/增加IMSI对应的Diameter兼容性(ADD DMCMPTBYIMSI)_72225977.md)<br>命令的配置记录，才会匹配<br>[**SET DMCMPT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/信令传输管理/Diameter管理/Diameter协议接口兼容性配置/设置Diameter兼容性(SET DMCMPT)_26306080.md)<br>命令的配置记录。 |

## [操作步骤](#ZH-CN_OPI_0170014699)

1. 进入 “MML命令行-UNC” 窗口。
2. **可选：**配置Diameter主机路由并将主机路由加入路由组。
  > **说明**
  > 如果在 [SLg接口配置](../../../../初始配置/UNC初始配置与调测/组网对接配置/配置AMF&MME&SGSN/配置MME/配置到E-SMLC的数据_29346481.md) 中已经完成Diameter路由配置，该步骤无需执行。
    a. 配置Diameter主机路由。
      [**ADD DMHOSTRT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/信令传输管理/Diameter管理/Diameter主机路由/增加Diameter主机路由(ADD DMHOSTRT)_26146272.md)
      > **说明**
      > 只有要添加的对端主机名在DMPE中未配置，才允许将 “目的实体选择方式” 配置为 “PEER_HOST_NAME（对端主机名）” 。
    b. 配置Diameter路由组。
      [**ADD DMRTGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/信令传输管理/Diameter管理/Diameter路由组/增加Diameter路由组(ADD DMRTGRP)_26146292.md)
      > **说明**
      > 当Diameter路由组应用于SLg接口，在MME上报位置信息给GMLC消息中必须携带对端主机名，因此要求该Diameter路由组只有主机路由且优选主机路由模式，并需要通过 [**ADD GMLCSELPLCY**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/LCS/GMLC选择策略/增加GMLC选择策略(ADD GMLCSELPLCY)_72225491.md) 配置引用关系。
3. 配置GMLC选择策略到GMLC选择策略组。
    a. 增加GMLC选择策略组。
      [**ADD GMLCSELGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/LCS/GMLC选择策略组/增加GMLC选择策略组(ADD GMLCSELGRP)_26145810.md)
    b. 增加GMLC选择策略。
      [**ADD GMLCSELPLCY**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/LCS/GMLC选择策略/增加GMLC选择策略(ADD GMLCSELPLCY)_72225491.md)

      > **说明**
      > GMLC选择策略组索引为 [**ADD GMLCSELPLCY**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/LCS/GMLC选择策略/增加GMLC选择策略(ADD GMLCSELPLCY)_72225491.md) 中的选择策略组索引号，Diameter路由组索引为 [**ADD DMRTGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/信令传输管理/Diameter管理/Diameter路由组/增加Diameter路由组(ADD DMRTGRP)_26146292.md) 配置的路由组索引号，并保证该路由组中只有主机路由，并且是优选主机路由模式。
4. 基于运营商打开紧急呼叫触发NI-LR的功能开关并配置相关流程策略。
  [**ADD LCSPARAEX**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/LCS/LCS扩展参数/增加LCS扩展参数(ADD LCSPARAEX)_26305624.md)
  > **说明**
  > GMLC选择策略组索引为 [**ADD GMLCSELGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/LCS/GMLC选择策略组/增加GMLC选择策略组(ADD GMLCSELGRP)_26145810.md) 的GMLC选择策略组索引。
5. **可选：**配置用户在ECM-IDLE态时，MME收到E-SMLC的Connection Oriented Information Transfer消息时触发Paging。
  [**SET LCSPARA**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/LCS/LCS软件参数表/设置LCS参数表记录(SET LCSPARA)_72225477.md)
  > **说明**
  > 应用于定位过程中，由于“user inactivity”导致用户进入ECM-IDLE态的场景。由于该配置为MT-LR和NI-LR公用，因此该配置也对MT-LR流程生效。
6. **可选：**根据实际场景判断配置MME Identifier、AMF Instance ID和MSC-Number信元的携带策略。
  在全网规划中，当网络中MME都支持该信元且上报策略都配置为“源侧上报”时，配置为携带AMF Instance ID/MME Identifier和MSC-Number信元。
    - 配置为携带MME Identifier后，在NI-LR流程中伴随紧急呼叫的Inter-MME Handover/Inter TAU场景下，新侧MME发送给老侧MME的Forward Relocation Response或Context Request消息中将包含MME Identifier信元，老侧MME再将该信息上报给GMLC。当GMLC再次发起MT-LR流程时，可以直接找到新侧MME。
      [**MOD MMECHARACT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/GTP-C接口管理/GnGp-SGSN_S10_S16_S3接口管理/MME属性/修改MME属性配置信息（MOD MMECHARACT）_26145958.md)
      > **说明**
      > 使用 [**ADD MMECHARACT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/GTP-C接口管理/GnGp-SGSN_S10_S16_S3接口管理/MME属性/增加MME属性配置信息（ADD MMECHARACT）_26305766.md) 还是 [**MOD MMECHARACT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/GTP-C接口管理/GnGp-SGSN_S10_S16_S3接口管理/MME属性/修改MME属性配置信息（MOD MMECHARACT）_26145958.md) 来修改MME属性，请根据参数 “对端设备范围” 是否已存在来确定。
    - 配置MSC IP和MSC-Number的映射关系后，在NI-LR流程中伴随紧急呼叫的SRVCC场景下，MME通过Subscriber Location Report消息将目标MSC的MSC-Number上报给GMLC。当GMLC再次发起MT-LR流程时，可以直接找到MSC。
      [**ADD MSCPARA**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/GTP-C接口管理/Sv接口管理/MSC参数/增加MSC参数(ADD MSCPARA)_72225657.md)
    - 配置为携带AMF Instance ID后，在NI-LR流程中伴随紧急呼叫的4G切换到5G场景下，源侧MME通过Subscirber Location Report消息将AMF Instance ID信元上报给GMLC。
      [**SET DMCMPT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/信令传输管理/Diameter管理/Diameter协议接口兼容性配置/设置Diameter兼容性(SET DMCMPT)_26306080.md)
      [**ADD DMCMPTBYIMSI**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/信令传输管理/Diameter管理/Diameter协议接口兼容性IMSI号段配置/增加IMSI对应的Diameter兼容性(ADD DMCMPTBYIMSI)_72225977.md)
      > **说明**
      > [**SET DMCMPT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/信令传输管理/Diameter管理/Diameter协议接口兼容性配置/设置Diameter兼容性(SET DMCMPT)_26306080.md) 与 [**ADD DMCMPTBYIMSI**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/信令传输管理/Diameter管理/Diameter协议接口兼容性IMSI号段配置/增加IMSI对应的Diameter兼容性(ADD DMCMPTBYIMSI)_72225977.md) 命令均可对Diameter兼容性参数进行配置。系统会首先匹配 [**ADD DMCMPTBYIMSI**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/信令传输管理/Diameter管理/Diameter协议接口兼容性IMSI号段配置/增加IMSI对应的Diameter兼容性(ADD DMCMPTBYIMSI)_72225977.md) 命令的配置记录，若发现系统中不存在或不匹配 [**ADD DMCMPTBYIMSI**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/信令传输管理/Diameter管理/Diameter协议接口兼容性IMSI号段配置/增加IMSI对应的Diameter兼容性(ADD DMCMPTBYIMSI)_72225977.md) 命令的配置记录，才会匹配 [**SET DMCMPT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/信令传输管理/Diameter管理/Diameter协议接口兼容性配置/设置Diameter兼容性(SET DMCMPT)_26306080.md) 命令的配置记录。
7. 打开特性开关。
  [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)

## [任务示例](#ZH-CN_OPI_0170014699)

任务描述

标准的LCS组网且网络不允许使用缺省承载进行紧急呼叫通话场景下，部署紧急呼叫NI-LR定位功能。

脚本

// 进入 “MML命令行-UNC” 窗口。

//（可选）配置到GMLC的Diameter路由。

//增加Diameter主机路由。

```
ADD DMHOSTRT: ROUTEIDX=2, APPNAM=SLG, RSELMODE=SELMODE_MASTER_SLAVE, PEERSEL=PEER_INDEX, PEERIDX=1;
```

//增加Diameter路由组。

```
ADD DMRTGRP: GRPIDX=1, RTMODE=HOST_ROUTE, RTPRIMODE=HOST_ROUTE_PREFER, ROUTEIDX=2, ROUTEGRPNAM="GMLC";
```

//配置GMLC选择策略。

//增加GMLC选择策略组。

```
ADD GMLCSELGRP: GMLCGRPID=6;
```

//增加GMLC选择策略。

```
ADD GMLCSELPLCY: GMLCGRPID=6, LCSCLIENTTYPE=EMERGENCY_SERVICES, LOCATIONTYPE=ECI, ECIBEGIN=3, ECIEND=16, REALMNAME="gmlc.epc.mnc456.mcc123.3gppnetwork.org", GRPIDX=1;
```

//基于运营商打开紧急呼叫触发的NI-LR流程开关，并配置流程策略。

```
ADD LCSPARAEX: NOID=46, NILRSWITCH=ON, GMLCGRPID=1, RPTTYPE=IMMEDIATELY-0&LOCATE-1, SPTDFTBRCALL=NO, HORPTTYPE=SOURCE;
```

//(可选)设置在定位过程中，由于“user inactivity”导致用户进入ECM-IDLE态场景下，MME收到E-SMLC的Connection Oriented Information Transfer消息时触发Paging。

```
SET LCSPARA: IDLEPAGING=YES;
```

//(可选)根据实际场景判断配置MME Identifier信元的携带策略。

```
MOD MMECHARACT: RANGE=ALL_MME, MMEIDIE=YES;
```

//(可选)根据实际场景判断配置MSC-Number信元的携带策略。

```
ADD MSCPARA: IPTYPE=IPV4, IPV4="10.65.39.80", MSCNUM="123456789";
```

//(可选)根据实际场景判断配置AMF Instance ID信元的携带策略。

```
SET DMCMPT: AMFID=SUPPORT; 
ADD DMCMPTBYIMSI: SUBRANGE=IMSI_PREFIX, IMSIPRE="123456", AMFID=SUPPORT;
```

//打开VoLTE紧急呼叫定位（NI-LR）的License配置开关。

```
SET LICENSESWITCH: LICITEM="LKV2NVEC01", SWITCH=ENABLE;
```
