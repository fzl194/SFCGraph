# 调测到Untrusted Non-3GPP GW的数据

- [操作场景](#ZH-CN_OPI_0270759400__1.3.1)
- [必备事项](#ZH-CN_OPI_0270759400__1.3.2)
- [操作步骤](#ZH-CN_OPI_0270759400__1.3.3)

## [操作场景](#ZH-CN_OPI_0270759400)

当运营商在部署分组交换网，新增 UDG 或Untrusted Non-3GPP GW时， UDG 和Untrusted Non-3GPP GW完成互通数据配置后，需要通过调试手段检查 UDG 与Untrusted Non-3GPP GW之间的链路是否连通。

> **说明**
> 适用于PGW-U。

## [必备事项](#ZH-CN_OPI_0270759400)

前提条件

- 请仔细阅读[GWFD-010155 Untrusted Non-3GPP网络用户接入](../GWFD-010155 Untrusted Non-3GPP网络用户接入_70759396.md)。
- 完成[激活Untrusted Non-3GPP网络用户接入功能](激活Untrusted Non-3GPP网络用户接入功能_70759399.md)。
- Untrusted Non-3GPP GW上已完成相应配置，并确保已配置到UDG的回程路由。

数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| [**TST PATH**](../../../../../OM参考/命令/UDG MML命令/用户面服务管理/路径管理/GTP路径管理/GTP路径测试/探测路径/探测路径（TST PATH）_82837231.md) | IP地址版本类型（IPVERSION） | IPV4 | 本端规划 | GTP<br>路径检测<br>说明：到Untrusted Non-3GPP GW数据业务的连通性采用GTPv1协议进行检测。 |
| [**TST PATH**](../../../../../OM参考/命令/UDG MML命令/用户面服务管理/路径管理/GTP路径管理/GTP路径测试/探测路径/探测路径（TST PATH）_82837231.md) | 本端IPv4地址（LOCALIPV4） | 10.8.10.1 | 已配置数据中获取 | GTP<br>路径检测<br>说明：到Untrusted Non-3GPP GW数据业务的连通性采用GTPv1协议进行检测。 |
| [**TST PATH**](../../../../../OM参考/命令/UDG MML命令/用户面服务管理/路径管理/GTP路径管理/GTP路径测试/探测路径/探测路径（TST PATH）_82837231.md) | 对端IPv4地址（PEERIPV4） | 172.16.47.0 | 对端获取 | GTP<br>路径检测<br>说明：到Untrusted Non-3GPP GW数据业务的连通性采用GTPv1协议进行检测。 |
| [**TST PATH**](../../../../../OM参考/命令/UDG MML命令/用户面服务管理/路径管理/GTP路径管理/GTP路径测试/探测路径/探测路径（TST PATH）_82837231.md) | VPN名字（VPNNAME） | vpn-s2b | 已配置数据中获取 | GTP<br>路径检测<br>说明：到Untrusted Non-3GPP GW数据业务的连通性采用GTPv1协议进行检测。 |
| [**TST PATH**](../../../../../OM参考/命令/UDG MML命令/用户面服务管理/路径管理/GTP路径管理/GTP路径测试/探测路径/探测路径（TST PATH）_82837231.md) | 协议版本（PROTOCOLTYPE） | GTPV1 | 本端规划 | GTP<br>路径检测<br>说明：到Untrusted Non-3GPP GW数据业务的连通性采用GTPv1协议进行检测。 |
| [**TST PATH**](../../../../../OM参考/命令/UDG MML命令/用户面服务管理/路径管理/GTP路径管理/GTP路径测试/探测路径/探测路径（TST PATH）_82837231.md) | 路径类型（PATHTYPE） | SIGNAL_PATH | 本端规划 | GTP<br>路径检测<br>说明：到Untrusted Non-3GPP GW数据业务的连通性采用GTPv1协议进行检测。 |
| [**PING**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/系统管理/系统维护/Ping和Tracert/Ping/IP Ping（PING）_16499685.md) | IP协议版本号（IPVERSION） | IPv4 | 本端规划 | UDG<br>上S2b抽象接口的IP地址。 |
| [**PING**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/系统管理/系统维护/Ping和Tracert/Ping/IP Ping（PING）_16499685.md) | 源IPv4地址（SOURCEIPV4ADDRESS） | 10.8.10.1 | 对端获取 | UDG<br>上S2b抽象接口的IP地址。 |
| [**PING**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/系统管理/系统维护/Ping和Tracert/Ping/IP Ping（PING）_16499685.md) | 目的IPv4地址（DESTIPV4ADDRESS） | 172.16.47.0 | 从已配置数据中获取 | UDG<br>上S2b抽象接口的IP地址。 |
| [**PING**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/系统管理/系统维护/Ping和Tracert/Ping/IP Ping（PING）_16499685.md) | VPN实例名称（VPNNAME） | vpn_s2b | 从已配置数据中获取 | UDG<br>上S2b抽象接口的IP地址。 |

工具

无。

## [操作步骤](#ZH-CN_OPI_0270759400)

1. 执行 [**TST PATH**](../../../../../OM参考/命令/UDG MML命令/用户面服务管理/路径管理/GTP路径管理/GTP路径测试/探测路径/探测路径（TST PATH）_82837231.md) 命令，调测 UDG 到Untrusted Non-3GPP GW的数据通信路径。
  ```
  TST PATH:IPVERSION=IPV4,LOCALIPV4="10.8.10.1",PEERIPV4="172.16.47.0",PROTOCOLTYPE=GTPV1;
  ```
    - 如果返回检测成功消息，表明通信正常，调测结束。
    - 如果检测无响应消息，请执行[步骤 2](#ZH-CN_OPI_0270759400__step2)。
2. 执行 [**LST UPGTPPATH**](../../../../../OM参考/命令/UDG MML命令/用户面服务管理/路径管理/GTP路径管理/GTP协议参数管理/GTP路径全局参数/查询路径相关属性（LST UPGTPPATH）_82837228.md) 命令，查看 UDG 上配置的Echo消息开关是否打开。
  ```
  LST UPGTPPATH:;
  ```
  ```
  RETCODE = 0  操作成功。  
  GTP路径配置 
  ----------- 
                                        V0 Echo开关  =  使能
                                 V1数据路径Echo开关  =  使能 
                          发送GTP心跳请求的间隔时间  =  60
                          GTP请求消息的重发时间间隔  =  3
                      GTP请求消息的最大尝试发送次数  =  5
                       是否去活路径上已激活的上下文  =  使能
                     路径断告警后发送心跳消息的次数  =  30
                                      EchoList 开关  =  不使能
                                      EchoList 类型  =  黑名单
                                           
  (结果个数 = 1)
  ---    END
  ```
    - 如果V1数据路径Echo开关设置为使能，请执行[步骤 4](#ZH-CN_OPI_0270759400__step4)。
    - 如果V1数据路径Echo开关设置为不使能，请参考[配置GTP/PFCP路径管理参数](../GWFD-010102 路径管理/配置GTP_PFCP路径管理参数_24082055.md)重新配置。
3. 执行 [**PING**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/系统管理/系统维护/Ping和Tracert/Ping/IP Ping（PING）_16499685.md) 命令，查看 UDG 到Untrusted Non-3GPP GW的连接是否正常。
  ```
  PING:IPVERSION=IPv4,VPNNAME="vpn-s2b",DESTIPV4ADDRESS="172.16.47.0",SOURCEIPV4ADDRESS="10.8.10.1";
  ```
  > **说明**
  > - 在执行命令时，请务必指定源地址为UDG的S2b接口IP地址，这样才能验证逻辑链路是否正常，否则只能检查两端的物理连接是否正常。
  > - 如果使用了VPN组网，需要指定VPN实例名称，这样才能验证VPN实例路由是否正常。
    - 如果收到对端网元的响应，表明连接正常，请执行[步骤 5](#ZH-CN_OPI_0270759400__step5)。
    - 如果连续出现timeout，表明链路不通，请执行[步骤 4](#ZH-CN_OPI_0270759400__step4)。
4. 检查 UDG 到Untrusted Non-3GPP GW的互通是否正常。
    a. 根据使用的路由方式，调测 UDG 到Untrusted Non-3GPP GW的路由。
    b. 根据使用的可靠性组网方式，调测 UDG 到Untrusted Non-3GPP GW的组网。
    c. 再次执行 [步骤 1](#ZH-CN_OPI_0270759400__step1) ，检查 UDG 到Untrusted Non-3GPP GW的数据和信令通信。
          - 如果返回检测成功消息，表明连接正常，调测结束。
          - 如果返回检测失败消息，请执行[步骤 6](#ZH-CN_OPI_0270759400__step153431333171)。
5. 查看是否存在ID为 “81018” （GTPU路径断）。
    - 如果产生告警，请参考[ALM-81018 GTPU路径断](../../../../../网络运维/故障处理/用户面告警/ALM-81018 GTPU路径断_93246969.md)处理步骤解决。
    - 如果没有产生告警，请执行[步骤 6](#ZH-CN_OPI_0270759400__step153431333171)。
6. 收集信息并寻求技术支持。
    a. 执行 [**EXP MML**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/操作维护/配置管理/配置导出管理/导出MML文件（EXP MML）_47200033.md) 命令将当前配置数据导出为MML脚本文件并保存。
    b. 查看并收集对端设备配置及接口状态信息。
    c. 收集归纳所有信息并联系华为技术支持解决。
