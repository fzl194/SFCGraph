# GWFD-010155 Untrusted Non-3GPP网络用户接入参考信息

- [命令](#ZH-CN_TOPIC_0270759401__1.3.1.1)
- [告警](#ZH-CN_TOPIC_0270759401__1.3.2.1)
- [软参](#ZH-CN_TOPIC_0270759401__1.3.3.1)
- [测量指标](#ZH-CN_TOPIC_0270759401__1.3.4.1)

#### [命令](#ZH-CN_TOPIC_0270759401)

本特性相关的MML命令如下：

- [**ADD L3VPNINST**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例/增加L3VPN实例（ADD L3VPNINST）_49802446.md)
- [**ADD VPNINSTAF**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例地址族/增加L3VPN实例地址族（ADD VPNINSTAF）_49802178.md)
- [**ADD VPNINST**](../../../../../OM参考/命令/UDG MML命令/用户面服务管理/DN管理/VPN管理/VPN/增加VPN实例（ADD VPNINST）_82837045.md)
- [**ADD LOGICINF**](../../../../../OM参考/命令/UDG MML命令/用户面服务管理/DN管理/逻辑接口管理/逻辑接口配置/接口/增加逻辑接口（ADD LOGICINF）_82835378.md)
- [**SET BFD**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/BFD管理/BFD全局配置/设置BFD全局属性（SET BFD）_00840937.md)
- [**ADD OSPF**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/OSPF管理/OSPF进程配置/创建OSPF进程配置（ADD OSPF）_00866089.md)
- [**ADD OSPFAREA**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/OSPF管理/OSPF区域配置/创建OSPF区域配置（ADD OSPFAREA）_50120650.md)
- [**ADD OSPFNETWORK**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/OSPF管理/指定OSPF运行的接口及所属区域/指定OSPF运行的接口及所属区域（ADD OSPFNETWORK）_00601465.md)
- [**ADD OSPFIMPORTROUTE**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/OSPF管理/引入外部路由配置/创建OSPF引入路由配置（ADD OSPFIMPORTROUTE）_00601057.md)
- [**ADD SRROUTE**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/静态路由管理/IPv4静态路由/增加IPv4静态路由（ADD SRROUTE）_49961498.md)
- [**ADD BFDSESSION**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/BFD管理/BFD会话/增加BFD会话（ADD BFDSESSION）_49801434.md)
- [**ADD INTERFACE**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/接口管理/接口配置/增加接口（ADD INTERFACE）_49960870.md)
- [**ADD IPBINDVPN**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/接口管理/IP绑定VPN/增加接口绑定VPN（ADD IPBINDVPN）_50120734.md)
- [**ADD ETHSUBIF**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/VLAN管理/VLAN子接口/增加子接口配置（ADD ETHSUBIF）_49801486.md)
- [**SET IFIPV6ENABLE**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/接口管理/IPv6使能/修改接口IPv6使能（SET IFIPV6ENABLE）_00601329.md)
- [**ADD IFIPV6ADDRESS**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/接口管理/IPv6地址/增加接口IPv6地址（ADD IFIPV6ADDRESS）_49961222.md)
- [**ADD OSPFV3**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/OSPFv3管理/OSPFv3进程配置/创建OSPFv3进程配置（ADD OSPFV3）_00440569.md)
- [**ADD OSPFV3IMPORTROUTE**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/OSPFv3管理/OSPFv3引入路由配置/创建OSPFv3引入路由配置（ADD OSPFV3IMPORTROUTE）_00840849.md)
- [**ADD OSPFV3AREA**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/OSPFv3管理/OSPFv3区域配置/创建OSPFv3区域配置（ADD OSPFV3AREA）_50120842.md)
- [**ADD OSPFV3INTERFACE**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/OSPFv3管理/OSPFv3接口配置/创建OSPFv3接口配置（ADD OSPFV3INTERFACE）_49801710.md)

#### [告警](#ZH-CN_TOPIC_0270759401)

本特性相关的告警如下：

[ALM-81018 GTPU路径断](../../../../../网络运维/故障处理/用户面告警/ALM-81018 GTPU路径断_93246969.md)

#### [软参](#ZH-CN_TOPIC_0270759401)

本特性无相关软参。

#### [测量指标](#ZH-CN_TOPIC_0270759401)

本特性相关的测量指标如下：

- 用户平面S2b上行用户面报文包数
- 用户平面S2b上行用户面报文千字节数
- 用户平面S2b上行收用户面报文峰值包速率
- 用户平面S2b上行用户面报文峰值千字节速率
- 用户平面S2b下行用户面报文包数
- 用户平面2b下行用户面报文千字节数
- 用户平面S2b下行用户面报文峰值包速率
- 用户平面S2b下行用户面报文峰值千字节速率
- 用户平面发送RAT类型为WLAN的漫游用户上行用户面报文千字节数
- 用户平面发送RAT类型为WLAN的漫游用户下行用户面报文千字节数
- 用户平面发送RAT类型为WLAN的拜访用户上行用户面报文千字节数
- 用户平面发送RAT类型为WLAN的拜访用户下行用户面报文千字节数
- 用户平面发送RAT类型为WLAN的本地用户上行用户面报文千字节数
- 用户平面发送RAT类型为WLAN的本地用户下行用户面报文千字节数
