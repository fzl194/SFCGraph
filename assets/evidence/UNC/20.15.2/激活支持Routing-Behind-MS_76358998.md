# 激活支持Routing Behind MS

- [操作场景](#ZH-CN_OPI_0276358998__1.3.1)
- [必备事项](#ZH-CN_OPI_0276358998__1.3.2)
- [操作步骤](#ZH-CN_OPI_0276358998__1.3.3)
- [任务示例](#ZH-CN_OPI_0276358998__1.3.4)

## [操作场景](#ZH-CN_OPI_0276358998)

当运营商需要开展移动VPN业务，使多台终端设备（PC）可以通过一个 MS/UE 接入PDN或Intranet网络，并使用独立的IP地址与网络侧设备进行双向数据业务时，需要激活 UNC 的Routing Behind MS功能。

> **说明**
> 适用于GGSN-C、SGW-C、PGW-C、SMF。

## [必备事项](#ZH-CN_OPI_0276358998)

前提条件

- 请仔细阅读[WSFD-205101 支持Routing Behind MS特性概述](WSFD-205101 支持Routing Behind MS特性概述_76358997.md)。
- 完成加载License。
- 本特性与UDG配合使用生效，请参考UDG中的**GWFD-110910 支持Routing Behind MS**。
- 如若本特性部署在新APN上，请参考章节[配置会话管理参数](../../../../初始配置/UNC初始配置与调测/组网对接配置/配置SMF&PGW-C&SGW-C&GGSN/配置SMF/配置会话管理参数_39872233.md)完成APN信息配置。

数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| [**SET APNADDRESSATTR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/基于APN的地址管理控制参数/设置基于APN的地址分配属性（SET APNADDRESSATTR）_33845575.md) | APN名称（APN） | huawei.com | 已配置数据中获取 | 规划使能Routing Behind MS功能的APN实例，已通过<br>[**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)<br>命令配置，可以使用<br>[**LST APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/查询APN配置（LST APN）_09652599.md)<br>命令进行查询。 |
| [**SET APNADDRESSATTR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/基于APN的地址管理控制参数/设置基于APN的地址分配属性（SET APNADDRESSATTR）_33845575.md) | 手机后路由（FRAMEDROUTE） | ENABLE | 本端规划 | 配置指定APN是否允许手机后路由用户接入。 |
| **[SET SMCOMMFUNC](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/会话协议参数管理/会话管理拓展功能/通用会话管理拓展功能/设置通用会话拓展功能（SET SMCOMMFUNC）_08433263.md)** | 手机后路由功能开关（RTBEHINDMSSW） | ENABLE | 本端规划 | 支持从本地配置中获取后路由。 |
| **[ADD ROUTINGBEHINDMS](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/UE地址管理/DHCP管理/手机后路由/增加本地配置的手机后路由信息（ADD ROUTINGBEHINDMS）_59000287.md)** | 用户IMSI号（IMSI） | 123000123456789 | 本端规划 | 本地配置手机后路由信息。AAA不返回后路由信息或未部署AAA服务器时，可使用本地配置的后路由信息。 |
| **[ADD ROUTINGBEHINDMS](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/UE地址管理/DHCP管理/手机后路由/增加本地配置的手机后路由信息（ADD ROUTINGBEHINDMS）_59000287.md)** | APN名称（APN） | huawei.com | 本端规划 | 本地配置手机后路由信息。AAA不返回后路由信息或未部署AAA服务器时，可使用本地配置的后路由信息。 |
| **[ADD ROUTINGBEHINDMS](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/UE地址管理/DHCP管理/手机后路由/增加本地配置的手机后路由信息（ADD ROUTINGBEHINDMS）_59000287.md)** | 后路由IPv4地址（FRAMEDROUTEIP） | 192.168.1.0 | 本端规划 | 本地配置手机后路由信息。AAA不返回后路由信息或未部署AAA服务器时，可使用本地配置的后路由信息。 |
| **[ADD ROUTINGBEHINDMS](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/UE地址管理/DHCP管理/手机后路由/增加本地配置的手机后路由信息（ADD ROUTINGBEHINDMS）_59000287.md)** | 后路由掩码（FRAMEDROUTEMASK） | 255.255.255.0 | 本端规划 | 本地配置手机后路由信息。AAA不返回后路由信息或未部署AAA服务器时，可使用本地配置的后路由信息。 |

## [操作步骤](#ZH-CN_OPI_0276358998)

1. 进入 “MML命令行-UNC” 窗口。
2. 打开本特性的License开关。
  [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
3. 使能该APN的Routing Behind MS功能。
  [**SET APNADDRESSATTR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/基于APN的地址管理控制参数/设置基于APN的地址分配属性（SET APNADDRESSATTR）_33845575.md)
  > **说明**
  > - 如果APN使能了L2TP功能，则无需开启Routing Behind MS功能。
  > - 在功能开启前，需要在AAA Server上配置好分配给终端设备使用的IP地址段。
4. 支持从本地配置中获取后路由。
  **[SET SMCOMMFUNC](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/会话协议参数管理/会话管理拓展功能/通用会话管理拓展功能/设置通用会话拓展功能（SET SMCOMMFUNC）_08433263.md)**
5. 本地配置手机后路由信息。AAA不返回后路由信息或未部署AAA服务器时，可使用本地配置的后路由信息。
  **[ADD ROUTINGBEHINDMS](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/UE地址管理/DHCP管理/手机后路由/增加本地配置的手机后路由信息（ADD ROUTINGBEHINDMS）_59000287.md)**

## [任务示例](#ZH-CN_OPI_0276358998)

任务描述

使能APN“huawei.com”的Routing Behind MS功能。

脚本

//打开本特性的License配置开关。

```
SET LICENSESWITCH:LICITEM="LKV3W9RBMS12",SWITCH=ENABLE;
```

//使能该APN的Routing Behind MS功能。

```
SET APNADDRESSATTR:APN="huawei.com",FRAMEDROUTE=ENABLE;
```

//支持从本地配置中获取后路由。

```
SET SMCOMMFUNC: RTBEHINDMSSW=ENABLE;
```

//本地配置手机后路由信息。

```
ADD ROUTINGBEHINDMS: IMSI="123000123456789", APN="huawei.com", FRAMEDROUTEIP="192.168.1.0", FRAMEDROUTEMASK="255.255.255.0";
```
