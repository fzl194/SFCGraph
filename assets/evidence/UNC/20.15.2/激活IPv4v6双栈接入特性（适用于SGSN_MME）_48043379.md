# 激活IPv4v6双栈接入特性（适用于SGSN/MME）

- [操作场景](#ZH-CN_OPI_0248043379__1.3.1)
- [必备事项](#ZH-CN_OPI_0248043379__1.3.2)
- [操作流程](#ZH-CN_OPI_0248043379__1.3.3)
- [操作步骤](#ZH-CN_OPI_0248043379__1.3.4)
- [任务示例](#ZH-CN_OPI_0248043379__1.3.5)

## [操作场景](#ZH-CN_OPI_0248043379)

本操作指导介绍在运行网络中激活IPv4v6双栈接入特性的操作过程。

UNC 支持创建IPv4v6双栈，通过IPv4v6地址为UE提供业务，使UE可以用IPv4v6地址进行数据传输。

> **说明**
> 适用于 SGSN/ MME。

## [必备事项](#ZH-CN_OPI_0248043379)

前提条件

- 请仔细阅读[WSFD-104002 IPv4v6双栈接入特性概述（适用于2G/3G/4G）](特性概述_48043389.md)。
- 完成加载License。
- 支持IPv4v6的用户已经接入到网络。

数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| [**SET SMFUNC**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/会话管理/SM扩展功能管理/设置会话管理扩展功能(SET SMFUNC)_26145684.md) | IPv4v6双栈（DUALFLAG） | YES | 全网规划 | 会话管理扩展功能 |
| **[**ADD SMSUBDATA**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/会话管理/签约数据纠正/增加签约数据纠正参数(ADD SMSUBDATA)_26305486.md)** | 用户范围（SUBRANGE） | ALL_USER | 全网规划 | 签约数据纠正参数 |
| **[**ADD SMSUBDATA**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/会话管理/签约数据纠正/增加签约数据纠正参数(ADD SMSUBDATA)_26305486.md)** | 签约PDP/PDN类型（PDPTYPE） | IPV4 | 全网规划 | 签约数据纠正参数 |
| **[**ADD SMSUBDATA**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/会话管理/签约数据纠正/增加签约数据纠正参数(ADD SMSUBDATA)_26305486.md)** | 签约IPv4 PDP/PDN地址分配类型（IPV4PDPADDRTYPE） | ALLOCATION_IPV4PDP_DYNAMIC | 全网规划 | 签约数据纠正参数 |
| **[**ADD SMSUBDATA**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/会话管理/签约数据纠正/增加签约数据纠正参数(ADD SMSUBDATA)_26305486.md)** | 新的签约PDP类型（NEWPDPTYPE） | IPV4V6 | 全网规划 | 签约数据纠正参数 |
| **[**ADD SMSUBDATA**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/会话管理/签约数据纠正/增加签约数据纠正参数(ADD SMSUBDATA)_26305486.md)** | 新的签约IPv4 PDP/PDN地址分配类型（NEWIPV4PDPADDRTYPE） | ALLOCATION_IPV4PDP_DYNAMIC | 全网规划 | 签约数据纠正参数 |
| **[**ADD SMSUBDATA**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/会话管理/签约数据纠正/增加签约数据纠正参数(ADD SMSUBDATA)_26305486.md)** | 新的签约IPv6 PDP/PDN地址分配类型（NEWIPV6PDPADDRTYPE ） | DYNAMIC | 全网规划 | 签约数据纠正参数 |

## [操作流程](#ZH-CN_OPI_0248043379)

激活IPv4v6双栈接入操作流程如 [图1](#ZH-CN_OPI_0248043379__fig_01) 所示。

**图1** 激活IPv4v6双栈接入操作流程

<br>

![](激活IPv4v6双栈接入特性（适用于SGSN_MME）_48043379.assets/zh-cn_image_0248043383_2.png)

## [操作步骤](#ZH-CN_OPI_0248043379)

1. 进入 “MML命令行-UNC” 窗口。
2. 打开IPv4v6双栈接入特性的License配置开关。
  [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
3. 开启IPv4v6双栈接入功能。
  [**SET SMFUNC**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/会话管理/SM扩展功能管理/设置会话管理扩展功能(SET SMFUNC)_26145684.md)
4. **可选：**增加签约数据纠正参数。如果Gr口连接的HLR或S6a口连接的HSS支持IPv4v6双栈，则不需要执行此步骤；若不支持IPv4v6双栈，需要执行此步骤。
  [**ADD SMSUBDATA**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/会话管理/签约数据纠正/增加签约数据纠正参数(ADD SMSUBDATA)_26305486.md)
5. **可选：** 增加GTP-C V0/V1协议兼容性配置。
  > **说明**
  > - “TMMSGTYPE”设置为“CREATE_PDP_CONTEXT_REQUEST”或者“UPDATE_PDP_CONTEXT_REQUEST”。
  > - 可通过[**LST GTPCCMPT**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/GTP-C接口管理/GTP-C协议管理/GTP-C V0 V1协议兼容性/查询GTP-C V0_V1协议兼容性配置(LST GTPCCMPT)_26145924.md)命令查看当前配置，如果携带方式被设置为不携带Common Flags信元时则需要重新配置。
  在 “MML命令行-UNC” 窗口上执行命令
  [**MOD GTPCCMPT**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/GTP-C接口管理/GTP-C协议管理/GTP-C V0 V1协议兼容性/修改GTP-C V0_V1协议兼容性配置(MOD GTPCCMPT)_72345523.md) : MSGCLS=TM，TMMSGTYPE=CREATE_PDP_CONTEXT_REQUEST, CRTPDPREQ=COMMON_FLAGS, UPDPDPREQ=COMMON_FLAGS, CMFLG=YES ;

## [任务示例](#ZH-CN_OPI_0248043379)

任务描述

开启IPv4v6双栈功能S6a口，所以需要增加一条签约数据纠正参数信息，其用户范围为所有用户，匹配条件为签约数据，签约APNNI范围为所有签约APNNI，签约PDP/PDN类型为IPv4，签约IPv4 PDP/PDN地址分配类型为动态分配，不修改签约APNNI，修改新的PDP类型为IPv4v6，新的IPv4地址为动态分配，新的IPv6地址为动态分配。

脚本

//打开License配置开关。

```
SET LICENSESWITCH: LICITEM="LKV2DUSA02", SWITCH=ENABLE;
```

//开启IPv4v6双栈。

```
SET SMFUNC: DUALFLAG=YES;
```

//可选：增加签约数据纠正参数。

```
ADD SMSUBDATA: SUBRANGE=ALL_USER, TYPE=SUBSCRIBED_PARAMETER, APNNIRANGE=APNNI_ALL, PDPTYPE=IPV4, IPV4PDPADDRTYPE=ALLOCATION_IPV4PDP_DYNAMIC, CORRECTAPNNI=NO, NEWPDPTYPE=IPV4V6, NEWIPV4PDPADDRTYPE=DYNAMIC, NEWIPV6PDPADDRTYPE=DYNAMIC;
```
