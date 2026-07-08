# 配置PGW-U到Untrusted Non-3GPP GW的数据（VPN缺省路由组网）

- [操作场景](#ZH-CN_OPI_0272489253__1.3.1)
- [必备事项](#ZH-CN_OPI_0272489253__1.3.2)
- [操作步骤](#ZH-CN_OPI_0272489253__1.3.3)
- [任务示例](#ZH-CN_OPI_0272489253__1.3.4)

## [操作场景](#ZH-CN_OPI_0272489253)

> **说明**
> 适用于PGW-U。

UDG 与ePDG互通，用于WiFi用户接入EPC网络。

- 逻辑接口：Paif接口。
- 路由：静态路由。

> **说明**
> 虚机容器：
>
> - 当数据流量小于10G时可参考本举例进行P-GW到ePDG的互通部署，当数据流量大于10G时请参考[配置PGW-U到Untrusted Non-3GPP GW的数据（VPN+OSPF动态路由组网）（虚机容器）](配置PGW-U到Untrusted Non-3GPP GW的数据（VPN+OSPF动态路由组网）（虚机容器）_72489252.md)部署。
> - Paif接口需与VPN实例绑定，这样可在VPN实例内配置到ePDG的缺省路由，实现与整机缺省路由的隔离。

## [必备事项](#ZH-CN_OPI_0272489253)

前提条件

- UDG与网络实体之间的网络环境已经构建完成。
- 操作员了解UDG各类接口的类型及命名规范。

数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| [**ADD L3VPNINST**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例/增加L3VPN实例（ADD L3VPNINST）_49802446.md) | VPN实例名称（VRFNAME） | vpn-s2b | 全网规划 | 配置L3VPN实例。 |
| [**ADD VPNINSTAF**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例地址族/增加L3VPN实例地址族（ADD VPNINSTAF）_49802178.md) | VPN实例名称（VRFNAME） | vpn-s2b | 已配置数据中获取 | 设置指定VPN实例下的地址族。 |
| [**ADD VPNINSTAF**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例地址族/增加L3VPN实例地址族（ADD VPNINSTAF）_49802178.md) | 地址族类型（AFTYPE） | ipv4uni | 本端规划 | 设置指定VPN实例下的地址族。 |
| [**ADD VPNINSTAF**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例地址族/增加L3VPN实例地址族（ADD VPNINSTAF）_49802178.md) | 路由标识（VRFRD） | 100:1 | 本端规划 | 设置指定VPN实例下的地址族。 |
| [**ADD VPNINST**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/DN管理/VPN管理/VPN/增加VPN实例（ADD VPNINST）_82837045.md) | VPN实例（VPNINSTANCE） | vpn-s2b | 全网规划 | 配置VPN实例。 |
| [**ADD LOGICINF**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/DN管理/逻辑接口管理/逻辑接口配置/接口/增加逻辑接口（ADD LOGICINF）_82835378.md) | 逻辑接口名称（NAME） | Paif1/1/0 | 固定取值 | 创建Paif接口。 |
| [**ADD LOGICINF**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/DN管理/逻辑接口管理/逻辑接口配置/接口/增加逻辑接口（ADD LOGICINF）_82835378.md) | 逻辑接口的IP版本（IPVERSION） | IPv4 | 本端规划 | 创建Paif接口。 |
| [**ADD LOGICINF**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/DN管理/逻辑接口管理/逻辑接口配置/接口/增加逻辑接口（ADD LOGICINF）_82835378.md) | 逻辑接口的IPv4地址1（IPV4ADDRESS1） | 10.10.10.10 | 本端规划 | 创建Paif接口。 |
| [**ADD LOGICINF**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/DN管理/逻辑接口管理/逻辑接口配置/接口/增加逻辑接口（ADD LOGICINF）_82835378.md) | 逻辑接口的IPv4掩码1（IPV4MASK1） | 255.255.255.255 | 本端规划 | 创建Paif接口。 |
| [**ADD LOGICINF**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/DN管理/逻辑接口管理/逻辑接口配置/接口/增加逻辑接口（ADD LOGICINF）_82835378.md) | VPN实例名称（VPNINSTANCE） | vpn-s2b | 已配置数据中获取 | 创建Paif接口。 |
| [**ADD SRROUTE**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/静态路由管理/IPv4静态路由/增加IPv4静态路由（ADD SRROUTE）_49961498.md) | 地址族（AFTYPE） | ipv4unicast | 本端规划 | 缺省路由。 |
| [**ADD SRROUTE**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/静态路由管理/IPv4静态路由/增加IPv4静态路由（ADD SRROUTE）_49961498.md) | 路由前缀（PREFIX） | 0.0.0.0 | 与对端协商 | 缺省路由。 |
| [**ADD SRROUTE**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/静态路由管理/IPv4静态路由/增加IPv4静态路由（ADD SRROUTE）_49961498.md) | 路由掩码长度（MASKLENGTH） | 0 | 本端规划 | 缺省路由。 |
| [**ADD SRROUTE**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/静态路由管理/IPv4静态路由/增加IPv4静态路由（ADD SRROUTE）_49961498.md) | VPN实例名称（VRFNAME） | vpn-s2b | 已配置数据中获取 | 缺省路由。 |
| [**ADD SRROUTE**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/静态路由管理/IPv4静态路由/增加IPv4静态路由（ADD SRROUTE）_49961498.md) | 路由下一跳（NEXTHOP） | 192.168.94.1.<br>192.168.94.9 | 与对端协商 | 缺省路由。 |
| [**ADD SRROUTE**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/静态路由管理/IPv4静态路由/增加IPv4静态路由（ADD SRROUTE）_49961498.md) | 路由出接口名字（IFNAME） | Invalid0 | 本端规划 | 缺省路由。 |

## [操作步骤](#ZH-CN_OPI_0272489253)

1. 参考初始配置中 **配置静态路由+BFD组网（IPv4）** 配置对应的组网。
2. 创建L3VPN实例。
  [**ADD L3VPNINST**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例/增加L3VPN实例（ADD L3VPNINST）_49802446.md)
  [**ADD VPNINSTAF**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例地址族/增加L3VPN实例地址族（ADD VPNINSTAF）_49802178.md)
3. 全局激活BFD。
  [**SET BFD**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/BFD管理/BFD全局配置/设置BFD全局属性（SET BFD）_00840937.md)
  > **说明**
  > 参数“DELAYUPTIMER”（会话延迟UP时间）和“TOSEXP”（动态会话报文优先级）可以不用输入，使用默认值即可。
4. 配置到ePDG的VPN缺省路由。
  [**ADD SRROUTE**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/静态路由管理/IPv4静态路由/增加IPv4静态路由（ADD SRROUTE）_49961498.md)
5. 配置VPN实例。
  [**ADD VPNINST**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/DN管理/VPN管理/VPN/增加VPN实例（ADD VPNINST）_82837045.md)
6. 创建Paif接口。
  [**ADD LOGICINF**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/DN管理/逻辑接口管理/逻辑接口配置/接口/增加逻辑接口（ADD LOGICINF）_82835378.md)

## [任务示例](#ZH-CN_OPI_0272489253)

任务描述

本实例中，操作员在 UDG 上进行数据配置实现以下要求：

- UDG使用Paif逻辑接口与ePDG建立逻辑连接。
- UDG使用VPN缺省路由与多个ePDG建立起正常的IP连接。

脚本

1. 参考初始配置中**配置静态路由+BFD组网（IPv4）**配置对应的组网。
2. 创建L3VPN实例。
  ```
  ADD L3VPNINST:VRFNAME="vpn-s2b";
  ```
  ```
  ADD VPNINSTAF:VRFNAME="vpn-s2b",AFTYPE=ipv4uni,VRFRD=100:1;
  ```
3. 全局激活BFD。
  ```
  SET BFD: BFDENABLE=TRUE;
  ```
4. 配置到ePDG的VPN缺省路由。
  ```
  ADD SRROUTE:VRFNAME="vpn-s2b",AFTYPE=ipv4unicast,PREFIX="172.16.47.0",MASKLENGTH=24,DESTVRFNAME="_public_",NEXTHOP="192.168.94.1",IFNAME="Invalid0";
  ADD SRROUTE:VRFNAME="vpn-s2b",AFTYPE=ipv4unicast,PREFIX="172.16.47.0",MASKLENGTH=24,DESTVRFNAME="_public_",NEXTHOP="192.168.94.9",IFNAME="Invalid0";
  ```
5. 配置VPN实例。
  ```
  ADD VPNINST: VPNINSTANCE ="vpn-s2b";
  ```
6. 创建Paif接口。
  ```
  ADD LOGICINF:NAME="Paif1/1/0",IPVERSION=IPV4,IPV4ADDRESS1="10.10.10.10",IPV4MASK1="255.255.255.255",VPNINSTANCE="vpn-s2b";
  ```
