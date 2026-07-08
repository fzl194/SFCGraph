# 激活Gy over DRA（静态路由+BFD组网）

- [操作场景](#ZH-CN_OPI_0229725460__1.3.1)
- [必备事项](#ZH-CN_OPI_0229725460__1.3.2)
- [操作步骤](#ZH-CN_OPI_0229725460__1.3.3)
- [任务示例一：Gy over DRA（TCP链路）](#ZH-CN_OPI_0229725460__1.3.4)
- [任务示例二：Gy over DRA（SCTP链路）](#ZH-CN_OPI_0229725460__1.3.5)

## [操作场景](#ZH-CN_OPI_0229725460)

当 GGSN/PGW-C 与OCS之间直连路径故障或者未配置直连路径时，可以配置Gy over DRA功能，DRA在 GGSN/PGW-C 与OCS间转交消息，提供OCS服务器寻址功能。

> **说明**
> 适用于 GGSN、 PGW-C。

## [必备事项](#ZH-CN_OPI_0229725460)

前提条件

- 请仔细阅读 [WSFD-011133 Gy over DRA特性概述](特性概述_29725459.md) 。
- 如果运营商规划采用VPN组网方式，则操作员在执行本操作前应已创建了相应的VPN实例。
- 提前进行Gy接口信令组网规划，获取DRA以及OCS所属Realm等配置信息。

数据

*表1 本端数据*

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| [**ADD VPNINST**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/增加VPN实例（ADD VPNINST）_09653755.md) | VPN实例名(VPNINSTANCE) | vpn_gyif | 本端规划 | - |
| **[SET CONCENPOINT](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/基础参数/集中点模式/设置集中点部署模式（SET CONCENPOINT）_09896704.md)** | Gy集中点模式(GYCONCENMODE) | LOCALPORT | 本端规划 | - |
| [**ADD LOGICIP**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/IP管理/IP配置/增加逻辑IP地址（ADD LOGICIP）_09587376.md) | IP地址类型（IPVERSION） | IPv4 | 本端规划 | 逻辑接口使用的逻辑IP。 |
| [**ADD LOGICIP**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/IP管理/IP配置/增加逻辑IP地址（ADD LOGICIP）_09587376.md) | IPv4地址（LOGICIPV4） | 10.8.10.1<br>10.8.10.2<br>10.8.10.4<br>10.8.10.5 | 本端规划 | 逻辑接口使用的逻辑IP。 |
| **[ADD LOGICINF](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)** | VPN实例名称（VPNINSTANCE） | vpn_gyif | 已配置数据中获取 | 接口绑定的VPN实例已通过<br>[**ADD VPNINST**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/增加VPN实例（ADD VPNINST）_09653755.md)<br>命令配置，可以使用<br>[**LST VPNINST**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/查询VPN实例（LST VPNINST）_09651519.md)<br>命令进行查询。 |
| **[ADD LOGICINF](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)** | 逻辑接口名称（NAME） | gxif1/0/0<br>gyif1/0/1 | 本端规划 | - |
| **[ADD LOGICINF](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)** | 逻辑接口的IP版本（IPVERSION） | IPv4 | 本端规划 | - |
| **[ADD LOGICINF](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)** | 逻辑接口的IPv4地址1(IPV4ADDRESS1) | 10.8.10.1<br>10.8.10.2 | 本端规划 | 其中10.8.10.1、10.8.10.2是逻辑接口的主IP地址，10.8.10.4、10.8.10.5是逻辑接口的从IP地址。 |
| **[ADD LOGICINF](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)** | 逻辑接口的IPv4地址2（IPV4ADDRESS2） | 10.8.10.4<br>10.8.10.5 | 本端规划 | 其中10.8.10.1、10.8.10.2是逻辑接口的主IP地址，10.8.10.4、10.8.10.5是逻辑接口的从IP地址。 |
| **[ADD LOGICINF](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)** | 逻辑接口的IPv4掩码1(IPV4MASK1) | 255.255.255.255 | 固定取值 | 逻辑接口的IP掩码只能为255.255.255.255，或掩码长度32。 |
| **[ADD LOGICINF](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)** | 逻辑接口的IPv4掩码2（IPV4MASK2） | 255.255.255.255 | 固定取值 | 逻辑接口的IP掩码只能为255.255.255.255，或掩码长度32。 |

*表2 对端DRA数据（SCTP）*

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| **[SET DIAMETERPARA](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/路由控制/Diameter路由控制/设置Diameter参数（SET DIAMETERPARA）_09897315.md)** | 基于域名的路由功能开关（REALMBASEROUTE） | ENABLE | 本端规划 | - |
| **[ADD SCTPENDPOINT](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/SCTP管理/SCTP端点/增加SCTP端点（ADD SCTPENDPOINT）_09897321.md)** | 端点名称（ENDPOINTNAME） | endpoint0<br>endpoint1<br>endpoint2<br>endpoint3 | 本端规划 | 对端端点的IP地址和端口号。对端端点各有两个IP地址，分别如下：<br>- 10.11.21.59和10.11.21.60<br>- 10.11.21.11和10.11.21.12<br>- 10.11.22.59和10.11.22.60<br>- 10.11.22.11和10.11.22.12 |
| **[ADD SCTPENDPOINT](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/SCTP管理/SCTP端点/增加SCTP端点（ADD SCTPENDPOINT）_09897321.md)** | IP版本（IPVERSION） | IPV4 | 全网规划 | 对端端点的IP地址和端口号。对端端点各有两个IP地址，分别如下：<br>- 10.11.21.59和10.11.21.60<br>- 10.11.21.11和10.11.21.12<br>- 10.11.22.59和10.11.22.60<br>- 10.11.22.11和10.11.22.12 |
| **[ADD SCTPENDPOINT](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/SCTP管理/SCTP端点/增加SCTP端点（ADD SCTPENDPOINT）_09897321.md)** | IPv4地址1（IPV4ADDRESS1） | 10.11.21.59<br>10.11.21.60<br>10.11.21.11<br>10.11.21.12 | 全网规划 | 对端端点的IP地址和端口号。对端端点各有两个IP地址，分别如下：<br>- 10.11.21.59和10.11.21.60<br>- 10.11.21.11和10.11.21.12<br>- 10.11.22.59和10.11.22.60<br>- 10.11.22.11和10.11.22.12 |
| **[ADD SCTPENDPOINT](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/SCTP管理/SCTP端点/增加SCTP端点（ADD SCTPENDPOINT）_09897321.md)** | 端口号（PORT） | 3868 | 与对端协商 | 对端端点的IP地址和端口号。对端端点各有两个IP地址，分别如下：<br>- 10.11.21.59和10.11.21.60<br>- 10.11.21.11和10.11.21.12<br>- 10.11.22.59和10.11.22.60<br>- 10.11.22.11和10.11.22.12 |
| **[ADD DRA](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/DRA管理/DRA信息/增加DRA（ADD DRA）_09897291.md)** | 主机名（HOSTNAME） | host1.example.com<br>host2.example.com | 本端规划 | - |
| **[ADD DRA](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/DRA管理/DRA信息/增加DRA（ADD DRA）_09897291.md)** | VPN实例（VPNINSTANCE） | vpn_gyif | 已配置数据中获取 | 已通过<br>[**ADD VPNINST**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/增加VPN实例（ADD VPNINST）_09653755.md)<br>命令配置。 |
| **[ADD DIAMPEERADDR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)** | 主机名称（HOSTNAME） | host1.example.com<br>host2.example.com | 已配置数据中获取 | 已通过<br>**[ADD DRA](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/DRA管理/DRA信息/增加DRA（ADD DRA）_09897291.md)**<br>命令配置。 |
| **[ADD DIAMPEERADDR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)** | 地址类型<br>（ADDRTYPE） | SCTP | 与对端协商 | - |
| **[ADD DIAMPEERADDR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)** | SCTP端点名称（SCTPENDPOINT） | endpoint0<br>endpoint1 | 已配置数据中获取 | 已通过<br>**[ADD SCTPENDPOINT](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/SCTP管理/SCTP端点/增加SCTP端点（ADD SCTPENDPOINT）_09897321.md)**<br>配置。 |

*表3 对端DRA数据（TCP）*

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| **[SET DIAMETERPARA](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/路由控制/Diameter路由控制/设置Diameter参数（SET DIAMETERPARA）_09897315.md)** | 基于域名的路由功能开关（REALMBASEROUTE） | ENABLE | 本端规划 | - |
| **[ADD DRA](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/DRA管理/DRA信息/增加DRA（ADD DRA）_09897291.md)** | 主机名（HOSTNAME） | host1.example.com<br>host2.example.com | 本端规划 | - |
| **[ADD DRA](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/DRA管理/DRA信息/增加DRA（ADD DRA）_09897291.md)** | VPN实例（VPNINSTANCE） | vpn_gyif | 已配置数据中获取 | 已通过<br>[**ADD VPNINST**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/增加VPN实例（ADD VPNINST）_09653755.md)<br>命令配置。 |
| **[ADD DIAMPEERADDR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)** | 主机名称（HOSTNAME） | host1.example.com<br>host2.example.com | 已配置数据中获取 | 已通过<br>**[ADD OCS](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/OCS Diameter连接/OCS Server/增加OCS（ADD OCS）_09896954.md)**<br>命令配置。 |
| **[ADD DIAMPEERADDR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)** | IPv4地址（IPV4ADDRESS） | 10.10.10.1<br>10.10.10.2<br>10.10.11.1<br>10.10.11.2 | 与对端协商 | - |
| **[ADD DIAMPEERADDR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)** | 端口号（PORT） | 3396<br>3397 | 全网规划 | - |
| **[ADD DIAMPEERADDR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)** | 地址类型<br>（ADDRTYPE） | IPv4 | 与对端协商 | - |

*表4 直连OCS信息*

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| **[ADD OCS](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/OCS Diameter连接/OCS Server/增加OCS（ADD OCS）_09896954.md)** | OCS主机名称（OCSHOSTNAME） | ocs1<br>ocs4 | 本端规划 | - |
| **[ADD OCS](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/OCS Diameter连接/OCS Server/增加OCS（ADD OCS）_09896954.md)** | OCS域名（REALMNAME） | ocs.huawei.com | 全网规划 | - |
| **[ADD OCS](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/OCS Diameter连接/OCS Server/增加OCS（ADD OCS）_09896954.md)** | VPN实例（VPNINSTANCE） | vpn_gyif | 已配置数据中获取 | 已通过<br>[**ADD VPNINST**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/增加VPN实例（ADD VPNINST）_09653755.md)<br>命令配置。 |
| **[ADD DIAMPEERADDR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)** | 主机名称（HOSTNAME） | ocs1<br>ocs4 | 已配置数据中获取 | 已通过<br>**[ADD OCS](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/OCS Diameter连接/OCS Server/增加OCS（ADD OCS）_09896954.md)**<br>命令配置。 |
| **[ADD DIAMPEERADDR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)** | IPv4地址（IPV4ADDRESS） | 10.11.21.1<br>10.11.21.2 | 与对端协商 | - |
| **[ADD DIAMPEERADDR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)** | 端口号（PORT） | 3868 | 全网规划 | - |
| **[ADD DIAMPEERADDR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)** | 地址类型<br>（ADDRTYPE） | IPv4 | 与对端协商 | - |
| **[ADD OCSGROUP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/OCS Diameter连接/OCS Group/增加Ocs组（ADD OCSGROUP）_09896959.md)** | OCS组名称（OCSGRPNAME） | og-test1<br>og-test2 | 本端规划 | - |
| **[ADD OCSBINDING](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/OCS Diameter连接/OCS绑定OCS Group/增加Ocs绑定关系（ADD OCSBINDING）_09896963.md)** | OCS组名称（OCSGRPNAME） | og-test1<br>og-test2 | 已配置数据中获取 | 已通过<br>**[ADD OCSGROUP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/OCS Diameter连接/OCS Group/增加Ocs组（ADD OCSGROUP）_09896959.md)**<br>命令配置 |
| **[ADD OCSBINDING](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/OCS Diameter连接/OCS绑定OCS Group/增加Ocs绑定关系（ADD OCSBINDING）_09896963.md)** | OCS主机名称（OCSHOSTNAME） | ocs1<br>ocs4 | 已配置数据中获取 | 已通过<br>**[ADD OCS](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/OCS Diameter连接/OCS Server/增加OCS（ADD OCS）_09896954.md)**<br>命令配置。 |

*表5 对接数据*

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| **[ADD DIAMLOCINFO](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter本端信息/增加Diameter本端信息（ADD DIAMLOCINFO）_09897271.md)** | 本端主机名（HOSTNAME） | unc_1 | 全网规划 | 配置设备信息。 |
| **[ADD DIAMLOCINFO](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter本端信息/增加Diameter本端信息（ADD DIAMLOCINFO）_09897271.md)** | 本端域名（REALMNAME） | example1.com | 与对端协商 | 配置设备信息。 |
| **[ADD DIAMLOCINFO](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter本端信息/增加Diameter本端信息（ADD DIAMLOCINFO）_09897271.md)** | 产品名称（PRODUCTNAME） | unc | 本端规划 | 配置设备信息。 |
| **[ADD DIAMCONNGRP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md)** | Diameter链路组名（CONNGROUPNAME） | dconn_dra1<br>dconn_dra2 | 本端规划 | 配置链路组信息。 |
| **[ADD DIAMCONNGRP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md)** | 本端主机名（LOCALHOSTNAME） | unc_1 | 全网规划 | 配置链路组信息。 |
| **[ADD DIAMCONNGRP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md)** | 对端主机名（PEERHOSTNAME） | host1.example.com<br>host2.example.com | 全网规划 | 配置链路组信息。 |
| **[ADD DIAMCONNGRP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md)** | Diameter应用（APPLICATION） | GY | 全网规划 | 配置链路组信息。 |
| **[ADD DIAMCONNGRP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md)** | 链路选择模式（SELECTMODE） | MASTER_SLAVE | 全网规划 | 配置链路组信息。 |
| **[ADD DIAMCONNECTION](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md)** | Diameter链路组名（CONNGROUPNAME） | dconn_dra1<br>dconn_dra2 | 本端规划 | 配置链路信息、端口。 |
| **[ADD DIAMCONNECTION](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md)** | 本端接口名（LOCINTERFACE） | gyif1/0/0<br>gyif1/0/1 | 本端规划 | 配置链路信息、端口。 |
| **[ADD DIAMCONNECTION](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md)** | 本端端口（LOCALPORT） | 13201<br>13202 | 本端规划 | “13201”对应gyif1/0/0接口的端口号，“13202”对应gyif1/0/1接口的端口号。 |
| **[ADD DIAMRTREALM](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/路由管理/Diameter路由/增加Diameter路由域名信息（ADD DIAMRTREALM）_09897303.md)** | Diameter域名名称（REALMNAME） | ocs.huawei.com | 与对端协商 | - |
| **[ADD DIAMRTREALM](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/路由管理/Diameter路由/增加Diameter路由域名信息（ADD DIAMRTREALM）_09897303.md)** | Diameter应用（APPLICATION） | GY | 全网规划 | - |
| **[ADD DIAMRTREALM](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/路由管理/Diameter路由/增加Diameter路由域名信息（ADD DIAMRTREALM）_09897303.md)** | 路由选择模式（SELECTMODE） | MASTER_SLAVE | 全网规划 | - |
| **[ADD DIAMRTNEXTHOP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/路由管理/Diameter路由配置/增加Diameter路由下一跳（ADD DIAMRTNEXTHOP）_09897310.md)** | Diameter域名名称（REALMNAME） | ocs.huawei.com | 与对端协商 | 说明：下一跳的主机名<br>“HOSTNAME”<br>只允许设置成已配置的DRA主机名。 |
| **[ADD DIAMRTNEXTHOP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/路由管理/Diameter路由配置/增加Diameter路由下一跳（ADD DIAMRTNEXTHOP）_09897310.md)** | Diameter应用（APPLICATION） | GY | 全网规划 | 说明：下一跳的主机名<br>“HOSTNAME”<br>只允许设置成已配置的DRA主机名。 |
| **[ADD DIAMRTNEXTHOP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/路由管理/Diameter路由配置/增加Diameter路由下一跳（ADD DIAMRTNEXTHOP）_09897310.md)** | 下一跳（NEXTHOP） | host1.example.com<br>host2.example.com | 已配置数据中获取 | 说明：下一跳的主机名<br>“HOSTNAME”<br>只允许设置成已配置的DRA主机名。 |
| **[ADD DIAMRTNEXTHOP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/路由管理/Diameter路由配置/增加Diameter路由下一跳（ADD DIAMRTNEXTHOP）_09897310.md)** | 序号（SEQUENCE） | 1<br>2 | 本端规划 | 说明：下一跳的主机名<br>“HOSTNAME”<br>只允许设置成已配置的DRA主机名。 |
| **[ADD REALMBINDAPN](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter Realm/Realm绑定APN/增加APN与Diameter Realm关联关系（ADD REALMBINDAPN）_09897285.md)** | APN名称(APN) | apn-test | 全网规划 | 已通过命令<br>[**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)<br>进行配置，可以使用命令<br>**[LST APN](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/查询APN配置（LST APN）_09652599.md)**<br>查询。 |
| **[ADD REALMBINDAPN](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter Realm/Realm绑定APN/增加APN与Diameter Realm关联关系（ADD REALMBINDAPN）_09897285.md)** | Diameter应用（APPLICATION） | GY | 与对端协商 | 已通过命令<br>[**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)<br>进行配置，可以使用命令<br>**[LST APN](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/查询APN配置（LST APN）_09652599.md)**<br>查询。 |
| **[ADD REALMBINDAPN](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter Realm/Realm绑定APN/增加APN与Diameter Realm关联关系（ADD REALMBINDAPN）_09897285.md)** | Realm名（REALMNAME） | ocs.huawei.com | 全网规划 | 已通过命令<br>[**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)<br>进行配置，可以使用命令<br>**[LST APN](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/查询APN配置（LST APN）_09652599.md)**<br>查询。 |
| **[ADD REALMBINDAPN](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter Realm/Realm绑定APN/增加APN与Diameter Realm关联关系（ADD REALMBINDAPN）_09897285.md)** | 根据IMSI构造归属地Realm开关(CONSTBYIMSISW) | DISABLE | 全网规划 | 已通过命令<br>[**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)<br>进行配置，可以使用命令<br>**[LST APN](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/查询APN配置（LST APN）_09652599.md)**<br>查询。 |

## [操作步骤](#ZH-CN_OPI_0229725460)

1. 参考 [静态路由+BFD组网](../../../../初始配置/UNC初始配置与调测/组网路由配置/配置VNF侧IP路由数据（非SDN）/自动部署（推荐）/配置静态路由+BFD组网（IPv4）_75096861.md) 配置对应的组网。
2. 进入 “MML命令行-UNC” 窗口。
3. 创建一个VPN实例。
  [**ADD VPNINST**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/增加VPN实例（ADD VPNINST）_09653755.md)
4. **可选：**配置Gy接口Diameter应用集中点模式。缺省情况下，本端的端口号不可配，使用系统自动分配的端口号。
  **[SET CONCENPOINT](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/基础参数/集中点模式/设置集中点部署模式（SET CONCENPOINT）_09896704.md)**
  > **说明**
  > - LOCALIP_PEER模式下，ADD DIAMCONNECTION命令添加的链路，仅LocalPort参数未配置或配置为0的链路生效。LocalPort参数配置为非0的链路，允许配置下发，但是不会建链。
  > - LOCALPORT模式下，ADD DIAMCONNECTION命令添加的链路，仅LocalPort参数配置为非0的链路生效。LocalPort参数未配置或配置为0的链路，允许配置下发，但是不会建链。
5. 配置Gy逻辑接口。
  [**ADD LOGICIP**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/IP管理/IP配置/增加逻辑IP地址（ADD LOGICIP）_09587376.md)
  **[ADD LOGICINF](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)**
6. 配置GGSN/PGW-C的设备标识信息。
  **[ADD DIAMLOCINFO](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter本端信息/增加Diameter本端信息（ADD DIAMLOCINFO）_09897271.md)**
7. **可选：**配置直连OCS相关信息。
  > **说明**
  > 请参考如下步骤配置OCS相关信息，这里仅给出关键配置，GGSN/PGW-C与OCS的详细配置请参见 [WSFD-011206 支持融合计费](../../计费管理功能/WSFD-011206 支持融合计费_62745898.md) 的Gy/Diameter在线计费章节。
    a. 配置OCS的设备标识。
      **[ADD OCS](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/OCS Diameter连接/OCS Server/增加OCS（ADD OCS）_09896954.md)**
    b. 配置OCS服务器组。
      **[ADD OCSGROUP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/OCS Diameter连接/OCS Group/增加Ocs组（ADD OCSGROUP）_09896959.md)**
    c. **可选：** 配置DCC模板以及主从OCS组。
      **[ADD DCCTEMPLATE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/信用控制/信用控制模板/增加DCC模板（ADD DCCTEMPLATE）_09896923.md)**
8. 配置DRA相关信息。
    a. **可选：**配置SCTP端点信息。
      **[ADD SCTPENDPOINT](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/SCTP管理/SCTP端点/增加SCTP端点（ADD SCTPENDPOINT）_09897321.md)**
    b. **可选：**使能Realm-based Routing。
      > **说明**
      > GGSN/PGW-C 与OCS之间有直连路径时，需要通过该命令配置是否允许携带Destination-Host AVP的消息通过Diameter路由发送。
      **[SET DIAMETERPARA](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/路由控制/Diameter路由控制/设置Diameter参数（SET DIAMETERPARA）_09897315.md)**
    c. 配置DRA信息。
          - 配置DRA主机名以及地址信息。
            **[ADD DRA](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/DRA管理/DRA信息/增加DRA（ADD DRA）_09897291.md)**
            **[ADD DIAMPEERADDR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)**
            > **说明**
            > 对于同一个DRA，不允许同时配置IP地址和SCTP端点。
          - 配置到DRA的链路组信息。
            **[ADD DIAMCONNGRP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md)**
          - 配置到DRA的链路。
            **[ADD DIAMCONNECTION](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md)**
            > **说明**
            > 配置链路时如果不选择地址类型，则表示本端接口与对端主机的全部地址建立链接。
            >
            > 当 “Gy集中点模式” 通过 **[SET CONCENPOINT](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/基础参数/集中点模式/设置集中点部署模式（SET CONCENPOINT）_09896704.md)** 命令选择为 “LOCALPORT” 时，可使用 **[ADD DIAMCONNECTION](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md)** 命令设置本端的端口号。
    d. 配置Diameter路由。
      **[ADD DIAMRTREALM](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/路由管理/Diameter路由/增加Diameter路由域名信息（ADD DIAMRTREALM）_09897303.md)**
      **[ADD DIAMRTNEXTHOP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/路由管理/Diameter路由配置/增加Diameter路由下一跳（ADD DIAMRTNEXTHOP）_09897310.md)**
    e. 配置Realm的绑定关系。
      > **说明**
      > 以下两者必配其一，若两者均配置， GGSN/PGW-C 优先选择基于APN的配置。
          - 基于APN配置Realm。
            **[ADD REALMBINDAPN](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter Realm/Realm绑定APN/增加APN与Diameter Realm关联关系（ADD REALMBINDAPN）_09897285.md)**
          - 基于IMSI/MSISDN号段或全局配置Realm。
            **[ADD GLBDIAMREALM](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter Realm/全局Realm/增加全局Diameter域（ADD GLBDIAMREALM）_09897280.md)**

## [任务示例一：Gy over DRA（TCP链路）](#ZH-CN_OPI_0229725460)

任务描述

如 [图1](#ZH-CN_OPI_0229725460__fig14649823145619) 所示，GGSN/PGW-C与OCS之间有直连路径，直连路径不可用的情况下可以通过DRA转交Diameter消息。

- GGSN/PGW-C使用VPN缺省路由与DRA建立起正常的IP连接。
- GGSN/PGW-C与OCS1、OCS4直连。
- GGSN/PGW-C与两个DRA采用TCP协议对接，host分别为host1.example.com、host2.example.com，每个DRA各两个IP地址。GGSN/PGW-C转发Diameter消息时，优先转发OCS1/OCS4，然后选择从DRA转发到OCS。
- GGSN/PGW-C到Realm（ocs.huawei.com）有两条Diameter路由，第一跳指向DRA1（host1.example.com），第二跳指向DRA2（host2.example.com）。
- 基于APN（apn-test）绑定Realm（ocs.huawei.com）。

**图1** Gy over DRA（TCP链路）

<br>

![](激活Gy over DRA（静态路由+BFD组网）_29725460.assets/zh-cn_image_0264087712_2.png)

脚本

1. 参考[静态路由+BFD组网](../../../../初始配置/UNC初始配置与调测/组网路由配置/配置VNF侧IP路由数据（非SDN）/自动部署（推荐）/配置静态路由+BFD组网（IPv4）_75096861.md)配置对应的组网。
2. 配置本端数据。
  //创建一个VPN实例。
  ```
  ADD VPNINST:VPNINSTANCE="vpn_gyif";
  ```
  //配置Gy接口Diamteter应用集中点模式。
  ```
  SET CONCENPOINT:GYCONCENMODE=LOCALPORT;
  ```
  //配置Gy逻辑接口。

  ```
  ADD LOGICIP: IPVERSION=IPv4, LOGICIPV4="10.8.10.1";
  ADD LOGICIP: IPVERSION=IPv4, LOGICIPV4="10.8.10.4";
  ADD LOGICINF:NAME="gyif1/0/0",IPVERSION=IPV4,IPV4ADDRESS1="10.8.10.1",IPV4MASK1="255.255.255.255",IPV4ADDRESS2="10.8.11.4",IPV4MASK2="255.255.255.255",VPNINSTANCE="vpn_gyif";
  ```

  ```
  ADD LOGICIP: IPVERSION=IPv4, LOGICIPV4="10.8.10.2";
  ADD LOGICIP: IPVERSION=IPv4, LOGICIPV4="10.8.10.5";
  ADD LOGICINF:NAME="gyif1/0/1",IPVERSION=IPV4,IPV4ADDRESS1="10.8.10.2",IPV4MASK1="255.255.255.255",IPV4ADDRESS2="10.8.10.5",IPV4MASK2="255.255.255.255",VPNINSTANCE="vpn_gyif";
  ```
3. 配置直连OCS相关信息。
  ```
  ADD OCS:OCSHOSTNAME="ocs1",REALMNAME="ocs.huawei.com",VPNINSTANCE="vpn_gyif";
  ```
  ```
  ADD OCS:OCSHOSTNAME="ocs4",REALMNAME="ocs.huawei.com",VPNINSTANCE="vpn_gyif";
  ```
  ```
  ADD DIAMPEERADDR:HOSTNAME="ocs1",ADDRTYPE=IPv4,IPV4ADDRESS="10.11.21.1",PORT=3868;
  ```
  ```
  ADD DIAMPEERADDR:HOSTNAME="ocs4",ADDRTYPE=IPv4,IPV4ADDRESS="10.11.21.2",PORT=3868;
  ```
  ```
  ADD OCSGROUP:OCSGRPNAME="og-test1";
  ```
  ```
  ADD OCSGROUP:OCSGRPNAME="og-test2";
  ```
  ```
  ADD OCSBINDING:OCSGRPNAME="og-test1",OCSHOSTNAME="ocs1";
  ```
  ```
  ADD OCSBINDING:OCSGRPNAME="og-test2",OCSHOSTNAME="ocs4";
  ```
4. 配置DRA数据。
  //使能Realm-Based Routing。
  ```
  SET DIAMETERPARA:REALMBASEROUTE=ENABLE;
  ```
  //配置DRA主机名以及地址信息。
  ```
  ADD DRA:HOSTNAME="host1.example.com",VPNINSTANCE="vpn_gyif";
  ```
  ```
  ADD DRA:HOSTNAME="host2.example.com",VPNINSTANCE="vpn_gyif";
  ```
  ```
  ADD DIAMPEERADDR:HOSTNAME="host1.example.com",ADDRTYPE=IPv4,IPV4ADDRESS="10.10.10.1",PORT=3396;
  ```
  ```
  ADD DIAMPEERADDR:HOSTNAME="host1.example.com",ADDRTYPE=IPv4,IPV4ADDRESS="10.10.10.2",PORT=3397;
  ```
  ```
  ADD DIAMPEERADDR:HOSTNAME="host2.example.com",ADDRTYPE=IPv4,IPV4ADDRESS="10.10.11.1",PORT=3396;
  ```
  ```
  ADD DIAMPEERADDR:HOSTNAME="host2.example.com",ADDRTYPE=IPv4,IPV4ADDRESS="10.10.11.2",PORT=3397;
  ```
5. 配置对接数据。
  //配置GGSN/PGW-C的设备标识。
  ```
  ADD DIAMLOCINFO:HOSTNAME="unc_1",REALMNAME="example1.com",PRODUCTNAME="unc";
  ```
  //配置网元对接。
  ```
  ADD DIAMCONNGRP:CONNGROUPNAME="dconn_dra1",LOCALHOSTNAME="unc_1",APPLICATION=GY,PEERHOSTNAME="host1.example.com",SELECTMODE=MASTER_SLAVE;
  ADD DIAMCONNGRP:CONNGROUPNAME="dconn_dra2",LOCALHOSTNAME="unc_1",APPLICATION=GY,PEERHOSTNAME="host2.example.com",SELECTMODE=MASTER_SLAVE;
  ADD DIAMCONNECTION:DIAMCONNGRP="dconn_dra1",LOCINTERFACE="gyif1/0/0",LOCALPORT=13201;
  ADD DIAMCONNECTION:DIAMCONNGRP="dconn_dra2",LOCINTERFACE="gyif1/0/1",LOCALPORT=13202;
  ADD DIAMRTREALM:REALMNAME="ocs.huawei.com",APPLICATION=GY,SELECTMODE=MASTER_SLAVE;
  ADD DIAMRTNEXTHOP:REALMNAME="ocs.huawei.com",APPLICATION=GY,NEXTHOP="host1.example.com",SEQUENCE=1;
  ADD APN:APN="apn-test";
  ADD DIAMRTNEXTHOP:REALMNAME="ocs.huawei.com",APPLICATION=GY,NEXTHOP="host2.example.com",SEQUENCE=2;
  ADD APN:APN="apn-test";
  ADD REALMBINDAPN:APN="apn-test",APPLICATION=GY,CONSTBYIMSISW=DISABLE,REALMNAME="ocs.huawei.com";
  ```

## [任务示例二：Gy over DRA（SCTP链路）](#ZH-CN_OPI_0229725460)

任务描述

如 [图2](#ZH-CN_OPI_0229725460__fig3) 所示，GGSN/PGW-C与OCS之间有直连路径，直连路径不可用的情况下可以通过DRA转交Diameter消息。

- GGSN/PGW-C使用VPN缺省路由与DRA建立起正常的IP连接。
- GGSN/PGW-C与两个DRA采用SCTP协议对接，host分别为host1.example.com、host2.example.com，每个DRA各两个IP地址。GGSN/PGW-C转发Diameter消息时，优先转发OCS1/OCS4，然后选择从DRA转发到OCS。
- GGSN/PGW-C到Realm（ocs.huawei.com）有两条Diameter路由，第一跳指向DRA1（host1.example.com），第二跳指向DRA2（host2.example.com）。
- 基于APN（apn-test）绑定Realm（ocs.huawei.com）。

**图2** Gy over DRA（SCTP链路）

<br>

![](激活Gy over DRA（静态路由+BFD组网）_29725460.assets/zh-cn_image_0264087710_2.png)

脚本

脚本

1. 参考[静态路由+BFD组网](../../../../初始配置/UNC初始配置与调测/组网路由配置/配置VNF侧IP路由数据（非SDN）/自动部署（推荐）/配置静态路由+BFD组网（IPv4）_75096861.md)配置对应的组网。
2. 配置本端数据。
  //创建一个VPN实例。
  ```
  ADD VPNINST:VPNINSTANCE="vpn_gyif";
  ```
  //配置Gy接口Diamteter应用集中点模式。
  ```
  SET CONCENPOINT:GYCONCENMODE=LOCALPORT;
  ```
  //配置Gy逻辑接口。

  ```
  ADD LOGICINF:NAME="gyif1/0/0",IPVERSION=IPV4,IPV4ADDRESS1="10.8.10.1",IPV4MASK1="255.255.255.255",IPV4ADDRESS2="10.8.10.4",IPV4MASK2="255.255.255.255",VPNINSTANCE="vpn_gyif";
  ```

  ```
  ADD LOGICINF:NAME="gyif1/0/1",IPVERSION=IPV4,IPV4ADDRESS1="10.8.10.2",IPV4MASK1="255.255.255.255",IPV4ADDRESS2="10.8.10.5",IPV4MASK2="255.255.255.255",VPNINSTANCE="vpn_gyif";
  ```
3. 配置DRA数据。
  //使能Realm-Based Routing。
  ```
  SET DIAMETERPARA:REALMBASEROUTE=ENABLE;
  ```
  //配置SCTP端点信息。
  ```
  ADD SCTPENDPOINT:ENDPOINTNAME="endpoint0",IPVERSION=IPV4,IPV4ADDRESS1="10.11.21.59",IPV4ADDRESS2="10.11.21.60",PORT=3868;
  ```
  ```
  ADD SCTPENDPOINT:ENDPOINTNAME="endpoint1",IPVERSION=IPV4,IPV4ADDRESS1="10.11.21.11",IPV4ADDRESS2="10.11.21.12",PORT=3868;
  ```
  ```
  ADD SCTPENDPOINT:ENDPOINTNAME="endpoint2",IPVERSION=IPV4,IPV4ADDRESS1="10.11.22.59",IPV4ADDRESS2="10.11.22.60",PORT=3868;
  ```
  ```
  ADD SCTPENDPOINT:ENDPOINTNAME="endpoint3",IPVERSION=IPV4,IPV4ADDRESS1="10.11.22.11",IPV4ADDRESS2="10.11.22.12",PORT=3868;
  ```
  //配置DRA主机名以及地址信息。
  ```
  ADD DRA:HOSTNAME="host1.example.com",VPNINSTANCE="vpn_gyif";
  ```
  ```
  ADD DRA:HOSTNAME="host2.example.com",VPNINSTANCE="vpn_gyif";
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
  ADD DIAMCONNGRP:CONNGROUPNAME="dconn_dra1",LOCALHOSTNAME="unc_1",APPLICATION=GY,PEERHOSTNAME="host1.example.com",SELECTMODE=MASTER_SLAVE;
  ADD DIAMCONNGRP:CONNGROUPNAME="dconn_dra2",LOCALHOSTNAME="unc_1",APPLICATION=GY,PEERHOSTNAME="host2.example.com",SELECTMODE=MASTER_SLAVE;
  ADD DIAMCONNECTION:DIAMCONNGRP="dconn_dra1",LOCINTERFACE="gyif1/0/0",LOCALPORT=13201;
  ADD DIAMCONNECTION:DIAMCONNGRP="dconn_dra2",LOCINTERFACE="gyif1/0/1",LOCALPORT=13202;
  ADD DIAMRTREALM:REALMNAME="ocs.huawei.com",APPLICATION=GY,SELECTMODE=MASTER_SLAVE;
  ADD DIAMRTNEXTHOP:REALMNAME="ocs.huawei.com",APPLICATION=GY,NEXTHOP="host1.example.com",SEQUENCE=1;
  ADD APN:APN="apn-test";
  ADD DIAMRTNEXTHOP:REALMNAME="ocs.huawei.com",APPLICATION=GY,NEXTHOP="host2.example.com",SEQUENCE=2;
  ADD APN:APN="apn-test";
  ADD REALMBINDAPN:APN="apn-test",APPLICATION=GY,CONSTBYIMSISW=DISABLE,REALMNAME="ocs.huawei.com";
  ```
