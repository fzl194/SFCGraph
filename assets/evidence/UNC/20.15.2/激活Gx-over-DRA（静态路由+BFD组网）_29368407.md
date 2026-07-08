# 激活Gx over DRA（静态路由+BFD组网）

- [操作场景](#ZH-CN_OPI_0229368407__1.3.1)
- [必备事项](#ZH-CN_OPI_0229368407__1.3.2)
- [操作步骤](#ZH-CN_OPI_0229368407__1.3.3)
- [任务示例一：Gx over DRA（TCP链路）](#ZH-CN_OPI_0229368407__1.3.4)
- [任务示例二：Gx over DRA（SCTP链路）](#ZH-CN_OPI_0229368407__1.3.5)

## [操作场景](#ZH-CN_OPI_0229368407)

当GGSN/PGW-C与PCRF之间直连路径故障或者未配置直连路径时，可以配置到Gx over DRA，DRA在GGSN/PGW-C与PCRF间转交消息，提供PCRF服务器寻址功能。

> **说明**
> 适用于 GGSN、 PGW-C。

## [必备事项](#ZH-CN_OPI_0229368407)

前提条件

- 请仔细阅读 [WSFD-011132 Gx over DRA特性概述](特性概述_29315043.md) 。
- 如果运营商规划采用VPN组网方式，则操作员在执行本操作前应已创建了相应的VPN实例。
- 提前进行Gx接口信令组网规划，获取DRA以及PCRF所属Realm等配置信息。
- 已通过**[ADD LOGICIP](../../../../../OM参考/命令/UNC MML命令/平台服务管理/IP管理/IP配置/增加逻辑IP地址（ADD LOGICIP）_09587376.md)**配置完成逻辑接口使用到的逻辑IP。

数据

*表1 本端数据*

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| [**ADD VPNINST**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/增加VPN实例（ADD VPNINST）_09653755.md) | VPN实例名(VPNINSTANCE) | vpn_gxif | 本端规划 | - |
| **[SET CONCENPOINT](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/基础参数/集中点模式/设置集中点部署模式（SET CONCENPOINT）_09896704.md)** | Gx集中点模式(GXCONCENMODE) | LOCALPORT | 本端规划 | - |
| **[ADD LOGICIP](../../../../../OM参考/命令/UNC MML命令/平台服务管理/IP管理/IP配置/增加逻辑IP地址（ADD LOGICIP）_09587376.md)** | IP地址类型（IPVERSION） | IPv4 | 本端规划 | 逻辑接口使用的逻辑IP。 |
| **[ADD LOGICIP](../../../../../OM参考/命令/UNC MML命令/平台服务管理/IP管理/IP配置/增加逻辑IP地址（ADD LOGICIP）_09587376.md)** | IPv4地址（LOGICIPV4） | 10.8.10.1<br>10.8.10.2 | 本端规划 | 逻辑接口使用的逻辑IP。 |
| **[ADD LOGICINF](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)** | 逻辑接口名称（NAME） | gxif1/0/0 | 全网规划 | 逻辑接口的IP掩码只能为255.255.255.255，或掩码长度32。 |
| **[ADD LOGICINF](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)** | 逻辑接口的IP版本（IPVERSION） | IPv4 | 本端规划 | 逻辑接口的IP掩码只能为255.255.255.255，或掩码长度32。 |
| **[ADD LOGICINF](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)** | 逻辑接口的IPv4地址1(IPV4ADDRESS1) | 10.8.10.1 | 全网规划 | 逻辑接口的IP掩码只能为255.255.255.255，或掩码长度32。 |
| **[ADD LOGICINF](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)** | 逻辑接口的IPv4掩码1(IPV4MASK1) | 255.255.255.255 | 固定取值 | 逻辑接口的IP掩码只能为255.255.255.255，或掩码长度32。 |
| **[ADD LOGICINF](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)** | 逻辑接口的IPv4地址2(IPV4ADDRESS2) | 10.8.10.2 | 全网规划 | 逻辑接口的IP掩码只能为255.255.255.255，或掩码长度32。 |
| **[ADD LOGICINF](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)** | 逻辑接口的IPv4掩码2(IPV4MASK2) | 255.255.255.255 | 固定取值 | 逻辑接口的IP掩码只能为255.255.255.255，或掩码长度32。 |
| **[ADD LOGICINF](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)** | VPN实例名称（VPNINSTANCE） | vpn_gxif | 已配置数据中获取 | 接口绑定的VPN实例已通过<br>[**ADD VPNINST**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/增加VPN实例（ADD VPNINST）_09653755.md)<br>命令配置，可以使用<br>[**LST VPNINST**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/查询VPN实例（LST VPNINST）_09651519.md)<br>命令进行查询。 |

*表2 对端DRA数据（TCP）*

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| **[SET DIAMETERPARA](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/路由控制/Diameter路由控制/设置Diameter参数（SET DIAMETERPARA）_09897315.md)** | 基于域名的路由功能开关（REALMBASEROUTE） | ENABLE | 本端规划 | - |
| **[ADD DRA](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/DRA管理/DRA信息/增加DRA（ADD DRA）_09897291.md)** | 主机名（HOSTNAME） | host1.example.com<br>host2.example.com | 本端规划 | - |
| **[ADD DRA](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/DRA管理/DRA信息/增加DRA（ADD DRA）_09897291.md)** | VPN实例（VPNINSTANCE） | vpn_gxif | 已配置数据中获取 | - |
| **[ADD DIAMPEERADDR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)** | 主机名称（HOSTNAME） | host1.example.com<br>host2.example.com | 已配置数据中获取 | - |
| **[ADD DIAMPEERADDR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)** | 地址类型（ADDRTYPE） | IPv4 | 与对端协商 | - |
| **[ADD DIAMPEERADDR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)** | IPv4地址（IPV4ADDRESS） | 10.10.0.1<br>10.10.0.2<br>10.10.10.1<br>10.10.10.2 | 与对端协商 | - |

*表3 对端DRA数据（SCTP）*

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| **[ADD SCTPENDPOINT](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/SCTP管理/SCTP端点/增加SCTP端点（ADD SCTPENDPOINT）_09897321.md)** | 端点名称（ENDPOINTNAME） | endpoint0<br>endpoint1<br>endpoint2<br>endpoint3 | 本端规划 | 对端端点的IP地址和端口号。对端端点各有两个IP地址，分别如下。<br>- 192.168.0.1和192.168.0.2<br>- 192.168.10.1和192.168.10.2<br>- 192.168.1.1和192.168.1.2<br>- 192.168.11.1和192.168.11.2 |
| **[ADD SCTPENDPOINT](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/SCTP管理/SCTP端点/增加SCTP端点（ADD SCTPENDPOINT）_09897321.md)** | IP版本（IPVERSION） | IPV4 | 与对端协商 | 对端端点的IP地址和端口号。对端端点各有两个IP地址，分别如下。<br>- 192.168.0.1和192.168.0.2<br>- 192.168.10.1和192.168.10.2<br>- 192.168.1.1和192.168.1.2<br>- 192.168.11.1和192.168.11.2 |
| **[ADD SCTPENDPOINT](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/SCTP管理/SCTP端点/增加SCTP端点（ADD SCTPENDPOINT）_09897321.md)** | IPv4地址1（IPV4ADDRESS1） | 192.168.0.1<br>192.168.10.1<br>192.168.1.1<br>192.168.11.1 | 全网规划 | 对端端点的IP地址和端口号。对端端点各有两个IP地址，分别如下。<br>- 192.168.0.1和192.168.0.2<br>- 192.168.10.1和192.168.10.2<br>- 192.168.1.1和192.168.1.2<br>- 192.168.11.1和192.168.11.2 |
| **[ADD SCTPENDPOINT](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/SCTP管理/SCTP端点/增加SCTP端点（ADD SCTPENDPOINT）_09897321.md)** | IPv4地址2（IPV4ADDRESS2） | 192.168.0.2<br>192.168.10.2<br>192.168.1.2<br>192.168.11.2 | 全网规划 | 对端端点的IP地址和端口号。对端端点各有两个IP地址，分别如下。<br>- 192.168.0.1和192.168.0.2<br>- 192.168.10.1和192.168.10.2<br>- 192.168.1.1和192.168.1.2<br>- 192.168.11.1和192.168.11.2 |
| **[ADD SCTPENDPOINT](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/SCTP管理/SCTP端点/增加SCTP端点（ADD SCTPENDPOINT）_09897321.md)** | 端口号（PORT） | 3868 | 与对端协商 | 对端端点的IP地址和端口号。对端端点各有两个IP地址，分别如下。<br>- 192.168.0.1和192.168.0.2<br>- 192.168.10.1和192.168.10.2<br>- 192.168.1.1和192.168.1.2<br>- 192.168.11.1和192.168.11.2 |
| **[SET DIAMETERPARA](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/路由控制/Diameter路由控制/设置Diameter参数（SET DIAMETERPARA）_09897315.md)** | 基于域名的路由功能开关（REALMBASEROUTE） | ENABLE | 本端规划 | - |
| **[ADD DRA](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/DRA管理/DRA信息/增加DRA（ADD DRA）_09897291.md)** | 主机名（HOSTNAME） | host1.example.com<br>host2.example.com | 本端规划 | - |
| **[ADD DRA](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/DRA管理/DRA信息/增加DRA（ADD DRA）_09897291.md)** | VPN实例（VPNINSTANCE） | vpn_gxif | 已配置数据中获取 | - |
| **[ADD DIAMPEERADDR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)** | 主机名称（HOSTNAME） | host1.example.com<br>host2.example.com | 已配置数据中获取 | - |
| **[ADD DIAMPEERADDR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)** | 地址类型（ADDRTYPE） | SCTP | 与对端协商 | - |
| **[ADD DIAMPEERADDR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)** | SCTP端点名称（SCTPENDPOINT） | endpoint0<br>endpoint1<br>endpoint2<br>endpoint3 | 与对端协商 | DRA绑定的SCTP端点已经通过<br>**[ADD SCTPENDPOINT](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/SCTP管理/SCTP端点/增加SCTP端点（ADD SCTPENDPOINT）_09897321.md)**<br>命令配置，可以使用<br>**[LST SCTPENDPOINT](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/SCTP管理/SCTP端点/查询SCTP端点（LST SCTPENDPOINT）_09897324.md)**<br>命令查询。 |

*表4 对接数据*

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| **[ADD DIAMLOCINFO](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter本端信息/增加Diameter本端信息（ADD DIAMLOCINFO）_09897271.md)** | 本端主机名（HOSTNAME） | unc_1 | 本端规划 | PCC架构中的设备信息。 |
| **[ADD DIAMLOCINFO](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter本端信息/增加Diameter本端信息（ADD DIAMLOCINFO）_09897271.md)** | 本端域名（REALMNAME） | example1.com | 与对端协商 | PCC架构中的设备信息。 |
| **[ADD DIAMLOCINFO](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter本端信息/增加Diameter本端信息（ADD DIAMLOCINFO）_09897271.md)** | 产品名称（PRODUCTNAME） | unc | 本端规划 | PCC架构中的设备信息。 |
| **[ADD DIAMCONNGRP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md)** | Diameter链路组名（CONNGROUPNAME） | dconn_gx1<br>dconn_gx2 | 本端规划 | - |
| **[ADD DIAMCONNGRP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md)** | 本端主机名（LOCALHOSTNAME） | unc_1 | 全网规划 | - |
| **[ADD DIAMCONNGRP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md)** | 对端主机名（PEERHOSTNAME） | host1.example.com<br>host2.example.com | 全网规划 | - |
| **[ADD DIAMCONNGRP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md)** | Diameter应用（APPLICATION） | GX | 全网规划 | - |
| **[ADD DIAMCONNGRP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md)** | 链路选择模式（SELECTMODE） | SESSION_ID | 全网规划 | - |
| **[ADD DIAMCONNECTION](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md)** | Diameter链路组名 | dconn_gx1<br>dconn_gx2 | 本端规划 | - |
| **[ADD DIAMCONNECTION](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md)** | 本端接口名（LOCINTERFACE） | gxif1/0/0 | 本端规划 | - |
| **[ADD DIAMCONNECTION](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md)** | 本端端口（LOCALPORT） | 16401<br>16402 | 本端规划 | - |
| **[ADD DIAMRTREALM](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/路由管理/Diameter路由/增加Diameter路由域名信息（ADD DIAMRTREALM）_09897303.md)** | Diameter域名名称（REALMNAME） | pcrf.huawei.com | 与对端协商 | - |
| **[ADD DIAMRTREALM](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/路由管理/Diameter路由/增加Diameter路由域名信息（ADD DIAMRTREALM）_09897303.md)** | Diameter应用（APPLICATION） | GX | 全网规划 | - |
| **[ADD DIAMRTREALM](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/路由管理/Diameter路由/增加Diameter路由域名信息（ADD DIAMRTREALM）_09897303.md)** | 路由选择模式（SELECTMODE） | MASTER_SLAVE | 全网规划 | - |
| **[ADD DIAMRTNEXTHOP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/路由管理/Diameter路由配置/增加Diameter路由下一跳（ADD DIAMRTNEXTHOP）_09897310.md)** | Diameter域名名称（REALMNAME） | pcrf.huawei.com | 与对端协商 | 说明：下一跳的主机名<br>“HOSTNAME”<br>只允许设置成已配置的DRA主机名。 |
| **[ADD DIAMRTNEXTHOP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/路由管理/Diameter路由配置/增加Diameter路由下一跳（ADD DIAMRTNEXTHOP）_09897310.md)** | Diameter应用（APPLICATION） | GX | 全网规划 | 说明：下一跳的主机名<br>“HOSTNAME”<br>只允许设置成已配置的DRA主机名。 |
| **[ADD DIAMRTNEXTHOP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/路由管理/Diameter路由配置/增加Diameter路由下一跳（ADD DIAMRTNEXTHOP）_09897310.md)** | 下一跳（NEXTHOP） | host1.example.com<br>host2.example.com | 已配置数据中获取 | 说明：下一跳的主机名<br>“HOSTNAME”<br>只允许设置成已配置的DRA主机名。 |
| **[ADD DIAMRTNEXTHOP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/路由管理/Diameter路由配置/增加Diameter路由下一跳（ADD DIAMRTNEXTHOP）_09897310.md)** | 序号（SEQUENCE） | 1<br>2 | 本端规划 | 说明：下一跳的主机名<br>“HOSTNAME”<br>只允许设置成已配置的DRA主机名。 |

*表5 业务数据*

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| **[ADD PCCTEMPLATE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md)** | PCC模板名称（PCCTEMPNAME） | test_template | 本端规划 | 配置由DRA或PCRF触发的PCRF重选和PCRF倒换。 |
| **[ADD PCCTEMPLATE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md)** | 基于CCA-I Origin-Host AVP触发PCRF重选（ORGHOSTCCAI） | ENABLE | 全网规划 | 配置由DRA或PCRF触发的PCRF重选和PCRF倒换。 |
| **[ADD PCCTEMPLATE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md)** | 基于CCA-U Origin-Host AVP触发PCRF重选（ORGHOSTCCAU） | ENABLE | 全网规划 | 配置由DRA或PCRF触发的PCRF重选和PCRF倒换。 |
| **[ADD PCCTEMPLATE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md)** | 基于RAR Origin-Host AVP触发PCRF重选（ORGHOSTRAR） | ENABLE | 全网规划 | 配置由DRA或PCRF触发的PCRF重选和PCRF倒换。 |
| **[SET PCCFUNC](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC功能（SET PCCFUNC）_09897057.md)** | 本地用户动态PCC功能（HOMEPCCSWITCH） | ENABLE | 本端规划 | 配置全局PCC开关。 |
| **[SET PCCFUNC](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC功能（SET PCCFUNC）_09897057.md)** | 漫游用户动态PCC功能（ROAMPCCSWITCH） | ENABLE | 本端规划 | 配置全局PCC开关。 |
| **[SET PCCFUNC](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC功能（SET PCCFUNC）_09897057.md)** | 拜访用户动态PCC功能（VISITPCCSWITCH） | ENABLE | 本端规划 | 配置全局PCC开关。 |
| **[ADD GLBDIAMREALM](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter Realm/全局Realm/增加全局Diameter域（ADD GLBDIAMREALM）_09897280.md)** | IMSI/MSISDN号段名称（SEGMENTNAME） | imsi_msisdn_segment_1 | 本端规划 | 用户号段已通过增加IMSI和MSISDN号段<br>**[ADD IMSIMSISDNSEG](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务公共/IMSI MSISDN号段/增加IMSI和MSISDN号段（ADD IMSIMSISDNSEG）_09897128.md)**<br>命令配置，可以使用查询IMSI和MSISDN号段<br>**[LST IMSIMSISDNSEG](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务公共/IMSI MSISDN号段/查询IMSI和MSISDN号段（LST IMSIMSISDNSEG）_09897131.md)**<br>命令进行查询。 |
| **[ADD GLBDIAMREALM](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter Realm/全局Realm/增加全局Diameter域（ADD GLBDIAMREALM）_09897280.md)** | 优先级（PRIORITY） | 2 | 全网规划 | - |
| **[ADD GLBDIAMREALM](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter Realm/全局Realm/增加全局Diameter域（ADD GLBDIAMREALM）_09897280.md)** | 根据IMSI构造归属地Realm开关（CONSTBYIMSISW） | DISABLE | 全网规划 | - |
| **[ADD GLBDIAMREALM](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter Realm/全局Realm/增加全局Diameter域（ADD GLBDIAMREALM）_09897280.md)** | Diameter域名（REALM） | pcrf.huawei.com | 与对端协商 | - |
| **[ADD GLBDIAMREALM](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter Realm/全局Realm/增加全局Diameter域（ADD GLBDIAMREALM）_09897280.md)** | Diameter应用（APPLICATION） | GX | 本端规划 | - |
| **[SET APNPCCFUNC](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/设置APN PCC功能（SET APNPCCFUNC）_09897034.md)** | APN名称（APN） | apn-test | 全网规划 | 已通过命令<br>**[ADD APN](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)**<br>进行配置，可以使用命令<br>**[LST APN](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/查询APN配置（LST APN）_09652599.md)**<br>查询。 |
| **[SET APNPCCFUNC](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/设置APN PCC功能（SET APNPCCFUNC）_09897034.md)** | PCC模板名称（PCCTEMPLATE） | test_template | 已配置数据中获取 | - |
| **[SET APNPCCFUNC](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/设置APN PCC功能（SET APNPCCFUNC）_09897034.md)** | 本地用户动态PCC功能（HOMEPCCSWITCH） | ENABLE | 与对端协商 | - |
| **[SET APNPCCFUNC](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/设置APN PCC功能（SET APNPCCFUNC）_09897034.md)** | 漫游用户动态PCC功能（ROAMPCCSWITCH） | ENABLE | 与对端协商 | - |
| **[SET APNPCCFUNC](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/设置APN PCC功能（SET APNPCCFUNC）_09897034.md)** | 拜访用户动态PCC功能（VISITPCCSWITCH） | ENABLE | 与对端协商 | - |
| **[ADD REALMBINDAPN](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter Realm/Realm绑定APN/增加APN与Diameter Realm关联关系（ADD REALMBINDAPN）_09897285.md)** | APN名称（APN） | apn-test | 全网规划 | 已通过命令<br>**[ADD APN](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)**<br>进行配置，可以使用命令<br>**[LST APN](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/查询APN配置（LST APN）_09652599.md)**<br>查询。 |
| **[ADD REALMBINDAPN](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter Realm/Realm绑定APN/增加APN与Diameter Realm关联关系（ADD REALMBINDAPN）_09897285.md)** | Diameter应用（APPLICATION） | GX | 与对端协商 | - |
| **[ADD REALMBINDAPN](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter Realm/Realm绑定APN/增加APN与Diameter Realm关联关系（ADD REALMBINDAPN）_09897285.md)** | 根据IMSI构造归属地Realm开关（CONSTBYIMSISW） | DISABLE | 全网规划 | - |
| **[ADD REALMBINDAPN](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter Realm/Realm绑定APN/增加APN与Diameter Realm关联关系（ADD REALMBINDAPN）_09897285.md)** | Realm名（REALMNAME） | pcrf.huawei.com | 全网规划 | - |

## [操作步骤](#ZH-CN_OPI_0229368407)

1. 参考 [静态路由+BFD组网](../../../../初始配置/UNC初始配置与调测/组网路由配置/配置VNF侧IP路由数据（非SDN）/自动部署（推荐）/配置静态路由+BFD组网（IPv4）_75096861.md) 配置对应的组网。
2. 进入 “MML命令行-UNC” 窗口。
3. 创建一个VPN实例。
  [**ADD VPNINST**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/增加VPN实例（ADD VPNINST）_09653755.md)
4. **可选：**配置Gx接口Diameter应用集中点模式。缺省情况下，本端的端口号不可配，使用系统自动分配的端口号。
  **[SET CONCENPOINT](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/基础参数/集中点模式/设置集中点部署模式（SET CONCENPOINT）_09896704.md)**
  > **说明**
  > - LOCALIP_PEER模式下，ADD DIAMCONNECTION命令添加的链路，仅LocalPort参数未配置或配置为0的链路生效。LocalPort参数配置为非0的链路，允许配置下发，但是不会建链。
  > - LOCALPORT模式下，ADD DIAMCONNECTION命令添加的链路，仅LocalPort参数配置为非0的链路生效。LocalPort参数未配置或配置为0的链路，允许配置下发，但是不会建链。
5. 配置Gx逻辑接口。
  **[ADD LOGICIP](../../../../../OM参考/命令/UNC MML命令/平台服务管理/IP管理/IP配置/增加逻辑IP地址（ADD LOGICIP）_09587376.md)**
  **[ADD LOGICINF](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)**
6. 配置GGSN/PGW-C的设备标识。
  **[ADD DIAMLOCINFO](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter本端信息/增加Diameter本端信息（ADD DIAMLOCINFO）_09897271.md)**
7. 配置PCRF信息及动态PCRF主机列表表项老化时长。
    a. 配置PCRF信息。
      **[ADD PCRF](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF/增加PCRF（ADD PCRF）_09897101.md)**
      > **说明**
      > 如果PCRF未配置域信息，则需要在本步骤中进行配置。
    b. **可选：**配置动态PCRF主机列表表项老化时长。
      **[SET PCCTIMER](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/定时器/设置PCC定时器（SET PCCTIMER）_09897082.md)**
8. 配置SCTP端点信息。
  **[ADD SCTPENDPOINT](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/SCTP管理/SCTP端点/增加SCTP端点（ADD SCTPENDPOINT）_09897321.md)**
  > **说明**
  > 如果GGSN/PGW-C和DRA之间选择SCTP链路，则需要在此步骤中配置SCTP的端点信息。
9. 配置DRA信息。
    a. 使能Realm-Based Routing。
      **[SET DIAMETERPARA](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/路由控制/Diameter路由控制/设置Diameter参数（SET DIAMETERPARA）_09897315.md)**
    b. 配置DRA主机名以及地址信息。
      **[ADD DRA](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/DRA管理/DRA信息/增加DRA（ADD DRA）_09897291.md)**
      **[ADD DIAMPEERADDR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)**
      > **说明**
      > - 只有App与IP/SCTP都配置才会生效。
      > - 对于同一个DRA，不允许同时配置IP地址和SCTP端点。
      >     - 如果配置IP地址，则**[ADD DIAMPEERADDR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)**中ADDRTYPE需要配置为IPv4，且需要在IPV4ADDRESS中输入对应的IPv4地址；
      >     - 如果配置SCTP端点，则**[ADD DIAMPEERADDR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)**ADDRTYPE需要配置为SCTP，且需要再SCTPENDPOINT中输入对应的SCTP端点名称。
      > - DRA与Diameter实体PCRF/OCS/AAA的主机名不能重复。
    c. 配置到DRA的链路组信息。
      **[ADD DIAMCONNGRP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md)**
    d. 配置到DRA的链路。
      **[ADD DIAMCONNECTION](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md)**
      > **说明**
      > 配置链路时如果不选择地址类型，则表示本端接口与对端主机的全部地址建立链接。
      >
      > 当 “Gx集中点模式” 通过 **[SET CONCENPOINT](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/基础参数/集中点模式/设置集中点部署模式（SET CONCENPOINT）_09896704.md)** 命令选择为 “LOCALPORT” 时，可使用 **[ADD DIAMCONNECTION](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md)** 命令设置本端的端口号。
    e. 配置PCRF域的Diameter路由。
      **[ADD DIAMRTREALM](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/路由管理/Diameter路由/增加Diameter路由域名信息（ADD DIAMRTREALM）_09897303.md)**
      **[ADD DIAMRTNEXTHOP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/路由管理/Diameter路由配置/增加Diameter路由下一跳（ADD DIAMRTNEXTHOP）_09897310.md)**
10. 配置激活和更新流程中，网关是否支持由DRA或PCRF触发的PCRF重选和PCRF倒换，并将PCC Template绑定到APN下。
    a. 配置PCC模板。
      **[ADD PCCTEMPLATE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md)**
    b. 配置APN。
      **[ADD APN](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)**
      > **说明**
      > 同一个APN只能配置TCP/SCTP中的一种场景，不允许两种场景同时配置到同一APN下。
    c. 将PCC Template绑定到APN下。
      **[SET APNPCCFUNC](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/设置APN PCC功能（SET APNPCCFUNC）_09897034.md)**
11. 开启全局缺省PCC开关并设置域名绑定。
    a. 配置IMSI或MSISDN号码段。
      **[ADD IMSIMSISDNSEG](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务公共/IMSI MSISDN号段/增加IMSI和MSISDN号段（ADD IMSIMSISDNSEG）_09897128.md)**
    b. 使能全局PCC开关。
      **[SET PCCFUNC](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC功能（SET PCCFUNC）_09897057.md)**
      > **说明**
      > GGSN/PGW-C支持基于用户的漫游属性开启PCC功能，可通过本命令使能本地用户、漫游用户和/或拜访用户的PCC功能。
    c. 将PCRF域和用户号段绑定。
      **[ADD GLBDIAMREALM](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter Realm/全局Realm/增加全局Diameter域（ADD GLBDIAMREALM）_09897280.md)**
      > **说明**
      > 为了可以更加灵活的和支持不同协议版本和不同能力的DRA进行对接，GGSN/PGW-C支持Supported Features动态协商功能，即与DRA在IP-CAN Session建立过程中进行协商，决定GGSN/PGW-C和DRA之间的会话按照哪个协议版本进行交互，或指示和DRA是否具有相应的Feature能力。Supported Features动态协商功能使能时，GGSN/PGW-C与DRA间协议版本支持能力的协商过程和GGSN/PGW-C与PCRF之间协商过程相同，协商流程请参见 [WSFD-109101 PCC基本功能](../../智能PCC解决方案/WSFD-109101 PCC基本功能_60374767.md) 。如果需要与指定DRA进行Supported Features动态协商，则需要将 **[ADD REALMBINDAPN](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter Realm/Realm绑定APN/增加APN与Diameter Realm关联关系（ADD REALMBINDAPN）_09897285.md)** 命令中的 “SUPFTNEGOSW” 参数设置为 “ENABLE” ，并选择对应的feature选项。
      **[ADD GLBDIAMREALM](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter Realm/全局Realm/增加全局Diameter域（ADD GLBDIAMREALM）_09897280.md)**
12. 设置APN所属的域名。
  **[ADD REALMBINDAPN](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter Realm/Realm绑定APN/增加APN与Diameter Realm关联关系（ADD REALMBINDAPN）_09897285.md)**

## [任务示例一：Gx over DRA（TCP链路）](#ZH-CN_OPI_0229368407)

任务描述

本实例中，将在GGSN/PGW-C上进行数据配置实现以下要求：

- GGSN/PGW-C使用逻辑接口与DRA连通。
- GGSN/PGW-C与主机名为host1.example.com、host2.example.com的DRA建立起多TCP链路。
- 两条Diameter路由，第一跳指向DRA1（host1.example.com），第二跳指向DRA2（host2.example.com）。

**图1** Gx over DRA（TCP链路）

<br>

![](激活Gx over DRA（静态路由+BFD组网）_29368407.assets/zh-cn_image_0263658297_2.png)

脚本

1. 参考[静态路由+BFD组网](../../../../初始配置/UNC初始配置与调测/组网路由配置/配置VNF侧IP路由数据（非SDN）/自动部署（推荐）/配置静态路由+BFD组网（IPv4）_75096861.md)配置对应的组网。
2. 配置本端数据。
  //创建一个VPN实例。
  ```
  ADD VPNINST:VPNINSTANCE="vpn_gxif";
  ```
  //配置Gx接口Diamteter应用集中点模式。
  ```
  SET CONCENPOINT:GXCONCENMODE=LOCALPORT;
  ```
  //配置Gx逻辑接口。

  ```
  ADD LOGICIP: IPVERSION=IPv4, LOGICIPV4="10.8.10.1";
  ADD LOGICIP: IPVERSION=IPv4, LOGICIPV4="10.8.10.2";
  ADD LOGICINF:NAME="gxif1/0/0",IPVERSION=IPV4,IPV4ADDRESS1="10.8.10.1",IPV4MASK1="255.255.255.255",IPV4ADDRESS2="10.8.10.2",IPV4MASK2="255.255.255.255",VPNINSTANCE="vpn_gxif";
  ```
3. 配置DRA数据。
  //使能Realm-Based Routing。
  ```
  SET DIAMETERPARA:REALMBASEROUTE=ENABLE;
  ```
  //配置DRA主机名以及地址信息。
  ```
  ADD DRA:HOSTNAME="host1.example.com",VPNINSTANCE="vpn_gxif";
  ADD DRA:HOSTNAME="host2.example.com",VPNINSTANCE="vpn_gxif";
  ADD DIAMPEERADDR:HOSTNAME="host1.example.com",ADDRTYPE=IPv4,IPV4ADDRESS="10.10.0.1";
  ADD DIAMPEERADDR:HOSTNAME="host1.example.com",ADDRTYPE=IPv4,IPV4ADDRESS="10.10.0.2";
  ADD DIAMPEERADDR:HOSTNAME="host2.example.com",ADDRTYPE=IPv4,IPV4ADDRESS="10.10.10.1";
  ADD DIAMPEERADDR:HOSTNAME="host2.example.com",ADDRTYPE=IPv4,IPV4ADDRESS="10.10.10.2";
  ```
4. 配置对接数据。
  //配置GGSN/PGW-C的设备标识。
  ```
  ADD DIAMLOCINFO:HOSTNAME="unc_1",REALMNAME="example1.com",PRODUCTNAME="unc";
  ```
  //配置网元对接。
  ```
  ADD DIAMCONNGRP:CONNGROUPNAME="dconn_gx1",LOCALHOSTNAME="unc_1",APPLICATION=GX,PEERHOSTNAME="host1.example.com",SELECTMODE=SESSION_ID;
  ADD DIAMCONNGRP:CONNGROUPNAME="dconn_gx2",LOCALHOSTNAME="unc_1",APPLICATION=GX,PEERHOSTNAME="host2.example.com",SELECTMODE=SESSION_ID;
  ADD DIAMCONNECTION:DIAMCONNGRP="dconn_gx1",LOCINTERFACE="gxif1/0/0",LOCALPORT=16401;
  ADD DIAMCONNECTION:DIAMCONNGRP="dconn_gx2",LOCINTERFACE="gxif1/0/0",LOCALPORT=16402;
  ADD DIAMRTREALM:REALMNAME="pcrf.huawei.com",APPLICATION=GX,SELECTMODE=MASTER_SLAVE;
  ADD DIAMRTNEXTHOP:REALMNAME="pcrf.huawei.com",APPLICATION=GX,NEXTHOP="host1.example.com",SEQUENCE=1;
  ADD DIAMRTNEXTHOP:REALMNAME="pcrf.huawei.com",APPLICATION=GX,NEXTHOP="host2.example.com",SEQUENCE=2;
  ```
5. 配置业务数据。
  //配置激活和更新流程中，网关支持由DRA或PCRF触发的PCRF重选和PCRF倒换，并将PCC Template绑定到APN下。
  ```
  ADD PCCTEMPLATE:PCCTEMPNAME="test_template",ORGHOSTCCAI=ENABLE,ORGHOSTCCAU=ENABLE,ORGHOSTRAR=ENABLE;
  ```
  ```
  ADD APN:APN="apn-test";
  ```
  ```
  SET APNPCCFUNC:APN="apn-test",PCCTEMPLATE="test_template",HOMEPCCSWITCH=ENABLE,ROAMPCCSWITCH=ENABLE,VISITPCCSWITCH=ENABLE;
  ```
  //配置全局缺省的PCC开关，将PCRF域pcrf.huawei.com和用户号段imsi_msisdn_segment_1绑定。
  ```
  ADD IMSIMSISDNSEG:SEGMENTNAME="imsi_msisdn_segment_1",SEGMENTTYPE=MSISDN,SEGSTART="13800000000",SEGEND="13849999999";
  ```
  ```
  SET PCCFUNC:HOMEPCCSWITCH=ENABLE,ROAMPCCSWITCH=ENABLE,VISITPCCSWITCH=ENABLE;
  ```
  ```
  ADD GLBDIAMREALM:APPLICATION=GX,SEGMENTNAME="imsi_msisdn_segment_1",PRIORITY=2,CONSTBYIMSISW=DISABLE,REALM="pcrf.huawei.com";
  ```
  //开启APN下的PCC开关，配置APN下对应的PCRF归属域信息为pcrf.huawei.com。
  ```
  ADD REALMBINDAPN:APN="apn-test",APPLICATION=GX,CONSTBYIMSISW=DISABLE,REALMNAME="pcrf.huawei.com";
  ```

## [任务示例二：Gx over DRA（SCTP链路）](#ZH-CN_OPI_0229368407)

任务描述

本实例中，在GGSN/PGW-C上进行数据配置实现以下要求：

- GGSN/PGW-C使用逻辑接口与DRA连通。
- GGSN/PGW-C与主机名为host1.example.com、host2.example.com的DRA建立起多链路接SCTP偶联。
- 两条Diameter路由，第一跳指向DRA1（host1.example.com），第二跳指向DRA2（host2.example.com）。

**图2** Gx over DRA（SCTP链路）

<br>

![](激活Gx over DRA（静态路由+BFD组网）_29368407.assets/zh-cn_image_0263660810_2.png)

脚本

1. 参考[静态路由+BFD组网](../../../../初始配置/UNC初始配置与调测/组网路由配置/配置VNF侧IP路由数据（非SDN）/自动部署（推荐）/配置静态路由+BFD组网（IPv4）_75096861.md)配置对应的组网。
2. 配置本端数据。
  //创建一个VPN实例。
  ```
  ADD VPNINST:VPNINSTANCE="vpn_gxif";
  ```
  //配置Gx接口Diamteter应用集中点模式。
  ```
  SET CONCENPOINT:GXCONCENMODE=LOCALPORT;
  ```
  //配置Gx逻辑接口。

  ```
  ADD LOGICIP: IPVERSION=IPv4, LOGICIPV4="10.8.10.1";
  ADD LOGICIP: IPVERSION=IPv4, LOGICIPV4="10.8.10.2";
  ADD LOGICINF:NAME="gxif1/0/0",IPVERSION=IPV4,IPV4ADDRESS1="10.8.10.1",IPV4MASK1="255.255.255.255",IPV4ADDRESS2="10.8.10.2",IPV4MASK2="255.255.255.255",VPNINSTANCE="vpn_gxif";
  ```
3. 配置DRA数据。
  //使能Realm-Based Routing。
  ```
  SET DIAMETERPARA:REALMBASEROUTE=ENABLE;
  ```
  //配置SCTP端点信息。
  ```
  ADD SCTPENDPOINT:ENDPOINTNAME="endpoint0",IPVERSION=IPV4,IPV4ADDRESS1="192.168.0.1",IPV4ADDRESS2="192.168.0.2",PORT=3868;
  ```
  ```
  ADD SCTPENDPOINT:ENDPOINTNAME="endpoint1",IPVERSION=IPV4,IPV4ADDRESS1="192.168.10.1",IPV4ADDRESS2="192.168.10.2",PORT=3868;
  ```
  ```
  ADD SCTPENDPOINT:ENDPOINTNAME="endpoint2",IPVERSION=IPV4,IPV4ADDRESS1="192.168.1.1",IPV4ADDRESS2="192.168.1.2",PORT=3868;
  ```
  ```
  ADD SCTPENDPOINT:ENDPOINTNAME="endpoint3",IPVERSION=IPV4,IPV4ADDRESS1="192.168.11.1",IPV4ADDRESS2="192.168.11.2",PORT=3868;
  ```
  //配置DRA主机名以及地址信息。
  ```
  SET DIAMETERPARA:REALMBASEROUTE=ENABLE;
  ```
  ```
  ADD DRA:HOSTNAME="host1.example.com",VPNINSTANCE="vpn_gxif";
  ```
  ```
  ADD DRA:HOSTNAME="host2.example.com",VPNINSTANCE="vpn_gxif";
  ```
  ```
  ADD DIAMPEERADDR:HOSTNAME="host1.example.com",ADDRTYPE=SCTP,SCTPENDPOINT="endpoint0";
  ```
  ```
  ADD DIAMPEERADDR:HOSTNAME="host1.example.com",ADDRTYPE=SCTP,SCTPENDPOINT="endpoint1";
  ```
  ```
  ADD DIAMPEERADDR:HOSTNAME="host2.example.com",ADDRTYPE=SCTP,SCTPENDPOINT="endpoint2";
  ```
  ```
  ADD DIAMPEERADDR:HOSTNAME="host2.example.com",ADDRTYPE=SCTP,SCTPENDPOINT="endpoint3";
  ```
4. 配置对接数据。
  //配置GGSN/PGW-C的设备标识。
  ```
  ADD DIAMLOCINFO:HOSTNAME="unc_1",REALMNAME="example1.com",PRODUCTNAME="unc";
  ```
  //配置网元对接。
  ```
  ADD DIAMCONNGRP:CONNGROUPNAME="dconn_gx1",LOCALHOSTNAME="unc_1",APPLICATION=GX,PEERHOSTNAME="host1.example.com",SELECTMODE=SESSION_ID;
  ADD DIAMCONNGRP:CONNGROUPNAME="dconn_gx2",LOCALHOSTNAME="unc_1",APPLICATION=GX,PEERHOSTNAME="host2.example.com",SELECTMODE=SESSION_ID;
  ADD DIAMCONNECTION:DIAMCONNGRP="dconn_gx1",LOCINTERFACE="gxif1/0/0",LOCALPORT=16401,PEERADDRTYPE=SCTP,PEERSCTPENDPT="endpoint0";
  ADD DIAMCONNECTION:DIAMCONNGRP="dconn_gx1",LOCINTERFACE="gxif1/0/0",LOCALPORT=16401,PEERADDRTYPE=SCTP,PEERSCTPENDPT="endpoint1";
  ADD DIAMCONNECTION:DIAMCONNGRP="dconn_gx2",LOCINTERFACE="gxif1/0/0",LOCALPORT=16402,PEERADDRTYPE=SCTP,PEERSCTPENDPT="endpoint2";
  ADD DIAMCONNECTION:DIAMCONNGRP="dconn_gx2",LOCINTERFACE="gxif1/0/0",LOCALPORT=16402,PEERADDRTYPE=SCTP,PEERSCTPENDPT="endpoint3";
  ADD DIAMRTREALM:REALMNAME="pcrf.huawei.com",APPLICATION=GX,SELECTMODE=MASTER_SLAVE;
  ADD DIAMRTNEXTHOP:REALMNAME="pcrf.huawei.com",APPLICATION=GX,NEXTHOP="host1.example.com",SEQUENCE=1;
  ADD DIAMRTNEXTHOP:REALMNAME="pcrf.huawei.com",APPLICATION=GX,NEXTHOP="host2.example.com",SEQUENCE=2;
  ```
5. 配置业务数据。
  //配置激活和更新流程中，网关支持由DRA或PCRF触发的PCRF重选和PCRF倒换，并将PCC Template绑定到APN下。
  ```
  ADD PCCTEMPLATE:PCCTEMPNAME="test_template",ORGHOSTCCAI=ENABLE,ORGHOSTCCAU=ENABLE,ORGHOSTRAR=ENABLE;
  ```
  ```
  ADD APN:APN="apn-test";
  ```
  ```
  SET APNPCCFUNC:APN="apn-test",PCCTEMPLATE="test_template",HOMEPCCSWITCH=ENABLE,ROAMPCCSWITCH=ENABLE,VISITPCCSWITCH=ENABLE;
  ```
  //配置全局缺省的PCC开关，将PCRF域pcrf.huawei.com和用户号段imsi_msisdn_segment_1绑定。
  ```
  ADD IMSIMSISDNSEG:SEGMENTNAME="imsi_msisdn_segment_1",SEGMENTTYPE=MSISDN,SEGSTART="13800000000",SEGEND="13849999999";
  ```
  ```
  SET PCCFUNC:HOMEPCCSWITCH=ENABLE,ROAMPCCSWITCH=ENABLE,VISITPCCSWITCH=ENABLE;
  ```
  ```
  ADD GLBDIAMREALM:APPLICATION=GX,SEGMENTNAME="imsi_msisdn_segment_1",PRIORITY=2,CONSTBYIMSISW=DISABLE,REALM="pcrf.huawei.com";
  ```
  //开启APN下的PCC开关，配置APN下对应的PCRF归属域信息为pcrf.huawei.com。
  ```
  ADD REALMBINDAPN:APN="apn-test",APPLICATION=GX,CONSTBYIMSISW=DISABLE,REALMNAME="pcrf.huawei.com";
  ```
