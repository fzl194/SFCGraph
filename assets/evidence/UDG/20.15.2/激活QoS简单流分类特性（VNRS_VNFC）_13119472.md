# 激活QoS简单流分类特性 （VNRS_VNFC）

- [操作场景](#ZH-CN_OPI_0213119472__1.3.1)
- [对系统的影响](#ZH-CN_OPI_0213119472__1.3.2)
- [必备事项](#ZH-CN_OPI_0213119472__1.3.3)
- [操作流程](#ZH-CN_OPI_0213119472__1.3.4)
- [操作步骤](#ZH-CN_OPI_0213119472__1.3.5)
- [任务示例](#ZH-CN_OPI_0213119472__1.3.6)

## [操作场景](#ZH-CN_OPI_0213119472)

本操作指导介绍在运行网络配置基于简单流分类的Qos策略的操作过程。

在以太主接口及以太子接口上配置基于简单流分类的QoS策略，比如说IP报文、VLAN报文的优先级。可以先在该接口上配置DiffServ域， 然后对该DS域配置各种优先级的映射关系，接口上的报文会按照DiffServ域中的映射关系进行简单流分类映射。

简单流分类通常配置在网络的核心位置。

当需要对来自上游设备的VLAN报文进行QoS调度的时候，可以通过本命令配置DiffServ域中VLAN报文的802.1p优先级到路由器内部服务等级之间的映射，并为报文着色。对于IP报文，则是将DSCP值映射成内部服务等级，并着色。将DiffServ域绑定到报文的入接口后，QoS将根据报文映射的路由器内部服务等级和颜色进行拥塞管理和拥塞避免。

对于下行报文则将路由器内部的服务等级和颜色映射成对应的DSCP值或者802.1p值。

> **说明**
> NP卡场景下，不支持接口重定向到指定VPN功能。

## [对系统的影响](#ZH-CN_OPI_0213119472)

该操作对系统正常运行无影响。

## [必备事项](#ZH-CN_OPI_0213119472)

前提条件

已经创建对应DiffServ域。

数据

需要准备本端规划的数据，无需准备与对端网元协商的数据，如 [表1](#ZH-CN_OPI_0213119472__zh-cn_opi_0134584205_tab_1) 所示。

*表1 需要准备的数据*

| 类别 | 参数 | 取值样例 | 获取方法 | 相关命令 |
| --- | --- | --- | --- | --- |
| QOSIFTRUST接口绑定DS域 | DS域名<br>(DSNAME) | ds1 | 本端规划 | [**ADD QOSIFTRUST**](../../../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/安全管理/QoS管理/接口信任信息/增加QoS接口信任（ADD QOSIFTRUST）_50121734.md) |
| QOSIFTRUST接口绑定DS域 | 接口名称（IFNAME） | Ethernet<br>64/0/3 | 本端规划 | [**ADD QOSIFTRUST**](../../../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/安全管理/QoS管理/接口信任信息/增加QoS接口信任（ADD QOSIFTRUST）_50121734.md) |
| QOSIFTRUST接口绑定DS域 | 8021p标志<br>(FLAG8021P) | 否 | 本端规划 | [**ADD QOSIFTRUST**](../../../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/安全管理/QoS管理/接口信任信息/增加QoS接口信任（ADD QOSIFTRUST）_50121734.md) |
| QOSDIFFERSERV配置DiffServ域 | DS域名<br>(DSNAME) | ds1 | 本端规划 | [**ADD QOSDIFFERSERV**](../../../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/安全管理/QoS管理/DS域配置/增加DS域（ADD QOSDIFFERSERV）_00841105.md) |
| QOSBA报文映射 | DS域名<br>(DSNAME) | ds1 | 本端规划 | [**SET QOSBA**](../../../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/安全管理/QoS管理/BA映射关系/设置QoS BA（SET QOSBA）_00441521.md) |
| QOSBA报文映射 | ba类型<br>(BATYPE) | ip_dscp | 本端规划 | [**SET QOSBA**](../../../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/安全管理/QoS管理/BA映射关系/设置QoS BA（SET QOSBA）_00441521.md) |
| QOSBA报文映射 | ba值<br>(BAVALUE) | 1 | 本端规划 | [**SET QOSBA**](../../../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/安全管理/QoS管理/BA映射关系/设置QoS BA（SET QOSBA）_00441521.md) |
| QOSBA报文映射 | 服务<br>分类<br>(SERVICECLASS) | be | 本端规划 | [**SET QOSBA**](../../../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/安全管理/QoS管理/BA映射关系/设置QoS BA（SET QOSBA）_00441521.md) |
| QOSBA报文映射 | 颜色<br>分类<br>(COLOR) | green | 本端规划 | [**SET QOSBA**](../../../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/安全管理/QoS管理/BA映射关系/设置QoS BA（SET QOSBA）_00441521.md) |
| 设置QoS PHB | DS域名<br>(DSNAME) | ds1 | 本端规划 | [**SET QOSPHB**](../../../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/安全管理/QoS管理/PHB映射关系/设置QoS PHB（SET QOSPHB）_00840685.md) |
| 设置QoS PHB | PHB类型<br>(PHBTYPE) | 8021p | 本端规划 | [**SET QOSPHB**](../../../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/安全管理/QoS管理/PHB映射关系/设置QoS PHB（SET QOSPHB）_00840685.md) |
| 设置QoS PHB | PHB值<br>(PHBVALUE) | 1 | 本端规划 | [**SET QOSPHB**](../../../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/安全管理/QoS管理/PHB映射关系/设置QoS PHB（SET QOSPHB）_00840685.md) |
| 设置QoS PHB | 服务<br>分类<br>(SERVICECLASS) | be | 本端规划 | [**SET QOSPHB**](../../../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/安全管理/QoS管理/PHB映射关系/设置QoS PHB（SET QOSPHB）_00840685.md) |
| 设置QoS PHB | 颜色<br>分类<br>(COLOR) | green | 本端规划 | [**SET QOSPHB**](../../../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/安全管理/QoS管理/PHB映射关系/设置QoS PHB（SET QOSPHB）_00840685.md) |
| 添加禁止QoS优先级映射的类型 | 接口名称（IFNAME） | Ethernet<br>64/0/3 | 本端规划 | [**ADD QOSIFPHB**](../../../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/安全管理/QoS管理/QoS IF PHB/添加禁止QoS优先级映射的类型（ADD QOSIFPHB）_00841181.md) |
| 添加禁止QoS优先级映射的类型 | 出接口报文的优先级字段映射类型<br>(<br>PHBTYPE<br>) | dscp | 本端规划 | [**ADD QOSIFPHB**](../../../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/安全管理/QoS管理/QoS IF PHB/添加禁止QoS优先级映射的类型（ADD QOSIFPHB）_00841181.md) |
| QOSRDRVPN重定向VPN | 接口名称（IFNAME） | Ethernet<br>64/0/3 | 本端规划 | [**ADD QOSRDRVPN**](../../../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/安全管理/QoS管理/重定向VPN/增加QoS重定向VPN（ADD QOSRDRVPN）_00441441.md) |
| QOSRDRVPN重定向VPN | VPN名称<br>(VRFNAME) | vpn1 | 本端规划 | [**ADD QOSRDRVPN**](../../../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/安全管理/QoS管理/重定向VPN/增加QoS重定向VPN（ADD QOSRDRVPN）_00441441.md) |

## [操作流程](#ZH-CN_OPI_0213119472)

激活QoS简单流分类特性操作流程如 [图1](#ZH-CN_OPI_0213119472__zh-cn_opi_0134584205_fig_dc_fenix_nps_mml_cfg_qos_000102) 所示。

**图1** 激活QoS简单流分类特性操作流程

<br>

![](激活QoS简单流分类特性（VNRS_VNFC）_13119472.assets/zh-cn_image_0262802181.png)

## [操作步骤](#ZH-CN_OPI_0213119472)

1. （可选）配置DiffServ域。
  在 “MML命令行-UDG” 窗口上执行：
  [**ADD QOSDIFFERSERV**](../../../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/安全管理/QoS管理/DS域配置/增加DS域（ADD QOSDIFFERSERV）_00841105.md) : DSNAME="DS 名称 ";
  > **说明**
  > 默认存在两个DiffServ域，default和5p3d，其中5p3d域不允许修改。
2. （可选）当配置DiffServ域时，可以修改上行或者下行的映射关系。
  在 “MML命令行-UDG” 窗口上执行：
  [**SET QOSBA**](../../../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/安全管理/QoS管理/BA映射关系/设置QoS BA（SET QOSBA）_00441521.md) : DSNAME="DS域名",BATYPE= ba类型 ,BAVALUE= ba值 ,SERVICECLASS=服务 分类 ,COLOR=颜色 分类 ;
  [**SET QOSPHB**](../../../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/安全管理/QoS管理/PHB映射关系/设置QoS PHB（SET QOSPHB）_00840685.md) : DSNAME="DS域名",PHBTYPE= PHB类型 ,PHBVALUE= PHB值 ,SERVICECLASS=服务 分类 ,COLOR=颜色 分类 ;
3. 配置接口绑定相应的DiffServ域。
  在 “MML命令行-UDG” 窗口上执行：
  [**ADD QOSIFTRUST**](../../../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/安全管理/QoS管理/接口信任信息/增加QoS接口信任（ADD QOSIFTRUST）_50121734.md) : DSNAME=" ds域 ", IFNAME="接口名 称 ";
  > **说明**
  > 只有以太子接口、GE子接口和Eth-Trunk主接口支持802.1p映射。
4. （可选）配置接口重定向到指定VPN。
  在 “MML命令行-UDG” 窗口上执行：
  [**ADD QOSRDRVPN**](../../../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/安全管理/QoS管理/重定向VPN/增加QoS重定向VPN（ADD QOSRDRVPN）_00441441.md) : IFNAME="接口名称", VRFNAME =" VPN名称 ";
  > **说明**
  > 必须先创建相应的VPN实例，只支持在以太主接口和GE主接口进行配置。
5. （可选）激活QoS不检查PHB表。
  在 “MML命令行-UDG” 窗口上执行：
  [**ADD QOSIFPHB**](../../../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/安全管理/QoS管理/QoS IF PHB/添加禁止QoS优先级映射的类型（ADD QOSIFPHB）_00841181.md) : IFNAME="接口名 称 ", PHBTYPE= 出接口报文的优先级字段映射类型 ;

## [任务示例](#ZH-CN_OPI_0213119472)

任务描述

VNF1与路由器接口Ethernet 64/0/2 在同一个网段，VNF2与路由器接口Ethernet 64/0/3 在同一个网段，在接口Ethernet 64/0/2 绑定DiffServ域default，在接口Ethernet 64/0/3 绑定DiffServ域5p3d。在VNF1上ping VNF2，并设置dscp值，在VNF2上查看收到的ping报文的dscp值，在经过入接口Ethernet 64/0/2 ，从dscp到路由内部服务等级及报文着色映射，在经过出接口Ethernet 64/0/3 ，从路由内部服务等级及报文颜色到外部dscp值的映射，最终dscp映射值是否与预期的一致。在简单流分类的下行，由于报文的服务等级、颜色等信息被存放在PHB表中，当报文转发时，检查PHB表，识别报文的业务优先级，进而根据DS域中的映射关系将路由器内部业务优先级映射成外部业务优先级。报文在接口 64/0/3 下行转发时不会检查PHB表。

**图2** QoS简单流分类配置示意图

<br>

![](激活QoS简单流分类特性（VNRS_VNFC）_13119472.assets/zh-cn_image_0262802184.png)

脚本

//对以太接口Ethernet 64/0/2 绑定DiffServ域default。

```
ADD QOSIFTRUST
: DSNAME="default", IFNAME="Ethernet
64/0/2
";
```

//对以太接口Ethernet 64/0/3 绑定DiffServ域5p3d。

```
ADD QOSIFTRUST
: DSNAME="5p3d", IFNAME="Ethernet
64/0/3
";
```

//在VNF1 ping的时候设置报文dscp值为0，最终在VNF2上得到的报文dscp值将是0。

```
Default domain:ip-dscp-inbound 0 phb be green
5p3d domain:ip-dscp-outbound be green map 0
```

//对以太接口Ethernet 64/0/3 去激活QoS不检查PHB表。

```
ADD QOSIFPHB
: IFNAME="Ethernet
64/0/3
",PHBTYPE=dscp;
```
