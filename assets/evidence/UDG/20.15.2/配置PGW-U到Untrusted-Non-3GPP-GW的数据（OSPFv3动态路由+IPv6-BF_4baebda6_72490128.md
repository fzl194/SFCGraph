# 配置PGW-U到Untrusted Non-3GPP GW的数据（OSPFv3动态路由+IPv6 BFD组网）（虚机容器）

- [操作场景](#ZH-CN_OPI_0272490128__1.3.1)
- [必备事项](#ZH-CN_OPI_0272490128__1.3.2)
- [操作步骤](#ZH-CN_OPI_0272490128__1.3.3)
- [任务示例](#ZH-CN_OPI_0272490128__1.3.4)

## [操作场景](#ZH-CN_OPI_0272490128)

UDG 与ePDG互通，用于部署WiFi用户接入EPC网络。

- 逻辑接口：Paif接口。
- 路由：OSPFv3动态路由，各接口对外发布的路由优先级相同，作为等价路由实现物理链路的负荷分担。

## [必备事项](#ZH-CN_OPI_0272490128)

前提条件

- UDG与网络实体之间的网络环境已经构建完成。
- 操作员了解UDG各类接口的类型及命名规范。

数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| [**ADD L3VPNINST**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例/增加L3VPN实例（ADD L3VPNINST）_49802446.md) | VPN实例名称（VRFNAME） | vpn-paif | 全网规划 | 配置L3VPN实例。 |
| [**ADD VPNINSTAF**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例地址族/增加L3VPN实例地址族（ADD VPNINSTAF）_49802178.md) | VPN实例名称（VRFNAME） | vpn-paif | 已配置数据中获取 | IPv6组网场景下，该参数选择ipv6uni。 |
| [**ADD VPNINSTAF**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例地址族/增加L3VPN实例地址族（ADD VPNINSTAF）_49802178.md) | 地址族类型（AFTYPE） | ipv6uni | 本端规划 | IPv6组网场景下，该参数选择ipv6uni。 |
| [**SET BFD**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/BFD管理/BFD全局配置/设置BFD全局属性（SET BFD）_00840937.md) | BFD使能标志（BFDENABLE） | TRUE | 本端规划 | 全局激活BFD。 |
| [**ADD OSPFV3**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/OSPFv3管理/OSPFv3进程配置/创建OSPFv3进程配置（ADD OSPFV3）_00440569.md) | OSPFv3进程号(PROCID) | 6 | 全网规划 | 创建OSPFv3进程。 |
| [**ADD OSPFV3**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/OSPFv3管理/OSPFv3进程配置/创建OSPFv3进程配置（ADD OSPFV3）_00440569.md) | 路由器标识(ROUTERID) | 10.8.20.1 | 全网规划 | 创建OSPFv3进程。 |
| [**ADD OSPFV3**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/OSPFv3管理/OSPFv3进程配置/创建OSPFv3进程配置（ADD OSPFV3）_00440569.md) | VPN的名称(VRFNAME) | vpn-paif | 已配置数据中获取 | 创建OSPFv3进程。 |
| [**ADD OSPFV3**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/OSPFv3管理/OSPFv3进程配置/创建OSPFv3进程配置（ADD OSPFV3）_00440569.md) | 使能BFD(BFDALLINTFFLG) | TRUE | 全网规划 | 创建OSPFv3进程。 |
| [**ADD OSPFV3**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/OSPFv3管理/OSPFv3进程配置/创建OSPFv3进程配置（ADD OSPFV3）_00440569.md) | 去使能VPN路由环路检测(VPNINSCAPSIMFLG) | TRUE | 全网规划 | 创建OSPFv3进程。 |
| [**ADD OSPFV3**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/OSPFv3管理/OSPFv3进程配置/创建OSPFv3进程配置（ADD OSPFV3）_00440569.md) | OSPFv3共网段虚拟系统使能标志(VIRTUALSYSFLAG) | TRUE | 全网规划 | 创建OSPFv3进程。 |
| [**ADD OSPFV3IMPORTROUTE**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/OSPFv3管理/OSPFv3引入路由配置/创建OSPFv3引入路由配置（ADD OSPFV3IMPORTROUTE）_00840849.md) | OSPFv3进程号(PROCID) | 6 | 已配置数据中获取 | OSPFv3引入的路由类型。 |
| [**ADD OSPFV3IMPORTROUTE**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/OSPFv3管理/OSPFv3引入路由配置/创建OSPFv3引入路由配置（ADD OSPFV3IMPORTROUTE）_00840849.md) | 拓扑标识(TOPOID) | 0 | 全网规划 | OSPFv3引入的路由类型。 |
| [**ADD OSPFV3IMPORTROUTE**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/OSPFv3管理/OSPFv3引入路由配置/创建OSPFv3引入路由配置（ADD OSPFV3IMPORTROUTE）_00840849.md) | 协议号(PROTOCOL) | wlr | 全网规划 | OSPFv3引入的路由类型。 |
| [**ADD OSPFV3IMPORTROUTE**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/OSPFv3管理/OSPFv3引入路由配置/创建OSPFv3引入路由配置（ADD OSPFV3IMPORTROUTE）_00840849.md) | 引入路由开销值配置(IMPTCOSTCFG) | FALSE | 全网规划 | OSPFv3引入的路由类型。 |
| [**ADD OSPFV3IMPORTROUTE**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/OSPFv3管理/OSPFv3引入路由配置/创建OSPFv3引入路由配置（ADD OSPFV3IMPORTROUTE）_00840849.md) | 引入路由标签配置(IMPTTAGCFG) | FALSE | 全网规划 | OSPFv3引入的路由类型。 |
| [**ADD OSPFV3IMPORTROUTE**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/OSPFv3管理/OSPFv3引入路由配置/创建OSPFv3引入路由配置（ADD OSPFV3IMPORTROUTE）_00840849.md) | 引入路由类型配置 (IMPTTYPECFG) | FALSE | 全网规划 | OSPFv3引入的路由类型。 |
| [**ADD OSPFV3AREA**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/OSPFv3管理/OSPFv3区域配置/创建OSPFv3区域配置（ADD OSPFV3AREA）_50120842.md) | OSPFv3进程号（PROCID） | 6 | 已配置数据中获取 | OSPFv3区域。 |
| [**ADD OSPFV3AREA**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/OSPFv3管理/OSPFv3区域配置/创建OSPFv3区域配置（ADD OSPFV3AREA）_50120842.md) | OSPFv3区域标识（AREAID） | 0.0.0.1 | 全网规划 | OSPFv3区域。 |
| [**ADD VPNINST**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/DN管理/VPN管理/VPN/增加VPN实例（ADD VPNINST）_82837045.md) | VPN实例（VPNINSTANCE） | vpn-s2b | 全网规划 | 配置VPN实例。 |
| [**ADD LOGICINF**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/DN管理/逻辑接口管理/逻辑接口配置/接口/增加逻辑接口（ADD LOGICINF）_82835378.md) | 逻辑接口名称(NAME) | Paif1/0/0 | 本端规划 | 逻辑接口。 |
| [**ADD LOGICINF**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/DN管理/逻辑接口管理/逻辑接口配置/接口/增加逻辑接口（ADD LOGICINF）_82835378.md) | 逻辑接口的IP版本(IPVERSION) | IPV6 | 本端规划 | 逻辑接口。 |
| [**ADD LOGICINF**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/DN管理/逻辑接口管理/逻辑接口配置/接口/增加逻辑接口（ADD LOGICINF）_82835378.md) | 逻辑接口的IPv6地址1(IPV6ADDRESS1) | fc00::1 | 本端规划 | 逻辑接口。 |
| [**ADD LOGICINF**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/DN管理/逻辑接口管理/逻辑接口配置/接口/增加逻辑接口（ADD LOGICINF）_82835378.md) | IPv6前缀长度1 (IPV6PREFIXLEN1) | 128 | 本端规划 | 逻辑接口。 |
| [**ADD LOGICINF**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/DN管理/逻辑接口管理/逻辑接口配置/接口/增加逻辑接口（ADD LOGICINF）_82835378.md) | VPN实例名称(VPNINSTANCE) | vpn-paif | 从已配置数据中获取 | 逻辑接口。 |

## [操作步骤](#ZH-CN_OPI_0272490128)

1. 参考初始配置中 **配置动态路由OSPFv3+BFD组网（IPv6）** 对应的组网配置。
2. 配置VPN实例。
  [**ADD L3VPNINST**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例/增加L3VPN实例（ADD L3VPNINST）_49802446.md)
  [**ADD VPNINSTAF**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例地址族/增加L3VPN实例地址族（ADD VPNINSTAF）_49802178.md)
3. 全局激活BFD。
  [**SET BFD**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/BFD管理/BFD全局配置/设置BFD全局属性（SET BFD）_00840937.md)
4. 配置OSPFv3路由。
    a. 创建OSPFv3进程。
      [**ADD OSPFV3**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/OSPFv3管理/OSPFv3进程配置/创建OSPFv3进程配置（ADD OSPFV3）_00440569.md)
    b. 可选：配置OSPF的路由器标识Router ID。
      [**MOD OSPFV3**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/OSPFv3管理/OSPFv3进程配置/修改OSPFv3进程配置（MOD OSPFV3）_00840769.md)
    c. 增加OSPFv3区域。
      [**ADD OSPFV3AREA**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/OSPFv3管理/OSPFv3区域配置/创建OSPFv3区域配置（ADD OSPFV3AREA）_50120842.md)
    d. 可选：设置OSPFv3引入路由类型。
      [**ADD OSPFV3IMPORTROUTE**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/OSPFv3管理/OSPFv3引入路由配置/创建OSPFv3引入路由配置（ADD OSPFV3IMPORTROUTE）_00840849.md)
5. 配置VPN实例及逻辑接口。
    a. 配置VPN实例。
      [**ADD VPNINST**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/DN管理/VPN管理/VPN/增加VPN实例（ADD VPNINST）_82837045.md)
      > **说明**
      > 外联口的VPN一定要与逻辑接口的VPN相同，否则从逻辑接口发出去的报文会查路由失败。
    b. 创建Paif接口。
      [**ADD LOGICINF**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/DN管理/逻辑接口管理/逻辑接口配置/接口/增加逻辑接口（ADD LOGICINF）_82835378.md)

## [任务示例](#ZH-CN_OPI_0272490128)

任务描述

本实例中，操作员在 UDG 上进行数据配置实现以下要求：

- UDG使用Paif逻辑接口与ePDG建立逻辑连接。
- UDG使用OSPFv3动态路由与ePDG建立起正常的IP连接。

脚本

1. 参考初始配置中**配置动态路由OSPFv3+BFD组网（IPv6）**对应的组网配置。
2.
  配置VPN实例。

  ```
  ADD L3VPNINST:VRFNAME="vpn-paif";
  ```

  ```
  ADD VPNINSTAF:VRFNAME="vpn-paif",AFTYPE=ipv6uni;
  ```
3.
  全局激活BFD。

  ```
  SET BFD:BFDENABLE=TRUE;
  ```
4. 配置OSPFv3动态路由数据。
    a. 创建OSPFv3进程。
      ```
      ADD OSPFV3:PROCID=6,VRFNAME="vpn-paif",ROUTERID="10.8.20.1",BFDALLINTFFLG=TRUE,VPNINSCAPSIMFLG=TRUE,VIRTUALSYSFLAG=TRUE;
      ```
    b. 设置OSPFv3引入路由类型。
      ```
      ADD OSPFV3IMPORTROUTE:PROCID=6, TOPOID =0,PROTOCOL=wlr,IMPTCOSTCFG=FALSE,IMPTTAGCFG=FALSE,IMPTTYPECFG=FALSE;
      ```
    c. 增加OSPFv3区域。
      ```
      ADD OSPFV3AREA:PROCID=6,AREAID="0.0.0.1";
      ```
5. 配置VPN实例及逻辑接口。
    a. 配置VPN实例。
      ```
      ADD VPNINST: VPNINSTANCE ="vpn-paif";
      ```
    b. 配置逻辑接口。
      ```
      ADD LOGICINF:NAME="Paif1/0/0",IPVERSION=IPV6,IPV6ADDRESS1="fc00::1",VPNINSTANCE="vpn-paif",IPV6PREFIXLEN1=128;
      ```
