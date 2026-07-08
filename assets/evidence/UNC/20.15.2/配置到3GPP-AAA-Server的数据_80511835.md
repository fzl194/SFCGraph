# 配置到3GPP AAA Server的数据

- [操作场景](#ZH-CN_OPI_0280511835__1.3.1)
- [必备事项](#ZH-CN_OPI_0280511835__1.3.2)
- [操作步骤](#ZH-CN_OPI_0280511835__1.3.3)
- [任务示例](#ZH-CN_OPI_0280511835__1.3.4)

## [操作场景](#ZH-CN_OPI_0280511835)

当 UNC 支持Non-3GPP GW接入或部署CDMA2000与LTE 、WLAN与LTE 互操作网络时，需要配置 UNC 到3GPP AAA Server的互通数据，用于更新PGW-C的IP地址和 APN 信息，并获取用户的授权信息。

## [必备事项](#ZH-CN_OPI_0280511835)

前提条件

- 请仔细阅读[WSFD-010102 Untrusted Non-3GPP网络用户接入](../../WSFD-010102 Untrusted Non-3GPP网络用户接入_80511024.md)和[激活Untrusted Non-3GPP网络用户接入功能](../激活Untrusted Non-3GPP网络用户接入功能_80511607.md)。
- UNC 与网络实体之间的网络环境已经构建完成。
- 操作员了解UNC各类接口的类型及命名规范，具体内容请参见[业务组网与逻辑接口介绍](../../../../../初始配置/UNC初始配置与调测/了解组网架构与原理/业务组网与逻辑接口介绍_96206590.md)。

数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| VPN实例 | VPN实例名（VPNINSTANCE） | vpn_3gpp_aaa | 本端规划 | [**ADD VPNINST**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/增加VPN实例（ADD VPNINST）_09653755.md) |
| VPN实例 | VPN实例名称(VRFNAME) | vpn_3gpp_aaa | 本端规划 | **[**ADD L3VPNINST**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例/增加L3VPN实例（ADD L3VPNINST）_49802446.md)**<br>**[**ADD VPNINSTAF**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例地址族/增加L3VPN实例地址族（ADD VPNINSTAF）_49802178.md)** |
| VPN实例 | 地址族类型(AFTYPE) | ipv4uni | 本端规划 | **[**ADD L3VPNINST**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例/增加L3VPN实例（ADD L3VPNINST）_49802446.md)**<br>**[**ADD VPNINSTAF**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例地址族/增加L3VPN实例地址族（ADD VPNINSTAF）_49802178.md)** |
| Diameter应用集中点模式 | S6b集中点模式（S6BCONCENMODE） | LOCALPORT | 本端规划 | [**SET CONCENPOINT**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/基础参数/集中点模式/设置集中点部署模式（SET CONCENPOINT）_09896704.md) |
| S6b逻辑接口 | 逻辑接口名称(NAME) | S6bif1/0/0 | 固定取值 | [**ADD LOGICINF**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md) |
| S6b逻辑接口 | 逻辑接口的IP版本（IPVERSION） | IPV4 | 本端规划 | [**ADD LOGICINF**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md) |
| S6b逻辑接口 | VPN实例名称(VPNINSTANCE) | vpn_3gpp_aaa | 从已配置数据中获取 | [**ADD LOGICINF**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md) |
| S6b逻辑接口 | 逻辑接口的IPv4地址1(IPV4ADDRESS1) | 192.168.7.7 | 全网规划 | [**ADD LOGICINF**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md) |
| S6b逻辑接口 | 逻辑接口的IPv4掩码1 (IPV4MASK1) | 255.255.255.255 | 固定取值 | [**ADD LOGICINF**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md) |
| 缺省路由 | VPN实例名称 (VRFNAME) | vpn_3gpp_aaa | 本端规划 | [**ADD SRROUTE**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/静态路由管理/IPv4静态路由/增加IPv4静态路由（ADD SRROUTE）_49961498.md) |
| 缺省路由 | 路由前缀（PREFIX） | 0.0.0.0 | 与对端网元协商 | [**ADD SRROUTE**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/静态路由管理/IPv4静态路由/增加IPv4静态路由（ADD SRROUTE）_49961498.md) |
| 缺省路由 | 路由掩码长度（MASKLENGTH） | 32 | 本端规划 | [**ADD SRROUTE**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/静态路由管理/IPv4静态路由/增加IPv4静态路由（ADD SRROUTE）_49961498.md) |
| 缺省路由 | 路由下一跳（NEXTHOP） | 10.3.37.81 | 与对端网元协商 | [**ADD SRROUTE**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/静态路由管理/IPv4静态路由/增加IPv4静态路由（ADD SRROUTE）_49961498.md) |
| SCTP端点信息 | 端点名称（ENDPOINTNAME） | dc1_AAA01-S6B-SCTPEP01 | 本端规划 | **[ADD SCTPENDPOINT](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/SCTP管理/SCTP端点/增加SCTP端点（ADD SCTPENDPOINT）_09897321.md)** |
| SCTP端点信息 | IP版（IPVERSION） | IPV4 | 与对端协商 | **[ADD SCTPENDPOINT](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/SCTP管理/SCTP端点/增加SCTP端点（ADD SCTPENDPOINT）_09897321.md)** |
| SCTP端点信息 | IPv4地址（IPV4ADDRESS1） | - 10.45.36.227<br>- 10.45.36.235 | 与对端协商 | **[ADD SCTPENDPOINT](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/SCTP管理/SCTP端点/增加SCTP端点（ADD SCTPENDPOINT）_09897321.md)** |
| SCTP端点信息 | 端口号（PORT） | 3868 | 与对端协商 | **[ADD SCTPENDPOINT](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/SCTP管理/SCTP端点/增加SCTP端点（ADD SCTPENDPOINT）_09897321.md)** |
| UNC<br>和3GPP AAA Server设备信息 | 本端主机名（HOSTNAME） | unc_1 | 与对端协商 | 与3GPP AAA Server上配置的参数保持一致。<br>[**ADD DIAMLOCINFO**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter本端信息/增加Diameter本端信息（ADD DIAMLOCINFO）_09897271.md) |
| UNC<br>和3GPP AAA Server设备信息 | 本端域名（REALMNAME） | apn2 | 与对端协商 | 与3GPP AAA Server上配置的参数保持一致。<br>[**ADD DIAMLOCINFO**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter本端信息/增加Diameter本端信息（ADD DIAMLOCINFO）_09897271.md) |
| UNC<br>和3GPP AAA Server设备信息 | 产品名称（PRODUCTNAME） | unc | 本端规划 | 与3GPP AAA Server上配置的参数保持一致。<br>[**ADD DIAMLOCINFO**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter本端信息/增加Diameter本端信息（ADD DIAMLOCINFO）_09897271.md) |
| UNC<br>和3GPP AAA Server设备信息 | 主机名（HOSTNAME） | 3gppaaa | 本端规划 | VPN实例已通过<br>[**ADD VPNINST**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/增加VPN实例（ADD VPNINST）_09653755.md)<br>命令配置，可以使用<br>[**LST VPNINST**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/查询VPN实例（LST VPNINST）_09651519.md)<br>命令进行查询。<br>[**ADD DIAMETERAAA**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/Diameter AAA管理/服务器配置/Diameter AAA信息/增加Diameter AAA服务器（ADD DIAMETERAAA）_64343821.md) |
| UNC<br>和3GPP AAA Server设备信息 | 域名（REALMNAME） | 3gppaaa.huawei.com | 本端规划 | VPN实例已通过<br>[**ADD VPNINST**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/增加VPN实例（ADD VPNINST）_09653755.md)<br>命令配置，可以使用<br>[**LST VPNINST**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/查询VPN实例（LST VPNINST）_09651519.md)<br>命令进行查询。<br>[**ADD DIAMETERAAA**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/Diameter AAA管理/服务器配置/Diameter AAA信息/增加Diameter AAA服务器（ADD DIAMETERAAA）_64343821.md) |
| UNC<br>和3GPP AAA Server设备信息 | VPN实例（VPNINSTANCE） | vpn_3gpp_aaa | 从已配置数据中获取 | VPN实例已通过<br>[**ADD VPNINST**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/增加VPN实例（ADD VPNINST）_09653755.md)<br>命令配置，可以使用<br>[**LST VPNINST**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/查询VPN实例（LST VPNINST）_09651519.md)<br>命令进行查询。<br>[**ADD DIAMETERAAA**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/Diameter AAA管理/服务器配置/Diameter AAA信息/增加Diameter AAA服务器（ADD DIAMETERAAA）_64343821.md) |
| UNC<br>和3GPP AAA Server设备信息 | 主机名（HOSTNAME） | 3gppaaa | 本端规划 | UNC<br>与3gppaaa之间构建一条IP链路，3gppaaa的IP地址为10.10.10.10。<br>[**ADD DIAMPEERADDR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md) |
| UNC<br>和3GPP AAA Server设备信息 | 地址类型（ADDRTYPE） | SCTP | 与对端协商 | - |
| UNC<br>和3GPP AAA Server设备信息 | SCTP端点名称（SCTPENDPOINT） | dc1_AAA01-S6B-SCTPEP01 | 本端规划 | 已通过<br>**[ADD SCTPENDPOINT](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/SCTP管理/SCTP端点/增加SCTP端点（ADD SCTPENDPOINT）_09897321.md)**<br>完成配置。 |
| UNC<br>和3GPP AAA Server设备信息 | Diameter链路组名（CONNGROUPNAME） | dconn_s6b | 本端规划 | [**ADD DIAMCONNGRP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md) |
| UNC<br>和3GPP AAA Server设备信息 | 本端主机名（LOCALHOSTNAME） | unc_1 | 全网规划 | [**ADD DIAMCONNGRP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md) |
| UNC<br>和3GPP AAA Server设备信息 | 对端主机名（PEERHOSTNAME） | 3gppaaa | 全网规划 | [**ADD DIAMCONNGRP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md) |
| UNC<br>和3GPP AAA Server设备信息 | Diameter应用（APPLICATION） | S6b | 全网规划 | [**ADD DIAMCONNGRP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md) |
| UNC<br>和3GPP AAA Server设备信息 | 链路选择模式（SELECTMODE） | SESSION_ID<br>ROUND-ROBIN | 全网规划 | [**ADD DIAMCONNGRP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md) |
| UNC<br>和3GPP AAA Server设备信息 | Diameter链路组名（CONNGROUPNAME） | dconn_s6b | 本端规划 | [**ADD DIAMCONNECTION**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md) |
| UNC<br>和3GPP AAA Server设备信息 | 本端接口名（LOCINTERFACE） | S6bif1/0/0 | 本端规划 | - |
| UNC<br>和3GPP AAA Server设备信息 | 本端端口（LOCALPORT） | 19765 | 本端规划 | - |
| UNC<br>和3GPP AAA Server设备信息 | 对端地址类型（PEERADDRTYPE） | SCTP | 与对端协商 | - |
| UNC<br>和3GPP AAA Server设备信息 | 对端SCTP端点名称（PEERSCTPENDPT） | dc1_AAA01-S6B-SCTPEP01 | 本端规划 | 已通过<br>**[ADD SCTPENDPOINT](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/SCTP管理/SCTP端点/增加SCTP端点（ADD SCTPENDPOINT）_09897321.md)**<br>完成配置。 |
| UNC<br>和3GPP AAA Server设备信息 | Diameter AAA组名（GROUPNAME） | 3gpprg | 本端规划 | 配置PGW-C identity的属性。<br>[**ADD DIAMAAAGRP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/Diameter AAA管理/服务器配置/Diameter AAA组/增加Diameter AAA服务器组（ADD DIAMAAAGRP）_64343820.md)<br>**[ADD PGWHOSTNAME](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/Diameter AAA管理/P-GW Host Name配置/P-GW逻辑接口主机名/增加逻辑接口的PGW主机名（ADD PGWHOSTNAME）_64343865.md)**<br>**[ADD DIAMAAABNDGRP](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/Diameter AAA管理/服务器配置/Diameter AAA服务器和Diameter AAA服务器组的绑定关系/增加Diameter AAA服务器到Diameter AAA服务器组（ADD DIAMAAABNDGRP）_64343819.md)**<br>[**ADD APNDIAMAAAGRP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/Diameter AAA管理/服务器配置/APN的Diameter AAA组/增加APN的Diameter AAA服务器组（ADD APNDIAMAAAGRP）_64343817.md) |
| UNC<br>和3GPP AAA Server设备信息 | PDN GW Identity携带方式（PGWIDENTITY） | HOST_NAME | 本端规划 | 配置PGW-C identity的属性。<br>[**ADD DIAMAAAGRP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/Diameter AAA管理/服务器配置/Diameter AAA组/增加Diameter AAA服务器组（ADD DIAMAAAGRP）_64343820.md)<br>**[ADD PGWHOSTNAME](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/Diameter AAA管理/P-GW Host Name配置/P-GW逻辑接口主机名/增加逻辑接口的PGW主机名（ADD PGWHOSTNAME）_64343865.md)**<br>**[ADD DIAMAAABNDGRP](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/Diameter AAA管理/服务器配置/Diameter AAA服务器和Diameter AAA服务器组的绑定关系/增加Diameter AAA服务器到Diameter AAA服务器组（ADD DIAMAAABNDGRP）_64343819.md)**<br>[**ADD APNDIAMAAAGRP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/Diameter AAA管理/服务器配置/APN的Diameter AAA组/增加APN的Diameter AAA服务器组（ADD APNDIAMAAAGRP）_64343817.md) |
| UNC<br>和3GPP AAA Server设备信息 | PGW-C主机名<br>（PGWHOSTNAME） | topon.Eth-0.canonical-node-name.gw32.california.west.example.com | 本端规划 | 配置PGW-C identity的属性。<br>[**ADD DIAMAAAGRP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/Diameter AAA管理/服务器配置/Diameter AAA组/增加Diameter AAA服务器组（ADD DIAMAAAGRP）_64343820.md)<br>**[ADD PGWHOSTNAME](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/Diameter AAA管理/P-GW Host Name配置/P-GW逻辑接口主机名/增加逻辑接口的PGW主机名（ADD PGWHOSTNAME）_64343865.md)**<br>**[ADD DIAMAAABNDGRP](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/Diameter AAA管理/服务器配置/Diameter AAA服务器和Diameter AAA服务器组的绑定关系/增加Diameter AAA服务器到Diameter AAA服务器组（ADD DIAMAAABNDGRP）_64343819.md)**<br>[**ADD APNDIAMAAAGRP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/Diameter AAA管理/服务器配置/APN的Diameter AAA组/增加APN的Diameter AAA服务器组（ADD APNDIAMAAAGRP）_64343817.md) |
| UNC<br>和3GPP AAA Server设备信息 | 接口类型<br>（INTFTYPE） | S5_P_OR_GN_OR_S2B | 本端规划 | 配置PGW-C identity的属性。<br>[**ADD DIAMAAAGRP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/Diameter AAA管理/服务器配置/Diameter AAA组/增加Diameter AAA服务器组（ADD DIAMAAAGRP）_64343820.md)<br>**[ADD PGWHOSTNAME](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/Diameter AAA管理/P-GW Host Name配置/P-GW逻辑接口主机名/增加逻辑接口的PGW主机名（ADD PGWHOSTNAME）_64343865.md)**<br>**[ADD DIAMAAABNDGRP](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/Diameter AAA管理/服务器配置/Diameter AAA服务器和Diameter AAA服务器组的绑定关系/增加Diameter AAA服务器到Diameter AAA服务器组（ADD DIAMAAABNDGRP）_64343819.md)**<br>[**ADD APNDIAMAAAGRP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/Diameter AAA管理/服务器配置/APN的Diameter AAA组/增加APN的Diameter AAA服务器组（ADD APNDIAMAAAGRP）_64343817.md) |
| UNC<br>和3GPP AAA Server设备信息 | 服务器类型（SERVERTYPE） | PARA_3GPP | 本端规划 | 配置PGW-C identity的属性。<br>[**ADD DIAMAAAGRP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/Diameter AAA管理/服务器配置/Diameter AAA组/增加Diameter AAA服务器组（ADD DIAMAAAGRP）_64343820.md)<br>**[ADD PGWHOSTNAME](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/Diameter AAA管理/P-GW Host Name配置/P-GW逻辑接口主机名/增加逻辑接口的PGW主机名（ADD PGWHOSTNAME）_64343865.md)**<br>**[ADD DIAMAAABNDGRP](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/Diameter AAA管理/服务器配置/Diameter AAA服务器和Diameter AAA服务器组的绑定关系/增加Diameter AAA服务器到Diameter AAA服务器组（ADD DIAMAAABNDGRP）_64343819.md)**<br>[**ADD APNDIAMAAAGRP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/Diameter AAA管理/服务器配置/APN的Diameter AAA组/增加APN的Diameter AAA服务器组（ADD APNDIAMAAAGRP）_64343817.md) |
| UNC<br>和3GPP AAA Server设备信息 | 主备用标记（PRIORSEC） | PRIMARY | 本端规划 | 配置PGW-C identity的属性。<br>[**ADD DIAMAAAGRP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/Diameter AAA管理/服务器配置/Diameter AAA组/增加Diameter AAA服务器组（ADD DIAMAAAGRP）_64343820.md)<br>**[ADD PGWHOSTNAME](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/Diameter AAA管理/P-GW Host Name配置/P-GW逻辑接口主机名/增加逻辑接口的PGW主机名（ADD PGWHOSTNAME）_64343865.md)**<br>**[ADD DIAMAAABNDGRP](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/Diameter AAA管理/服务器配置/Diameter AAA服务器和Diameter AAA服务器组的绑定关系/增加Diameter AAA服务器到Diameter AAA服务器组（ADD DIAMAAABNDGRP）_64343819.md)**<br>[**ADD APNDIAMAAAGRP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/Diameter AAA管理/服务器配置/APN的Diameter AAA组/增加APN的Diameter AAA服务器组（ADD APNDIAMAAAGRP）_64343817.md) |
| UNC<br>和3GPP AAA Server设备信息 | APN名称（APN） | apn1 | 本端规划 | 配置PGW-C identity的属性。<br>[**ADD DIAMAAAGRP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/Diameter AAA管理/服务器配置/Diameter AAA组/增加Diameter AAA服务器组（ADD DIAMAAAGRP）_64343820.md)<br>**[ADD PGWHOSTNAME](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/Diameter AAA管理/P-GW Host Name配置/P-GW逻辑接口主机名/增加逻辑接口的PGW主机名（ADD PGWHOSTNAME）_64343865.md)**<br>**[ADD DIAMAAABNDGRP](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/Diameter AAA管理/服务器配置/Diameter AAA服务器和Diameter AAA服务器组的绑定关系/增加Diameter AAA服务器到Diameter AAA服务器组（ADD DIAMAAABNDGRP）_64343819.md)**<br>[**ADD APNDIAMAAAGRP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/Diameter AAA管理/服务器配置/APN的Diameter AAA组/增加APN的Diameter AAA服务器组（ADD APNDIAMAAAGRP）_64343817.md) |

## [操作步骤](#ZH-CN_OPI_0280511835)

1. 进入 “MML命令行-UNC” 窗口。
2. 配置VPN实例。
  [**ADD VPNINST**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/增加VPN实例（ADD VPNINST）_09653755.md)
3. 配置L3VPN实例。
  **[**ADD L3VPNINST**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例/增加L3VPN实例（ADD L3VPNINST）_49802446.md)**
  **[**ADD VPNINSTAF**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例地址族/增加L3VPN实例地址族（ADD VPNINSTAF）_49802178.md)**
4. **可选：**配置S6b接口Diameter应用集中点模式。缺省情况下，本端的端口号不可配，使用系统自动分配的端口号。
  [**SET CONCENPOINT**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/基础参数/集中点模式/设置集中点部署模式（SET CONCENPOINT）_09896704.md)
5. 创建S6bif接口。
  [**ADD LOGICINF**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)
6. 配置到3GPP AAA Server的VPN缺省路由。
  [**ADD SRROUTE**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/静态路由管理/IPv4静态路由/增加IPv4静态路由（ADD SRROUTE）_49961498.md)
7. 如果通过SCTP方式与3GPP AAA Server建立链接，需要配置SCTP端点信息。
  **[ADD SCTPENDPOINT](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/SCTP管理/SCTP端点/增加SCTP端点（ADD SCTPENDPOINT）_09897321.md)**
8. 配置本端端点的主机信息。
  [**ADD DIAMLOCINFO**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter本端信息/增加Diameter本端信息（ADD DIAMLOCINFO）_09897271.md)
9. 配置3GPP AAA Server。
  [**ADD DIAMETERAAA**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/Diameter AAA管理/服务器配置/Diameter AAA信息/增加Diameter AAA服务器（ADD DIAMETERAAA）_64343821.md)
  [**ADD DIAMPEERADDR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)
    - 通过TCP方式与3GPP AAA Server建立起正常的IP连接时，[**ADD DIAMPEERADDR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)中的“ADDRTYPE”根据实际规划配置为“IPv4”或“IPv6”。
    - 通过SCTP方式与3GPP AAA Server建立起正常的IP连接时，[**ADD DIAMPEERADDR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)中的“ADDRTYPE”配置为“SCTP”，“SCTPENDPOINT”已通过**[ADD SCTPENDPOINT](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/SCTP管理/SCTP端点/增加SCTP端点（ADD SCTPENDPOINT）_09897321.md)**完成配置。
10. 建立本端与对端的链路组，并配置链路选择模式。
  [**ADD DIAMCONNGRP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md)
11. 配置到3GPP AAA Server的链路。
  [**ADD DIAMCONNECTION**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md)
    - 通过TCP方式与3GPP AAA Server建立起正常的IP连接时，[**ADD DIAMCONNECTION**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md)中的“PEERADDRTYPE”根据实际规划配置为“PEERIPV4ADDR”或“PEERIPV6ADDR”。
    - 通过SCTP方式与3GPP AAA Server建立起正常的IP连接时，[**ADD DIAMCONNECTION**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md)中的“PEERADDRTYPE”配置为“SCTP”，“PEERSCTPENDPT”已通过**[ADD SCTPENDPOINT](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/SCTP管理/SCTP端点/增加SCTP端点（ADD SCTPENDPOINT）_09897321.md)**完成配置。
  > **说明**
  > 配置链路时如果不选择地址类型，则表示本端接口与对端主机的全部地址建立链接。
  >
  > 当 “S6b集中点模式” 通过 [**SET CONCENPOINT**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/基础参数/集中点模式/设置集中点部署模式（SET CONCENPOINT）_09896704.md) 命令选择为 “LOCALPORT” 时，可使用 [**ADD DIAMCONNECTION**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md) 命令设置本端的端口号。
12. 配置PGW-C identity的属性。
  [**ADD DIAMAAAGRP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/Diameter AAA管理/服务器配置/Diameter AAA组/增加Diameter AAA服务器组（ADD DIAMAAAGRP）_64343820.md)
13. 增加逻辑接口的PGW-C主机名。
  **[ADD PGWHOSTNAME](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/Diameter AAA管理/P-GW Host Name配置/P-GW逻辑接口主机名/增加逻辑接口的PGW主机名（ADD PGWHOSTNAME）_64343865.md)**
14. 绑定3GPP AAA Server到服务器组。
  **[ADD DIAMAAABNDGRP](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/Diameter AAA管理/服务器配置/Diameter AAA服务器和Diameter AAA服务器组的绑定关系/增加Diameter AAA服务器到Diameter AAA服务器组（ADD DIAMAAABNDGRP）_64343819.md)**
15. 绑定diameter-server group到APN。
  [**ADD APNDIAMAAAGRP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/Diameter AAA管理/服务器配置/APN的Diameter AAA组/增加APN的Diameter AAA服务器组（ADD APNDIAMAAAGRP）_64343817.md)

## [任务示例](#ZH-CN_OPI_0280511835)

任务描述

UNC 与3GPP AAA Server通过VPN+缺省路由组网方式对接时的配置范例。

本实例中，操作员在 UNC 上进行数据配置实现以下要求：

UNC 使用VPN缺省路由，通过SCTP方式与3GPP AAA Server建立起正常的IP连接。

脚本

1. 进入 “MML命令行-UNC” 窗口。
2. 配置VPN实例。
  ```
  ADD VPNINST:VPNINSTANCE="vpn_3gpp_aaa";
  ```
3. 创建VPN实例。
  ```
  ADD L3VPNINST: VRFNAME="vpn_3gpp_aaa";
  ```
  ```
  ADD VPNINSTAF: VRFNAME="vpn_3gpp_aaa",AFTYPE=ipv4uni;
  ```
4. 配置S6b接口Diameter应用集中点模式。
  ```
  SET CONCENPOINT:S6BCONCENMODE=LOCALPORT;
  ```
5. 创建S6bif接口。
  ```
  ADD LOGICINF:NAME="s6bif1/0/0",IPVERSION=IPV4,IPV4ADDRESS1="192.168.7.7",IPV4MASK1="255.255.255.255",VPNINSTANCE="vpn_3gpp_aaa";
  ```
6. 配置到3GPP AAA Server的VPN缺省路由。
  ```
  ADD SRROUTE: VRFNAME="vpn_3gpp_aaa",AFTYPE=ipv4unicast,PREFIX="0.0.0.0",MASKLENGTH=32,DESTVRFNAME="vpn_3gpp_aaa",IFNAME="Invalid0",NEXTHOP="10.3.37.81";
  ```
7. 配置SCTP端点信息。
  ```
  ADD SCTPENDPOINT: ENDPOINTNAME="dc1_AAA01-S6B-SCTPEP01",IPVERSION=IPV4,IPV4ADDRESS1="10.45.36.227",PORT=3868;
  ```
8. 配置本端端点的主机信息，端口号固定，由系统自动生成。
  ```
  ADD DIAMLOCINFO: HOSTNAME="unc_1",REALMNAME="apn2",PRODUCTNAME="unc";
  ```
9. 配置3GPP AAA Server的设备标识及其主机信息。
  ```
  ADD DIAMETERAAA: HOSTNAME="3gppaaa",REALMNAME="3gppaaa.huawei.com",VPNINSTANCE="vpn_3gpp_aaa";
  ```
  ```
  ADD DIAMPEERADDR: HOSTNAME="3gppaaa",ADDRTYPE=SCTP,SCTPENDPOINT="dc1_AAA01-S6B-SCTPEP01";
  ```
10. 建立本端与对端的链路组，并配置链路选择模式。
  ```
  ADD DIAMCONNGRP: CONNGROUPNAME="dconn_s6b",LOCALHOSTNAME="unc_1",APPLICATION=S6b,PEERHOSTNAME="3gppaaa";
  ```
11. 配置到3GPP AAA Server的链路。
  ```
  ADD DIAMCONNECTION:DIAMCONNGRP="dconn_s6b",LOCINTERFACE="S6bif1/0/0",LOCALPORT=19765,PEERADDRTYPE=SCTP,PEERSCTPENDPT="dc1_AAA01-S6B-SCTPEP01";
  ```
12. 配置PGW-C identity的属性。
  ```
  ADD DIAMAAAGRP:GROUPNAME="3gpprg",PGWIDENTITY=HOST_NAME;
  ```
13. 增加逻辑接口的PGW-C主机名。
  ```
  ADD PGWHOSTNAME:PGWHOSTNAME="topon.Eth-0.canonical-node-name.gw32.california.west.example.com",INTFTYPE=S5_P_OR_GN_OR_S2B;
  ```
14. 绑定3GPP AAA Server到服务器组。
  ```
  ADD DIAMAAABNDGRP: GROUPNAME="3gpprg", SERVERTYPE=PARA_3GPP, HOSTNAME="3gppaaa", PRIORSEC=PRIMARY;
  ```
15. 绑定diameter-server group到APN。
  ```
  ADD APNDIAMAAAGRP:APN="apn1",GROUPNAME="3gpprg";
  ```
