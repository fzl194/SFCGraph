# 调测Gy over SCTP功能

- [操作场景](#ZH-CN_OPI_0230602208__1.3.1)
- [必备事项](#ZH-CN_OPI_0230602208__1.3.2)
- [操作步骤](#ZH-CN_OPI_0230602208__1.3.3)

## [操作场景](#ZH-CN_OPI_0230602208)

运营商规划GGSN/PGW-C与OCS之间的信令采用SCTP传输时，需要通过调试手段检查GGSN/PGW-C与OCS之间的链路是否连通，以此确定SCTP功能生效。

> **说明**
> 适用于 GGSN、 PGW-C。

## [必备事项](#ZH-CN_OPI_0230602208)

前提条件

- 请仔细阅读 [WSFD-104508 SCTP](../../WSFD-104508 SCTP_27680892.md) 。
- 完成[配置Gy over SCTP功能](../激活SCTP/配置Gy over SCTP功能_30602207.md)。
- OCS上已完成相应配置，并确保已配置到 GGSN/PGW-C 的回程路由。

数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| OCS信息 | Ocs主机名称（OCSHOSTNAME） | ocs | 已配置数据中获取 | 取自<br>[配置Gy over SCTP功能](../激活SCTP/配置Gy over SCTP功能_30602207.md)<br>中配置的数据。 |
| OCS信息 | SCTP端点名称（SCTPENDPOINT） | ocsend | 已配置数据中获取 | 取自<br>[配置Gy over SCTP功能](../激活SCTP/配置Gy over SCTP功能_30602207.md)<br>中配置的数据。 |
| Gy interface | 逻辑接口名称（NAME） | gyif1/0/0 | 已配置数据中获取 | 取自<br>[配置Gy over SCTP功能](../激活SCTP/配置Gy over SCTP功能_30602207.md)<br>中配置的数据。 |

工具

第三方抓包工具。

## [操作步骤](#ZH-CN_OPI_0230602208)

1. 查询SCTP功能对应的License配置开关是否打开。
  **[LST LICENSESWITCH](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md)**
    - 如果“SWITCH”为“ENABLE”，请执行[步骤 2](#ZH-CN_OPI_0230602208__stp1)。
    - 如果“SWITCH”为“DISABLE”，则执行**[SET LICENSESWITCH](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)**命令打开本特性对应的License配置开关。
2. 执行 **[DSP OCSSTATUS](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/OCS Diameter连接/OCS状态/查询OCS状态（DSP OCSSTATUS）_09896968.md)** 命令，查看OCS的状态是否正常。
  ```
  DSP OCSSTATUS:HOSTNAME="ocs";
  ```
  ```
  ......

  -------------------------
   OCS主机名  =  ocs
     POD名称  =  uncpod-0131-30-0-197
      RU名称  =  unc
    本端地址  =  10.8.10.1:13200
  本端子地址  =  -
    对端地址  =  ocsend 
   Gy Status  =  异常
  (结果个数 = 1)
  ---    END
  ```
    - 如果检测OCS状态正常，请执行[步骤 3](#ZH-CN_OPI_0230602208__step13151931172811)。
    - 如果检测OCS状态异常，请执行[步骤 4](#ZH-CN_OPI_0230602208__stp2)。
3. 使用第三方抓包工具，查看报文中使用的协议。
    - 如果使用的是SCTP协议，则调测结束。
    - 如果使用的不是SCTP协议，请参考[配置Gy over SCTP功能](../激活SCTP/配置Gy over SCTP功能_30602207.md)重新配置，并再次执行[步骤 2](#ZH-CN_OPI_0230602208__stp1)。
4. 执行 **[LST OCS](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/OCS Diameter连接/OCS Server/查询OCS（LST OCS）_09896957.md)** 、 **[LST SCTPENDPOINT](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/SCTP管理/SCTP端点/查询SCTP端点（LST SCTPENDPOINT）_09897324.md)** 以及 **[LST DIAMPEERADDR](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/查询Diameter对端地址（LST DIAMPEERADDR）_09897259.md)** 命令，查看GGSN/PGW-C上的OCS设备标识是否和规划值及OCS上的配置一致。
  ```
  LST OCS:OCSHOSTNAME="ocs";
  ```
  ```
  ......

  -------------------------
    OCS主机名称  =  ocs
           域名  =  ocs.huawei.com
        VPN实例  =  vpn_gyif
         DSCP值  =  255
  (结果个数 = 1)
  ---    END
  ```
  ```
  LST SCTPENDPOINT:ENDPOINTNAME="ocsend";
  ```
  ```
  ......

  -------------------------
        端点名称  =  ocsend
          端口号  =  3868
          IP版本  =  IPV4
       IPv4地址1  =  10.11.11.59
       IPv4地址2  =  10.11.11.60
    SCTP模板名称  =  testtemplate
  	      ......
  (结果个数 = 1)
  ---    END
  ```
  ```
  LST DIAMPEERADDR:HOSTNAME="ocs";
  ```
  ```
  ......
  ------------------------
  主机名称     地址类型       IP地址           端口号       SCTP端点名称 
  ocs          SCTP           10.11.11.59      3868         ocsend         
  (结果个数 = 1)
  ---    END
  ```
    - 如果配置一致，请执行[步骤 5](#ZH-CN_OPI_0230602208__stp4)。
    - 如果配置不一致，请参考[配置Gy over SCTP功能](../激活SCTP/配置Gy over SCTP功能_30602207.md)重新配置，并再次执行[步骤 2](#ZH-CN_OPI_0230602208__stp1)。
5. 执行 **[LST LOGICINF](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/查询逻辑接口（LST LOGICINF）_09896726.md)** 和 **[LST DIAMLOCINFO](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter本端信息/查询Diameter本端信息（LST DIAMLOCINFO）_09897274.md)** 命令，查看GGSN/PGW-C的Gy口设备标识与IP等是否和规划值及OCS上的配置一致。
  ```
  LST LOGICINF:NAME="gyif1/0/0";
  ```
  ```
  ......

  -------------------------
                    逻辑接口名称  =  gyif1/0/0
             逻辑接口的IPv4地址1  =  10.8.20.1
             逻辑接口的IPv4掩码1  =  255.255.255.255
             逻辑接口的IPv4地址2  =  10.8.20.2
             逻辑接口的IPv4掩码2  =  255.255.255.255
                     VPN实例名称  =  vpn_gyif
                                ......
  (结果个数 = 1)
  ---    END
  ```
  ```
  LST DIAMLOCINFO:HOSTNAME="unc_1";
  ```
  ```
  ......

  -------------------------
                 本端主机名  =  unc_1
                   本端域名  =  example.com
                   产品名称  =  unc
            Vendor-Id AVP值  =  10415
     Firmware-RevisionAVP值  =  0
        Origin-State-Id AVP  =  不使能
    Supported-Vendor-Id AVP  =  不使能
  (结果个数 = 1)
  ---    END
  ```
    - 如果配置一致，请执行[步骤 6](#ZH-CN_OPI_0230602208__stp6)。
    - 如果配置不一致，请参考[配置Gy over SCTP功能](../激活SCTP/配置Gy over SCTP功能_30602207.md)重新配置，并再次执行[步骤 2](#ZH-CN_OPI_0230602208__stp1)。
6. 检查GGSN/PGW-C到OCS的互通是否正常。
    a. 根据使用的路由方式，调测GGSN/PGW-C到OCS的路由。
    b. 根据使用的可靠性组网方式，调测GGSN/PGW-C到OCS的组网。
    c. 再次执行 [步骤 2](#ZH-CN_OPI_0230602208__stp1) ，查看OCS状态。
          - 如果检测OCS状态正常，则调测结束。
          - 如果检测OCS状态异常，请执行[步骤 7](#ZH-CN_OPI_0230602208__stp7)。
7. 查看是否存在ID为 “81023” （OCS无响应告警）的告警。
    - 如果产生告警，请参考[ALM-81023 OCS无响应](../../../../../../网络运维/故障处理/UNC告警处理/业务告警/SMF&GW-C&GGSN/ALM-81023 OCS无响应_13899697.md)处理此问题。
    - 如果没有产生告警，请执行[步骤 8](#ZH-CN_OPI_0230602208__step1829245425110)。
8. 收集信息并寻求技术支持。
    a. 执行 **[EXP MML](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/配置管理/配置导出管理/导出MML文件（EXP MML）_47200033.md)** 命令将当前配置数据导出为MML脚本文件并保存。
    b. 收集并保存上述所有查询信息。
    c. 收集归纳所有信息并联系华为技术支持解决。
