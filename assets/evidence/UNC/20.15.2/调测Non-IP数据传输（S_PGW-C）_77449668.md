# 调测 Non-IP数据传输 （S/PGW-C）

- [操作场景](#ZH-CN_OPI_0277449668__1.3.1)
- [必备事项](#ZH-CN_OPI_0277449668__1.3.2)
- [操作步骤](#ZH-CN_OPI_0277449668__1.3.3)

## [操作场景](#ZH-CN_OPI_0277449668)

当运营商部署 Non-IP数据传输 功能时，需对该功能进行调测，确保该功能正常生效。

> **说明**
> SGW-C、PGW-C

## [必备事项](#ZH-CN_OPI_0277449668)

前提条件

- 请仔细阅读[WSFD-215103 Non-IP数据传输特性概述（S/PGW-C）](特性概述_77449666.md)。
- 完成 [调测NB-IoT终端标准接入（适用于S/PGW-C）](../../WSFD-011601 NB-IoT终端标准接入/WSFD-011601 NB-IoT终端标准接入（适用于S_PGW-C）/调测NB-IoT终端标准接入（适用于S_PGW-C）_76669509.md) 。
- 完成 [调测基于信令面的数据传输（SGW-C）](../../WSFD-215101 基于信令面的数据传输/WSFD-215101 基于信令面的数据传输（SGW-C）/调测基于信令面的数据传输（SGW-C）_77260997.md) 。
- 完成[激活Non-IP数据传输（S/PGW-C）](激活Non-IP数据传输（S_PGW-C）_77449667.md)。

数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| 用户信息查询 | IMSI | 123000123456789 | 测试终端自带 | - |
| 测试终端使用的APN | APN | test | 已配置数据中获取 | 取自<br>[激活Non-IP数据传输（S/PGW-C）](激活Non-IP数据传输（S_PGW-C）_77449667.md)<br>中配置的APN实例名。 |

工具

- 测试终端
- OM Portal跟踪工具

## [操作步骤](#ZH-CN_OPI_0277449668)

1. 进入 “MML命令行-UNC” 窗口。
2. 查询License中是否允许使用 Non-IP数据传输 功能。
  [**LST LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md) : LICITEM="LKV3WNBNIP11";
    - 如果“ 开关”为“使能”，请执行[3](#ZH-CN_OPI_0277449668__cmd1236500464184705)。
    - 如果“ 开关”为“不使能”，则执行 [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md) 命令打开本特性对应的License配置开关。
3. 执行 [**LST NONIPFUNC**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/M2M/全局Non-IP配置/查询Non-IP功能配置（LST NONIPFUNC）_28567650.md) 命令，检查全局Non-IP功能是否开启。
    - 如果 “Non-IP功能开关” 为 “使能” ， [4](#ZH-CN_OPI_0277449668__cmd1583218602184705) 。
    - 如果 “Non-IP功能开关” 为 “不使能” ，请参考 [激活Non-IP数据传输](激活Non-IP数据传输（S_PGW-C）_77449667.md) 开启全局Non-IP功能开关，并重新执行此步骤。
4. 执行 [**LST APNNONIPFUNC**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/M2M/APN的Non-IP配置/查询APN Non-IP功能配置（LST APNNONIPFUNC）_28567628.md) 命令，检查指定APN下的Non-IP功能是否开启。
    - 如果 “APN Non-IP功能开关” 为 “使能” ， [5](#ZH-CN_OPI_0277449668__cmd47672955184705) 。
    - 如果 “APN Non-IP功能开关” 为 “不使能” ，请参考 [激活Non-IP数据传输](激活Non-IP数据传输（S_PGW-C）_77449667.md) 开启指定APN下的Non-IP功能开关，并重新执行此步骤。
5. 在OM Portal上 [创建用户跟踪任务](../../../../../../网络运维/日常维护/UNC基础运维操作/创建消息跟踪/创建用户跟踪/用户跟踪_72467812.md) ，在“参数配置”栏输入用户IMSI，在“消息类型”栏选择GTPC、UP DATA和DOWN DATA消息类型。
6. 激活用户，并跟踪该用户消息。
7. 查看用户跟踪消息，检查MME发送给S-GW的Create Session Request消息的PAA信元和PDN Type信元是否携带Non-IP标识，如 [图1](#ZH-CN_OPI_0277449668__fig1) 所示。
  **图1** PAA信元和PDN Type信元

  <br>

  ![](调测Non-IP数据传输（S_PGW-C）_77449668.assets/zh-cn_image_0000002083977620_2.png)
    - 如果携带Non-IP标识，则请执行 [8](#ZH-CN_OPI_0277449668__cmd1468625985184705) 。
    - 如果未携带Non-IP标识，请执行 [11](#ZH-CN_OPI_0277449668__cmd410818743184705) 。
8. 执行 [**PING**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/系统管理/系统维护/Ping和Tracert/Ping/IP Ping（PING）_16499685.md) 命令，在 UNC 上 [**PING**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/系统管理/系统维护/Ping和Tracert/Ping/IP Ping（PING）_16499685.md) 对端M2M服务器地址，查看 UNC 到对端M2M服务器的互通链路是否正常。
  ```
  PING: IPVERSION=IPv4, SOURCEIPV4ADDRESS="10.108.10.10",DESTIPV4ADDRESS="10.107.242.16";
  ```
    - 如果收到对端M2M服务器的响应，表明连接正常，则调测结束。
    - 如果连接出现timeout，表明链路不通，请执行 [9](#ZH-CN_OPI_0277449668__cmd421880149184705) 。
9. 执行 [**LST M2MSERVERGRP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/M2M/M2M服务器组/查询M2M服务器组（LST M2MSERVERGRP）_73321234.md) 、 [**LST M2MSERVER**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/M2M/M2M服务器/查询M2M服务器（LST M2MSERVER）_73321233.md) 和 [**LST M2MSVRGRPBIND**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/M2M/M2M服务器组绑定关系/查询M2M服务器组绑定关系（LST M2MSVRGRPBIND）_73321235.md) 命令查看 UNC 的M2M服务器配置信息是否和规划值及M2M服务器上的配置一致。
  ```
  LST M2MSERVERGRP: GROUPNAME="m2msrvgroup01";
  ```
  ```
  M2M服务器组信息：
  -----------------------------
      M2M服务器组名称  =  m2msrvgroup01
  M2M服务器IP地址类型  =  IPV4
  (结果个数 = 1)
  ---    END
  ```
  ```
  LST M2MSERVER: GROUPNAME="m2msrvgroup01";
  ```
  ```
  M2M服务器
  ---------
      M2M服务器组名称  =  m2msrvgroup01
        M2M服务器索引  =  1
   M2M服务器IP地址类型  =  IPV4
    M2M服务器IPv4地址  =  10.107.242.17
    M2M服务器IPv6地址  =  ::
         服务器端口号  =  2020
  (结果个数 = 1)
  ---    END
  ```
  ```
  LST M2MSVRGRPBIND: APN="isp";
  RETCODE = 0  操作成功  

  结果如下
  --------
  M2M服务器组名称  =  m2msrvgroup01             
              APN  =  isp 
  UPF实例标识集合  =  NULL
   (结果个数 = 1) 
   ---    END
  ```
    - 如果配置一致，执行[11](#ZH-CN_OPI_0277449668__cmd410818743184705)。
    - 如果配置不一致，执行[10](#ZH-CN_OPI_0277449668__cmd1118530956184705)。
10. 修改 UNC 上的M2M服务器配置信息。
    a. 执行**[RMV M2MSVRGRPBIND](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/M2M/M2M服务器组绑定关系/删除M2M服务器组绑定关系（RMV M2MSVRGRPBIND）_73321244.md)**、[**RMV M2MSERVER**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/M2M/M2M服务器/删除M2M服务器（RMV M2MSERVER）_73321242.md)和[**RMV M2MSERVERGRP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/M2M/M2M服务器组/删除M2M服务器组（RMV M2MSERVERGRP）_73321243.md)命令，删除原有配置信息。
    b. 执行[**ADD M2MSERVER**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/M2M/M2M服务器/增加M2M服务器（ADD M2MSERVER）_73321225.md)、[**ADD M2MSERVERGRP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/M2M/M2M服务器组/增加M2M服务器组（ADD M2MSERVERGRP）_73321226.md)和[**ADD M2MSVRGRPBIND**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/M2M/M2M服务器组绑定关系/增加M2M服务器组绑定关系（ADD M2MSVRGRPBIND）_73321227.md)命令，按照规划数据重新配置UNC上的M2M服务器信息。
    c. 再次执行[步骤 8](#ZH-CN_OPI_0277449668__step5)，检查UNC和M2M服务器之间的链路状态是否正常。
          - 如果链路互通正常，则调测结束。
          - 如果链路互通异常，请执行[11](#ZH-CN_OPI_0277449668__cmd410818743184705)。
11. 收集信息并寻求技术支持。
    a. 在OM Portal上创建用户跟踪任务 ，执行 [步骤 6](#ZH-CN_OPI_0277449668__step3) 并保存报文。
    b. 执行 **[EXP MML](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/配置管理/配置导出管理/导出MML文件（EXP MML）_47200033.md)** 命令将当前配置数据导出为MML脚本文件并保存。
    c. 查看并收集对端设备配置及接口状态信息。
    d. 收集归纳所有信息并联系华为技术支持解决。
