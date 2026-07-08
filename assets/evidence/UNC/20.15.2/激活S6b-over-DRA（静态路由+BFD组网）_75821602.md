# 激活S6b over DRA（静态路由+BFD组网）

- [操作场景](#ZH-CN_OPI_0275821602__1.3.1)
- [必备事项](#ZH-CN_OPI_0275821602__1.3.2)
- [操作步骤](#ZH-CN_OPI_0275821602__1.3.3)
- [任务示例一：S6b over DRA（TCP链路）](#ZH-CN_OPI_0275821602__1.3.4)
- [任务示例二：S6b over DRA（SCTP链路）](#ZH-CN_OPI_0275821602__1.3.5)

## [操作场景](#ZH-CN_OPI_0275821602)

当 GGSN/PGW-C 与3GPP AAA之间直连路径故障或者未配置直连路径时，可以激活S6b over DRA功能，DRA在 GGSN/PGW-C 与3GPP AAA间转交消息，提供3GPP AAA服务器寻址功能。

> **说明**
> 适用于 GGSN、 PGW-C。

## [必备事项](#ZH-CN_OPI_0275821602)

前提条件

- 请仔细阅读 [WSFD-011134 S6b over DRA](../WSFD-011134 S6b over DRA_75821599.md) 。
- 如果运营商规划采用VPN组网方式，则操作员在执行本操作前应已创建了相应的VPN实例。
- 提前进行S6b接口信令组网规划，获取DRA以及3GPP AAA所属Realm等配置信息。

数据

*表1 本端数据*

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| [**ADD VPNINST**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/增加VPN实例（ADD VPNINST）_09653755.md) | VPN实例名（VPNINSTANCE） | vpn_s6bif | 本端规划 | - |
| [**SET CONCENPOINT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/基础参数/集中点模式/设置集中点部署模式（SET CONCENPOINT）_09896704.md) | S6b集中点模式（S6BCONCENMODE） | LOCALPORT | 本端规划 | - |
| [**ADD LOGICINF**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md) | VPN实例名称（VPNINSTANCE） | vpn_s6bif | 已配置数据中获取 | 接口绑定的VPN实例已通过<br>[**ADD VPNINST**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/增加VPN实例（ADD VPNINST）_09653755.md)<br>命令配置，可以使用<br>[**LST VPNINST**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/查询VPN实例（LST VPNINST）_09651519.md)<br>命令进行查询。 |
| [**ADD LOGICINF**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md) | 逻辑接口名称（NAME） | s6bif1/0/0<br>s6bif1/0/1 | 全网规划 | 逻辑接口的IP掩码只能为255.255.255.255，或掩码长度32。 |
| [**ADD LOGICINF**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md) | 逻辑接口的IP版本（IPVERSION） | IPv4 | 本端规划 | 逻辑接口的IP掩码只能为255.255.255.255，或掩码长度32。 |
| [**ADD LOGICINF**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md) | 逻辑接口的IPv4地址1(IPV4ADDRESS1) | 10.8.10.1<br>10.8.10.4 | 全网规划 | 逻辑接口的IP掩码只能为255.255.255.255，或掩码长度32。 |
| [**ADD LOGICINF**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md) | 逻辑接口的IPv4掩码1(IPV4MASK1) | 255.255.255.255 | 固定取值 | 逻辑接口的IP掩码只能为255.255.255.255，或掩码长度32。 |
| [**ADD LOGICINF**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md) | 逻辑接口的IPv4地址2(IPV4ADDRESS2) | 10.8.10.2<br>10.8.10.5 | 全网规划 | 逻辑接口的IP掩码只能为255.255.255.255，或掩码长度32。 |
| [**ADD LOGICINF**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md) | 逻辑接口的IPv4掩码2(IPV4MASK2) | 255.255.255.255 | 固定取值 | 逻辑接口的IP掩码只能为255.255.255.255，或掩码长度32。 |

*表2 对端DRA数据（TCP）*

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| **[SET DIAMETERPARA](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/路由控制/Diameter路由控制/设置Diameter参数（SET DIAMETERPARA）_09897315.md)** | 基于域名的路由功能开关（REALMBASEROUTE） | ENABLE | 本端规划 | - |
| **[ADD DRA](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/DRA管理/DRA信息/增加DRA（ADD DRA）_09897291.md)** | 主机名（HOSTNAME） | host1.example.com<br>host2.example.com | 与对端协商 | - |
| **[ADD DRA](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/DRA管理/DRA信息/增加DRA（ADD DRA）_09897291.md)** | VPN实例（VPNINSTANCE） | vpn_gyif | 已配置数据中获取 | - |
| **[ADD DIAMPEERADDR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)** | 地址类型（ADDRTYPE） | IPv4 | 与对端协商 | - |
| **[ADD DIAMPEERADDR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)** | IPv4地址（IPV4ADDRESS） | 10.10.10.1<br>10.10.10.2<br>10.10.11.1<br>10.10.11.2 | 对端获取 | - |

*表3 对端DRA数据（SCTP）*

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| [**ADD SCTPENDPOINT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/SCTP管理/SCTP端点/增加SCTP端点（ADD SCTPENDPOINT）_09897321.md) | 端点名称（ENDPOINTNAME） | endpoint0<br>endpoint1<br>endpoint2<br>endpoint3 | 本端规划 | 对端端点的IP地址和端口号。对端端点各有两个IP地址，分别如下。<br>- 10.11.21.59和10.11.21.60<br>- 10.11.21.11和10.11.21.12<br>- 10.11.22.59和10.11.22.60<br>- 10.11.22.11和10.11.22.12 |
| [**ADD SCTPENDPOINT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/SCTP管理/SCTP端点/增加SCTP端点（ADD SCTPENDPOINT）_09897321.md) | IPV4地址1 | 10.11.21.59<br>10.11.21.11<br>10.11.22.59<br>10.11.22.11 | 与对端协商 | 对端端点的IP地址和端口号。对端端点各有两个IP地址，分别如下。<br>- 10.11.21.59和10.11.21.60<br>- 10.11.21.11和10.11.21.12<br>- 10.11.22.59和10.11.22.60<br>- 10.11.22.11和10.11.22.12 |
| [**ADD SCTPENDPOINT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/SCTP管理/SCTP端点/增加SCTP端点（ADD SCTPENDPOINT）_09897321.md) | IPv4地址2（IPV4ADDRESS2） | 10.11.21.60<br>10.11.21.12<br>10.11.22.60<br>10.11.22.12 | 全网规划 | 对端端点的IP地址和端口号。对端端点各有两个IP地址，分别如下。<br>- 10.11.21.59和10.11.21.60<br>- 10.11.21.11和10.11.21.12<br>- 10.11.22.59和10.11.22.60<br>- 10.11.22.11和10.11.22.12 |
| [**ADD SCTPENDPOINT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/SCTP管理/SCTP端点/增加SCTP端点（ADD SCTPENDPOINT）_09897321.md) | 端口号（PORT） | 3868 | 全网规划 | 对端端点的IP地址和端口号。对端端点各有两个IP地址，分别如下。<br>- 10.11.21.59和10.11.21.60<br>- 10.11.21.11和10.11.21.12<br>- 10.11.22.59和10.11.22.60<br>- 10.11.22.11和10.11.22.12 |
| [**SET DIAMETERPARA**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/路由控制/Diameter路由控制/设置Diameter参数（SET DIAMETERPARA）_09897315.md) | 基于域名的路由功能开关（REALMBASEROUTE） | ENABLE | 本端规划 | - |
| **[ADD DRA](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/DRA管理/DRA信息/增加DRA（ADD DRA）_09897291.md)** | 主机名（HOSTNAME） | host1.example.com<br>host2.example.com | 本端规划 | - |
| **[ADD DRA](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/DRA管理/DRA信息/增加DRA（ADD DRA）_09897291.md)** | VPN实例（VPNINSTANCE） | vpn_s6bif | 已配置数据中获取 | - |
| **[ADD DIAMPEERADDR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)** | 地址类型（ADDRTYPE） | SCTP | 与对端协商 | - |
| **[ADD DIAMPEERADDR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)** | SCTP端点名称（SCTPENDPOINT） | endpoint0<br>endpoint1<br>endpoint2<br>endpoint3 | 与对端协商 | DRA绑定的SCTP端点已经通过<br>[**ADD SCTPENDPOINT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/SCTP管理/SCTP端点/增加SCTP端点（ADD SCTPENDPOINT）_09897321.md)<br>命令配置，可以使用<br>[**LST SCTPENDPOINT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/SCTP管理/SCTP端点/查询SCTP端点（LST SCTPENDPOINT）_09897324.md)<br>命令查询。 |

*表4 对接数据*

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| [**ADD DIAMLOCINFO**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter本端信息/增加Diameter本端信息（ADD DIAMLOCINFO）_09897271.md) | 本端主机名（HOSTNAME） | pgw_1<br>pgw_2 | 本端规划 | - |
| [**ADD DIAMLOCINFO**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter本端信息/增加Diameter本端信息（ADD DIAMLOCINFO）_09897271.md) | 本端域名（REALMNAME） | example1.com | 与对端协商 | - |
| [**ADD DIAMLOCINFO**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter本端信息/增加Diameter本端信息（ADD DIAMLOCINFO）_09897271.md) | 产品名称（PRODUCTNAME） | unc | 本端规划 | - |
| [**ADD DIAMCONNGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md) | Diameter链路组名（CONNGROUPNAME） | dconn_s6b1<br>dconn_s6b2 | 本端规划 | - |
| [**ADD DIAMCONNGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md) | 本端主机名（LOCALHOSTNAME） | pgw_1<br>pgw_2 | 全网规划 | - |
| [**ADD DIAMCONNGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md) | 对端主机名（PEERHOSTNAME） | host1.example.com<br>host2.example.com | 全网规划 | - |
| [**ADD DIAMCONNGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md) | Diameter应用（APPLICATION） | S6B | 全网规划 | - |
| [**ADD DIAMCONNGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md) | 链路选择模式（SELECTMODE） | SESSION_ID | 全网规划 | - |
| [**ADD DIAMCONNECTION**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md) | Diameter链路组名 | dconn_s6b1<br>dconn_s6b2 | 本端规划 | - |
| [**ADD DIAMCONNECTION**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md) | 本端接口名（LOCINTERFACE） | s6bif1/0/0<br>s6bif1/0/1 | 本端规划 | - |
| [**ADD DIAMCONNECTION**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md) | 本端端口号（LOCALPORT） | 19766<br>19767 | 本端规划 | - |
| [**ADD DIAMRTREALM**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/路由管理/Diameter路由/增加Diameter路由域名信息（ADD DIAMRTREALM）_09897303.md) | Diameter域名名称（REALMNAME） | 3gppaaa.huawei.com | 与对端协商 | - |
| [**ADD DIAMRTREALM**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/路由管理/Diameter路由/增加Diameter路由域名信息（ADD DIAMRTREALM）_09897303.md) | Diameter应用（APPLICATION） | S6B | 全网规划 | - |
| [**ADD DIAMRTREALM**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/路由管理/Diameter路由/增加Diameter路由域名信息（ADD DIAMRTREALM）_09897303.md) | 路由选择模式（SELECTMODE） | MASTER_SLAVE | 全网规划 | - |
| [**ADD DIAMRTNEXTHOP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/路由管理/Diameter路由配置/增加Diameter路由下一跳（ADD DIAMRTNEXTHOP）_09897310.md) | Diameter域名名称（REALMNAME） | 3gppaaa.huawei.com | 与对端协商 | 说明：下一跳的主机名<br>“HOSTNAME”<br>只允许设置成已配置的DRA主机名。 |
| [**ADD DIAMRTNEXTHOP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/路由管理/Diameter路由配置/增加Diameter路由下一跳（ADD DIAMRTNEXTHOP）_09897310.md) | Diameter应用（APPLICATION） | S6B | 全网规划 | 说明：下一跳的主机名<br>“HOSTNAME”<br>只允许设置成已配置的DRA主机名。 |
| [**ADD DIAMRTNEXTHOP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/路由管理/Diameter路由配置/增加Diameter路由下一跳（ADD DIAMRTNEXTHOP）_09897310.md) | 下一跳（NEXTHOP） | host1.example.com<br>host2.example.com | 已配置数据中获取 | 说明：下一跳的主机名<br>“HOSTNAME”<br>只允许设置成已配置的DRA主机名。 |
| [**ADD DIAMRTNEXTHOP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/路由管理/Diameter路由配置/增加Diameter路由下一跳（ADD DIAMRTNEXTHOP）_09897310.md) | 序号（SEQUENCE） | 1<br>2 | 本端规划 | 说明：下一跳的主机名<br>“HOSTNAME”<br>只允许设置成已配置的DRA主机名。 |
| [**ADD REALMBINDAPN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter Realm/Realm绑定APN/增加APN与Diameter Realm关联关系（ADD REALMBINDAPN）_09897285.md) | APN名称（APN） | ims | 全网规划 | - |
| [**ADD REALMBINDAPN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter Realm/Realm绑定APN/增加APN与Diameter Realm关联关系（ADD REALMBINDAPN）_09897285.md) | Diameter应用（APPLICATION） | S6B | 与对端协商 | - |
| [**ADD REALMBINDAPN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter Realm/Realm绑定APN/增加APN与Diameter Realm关联关系（ADD REALMBINDAPN）_09897285.md) | 根据IMSI构造归属地Realm开关（CONSTBYIMSISW） | DISABLE | 全网规划 | - |
| [**ADD REALMBINDAPN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter Realm/Realm绑定APN/增加APN与Diameter Realm关联关系（ADD REALMBINDAPN）_09897285.md) | Realm名（REALMNAME） | 3gppaaa.huawei.com | 全网规划 | - |

## [操作步骤](#ZH-CN_OPI_0275821602)

1. 参考 [配置静态路由+BFD组网（IPv4）](../../../../初始配置/UNC初始配置与调测/组网路由配置/配置VNF侧IP路由数据（非SDN）/自动部署（推荐）/配置静态路由+BFD组网（IPv4）_75096861.md) 配置对应的组网。
2. 进入 “MML命令行-UNC” 窗口。
3. 创建一个VPN实例。
  [**ADD VPNINST**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/增加VPN实例（ADD VPNINST）_09653755.md)
4. **可选：**配置S6b接口Diameter应用集中点模式。缺省情况下，本端的端口号不可配，使用系统自动分配的端口号。
  [**SET CONCENPOINT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/基础参数/集中点模式/设置集中点部署模式（SET CONCENPOINT）_09896704.md)
  > **说明**
  > - LOCALIP_PEER模式下，ADD DIAMCONNECTION命令添加的链路，仅LocalPort参数未配置或配置为0的链路生效。LocalPort参数配置为非0的链路，允许配置下发，但是不会建链。
  > - LOCALPORT模式下，ADD DIAMCONNECTION命令添加的链路，仅LocalPort参数配置为非0的链路生效。LocalPort参数未配置或配置为0的链路，允许配置下发，但是不会建链。
5. 配置S6b逻辑接口。
  [**ADD LOGICINF**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)
6. 配置GGSN/PGW-C的设备标识。
  [**ADD DIAMLOCINFO**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter本端信息/增加Diameter本端信息（ADD DIAMLOCINFO）_09897271.md)
7. 配置3GPP AAA相关信息。
  > **说明**
  > - 当需要配置PGW-C向Diameter AAA请求授权时携带P-GW的IP地址时，需配置本步骤。
  > - 注意，AMF发现SMF仅支持FQDN方式，AMF无法通过配置的P-GW的IP发现SMF。
    a. 配置3GPP AAA Server服务器组。
      [**ADD DIAMAAAGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/Diameter AAA管理/服务器配置/Diameter AAA组/增加Diameter AAA服务器组（ADD DIAMAAAGRP）_64343820.md)
      > **说明**
      > - 如果不需要支持VoWifi切换到VoNR，则“PGWIDENTITY”参数配置为“IP（P-GW IP地址）”或“HOST_NAME（P-GW主机名）”即IP或FQDN方式均可以；
      > - 如果需要VoWifi支持切换到VoNR，则“PGWIDENTITY”参数需要配置为FQDN方式，因为AMF不支持IP方式服务发现SMF。
      > - 当“PGWIDENTITY”参数配置为FQDN方式时，那么需要继续配置步骤[8](#ZH-CN_OPI_0275821602__step1666818212525)。
    b. 将3GPP AAA Server服务器组绑定到APN实例。
      [**ADD APNDIAMAAAGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/Diameter AAA管理/服务器配置/APN的Diameter AAA组/增加APN的Diameter AAA服务器组（ADD APNDIAMAAAGRP）_64343817.md)
8. **可选：**增加逻辑接口的PGW-C主机名。
  **[ADD PGWHOSTNAME](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/Diameter AAA管理/P-GW Host Name配置/P-GW逻辑接口主机名/增加逻辑接口的PGW主机名（ADD PGWHOSTNAME）_64343865.md)**
  > **说明**
  > - 当需要配置PGW-C向Diameter AAA请求授权携带FQDN时，需配置**ADD PGWHOSTNAME**。
  > - **ADD PGWHOSTNAME**命令“PGWHOSTNAME”参数取值需与**ADD SMFINFO**命令的“PGWFQDN”参数值保持一致。
9. 配置DRA相关信息。
    a. 使能Realm-Based Routing。
      [**SET DIAMETERPARA**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/路由控制/Diameter路由控制/设置Diameter参数（SET DIAMETERPARA）_09897315.md)
    b. 配置DRA主机名以及地址信息。
      [**ADD DRA**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/DRA管理/DRA信息/增加DRA（ADD DRA）_09897291.md)
      [**ADD DIAMPEERADDR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)
      > **说明**
      > - 对于同一个DRA，不允许同时配置IP地址和SCTP端点。
      > - DRA与Diameter实体PCRF/OCS/AAA的主机名不能重复。
    c. 配置到DRA的链路组信息。
      [**ADD DIAMCONNGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md)
    d. 配置到DRA的链路。
      [**ADD DIAMCONNECTION**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md)
      > **说明**
      > 配置链路时如果不选择地址类型，则表示本端接口与对端主机的全部地址建立链接。
      >
      > 当 “S6b集中点模式” 通过 [**SET CONCENPOINT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/基础参数/集中点模式/设置集中点部署模式（SET CONCENPOINT）_09896704.md) 命令选择为 “LOCALPORT” 时，可使用 [**ADD DIAMCONNECTION**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md) 命令设置本端的端口号。
    e. 配置Diameter路由。
      [**ADD DIAMRTREALM**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/路由管理/Diameter路由/增加Diameter路由域名信息（ADD DIAMRTREALM）_09897303.md)
      [**ADD DIAMRTNEXTHOP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/路由管理/Diameter路由配置/增加Diameter路由下一跳（ADD DIAMRTNEXTHOP）_09897310.md)
    f. 配置Realm的绑定关系。
      > **说明**
      > 以下两者必配其一，若两者均配置，GGSN/PGW-C优先选择基于APN的配置。
          - 基于APN配置Realm。
            [**ADD REALMBINDAPN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter Realm/Realm绑定APN/增加APN与Diameter Realm关联关系（ADD REALMBINDAPN）_09897285.md)
          - 基于IMSI/MSISDN号段或全局配置Realm。
            [**ADD GLBDIAMREALM**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter Realm/全局Realm/增加全局Diameter域（ADD GLBDIAMREALM）_09897280.md)

## [任务示例一：S6b over DRA（TCP链路）](#ZH-CN_OPI_0275821602)

任务描述

本实例中，将在GGSN/PGW-C上进行数据配置实现以下要求：

- GGSN/PGW-C使用VPN缺省路由与DRA建立起正常的IP连接。
- GGSN/PGW-C与3GPP AAA之间无直连路径，通过DRA进行Diameter消息的转发。
    - GGSN/PGW-C与两个DRA对接，host分别为host1.example.com、host2.example.com，每个DRA各两个IP地址。
    - 两条Diameter路由，第一跳指向DRA1（host1.example.com），第二跳指向DRA2（host2.example.com）。
    - 基于APN（ims）绑定Realm（3gppaaa.huawei.com）。

**图1** S6b over DRA（TCP链路）

<br>

![](激活S6b over DRA（静态路由+BFD组网）_75821602.assets/zh-cn_image_0000002524152690_2.png)

脚本

1. 参考[静态路由+BFD组网](../../../../初始配置/UNC初始配置与调测/组网路由配置/配置VNF侧IP路由数据（非SDN）/自动部署（推荐）/配置静态路由+BFD组网（IPv4）_75096861.md)配置对应的组网。
2. 配置本端数据。
  //创建一个VPN实例。
  ```
  ADD VPNINST:VPNINSTANCE="vpn_s6bif";
  ```
  //配置S6b接口Diameter应用集中点模式。
  ```
  SET CONCENPOINT:S6BCONCENMODE=LOCALPORT;
  ```
  //配置S6b逻辑接口。

  ```
  ADD LOGICINF:NAME="s6bif1/0/0",IPVERSION=IPV4,IPV4ADDRESS1="10.8.10.1",IPV4MASK1="255.255.255.255",IPV4ADDRESS2="10.8.10.2",IPV4MASK2="255.255.255.255",VPNINSTANCE="vpn_s6bif";
  ```

  ```
  ADD LOGICINF:NAME="s6bif1/0/1",IPVERSION=IPV4,IPV4ADDRESS1="10.8.10.4",IPV4MASK1="255.255.255.255",IPV4ADDRESS2="10.8.10.5",IPV4MASK2="255.255.255.255",VPNINSTANCE="vpn_s6bif";
  ```
3. 配置DRA数据。
  //使能Realm-Based Routing。
  ```
  SET DIAMETERPARA:REALMBASEROUTE=ENABLE;
  ```
  //配置DRA主机名以及地址信息。
  ```
  ADD DRA:HOSTNAME="host1.example.com",VPNINSTANCE="vpn_s6bif";
  ```
  ```
  ADD DRA:HOSTNAME="host2.example.com",VPNINSTANCE="vpn_s6bif";
  ```
  ```
  ADD DIAMPEERADDR:HOSTNAME="host1.example.com",ADDRTYPE=IPv4,IPV4ADDRESS="10.10.10.1";
  ```
  ```
  ADD DIAMPEERADDR:HOSTNAME="host1.example.com",ADDRTYPE=IPv4,IPV4ADDRESS="10.10.10.2";
  ```
  ```
  ADD DIAMPEERADDR:HOSTNAME="host2.example.com",ADDRTYPE=IPv4,IPV4ADDRESS="10.10.11.1";
  ```
  ```
  ADD DIAMPEERADDR:HOSTNAME="host2.example.com",ADDRTYPE=IPv4,IPV4ADDRESS="10.10.11.2";
  ```
4. 配置对接数据。
  //配置GGSN/PGW-C的设备标识。
  ```
  ADD DIAMLOCINFO:HOSTNAME="pgw_1",REALMNAME="example1.com",PRODUCTNAME="unc";
  ```
  ```
  ADD DIAMLOCINFO:HOSTNAME="pgw_2",REALMNAME="example1.com",PRODUCTNAME="unc";
  ```
  //配置网元对接。
  ```
  ADD DIAMCONNGRP:CONNGROUPNAME="dconn_s6b1",LOCALHOSTNAME="pgw_1",APPLICATION=S6B,PEERHOSTNAME="host1.example.com";
  ```
  ```
  ADD DIAMCONNGRP:CONNGROUPNAME="dconn_s6b2",LOCALHOSTNAME="pgw_2",APPLICATION=S6B,PEERHOSTNAME="host2.example.com";
  ```
  ```
  ADD DIAMCONNECTION:DIAMCONNGRP="dconn_s6b1",LOCINTERFACE="s6bif1/0/0",LOCALPORT=19766;
  ```
  ```
  ADD DIAMCONNECTION:DIAMCONNGRP="dconn_s6b2",LOCINTERFACE="s6bif1/0/1",LOCALPORT=19767;
  ```
  ```
  ADD DIAMRTREALM:REALMNAME="3gppaaa.huawei.com",APPLICATION=S6B,SELECTMODE=MASTER_SLAVE;
  ```
  ```
  ADD DIAMRTNEXTHOP:REALMNAME="3gppaaa.huawei.com",APPLICATION=S6B,NEXTHOP="host1.example.com",SEQUENCE=1;
  ```
  ```
  ADD DIAMRTNEXTHOP:REALMNAME="3gppaaa.huawei.com",APPLICATION=S6B,NEXTHOP="host2.example.com",SEQUENCE=2;
  ```
  ```
  ADD APN:APN="ims";
  ```
  ```
  ADD REALMBINDAPN:APN="ims",APPLICATION=S6B,CONSTBYIMSISW=DISABLE,REALMNAME="3gppaaa.huawei.com";
  ```
  //配置3GPP AAA相关信息，用于配置PGW-C向Diameter AAA请求授权时携带P-GW的IP地址。
  /*如果不需要支持VoWifi切换到VoNR，则 **ADD DIAMAAAGRP** 命令的 “PGWIDENTITY” 参数配置为IP或FQDN方式均可以；如果需要VoWifi支持切换到VoNR，则 **ADD DIAMAAAGRP** 命令的 “PGWIDENTITY” 参数需要配置为FQDN方式，因为AMF不支持IP方式服务发现SMF。当 “PGWIDENTITY” 参数配置为FQDN方式时，那么需要继续配置脚本“增加逻辑接口主机名”。*/
  ```
  ADD DIAMAAAGRP: GROUPNAME="diametergroup", PGWIDENTITY=HOST_NAME;
  ```
  ```
  ADD APNDIAMAAAGRP: APN="ims", GROUPNAME="diametergroup";
  ```
  //【可选】增加逻辑接口主机名，用于PGW-C向Diameter AAA请求授权携带FQDN时配置。
  ```
  ADD PGWHOSTNAME:PGWHOSTNAME="topon.pgw-s5.app-hdnnboshsaegwc014bhw-02ahw012.sh.sh.node.epc.mnc000.mcc460.3gppnetwork.org",INTFTYPE=S5_P_OR_GN_OR_S2B;
  ```

## [任务示例二：S6b over DRA（SCTP链路）](#ZH-CN_OPI_0275821602)

任务描述

本实例中，将在GGSN/PGW-C上进行数据配置实现以下要求：

- GGSN/PGW-C使用VPN缺省路由与DRA建立起正常的IP连接。
- GGSN/PGW-C与3GPP AAA之间无直连路径，通过DRA进行Diameter消息的转发。
    - GGSN/PGW-C与两个DRA对接，host分别为host1.example.com、host2.example.com，每个DRA各两个IP地址。
    - 两条Diameter路由，第一跳指向DRA1（host1.example.com），第二跳指向DRA2（host2.example.com）。
    - 基于APN（ims）绑定Realm（3gppaaa.huawei.com）。

**图2** S6b over DRA（SCTP链路）

<br>

![](激活S6b over DRA（静态路由+BFD组网）_75821602.assets/zh-cn_image_0000002555152567_2.png)

脚本

1. 参考[静态路由+BFD组网](../../../../初始配置/UNC初始配置与调测/组网路由配置/配置VNF侧IP路由数据（非SDN）/自动部署（推荐）/配置静态路由+BFD组网（IPv4）_75096861.md)配置对应的组网。
2. 配置本端数据。
  //创建一个VPN实例。
  ```
  ADD VPNINST:VPNINSTANCE="vpn_s6bif";
  ```
  //配置S6b接口Diameter应用集中点模式。
  ```
  SET CONCENPOINT:S6BCONCENMODE=LOCALPORT;
  ```
  //配置S6b逻辑接口。

  ```
  ADD LOGICINF:NAME="s6bif1/0/0",IPVERSION=IPV4,IPV4ADDRESS1="10.8.10.1",IPV4MASK1="255.255.255.255",IPV4ADDRESS2="10.8.10.2",IPV4MASK2="255.255.255.255",VPNINSTANCE="vpn_s6bif";
  ```

  ```
  ADD LOGICINF:NAME="s6bif1/0/1",IPVERSION=IPV4,IPV4ADDRESS1="10.8.10.4",IPV4MASK1="255.255.255.255",IPV4ADDRESS2="10.8.10.5",IPV4MASK2="255.255.255.255",VPNINSTANCE="vpn_s6bif";
  ```
3. 配置DRA数据。
  //使能Realm-Based Routing。
  ```
  SET DIAMETERPARA:REALMBASEROUTE=ENABLE;
  ```
  //配置DRA主机名以及地址信息。
  ```
  ADD SCTPENDPOINT:ENDPOINTNAME="endpoint0",IPVERSION=IPV4,IPV4ADDRESS1="10.11.21.59",IPV4ADDRESS2="10.11.21.60";
  ```
  ```
  ADD SCTPENDPOINT:ENDPOINTNAME="endpoint1",IPVERSION=IPV4,IPV4ADDRESS1="10.11.21.11",IPV4ADDRESS2="10.11.21.12";
  ```
  ```
  ADD SCTPENDPOINT:ENDPOINTNAME="endpoint2",IPVERSION=IPV4,IPV4ADDRESS1="10.11.22.59",IPV4ADDRESS2="10.11.22.60";
  ```
  ```
  ADD SCTPENDPOINT:ENDPOINTNAME="endpoint3",IPVERSION=IPV4,IPV4ADDRESS1="10.11.22.11",IPV4ADDRESS2="10.11.22.12";
  ```
  ```
  ADD DRA:HOSTNAME="host1.example.com",VPNINSTANCE="vpn_s6bif";
  ```
  ```
  ADD DRA:HOSTNAME="host2.example.com",VPNINSTANCE="vpn_s6bif";
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
  ADD DIAMLOCINFO:HOSTNAME="pgw_1",REALMNAME="example1.com",PRODUCTNAME="unc";
  ```
  ```
  ADD DIAMLOCINFO:HOSTNAME="pgw_2",REALMNAME="example1.com",PRODUCTNAME="unc";
  ```
  //配置网元对接。
  ```
  ADD DIAMCONNGRP:CONNGROUPNAME="dconn_s6b1",LOCALHOSTNAME="pgw_1",APPLICATION=S6B,PEERHOSTNAME="host1.example.com";
  ```
  ```
  ADD DIAMCONNGRP:CONNGROUPNAME="dconn_s6b2",LOCALHOSTNAME="pgw_2",APPLICATION=S6B,PEERHOSTNAME="host2.example.com";
  ```
  ```
  ADD DIAMCONNECTION:DIAMCONNGRP="dconn_s6b1",LOCINTERFACE="s6bif1/0/0",LOCALPORT=19766;
  ```
  ```
  ADD DIAMCONNECTION:DIAMCONNGRP="dconn_s6b2",LOCINTERFACE="s6bif1/0/1",LOCALPORT=19767;
  ```
  ```
  ADD DIAMRTREALM:REALMNAME="3gppaaa.huawei.com",APPLICATION=S6B,SELECTMODE=MASTER_SLAVE;
  ```
  ```
  ADD DIAMRTNEXTHOP:REALMNAME="3gppaaa.huawei.com",APPLICATION=S6B,NEXTHOP="host1.example.com",SEQUENCE=1;
  ```
  ```
  ADD DIAMRTNEXTHOP:REALMNAME="3gppaaa.huawei.com",APPLICATION=S6B,NEXTHOP="host2.example.com",SEQUENCE=2;
  ```
  ```
  ADD APN:APN="ims";
  ```
  ```
  ADD REALMBINDAPN:APN="ims",APPLICATION=S6B,CONSTBYIMSISW=DISABLE,REALMNAME="3gppaaa.huawei.com";
  ```
  //配置3GPP AAA相关信息，用于配置PGW-C向Diameter AAA请求授权时携带P-GW的IP地址。
  /*如果不需要支持VoWifi切换到VoNR，则 **ADD DIAMAAAGRP** 命令的 “PGWIDENTITY” 参数配置为IP或FQDN方式均可以；如果需要VoWifi支持切换到VoNR，则 **ADD DIAMAAAGRP** 命令的 “PGWIDENTITY” 参数需要配置为FQDN方式，因为AMF不支持IP方式服务发现SMF。当 “PGWIDENTITY” 参数配置为FQDN方式时，那么需要继续配置脚本“增加逻辑接口主机名”。*/
  ```
  ADD DIAMAAAGRP: GROUPNAME="diametergroup", PGWIDENTITY=HOST_NAME;
  ```
  ```
  ADD APNDIAMAAAGRP: APN="ims", GROUPNAME="diametergroup";
  ```
  //【可选】增加逻辑接口主机名，用于PGW-C向Diameter AAA请求授权携带FQDN时配置。
  ```
  ADD PGWHOSTNAME:PGWHOSTNAME="topon.pgw-s5.app-hdnnboshsaegwc014bhw-02ahw012.sh.sh.node.epc.mnc000.mcc460.3gppnetwork.org",INTFTYPE=S5_P_OR_GN_OR_S2B;
  ```
