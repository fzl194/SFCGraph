# 激活外部网元地址分配的IPv6 Prefix Delegation功能

- [操作场景](#ZH-CN_OPI_0280269177__1.3.1)
- [必备事项](#ZH-CN_OPI_0280269177__1.3.2)
- [操作步骤](#ZH-CN_OPI_0280269177__1.3.3)
- [任务示例](#ZH-CN_OPI_0280269177__1.3.4)

## [操作场景](#ZH-CN_OPI_0280269177)

运营商支持基于外部网元为UE分配地址时，激活本特性。

> **说明**
> 适用于PGW-U、UPF。

## [必备事项](#ZH-CN_OPI_0280269177)

前提条件

请仔细阅读 [GWFD-020406 IPv6 Prefix Delegation](../GWFD-020406 IPv6 Prefix Delegation_79370033.md) 。

数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| [**ADD VPNINST**](../../../../../OM参考/命令/UDG MML命令/用户面服务管理/DN管理/VPN管理/VPN/增加VPN实例（ADD VPNINST）_82837045.md) | VPN实例（VPNINSTANCE） | vpn1 | 全网规划 | - |
| [**ADD POOLGROUP**](../../../../../OM参考/命令/UDG MML命令/用户面服务管理/会话管理/会话地址管理/地址池组/添加地址池组（ADD POOLGROUP）_82837138.md) | 地址池组名称（POOLGRPNAME） | poolgroup1 | 本端规划 | - |
| [**ADD POOL**](../../../../../OM参考/命令/UDG MML命令/用户面服务管理/会话管理/会话地址管理/地址池配置/添加地址池（ADD POOL）_82837132.md) | 地址池名称（POOLNAME） | testpool | 本端规划 | - |
| [**ADD POOL**](../../../../../OM参考/命令/UDG MML命令/用户面服务管理/会话管理/会话地址管理/地址池配置/添加地址池（ADD POOL）_82837132.md) | 地址池类型（POOLTYPE） | EXTERNAL | 本端规划 | - |
| [**ADD POOL**](../../../../../OM参考/命令/UDG MML命令/用户面服务管理/会话管理/会话地址管理/地址池配置/添加地址池（ADD POOL）_82837132.md) | 检查地址合法性（CHECKIPVALID） | ENABLE | 本端规划 | - |
| [**ADD POOL**](../../../../../OM参考/命令/UDG MML命令/用户面服务管理/会话管理/会话地址管理/地址池配置/添加地址池（ADD POOL）_82837132.md) | 绑定VPN（HASVPN） | ENABLE | 本端规划 | - |
| [**ADD POOL**](../../../../../OM参考/命令/UDG MML命令/用户面服务管理/会话管理/会话地址管理/地址池配置/添加地址池（ADD POOL）_82837132.md) | VPN实例名（VPNINSTANCE） | vpn1 | 已配置数据中获取 | 可以使用<br>[**LST VPNINST**](../../../../../OM参考/命令/UDG MML命令/用户面服务管理/DN管理/VPN管理/VPN/查询VPN实例（LST VPNINST）_82837047.md)<br>命令进行查询。 |
| [**ADD SECTION**](../../../../../OM参考/命令/UDG MML命令/用户面服务管理/会话管理/会话地址管理/地址段配置/添加地址池IP地址段（ADD SECTION）_82837114.md) | 地址池名称（POOLNAME） | testpool | 本端规划 | 可以使用<br>[**LST POOL**](../../../../../OM参考/命令/UDG MML命令/用户面服务管理/会话管理/会话地址管理/地址池配置/显示地址池（LST POOL）_82837135.md)<br>命令进行查询。 |
| [**ADD SECTION**](../../../../../OM参考/命令/UDG MML命令/用户面服务管理/会话管理/会话地址管理/地址段配置/添加地址池IP地址段（ADD SECTION）_82837114.md) | 地址段号（SECTIONNUM） | 1 | 本端规划 | - |
| [**ADD SECTION**](../../../../../OM参考/命令/UDG MML命令/用户面服务管理/会话管理/会话地址管理/地址段配置/添加地址池IP地址段（ADD SECTION）_82837114.md) | IP地址类型（IPVERSION） | IPV6 | 本端规划 | - |
| [**ADD SECTION**](../../../../../OM参考/命令/UDG MML命令/用户面服务管理/会话管理/会话地址管理/地址段配置/添加地址池IP地址段（ADD SECTION）_82837114.md) | IPv6前缀起始地址（V6PREFIXSTART） | fc00:0000:0000:fcee:0000:0000:0000:0000 | 全网规划 | 本地地址池支持IPv4和IPv6类型，如果规划UE IPv4v6双栈地址，则需要配置两种类型的地址池。 |
| [**ADD SECTION**](../../../../../OM参考/命令/UDG MML命令/用户面服务管理/会话管理/会话地址管理/地址段配置/添加地址池IP地址段（ADD SECTION）_82837114.md) | IPv6前缀结束地址（V6PREFIXEND） | fc00:0000:0000:fcef:ffff:ffff:ffff:ffff | 全网规划 | - |
| [**ADD SECTION**](../../../../../OM参考/命令/UDG MML命令/用户面服务管理/会话管理/会话地址管理/地址段配置/添加地址池IP地址段（ADD SECTION）_82837114.md) | IPv6前缀长度（V6PREFIXLENGTH） | 63 | 全网规划 | 前缀长度范围为49~64，当前缀长度小于64时，则表示该地址池采用IPv6 Prefix Delegation方式分配。 |
| [**ADD POOLBINDGROUP**](../../../../../OM参考/命令/UDG MML命令/用户面服务管理/会话管理/会话地址管理/地址池绑定地址池组/绑定地址池到地址池组（ADD POOLBINDGROUP）_82837143.md) | 地址池组名称(POOLGROUPNAME) | poolgroup1 | 本端规划 | 可以使用<br>[**LST POOLBINDGROUP**](../../../../../OM参考/命令/UDG MML命令/用户面服务管理/会话管理/会话地址管理/地址池绑定地址池组/显示地址池与地址池组绑定关系（LST POOLBINDGROUP）_82837146.md)<br>命令进行查询。 |
| [**ADD POOLBINDGROUP**](../../../../../OM参考/命令/UDG MML命令/用户面服务管理/会话管理/会话地址管理/地址池绑定地址池组/绑定地址池到地址池组（ADD POOLBINDGROUP）_82837143.md) | 地址池名称(POOLNAME) | testpool | 本端规划 | 可以使用<br>[**LST POOL**](../../../../../OM参考/命令/UDG MML命令/用户面服务管理/会话管理/会话地址管理/地址池配置/显示地址池（LST POOL）_82837135.md)<br>命令进行查询。 |
| [**ADD APN**](../../../../../OM参考/命令/UDG MML命令/用户面服务管理/DN管理/APN管理/APN/添加APN配置（ADD APN）_82837014.md) | APN名称(APN) | apn-test | 本端规划 | - |
| [**ADD APN**](../../../../../OM参考/命令/UDG MML命令/用户面服务管理/DN管理/APN管理/APN/添加APN配置（ADD APN）_82837014.md) | 绑定VPN(HASVPN) | ENABLE | 本端规划 | - |
| [**ADD APN**](../../../../../OM参考/命令/UDG MML命令/用户面服务管理/DN管理/APN管理/APN/添加APN配置（ADD APN）_82837014.md) | VPN实例名(VPNINSTANCE) | vpn1 | 本端规划 | 可以使用<br>[**LST VPNINST**](../../../../../OM参考/命令/UDG MML命令/用户面服务管理/DN管理/VPN管理/VPN/查询VPN实例（LST VPNINST）_82837047.md)<br>命令进行查询。 |
| [**ADD POOLGRPMAP**](../../../../../OM参考/命令/UDG MML命令/用户面服务管理/会话管理/会话地址管理/地址池组映射关系/添加地址池组映射关系（ADD POOLGRPMAP）_82837148.md) | 映射规则名称(MAPPINGNAME) | mapping1 | 本端规划 | - |
| [**ADD POOLGRPMAP**](../../../../../OM参考/命令/UDG MML命令/用户面服务管理/会话管理/会话地址管理/地址池组映射关系/添加地址池组映射关系（ADD POOLGRPMAP）_82837148.md) | APN名称(APN) | apn-test | 本端规划 | 可以使用<br>[查询APN配置（LST APN）](../../../../../OM参考/命令/UDG MML命令/用户面服务管理/DN管理/APN管理/APN/查询APN配置（LST APN）_82837017.md)<br>命令进行查询。 |
| [**ADD POOLGRPMAP**](../../../../../OM参考/命令/UDG MML命令/用户面服务管理/会话管理/会话地址管理/地址池组映射关系/添加地址池组映射关系（ADD POOLGRPMAP）_82837148.md) | 地址池组名称(POOLGROUPNAME) | poolgroup1 | 本端规划 | 可以使用<br>[**LST POOLBINDGROUP**](../../../../../OM参考/命令/UDG MML命令/用户面服务管理/会话管理/会话地址管理/地址池绑定地址池组/显示地址池与地址池组绑定关系（LST POOLBINDGROUP）_82837146.md)<br>命令进行查询。 |
| [**ADD OSPFV3**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/OSPFv3管理/OSPFv3进程配置/创建OSPFv3进程配置（ADD OSPFV3）_00440569.md) | OSPFv3进程号(PROCID) | 6 | 已配置数据中获取 | - |
| [**ADD OSPFV3**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/OSPFv3管理/OSPFv3进程配置/创建OSPFv3进程配置（ADD OSPFV3）_00440569.md) | 路由器标识(ROUTERID) | 10.8.25.1 | 已配置数据中获取 | 须知：<br>Router ID必须全网唯一。 |
| [**ADD OSPFV3**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/OSPFv3管理/OSPFv3进程配置/创建OSPFv3进程配置（ADD OSPFV3）_00440569.md) | VPN的名称(VRFNAME) | vpn1 | 全网规划 | 可以使用<br>[**LST VPNINST**](../../../../../OM参考/命令/UDG MML命令/用户面服务管理/DN管理/VPN管理/VPN/查询VPN实例（LST VPNINST）_82837047.md)<br>命令进行查询。 |
| [**ADD OSPFV3**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/OSPFv3管理/OSPFv3进程配置/创建OSPFv3进程配置（ADD OSPFV3）_00440569.md) | 使能BFD(BFDALLINTFFLG) | TRUE | 全网规划 | - |
| [**ADD OSPFV3**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/OSPFv3管理/OSPFv3进程配置/创建OSPFv3进程配置（ADD OSPFV3）_00440569.md) | 去使能VPN路由环路检测(VPNINSCAPSIMFLG) | TRUE | 固定取值 | 支持VPN多实例，需要取消环路检查（参数<br>“VPNINSCAPSIMFLG”<br>配置为<br>“TRUE”<br>），否则会导致OSPF路由引入失败。 |
| [**ADD OSPFV3**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/OSPFv3管理/OSPFv3进程配置/创建OSPFv3进程配置（ADD OSPFV3）_00440569.md) | OSPFv3共网段虚拟系统使能标志(VIRTUALSYSFLAG) | TRUE | 全网规划 | 当OSPFv3路由配置共网段时，需要将参数<br>“VIRTUALSYSFLAG（OSPFv3共网段虚拟系统使能标志）”<br>配置为<br>“TRUE”<br>。 |
| [**ADD OSPFV3AREA**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/OSPFv3管理/OSPFv3区域配置/创建OSPFv3区域配置（ADD OSPFV3AREA）_50120842.md) | OSPFv3进程号（PROCID） | 6 | 本端规划 | - |
| [**ADD OSPFV3AREA**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/OSPFv3管理/OSPFv3区域配置/创建OSPFv3区域配置（ADD OSPFV3AREA）_50120842.md) | OSPFv3区域标识（AREAID） | 0.0.0.5 | 与对端协商 | - |
| [**ADD OSPFV3INTERFACE**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/OSPFv3管理/OSPFv3接口配置/创建OSPFv3接口配置（ADD OSPFV3INTERFACE）_49801710.md) | OSPFv3进程号(PROCID) | 6 | 本端规划 | - |
| [**ADD OSPFV3INTERFACE**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/OSPFv3管理/OSPFv3接口配置/创建OSPFv3接口配置（ADD OSPFV3INTERFACE）_49801710.md) | OSPFv3区域号（AREAID） | 0.0.0.5 | 与对端协商 | - |
| [**ADD OSPFV3INTERFACE**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/OSPFv3管理/OSPFv3接口配置/创建OSPFv3接口配置（ADD OSPFV3INTERFACE）_49801710.md) | 接口名称（IFNAME） | Eth-trunk1.1 | 全网规划 | - |
| [**ADD OSPFV3INTERFACE**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/OSPFv3管理/OSPFv3接口配置/创建OSPFv3接口配置（ADD OSPFV3INTERFACE）_49801710.md) | 指定路由器优先级（DRPRI） | 0 | - | 广播或NBMA网络中，根据此接口优先级选举DR和BDR路由器，<br>“优先级”<br>设置为<br>“0”<br>表示不参与DR和BDR的选举。为避免VNF被选为DR或BDR，建议将VNF<br>“优先级”<br>配置为0，对端配置为非0。 |
| [**ADD OSPFV3INTERFACE**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/OSPFv3管理/OSPFv3接口配置/创建OSPFv3接口配置（ADD OSPFV3INTERFACE）_49801710.md) | OSPFv3共网段虚拟系统使能标志(VIRTUALSYSFLAG) | TRUE | - | 当OSPFv3路由配置共网段时，需要将参数<br>“VIRTUALSYSFLAG（OSPFv3共网段虚拟系统使能标志）”<br>配置为<br>“TRUE”<br>。 |
| [**ADD OSPFV3IMPORTROUTE**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/OSPFv3管理/OSPFv3引入路由配置/创建OSPFv3引入路由配置（ADD OSPFV3IMPORTROUTE）_00840849.md) | OSPFv3进程号(PROCID) | 6 | 本端规划 | - |
| [**ADD OSPFV3IMPORTROUTE**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/OSPFv3管理/OSPFv3引入路由配置/创建OSPFv3引入路由配置（ADD OSPFV3IMPORTROUTE）_00840849.md) | 拓扑标识(TOPOID) | 0 | 全网规划 | - |
| [**ADD OSPFV3IMPORTROUTE**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/OSPFv3管理/OSPFv3引入路由配置/创建OSPFv3引入路由配置（ADD OSPFV3IMPORTROUTE）_00840849.md) | 协议号(PROTOCOL) | wlr | 本端规划 | - |

## [操作步骤](#ZH-CN_OPI_0280269177)

1. 打开本特性的License配置开关。
  [**SET LICENSESWITCH**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09587387.md)
2. **可选：**配置白名单检测功能。
    a. 配置VPN实例。
      [**ADD VPNINST**](../../../../../OM参考/命令/UDG MML命令/用户面服务管理/DN管理/VPN管理/VPN/增加VPN实例（ADD VPNINST）_82837045.md)
    b. 配置地址池组。
      [**ADD POOLGROUP**](../../../../../OM参考/命令/UDG MML命令/用户面服务管理/会话管理/会话地址管理/地址池组/添加地址池组（ADD POOLGROUP）_82837138.md)
    c. 配置EXTERNAL类型地址池。
      [**ADD POOL**](../../../../../OM参考/命令/UDG MML命令/用户面服务管理/会话管理/会话地址管理/地址池配置/添加地址池（ADD POOL）_82837132.md)
      > **说明**
      > 如果需要开启静态地址的白名单检测功能，需将 [**ADD POOL**](../../../../../OM参考/命令/UDG MML命令/用户面服务管理/会话管理/会话地址管理/地址池配置/添加地址池（ADD POOL）_82837132.md) 的 “CHECKIPVALID” 设置为 “ENABLE” 。
    d. 配置地址池里的IPv4地址段。
      [**ADD SECTION**](../../../../../OM参考/命令/UDG MML命令/用户面服务管理/会话管理/会话地址管理/地址段配置/添加地址池IP地址段（ADD SECTION）_82837114.md)
    e. 将地址池绑定地址池组。
      [**ADD POOLBINDGROUP**](../../../../../OM参考/命令/UDG MML命令/用户面服务管理/会话管理/会话地址管理/地址池绑定地址池组/绑定地址池到地址池组（ADD POOLBINDGROUP）_82837143.md)
    f. 配置APN名称。
      [**ADD APN**](../../../../../OM参考/命令/UDG MML命令/用户面服务管理/DN管理/APN管理/APN/添加APN配置（ADD APN）_82837014.md)
    g. 配置地址池组与APN的映射关系。
      [**ADD POOLGRPMAP**](../../../../../OM参考/命令/UDG MML命令/用户面服务管理/会话管理/会话地址管理/地址池组映射关系/添加地址池组映射关系（ADD POOLGRPMAP）_82837148.md)
3. 配置手机下行路由。
    a. 创建OSPFv3进程。
      [**ADD OSPFV3**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/OSPFv3管理/OSPFv3进程配置/创建OSPFv3进程配置（ADD OSPFV3）_00440569.md)
    b. 增加OSPFv3区域。
      [**ADD OSPFV3AREA**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/OSPFv3管理/OSPFv3区域配置/创建OSPFv3区域配置（ADD OSPFV3AREA）_50120842.md)
    c. 配置运行OSPFv3协议的接口。
      [**ADD OSPFV3INTERFACE**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/OSPFv3管理/OSPFv3接口配置/创建OSPFv3接口配置（ADD OSPFV3INTERFACE）_49801710.md)
    d. 设置OSPFv3引入路由类型。
      [**ADD OSPFV3IMPORTROUTE**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/OSPFv3管理/OSPFv3引入路由配置/创建OSPFv3引入路由配置（ADD OSPFV3IMPORTROUTE）_00840849.md)

## [任务示例](#ZH-CN_OPI_0280269177)

任务描述

UE接入核心网， UDG 采用外部地址分配方式为UE分配IP地址。

脚本

//配置外部地址分配时的白名单检测功能。

```
ADD VPNINST:VPNINSTANCE="vpn1";
```

```
ADD POOLGROUP: POOLGRPNAME="poolgroup1";
```

```
ADD POOL
:POOLNAME="testpool",POOLTYPE=EXTERNAL,IPVERSION=IPV6,CHECKIPVALID=ENABLE,HASVPN=ENABLE,VPNINSTANCE="vpn1";
ADD SECTION:POOLNAME="testpool",SECTIONNUM=1,IPVERSION=IPV6,V6PREFIXSTART="fc00:0000:0000:fcee:0000:0000:0000:0000",V6PREFIXEND="fc00:0000:0000:fcef:ffff:ffff:ffff:ffff", V6PREFIXLENGTH=63;
```

```
ADD POOLBINDGROUP:POOLGROUPNAME="poolgroup1", POOLNAME="testpool";
```

```
ADD APN
:APN="apn-test",HASVPN=ENABLE,VPNINSTANCE="vpn1";
```

```
ADD POOLGRPMAP: MAPPINGNAME="mapping1", APN="apn-test", POOLGROUPNAME="poolgroup1";
```

//配置手机下行路由。

```
ADD OSPFV3:PROCID=6,VRFNAME="vpn1",ROUTERID="10.8.25.1",BFDALLINTFFLG=TRUE,VPNINSCAPSIMFLG=TRUE,VIRTUALSYSFLAG=TRUE;
```

```
ADD OSPFV3AREA:PROCID=6,AREAID="0.0.0.5";
```

```
ADD OSPFV3INTERFACE:PROCID=6,AREAID="0.0.0.5",IFNAME="Eth-trunk1.1",DRPRI=0,VIRTUALSYSFLAG=TRUE, CFGROUTERIDFLAG=FALSE;
```

```
ADD OSPFV3IMPORTROUTE:PROCID=6,TOPOID=0,PROTOCOL=wlr;
```
