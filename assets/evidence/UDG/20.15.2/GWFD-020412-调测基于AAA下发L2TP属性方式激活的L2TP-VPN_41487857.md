# 调测基于AAA下发L2TP属性方式激活的L2TP VPN

- [操作场景](#ZH-CN_OPI_0241487857__1.3.1)
- [必备事项](#ZH-CN_OPI_0241487857__1.3.2)
- [操作流程](#ZH-CN_OPI_0241487857__1.3.3)
- [操作步骤](#ZH-CN_OPI_0241487857__1.3.4)

## [操作场景](#ZH-CN_OPI_0241487857)

配置AAA下发L2TP属性方式启用L2TP隧道后，需要执行本任务，检查L2TP隧道是否正常工作。

> **说明**
> 适用于PGW-U、UPF。

## [必备事项](#ZH-CN_OPI_0241487857)

前提条件

- UDG 的L2TP配置已经完成，请参见 [AAA下发L2TP属性方式激活L2TP VPN](../激活L2TP VPN/AAA下发L2TP属性方式激活L2TP VPN_41487855.md) 。
- AAA Server上的L2TP配置已经完成。

数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| ping数据包 | VPN实例名（VPNINSTANCE） | vpn_12tp | 已配置数据中获取 | [**ADD VPNINST**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/DN管理/VPN管理/VPN/增加VPN实例（ADD VPNINST）_82837045.md) |
| ping数据包 | 逻辑接口的IPv4地址1(IPV4ADDRESS1) | 10.8.20.2 | 已配置数据中获取 | [**ADD LOGICINF**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/DN管理/逻辑接口管理/逻辑接口配置/接口/增加逻辑接口（ADD LOGICINF）_82835378.md) |
| ping数据包 | 第一个LNS IP地址（FIRSTLNSIP） | 10.10.10.1 | 已配置数据中获取 | 取自AAA Server下发的LNS host。 |
| 接口配置信息 | 逻辑接口名称（NAME） | giif1/0/0 | 已配置数据中获取 | [**ADD LOGICINF**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/DN管理/逻辑接口管理/逻辑接口配置/接口/增加逻辑接口（ADD LOGICINF）_82835378.md) |
| 测试终端使用的APN | APN名称（APN） | apn-l2tp | 已配置数据中获取 | 用户激活使用的APN，取自接入配置中的APN实例名。可以使用<br>[查询APN配置（LST APN）](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/DN管理/APN管理/APN/查询APN配置（LST APN）_82837017.md)<br>命令进行查询。 |
| L2TP用户信息 | MSISDN | 8613801040032 | 测试终端自带 | - |

工具

OM Portal跟踪工具

## [操作流程](#ZH-CN_OPI_0241487857)

该任务操作流程如 [图1](#ZH-CN_OPI_0241487857__fig168581147104515) 所示。

**图1** L2TP隧道调测流程

<br>

![](调测基于AAA下发L2TP属性方式激活的L2TP VPN_41487857.assets/zh-cn_image_0241818184.png)

## [操作步骤](#ZH-CN_OPI_0241487857)

1. 执行 [**LST LICENSESWITCH**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09587900.md) 命令查询 UDG 上本功能对应的License配置开关是否打开。
  ```
  LST LICENSESWITCH:LICITEM="LKV3G5L2TP01";
  ```
    - 如果“SWITCH”为“ENABLE”，请执行[步骤 2](#ZH-CN_OPI_0241487857__step86965143117)。
    - 如果“SWITCH”为“DISABLE”，则执行[**SET LICENSESWITCH**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09587387.md)命令打开本特性对应的License配置开关。
2. 在OM Portal上创建Gi接口跟踪任务，在“参数配置”栏输入需要跟踪的Gi逻辑接口名称，选择PPP和L2TP消息类型。并创建 [UDG N4接口跟踪](../../../../../../网络运维/日常维护/UDG基础运维操作/创建消息跟踪/创建接口跟踪/UDG N4接口跟踪_88792205.md) 任务。
3. L2TP用户入网，查看Gi接口跟踪任务，检查是否能跟踪到 UDG 与LNS之间的IPCP报文， UDG 是否收到了LNS响应的Ipcp Configure Ack消息。
    - 如果L2TP用户业务正常，Gi接口能跟踪到UDG与LNS之间的IPCP报文，请执行[步骤 4](#ZH-CN_OPI_0241487857__step186541131103215)。
    - 如果L2TP用户业务无法进行，Gi接口跟踪不到UDG与LNS之间的IPCP报文，请执行[步骤 5](#ZH-CN_OPI_0241487857__step8999143514379)。
4. 执行 [**DSP L2TPSESSION**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/会话管理/L2TP隧道管理/L2TP会话查询/查询L2TP隧道下L2TP会话相关信息（DSP L2TPSESSION）_35373531.md) 命令，查看用户的L2TP会话是否建立成功。
  ```
  DSP L2TPSESSION: INTERFACENAME="giif1/0/1",TUNNELID=1,SESSIONID=2;
  ```
  ```
  -----------------
            对端名称  =  NULL
            L2TP组号  =  1
          本端隧道ID  =  1
          对端隧道ID  =  2
          对端IP地址  =  10.10.10.1
          对端端口号  =  1701
              会话数  =  1
        Giif接口名称  =  Giif1/0/0 
      Giif接口IP地址  =  10.8.20.1
            创建时长  =  0 days, 0 hours, 4 minutes
          本端会话ID  =  2
   远端（LNS）会话ID  =  102
          用户MSISDN  =  8613801040032 
  (结果个数 = 1)
  ```
    - 如果L2TP会话建立成功，且其“MSISDN”与L2TP用户一致，L2TP组网正常，调测结束。
    - 如果L2TP会话建立失败，请执行 [步骤 5](#ZH-CN_OPI_0241487857__step8999143514379) 。
5. 执行 [**DSP L2TPTUNNEL**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/会话管理/L2TP隧道管理/L2TP隧道查询/查询L2TP隧道的相关信息（DSP L2TPTUNNEL）_35373529.md) 命令，查看L2TP隧道是否建立成功。
  ```
  DSP L2TPTUNNEL: SHOWTYPE=INTERFACE,INTERFACENAME="giif1/0/1",TUNNELID=1;
  ```
  ```
  -------------------------
         对端名称  =  NULL
         L2TP组号  =  1
       本端隧道ID  =  1
       对端隧道ID  =  2
       对端IP地址  =  10.10.10.1
       对端端口号  =  1701
           会话数  =  1
     Giif接口名称  =  Giif1/0/0
   Giif接口IP地址  =  10.8.20.1
         创建时长  =  0 days, 0 hours, 1 minutes 
  (结果个数 = 1)
  ```
    - 如果L2TP隧道建立成功，请执行 [步骤 13](#ZH-CN_OPI_0241487857__step153431333171) 。
    - 如果L2TP隧道建立失败，请执行 [步骤 6](#ZH-CN_OPI_0241487857__step432201415173) 。
6. 检查N4接口跟踪任务，PGW-C/SMF在PFCP Session Establishment Request消息中为PGW-U/UPF下发的L2TP属性值与规划是否一致。
    - 一致，请执行[步骤 8](#ZH-CN_OPI_0241487857__step4289537134120)。
    - 不一致，请执行[步骤 7](#ZH-CN_OPI_0241487857__step8980191914222)。
7. 请求修改AAA上的配置后再次执行 [步骤 3](#ZH-CN_OPI_0241487857__step166471454162915) 。
    - 问题解决，调测结束。
    - 问题未解决，请执行[步骤 8](#ZH-CN_OPI_0241487857__step4289537134120)。
8. 执行 [**PING**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/系统管理/系统维护/Ping和Tracert/Ping/IP Ping（PING）_16499685.md) 命令，在 UDG 上以Giif接口为源地址，向对端LNS的接口IP发起ping诊断，使用 [**PING**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/系统管理/系统维护/Ping和Tracert/Ping/IP Ping（PING）_16499685.md) 查询ping结果，查看 UDG 到LNS是否正常连通。
  ![](调测基于AAA下发L2TP属性方式激活的L2TP VPN_41487857.assets/notice_3.0-zh-cn.png)

  在检测隧道时，请务必使用指定源地址SOURCEIPV4ADDRESS为 UDG 逻辑接口的IP地址（该地址是隧道对端网元配置隧道路由时使用的报文入口地址），这样才能验证L2TP隧道是否建立成功。

  如果接口绑定了VPN实例，还需要使用指定VPN实例名称VPNNAME，这样才能验证VPN实例路由是否正常。
  ```
  PING: IPVERSION=IPv4, VPNNAME=vpn_12tp, SOURCEIPV4ADDRESS=10.8.20.2, DESTIPV4ADDRESS="10.10.10.1";
  ```
    - 如果收到对端网元的响应，表明连接正常，请执行 [步骤 12](#ZH-CN_OPI_0241487857__step12214545865) 。
    - 如果连接出现timeout，表明链路不通，请执行 [步骤 9](#ZH-CN_OPI_0241487857__step53541837174517) 。
9. 执行 [**DSP ROUTE**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/路由基础/IPv4路由表/显示IPv4路由表（DSP ROUTE）_00441129.md) 命令，查看 UDG 到LNS的路由是否正确。
  ```
  DSP ROUTE:VRFNAME="vpn_12tp",PREFIX="10.10.10.1";
  ```
  > **说明**
  > 查询结果中的 *路由接口名字* 需要在 [步骤 9](调测基于本地配置方式激活的L2TP VPN_40342150.md#ZH-CN_OPI_0240342150__step72824504505) 中使用。
    - 如果路由信息正确，请执行 [步骤 13](#ZH-CN_OPI_0241487857__step153431333171) 。
    - 如果没有配置到LNS的路由或路由配置错误，请执行 [步骤 10.a](#ZH-CN_OPI_0241487857__substep18655111025016) 。
10. 重新配置路由。
    a. 执行 [**ADD SRROUTE**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/静态路由管理/IPv4静态路由/增加IPv4静态路由（ADD SRROUTE）_49961498.md) 或 [**MOD SRROUTE**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/静态路由管理/IPv4静态路由/修改IPv4静态路由（MOD SRROUTE）_49962042.md) 命令，配置或修改原有到LNS的路由。
    b. 配置完成后再次执行 [步骤 8](#ZH-CN_OPI_0241487857__step4289537134120) ，查看链路是否Ping通。
    - 如果可以Ping通，说明到对端网元的链路正常，请执行[步骤 12](#ZH-CN_OPI_0241487857__step12214545865)。
    - 如果不能Ping通，请执行[步骤 11](#ZH-CN_OPI_0241487857__step72824504505)。
11. 执行 [**LST LOGICINF**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/DN管理/逻辑接口管理/逻辑接口配置/接口/查询逻辑接口（LST LOGICINF）_86526672.md) 和 [**LST INTERFACE**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/接口管理/接口配置/查询接口（LST INTERFACE）_49801850.md) 命令，查询Giif逻辑接口与路由的出接口是否处于同一VPN实例中。
  ```
  LST LOGICINF:NAME="giif1/0/0";
  ```
  ```
  RETCODE = 0  操作成功。
  
  逻辑接口信息 ------------
              逻辑接口名称  =  giif1/0/1
       逻辑接口的IPv4地址1  =  10.8.20.2
       逻辑接口的IPv4掩码1  =  255.255.255.255
   IPv4逻辑接口MTU（字节）  =  1500
               VPN实例名称  =  vpn_l2tp
          逻辑接口的IP版本  =  IPv4
                          ...... 
  (结果个数 = 1) 
  ---    END
  ```
  ```
  LST INTERFACE:IFNAME = "Ethernet64/0/3";
  ```
  ```
  RETCODE = 0  操作成功  
  结果如下 
  -------------------------
                  接口名  =  Ethernet64/0/3
                接口类别  =  主接口
                接口类型  =  Ethernet 
                接口编号  =  64/0/3 
                接口描述  =  NULL
                管理状态  =  up
        接口最大传输单元  =  1500
             接口MAC地址  =  0000-0000-0000
             VPN实例名称  =  vpn_l2tp
                       ...... 
  (结果个数 = 1)  
  ---   END
  ```
    - 如果Giif接口与路由的出接口处于相同的VPN实例中，请执行 [步骤 13](#ZH-CN_OPI_0241487857__step153431333171) 。
    - 如果Giif接口与路由的出接口处于不同的VPN实例中，请参考配置数据表，使用 [**MOD LOGICINF**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/DN管理/逻辑接口管理/逻辑接口配置/接口/修改逻辑接口（MOD LOGICINF）_86526348.md) 命令更改接口的VPN实例配置，使Giif接口与路由的出接口处于相同的VPN实例中，然后重新执行 [步骤 3](#ZH-CN_OPI_0241487857__step166471454162915) 。
12. 执行 [**LST APNL2TPATTR**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/会话管理/L2TP隧道管理/APN的L2TP属性/查询APN L2TP配置（LST APNL2TPATTR）_35373519.md) 命令，查询APN实例中L2TP的配置是否正确。
  ```
  LST APNL2TPATTR:APN="apn-l2tp";
  ```
    - 如果APN实例没有使能L2TP功能，请执行 [**SET APNL2TPATTR**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/会话管理/L2TP隧道管理/APN的L2TP属性/设置APN L2TP配置（SET APNL2TPATTR）_35373518.md) 命令，使能APN实例的L2TP功能。然后重新执行 [步骤 3](#ZH-CN_OPI_0241487857__step166471454162915) 。
    - 如果APN中L2TP使能，请执行 [步骤 13](#ZH-CN_OPI_0241487857__step153431333171) 。
13. 收集信息并寻求技术支持。
    a. 在OM Portal上创建Gi接口跟踪任务，执行 [步骤 3](调测基于本地配置方式激活的L2TP VPN_40342150.md#ZH-CN_OPI_0240342150__step166471454162915) 并保存报文。
    b. 执行 [**EXP MML**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/操作维护/配置管理/配置导出管理/导出MML文件（EXP MML）_47200033.md) 命令将当前配置数据导出为MML脚本文件并保存。
    c. 执行 [**DSP ROUTE**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/路由基础/IPv4路由表/显示IPv4路由表（DSP ROUTE）_00441129.md) 命令查看当前路由信息并保存查询结果。
    d. 执行 [**LST INTERFACE**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/接口管理/接口配置/查询接口（LST INTERFACE）_49801850.md) 命令查看当前接口信息并保存查询结果。
    e. 查看并收集对端设备配置及接口状态信息。
    f. 收集归纳所有信息并联系华为技术支持解决。
