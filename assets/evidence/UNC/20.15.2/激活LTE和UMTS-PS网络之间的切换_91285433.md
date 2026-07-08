# 激活LTE和UMTS PS网络之间的切换

- [操作场景](#ZH-CN_OPI_0191285433__1.3.1)
- [必备事项](#ZH-CN_OPI_0191285433__1.3.2)
- [操作流程](#ZH-CN_OPI_0191285433__1.3.3)
- [操作步骤](#ZH-CN_OPI_0191285433__1.3.4)
- [任务示例](#ZH-CN_OPI_0191285433__1.3.5)

## [操作场景](#ZH-CN_OPI_0191285433)

本操作指导介绍在运行网络中激活LTE和UMTS PS网络之间的切换特性的操作过程。

- LTE到UMTS PS网络的切换
  UMTS与LTE共存的情况下，UE在LTE网络进行业务，当UMTS网络的覆盖（信号）优于LTE网络时，或者在eNodeB负荷较重等情况下，eNodeB会触发UE切换到UMTS网络。
- UMTS到LTE网络的切换
  UMTS与LTE共存的情况下，UE在UMTS网络进行业务，当UE移动到LTE覆盖范围等情况下，RNC可能会触发UE切换到LTE网络，以便为UE提供更好的服务。
  > **说明**
  > 适用于 SGSN、 GGSN、 MME、SGW-C、PGW-C。

## [必备事项](#ZH-CN_OPI_0191285433)

前提条件

- 请仔细阅读[WSFD-104503 LTE和UMTS PS网络之间的切换特性概述](特性概述_91532261.md)。
- 完成加载License。

数据

| 类别 | 参数 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| [**SET PESELPLCY**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/GTP-C接口管理/GnGp-SGSN_S10_S16_S3接口管理/SGSN MME选择/设置SGSN_MME选择策略（SET PESELPLCY）_72225643.md) | 对等网元识别模式（PEIDMODE） | SECTION_MODE | 全网规划 | 对端网元识别参数 |
| [**SET PESELPLCY**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/GTP-C接口管理/GnGp-SGSN_S10_S16_S3接口管理/SGSN MME选择/设置SGSN_MME选择策略（SET PESELPLCY）_72225643.md) | 比特掩码（BITMASK） | 0x8000 | 全网规划 | 对端网元识别参数 |
| [**SET PESELPLCY**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/GTP-C接口管理/GnGp-SGSN_S10_S16_S3接口管理/SGSN MME选择/设置SGSN_MME选择策略（SET PESELPLCY）_72225643.md) | MME Group ID（MMEGI） | 0x1000 | 全网规划 | 对端网元识别参数 |
| [**SET PESELPLCY**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/GTP-C接口管理/GnGp-SGSN_S10_S16_S3接口管理/SGSN MME选择/设置SGSN_MME选择策略（SET PESELPLCY）_72225643.md) | MME Group ID范围（MMEGIRANGE） | 0x1088 | 全网规划 | 对端网元识别参数 |
| [**SET PESELPLCY**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/GTP-C接口管理/GnGp-SGSN_S10_S16_S3接口管理/SGSN MME选择/设置SGSN_MME选择策略（SET PESELPLCY）_72225643.md) | 使用RNC ID域名（RNCID） | NO | 全网规划 | 对端网元识别参数 |
| [**ADD DNSS**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/GTP-C接口管理/DNS/DNS服务器管理/增加DNS服务器(ADD DNSS)_72345497.md) | IP 地址（IP） | 172.28.1.33、172.28.2.33、172.29.3.10 | 全网规划 | DNS服务器数据 |
| [**ADD DNSS**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/GTP-C接口管理/DNS/DNS服务器管理/增加DNS服务器(ADD DNSS)_72345497.md) | 域名服务器优先级（PRI） | PRI1、PRI2、PRI3 | 全网规划 | DNS服务器数据 |
| [**ADD IPV4DNSH**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/GTP-C接口管理/DNS/DNS Hostfile管理/增加IPV4 DNS Hostfile记录(ADD IPV4DNSH)_26145884.md) | Host Name索引（HSINDEX） | 1 | 全网规划 | A解析数据 |
| [**ADD IPV4DNSH**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/GTP-C接口管理/DNS/DNS Hostfile管理/增加IPV4 DNS Hostfile记录(ADD IPV4DNSH)_26145884.md) | 主机名（HOSTNAME） | RAC0000.LAC2302.MNC0000.MCC0123.GPRS | 全网规划 | A解析数据 |
| [**ADD IPV4DNSH**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/GTP-C接口管理/DNS/DNS Hostfile管理/增加IPV4 DNS Hostfile记录(ADD IPV4DNSH)_26145884.md) | IPv4地址1（IPV4ADDR1） | 172.25.6.53 | 全网规划 | A解析数据 |
| [**ADD IPV4DNSH**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/GTP-C接口管理/DNS/DNS Hostfile管理/增加IPV4 DNS Hostfile记录(ADD IPV4DNSH)_26145884.md) | 地址区间号（ADDRSECTION） | SECTION1 | 全网规划 | A解析数据 |
| [**ADD DNSN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/GTP-C接口管理/DNS/DNS NAPTR管理/增加DNS NAPTR记录(ADD DNSN)_72225569.md) | 域名（FQDN） | MMEC12.MMEGI8001.MME.EPC.MNC000.MCC123.3GPPNETWORK.ORG | 全网规划 | NAPTR解析数据 |
| [**ADD DNSN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/GTP-C接口管理/DNS/DNS NAPTR管理/增加DNS NAPTR记录(ADD DNSN)_72225569.md) | 网元类型（ENTITY） | MME | 全网规划 | NAPTR解析数据 |
| [**ADD DNSN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/GTP-C接口管理/DNS/DNS NAPTR管理/增加DNS NAPTR记录(ADD DNSN)_72225569.md) | 接口类型（INTYPE） | Gn | 全网规划 | NAPTR解析数据 |
| [**ADD DNSN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/GTP-C接口管理/DNS/DNS NAPTR管理/增加DNS NAPTR记录(ADD DNSN)_72225569.md) | 优先级（PRIORITY） | 1 | 全网规划 | NAPTR解析数据 |
| [**ADD DNSN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/GTP-C接口管理/DNS/DNS NAPTR管理/增加DNS NAPTR记录(ADD DNSN)_72225569.md) | 权重（WEIGHT） | 150 | 全网规划 | NAPTR解析数据 |
| [**ADD DNSN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/GTP-C接口管理/DNS/DNS NAPTR管理/增加DNS NAPTR记录(ADD DNSN)_72225569.md) | 主机名索引（HSINDEX） | 2 | 全网规划 | NAPTR解析数据 |
| [**SET COMPATIBILITY**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/QoS兼容性管理/QoS兼容性配置/设置QoS兼容性配置(SET COMPATIBILITY)_72345835.md) | H值（HARP） | 5 | 全网规划 | 配置EPS QoS和GPRS QoS的ARP参数转换规则 |
| [**SET COMPATIBILITY**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/QoS兼容性管理/QoS兼容性配置/设置QoS兼容性配置(SET COMPATIBILITY)_72345835.md) | M值（MARP） | 10 | 全网规划 | 配置EPS QoS和GPRS QoS的ARP参数转换规则 |
| [**SET R8QOSMAP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/QoS兼容性管理/EPS QoS参数到Pre-R8 QoS参数映射/设置EPS QoS参数到Pre-R8 QoS参数映射规则（SET R8QOSMAP）_26146234.md) | QoS 级别标识（QCI） | 9 | 全网规划 | EPS QoS参数到Pre-R8 QoS参数映射规则 |
| [**SET R8QOSMAP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/QoS兼容性管理/EPS QoS参数到Pre-R8 QoS参数映射/设置EPS QoS参数到Pre-R8 QoS参数映射规则（SET R8QOSMAP）_26146234.md) | 流量等级（TC） | CC | 全网规划 | EPS QoS参数到Pre-R8 QoS参数映射规则 |
| [**SET R8QOSMAP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/QoS兼容性管理/EPS QoS参数到Pre-R8 QoS参数映射/设置EPS QoS参数到Pre-R8 QoS参数映射规则（SET R8QOSMAP）_26146234.md) | 最大SDU长度（MAXSDU） | 150 | 全网规划 | EPS QoS参数到Pre-R8 QoS参数映射规则 |
| [**SET R8QOSMAP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/QoS兼容性管理/EPS QoS参数到Pre-R8 QoS参数映射/设置EPS QoS参数到Pre-R8 QoS参数映射规则（SET R8QOSMAP）_26146234.md) | 发送次序（DO） | ORDER | 全网规划 | EPS QoS参数到Pre-R8 QoS参数映射规则 |
| [**SET R8QOSMAP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/QoS兼容性管理/EPS QoS参数到Pre-R8 QoS参数映射/设置EPS QoS参数到Pre-R8 QoS参数映射规则（SET R8QOSMAP）_26146234.md) | 发送错误SDU（DESDU） | NOT_DETECT | 全网规划 | EPS QoS参数到Pre-R8 QoS参数映射规则 |
| [**SET R8QOSMAP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/QoS兼容性管理/EPS QoS参数到Pre-R8 QoS参数映射/设置EPS QoS参数到Pre-R8 QoS参数映射规则（SET R8QOSMAP）_26146234.md) | 保留BER（RBER） | E_RESIDUAL_BIT_ERR_RATIO_7 | 全网规划 | EPS QoS参数到Pre-R8 QoS参数映射规则 |
| [**SET R8QOSMAP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/QoS兼容性管理/EPS QoS参数到Pre-R8 QoS参数映射/设置EPS QoS参数到Pre-R8 QoS参数映射规则（SET R8QOSMAP）_26146234.md) | SDU误码率（SDUER） | SDUER4 | 全网规划 | EPS QoS参数到Pre-R8 QoS参数映射规则 |
| [**SET R8QOSMAP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/QoS兼容性管理/EPS QoS参数到Pre-R8 QoS参数映射/设置EPS QoS参数到Pre-R8 QoS参数映射规则（SET R8QOSMAP）_26146234.md) | 发送控制优先级（THPRI） | THPRI1 | 全网规划 | EPS QoS参数到Pre-R8 QoS参数映射规则 |
| [**SET R8QOSMAP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/QoS兼容性管理/EPS QoS参数到Pre-R8 QoS参数映射/设置EPS QoS参数到Pre-R8 QoS参数映射规则（SET R8QOSMAP）_26146234.md) | 传递时延（TD） | 10 | 全网规划 | EPS QoS参数到Pre-R8 QoS参数映射规则 |
| [**SET SMFUNC**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/会话管理/SM扩展功能管理/设置会话管理扩展功能(SET SMFUNC)_26145684.md) | 强制启动间接转发方式（INDFWD） | YES | 全网规划 | 切换流程中的数据转发模式 |

## [操作流程](#ZH-CN_OPI_0191285433)

激活LTE和UMTS PS网络之间的切换操作流程如 [图1](#ZH-CN_OPI_0191285433__zh-cn_opi_0130428818_fig_01) 所示。

**图1** 激活LTE和UMTS PS网络之间的切换操作流程

<br>

![](激活LTE和UMTS PS网络之间的切换_91285433.assets/zh-cn_image_0191288961_2.png)

## [操作步骤](#ZH-CN_OPI_0191285433)

1. 进入 “MML命令行-UNC” 窗口。
2. 打开本特性的License配置开关。
  [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
3. （可选）配置在切换流程中是否使用RNC ID域名进行查询。如果不使用RNC ID域名，系统会组装RAI域名进行查询。
  [**SET PESELPLCY**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/GTP-C接口管理/GnGp-SGSN_S10_S16_S3接口管理/SGSN MME选择/设置SGSN_MME选择策略（SET PESELPLCY）_72225643.md) 命令主要适用于重选流程，仅仅“使用RNC ID域名”参数对切换流程域名组装有影响。
  [**SET PESELPLCY**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/GTP-C接口管理/GnGp-SGSN_S10_S16_S3接口管理/SGSN MME选择/设置SGSN_MME选择策略（SET PESELPLCY）_72225643.md)
4. 配置到DNS的数据，进行对端网元寻址。
    - 使用DNS服务器。具体配置请参见[配置DNS服务器的数据](../../../../初始配置/UNC初始配置与调测/组网对接配置/配置AMF&MME&SGSN/配置AMF/配置到DNS相关数据_82467040.md)。
    - 不使用DNS服务器，使用本地的DNS Hostfile。具体配置请参见[配置Hostfile的数据](../../../../初始配置/UNC初始配置与调测/组网对接配置/配置AMF&MME&SGSN/配置AMF/配置到DNS相关数据_82467040.md)。
5. **可选：**配置QoS参数转换规则。
    - 配置EPS QoS和GPRS QoS的ARP参数转换规则。
      [**SET COMPATIBILITY**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/QoS兼容性管理/QoS兼容性配置/设置QoS兼容性配置(SET COMPATIBILITY)_72345835.md)
    - 配置EPS QoS和GPRS QoS的QCI参数转换规则。
      [**SET R8QOSMAP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/QoS管理/QoS兼容性管理/EPS QoS参数到Pre-R8 QoS参数映射/设置EPS QoS参数到Pre-R8 QoS参数映射规则（SET R8QOSMAP）_26146234.md)
6. 配置切换流程中的数据转发模式。
  [**SET SMFUNC**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/会话管理/SM扩展功能管理/设置会话管理扩展功能(SET SMFUNC)_26145684.md)

## [任务示例](#ZH-CN_OPI_0191285433)

任务描述

激活LTE和UMTS PS网络之间的切换特性，进行如下配置：

- 配置MME Group ID的范围为0x1000~0x1088，其它取值都作为LAC；系统不使用RNC ID域名，切换过程中也使用RAI域名查找对端SGSN。
- 配置RAI 3080023020000的域名对应的SGSN IP地址，IP地址为172.25.6.53和172.25.6.54使用负荷分担方式工作。
- 配置设备mme6.cluster1.net27.operator.com的接口1对应的IP地址，IP地址为172.25.6.56和172.25.6.57使用负荷分担方式工作。
- 配置设备mme7.cluster1.net27.operator.com的接口2对应的IP地址，IP地址为172.25.6.66和172.25.6.67使用负荷分担方式工作。
- 配置TAI为0x7101的MME对应的设备主机名，负荷分担使用MME6的接口1和MME7的接口2。
- 配置QCI 9的EPS QoS转换到GPRS QoS时，映射出的保留BER参数为1*10<sup>-5</sup>。
- 配置切换流程中使用SGW-C在源侧RAN与目标侧RAN之间进行间接数据转发。

脚本

//开启LTE和UMTS PS网络之间的切换功能开关。

```
SET LICENSESWITCH: LICITEM="LKV2HOLU02", SWITCH=ENABLE;
```

//配置在切换流程中不使用RNC ID域名进行查询。

```
SET PESELPLCY: RNCID=NO;
```

//配置到DNS的数据，进行对端网元寻址。

```
ADD IPV4DNSH: HSINDEX=1, HOSTNAME="RAC0000.LAC2302.MNC0000.MCC0123.GPRS", ADDRSECTION=SECTION1, IPV4ADDR1="172.25.6.53", PRIORITY1=1, WEIGHT1=50, IPV4ADDR2="172.25.6.54", PRIORITY2=1, WEIGHT2=50;
```

```
ADD IPV4DNSH: HSINDEX=2, HOSTNAME="topoff.Interface1.mme6.cluster1.net27.operator.com", ADDRSECTION=SECTION1, IPV4ADDR1="172.25.6.56", PRIORITY1=1, WEIGHT1=50, IPV4ADDR2="172.25.6.57", PRIORITY2=1, WEIGHT2=50;
```

```
ADD IPV4DNSH: HSINDEX=3, HOSTNAME="topoff.Interface2.mme7.cluster1.net27.operator.com", ADDRSECTION=SECTION1, IPV4ADDR1="172.25.6.66", PRIORITY1=1, WEIGHT1=50, IPV4ADDR2="172.25.6.67", PRIORITY2=1, WEIGHT2=50;
```

```
ADD DNSN: FQDN="TAC-LB01.TAC-HB71.TAC.EPC.MNC000.MCC123.3GPPNETWORK.ORG", HSINDEX=2, ENTITY=MME, INTYPE=Gn, PRIORITY=1, WEIGHT=150;
```

```
ADD DNSN: FQDN="TAC-LB02.TAC-HB72.TAC.EPC.MNC000.MCC123.3GPPNETWORK.ORG", HSINDEX=3, ENTITY=MME, INTYPE=Gn, PRIORITY=1, WEIGHT=150;
```

//可选：配置ARP转换的H值和M值。

```
SET COMPATIBILITY: HARP=6, MARP=11;
```

//可选：配置EPS QoS和GPRS QoS的QCI参数转换规则。

```
SET R8QOSMAP: QCI=9, RBER=E_RESIDUAL_BIT_ERR_RATIO_7;
```

//配置切换流程中的数据转发模式。

```
SET SMFUNC: INDFWD=YES;
```
