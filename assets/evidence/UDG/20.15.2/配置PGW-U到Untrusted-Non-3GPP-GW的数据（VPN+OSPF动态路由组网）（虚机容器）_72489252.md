# 配置PGW-U到Untrusted Non-3GPP GW的数据（VPN+OSPF动态路由组网）（虚机容器）

- [操作场景](#ZH-CN_OPI_0272489252__1.3.1)
- [必备事项](#ZH-CN_OPI_0272489252__1.3.2)
- [操作步骤](#ZH-CN_OPI_0272489252__1.3.3)
- [任务示例](#ZH-CN_OPI_0272489252__1.3.4)

## [操作场景](#ZH-CN_OPI_0272489252)

> **说明**
> 适用于PGW-U。

UDG 与ePDG互通，用于部署WiFi用户接入EPC网络。

- 逻辑接口：Paif接口。
- 路由：OSPF动态路由，各接口对外发布的路由优先级相同，作为等价路由实现物理链路的负荷分担。

## [必备事项](#ZH-CN_OPI_0272489252)

前提条件

- 请仔细阅读[IPFD-015001 VRF功能](../../../IP基本特性/IPFD-015000 VPN功能/IPFD-015001 VRF功能_61317255.md)和[IPFD-014001 支持OSPF特性概述](../../../IP基本特性/IPFD-014000 路由功能/IPFD-014001 支持OSPF/IPFD-014001 支持OSPF特性概述_61317384.md)。
- UDG与网络实体之间的网络环境已经构建完成。
- 操作员了解UDG各类接口的类型及命名规范。

数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| [**ADD L3VPNINST**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例/增加L3VPN实例（ADD L3VPNINST）_49802446.md) | VPN实例名称（VRFNAME） | vpn-s2b | 全网规划 | VPN实例全网统一规划，一条通信路径上所有节点绑定的VPN实例要一致，才能正常通信。 |
| [**ADD VPNINSTAF**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例地址族/增加L3VPN实例地址族（ADD VPNINSTAF）_49802178.md) | VPN实例名称（VRFNAME） | vpn-s2b | 已配置数据中获取 | 设置指定VPN实例下的地址族。 |
| [**ADD VPNINSTAF**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例地址族/增加L3VPN实例地址族（ADD VPNINSTAF）_49802178.md) | 地址族类型（AFTYPE） | ipv4uni | 本端规划 | 设置指定VPN实例下的地址族。 |
| [**ADD VPNINSTAF**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例地址族/增加L3VPN实例地址族（ADD VPNINSTAF）_49802178.md) | 路由标识（VRFRD） | 100:1 | 本端规划 | 设置指定VPN实例下的地址族。 |
| [**ADD VPNINST**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/DN管理/VPN管理/VPN/增加VPN实例（ADD VPNINST）_82837045.md) | VPN实例（VPNINSTANCE） | vpn-s2b | 全网规划 | 配置VPN实例。 |
| [**ADD LOGICINF**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/DN管理/逻辑接口管理/逻辑接口配置/接口/增加逻辑接口（ADD LOGICINF）_82835378.md) | 逻辑接口名称（NAME） | Paif1/1/0 | 固定取值 | 创建Paif接口。 |
| [**ADD LOGICINF**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/DN管理/逻辑接口管理/逻辑接口配置/接口/增加逻辑接口（ADD LOGICINF）_82835378.md) | 逻辑接口的IP版本（IPVERSION） | IPv4 | 本端规划 | 创建Paif接口。 |
| [**ADD LOGICINF**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/DN管理/逻辑接口管理/逻辑接口配置/接口/增加逻辑接口（ADD LOGICINF）_82835378.md) | 逻辑接口的IPv4地址1（IPV4ADDRESS1） | 10.10.10.10 | 本端规划 | 创建Paif接口。 |
| [**ADD LOGICINF**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/DN管理/逻辑接口管理/逻辑接口配置/接口/增加逻辑接口（ADD LOGICINF）_82835378.md) | 逻辑接口的IPv4掩码1（IPV4MASK1） | 255.255.255.255 | 本端规划 | 创建Paif接口。 |
| [**ADD LOGICINF**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/DN管理/逻辑接口管理/逻辑接口配置/接口/增加逻辑接口（ADD LOGICINF）_82835378.md) | VPN实例名称（VPNINSTANCE） | vpn-s2b | 已配置数据中获取 | 创建Paif接口。 |
| [**SET BFD**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/BFD管理/BFD全局配置/设置BFD全局属性（SET BFD）_00840937.md) | BFD使能标志（BFDENABLE） | TRUE | 本端规划 | 设置BFD全局属性。 |
| [**ADD OSPF**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/OSPF管理/OSPF进程配置/创建OSPF进程配置（ADD OSPF）_00866089.md) | 进程号(PROCID) | 6 | 全网规划 | UDG<br>到ePDG动态路由的OSPF进程号。<br>说明：路由器的Router ID必须全网唯一。 |
| [**ADD OSPF**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/OSPF管理/OSPF进程配置/创建OSPF进程配置（ADD OSPF）_00866089.md) | VPN名称(VRFNAME) | vpn-s2b | 已配置数据中获取 | UDG<br>到ePDG动态路由的OSPF进程号。<br>说明：路由器的Router ID必须全网唯一。 |
| [**ADD OSPF**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/OSPF管理/OSPF进程配置/创建OSPF进程配置（ADD OSPF）_00866089.md) | 路由器标识(SCHEMAROUID) | 10.8.20.1 | 全网规划 | UDG<br>到ePDG动态路由的OSPF进程号。<br>说明：路由器的Router ID必须全网唯一。 |
| [**ADD OSPFAREA**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/OSPF管理/OSPF区域配置/创建OSPF区域配置（ADD OSPFAREA）_50120650.md) | 进程号(PROCID) | 6 | 已配置数据中获取 | 在OSPF进程下创建区域。 |
| [**ADD OSPFAREA**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/OSPF管理/OSPF区域配置/创建OSPF区域配置（ADD OSPFAREA）_50120650.md) | 区域号（AREAID） | 0.0.0.1 | 全网规划 | 在OSPF进程下创建区域。 |
| [**ADD OSPFNETWORK**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/OSPF管理/指定OSPF运行的接口及所属区域/指定OSPF运行的接口及所属区域（ADD OSPFNETWORK）_00601465.md) | 进程号(PROCID) | 6 | 已配置数据中获取 | 在OSPF进程下的区域增加一个网段。 |
| [**ADD OSPFNETWORK**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/OSPF管理/指定OSPF运行的接口及所属区域/指定OSPF运行的接口及所属区域（ADD OSPFNETWORK）_00601465.md) | 区域号（AREAID） | 0.0.0.1 | 全网规划 | 在OSPF进程下的区域增加一个网段。 |
| [**ADD OSPFNETWORK**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/OSPF管理/指定OSPF运行的接口及所属区域/指定OSPF运行的接口及所属区域（ADD OSPFNETWORK）_00601465.md) | IP地址（IPADDRESS） | 10.8.7.0<br>10.8.8.0 | 全网规划 | 在OSPF进程下的区域增加一个网段。 |
| [**ADD OSPFNETWORK**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/OSPF管理/指定OSPF运行的接口及所属区域/指定OSPF运行的接口及所属区域（ADD OSPFNETWORK）_00601465.md) | 反掩码（WILDCARDMASK） | 0.0.0.15 | 全网规划 | 在OSPF进程下的区域增加一个网段。 |
| [**ADD OSPFIMPORTROUTE**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/OSPF管理/引入外部路由配置/创建OSPF引入路由配置（ADD OSPFIMPORTROUTE）_00601057.md) | OSPF进程号（PROCID） | 6 | 已配置数据中获取 | 将外部路由引入到OSPF域中，并在OSPF域中发布引入的路由信息。 |
| [**ADD OSPFIMPORTROUTE**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/OSPF管理/引入外部路由配置/创建OSPF引入路由配置（ADD OSPFIMPORTROUTE）_00601057.md) | 协议分类 （PROTOCOL） | wlr | 全网规划 | 将外部路由引入到OSPF域中，并在OSPF域中发布引入的路由信息。 |

## [操作步骤](#ZH-CN_OPI_0272489252)

1. 参考初始配置中 **配置动态路由OSPF+BFD组网（IPv4）** 对应组网配置。
2. 创建L3VPN实例。
  [**ADD L3VPNINST**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例/增加L3VPN实例（ADD L3VPNINST）_49802446.md)
  [**ADD VPNINSTAF**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例地址族/增加L3VPN实例地址族（ADD VPNINSTAF）_49802178.md)
3. 配置VPN实例。
  [**ADD VPNINST**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/DN管理/VPN管理/VPN/增加VPN实例（ADD VPNINST）_82837045.md)
4. 全局激活BFD。
  [**SET BFD**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/BFD管理/BFD全局配置/设置BFD全局属性（SET BFD）_00840937.md)
  > **说明**
  > 参数“DELAYUPTIMER”（会话延迟UP时间）和“TOSEXP”（动态会话报文优先级）可以不用输入，使用默认值即可。
5. 创建OSPF进程。
  [**ADD OSPF**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/OSPF管理/OSPF进程配置/创建OSPF进程配置（ADD OSPF）_00866089.md)
  > **说明**
  > - UDG 支持VPN多实例，需要取消环路检查，否则会导致OSPF路由引入失败。需要将 “VPNINSCAPSIMFLG” 配置为 “TRUE” 。
  > - 优选用户配置的Router ID。如果未配置，则选择OSPF进程所在VRF内或者公网内的最大接口IP地址。
  > - 如果需要为OSPF动态路由绑定BFD会话，通过[**ADD OSPF**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/OSPF管理/OSPF进程配置/创建OSPF进程配置（ADD OSPF）_00866089.md)配置“使能BFD”为“TRUE”。
  > - 当OSPF路由配置共网段时，需[**MOD OSPFAREA**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/OSPF管理/OSPF区域配置/修改OSPF区域配置（MOD OSPFAREA）_50121130.md)将“VIRTUALSYSFLAG”配置为“TRUE”。
6. 增加OSPF区域。
  根据不同的验证类型选择不同的区域配置。
    - 不指定验证类型。
      [**ADD OSPFAREA**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/OSPF管理/OSPF区域配置/创建OSPF区域配置（ADD OSPFAREA）_50120650.md)
      > **说明**
      > - “AERATYPE（区域类型）”可以设置为“NSSA”或“Normal”。
      > - 如果参数“AERATYPE（区域类型）”配置为“NSSA”时, 必须配置Loopback地址，这样设备会自动选取该Loopback地址作为FA。当有其他设备存在多条开销值相同的路径到NSSA设备时，可以形成负载分担。
    - 指定验证类型。
      [**ADD OSPFAREAAUTH**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/OSPF管理/OSPF区域认证配置/修改OSPF区域认证配置（MOD OSPFAREAAUTH）_00600321.md)
7. 增加运行OSPF协议的接口。
  [**ADD OSPFNETWORK**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/OSPF管理/指定OSPF运行的接口及所属区域/指定OSPF运行的接口及所属区域（ADD OSPFNETWORK）_00601465.md)
8. **可选** ：配置OSPF协议的接口属性。
  [**ADD OSPFINTERFACE**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/OSPF管理/OSPF接口配置/创建OSPF接口配置（ADD OSPFINTERFACE）_00866569.md)
  > **说明**
  > - 参数“NETWORKTYPE”（网络类型）选择“broadcast”、“nbma”、“p2p”或“p2mp”。
  > - 广播或NBMA网络中，根据此接口优先级选举DR和BDR路由器，“优先级”设置为“0”表示不参与DR和BDR的选举。为避免VNF被选为DR或BDR，建议将VNF“优先级”配置为0，对端配置为非0。
9. 设置OSPF引入路由类型。
  [**ADD OSPFIMPORTROUTE**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/OSPF管理/引入外部路由配置/创建OSPF引入路由配置（ADD OSPFIMPORTROUTE）_00601057.md)
10. 创建Paif接口。
  [**ADD LOGICINF**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/DN管理/逻辑接口管理/逻辑接口配置/接口/增加逻辑接口（ADD LOGICINF）_82835378.md)

## [任务示例](#ZH-CN_OPI_0272489252)

任务描述

本实例中，操作员在 UDG 上进行数据配置实现以下要求：

- UDG使用Paif逻辑接口与ePDG建立逻辑连接。
- UDG使用OSPF动态路由与ePDG建立起正常的IP连接。

脚本

1. 参考初始配置中**配置动态路由OSPF+BFD组网（IPv4）**对应组网配置。
2. 配置L3VPN实例。
  ```
  ADD L3VPNINST:VRFNAME="vpn-s2b";
  ```
  ```
  ADD VPNINSTAF:VRFNAME="vpn-s2b",AFTYPE=ipv4uni,VRFRD=100:1;
  ```
3. 配置VPN实例。
  ```
  ADD VPNINST: VPNINSTANCE ="vpn-s2b";
  ```
4. 全局激活BFD。
  ```
  SET BFD: BFDENABLE=TRUE;
  ```
5. 配置动态路由数据。
  ```
  ADD OSPF:PROCID=6,VRFNAME="vpn-s2b",SCHEMAROUID="10.8.20.1";
  ```
  ```
  ADD OSPFIMPORTROUTE:PROCID=6, TOPOID =0,PROTOCOL=wlr, IMPTCOSTCFG=FALSE, IMPTTAGCFG=FALSE, IMPTTYPECFG=FALSE;
  ```
  ```
  MOD OSPF:PROCID=6,BFDALLINTFFLG=TRUE;
  ```
  ```
  ADD OSPFAREA:PROCID=6,AREAID="0.0.0.1";
  ```
  ```
  ADD OSPFNETWORK:PROCID=6,AREAID="0.0.0.1",IPADDRESS="10.8.7.0",WILDCARDMASK="0.0.0.15";
  ```
  ```
  ADD OSPFNETWORK:PROCID=6,AREAID="0.0.0.1",IPADDRESS="10.8.8.0",WILDCARDMASK="0.0.0.15";
  ```
6. 创建Paif接口。
  ```
  ADD LOGICINF:NAME="Paif1/1/0",IPVERSION=IPV4,IPV4ADDRESS1="10.10.10.10",IPV4MASK1="255.255.255.255",VPNINSTANCE="vpn-s2b";
  ```
