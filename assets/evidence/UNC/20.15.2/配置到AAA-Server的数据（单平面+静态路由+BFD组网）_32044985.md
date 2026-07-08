# 配置到AAA Server的数据（单平面+静态路由+BFD组网）

- [操作场景](#ZH-CN_OPI_0232044985__1.3.1)
- [必备事项](#ZH-CN_OPI_0232044985__1.3.2)
- [操作步骤](#ZH-CN_OPI_0232044985__1.3.3)
- [验证方法](#ZH-CN_OPI_0232044985__1.3.4)
- [任务示例](#ZH-CN_OPI_0232044985__1.3.5)

## [操作场景](#ZH-CN_OPI_0232044985)

当AAA Server（计费/鉴权AAA服务器）位于Internet中， UNC 与计费/鉴权AAA服务器之间采用带外组网方式，以起到保护数据的作用。即到PDN的数据报文和到计费/鉴权AAA服务器的RADIUS信令报文使用不同的出接口，并绑定在不同的VPN中。

> **说明**
> 适用于 GGSN、 PGW-C、SMF。

## [必备事项](#ZH-CN_OPI_0232044985)

前提条件

UNC 与网络实体之间的网络环境已经构建完成。

数据

*表1 整体配置*

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| [**ADD L3VPNINST**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例/增加L3VPN实例（ADD L3VPNINST）_49802446.md) | VPN实例名称 (VRFNAME) | vpn_pdn<br>vpn_aaa | 本端规划 | - |
| **[**ADD VPNINSTAF**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例地址族/增加L3VPN实例地址族（ADD VPNINSTAF）_49802178.md)** | VPN实例名称 (VRFNAME) | vpn_pdn<br>vpn_aaa | 已配置数据中获取 | 已通过<br>[**ADD L3VPNINST**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例/增加L3VPN实例（ADD L3VPNINST）_49802446.md)<br>命令进行配置，可以使用<br>**[**LST L3VPNINST**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例/查询L3VPN实例（LST L3VPNINST）_49961238.md)**<br>进行查询 |
| **[**ADD VPNINSTAF**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例地址族/增加L3VPN实例地址族（ADD VPNINSTAF）_49802178.md)** | 地址族类型 (AFTYPE) | ipv4uni | 本端规划 | - |
| **[**ADD VPNINSTAF**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例地址族/增加L3VPN实例地址族（ADD VPNINSTAF）_49802178.md)** | 路由标识（VRFRD） | 100:1<br>200:1 | 本端规划 | - |
| **[**ADD VPNINSTAF**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例地址族/增加L3VPN实例地址族（ADD VPNINSTAF）_49802178.md)** | 实例的标签分配模式 (VRFLABELMODE) | perRoute | 本端规划 | - |
| [**ADD VPNINST**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/增加VPN实例（ADD VPNINST）_09653755.md) | VPN实例名（VPNINSTANCE） | vpn_pdn<br>vpn_aaa | 本端规划 | - |
| [**ADD LOGICIP**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IP管理/IP配置/增加逻辑IP地址（ADD LOGICIP）_09587376.md) | IP地址类型（IPVERSION） | IPv4 | 本端规划 | 逻辑接口使用的逻辑IP。 |
| [**ADD LOGICIP**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IP管理/IP配置/增加逻辑IP地址（ADD LOGICIP）_09587376.md) | IPv4地址（LOGICIPV4） | 10.8.20.1<br>10.8.20.2 | 本端规划 | 逻辑接口使用的逻辑IP。 |
| **[ADD LOGICINF](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)** | 逻辑接口名称（NAME） | giif1/0/0<br>giif1/0/1 | 本端规划 | 配置使用的逻辑接口，其中“giif1/0/0”和“10.8.20.1”用于鉴权AAA服务器，“giif1/0/1”和“10.8.20.2”用于计费AAA服务器。 |
| **[ADD LOGICINF](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)** | 逻辑接口的IP版本（IPVERSION） | IPV4 | 本端规划 | 配置使用的逻辑接口，其中“giif1/0/0”和“10.8.20.1”用于鉴权AAA服务器，“giif1/0/1”和“10.8.20.2”用于计费AAA服务器。 |
| **[ADD LOGICINF](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)** | 逻辑接口的IPv4地址1（IPV4ADDRESS1） | 10.8.20.1<br>10.8.20.2 | 全网规划 | 配置使用的逻辑接口，其中“giif1/0/0”和“10.8.20.1”用于鉴权AAA服务器，“giif1/0/1”和“10.8.20.2”用于计费AAA服务器。 |
| **[ADD LOGICINF](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)** | 逻辑接口的IPv4掩码1（IPV4MASK1） | 255.255.255.255 | 固定取值 | 配置使用的逻辑接口，其中“giif1/0/0”和“10.8.20.1”用于鉴权AAA服务器，“giif1/0/1”和“10.8.20.2”用于计费AAA服务器。 |
| **[ADD LOGICINF](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)** | VPN实例名称（VPNINSTANCE） | vpn_pdn<br>vpn_aaa | 已配置数据中获取 | 鉴权/计费AAA服务器所属的VPN实例名。已通过<br>[**ADD VPNINST**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/增加VPN实例（ADD VPNINST）_09653755.md)<br>配置，可以使用<br>[**LST VPNINST**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/查询VPN实例（LST VPNINST）_09651519.md)<br>命令进行查询。 |
| **[ADD RDSSVRGRP](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/RADIUS管理/连接管理/Radius服务器组/增加Radius服务器组（ADD RDSSVRGRP）_09896730.md)** | Radius Server Group名称（RDSSVRGRPNAME） | isprg | 本端规划 | - |
| **[ADD RDSSVRGRP](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/RADIUS管理/连接管理/Radius服务器组/增加Radius服务器组（ADD RDSSVRGRP）_09896730.md)** | 模式（Mode） | ROUND_ROBIN | 本端规划 | 将RADIUS AAA服务器组设置为轮选负荷分担模式。 |
| **[ADD RDSSVRGRP](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/RADIUS管理/连接管理/Radius服务器组/增加Radius服务器组（ADD RDSSVRGRP）_09896730.md)** | 支持可选计费消息（SIGOPTACCTMSG） | DISABLE | 本端规划 | - |
| [**ADD APN**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md) | APN名称（APN） | apn1 | 全网规划 | - |
| [**ADD APN**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md) | 绑定VPN（HASVPN） | ENABLE | 本端规划 | - |
| [**ADD APN**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md) | VPN实例名（VPNINSTANCE） | vpn_pdn | 已配置数据中获取 | 已通过<br>[**ADD VPNINST**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/增加VPN实例（ADD VPNINST）_09653755.md)<br>配置，可以使用<br>[**LST VPNINST**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/查询VPN实例（LST VPNINST）_09651519.md)<br>命令进行查询。 |
| [**ADD APN**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md) | 绑定IPv6 VPN（HASVPNIPV6） | DISABLE | 本端规划 | - |
| [**ADD APN**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md) | 故障重启业务恢复功能PGW开关（RESTORPGWSWITCH） | INHERIT | 本端规划 | - |
| [**ADD APN**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md) | 去活消息携带reactivation-request开关（REACWITHDEL） | DISABLE | 本端规划 | - |
| **[ADD APNRDSCLIENTIP](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/RADIUS管理/APN的Radius客户端地址属性/增加APN Radius Client IP接口（ADD APNRDSCLIENTIP）_09897362.md)** | APN名称（APN） | apn1 | 全网规划 | 已通过<br>[**ADD APN**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)<br>配置，可以使用<br>**[**LST APN**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/查询APN配置（LST APN）_09652599.md)**<br>命令进行查询。 |
| **[ADD APNRDSCLIENTIP](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/RADIUS管理/APN的Radius客户端地址属性/增加APN Radius Client IP接口（ADD APNRDSCLIENTIP）_09897362.md)** | 鉴权或计费（AUTHORACCT） | ACCOUNTING<br>AUTHENTICATION | 全网规划 | - |
| **[ADD APNRDSCLIENTIP](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/RADIUS管理/APN的Radius客户端地址属性/增加APN Radius Client IP接口（ADD APNRDSCLIENTIP）_09897362.md)** | 接口名称（INTFNAME） | giif1/0/0<br>giif1/0/1 | 已配置数据中获取 | 已通过<br>**[ADD LOGICINF](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)**<br>配置，可以使用<br>**[LST LOGICINF](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/查询逻辑接口（LST LOGICINF）_09896726.md)**<br>命令进行查询。 |
| **[ADD APNRDSSVRGRP](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/RADIUS管理/连接管理/APN Radius服务器/设置APN Radius服务器组（ADD APNRDSSVRGRP）_09896735.md)** | APN名称（APN） | apn1 | 全网规划 | 已通过<br>[**ADD APN**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)<br>配置，可以使用<br>**[**LST APN**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/查询APN配置（LST APN）_09652599.md)**<br>命令进行查询。 |
| **[ADD APNRDSSVRGRP](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/RADIUS管理/连接管理/APN Radius服务器/设置APN Radius服务器组（ADD APNRDSSVRGRP）_09896735.md)** | Radius Server Group名称（RDSSVRGRPNAME） | isprg | 已配置数据中获取 | 鉴权AAA服务器所在的AAA服务器组，已通过<br>**[ADD RDSSVRGRP](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/RADIUS管理/连接管理/Radius服务器组/增加Radius服务器组（ADD RDSSVRGRP）_09896730.md)**<br>进行配置。 |

*表2 鉴权AAA服务器配置*

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| **[ADD RDSSVR](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/RADIUS管理/连接管理/Radius服务器/增加RADIUS服务器（ADD RDSSVR）_09896756.md)** | Radius Server Group名称（RDSSVRGRPNAME） | isprg | 已配置数据中获取 | 鉴权AAA服务器所在的AAA服务器组，已通过<br>**[ADD RDSSVRGRP](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/RADIUS管理/连接管理/Radius服务器组/增加Radius服务器组（ADD RDSSVRGRP）_09896730.md)**<br>进行配置。 |
| **[ADD RDSSVR](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/RADIUS管理/连接管理/Radius服务器/增加RADIUS服务器（ADD RDSSVR）_09896756.md)** | 服务器类型（SERVERTYPE） | AUTHENTICATION | 全网规划 | - |
| **[ADD RDSSVR](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/RADIUS管理/连接管理/Radius服务器/增加RADIUS服务器（ADD RDSSVR）_09896756.md)** | 服务器IP版本（IPVERSION） | IPV4 | 全网规划 | 鉴权AAA服务器IP地址、端口号、密钥。 |
| **[ADD RDSSVR](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/RADIUS管理/连接管理/Radius服务器/增加RADIUS服务器（ADD RDSSVR）_09896756.md)** | IPv4地址（SERVERIPV4） | 10.168.10.1 | 全网规划 | 鉴权AAA服务器IP地址、端口号、密钥。 |
| **[ADD RDSSVR](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/RADIUS管理/连接管理/Radius服务器/增加RADIUS服务器（ADD RDSSVR）_09896756.md)** | 端口（PORT） | 1812 | 与对端协商 | 鉴权AAA服务器IP地址、端口号、密钥。 |
| **[ADD RDSSVR](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/RADIUS管理/连接管理/Radius服务器/增加RADIUS服务器（ADD RDSSVR）_09896756.md)** | 服务器密钥（加密的）（CIPHERKEY） | ispchina | 与对端协商 | 鉴权AAA服务器IP地址、端口号、密钥。 |
| **[ADD RDSSVR](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/RADIUS管理/连接管理/Radius服务器/增加RADIUS服务器（ADD RDSSVR）_09896756.md)** | 主备用类型（PRIFLAG） | PRIMARY | 本端规划 | - |
| **[ADD RDSSVR](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/RADIUS管理/连接管理/Radius服务器/增加RADIUS服务器（ADD RDSSVR）_09896756.md)** | VPN实例名（VPNINSTANCE） | vpn_aaa | 已配置数据中获取 | 计费AAA服务器所属的VPN实例名。已通过<br>[**ADD VPNINST**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/增加VPN实例（ADD VPNINST）_09653755.md)<br>配置，可以使用<br>[**LST VPNINST**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/查询VPN实例（LST VPNINST）_09651519.md)<br>命令进行查询。 |
| **[ADD RDSSVR](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/RADIUS管理/连接管理/Radius服务器/增加RADIUS服务器（ADD RDSSVR）_09896756.md)** | 确认服务器密钥（加密的）（CIPHERKEYCNFM） | ispchina | 与对端协商 | - |

*表3 计费AAA服务器配置*

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| **[ADD RDSSVR](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/RADIUS管理/连接管理/Radius服务器/增加RADIUS服务器（ADD RDSSVR）_09896756.md)** | Radius Server Group名称（RDSSVRGRPNAME） | isprg | 已配置数据中获取 | 计费AAA服务器所在的AAA服务器组，已通过<br>**[ADD RDSSVRGRP](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/RADIUS管理/连接管理/Radius服务器组/增加Radius服务器组（ADD RDSSVRGRP）_09896730.md)**<br>进行配置。 |
| **[ADD RDSSVR](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/RADIUS管理/连接管理/Radius服务器/增加RADIUS服务器（ADD RDSSVR）_09896756.md)** | 服务器类型（SERVERTYPE） | ACCOUNTING | 全网规划 | - |
| **[ADD RDSSVR](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/RADIUS管理/连接管理/Radius服务器/增加RADIUS服务器（ADD RDSSVR）_09896756.md)** | 服务器IP版本（IPVERSION） | IPV4 | 全网规划 | 计费AAA服务器IP地址、端口号、密钥。 |
| **[ADD RDSSVR](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/RADIUS管理/连接管理/Radius服务器/增加RADIUS服务器（ADD RDSSVR）_09896756.md)** | IPv4地址（SERVERIPV4） | 10.168.10.1 | 全网规划 | 计费AAA服务器IP地址、端口号、密钥。 |
| **[ADD RDSSVR](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/RADIUS管理/连接管理/Radius服务器/增加RADIUS服务器（ADD RDSSVR）_09896756.md)** | 端口（PORT） | 1813 | 与对端协商 | 计费AAA服务器IP地址、端口号、密钥。 |
| **[ADD RDSSVR](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/RADIUS管理/连接管理/Radius服务器/增加RADIUS服务器（ADD RDSSVR）_09896756.md)** | 服务器密钥（加密的）（CIPHERKEY） | ispchina | 与对端协商 | 计费AAA服务器IP地址、端口号、密钥。 |
| **[ADD RDSSVR](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/RADIUS管理/连接管理/Radius服务器/增加RADIUS服务器（ADD RDSSVR）_09896756.md)** | 主备用类型（PRIFLAG） | PRIMARY | 本端规划 | - |
| **[ADD RDSSVR](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/RADIUS管理/连接管理/Radius服务器/增加RADIUS服务器（ADD RDSSVR）_09896756.md)** | VPN实例名（VPNINSTANCE） | vpn_aaa | 已配置数据中获取 | 计费AAA服务器所属的VPN实例名。已通过<br>[**ADD VPNINST**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/增加VPN实例（ADD VPNINST）_09653755.md)<br>配置，可以使用<br>[**LST VPNINST**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/查询VPN实例（LST VPNINST）_09651519.md)<br>命令进行查询。 |
| **[ADD RDSSVR](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/RADIUS管理/连接管理/Radius服务器/增加RADIUS服务器（ADD RDSSVR）_09896756.md)** | 确认服务器密钥（加密的）（CIPHERKEYCNFM） | ispchina | 与对端协商 | - |

## [操作步骤](#ZH-CN_OPI_0232044985)

1. 参考 [配置静态路由+BFD组网（IPv4）](../../../../../初始配置/UNC初始配置与调测/组网路由配置/配置VNF侧IP路由数据（非SDN）/自动部署（推荐）/配置静态路由+BFD组网（IPv4）_75096861.md) 配置对应的组网。
2. 进入 “MML命令行-UNC” 窗口。
3. 创建L3VPN实例。
  [**ADD L3VPNINST**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例/增加L3VPN实例（ADD L3VPNINST）_49802446.md)
  **[**ADD VPNINSTAF**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例地址族/增加L3VPN实例地址族（ADD VPNINSTAF）_49802178.md)**
4. 创建VPN实例。
  [**ADD VPNINST**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/增加VPN实例（ADD VPNINST）_09653755.md)
5. 配置Gi逻辑接口。
  [**ADD LOGICIP**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IP管理/IP配置/增加逻辑IP地址（ADD LOGICIP）_09587376.md)
  **[ADD LOGICINF](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)**
6. **可选：** 配置鉴权或计费AAA服务器使用的PGW-U/UPF列表。
  **[ADD UPLIST4RDS](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/RADIUS管理/连接管理/UP列表/向RADIUS服务器使用的UP列表中增加UP（ADD UPLIST4RDS）_52749060.md)**
7. 配置鉴权/计费AAA服务器。
    a. 配置AAA服务器组以及服务器的工作模式。
      **[ADD RDSSVRGRP](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/RADIUS管理/连接管理/Radius服务器组/增加Radius服务器组（ADD RDSSVRGRP）_09896730.md)**
    b. 设置主用鉴权AAA服务器的IP地址、目的端口号、所属VPN、密钥。
      **[ADD RDSSVR](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/RADIUS管理/连接管理/Radius服务器/增加RADIUS服务器（ADD RDSSVR）_09896756.md)**
    c. **可选：**设置备用鉴权AAA服务器的IP地址、目的端口号、所属VPN、密钥。
      **[ADD RDSSVR](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/RADIUS管理/连接管理/Radius服务器/增加RADIUS服务器（ADD RDSSVR）_09896756.md)**
    d. 配置主用计费AAA服务器的IP地址、目的端口号、所属VPN、密钥。
      **[ADD RDSSVR](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/RADIUS管理/连接管理/Radius服务器/增加RADIUS服务器（ADD RDSSVR）_09896756.md)**
    e. **可选：**配置备用计费AAA服务器的IP地址、目的端口号、所属VPN、密钥。
      **[ADD RDSSVR](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/RADIUS管理/连接管理/Radius服务器/增加RADIUS服务器（ADD RDSSVR）_09896756.md)**
      > **说明**
      > 步骤b-e中，执行该命令多次，可以配置多个计费/鉴权AAA服务器。
    f. 配置APN。
      [**ADD APN**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)
    g. 配置APN下的Client-IP。
      **[ADD APNRDSCLIENTIP](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/RADIUS管理/APN的Radius客户端地址属性/增加APN Radius Client IP接口（ADD APNRDSCLIENTIP）_09897362.md)**
    h. APN实例下绑定RADIUS服务器组。
      **[ADD APNRDSSVRGRP](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/RADIUS管理/连接管理/APN Radius服务器/设置APN Radius服务器组（ADD APNRDSSVRGRP）_09896735.md)**

## [验证方法](#ZH-CN_OPI_0232044985)

具体步骤请参见 [调测到AAA Server的数据](../调测到AAA Server的数据_32027181.md) 。

## [任务示例](#ZH-CN_OPI_0232044985)

任务描述

UNC 与计费/鉴权AAA服务器通过带外组网方式对接时的配置范例，使用缺省路由与计费/鉴权AAA服务器建立起正常的IP连接。

脚本

//参考 [配置静态路由+BFD组网（IPv4）](../../../../../初始配置/UNC初始配置与调测/组网路由配置/配置VNF侧IP路由数据（非SDN）/自动部署（推荐）/配置静态路由+BFD组网（IPv4）_75096861.md) 配置对应的组网。

//创建L3VPN实例。

//1.数据报文所属的L3VPN实例。

```
ADD L3VPNINST: VRFNAME ="vpn_pdn";
```

```
ADD VPNINSTAF: VRFNAME ="vpn_pdn",AFTYPE=ipv4uni,VRFRD="100:1", VRFLABELMODE=perRoute;
```

//2.RADIUS信令报文所属的L3VPN实例。

```
ADD L3VPNINST: VRFNAME ="vpn_aaa";
```

```
ADD VPNINSTAF: VRFNAME="vpn_aaa", AFTYPE=ipv4uni, VRFRD="200:1", VRFLABELMODE=perRoute;
```

//创建VPN实例。

```
ADD VPNINST: VPNINSTANCE ="vpn_pdn";
ADD VPNINST:VPNINSTANCE="vpn_aaa";
```

//配置Gi接口。

//1.配置Giif1/0/0接口。

```
ADD LOGICIP: IPVERSION=IPv4, LOGICIPV4="10.8.20.1", VPNINSTNAME="vpn_aaa";
ADD LOGICINF:NAME="giif1/0/0",IPVERSION=IPV4,IPV4ADDRESS1="10.8.20.1",IPV4MASK1="255.255.255.255",VPNINSTANCE="vpn_aaa";
```

//2.配置Giif1/0/1接口。

```
ADD LOGICIP: IPVERSION=IPv4, LOGICIPV4="10.8.20.2", VPNINSTNAME="vpn_aaa";
ADD LOGICINF:NAME="giif1/0/1",IPVERSION=IPV4,IPV4ADDRESS1="10.8.20.2",IPV4MASK1="255.255.255.255",VPNINSTANCE="vpn_aaa";
```

//配置鉴权/计费AAA服务器。

```
ADD RDSSVRGRP: RDSSVRGRPNAME="isprg", MODE=ROUND_ROBIN, SIGOPTACCTMSG=DISABLE;
```

```
ADD RDSSVR: RDSSVRGRPNAME="isprg", SERVERTYPE=AUTHENTICATION, IPVERSION=IPV4, SERVERIPV4="10.168.10.1", PORT=1812, VPNINSTANCE="vpn_aaa", CIPHERKEY="*****", PRIFLAG=PRIMARY, CIPHERKEYCNFM="*****";
```

```
ADD RDSSVR: RDSSVRGRPNAME="isprg", SERVERTYPE=ACCOUNTING, IPVERSION=IPV4, SERVERIPV4="10.168.10.1", PORT=1813, VPNINSTANCE="vpn_aaa", CIPHERKEY="*****", PRIFLAG=PRIMARY, CIPHERKEYCNFM="*****";
```

```
ADD APN: APN="apn1", HASVPN=ENABLE, VPNINSTANCE="vpn_pdn", HASVPNIPV6=DISABLE, RESTORPGWSWITCH=INHERIT, REACWITHDEL=DISABLE;
```

```
ADD APNRDSCLIENTIP: APN="apn1",AUTHORACCT=AUTHENTICATION,INTFNAME="giif1/0/0";
```

```
ADD APNRDSCLIENTIP: APN="apn1",AUTHORACCT=ACCOUNTING,INTFNAME="giif1/0/1";
```

```
ADD APNRDSSVRGRP: APN="apn1",RDSSVRGRPNAME="isprg";
```
