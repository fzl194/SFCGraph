# 激活基于服务PLMN的NB-IoT终端接入速率控制（MME）

- [操作场景](#ZH-CN_OPI_0276026860__1.3.1)
- [必备事项](#ZH-CN_OPI_0276026860__1.3.2)
- [操作步骤](#ZH-CN_OPI_0276026860__1.3.3)
- [任务示例](#ZH-CN_OPI_0276026860__1.3.4)

## [操作场景](#ZH-CN_OPI_0276026860)

本操作指导介绍在运行网络中激活基于服务PLMN的NB-IoT终端接入速率控制的操作过程。

本特性通过MME向网关及M2M终端发送Serving PLMN Rate Control信元，以用户粒度对M2M终端进行上下行速率控制，预防系统进入拥塞状态。

> **说明**
> 适用于MME。

## [必备事项](#ZH-CN_OPI_0276026860)

前提条件

- 请仔细阅读[WSFD-215205 基于服务PLMN的NB-IoT终端接入速率控制特性概述（MME）](特性概述_75873439.md)。
- 已完成加载License。

数据

*表1 需要准备的数据*

| 类别 | 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- | --- |
| [**ADD M2MPLCY**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/M2M管理/M2M策略参数配置/增加M2M策略参数(ADD M2MPLCY)_72225443.md) | [**ADD M2MPLCY**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/M2M管理/M2M策略参数配置/增加M2M策略参数(ADD M2MPLCY)_72225443.md) | 用户范围（SUBRANGE） | IMSI_PREFIX | 全网规划 | 增加M2M策略参数 |
| [**ADD M2MPLCY**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/M2M管理/M2M策略参数配置/增加M2M策略参数(ADD M2MPLCY)_72225443.md) | [**ADD M2MPLCY**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/M2M管理/M2M策略参数配置/增加M2M策略参数(ADD M2MPLCY)_72225443.md) | IMSI前缀（IMSIPRE） | 12303 | 全网规划 | 增加M2M策略参数 |
| [**ADD M2MPLCY**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/M2M管理/M2M策略参数配置/增加M2M策略参数(ADD M2MPLCY)_72225443.md) | [**ADD M2MPLCY**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/M2M管理/M2M策略参数配置/增加M2M策略参数(ADD M2MPLCY)_72225443.md) | APNNI（APNNI） | HUAWEI.COM | 全网规划 | 增加M2M策略参数 |
| [**ADD M2MPLCY**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/M2M管理/M2M策略参数配置/增加M2M策略参数(ADD M2MPLCY)_72225443.md) | [**ADD M2MPLCY**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/M2M管理/M2M策略参数配置/增加M2M策略参数(ADD M2MPLCY)_72225443.md) | CP优化功能（CPOPSW） | SUPPORT | 全网规划 | 增加M2M策略参数 |
| [**ADD M2MPLCY**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/M2M管理/M2M策略参数配置/增加M2M策略参数(ADD M2MPLCY)_72225443.md) | [**ADD M2MPLCY**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/M2M管理/M2M策略参数配置/增加M2M策略参数(ADD M2MPLCY)_72225443.md) | CP上行数据包数（UPRATECTL） | 10 | 全网规划 | 增加M2M策略参数 |
| [**ADD M2MPLCY**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/M2M管理/M2M策略参数配置/增加M2M策略参数(ADD M2MPLCY)_72225443.md) | [**ADD M2MPLCY**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/M2M管理/M2M策略参数配置/增加M2M策略参数(ADD M2MPLCY)_72225443.md) | CP下行数据包数（DOWNRATECTL） | 10 | 全网规划 | 增加M2M策略参数 |
| [**ADD GTPCV2CMPT**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/GTP-C接口管理/GTP-C协议管理/GTP-C V2协议兼容性/增加GTP-C V2协议兼容性(ADD GTPCV2CMPT)_26305734.md) | [**ADD GTPCV2CMPT**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/GTP-C接口管理/GTP-C协议管理/GTP-C V2协议兼容性/增加GTP-C V2协议兼容性(ADD GTPCV2CMPT)_26305734.md) | 索引（IDX） | 0 | 全网规划 | 添加GTP-C V2协议兼容性 |
| [**ADD GTPCV2CMPT**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/GTP-C接口管理/GTP-C协议管理/GTP-C V2协议兼容性/增加GTP-C V2协议兼容性(ADD GTPCV2CMPT)_26305734.md) | [**ADD GTPCV2CMPT**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/GTP-C接口管理/GTP-C协议管理/GTP-C V2协议兼容性/增加GTP-C V2协议兼容性(ADD GTPCV2CMPT)_26305734.md) | 消息分类（MSGCLS） | TM | 全网规划 | 添加GTP-C V2协议兼容性 |
| [**ADD GTPCV2CMPT**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/GTP-C接口管理/GTP-C协议管理/GTP-C V2协议兼容性/增加GTP-C V2协议兼容性(ADD GTPCV2CMPT)_26305734.md) | [**ADD GTPCV2CMPT**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/GTP-C接口管理/GTP-C协议管理/GTP-C V2协议兼容性/增加GTP-C V2协议兼容性(ADD GTPCV2CMPT)_26305734.md) | 消息类型（TMMSGTYPE） | CRT_SES_REQ | 全网规划 | 添加GTP-C V2协议兼容性 |
| [**ADD GTPCV2CMPT**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/GTP-C接口管理/GTP-C协议管理/GTP-C V2协议兼容性/增加GTP-C V2协议兼容性(ADD GTPCV2CMPT)_26305734.md) | [**ADD GTPCV2CMPT**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/GTP-C接口管理/GTP-C协议管理/GTP-C V2协议兼容性/增加GTP-C V2协议兼容性(ADD GTPCV2CMPT)_26305734.md) | Create Session Request的信元类型（CRTSESREQ） | INDICATION | 全网规划 | 添加GTP-C V2协议兼容性 |
| [**ADD GTPCV2CMPT**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/GTP-C接口管理/GTP-C协议管理/GTP-C V2协议兼容性/增加GTP-C V2协议兼容性(ADD GTPCV2CMPT)_26305734.md) | [**ADD GTPCV2CMPT**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/GTP-C接口管理/GTP-C协议管理/GTP-C V2协议兼容性/增加GTP-C V2协议兼容性(ADD GTPCV2CMPT)_26305734.md) | Indication Bit位（CRTSESREQIND） | CPOPCI-1 | 全网规划 | 添加GTP-C V2协议兼容性 |

## [操作步骤](#ZH-CN_OPI_0276026860)

1. 进入 “MML命令行-UNC” 窗口。
2. 设置基于服务PLMN的NB-IoT终端接入速率控制参数。
  [**ADD M2MPLCY**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/M2M管理/M2M策略参数配置/增加M2M策略参数(ADD M2MPLCY)_72225443.md)
  > **说明**
  > 当 [**SET M2MCTRL**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/M2M管理/M2M控制参数/设置M2M控制参数(SET M2MCTRL)_72345369.md) 开启“NB-IoT用户支持多PDN连接”功能时，UE下不同APN配置的速率控制参数必须保持一致。
3. 配置GTP-C V2协议兼容性，MME在Create Session Request以及Context Response消息中支持携带CPOCPI标志位。
  [**ADD GTPCV2CMPT**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/GTP-C接口管理/GTP-C协议管理/GTP-C V2协议兼容性/增加GTP-C V2协议兼容性(ADD GTPCV2CMPT)_26305734.md)
  [**ADD GTPCV2CMPT**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/GTP-C接口管理/GTP-C协议管理/GTP-C V2协议兼容性/增加GTP-C V2协议兼容性(ADD GTPCV2CMPT)_26305734.md)
4. 打开本特性的License配置开关。
  [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)

## [任务示例](#ZH-CN_OPI_0276026860)

任务描述

某物联网行业用户的M2M终端出现故障时，终端在短时间内高频率地向网络发送业务数据包，可能会导致网络拥塞。此时建议开启本特性来缓解网络负荷、预防网络拥塞。

脚本

//设置基于服务PLMN的NB-IoT终端接入速率控制参数。

```
ADD M2MPLCY: SUBRANGE=IMSI_PREFIX, IMSIPRE="12303", APNNI="HUAWEI.COM", CPOPSW=SUPPORT, UPRATECTL=10, DOWNRATECTL=10;
```

//配置GTP-C V2协议兼容性，MME在Create Session Request以及Context Response消息中支持携带CPOCPI标志位。

```
ADD GTPCV2CMPT: IDX=1, MSGCLS=TM, TMMSGTYPE=CRT_SES_REQ, CRTSESREQ=INDICATION, CRTSESREQIND=CPOPCI-1;
ADD GTPCV2CMPT: IDX=2, MSGCLS=MM, MMMSGTYPE=CTX_RSP, CTXRSP=INDICATION, CTXRSPIND=CPOPCI-1;
```

//打开本特性的License配置开关。

```
SET LICENSESWITCH: LICITEM="LKV2SARC01", SWITCH=ENABLE;
```
