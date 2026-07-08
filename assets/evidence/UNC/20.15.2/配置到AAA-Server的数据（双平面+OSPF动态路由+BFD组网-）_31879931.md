# 配置到AAA Server的数据（双平面+OSPF动态路由+BFD组网 ）

- [操作场景](#ZH-CN_OPI_0231879931__1.3.1)
- [必备事项](#ZH-CN_OPI_0231879931__1.3.2)
- [操作步骤](#ZH-CN_OPI_0231879931__1.3.3)
- [验证方法](#ZH-CN_OPI_0231879931__1.3.4)
- [任务示例](#ZH-CN_OPI_0231879931__1.3.5)

## [操作场景](#ZH-CN_OPI_0231879931)

在企业网中，可以通过在网络边缘部署AAA Server（计费/鉴权AAA服务器）进行跨IP鉴权和计费，实现外部办公人员接入。当计费/鉴权AAA服务器位于企业网中， UNC 与计费/鉴权AAA服务器之间采用带内组网方式，即到PDN的数据报文和到计费AAA服务器服务器的RADIUS信令报文在同一VPN下。

> **说明**
> 适用于 GGSN、 PGW-C、SMF。

## [必备事项](#ZH-CN_OPI_0231879931)

前提条件

- 请仔细阅读[IPFD-015001 VRF功能](../../../IP基本功能/IPFD-015001 VRF功能_61317255.md)和[IPFD-014001 支持OSPF特性概述](../../../IP基本功能/IPFD-014000 路由功能/IPFD-014001 支持OSPF/IPFD-014001 支持OSPF特性概述_61317384.md)。
- UNC与网络实体之间的网络环境已经构建完成。

数据

*表1 整体配置*

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| [**ADD L3VPNINST**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例/增加L3VPN实例（ADD L3VPNINST）_49802446.md) | VPN实例名称 (VRFNAME) | vpn_pdn | 本端规划 | - |
| **[**ADD VPNINSTAF**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例地址族/增加L3VPN实例地址族（ADD VPNINSTAF）_49802178.md)** | VPN实例名称 (VRFNAME) | vpn_pdn | 已配置数据中获取 | 已通过<br>[**ADD L3VPNINST**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例/增加L3VPN实例（ADD L3VPNINST）_49802446.md)<br>命令进行配置，可以使用<br>**[**LST L3VPNINST**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例/查询L3VPN实例（LST L3VPNINST）_49961238.md)**<br>进行查询 |
| **[**ADD VPNINSTAF**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例地址族/增加L3VPN实例地址族（ADD VPNINSTAF）_49802178.md)** | 地址族类型 (AFTYPE) | ipv4uni | 本端规划 | - |
| **[**ADD VPNINSTAF**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例地址族/增加L3VPN实例地址族（ADD VPNINSTAF）_49802178.md)** | 实例的标签分配模式 (VRFLABELMODE) | perRoute | 本端规划 | - |
| [**ADD VPNINST**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/增加VPN实例（ADD VPNINST）_09653755.md) | VPN实例名（VPNINSTANCE） | vpn_pdn | 本端规划 | - |
| [**ADD LOGICIP**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IP管理/IP配置/增加逻辑IP地址（ADD LOGICIP）_09587376.md) | IP地址类型（IPVERSION） | IPv4 | 本端规划 | 逻辑接口使用的逻辑IP。 |
| [**ADD LOGICIP**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IP管理/IP配置/增加逻辑IP地址（ADD LOGICIP）_09587376.md) | IPv4地址（LOGICIPV4） | 10.8.20.1<br>10.8.20.2 | 本端规划 | 逻辑接口使用的逻辑IP。 |
| **[**ADD LOGICINF**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)** | 逻辑接口名称（NAME） | giif1/0/0<br>giif1/0/1 | 本端规划 | 配置使用的逻辑接口，其中“giif1/0/0”和“10.8.20.1”用于鉴权AAA服务器，“giif1/0/1”和“10.8.20.2”用于计费AAA服务器。 |
| **[**ADD LOGICINF**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)** | 逻辑接口的IP版本（IPVERSION） | IPV4 | 本端规划 | 配置使用的逻辑接口，其中“giif1/0/0”和“10.8.20.1”用于鉴权AAA服务器，“giif1/0/1”和“10.8.20.2”用于计费AAA服务器。 |
| **[**ADD LOGICINF**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)** | 逻辑接口的IPv4地址1（IPV4ADDRESS1） | 10.8.20.1<br>10.8.20.2 | 全网规划 | 配置使用的逻辑接口，其中“giif1/0/0”和“10.8.20.1”用于鉴权AAA服务器，“giif1/0/1”和“10.8.20.2”用于计费AAA服务器。 |
| **[**ADD LOGICINF**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)** | 逻辑接口的IPv4掩码1（IPV4MASK1） | 255.255.255.255 | 固定取值 | 配置使用的逻辑接口，其中“giif1/0/0”和“10.8.20.1”用于鉴权AAA服务器，“giif1/0/1”和“10.8.20.2”用于计费AAA服务器。 |
| **[**ADD LOGICINF**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)** | VPN实例名称（VPNINSTANCE） | vpn_pdn | 已配置数据中获取 | 鉴权/计费AAA服务器所属的VPN实例名。已通过<br>[**ADD VPNINST**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/增加VPN实例（ADD VPNINST）_09653755.md)<br>配置，可以使用<br>[**LST VPNINST**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/查询VPN实例（LST VPNINST）_09651519.md)<br>命令进行查询。 |
| **[ADD RDSSVRGRP](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/RADIUS管理/连接管理/Radius服务器组/增加Radius服务器组（ADD RDSSVRGRP）_09896730.md)** | Radius Server Group名称（RDSSVRGRPNAME） | isprg | 本端规划 | - |
| **[ADD RDSSVRGRP](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/RADIUS管理/连接管理/Radius服务器组/增加Radius服务器组（ADD RDSSVRGRP）_09896730.md)** | 模式（MODE） | MASTER_SLAVE | 本端规划 | - |
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
| **[ADD RDSSVR](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/RADIUS管理/连接管理/Radius服务器/增加RADIUS服务器（ADD RDSSVR）_09896756.md)** | VPN实例名（VPNINSTANCE） | vpn_pdn | 已配置数据中获取 | 计费AAA服务器所属的VPN实例名。已通过<br>[**ADD VPNINST**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/增加VPN实例（ADD VPNINST）_09653755.md)<br>配置，可以使用<br>[**LST VPNINST**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/查询VPN实例（LST VPNINST）_09651519.md)<br>命令进行查询。 |
| **[ADD RDSSVR](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/RADIUS管理/连接管理/Radius服务器/增加RADIUS服务器（ADD RDSSVR）_09896756.md)** | 确认服务器密钥（加密的）（CIPHERKEYCNFM） | ispchina | 与对端协商 | - |

*表3 计费AAA服务器配置*

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| **[ADD UPLIST4RDS](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/RADIUS管理/连接管理/UP列表/向RADIUS服务器使用的UP列表中增加UP（ADD UPLIST4RDS）_52749060.md)** | UP列表名称（UPLISTNAME） | uplist1 | 本端规划 | - |
| **[ADD UPLIST4RDS](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/RADIUS管理/连接管理/UP列表/向RADIUS服务器使用的UP列表中增加UP（ADD UPLIST4RDS）_52749060.md)** | UP实例标识（UPINSTANCEID） | up1<br>up2 | 已配置数据中获取 | 在初始配置时已经通过<br>**[ADD PNFPROFILE](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端NF实例概述信息管理/增加对端NF实例概述信息（ADD PNFPROFILE）_09653772.md)**<br>命令配置。此处以配置的UP名称为“up1”和“up2”为例。 |
| **[ADD RDSSVR](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/RADIUS管理/连接管理/Radius服务器/增加RADIUS服务器（ADD RDSSVR）_09896756.md)** | Radius Server Group名称（RDSSVRGRPNAME） | isprg | 已配置数据中获取 | 计费AAA服务器所在的AAA服务器组，已通过<br>**[ADD RDSSVRGRP](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/RADIUS管理/连接管理/Radius服务器组/增加Radius服务器组（ADD RDSSVRGRP）_09896730.md)**<br>进行配置。 |
| **[ADD RDSSVR](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/RADIUS管理/连接管理/Radius服务器/增加RADIUS服务器（ADD RDSSVR）_09896756.md)** | 服务器类型（SERVERTYPE） | ACCOUNTING | 全网规划 | - |
| **[ADD RDSSVR](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/RADIUS管理/连接管理/Radius服务器/增加RADIUS服务器（ADD RDSSVR）_09896756.md)** | 服务器IP版本（IPVERSION） | IPV4 | 全网规划 | 计费AAA服务器IP地址、端口号、密钥。 |
| **[ADD RDSSVR](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/RADIUS管理/连接管理/Radius服务器/增加RADIUS服务器（ADD RDSSVR）_09896756.md)** | IPv4地址（SERVERIPV4） | 10.168.10.1 | 全网规划 | 计费AAA服务器IP地址、端口号、密钥。 |
| **[ADD RDSSVR](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/RADIUS管理/连接管理/Radius服务器/增加RADIUS服务器（ADD RDSSVR）_09896756.md)** | 端口（PORT） | 1813 | 与对端协商 | 计费AAA服务器IP地址、端口号、密钥。 |
| **[ADD RDSSVR](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/RADIUS管理/连接管理/Radius服务器/增加RADIUS服务器（ADD RDSSVR）_09896756.md)** | 服务器密钥（加密的）（CIPHERKEY） | ispchina | 与对端协商 | 计费AAA服务器IP地址、端口号、密钥。 |
| **[ADD RDSSVR](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/RADIUS管理/连接管理/Radius服务器/增加RADIUS服务器（ADD RDSSVR）_09896756.md)** | 主备用类型（PRIFLAG） | PRIMARY | 本端规划 | - |
| **[ADD RDSSVR](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/RADIUS管理/连接管理/Radius服务器/增加RADIUS服务器（ADD RDSSVR）_09896756.md)** | VPN实例名（VPNINSTANCE） | vpn_pdn | 已配置数据中获取 | 计费AAA服务器所属的VPN实例名。已通过<br>[**ADD VPNINST**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/增加VPN实例（ADD VPNINST）_09653755.md)<br>配置，可以使用<br>[**LST VPNINST**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/查询VPN实例（LST VPNINST）_09651519.md)<br>命令进行查询。 |
| **[ADD RDSSVR](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/RADIUS管理/连接管理/Radius服务器/增加RADIUS服务器（ADD RDSSVR）_09896756.md)** | 确认服务器密钥（加密的）（CIPHERKEYCNFM） | ispchina | 与对端协商 | - |

## [操作步骤](#ZH-CN_OPI_0231879931)

1. 参考 [配置动态路由OSPF+BFD组网（IPv4）](../../../../../初始配置/UNC初始配置与调测/组网路由配置/配置VNF侧IP路由数据（非SDN）/手动部署/配置动态路由OSPF+BFD组网（IPv4）_75096780.md) 配置对应的组网。
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

## [验证方法](#ZH-CN_OPI_0231879931)

具体步骤请参见 [调测到AAA Server的数据](../调测到AAA Server的数据_32027181.md) 。

## [任务示例](#ZH-CN_OPI_0231879931)

任务描述

UNC 与计费/鉴权AAA服务器通过带内组网方式对接时的配置范例，使用OSPF动态路由与计费/鉴权AAA服务器建立起正常的IP连接。要求 UNC 基于UPF列表选择计费AAA服务器。

脚本

//参考 [配置动态路由OSPF+BFD组网（IPv4）](../../../../../初始配置/UNC初始配置与调测/组网路由配置/配置VNF侧IP路由数据（非SDN）/手动部署/配置动态路由OSPF+BFD组网（IPv4）_75096780.md) 配置对应的组网。

//创建L3VPN实例。

```
ADD L3VPNINST:VRFNAME="vpn_pdn";
```

```
ADD VPNINSTAF: VRFNAME="vpn_pdn", AFTYPE=ipv4uni, VRFLABELMODE=perRoute;
```

//创建VPN实例。

```
ADD VPNINST: VPNINSTANCE ="vpn_pdn";
```

//配置Gi接口：

//1.配置Giif1/0/0接口。

```
ADD LOGICIP: IPVERSION=IPv4, LOGICIPV4="10.8.20.1", VPNINSTNAME="vpn_pdn";
ADD LOGICINF:NAME="giif1/0/0",IPVERSION=IPV4,IPV4ADDRESS1="10.8.20.1",IPV4MASK1="255.255.255.255",VPNINSTANCE="vpn_pdn";
```

//2.配置Giif1/0/1接口。

```
ADD LOGICIP: IPVERSION=IPv4, LOGICIPV4="10.8.20.2", VPNINSTNAME="vpn_pdn";
ADD LOGICINF:NAME="giif1/0/1",IPVERSION=IPV4,IPV4ADDRESS1="10.8.20.2",IPV4MASK1="255.255.255.255",VPNINSTANCE="vpn_pdn";
```

//配置UPF列表。

```
ADD UPLIST4RDS: UPLISTNAME="uplist1", UPINSTANCEID="up1";
ADD UPLIST4RDS: UPLISTNAME="uplist1", UPINSTANCEID="up2";
```

//配置鉴权/计费AAA服务器。

```
ADD RDSSVRGRP: RDSSVRGRPNAME="isprg", MODE=MASTER_SLAVE, SIGOPTACCTMSG=DISABLE;
```

```
ADD RDSSVR: RDSSVRGRPNAME="isprg", SERVERTYPE=AUTHENTICATION, IPVERSION=IPV4, SERVERIPV4="10.168.10.1", PORT=1812, VPNINSTANCE="vpn_pdn", CIPHERKEY="*****", PRIFLAG=PRIMARY, CIPHERKEYCNFM="*****"，UPLISTNAME="uplist1";
```

```
ADD RDSSVR: RDSSVRGRPNAME="isprg", SERVERTYPE=ACCOUNTING, IPVERSION=IPV4, SERVERIPV4="10.168.10.1", PORT=1813, VPNINSTANCE="vpn_pdn", CIPHERKEY="*****", PRIFLAG=PRIMARY, CIPHERKEYCNFM="*****"，UPLISTNAME="uplist1";
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
