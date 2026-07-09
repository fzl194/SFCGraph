# 配置到ICAP Server的互通数据

- [操作场景](#ZH-CN_OPI_0000001475400117__1.3.1)
- [必备事项](#ZH-CN_OPI_0000001475400117__1.3.2)
- [操作步骤](#ZH-CN_OPI_0000001475400117__1.3.3)
- [任务示例](#ZH-CN_OPI_0000001475400117__1.3.4)

## [操作场景](#ZH-CN_OPI_0000001475400117)

部署URL过滤基本功能特性时，需要配置 UDG 与ICAP Server的互通数据。

> **说明**
> 适用于PGW-U、UPF。

## [必备事项](#ZH-CN_OPI_0000001475400117)

前提条件

- 请仔细阅读[GWFD-110471 URL过滤基本功能](../../GWFD-110471 URL过滤基本功能_05929912.md)。
- ICAP Server上的基础数据已搭建完毕。

数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| [**ADD VPNINST**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/DN管理/VPN管理/VPN/增加VPN实例（ADD VPNINST）_82837045.md) | VPN实例名（VPNINSTANCE） | vpn-gcfif | 本端规划 | - |
| **[**ADD LOGICINF**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/DN管理/逻辑接口管理/逻辑接口配置/接口/增加逻辑接口（ADD LOGICINF）_82835378.md)** | 逻辑接口名称（NAME） | gcfif1/0/0 | 本端规划 | 配置逻辑接口。 |
| **[**ADD LOGICINF**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/DN管理/逻辑接口管理/逻辑接口配置/接口/增加逻辑接口（ADD LOGICINF）_82835378.md)** | 逻辑接口的IP版本（IPVERSION） | IPV4 | 全网规划 | 配置逻辑接口。 |
| **[**ADD LOGICINF**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/DN管理/逻辑接口管理/逻辑接口配置/接口/增加逻辑接口（ADD LOGICINF）_82835378.md)** | 逻辑接口的IPv4地址1（IPV4ADDRESS1） | 10.10.1.7 | 全网规划 | 配置逻辑接口。 |
| **[**ADD LOGICINF**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/DN管理/逻辑接口管理/逻辑接口配置/接口/增加逻辑接口（ADD LOGICINF）_82835378.md)** | 逻辑接口的IPv4掩码1（IPV4MASK1） | 255.255.255.255 | 全网规划 | 配置逻辑接口。 |
| **[**ADD LOGICINF**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/DN管理/逻辑接口管理/逻辑接口配置/接口/增加逻辑接口（ADD LOGICINF）_82835378.md)** | VPN实例名称（VPNINSTANCE） | vpn-gcfif | 已配置数据中获取 | 已通过<br>[**ADD VPNINST**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/DN管理/VPN管理/VPN/增加VPN实例（ADD VPNINST）_82837045.md)<br>配置。 |
| **[**ADD ICAPSERVER**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/ICAPC管理/ICAP服务器/增加ICAP服务器（ADD ICAPSERVER）_28751562.md)** | ICAP服务器名称（ICAPSERVERNAME） | icapserver1 | 全网规划 | 配置ICAP Server。 |
| **[**ADD ICAPSERVER**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/ICAPC管理/ICAP服务器/增加ICAP服务器（ADD ICAPSERVER）_28751562.md)** | ICAP服务器类型（ICAPSERVERTYPE） | URL_FILTERING | 固定取值 | 配置ICAP Server。 |
| **[**ADD ICAPSERVER**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/ICAPC管理/ICAP服务器/增加ICAP服务器（ADD ICAPSERVER）_28751562.md)** | ICAP 服务器IP地址类型（ICAPSVRIPTYPE） | IPV4 | 全网规划 | 配置ICAP Server。 |
| **[**ADD ICAPSERVER**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/ICAPC管理/ICAP服务器/增加ICAP服务器（ADD ICAPSERVER）_28751562.md)** | ICAP服务器IPv4地址（ICAPSERVERIPV4） | 172.16.39.136 | 全网规划 | 配置ICAP Server。 |
| **[**ADD ICAPSERVER**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/ICAPC管理/ICAP服务器/增加ICAP服务器（ADD ICAPSERVER）_28751562.md)** | VPN实例名称（VPNINSTANCE） | vpn-gcfif | 已配置数据中获取 | 已通过<br>[**ADD VPNINST**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/DN管理/VPN管理/VPN/增加VPN实例（ADD VPNINST）_82837045.md)<br>配置，与<br>**[ADD LOGICINF](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/DN管理/逻辑接口管理/逻辑接口配置/接口/增加逻辑接口（ADD LOGICINF）_82835378.md)**<br>中配置的<br>**VPNINSTANCE**<br>保持一致。 |
| **[ADD ICAPLOCALINFO](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/ICAPC管理/ICAP本端信息/增加ICAP本端信息（ADD ICAPLOCALINFO）_28984184.md)** | ICAP服务器类型（ICAPSERVERTYPE） | URL_FILTERING | 已配置数据中获取 | 已通过<br>**[ADD ICAPSERVER](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/ICAPC管理/ICAP服务器/增加ICAP服务器（ADD ICAPSERVER）_28751562.md)**<br>配置。 |
| **[ADD ICAPLOCALINFO](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/ICAPC管理/ICAP本端信息/增加ICAP本端信息（ADD ICAPLOCALINFO）_28984184.md)** | User Agent（USERAGENT） | test | 本端规划 | - |
| [**ADD ICAPSVRGRP**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/ICAPC管理/ICAP服务器组/增加ICAP服务器组（ADD ICAPSVRGRP）_28984182.md) | ICAP服务器组名称（ICAPSVRGRPNAME） | icapsvrgrp1 | 全网规划 | 配置ICAP服务器组。 |
| [**ADD ICAPSVRGRP**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/ICAPC管理/ICAP服务器组/增加ICAP服务器组（ADD ICAPSVRGRP）_28984182.md) | ICAP服务器类型（ICAPSERVERTYPE） | URL_FILTERING | 固定取值 | 配置ICAP服务器组。 |
| [**ADD ICAPSVRBINDISG**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/ICAPC管理/ICAP服务器绑定/增加ICAP服务器绑定关系（ADD ICAPSVRBINDISG）_29222372.md) | ICAP服务器组名称（ICAPSVRGRPNAME） | icapsvrgrp1 | 已配置数据中获取 | 已通过<br>[**ADD ICAPSVRGRP**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/ICAPC管理/ICAP服务器组/增加ICAP服务器组（ADD ICAPSVRGRP）_28984182.md)<br>配置。 |
| [**ADD ICAPSVRBINDISG**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/ICAPC管理/ICAP服务器绑定/增加ICAP服务器绑定关系（ADD ICAPSVRBINDISG）_29222372.md) | ICAP服务器名称（ICAPSERVERNAME） | icapserver1 | 已配置数据中获取 | 已通过<br>**[ADD ICAPSERVER](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/ICAPC管理/ICAP服务器/增加ICAP服务器（ADD ICAPSERVER）_28751562.md)**<br>配置。 |

## [操作步骤](#ZH-CN_OPI_0000001475400117)

1. 添加VPN实例。
  [**ADD VPNINST**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/DN管理/VPN管理/VPN/增加VPN实例（ADD VPNINST）_82837045.md)
2. 配置 UDG 与ICAP Server间逻辑接口。
  **[ADD LOGICINF](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/DN管理/逻辑接口管理/逻辑接口配置/接口/增加逻辑接口（ADD LOGICINF）_82835378.md)**
3. 配置ICAP Server信息。
    a. 配置ICAP Server。
      **[ADD ICAPSERVER](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/ICAPC管理/ICAP服务器/增加ICAP服务器（ADD ICAPSERVER）_28751562.md)**
    b. 配置 UDG 与ICAP Server间逻辑接口相关的标识信息。
      **[ADD ICAPLOCALINFO](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/ICAPC管理/ICAP本端信息/增加ICAP本端信息（ADD ICAPLOCALINFO）_28984184.md)**
4. 配置ICAP服务器组。
  [**ADD ICAPSVRGRP**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/ICAPC管理/ICAP服务器组/增加ICAP服务器组（ADD ICAPSVRGRP）_28984182.md)
5. 配置ICAP服务器绑定关系。
  [**ADD ICAPSVRBINDISG**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/ICAPC管理/ICAP服务器绑定/增加ICAP服务器绑定关系（ADD ICAPSVRBINDISG）_29222372.md)

## [任务示例](#ZH-CN_OPI_0000001475400117)

任务描述

配置 UDG 与ICAP Server的互通数据。

脚本

//添加VPN实例。

```
ADD VPNINST:VPNINSTANCE="vpn-gcfif";
```

//配置 UDG 与ICAP Server间逻辑接口。

```
ADD LOGICINF: NAME="gcfif1/0/0", IPVERSION=IPV4, IPV4ADDRESS1="192.168.1.1", IPV4MASK1="255.255.255.255", VPNINSTANCE="vpn-gcfif";
```

//配置ICAP Server信息。

```
ADD ICAPSERVER: ICAPSERVERNAME="icapserver1", ICAPSERVERTYPE=URL_FILTERING, ICAPSVRIPTYPE=IPV4, ICAPSERVERIPV4="172.16.39.136", VPNINSTANCE="vpn-gcfif";
```

```
ADD ICAPLOCALINFO:ICAPSERVERTYPE=URL_FILTERING, USERAGENT="test";
```

//配置ICAP服务器组。

```
ADD ICAPSVRGRP: ICAPSVRGRPNAME="icapsvrgrp1", ICAPSERVERTYPE=URL_FILTERING;
```

//配置ICAP服务器绑定关系。

```
ADD ICAPSVRBINDISG: ICAPSVRGRPNAME="icapsvrgrp1", ICAPSERVERNAME="icapserver1";
```
