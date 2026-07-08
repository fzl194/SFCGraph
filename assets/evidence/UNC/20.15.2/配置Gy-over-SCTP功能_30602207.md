# 配置Gy over SCTP功能

- [操作场景](#ZH-CN_OPI_0230602207__1.3.1)
- [必备事项](#ZH-CN_OPI_0230602207__1.3.2)
- [操作步骤](#ZH-CN_OPI_0230602207__1.3.3)
- [验证方法](#ZH-CN_OPI_0230602207__1.3.4)
- [任务示例](#ZH-CN_OPI_0230602207__1.3.5)

## [操作场景](#ZH-CN_OPI_0230602207)

运营商规划与OCS对接时使用SCTP功能，以提高Gy接口信令传输的可靠性，则需要在GGSN/PGW-C上部署SCTP功能，保证与OCS信令链路的连通性。

> **说明**
> 适用于 GGSN、 PGW-C。

## [必备事项](#ZH-CN_OPI_0230602207)

前提条件

- 请仔细阅读 [WSFD-104508 SCTP](../../WSFD-104508 SCTP_27680892.md) 。
- 如果运营商规划采用VPN组网方式，则操作员在执行本操作前应已创建了相应的VPN实例。
- GGSN/PGW-C与OCS之间的物理链路已连通。
- 完成加载License（如果有需求，请联系华为技术支持工程师处理）。

数据

与OCS对接使用SCTP时，GGSN/PGW-C支持使用IPv4或IPv6地址进行对接，本处以IPv4为例进行说明。

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| [**ADD VPNINST**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/增加VPN实例（ADD VPNINST）_09653755.md) | VPN实例名称（VPNINSTANCE） | vpn_gyif | 本端规划 | - |
| **[ADD LOGICINF](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)** | 逻辑接口名称（NAME） | gyif1/0/0 | 本端规划 | 其中10.8.10.1为主IP地址，10.8.10.2为从IP地址。 |
| **[ADD LOGICINF](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)** | 逻辑接口的IP版本（IPVERSION） | IPV4 | 本端规划 | 其中10.8.10.1为主IP地址，10.8.10.2为从IP地址。 |
| **[ADD LOGICINF](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)** | 逻辑接口的IPv4地址1（IPV4ADDRESS1） | 10.8.10.1 | 全网规划 | 其中10.8.10.1为主IP地址，10.8.10.2为从IP地址。 |
| **[ADD LOGICINF](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)** | 逻辑接口的IPv4地址2（IPV4ADDRESS2） | 10.8.10.2 | 全网规划 | 其中10.8.10.1为主IP地址，10.8.10.2为从IP地址。 |
| **[ADD LOGICINF](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)** | 逻辑接口的IPv4掩码1（IPV4MASK1） | 255.255.255.255 | 固定取值 | 逻辑接口的IP掩码只能为255.255.255.255，或掩码长度32。 |
| **[ADD LOGICINF](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)** | 逻辑接口的IPv4掩码2（IPV4MASK2） | 255.255.255.255 | 固定取值 | 逻辑接口的IP掩码只能为255.255.255.255，或掩码长度32。 |
| **[ADD LOGICINF](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)** | VPN实例名称（VPNINSTANCE） | vpn_gyif | 已配置数据中获取 | 接口绑定的VPN实例已通过<br>[**ADD VPNINST**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/增加VPN实例（ADD VPNINST）_09653755.md)<br>命令配置，可以使用<br>[**LST VPNINST**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/查询VPN实例（LST VPNINST）_09651519.md)<br>命令进行查询。 |
| [**ADD DIAMLOCINFO**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter本端信息/增加Diameter本端信息（ADD DIAMLOCINFO）_09897271.md) | 本端主机名（HOSTNAME） | unc_1 | 与对端协商 | GGSN/PGW-C的设备信息。其中host和realm需要与OCS上配置的一致。 |
| [**ADD DIAMLOCINFO**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter本端信息/增加Diameter本端信息（ADD DIAMLOCINFO）_09897271.md) | 本端域名（REALMNAME） | example.com | 与对端协商 | GGSN/PGW-C的设备信息。其中host和realm需要与OCS上配置的一致。 |
| [**ADD DIAMLOCINFO**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter本端信息/增加Diameter本端信息（ADD DIAMLOCINFO）_09897271.md) | 产品名称（PRODUCTNAME） | unc | 与对端协商 | GGSN/PGW-C的设备信息。其中host和realm需要与OCS上配置的一致。 |
| **[ADD SCTPTEMPLATE](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/SCTP管理/SCTP模板/增加SCTP模板（ADD SCTPTEMPLATE）_09897332.md)** | SCTP模板名称（SCTPTEMPLNAME） | testtemplate | 本端规划 | - |
| **[ADD SCTPTEMPLATE](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/SCTP管理/SCTP模板/增加SCTP模板（ADD SCTPTEMPLATE）_09897332.md)** | SCTP发送心跳消息的间隔周期（毫秒）（HEARTBEATINTVAL） | 30000 | 本端规划 | - |
| **[ADD SCTPTEMPLATE](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/SCTP管理/SCTP模板/增加SCTP模板（ADD SCTPTEMPLATE）_09897332.md)** | SCTP耦联上消息重传的最大次数（MAXASSOCRETRY） | 5 | 本端规划 | - |
| **[ADD SCTPTEMPLATE](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/SCTP管理/SCTP模板/增加SCTP模板（ADD SCTPTEMPLATE）_09897332.md)** | SCTP到特定IP消息重传的最大次数（MAXPATHRETRY） | 4 | 本端规划 | - |
| **[ADD SCTPTEMPLATE](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/SCTP管理/SCTP模板/增加SCTP模板（ADD SCTPTEMPLATE）_09897332.md)** | SCTP协议校验和算法（CHECKSUMTYPE） | CRC32 | 本端规划 | - |
| **[ADD SCTPENDPOINT](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/SCTP管理/SCTP端点/增加SCTP端点（ADD SCTPENDPOINT）_09897321.md)** | 端点名称（ENDPOINTNAME） | ocsend | 本端规划 | 对端端点的IP地址和端口号。对端端点有两个IP地址，分别为10.10.11.59和10.10.11.60。 |
| **[ADD SCTPENDPOINT](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/SCTP管理/SCTP端点/增加SCTP端点（ADD SCTPENDPOINT）_09897321.md)** | IP版本（IPVERSION） | IPV4 | 本端规划 | 对端端点的IP地址和端口号。对端端点有两个IP地址，分别为10.10.11.59和10.10.11.60。 |
| **[ADD SCTPENDPOINT](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/SCTP管理/SCTP端点/增加SCTP端点（ADD SCTPENDPOINT）_09897321.md)** | IPv4地址1（IPV4ADDRESS1） | 10.11.11.59 | 本端规划 | 对端端点的IP地址和端口号。对端端点有两个IP地址，分别为10.10.11.59和10.10.11.60。 |
| **[ADD SCTPENDPOINT](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/SCTP管理/SCTP端点/增加SCTP端点（ADD SCTPENDPOINT）_09897321.md)** | IPv4地址2（IPV4ADDRESS2） | 10.11.11.60 | 本端规划 | 对端端点的IP地址和端口号。对端端点有两个IP地址，分别为10.10.11.59和10.10.11.60。 |
| **[ADD SCTPENDPOINT](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/SCTP管理/SCTP端点/增加SCTP端点（ADD SCTPENDPOINT）_09897321.md)** | 端口号（PORT） | 3868 | 与对端协商 | 对端端点的IP地址和端口号。对端端点有两个IP地址，分别为10.10.11.59和10.10.11.60。 |
| **[ADD SCTPENDPOINT](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/SCTP管理/SCTP端点/增加SCTP端点（ADD SCTPENDPOINT）_09897321.md)** | SCTP模板名称（SCTPTEMPLNAME） | testtemplate | 已配置数据中获取 | 已通过<br>**[ADD SCTPTEMPLATE](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/SCTP管理/SCTP模板/增加SCTP模板（ADD SCTPTEMPLATE）_09897332.md)**<br>命令配置，可以使用<br>**[LST SCTPTEMPLATE](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/SCTP管理/SCTP模板/查询SCTP模板（LST SCTPTEMPLATE）_09897335.md)**<br>命令查询。 |
| **[SET GLBSCTPPARA](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/SCTP管理/SCTP基础参数/设置SCTP全局参数（SET GLBSCTPPARA）_09897326.md)** | SCTP路径选择模式（PATHSELECTMODE） | ALL | 全网规划 | - |
| **[ADD OCS](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/OCS Diameter连接/OCS Server/增加OCS（ADD OCS）_09896954.md)** | Ocs主机名称（OCSHOSTNAME） | ocs | 与对端协商 | 与OCS上的配置保持一致。 |
| **[ADD OCS](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/OCS Diameter连接/OCS Server/增加OCS（ADD OCS）_09896954.md)** | Ocs域名（REALMNAME） | ocs.huawei.com | 与对端协商 | 与OCS上的配置保持一致。 |
| **[ADD OCS](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/OCS Diameter连接/OCS Server/增加OCS（ADD OCS）_09896954.md)** | VPN实例<br>（VPNINSTANCE） | vpn_gyif | 已配置数据中获取 | VPN实例已通过<br>[**ADD VPNINST**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/增加VPN实例（ADD VPNINST）_09653755.md)<br>命令配置，可以使用<br>[**LST VPNINST**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/查询VPN实例（LST VPNINST）_09651519.md)<br>命令进行查询。 |
| **[ADD DIAMPEERADDR](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)** | Ocs主机名称（OCSHOSTNAME） | ocs | 已配置数据中获取 | 已通过<br>**[ADD OCS](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/OCS Diameter连接/OCS Server/增加OCS（ADD OCS）_09896954.md)**<br>命令配置，可以通过<br>**[LST OCS](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/OCS Diameter连接/OCS Server/查询OCS（LST OCS）_09896957.md)**<br>命令进行查询。 |
| **[ADD DIAMPEERADDR](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)** | 地址类型（ADDRTYPE） | SCTP | 与对端协商 | 配置直连OCS的SCTP端点名称，SCTP端点已通过<br>**[ADD SCTPENDPOINT](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/SCTP管理/SCTP端点/增加SCTP端点（ADD SCTPENDPOINT）_09897321.md)**<br>命令配置，可以使用<br>**[LST SCTPENDPOINT](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/SCTP管理/SCTP端点/查询SCTP端点（LST SCTPENDPOINT）_09897324.md)**<br>查询。 |
| **[ADD DIAMPEERADDR](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)** | SCTP端点名称（SCTPENDPOINT） | ocsend | 已配置数据中获取 | 配置直连OCS的SCTP端点名称，SCTP端点已通过<br>**[ADD SCTPENDPOINT](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/SCTP管理/SCTP端点/增加SCTP端点（ADD SCTPENDPOINT）_09897321.md)**<br>命令配置，可以使用<br>**[LST SCTPENDPOINT](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/SCTP管理/SCTP端点/查询SCTP端点（LST SCTPENDPOINT）_09897324.md)**<br>查询。 |
| **[ADD DIAMCONNGRP](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md)** | Diameter链路组名（CONNGROUPNAME） | dconn_gy | 本端规划 | - |
| **[ADD DIAMCONNGRP](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md)** | 本端主机名（LOCALHOSTNAME） | unc_1 | 全网规划 | - |
| **[ADD DIAMCONNGRP](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md)** | 对端主机名（PEERHOSTNAME） | ocs | 与对端协商 | - |
| **[ADD DIAMCONNGRP](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md)** | Diameter应用（APPLICATION） | GY | 全网规划 | - |
| **[ADD DIAMCONNGRP](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md)** | 链路选择模式（SELECTMODE） | SESSION_ID | 全网规划 | - |
| **[SET CONCENPOINT](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/基础参数/集中点模式/设置集中点部署模式（SET CONCENPOINT）_09896704.md)** | Gy集中点模式(GYCONCENMODE) | LOCALPORT | 本端规划 | - |
| **[ADD DIAMCONNECTION](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md)** | Diameter链路组名 | dconn_gy | 已配置数据中获取 | 已经通过<br>**[ADD DIAMCONNGRP](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md)**<br>命令配置，可以使用<br>**[LST DIAMCONNGRP](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/查询Diameter链路组（LST DIAMCONNGRP）_09897264.md)**<br>查询。 |
| **[ADD DIAMCONNECTION](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md)** | 本端接口名（LOCINTERFACE） | gyif1/0/0 | 已配置数据中获取 | 已经通过<br>[**ADD LOGICINF**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)<br>命令配置，可以使用<br>[**LST LOGICINF**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/查询逻辑接口（LST LOGICINF）_09896726.md)<br>查询。 |
| **[ADD DIAMCONNECTION](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md)** | 本端端口（LOCALPORT） | 13200 | 本端规划 | - |
| **[ADD DIAMCONNECTION](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md)** | 对端SCTP端点名称（PEERSCTPENDPT） | ocsend | 已配置数据中获取 | SCTP端点已通过<br>**[ADD SCTPENDPOINT](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/SCTP管理/SCTP端点/增加SCTP端点（ADD SCTPENDPOINT）_09897321.md)**<br>命令配置，可以使用<br>**[LST SCTPENDPOINT](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/SCTP管理/SCTP端点/查询SCTP端点（LST SCTPENDPOINT）_09897324.md)**<br>查询。 |
| **[ADD DIAMCONNECTION](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md)** | 对端地址类型（PEERADDRTYPE） | SCTP | 与对端协商 | - |
| **[ADD DIAMCONNECTION](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md)** | SCTP建链交换本端IP地址（REVERSEIP） | ENABLE | 与对端协商 | - |

## [操作步骤](#ZH-CN_OPI_0230602207)

1. 进入 “MML命令行-UNC” 窗口。
2. 打开本特性的License配置开关。
  **[SET LICENSESWITCH](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)**
3. 创建VPN实例。
  **[**ADD VPNINSTAF**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例地址族/增加L3VPN实例地址族（ADD VPNINSTAF）_49802178.md)**
4. 配置SCTP本端端点。
  **[ADD LOGICINF](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)**
  > **说明**
  > 在对端的端口号为奇数时，可以通过 [**MOD DIAMCONNECTION**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/修改Diameter链路（MOD DIAMCONNECTION）_09897267.md) 命令设置 “REVERSEIP” 为 “ENABLE” 来颠倒本端的主从IP地址，与对端建立偶联，即本端配置的从IP作为偶联的主IP，本端配置的主IP作为偶联的从IP。
5. 配置本端端点的主机信息。
  [**ADD DIAMLOCINFO**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter本端信息/增加Diameter本端信息（ADD DIAMLOCINFO）_09897271.md)
6. 配置SCTP模板参数。
  **[ADD SCTPTEMPLATE](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/SCTP管理/SCTP模板/增加SCTP模板（ADD SCTPTEMPLATE）_09897332.md)**
  > **说明**
  > SCTP模板可以应用在不同的SCTP偶联上，即一个SCTP模板可以绑定到不同的SCTP端点上。如Gx、Gy接口建立的SCTP偶联可以使用相同的SCTP模板参数，也可以使用不同的SCTP模板参数。
7. **可选：**配置SCTP对端端点及主机信息。
    a. 配置对端端点信息。
      **[ADD SCTPENDPOINT](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/SCTP管理/SCTP端点/增加SCTP端点（ADD SCTPENDPOINT）_09897321.md)**
    b. 重复执行 **[ADD SCTPENDPOINT](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/SCTP管理/SCTP端点/增加SCTP端点（ADD SCTPENDPOINT）_09897321.md)** 命令，配置多个对端端点。
      > **说明**
      > GGSN/PGW-C可以与一个OCS的多个SCTP端点间建立多条SCTP偶联，各偶联间为主备还是负荷分担模式通过 [**ADD DIAMCONNGRP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md) 命令中的 “SELECTMODE” 参数来设置。
8. 配置SCTP偶联内使用路径的模式，本场景采用全路径模式，即SCTP多归属模式。
  **[SET GLBSCTPPARA](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/SCTP管理/SCTP基础参数/设置SCTP全局参数（SET GLBSCTPPARA）_09897326.md)**
9. 配置对端端点的主机信息。
    a. 配置OCS。
      **[ADD OCS](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/OCS Diameter连接/OCS Server/增加OCS（ADD OCS）_09896954.md)**
    b. 配置OCS的SCTP端点。
      **[ADD DIAMPEERADDR](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)**
      > **说明**
      > **[ADD OCS](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/OCS Diameter连接/OCS Server/增加OCS（ADD OCS）_09896954.md)** 的主机名 “OCSHOSTNAME” 和域名 “REALMNAME” 要与 **[ADD DIAMPEERADDR](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)** 命令配置的一致。
10. 建立本端与对端的链路组，并配置链路选择模式。
  **[ADD DIAMCONNGRP](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md)**
11. 配置Gy接口Diameter应用集中点模式。缺省情况下，本端的端口号不可配，使用系统自动分配的端口号。
  **[SET CONCENPOINT](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/基础参数/集中点模式/设置集中点部署模式（SET CONCENPOINT）_09896704.md)**
12. 建立本端到对端SCTP端点的链路。
  **[ADD DIAMCONNECTION](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md)**
  > **说明**
  > 当 “Gy集中点模式” 通过 **[SET CONCENPOINT](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/基础参数/集中点模式/设置集中点部署模式（SET CONCENPOINT）_09896704.md)** 命令选择为 “LOCALPORT” 时，支持使用 **[ADD DIAMCONNECTION](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md)** 命令设置本端的端口号。

## [验证方法](#ZH-CN_OPI_0230602207)

具体步骤请参见 [调测Gy over SCTP功能](../调测SCTP/调测Gy over SCTP功能_30602208.md) 。

## [任务示例](#ZH-CN_OPI_0230602207)

任务描述

如 [图1](#ZH-CN_OPI_0230602207__fig1) 所示，GGSN/PGW-C上定义一个端点SCTP Endpoint A，端点中包含两个IP地址，分别为gyif1/0/0的主从IP地址10.8.10.1和10.8.10.2，OCS上定义一个端点SCTP Endpoint B，包含两个IP地址10.11.11.59和10.11.11.60，SCTP Endpoint A和SCTP Endpoint B之间形成一个偶联，且采用SCTP双归属，即一个偶联中包含四条路径，一条首选路径和三条备选路径。

> **说明**
> GGSN/PGW-C上可以配置多个端点，与同一个远端端点形成不同的偶联。

**图1** SCTP多归属连接

<br>

![](配置Gy over SCTP功能_30602207.assets/zh-cn_image_0230638532_2.png)

脚本

//打开本特性的License配置开关。

```
SET LICENSESWITCH:LICITEM="LKV3WPSCTP11",SWITCH=ENABLE;
```

//配置SCTP本端端点。

```
ADD VPNINST: VPNINSTANCE="vpn_gyif";
ADD LOGICINF:NAME="gyif1/0/0",IPVERSION=IPV4,IPV4ADDRESS1="10.8.10.1",IPV4MASK1="255.255.255.255",IPV4ADDRESS2="10.8.10.2",IPV4MASK2="255.255.255.255",VPNINSTANCE="vpn_gyif";
```

//配置本端端点的主机信息，端口号固定，由系统自动生成。

```
ADD DIAMLOCINFO:HOSTNAME="unc_1",REALMNAME="example.com",PRODUCTNAME="unc";
```

//配置SCTP模板参数。

```
ADD SCTPTEMPLATE:SCTPTEMPLNAME="testtemplate",HEARTBEATINTVAL=30000,MAXASSOCRETRY=5,MAXPATHRETRY=4,CHECKSUMTYPE=CRC32;
```

//配置SCTP对端端点，并将模板分别与SCTP端点绑定。

```
ADD SCTPENDPOINT:ENDPOINTNAME="ocsend",IPVERSION=IPV4,IPV4ADDRESS1="10.11.11.59",IPV4ADDRESS2="10.11.11.60",PORT=3868,SCTPTEMPLNAME="testtemplate";
```

//配置SCTP重传超时（RTO，Retransmission Time-Out）参数和SCTP偶联内使用路径的模式。

```
SET GLBSCTPPARA:PATHSELECTMODE=ALL,RTOMINVALUE=500,RTOMAXVALUE=1500,RTOINITVALUE=500;
```

//配置OCS的设备标识及其主机信息。

```
ADD OCS:OCSHOSTNAME="ocs",REALMNAME="ocs.huawei.com",VPNINSTANCE="vpn_gyif";
ADD DIAMPEERADDR:HOSTNAME="ocs",ADDRTYPE=SCTP,SCTPENDPOINT="ocsend";
```

//建立本端与对端的链路组，并配置链路选择模式。

```
ADD DIAMCONNGRP:CONNGROUPNAME="dconn_gy",LOCALHOSTNAME="unc_1",APPLICATION=GY,PEERHOSTNAME="ocs",SELECTMODE=SESSION_ID;
```

//建立本端到对端SCTP端点的链路。

```
SET CONCENPOINT:GYCONCENMODE=LOCALPORT;
```

```
ADD DIAMCONNECTION:DIAMCONNGRP="dconn_gy",LOCINTERFACE="gyif1/0/0",LOCALPORT=13200,PEERADDRTYPE=SCTP,PEERSCTPENDPT="ocsend";
```
