# 调测Gx over DRA

- [操作场景](#ZH-CN_OPI_0229578142__1.3.1)
- [必备事项](#ZH-CN_OPI_0229578142__1.3.2)
- [操作步骤](#ZH-CN_OPI_0229578142__1.3.3)

## [操作场景](#ZH-CN_OPI_0229578142)

当运营商在部署分组交换网，新增 GGSN/PGW-C 或DRA时， GGSN/PGW-C 和DRA完成互通数据配置后，需要通过调试手段检查 GGSN/PGW-C 与DRA之间的链路是否连通。如果 GGSN/PGW-C 与DRA之间的链路不通，则运营商无法应用Gx over DRA的PCC功能，导致相关的PCC用户无法激活，或者只能采用非PCC的方式激活。

> **说明**
> 适用于 GGSN、 PGW-C。

## [必备事项](#ZH-CN_OPI_0229578142)

前提条件

- 请仔细阅读 [WSFD-011132 Gx over DRA特性概述](特性概述_29315043.md) 。
- 完成[激活Gx over DRA（静态路由+BFD组网）](激活Gx over DRA（静态路由+BFD组网）_29368407.md)。
- DRA和PCRF上已完成相应配置，并确保已配置到 GGSN/PGW-C 的回程路由。

数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| DRA信息 | 主机名（HOSTNAME） | host1.example.com<br>host2.example.com | 已配置数据中获取 | 取自<br>[激活Gx over DRA（静态路由+BFD组网）](激活Gx over DRA（静态路由+BFD组网）_29368407.md)<br>中配置的数据。 |
| Gx interface | 逻辑接口名称（NAME） | gxif1/0/0 | 已配置数据中获取 | 取自<br>[激活Gx over DRA（静态路由+BFD组网）](激活Gx over DRA（静态路由+BFD组网）_29368407.md)<br>中配置的数据。 |

工具

OM Portal

## [操作步骤](#ZH-CN_OPI_0229578142)

1. 启动OM Portal，指定下一跳DRA的IP地址创建Gx接口跟踪。
2. 跟踪Gx接口消息，观察Gx接口上是否存在Gx接口到DRA之间交互的CER和CEA消息。
    - 如果Gx接口消息存在从GGSN/PGW-C到DRA的CER消息和DRA响应的CEA消息，则调测结束。
    - 如果Gx接口消息只有从GGSN/PGW-C到DRA的CER消息，而没有收到DRA的CEA消息，请执行[步骤 3](#ZH-CN_OPI_0229578142__stp1)。
3. 执行 [**DSP DRASTATUS**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/DRA管理/DRA状态/显示DRA状态（DSP DRASTATUS）_09897296.md) 命令，查看DRA的链路组状态是否正常。
  ```
  DSP DRASTATUS:;
  ```
  ```
  ......

  -------------------------
  DRA主机名                POD名称                    本端地址            本端子地址            对端地址           正常链路      异常链路 
  host1.example.com       uncpod-0116-30-0-195       10.8.10.1:16401      -                    10.10.10.1:3868    gx             - 
  host1.example.com       uncpod-0116-30-0-195       10.8.10.1:16401      -                    10.10.10.2:3868    gx             -      
  host2.example.com       uncpod-0116-30-0-195       10.8.10.1:16402      10.8.10.2:16402      endpoint0          gx             -  
  host2.example.com       uncpod-0116-30-0-195       10.8.10.1:16402      10.8.10.2:16402      endpoint1          gx             -         
  (Number of results = 2)
  ---    END
  ```
    - 如果检测DRA的链路组状态正常，则GGSN/PGW-C和DRA之间的链路互通调测结束。
    - 如果检测DRA的链路组状态异常，请执行[步骤 4](#ZH-CN_OPI_0229578142__stp2)。
4. 执行 [**LST DRA**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/DRA管理/DRA信息/查询DRA（LST DRA）_09897294.md) 和 **[LST DIAMPEERADDR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/查询Diameter对端地址（LST DIAMPEERADDR）_09897259.md)** 命令，查看GGSN/PGW-C上的DRA设备标识是否和规划值及DRA上的配置一致。
  ```
  LST DRA:;
  ```
  ```
  ......

  -------------------------
  主机名                  VPN实例         DSCP值    
  host1.example.com       vpn_gxif        46         
  host2.example.com       vpn_gxif        46        
  (结果个数 = 2)
  ---    END
  ```
  ```
  LST DIAMPEERADDR:;
  ```
  ```
  ......

  --------------------
  主机名称             地址类型         IP地址           端口号         SCTP端点名称 
  host1.example.com    IPv4             10.10.10.1       3868           NULL               
  host1.example.com    IPv4             10.10.10.2       3868           NULL               
  host2.example.com    SCTP             10.0.0.1         0              endpoint0          
  host2.example.com    SCTP             10.0.0.2         0              endpoint1          
  (结果个数 = 4)
  ---    END
  ```
    - 如果配置一致，请执行[步骤 6](#ZH-CN_OPI_0229578142__stp4)。
    - 如果配置不一致，请执行[步骤 5](#ZH-CN_OPI_0229578142__stp3)。
5. 修改 GGSN/PGW-C 上DRA设备标识。
    a. 执行 **[RMV DRA](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/DRA管理/DRA信息/删除DRA（RMV DRA）_09897293.md)** 命令，删除原有配置。
    b. 执行 **[ADD DRA](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/DRA管理/DRA信息/增加DRA（ADD DRA）_09897291.md)** 命令，按照规划数据和DRA上的数据重新配置 GGSN/PGW-C 的DRA信息。
    c. 再次执行 [步骤 2](#ZH-CN_OPI_0229578142__stp0) ，查看DRA的链路组状态。
    - 如果检测DRA的链路组状态正常，则GGSN/PGW-C和DRA之间的链路互通调测结束。
    - 如果检测DRA的链路组状态异常，请执行[步骤 6](#ZH-CN_OPI_0229578142__stp4)。
6. 执行 **[LST DIAMLOCINFO](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter本端信息/查询Diameter本端信息（LST DIAMLOCINFO）_09897274.md)** 和 **[LST LOGICINF](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/查询逻辑接口（LST LOGICINF）_09896726.md)** 命令，查看 GGSN/PGW-C 的Gx口设备标识与IP等是否和规划值及DRA上的配置一致。
  ```
  LST DIAMLOCINFO:;
  ```
  ```
  ......

  -------------------------
  本端主机名   本端域名       产品名称    Vendor-Id AVP值    Firmware-RevisionAVP值    Origin-State-Id AVP    Supported-Vendor-Id AVP 
  unc_1        example1.com    unc        10415              0                         不使能                 不使能
  unc_2        example1.com    unc        10415              0                         不使能                 不使能
  (结果个数 = 2)
  ---    END
  ```
  ```
  LST LOGICINF: NAME="gxif1/0/0";
  ```
  ```
  ......

  -------------------------
             逻辑接口名称  =  gxif1/0/0
      逻辑接口的IPv4地址1  =  10.8.10.1
      逻辑接口的IPv4掩码1  =  255.255.255.255
      逻辑接口的IPv4地址2  =  10.8.10.2
      逻辑接口的IPv4掩码2  =  255.255.255.255
              VPN实例名称  =  vpn_gxif
   	               ......
  (结果个数 = 1)
  ---    END
  ```
    - 如果配置一致，请执行[步骤 11](#ZH-CN_OPI_0229578142__stp6)。
    - 如果配置不一致，请执行[步骤 7](#ZH-CN_OPI_0229578142__stp5)。
7. 修改 GGSN/PGW-C 的Gx口设备标识。
    a. 执行 **[RMV DIAMLOCINFO](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter本端信息/删除Diameter本端信息（RMV DIAMLOCINFO）_09897273.md)** 命令，删除原有配置。
    b. 执行 **[ADD DIAMLOCINFO](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter本端信息/增加Diameter本端信息（ADD DIAMLOCINFO）_09897271.md)** 命令，按照规划数据重新配置 GGSN/PGW-C 的Gx口设备标识。
    c. 再次执行 [步骤 2](#ZH-CN_OPI_0229578142__stp0) ，查看DRA的链路组状态。
          - 如果检测DRA的链路组状态正常，则GGSN/PGW-C和DRA之间的链路互通调测结束。
          - 如果检测DRA的链路组状态异常，请执行[步骤 8](#ZH-CN_OPI_0229578142__stp18)。
8. 执行 **[DSP DIAMRTSTATUS](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/路由管理/路由状态/显示Diameter Route状态（DSP DIAMRTSTATUS）_09897308.md)** 命令，查看Diameter路由状态。
  ```
  DSP DIAMRTSTATUS:;
  ```
  ```
  ......

  -------------------------
  Diameter域名       Diameter应用     RU名称      状态 
  pcrf.huawei.com    Gx               unc1        Normal 
  pcrf.huawei.com    Gx               unc2        Normal 
  (结果个数 = 2)
  ---    END
  ```
    - 如果Diameter路由状态正常，请执行[步骤 11](#ZH-CN_OPI_0229578142__stp6)。
    - 如果Diameter路由状态异常，请执行[步骤 9](#ZH-CN_OPI_0229578142__stp291)。
9. 执行 [**LST DIAMRTREALM**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/路由管理/Diameter路由/查询Diameter路由域名信息（LST DIAMRTREALM）_09897306.md) 和 [**LST DIAMRTNEXTHOP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/路由管理/Diameter路由配置/查询Diameter路由下一跳（LST DIAMRTNEXTHOP）_09897312.md) 命令，查询Diameter路由数据配置是否与规划值一致。
  ```
  LST DIAMRTREALM:;
  ```
  ```
  ......

  -------------------------
    Diameter域名名称  =  pcrf.huawei.com
        Diameter应用  =  Gx
        路由选择模式  =  主备
        Failover开关  =  禁止
        自动倒回开关  =  禁止
  (结果个数 = 1)
  ---    END
  ```
  ```
  LST DIAMRTNEXTHOP:REALMNAME="pcrf.huawei.com";
  ```
  ```
  ......

  -------------------------
  Diameter域名名称       Diameter应用      下一跳                 sequence

  pcrf.huawei.com        Gx                host1.example.com       1
  pcrf.huawei.com        Gx                host2.example.com       2      
  (结果个数 = 2)
  ---    END
  ```
    - 如果配置一致，请执行[步骤 11](#ZH-CN_OPI_0229578142__stp6)。
    - 如果配置不一致，请执行[步骤 10](#ZH-CN_OPI_0229578142__stp310)。
10. 修改 GGSN/PGW-C 上Diameter路由配置数据。
    a. 执行 [**RMV DIAMRTREALM**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/路由管理/Diameter路由/删除Diameter路由域名信息（RMV DIAMRTREALM）_09897305.md) 命令，删除原有配置。
    b. 执行 **[ADD DIAMRTREALM](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/路由管理/Diameter路由/增加Diameter路由域名信息（ADD DIAMRTREALM）_09897303.md)** 和 **[ADD DIAMRTNEXTHOP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/路由管理/Diameter路由配置/增加Diameter路由下一跳（ADD DIAMRTNEXTHOP）_09897310.md)** 命令，按照规划数据和DRA上的数据重新配置 GGSN/PGW-C 的Diameter路由。
    c. 再次执行 [步骤 2](#ZH-CN_OPI_0229578142__stp0) ，查看DRA的链路组状态。
          - 如果检测DRA的链路组状态正常，则GGSN/PGW-C和DRA之间的链路互通调测结束。
          - 如果检测DRA的链路组状态异常，请执行[步骤 11](#ZH-CN_OPI_0229578142__stp6)。
11. 检查 GGSN/PGW-C 到DRA的互通是否正常。
    a. 根据使用的路由方式，调测 GGSN/PGW-C 到DRA的路由。
    b. 根据使用的可靠性组网方式，调测 GGSN/PGW-C 到DRA的组网。
    c. 再次执行 [步骤 2](#ZH-CN_OPI_0229578142__stp0) ，查看DRA的链路组状态。
          - 如果检测DRA的链路组状态正常，则GGSN/PGW-C和DRA之间的链路互通调测结束。
          - 如果检测DRA的链路组状态异常，请执行[步骤 12](#ZH-CN_OPI_0229578142__step1829245425110)。
12. 收集信息并寻求技术支持。
    a. 执行 **[EXP MML](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/配置管理/配置导出管理/导出MML文件（EXP MML）_47200033.md)** 命令将当前配置数据导出为MML脚本文件并保存。
    b. 收集并保存上述所有查询信息。
    c. 收集归纳所有信息并联系华为技术支持解决。
