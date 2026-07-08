# 调测到AAA Server的数据

- [操作场景](#ZH-CN_OPI_0232027181__1.3.1)
- [必备事项](#ZH-CN_OPI_0232027181__1.3.2)
- [操作步骤](#ZH-CN_OPI_0232027181__1.3.3)

## [操作场景](#ZH-CN_OPI_0232027181)

当运营商在部署分组交换网，新增 UNC 或AAA Server时， UNC 和AAA Server完成互通数据配置后，需要检查 UNC 与AAA Server之间的链路是否连通。

> **说明**
> 适用于 GGSN、 PGW-C、SMF。

## [必备事项](#ZH-CN_OPI_0232027181)

前提条件

- 请仔细阅读[WSFD-011306 Radius功能特性概述](特性概述_31467848.md)。
- 完成[配置RADIUS功能](激活RADIUS功能/配置RADIUS功能_32909765.md)。
- AAA Server上已经完成相应配置，并确保已配置到 UNC 的回程路由。

数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| **[TST AAA](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/RADIUS管理/RADIUS维护/服务器检测/测试AAA服务器（TST AAA）_09896762.md)** | 服务器IP地址（IPADDRESS） | 10.1.128.23 | 与对端协商 | AAA Server的IP地址。 |
| **[TST AAA](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/RADIUS管理/RADIUS维护/服务器检测/测试AAA服务器（TST AAA）_09896762.md)** | VPN实例名（VPNINSTANCE） | test_vpn | 本端规划 | AAA Server的VPN实例。 |
| **[TST AAA](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/RADIUS管理/RADIUS维护/服务器检测/测试AAA服务器（TST AAA）_09896762.md)** | 服务器类型（SERVERTYPE） | ACCOUNTING | 本端规划 | 选择发送鉴权或计费探测消息。 |
| **[TST AAA](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/RADIUS管理/RADIUS维护/服务器检测/测试AAA服务器（TST AAA）_09896762.md)** | 用户名（USERNAME） | hello | 本端规划 | 探测消息中携带的用户名。 |
| **[TST AAA](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/RADIUS管理/RADIUS维护/服务器检测/测试AAA服务器（TST AAA）_09896762.md)** | 密码（PASSWORD） | hello | 本端规划 | 探测消息中携带的密码。 |
| **[ADD RDSSVRGRP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/RADIUS管理/连接管理/Radius服务器组/增加Radius服务器组（ADD RDSSVRGRP）_09896730.md)** | Radius Server Group名称（RDSSVRGRPNAME） | groupggsn | 本端规划 | - |
| **[**DSP ROUTE**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/路由基础/IPv4路由表/显示IPv4路由表（DSP ROUTE）_00441129.md)** | 路由下一跳（NEXTHOP） | 10.168.10.1 | 与对端协商 | AAA Server的IP地址。 |
| **[**DSP ROUTE**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/路由基础/IPv4路由表/显示IPv4路由表（DSP ROUTE）_00441129.md)** | 路由前缀（PREFIX） | 10.8.20.1 | 已配置数据中获取 | UNC<br>与AAA Server互通使用的Gi接口IP地址。 |
| **[**DSP ROUTE**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/路由基础/IPv4路由表/显示IPv4路由表（DSP ROUTE）_00441129.md)** | 路由VPN名字（VRFNAME） | vpn_Gi | 已配置数据中获取 | VPN组网时使用的VPN实例名称。 |

工具

该操作无需准备其他工具

## [操作步骤](#ZH-CN_OPI_0232027181)

1. 在窗口上 执行 **[TST AAA](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/RADIUS管理/RADIUS维护/服务器检测/测试AAA服务器（TST AAA）_09896762.md)** 命令，调测 UNC 到AAA Server的数据通信。
  ```
  TST AAA: SERVERTYPE=ACCOUNTING, IPVERSION=IPV4, IPADDRESS="10.1.128.23";
  TST AAA: SERVERTYPE=AUTHENTICATION, VPNINSTANCE="test_vpn", IPVERSION=IPV4, IPADDRESS="10.1.128.23";
  ```
    - 如果返回检测成功消息，表明通信正常，调测结束。
    - 如果检测无响应消息，请执行[步骤 2](#ZH-CN_OPI_0232027181__step2)。
2. 执行 **[NGPING](../../../../../OM参考/命令/UNC MML命令/平台服务管理/IP管理/IP维护/NGPING（NGPING）_09587930.md)** 命令，查看 UNC 到AAA Server的连接是否正常。
  > **说明**
  > 在执行命令时，请务必指定源地址 **“** **SRCIPV4ADDR** **”** 为 UNC 的Gi接口IP地址，这样才能验证逻辑链路是否正常，否则只能检查两端的物理连接是否正常（IPv6地址同理）。
  >
  > 如果使用了VPN组网，还需指定VPN实例名称 **“** **VPNNAME** **”** ，这样才能验证VPN实例路由是否正常。
    - 如果收到对端网元的响应，表明连接正常，请执行[步骤 3](#ZH-CN_OPI_0232027181__step3)。
    - 如果连接出现timeout，表明链路不通，请执行[步骤 4](#ZH-CN_OPI_0232027181__step4)。
3. 执行 **[LST RDSSVRGRP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/RADIUS管理/连接管理/Radius服务器组/查询Radius服务器组（LST RDSSVRGRP）_09896733.md)** 命令，查看 UNC 上AAA服务器组的配置是否和规划值及AAA Server的配置一致，查看相应Radius-Server Group和APN的绑定关系是否已经配置完成。
  > **说明**
  > UNC 上配置的AAA Server的IP地址、端口、Key必须和AAA Server网元配置的一致。
    - 如果配置与AAA Server一致，请执行[步骤 5](#ZH-CN_OPI_0232027181__step5)。
    - 如果配置AAA Server不一致，请参考[激活RADIUS功能](激活RADIUS功能_15542173.md)重新配置鉴权/计费AAA Server。
4. 检查 UNC 到AAA Server的互通是否正常。
    a. 根据使用的路由方式，调测 UNC 到AAA Server的路由。
    b. 根据使用的可靠性组网方式，调测 UNC 到AAA Server的组网。
    c. 根据使用的VPN组网方式，调测 UNC 到AAA Server的VPN组网。
    d. 再次执行 [步骤 1](#ZH-CN_OPI_0232027181__step1) ，检查 UNC 到AAA Server的数据通信。
          - 如果返回检测成功消息，表明连接正常，调测结束。
          - 如果返回检测失败消息，请执行[步骤 5](#ZH-CN_OPI_0232027181__step5)。
5. 查看是否存在ID为 “100197” （RADIUS鉴权服务器无响应告警）或 “81020” （RADIUS计费服务器无响应告警）的告警。
    - 如果产生告警，请参考[ALM-100197 RADIUS鉴权服务器无响应](../../../../../网络运维/故障处理/UNC告警处理/业务告警/SMF&GW-C&GGSN/ALM-100197 RADIUS鉴权服务器无响应_39047078.md)或[ALM-81020 RADIUS计费服务器无响应](../../../../../网络运维/故障处理/UNC告警处理/业务告警/SMF&GW-C&GGSN/ALM-81020 RADIUS计费服务器无响应_13767441.md)处理步骤解决。
    - 如果没有产生告警，请执行[步骤 6](#ZH-CN_OPI_0232027181__step1829245425110)。
6. 收集信息并寻求技术支持。
    a. 执行 **[EXP MML](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/配置管理/配置导出管理/导出MML文件（EXP MML）_47200033.md)** 命令将当前配置数据导出为MML脚本文件并保存。
    b. 收集并保存上述所有查询信息。
    c. 收集归纳所有信息并联系华为技术支持解决。
