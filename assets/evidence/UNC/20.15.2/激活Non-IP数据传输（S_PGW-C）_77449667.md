# 激活 Non-IP数据传输 （S/PGW-C）

- [操作场景](#ZH-CN_OPI_0277449667__1.3.1)
- [必备事项](#ZH-CN_OPI_0277449667__1.3.2)
- [操作步骤](#ZH-CN_OPI_0277449667__1.3.3)
- [任务示例](#ZH-CN_OPI_0277449667__1.3.4)

## [操作场景](#ZH-CN_OPI_0277449667)

本操作指导介绍在运行网络中激活 Non-IP数据传输 特性的操作过程。当Non-IP用户接入网络时，需要在 UNC 上开启Non-IP功能开关，并且为Non-IP用户配置目的服务器的地址。

> **说明**
> SGW-C、PGW-C

## [必备事项](#ZH-CN_OPI_0277449667)

前提条件

- 请仔细阅读 [WSFD-215103 Non-IP数据传输特性概述（S/PGW-C）](特性概述_77449666.md) 。
- 完成 [激活基于信令面的数据传输（SGW-C）](../../WSFD-215101 基于信令面的数据传输/WSFD-215101 基于信令面的数据传输（SGW-C）/激活基于信令面的数据传输（SGW-C）_77260996.md) 。
- 完成加载License。

数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| [**SET NONIPFUNC**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/M2M/全局Non-IP配置/设置Non-IP功能配置（SET NONIPFUNC）_28567659.md) | Non-IP功能开关（NONIPSWITCH） | ENABLE | 本端规划 | 全局Non-IP功能开关 |
| [**SET APNNONIPFUNC**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/M2M/APN的Non-IP配置/设置APN Non-IP功能配置（SET APNNONIPFUNC）_28567657.md) | APN | test | 已配置数据中获取 | 指定APN下的Non-IP功能开关 |
| [**SET APNNONIPFUNC**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/M2M/APN的Non-IP配置/设置APN Non-IP功能配置（SET APNNONIPFUNC）_28567657.md) | APN Non-IP功能开关（NONIPSWITCH） | ENABLE | 本端规划 | 指定APN下的Non-IP功能开关 |
| [**ADD M2MSERVERGRP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/M2M/M2M服务器组/增加M2M服务器组（ADD M2MSERVERGRP）_73321226.md) | M2M服务器组名称（GROUPNAME） | m2msrvgroup01 | 本端规划 | M2M服务器组 |
| [**ADD M2MSERVERGRP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/M2M/M2M服务器组/增加M2M服务器组（ADD M2MSERVERGRP）_73321226.md) | M2M服务器IP地址类型（SERVERIPTYPE） | IPV4 | 与对端协商 | M2M服务器组 |
| [**ADD M2MSERVER**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/M2M/M2M服务器/增加M2M服务器（ADD M2MSERVER）_73321225.md) | M2M服务器组名称（GROUPNAME） | m2msrvgroup01 | 已配置数据中获取 | M2M服务器 |
| [**ADD M2MSERVER**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/M2M/M2M服务器/增加M2M服务器（ADD M2MSERVER）_73321225.md) | M2M服务器索引（SERVERINDEX） | 1 | 本端规划 | M2M服务器 |
| [**ADD M2MSERVER**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/M2M/M2M服务器/增加M2M服务器（ADD M2MSERVER）_73321225.md) | M2M服务器IP地址类型（SERVERIPTYPE） | IPV4 | 与对端协商 | M2M服务器 |
| [**ADD M2MSERVER**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/M2M/M2M服务器/增加M2M服务器（ADD M2MSERVER）_73321225.md) | M2M服务器IPv4地址（SERVERIPV4ADDR） | 10.107.242.16 | 全网规划 | M2M服务器 |
| [**ADD M2MSERVER**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/M2M/M2M服务器/增加M2M服务器（ADD M2MSERVER）_73321225.md) | 服务器端口号（SERVERPORT） | 2020 | 与对端协商 | M2M服务器 |
| [**ADD M2MSVRGRPBIND**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/M2M/M2M服务器组绑定关系/增加M2M服务器组绑定关系（ADD M2MSVRGRPBIND）_73321227.md) | M2M服务器组名称（GROUPNAME） | m2msrvgroup01 | 本端规划 | 指定M2M服务器组的名称 |
| [**ADD M2MSVRGRPBIND**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/M2M/M2M服务器组绑定关系/增加M2M服务器组绑定关系（ADD M2MSVRGRPBIND）_73321227.md) | APN | test | 本端规划 | 指定APN实例名称 |

## [操作步骤](#ZH-CN_OPI_0277449667)

1. 进入 “MML命令行-UNC” 窗口。
2. 打开本特性的License配置开关。
  [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
3. 使能全局的Non-IP功能开关。
  [**SET NONIPFUNC**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/M2M/全局Non-IP配置/设置Non-IP功能配置（SET NONIPFUNC）_28567659.md)
4. 使能指定APN下的Non-IP功能开关。
  [**SET APNNONIPFUNC**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/M2M/APN的Non-IP配置/设置APN Non-IP功能配置（SET APNNONIPFUNC）_28567657.md)

  > **说明**
  > 业务处理过程中优先应用APN下的设置，只有当APN下配置为Inherit时才应用全局下的设置。
5. 配置M2M服务器组。
  [**ADD M2MSERVERGRP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/M2M/M2M服务器组/增加M2M服务器组（ADD M2MSERVERGRP）_73321226.md)
6. 配置M2M服务器组下的M2M服务器。
  [**ADD M2MSERVER**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/M2M/M2M服务器/增加M2M服务器（ADD M2MSERVER）_73321225.md)
7. **可选：**配置指定APN下的M2M服务器组。
  [**ADD M2MSVRGRPBIND**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/M2M/M2M服务器组绑定关系/增加M2M服务器组绑定关系（ADD M2MSVRGRPBIND）_73321227.md)
8. **可选：**配置话单中是否携带pdp-type-extension、sgi-ptp-tunnelling-method字段。
  [**ADD CDRFIELDTEMP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/话单字段控制/话单字段模板/增加话单字段模板（ADD CDRFIELDTEMP）_09896890.md)

## [任务示例](#ZH-CN_OPI_0277449667)

任务描述

在 UNC 上配置 Non-IP数据传输 功能。

脚本

//打开本特性的License配置开关。

```
SET LICENSESWITCH:LICITEM="LKV3WNBNIP11",SWITCH=ENABLE;
```

//使能全局的Non-IP功能开关。

```
SET NONIPFUNC:NONIPSWITCH=ENABLE;
```

//使能ITEM指定APN下的Non-IP功能开关。

```
SET APNNONIPFUNC:APN="test",NONIPSWITCH=ENABLE;
```

//配置组名为“m2msrvgroup01”，服务器IP类型为IPV4的M2M服务器组。

```
ADD M2MSERVERGRP: GROUPNAME="m2msrvgroup01", SERVERIPTYPE=IPV4;
```

//在“m2msrvgroup01”M2M服务器组下新增一个M2M服务器。

```
ADD M2MSERVER: GROUPNAME="m2msrvgroup01", SERVERINDEX=1, SERVERIPTYPE=IPV4, SERVERIPV4ADDR="10.107.242.16", SERVERPORT=2020;
```

//配置APN与M2M服务器组的绑定。

```
ADD M2MSVRGRPBIND: APN="test", GROUPNAME="m2msrvgroup01";
```

//可选：配置话单中携带pdp-type-extension、sgi-ptp-tunnelling-method字段。

```
ADD CDRFIELDTEMP:TEMPLATENAME="cdrfieldtemp",PDPTYPEEXT=ENABLE,SGIPTPTUNMETH=ENABLE;
```
