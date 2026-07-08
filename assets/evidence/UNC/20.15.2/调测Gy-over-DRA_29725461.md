# 调测Gy over DRA

- [操作场景](#ZH-CN_OPI_0229725461__1.3.1)
- [必备事项](#ZH-CN_OPI_0229725461__1.3.2)
- [操作步骤](#ZH-CN_OPI_0229725461__1.3.3)

## [操作场景](#ZH-CN_OPI_0229725461)

当运营商在部署分组交换网，新增 GGSN/PGW-C 或DRA时， GGSN/PGW-C 完成Gy over DRA功能配置后，需要通过调试手段检查 GGSN/PGW-C 与DRA之间是否能够正常交互Diameter消息。

> **说明**
> 适用于 GGSN、 PGW-C。

## [必备事项](#ZH-CN_OPI_0229725461)

前提条件

- 请仔细阅读 [WSFD-011133 Gy over DRA特性概述](特性概述_29725459.md) 。
- 完成[激活Gy over DRA（静态路由+BFD组网）](激活Gy over DRA（静态路由+BFD组网）_29725460.md)。
- DRA上已完成相应配置，并确保已配置到GGSN/PGW-C的回程路由。

数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| DRA信息 | 主机名（HOSTNAME） | host1.example.com<br>host2.example.com | 已配置数据中获取 | 取自<br>[激活Gy over DRA（静态路由+BFD组网）](激活Gy over DRA（静态路由+BFD组网）_29725460.md)<br>中配置的数据。 |
| Gy interface | 逻辑接口名称（NAME） | gyif1/0/0 | 已配置数据中获取 | 取自<br>[激活Gy over DRA（静态路由+BFD组网）](激活Gy over DRA（静态路由+BFD组网）_29725460.md)<br>中配置的数据。 |

工具

OM Portal

## [操作步骤](#ZH-CN_OPI_0229725461)

1. 断开 GGSN/PGW-C 与OCS1、OCS4的连接，例如删除 GGSN/PGW-C 到OCS的路由，这里主要调测经DRA转交Diameter消息的场景。调测结束后，请恢复 GGSN/PGW-C 与OCS1、OCS4的连接。
2. 在OM Portal上创建Gy接口跟踪，在“对端IP地址”栏输入DRA的IP地址（ **[ADD DIAMRTNEXTHOP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/路由管理/Diameter路由配置/增加Diameter路由下一跳（ADD DIAMRTNEXTHOP）_09897310.md)** 命令指定的 “SEQUENCE” 值最小的DRA ， **[ADD DIAMPEERADDR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)** 命令配置的第一个DRA的IP地址）。
3. 测试终端使用APN“apn-test”接入网络，用户访问业务。
4. 查看消息跟踪，观察 GGSN/PGW-C 是否向DRA发送了CCR消息，如 [图1](#ZH-CN_OPI_0229725461__fig1) 所示。
  **图1** Gy接口跟踪

  <br>

  ![](调测Gy over DRA_29725461.assets/zh-cn_image_0232662120_2.png "点击放大")
    - 是：功能正常，调测结束。
    - 否：执行[步骤 5](#ZH-CN_OPI_0229725461__step4)。
5. 执行 [**DSP ROUTE**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/路由基础/IPv4路由表/显示IPv4路由表（DSP ROUTE）_00441129.md) 命令，源地址是Gy接口的IP地址（gyif1/0/0的IP地址），目的地址是DRA的IP地址（同“对端IP地址”栏输入的DRA IP地址），观察是否能ping通对端。
    - 是：执行[步骤 7](#ZH-CN_OPI_0229725461__step6)。
    - 否：执行[步骤 6](#ZH-CN_OPI_0229725461__step5)。
6. 执行 [**DSP ROUTE**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/路由基础/IPv4路由表/显示IPv4路由表（DSP ROUTE）_00441129.md) 命令查看 GGSN/PGW-C 与DRA之间的路由是否正确。
    - 是：执行[步骤 7](#ZH-CN_OPI_0229725461__step6)。
    - 否：参考[激活Gy over DRA（静态路由+BFD组网）](激活Gy over DRA（静态路由+BFD组网）_29725460.md)重新配置后执行[步骤 4](#ZH-CN_OPI_0229725461__step3)。
7. 执行 [**DSP DRASTATUS**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/DRA管理/DRA状态/显示DRA状态（DSP DRASTATUS）_09897296.md) 命令，查看指定DRA的链路组状态是否正常。
  ```
  DSP DRASTATUS:;

  ......

  -------------------------
  DRA主机名                  POD名称                   本端地址           本端子地址           对端地址            正常链路         异常链路         无链路 
  host1.example.com         uncpod-0116-30-0-195      10.8.10.1:13201     -                   10.10.10.1:3868     gy                -                -       
  host1.example.com         uncpod-0116-30-0-195      10.8.10.1:13201     -                   10.10.10.2:3868     gy                -                -       
  host2.example.com         uncpod-0116-30-0-195      10.8.10.2:13202     10.8.10.5:13202     endpoint0           gy                -                -       
  host2.example.com         uncpod-0116-30-0-195      10.8.10.2:13202     10.8.10.5:13202     endpoint1           gy                -                -        
  (Number of results = 4)
  ---    END
  ```
    - 是：执行[步骤 9](#ZH-CN_OPI_0229725461__step81)。
    - 否：执行[步骤 8](#ZH-CN_OPI_0229725461__step7)。
8. 执行 [**LST DRA**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/DRA管理/DRA信息/查询DRA（LST DRA）_09897294.md) 命令，查看 GGSN/PGW-C 上的DRA设备标识是否和规划值及DRA上的配置一致。
  ```
  LST DRA:;
  ```
  ```
  ......

  -------------------------
  主机名               VPN实例        DSCP值 
  host1.example.com    vpn_gyif         46         
  host2.example.com    vpn_gyif         46         
  (结果个数 = 2)
  ---    END
  ```
    - 是：执行[步骤 10](#ZH-CN_OPI_0229725461__step9)。
    - 否：参考[激活Gy over DRA（静态路由+BFD组网）](激活Gy over DRA（静态路由+BFD组网）_29725460.md)重新配置后执行[步骤 4](#ZH-CN_OPI_0229725461__step3)。
9. 执行 [**LST DIAMRTREALM**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/路由管理/Diameter路由/查询Diameter路由域名信息（LST DIAMRTREALM）_09897306.md) 和 [**LST DIAMRTNEXTHOP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/路由管理/Diameter路由配置/查询Diameter路由下一跳（LST DIAMRTNEXTHOP）_09897312.md) 命令，查询Diameter路由数据配置是否与规划值一致。
  ```
  LST DIAMRTREALM:;
  ```
  ```
  ......

  -------------------------
       Diameter域名名称  =  ocs.huawei.com
           Diameter应用  =  Gy
           路由选择模式  =  主备
           Failover开关  =  禁止
           自动倒回开关  =  禁止
  (结果个数 = 1)
  ---    END
  ```
  ```
  LST DIAMRTNEXTHOP:REALMNAME="ocs.huawei.com";
  ```
  ```
  ......

  -------------------------
  Diameter域名名称     Diameter应用     下一跳                 sequence

  ocs.huawei.com       Gy               host1.example.com      1   
  ocs.huawei.com       Gy               host2.example.com      2      
  (结果个数 = 2)
  ---    END
  ```
    - 是：执行[步骤 11](#ZH-CN_OPI_0229725461__step1829245425110)。
    - 否：参考[激活Gy over DRA（静态路由+BFD组网）](激活Gy over DRA（静态路由+BFD组网）_29725460.md)重新配置后执行[步骤 4](#ZH-CN_OPI_0229725461__step3)。
10. 执行 **[LST DIAMLOCINFO](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter本端信息/查询Diameter本端信息（LST DIAMLOCINFO）_09897274.md)** 和 **[LST LOGICINF](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/查询逻辑接口（LST LOGICINF）_09896726.md)** 命令，查看 GGSN/PGW-C 的Gy口设备标识与IP等是否和规划值及DRA上的配置一致。
  ```
  LST DIAMLOCINFO:;
  ```
  ```
  ......

  -------------------------
  本端主机名    本端域名         产品名称     Vendor-Id AVP值      Firmware-Revision AVP值    Origin-State-Id AVP    Supported-Vendor-Id AVP 
  unc_1         example.com      UNC          10415                0                          不使能                  不使能                 
  unc_2         example.com      UNC          10415                0                          不使能                  不使能                               
  (结果个数 = 2)
  ---    END
  ```
  ```
  LST LOGICINF: NAME="gyif1/0/0";
  ```
  ```
  ......

  -------------------------
             逻辑接口名称  =  gyif1/0/0
      逻辑接口的IPv4地址1  =  10.8.10.1
      逻辑接口的IPv4掩码1  =  255.255.255.255
      逻辑接口的IPv4地址2  =  10.8.10.4
      逻辑接口的IPv4掩码2  =  255.255.255.255
              VPN实例名称  =  vpn_gyif
  	               ......
  (结果个数 = 1)
  ---    END
  ```
    - 是：执行[步骤 11](#ZH-CN_OPI_0229725461__step1829245425110)。
    - 否：参考[激活Gy over DRA（静态路由+BFD组网）](激活Gy over DRA（静态路由+BFD组网）_29725460.md)重新配置后执行[步骤 4](#ZH-CN_OPI_0229725461__step3)。
11. 收集信息并寻求技术支持。
    a. 执行 **[EXP MML](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/配置管理/配置导出管理/导出MML文件（EXP MML）_47200033.md)** 命令将当前配置数据导出为MML脚本文件并保存。
    b. 收集并保存上述所有查询信息。
    c. 收集归纳所有信息并联系华为技术支持解决。
