# 配置Gx over SCTP功能

- [操作场景](#ZH-CN_OPI_0230442391__1.3.1)
- [必备事项](#ZH-CN_OPI_0230442391__1.3.2)
- [操作步骤](#ZH-CN_OPI_0230442391__1.3.3)
- [验证方法](#ZH-CN_OPI_0230442391__1.3.4)
- [任务示例](#ZH-CN_OPI_0230442391__1.3.5)

## [操作场景](#ZH-CN_OPI_0230442391)

运营商规划与PCRF对接时使用SCTP功能，以提高Gx接口信令传输的可靠性，则需要在GGSN/PGW-C上部署SCTP功能，保证与PCRF信令链路的连通性。

> **说明**
> 适用于 GGSN、 PGW-C。

## [必备事项](#ZH-CN_OPI_0230442391)

前提条件

- 请仔细阅读 [WSFD-104508 SCTP](../../WSFD-104508 SCTP_27680892.md) 。
- 如果运营商规划采用VPN组网方式，则操作员在执行本操作前应已创建了相应的VPN实例。
- GGSN/PGW-C与PCRF之间的物理链路已连通。
- 完成加载License（如果有需求，请联系华为技术支持工程师处理）。

数据

与PCRF对接使用SCTP时，GGSN/PGW-C支持使用IPv4或IPv6地址进行对接，本处以IPv4为例进行说明。

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| [**ADD VPNINST**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/增加VPN实例（ADD VPNINST）_09653755.md) | VPN实例名称（VPNINSTANCE） | vpn_gxif | 本端规划 | - |
| **[**ADD LOGICINF**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)** | 逻辑接口名称（NAME） | gxif1/0/0 | 本端规划 | 其中10.8.20.1为主IP地址，10.8.20.2为从IP地址。<br>逻辑接口的IP掩码只能为255.255.255.255，或掩码长度32。 |
| **[**ADD LOGICINF**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)** | 逻辑接口的IPv4地址1(IPV4ADDRESS1) | 10.8.20.1 | 全网规划 | 其中10.8.20.1为主IP地址，10.8.20.2为从IP地址。<br>逻辑接口的IP掩码只能为255.255.255.255，或掩码长度32。 |
| **[**ADD LOGICINF**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)** | 逻辑接口的IP版本（IPVERSION） | IPV4 | 本端规划 | 其中10.8.20.1为主IP地址，10.8.20.2为从IP地址。<br>逻辑接口的IP掩码只能为255.255.255.255，或掩码长度32。 |
| **[**ADD LOGICINF**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)** | 逻辑接口的IPv4掩码1(IPV4MASK1) | 255.255.255.255 | 固定取值 | 其中10.8.20.1为主IP地址，10.8.20.2为从IP地址。<br>逻辑接口的IP掩码只能为255.255.255.255，或掩码长度32。 |
| **[**ADD LOGICINF**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)** | 逻辑接口的IPv4地址2（IPV4ADDRESS2） | 10.8.20.2 | 全网规划 | 其中10.8.20.1为主IP地址，10.8.20.2为从IP地址。<br>逻辑接口的IP掩码只能为255.255.255.255，或掩码长度32。 |
| **[**ADD LOGICINF**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)** | 逻辑接口的IPv4掩码2(IPV4MASK2) | 255.255.255.255 | 固定取值 | 其中10.8.20.1为主IP地址，10.8.20.2为从IP地址。<br>逻辑接口的IP掩码只能为255.255.255.255，或掩码长度32。 |
| **[**ADD LOGICINF**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)** | VPN实例名称（VPNINSTANCE） | vpn_gxif | 已配置数据中获取 | 接口绑定的VPN实例已通过<br>[**ADD VPNINST**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/增加VPN实例（ADD VPNINST）_09653755.md)<br>命令配置，可以使用<br>[**LST VPNINST**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/查询VPN实例（LST VPNINST）_09651519.md)<br>命令进行查询。 |
| [**ADD DIAMLOCINFO**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter本端信息/增加Diameter本端信息（ADD DIAMLOCINFO）_09897271.md) | 本端主机名（HOSTNAME） | unc_1 | 与对端协商 | - |
| [**ADD DIAMLOCINFO**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter本端信息/增加Diameter本端信息（ADD DIAMLOCINFO）_09897271.md) | 本端域名（REALMNAME） | example.com | 与对端协商 | - |
| [**ADD DIAMLOCINFO**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter本端信息/增加Diameter本端信息（ADD DIAMLOCINFO）_09897271.md) | 产品名称（PRODUCTNAME） | unc | 本端规划 | - |
| **[ADD SCTPTEMPLATE](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/SCTP管理/SCTP模板/增加SCTP模板（ADD SCTPTEMPLATE）_09897332.md)** | SCTP模板名称（SCTPTEMPLNAME） | testtemplate | 本端规划 | - |
| **[ADD SCTPTEMPLATE](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/SCTP管理/SCTP模板/增加SCTP模板（ADD SCTPTEMPLATE）_09897332.md)** | SCTP发送心跳消息的间隔周期（毫秒）（HEARTBEATINTVAL） | 30000 | 本端规划 | - |
| **[ADD SCTPTEMPLATE](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/SCTP管理/SCTP模板/增加SCTP模板（ADD SCTPTEMPLATE）_09897332.md)** | SCTP耦联上消息重传的最大次数（MAXASSOCRETRY） | 5 | 本端规划 | - |
| **[ADD SCTPTEMPLATE](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/SCTP管理/SCTP模板/增加SCTP模板（ADD SCTPTEMPLATE）_09897332.md)** | SCTP到特定IP消息重传的最大次数（MAXPATHRETRY） | 4 | 本端规划 | - |
| **[ADD SCTPTEMPLATE](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/SCTP管理/SCTP模板/增加SCTP模板（ADD SCTPTEMPLATE）_09897332.md)** | SCTP协议校验和算法（CHECKSUMTYPE） | CRC32 | 本端规划 | - |
| **[ADD SCTPENDPOINT](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/SCTP管理/SCTP端点/增加SCTP端点（ADD SCTPENDPOINT）_09897321.md)** | 端点名称（ENDPOINTNAME） | pcrfendb<br>pcrfendc | 本端规划 | 对端定义两个端点为“pcrfendb”和“pcrfendc”，每个端点有两个IP地址，端点“pcrfendb”的IP地址为10.11.21.59和10.11.21.60，端点“pcrfendc”的IP地址为10.11.21.11和10.11.21.12。端口号均为3868。 |
| **[ADD SCTPENDPOINT](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/SCTP管理/SCTP端点/增加SCTP端点（ADD SCTPENDPOINT）_09897321.md)** | IP版本（IPVERSION） | IPV4 | 与对端协商 | 对端定义两个端点为“pcrfendb”和“pcrfendc”，每个端点有两个IP地址，端点“pcrfendb”的IP地址为10.11.21.59和10.11.21.60，端点“pcrfendc”的IP地址为10.11.21.11和10.11.21.12。端口号均为3868。 |
| **[ADD SCTPENDPOINT](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/SCTP管理/SCTP端点/增加SCTP端点（ADD SCTPENDPOINT）_09897321.md)** | IPv4地址1（IPV4ADDRESS1） | 10.11.21.59<br>10.11.21.11 | 全网规划 | 对端定义两个端点为“pcrfendb”和“pcrfendc”，每个端点有两个IP地址，端点“pcrfendb”的IP地址为10.11.21.59和10.11.21.60，端点“pcrfendc”的IP地址为10.11.21.11和10.11.21.12。端口号均为3868。 |
| **[ADD SCTPENDPOINT](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/SCTP管理/SCTP端点/增加SCTP端点（ADD SCTPENDPOINT）_09897321.md)** | IPv4地址2（IPV4ADDRESS2） | 10.11.21.60<br>10.11.21.12 | 全网规划 | 对端定义两个端点为“pcrfendb”和“pcrfendc”，每个端点有两个IP地址，端点“pcrfendb”的IP地址为10.11.21.59和10.11.21.60，端点“pcrfendc”的IP地址为10.11.21.11和10.11.21.12。端口号均为3868。 |
| **[ADD SCTPENDPOINT](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/SCTP管理/SCTP端点/增加SCTP端点（ADD SCTPENDPOINT）_09897321.md)** | 端口号(PORT) | 3868 | 与对端协商 | 对端定义两个端点为“pcrfendb”和“pcrfendc”，每个端点有两个IP地址，端点“pcrfendb”的IP地址为10.11.21.59和10.11.21.60，端点“pcrfendc”的IP地址为10.11.21.11和10.11.21.12。端口号均为3868。 |
| **[ADD SCTPENDPOINT](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/SCTP管理/SCTP端点/增加SCTP端点（ADD SCTPENDPOINT）_09897321.md)** | SCTP模板名称（SCTPTEMPLNAME） | testtemplate | 已配置数据中获取 | 已通过<br>**[ADD SCTPTEMPLATE](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/SCTP管理/SCTP模板/增加SCTP模板（ADD SCTPTEMPLATE）_09897332.md)**<br>命令配置，可以使用<br>**[LST SCTPTEMPLATE](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/SCTP管理/SCTP模板/查询SCTP模板（LST SCTPTEMPLATE）_09897335.md)**<br>命令查询。 |
| **[SET GLBSCTPPARA](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/SCTP管理/SCTP基础参数/设置SCTP全局参数（SET GLBSCTPPARA）_09897326.md)** | SCTP路径选择模式（PATHSELECTMODE） | ALL | 全网规划 | - |
| **[SET GLBSCTPPARA](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/SCTP管理/SCTP基础参数/设置SCTP全局参数（SET GLBSCTPPARA）_09897326.md)** | RTO重发超时的最小值（毫秒）（RTOMINVALUE） | 500 | 与对端协商 | - |
| **[SET GLBSCTPPARA](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/SCTP管理/SCTP基础参数/设置SCTP全局参数（SET GLBSCTPPARA）_09897326.md)** | RTO重发超时的最大值（毫秒）（RTOMAXVALUE） | 1500 | 与对端协商 | - |
| **[SET GLBSCTPPARA](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/SCTP管理/SCTP基础参数/设置SCTP全局参数（SET GLBSCTPPARA）_09897326.md)** | RTO重发超时的初始值（毫秒）（RTOINITVALUE） | 500 | 与对端协商 | - |
| **[ADD PCRF](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF/增加PCRF（ADD PCRF）_09897101.md)** | PCRF主机名（HOSTNAME） | pcrf | 与对端协商 | PCC架构中PCRF的设备信息。 |
| **[ADD PCRF](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF/增加PCRF（ADD PCRF）_09897101.md)** | PCRF域名（REALMNAME） | pcrf.huawei.com | 全网规划 | PCC架构中PCRF的设备信息。 |
| **[ADD PCRF](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF/增加PCRF（ADD PCRF）_09897101.md)** | VPN实例（VPNINSTANCE） | vpn_gxif | 已配置数据中获取 | VPN实例已通过<br>[**ADD VPNINST**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/增加VPN实例（ADD VPNINST）_09653755.md)<br>命令配置，可以使用<br>[**LST VPNINST**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/查询VPN实例（LST VPNINST）_09651519.md)<br>命令进行查询。 |
| **[ADD DIAMPEERADDR](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)** | PCRF主机名（HOSTNAME） | pcrf | 与对端协商 | - |
| **[ADD DIAMPEERADDR](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)** | 地址类型（ADDRTYPE） | SCTP | 与对端协商 | - |
| **[ADD DIAMPEERADDR](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)** | SCTP端点名称（SCTPENDPOINT） | pcrfendb<br>pcrfendc | 已配置数据中获取 | 配置直连PCRF的SCTP端点名称，SCTP端点已通过<br>**[ADD SCTPENDPOINT](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/SCTP管理/SCTP端点/增加SCTP端点（ADD SCTPENDPOINT）_09897321.md)**<br>命令配置，可以使用<br>**[LST SCTPENDPOINT](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/SCTP管理/SCTP端点/查询SCTP端点（LST SCTPENDPOINT）_09897324.md)**<br>查询。 |
| **[ADD DIAMCONNGRP](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md)** | Diameter链路组名（CONNGROUPNAME） | dconn_gx | 本端规划 | 本端的一个端点与对端的两个端点“pcrfendb”和“pcrfendc”构建两个偶联，参数<br>“SELECTMODE”<br>用来配置两个偶联间的链路选择模式。 |
| **[ADD DIAMCONNGRP](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md)** | 本端主机名（LOCALHOSTNAME） | unc_1 | 全网规划 | 本端的一个端点与对端的两个端点“pcrfendb”和“pcrfendc”构建两个偶联，参数<br>“SELECTMODE”<br>用来配置两个偶联间的链路选择模式。 |
| **[ADD DIAMCONNGRP](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md)** | 对端主机名（PEERHOSTNAME） | pcrf | 与对端协商 | 本端的一个端点与对端的两个端点“pcrfendb”和“pcrfendc”构建两个偶联，参数<br>“SELECTMODE”<br>用来配置两个偶联间的链路选择模式。 |
| **[ADD DIAMCONNGRP](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md)** | Diameter应用（APPLICATION） | GX | 全网规划 | 本端的一个端点与对端的两个端点“pcrfendb”和“pcrfendc”构建两个偶联，参数<br>“SELECTMODE”<br>用来配置两个偶联间的链路选择模式。 |
| **[ADD DIAMCONNGRP](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md)** | 链路选择模式（SELECTMODE） | SESSION_ID | 全网规划 | 本端的一个端点与对端的两个端点“pcrfendb”和“pcrfendc”构建两个偶联，参数<br>“SELECTMODE”<br>用来配置两个偶联间的链路选择模式。 |
| **[SET CONCENPOINT](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/基础参数/集中点模式/设置集中点部署模式（SET CONCENPOINT）_09896704.md)** | Gx集中点模式(GXCONCENMODE) | LOCALPORT | 本端规划 | - |
| **[ADD DIAMCONNECTION](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md)** | Diameter链路组名 | dconn_gx | 已配置数据中获取 | 已经通过<br>**[ADD DIAMCONNGRP](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md)**<br>命令配置，可以使用<br>**[LST DIAMCONNGRP](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/查询Diameter链路组（LST DIAMCONNGRP）_09897264.md)**<br>查询。 |
| **[ADD DIAMCONNECTION](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md)** | 本端接口名（LOCINTERFACE） | gxif1/0/0 | 已配置数据中获取 | 已经通过<br>**[ADD LOGICINF](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)**<br>命令配置，可以使用<br>**[LST LOGICINF](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/查询逻辑接口（LST LOGICINF）_09896726.md)**<br>查询。 |
| **[ADD DIAMCONNECTION](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md)** | 本端端口（LOCALPORT） | 16400 | 本端规划 | - |
| **[ADD DIAMCONNECTION](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md)** | 对端SCTP端点名称（PEERSCTPENDPT） | pcrfendb<br>pcrfendc | 已配置数据中获取 | SCTP端点已通过<br>**[ADD SCTPENDPOINT](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/SCTP管理/SCTP端点/增加SCTP端点（ADD SCTPENDPOINT）_09897321.md)**<br>命令配置，可以使用<br>**[LST SCTPENDPOINT](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/SCTP管理/SCTP端点/查询SCTP端点（LST SCTPENDPOINT）_09897324.md)**<br>查询。 |
| **[ADD DIAMCONNECTION](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md)** | 对端地址类型（PEERADDRTYPE） | SCTP | 与对端协商 | - |
| **[ADD DIAMCONNECTION](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md)** | SCTP建链交换本端IP地址（REVERSEIP） | ENABLE | 与对端协商 | - |

## [操作步骤](#ZH-CN_OPI_0230442391)

1. 进入 “MML命令行-UNC” 窗口。
2. 打开本特性的License配置开关。
  **[SET LICENSESWITCH](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)**
3. 创建VPN实例。
  **[**ADD VPNINSTAF**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例地址族/增加L3VPN实例地址族（ADD VPNINSTAF）_49802178.md)**
4. 配置SCTP本端端点。
  **[ADD LOGICINF](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)**
  > **说明**
  > 在对端的端口号为奇数时，可以通过 **[MOD DIAMCONNECTION](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/修改Diameter链路（MOD DIAMCONNECTION）_09897267.md)** 命令设置 “REVERSEIP” 为 “ENABLE” 来颠倒本端的主从IP地址，与对端建立偶联，即本端配置的从IP作为偶联的主IP，本端配置的主IP作为偶联的从IP。
5. 配置本端端点的主机信息。
  [**ADD DIAMLOCINFO**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter本端信息/增加Diameter本端信息（ADD DIAMLOCINFO）_09897271.md)
6. 配置SCTP模板参数。
  **[ADD SCTPTEMPLATE](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/SCTP管理/SCTP模板/增加SCTP模板（ADD SCTPTEMPLATE）_09897332.md)**
  > **说明**
  > SCTP模板可以应用在不同的SCTP偶联上，即一个SCTP模板可以绑定到不同的SCTP端点上。如Gx、Gy接口建立的SCTP偶联可以使用相同的SCTP模板参数，也可以使用不同的SCTP模板参数。
7. 配置SCTP对端端点及主机信息。
    a. 配置对端端点信息。
      **[ADD SCTPENDPOINT](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/SCTP管理/SCTP端点/增加SCTP端点（ADD SCTPENDPOINT）_09897321.md)**
    b. 重复执行 **[ADD SCTPENDPOINT](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/SCTP管理/SCTP端点/增加SCTP端点（ADD SCTPENDPOINT）_09897321.md)** 命令，配置多个对端端点。
      > **说明**
      > GGSN/PGW-C可以与一个PCRF的多个SCTP端点间建立多条SCTP偶联，各偶联间为主备还是负荷分担模式通过 **[ADD DIAMCONNGRP](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md)** 命令中的 “SELECTMODE” 参数来设置。
8. 配置SCTP重传超时（RTO，Retransmission Time-Out）参数，缺省使用初始值；配置SCTP偶联内使用路径的模式，本场景采用全路径模式。
  **[SET GLBSCTPPARA](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/SCTP管理/SCTP基础参数/设置SCTP全局参数（SET GLBSCTPPARA）_09897326.md)**
9. 配置对端端点的主机信息。
    a. 配置PCRF。
      **[ADD PCRF](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF/增加PCRF（ADD PCRF）_09897101.md)**
    b. 配置PCRF的SCTP端点。
      **[ADD DIAMPEERADDR](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)**
      > **说明**
      > **[ADD PCRF](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF/增加PCRF（ADD PCRF）_09897101.md)** 的主机名 “HOSTNAME” 和域名 “REALMNAME” 要与 **[ADD DIAMPEERADDR](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)** 命令配置的一致。
10. 建立本端与对端的链路组，并配置链路选择模式。
  **[ADD DIAMCONNGRP](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md)**
11. 配置Gx接口Diameter应用集中点模式。缺省情况下，本端的端口号不可配，使用系统自动分配的端口号。
  **[SET CONCENPOINT](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/基础参数/集中点模式/设置集中点部署模式（SET CONCENPOINT）_09896704.md)**
12. 建立本端到对端SCTP端点的链路。
  **[ADD DIAMCONNECTION](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md)**
  > **说明**
  > 当 “Gx集中点模式” 通过 **[SET CONCENPOINT](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/基础参数/集中点模式/设置集中点部署模式（SET CONCENPOINT）_09896704.md)** 命令选择为 “LOCALPORT” 时，支持使用 **[ADD DIAMCONNECTION](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md)** 命令设置本端的端口号。

## [验证方法](#ZH-CN_OPI_0230442391)

具体步骤请参见 [调测Gx over SCTP功能](../调测SCTP/调测Gx over SCTP功能_30442392.md) 。

## [任务示例](#ZH-CN_OPI_0230442391)

任务描述

如 [图1](#ZH-CN_OPI_0230442391__fig1) 所示，GGSN/PGW-C上定义的一个端点SCTP Endpoint A和PCRF上定义的两个端点SCTP Endpoint B、SCTP Endpoint C之间构建两个偶联，偶联间负荷分担基于用户的信令消息，每个偶联采用SCTP双归属，即一个偶联中包含四条路径，一条首选路径和三条备选路径。每个端点的具体信息如下：

- SCTP Endpoint A（gxif1/0/0）：10.8.20.1（主IP）/16400、10.8.20.2（从IP）/16400
- SCTP Endpoint B：10.11.21.59/3868、10.11.21.60/3868
- SCTP Endpoint C：10.11.21.11/3868、10.11.21.12/3868

> **说明**
> GGSN/PGW-C上可以配置多个端点，与同一个远端端点形成不同的偶联。

**图1** SCTP多归属连接

<br>

![](配置Gx over SCTP功能_30442391.assets/zh-cn_image_0230555069_2.png)

脚本

//打开本特性的License配置开关。

```
SET LICENSESWITCH:LICITEM="LKV3WPSCTP11",SWITCH=ENABLE;
```

//配置SCTP本端端点。

```
ADD VPNINST: VPNINSTANCE="vpn_gxif";
ADD LOGICINF:NAME="gxif1/0/0",IPVERSION=IPV4,IPV4ADDRESS1="10.8.20.1",IPV4MASK1="255.255.255.255",IPV4ADDRESS2="10.8.20.2",IPV4MASK2="255.255.255.255",VPNINSTANCE="vpn_gxif";
```

//配置本端端点的主机信息，端口号固定，由系统自动生成。

```
ADD DIAMLOCINFO:HOSTNAME="unc_1",REALMNAME="example.com",PRODUCTNAME="unc";
```

//配置SCTP模板参数。

```
ADD SCTPTEMPLATE:SCTPTEMPLNAME="testtemplate",HEARTBEATINTVAL=30000,MAXASSOCRETRY=5,MAXPATHRETRY=4,CHECKSUMTYPE=CRC32;
```

//配置2个SCTP对端端点，并将模板分别与SCTP端点绑定。

```
ADD SCTPENDPOINT:ENDPOINTNAME="pcrfendb",IPVERSION=IPV4,IPV4ADDRESS1="10.11.21.59",IPV4ADDRESS2="10.11.21.60",PORT=3868,SCTPTEMPLNAME="testtemplate";
ADD SCTPENDPOINT:ENDPOINTNAME="pcrfendc",IPVERSION=IPV4,IPV4ADDRESS1="10.11.21.11",IPV4ADDRESS2="10.11.21.12",PORT=3868,SCTPTEMPLNAME="testtemplate";
```

//配置SCTP重传超时（RTO，Retransmission Time-Out）参数和SCTP偶联内使用路径的模式。

```
SET GLBSCTPPARA:PATHSELECTMODE=ALL,RTOMINVALUE=500,RTOMAXVALUE=1500,RTOINITVALUE=500;
```

//配置PCRF的设备标识及其主机信息。

```
ADD PCRF:HOSTNAME="pcrf",REALMNAME="pcrf.huawei.com",VPNINSTANCE="vpn_gxif";
ADD DIAMPEERADDR:HOSTNAME="pcrf",ADDRTYPE=SCTP,SCTPENDPOINT="pcrfendb";
ADD DIAMPEERADDR:HOSTNAME="pcrf",ADDRTYPE=SCTP,SCTPENDPOINT="pcrfendc";
```

//建立本端与对端的链路组，并配置链路选择模式。

```
ADD DIAMCONNGRP:CONNGROUPNAME="dconn_gx",LOCALHOSTNAME="unc_1",APPLICATION=GX,PEERHOSTNAME="pcrf",SELECTMODE=SESSION_ID;
```

//建立本端到对端SCTP端点的链路。

```
SET CONCENPOINT:GXCONCENMODE=LOCALPORT;
```

```
ADD DIAMCONNECTION:DIAMCONNGRP="dconn_gx",LOCINTERFACE="gxif1/0/0",LOCALPORT=16400,PEERADDRTYPE=SCTP,PEERSCTPENDPT="pcrfendb";
ADD DIAMCONNECTION:DIAMCONNGRP="dconn_gx",LOCINTERFACE="gxif1/0/0",LOCALPORT=16400,PEERADDRTYPE=SCTP,PEERSCTPENDPT="pcrfendc";
```
