# 激活 NSA(Opt.3)双连接管理

- [操作场景](#ZH-CN_OPI_0193270612__1.3.1)
- [必备事项](#ZH-CN_OPI_0193270612__1.3.2)
- [操作步骤](#ZH-CN_OPI_0193270612__1.3.3)
- [任务示例](#ZH-CN_OPI_0193270612__1.3.4)

## [操作场景](#ZH-CN_OPI_0193270612)

本操作指导介绍在运行网络中激活 NSA(Opt.3)双连接管理 的操作过程。

> **说明**
> 适用于MME。

## [必备事项](#ZH-CN_OPI_0193270612)

前提条件

- 请仔细阅读[WSFD-011502 NSA(Opt.3)双连接管理](../WSFD-011502 NSA(Opt.3)双连接管理_93270610.md)。

数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| [**SET S1CMPT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/S1接口管理/S1接口兼容性/设置S1接口兼容性(SET S1CMPT)_72345837.md) | 是否携带NR UE Security Capabilities信元（NRSEC） | YES | 全网规划 | 配置安全协商相关信元的携带情况 |
| [**SET NSACTRL**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/网络管理/NSA组网管理/NSA控制参数/设置NSA控制参数(SET NSACTRL)_26305942.md) | NR流量上报（NRUSERPT） | YES | 全网规划 | 配置流量上报策略 |
| [**ADD SGWCHARACT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/GTP-C接口管理/S11接口管理/S-GW属性/增加S-GW特性对接配置(ADD SGWCHARACT)_26305778.md) | 对端设备范围（RANGE） | SPECIFIED | 全网规划 | 配置流量上报策略 |
| [**ADD SGWCHARACT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/GTP-C接口管理/S11接口管理/S-GW属性/增加S-GW特性对接配置(ADD SGWCHARACT)_26305778.md) | IP地址类型（IPT） | IPV4 | 全网规划 | 配置流量上报策略 |
| [**ADD SGWCHARACT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/GTP-C接口管理/S11接口管理/S-GW属性/增加S-GW特性对接配置(ADD SGWCHARACT)_26305778.md) | IPV4地址（IPV4） | 10.10.10.10 | 全网规划 | 配置流量上报策略 |
| [**ADD SGWCHARACT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/GTP-C接口管理/S11接口管理/S-GW属性/增加S-GW特性对接配置(ADD SGWCHARACT)_26305778.md) | IPV4地址掩码（IPV4MSK） | 255.255.255.0 | 全网规划 | 配置流量上报策略 |
| [**ADD SGWCHARACT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/GTP-C接口管理/S11接口管理/S-GW属性/增加S-GW特性对接配置(ADD SGWCHARACT)_26305778.md) | S-GW支持Secondary RAT Usage Data Report（SECRATRPT） | YES | 全网规划 | 配置流量上报策略 |
| [**ADD SGWCHARACT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/GTP-C接口管理/S11接口管理/S-GW属性/增加S-GW特性对接配置(ADD SGWCHARACT)_26305778.md) | 描述（DESC） | noname | 本端规划 | 配置流量上报策略 |
| [**ADD MMECHARACT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/GTP-C接口管理/GnGp-SGSN_S10_S16_S3接口管理/MME属性/增加MME属性配置信息（ADD MMECHARACT）_26305766.md) | 对端设备范围（RANGE） | SPECIAL_MME | 全网规划 | 配置流量上报策略 |
| [**ADD MMECHARACT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/GTP-C接口管理/GnGp-SGSN_S10_S16_S3接口管理/MME属性/增加MME属性配置信息（ADD MMECHARACT）_26305766.md) | IP地址类型（IPTYPE） | IPV4 | 全网规划 | 配置流量上报策略 |
| [**ADD MMECHARACT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/GTP-C接口管理/GnGp-SGSN_S10_S16_S3接口管理/MME属性/增加MME属性配置信息（ADD MMECHARACT）_26305766.md) | MME IPv4信令面地址（IPV4） | 10.20.10.13 | 全网规划 | 配置流量上报策略 |
| [**ADD MMECHARACT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/GTP-C接口管理/GnGp-SGSN_S10_S16_S3接口管理/MME属性/增加MME属性配置信息（ADD MMECHARACT）_26305766.md) | IPv4掩码（MASKV4） | 255.255.255.0 | 全网规划 | 配置流量上报策略 |
| [**ADD MMECHARACT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/GTP-C接口管理/GnGp-SGSN_S10_S16_S3接口管理/MME属性/增加MME属性配置信息（ADD MMECHARACT）_26305766.md) | 是否携带Secondary RAT Usage Data Report信元（SECRATRPT） | YES | 全网规划 | 配置流量上报策略 |
| [**ADD MMECHARACT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/GTP-C接口管理/GnGp-SGSN_S10_S16_S3接口管理/MME属性/增加MME属性配置信息（ADD MMECHARACT）_26305766.md) | 描述（DESC） | noname | 全网规划 | 配置流量上报策略 |
| [**ADD MMECHARACT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/GTP-C接口管理/GnGp-SGSN_S10_S16_S3接口管理/MME属性/增加MME属性配置信息（ADD MMECHARACT）_26305766.md) | 对端设备范围（RANGE） | SPECIAL_MME | 全网规划 | 配置Inter流程中对等网元间NSA用户信息传递策略。 |
| [**ADD MMECHARACT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/GTP-C接口管理/GnGp-SGSN_S10_S16_S3接口管理/MME属性/增加MME属性配置信息（ADD MMECHARACT）_26305766.md) | IP地址类型（IPTYPE） | IPV4 | 全网规划 | 配置Inter流程中对等网元间NSA用户信息传递策略。 |
| [**ADD MMECHARACT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/GTP-C接口管理/GnGp-SGSN_S10_S16_S3接口管理/MME属性/增加MME属性配置信息（ADD MMECHARACT）_26305766.md) | MME IPv4信令面地址（IPV4） | 10.20.10.13 | 全网规划 | 配置Inter流程中对等网元间NSA用户信息传递策略。 |
| [**ADD MMECHARACT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/GTP-C接口管理/GnGp-SGSN_S10_S16_S3接口管理/MME属性/增加MME属性配置信息（ADD MMECHARACT）_26305766.md) | IPv4掩码（MASKV4） | 255.255.255.0 | 全网规划 | 配置Inter流程中对等网元间NSA用户信息传递策略。 |
| [**ADD MMECHARACT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/GTP-C接口管理/GnGp-SGSN_S10_S16_S3接口管理/MME属性/增加MME属性配置信息（ADD MMECHARACT）_26305766.md) | 是否携带扩展接入限制数据（EXTARD） | YES | 全网规划 | 配置Inter流程中对等网元间NSA用户信息传递策略。 |
| [**ADD MMECHARACT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/GTP-C接口管理/GnGp-SGSN_S10_S16_S3接口管理/MME属性/增加MME属性配置信息（ADD MMECHARACT）_26305766.md) | 是否携带UE附加安全能力（UEASECCAP） | YES | 全网规划 | 配置Inter流程中对等网元间NSA用户信息传递策略。 |
| [**ADD MMECHARACT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/GTP-C接口管理/GnGp-SGSN_S10_S16_S3接口管理/MME属性/增加MME属性配置信息（ADD MMECHARACT）_26305766.md) | 是否限制最大速率（BITRATE） | NO | 全网规划 | 配置Inter流程中对等网元间NSA用户信息传递策略。 |
| [**ADD SGSNCHARACT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/GTP-C接口管理/GnGp-SGSN_S10_S16_S3接口管理/GnGp SGSN属性/增加GnGp SGSN属性配置信息(ADD SGSNCHARACT)_72225633.md) | 对端设备范围（RANGE） | SPECIAL_SGSN | 全网规划 | 配置Inter流程中对等网元间NSA用户信息传递策略。 |
| [**ADD SGSNCHARACT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/GTP-C接口管理/GnGp-SGSN_S10_S16_S3接口管理/GnGp SGSN属性/增加GnGp SGSN属性配置信息(ADD SGSNCHARACT)_72225633.md) | IP地址类型（IPT） | IPV4 | 全网规划 | 配置Inter流程中对等网元间NSA用户信息传递策略。 |
| [**ADD SGSNCHARACT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/GTP-C接口管理/GnGp-SGSN_S10_S16_S3接口管理/GnGp SGSN属性/增加GnGp SGSN属性配置信息(ADD SGSNCHARACT)_72225633.md) | SGSN IPv4信令面地址（IPV4） | 10.20.10.14 | 全网规划 | 配置Inter流程中对等网元间NSA用户信息传递策略。 |
| [**ADD SGSNCHARACT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/GTP-C接口管理/GnGp-SGSN_S10_S16_S3接口管理/GnGp SGSN属性/增加GnGp SGSN属性配置信息(ADD SGSNCHARACT)_72225633.md) | 掩码（MASKV4） | 255.255.255.0 | 全网规划 | 配置Inter流程中对等网元间NSA用户信息传递策略。 |
| [**ADD SGSNCHARACT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/GTP-C接口管理/GnGp-SGSN_S10_S16_S3接口管理/GnGp SGSN属性/增加GnGp SGSN属性配置信息(ADD SGSNCHARACT)_72225633.md) | 是否携带扩展接入限制数据（ARD） | YES | 全网规划 | 配置Inter流程中对等网元间NSA用户信息传递策略。 |

## [操作步骤](#ZH-CN_OPI_0193270612)

1. 进入 “MML命令行-UNC” 窗口。
2. 配置安全协商相关信元的携带情况。
  [**SET S1CMPT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/S1接口管理/S1接口兼容性/设置S1接口兼容性(SET S1CMPT)_72345837.md)
3. 配置流量上报策略。
    a. 设置MME支持NR流量上报功能。
      [**SET NSACTRL**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/网络管理/NSA组网管理/NSA控制参数/设置NSA控制参数(SET NSACTRL)_26305942.md)
    b. 设置给SGW携带Secondary RAT Usage Data Report信元。
      [**ADD SGWCHARACT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/GTP-C接口管理/S11接口管理/S-GW属性/增加S-GW特性对接配置(ADD SGWCHARACT)_26305778.md)
    c. **可选：**设置给对端MME携带Secondary RAT Usage Data Report信元。如果对端网元支持NSA用户数据报告上报功能且支持处理Secondary RAT Usage Data Report信元时执行此步骤。
      [**ADD MMECHARACT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/GTP-C接口管理/GnGp-SGSN_S10_S16_S3接口管理/MME属性/增加MME属性配置信息（ADD MMECHARACT）_26305766.md)
4. 配置Inter流程中对等网元间NSA用户信息传递策略。
  [**ADD MMECHARACT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/GTP-C接口管理/GnGp-SGSN_S10_S16_S3接口管理/MME属性/增加MME属性配置信息（ADD MMECHARACT）_26305766.md)
  [**ADD SGSNCHARACT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/GTP-C接口管理/GnGp-SGSN_S10_S16_S3接口管理/GnGp SGSN属性/增加GnGp SGSN属性配置信息(ADD SGSNCHARACT)_72225633.md)

## [任务示例](#ZH-CN_OPI_0193270612)

任务描述

激活 NSA(Opt.3)双连接管理 特性。

脚本

//配置S1接口兼容性。

```
SET S1CMPT: NRSEC=YES;
```

//配置MME启动NR流量上报功能。

```
SET NSACTRL: NRUSERPT=YES; 
```

//设置给SGW携带Secondary RAT Usage Data Report信元。

```
ADD SGWCHARACT: RANGE=SPECIFIED, IPT=IPV4, IPV4="10.10.10.10", IPV4MSK="255.255.255.0", SECRATRPT=YES;
```

//设置给MME携带Secondary RAT Usage Data Report信元。

```
ADD MMECHARACT: RANGE=SPECIAL_MME, IPTYPE=IPV4, IPV4="10.20.10.13", MASKV4="255.255.255.0", SECRATRPT=YES;
```

//配置Inter流程中对等网元间DCNR信息传递策略。

```
ADD MMECHARACT: RANGE=SPECIAL_MME, IPTYPE=IPV4, IPV4="10.20.10.15", MASKV4="255.255.255.0", EXTARD=YES, UEASECCAP=YES, BITRATE=NO;
```

```
ADD SGSNCHARACT: RANGE=SPECIAL_SGSN, IPT=IPV4, IPV4="10.20.10.14", MASKV4="255.255.255.0", ARD=YES;
```
