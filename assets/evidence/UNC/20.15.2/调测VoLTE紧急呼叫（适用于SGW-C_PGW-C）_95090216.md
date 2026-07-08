# 调测 VoLTE紧急呼叫 （适用于SGW-C/PGW-C）

- [操作场景](#ZH-CN_OPI_0295090216__1.3.1)
- [必备事项](#ZH-CN_OPI_0295090216__1.3.2)
- [操作步骤](#ZH-CN_OPI_0295090216__1.3.3)

## [操作场景](#ZH-CN_OPI_0295090216)

当运营商部署紧急呼叫功能时，需对 UNC 的紧急呼叫功能进行调测，确保用户可以正常接入网络。

> **说明**
> 适用于SGW-C、PGW-C。

## [必备事项](#ZH-CN_OPI_0295090216)

前提条件

- 请仔细阅读[WSFD-102101 VoLTE紧急呼叫](../WSFD-102101 VoLTE紧急呼叫_70014690.md)。
- 完成[激活VoLTE紧急呼叫（适用于SGW-C/PGW-C）](激活VoLTE紧急呼叫（适用于SGW-C_PGW-C）_30394882.md)。

数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| 用户信息查询 | IMSI | 123000123456789或Null | 测试终端自带 | - |
| 用户信息查询 | IMEI | 123456789011121 | 测试终端自带 | - |
| 测试终端使用的APN | APN名称（APN） | sos | 已配置数据中获取 | 取自<br>[激活VoLTE紧急呼叫（适用于SGW-C/PGW-C）](激活VoLTE紧急呼叫（适用于SGW-C_PGW-C）_30394882.md)<br>中配置的<br>“APN”<br>实例名。 |

工具

- 测试终端
- OM Portal

## [操作步骤](#ZH-CN_OPI_0295090216)

1. 在 “MML命令行-UNC” 窗口执行命令
2. 执行 [**LST LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md) 命令，查询License功能是否正常开启。
  [**LST LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md) : LICITEM="LKV3W9ECAL11";
    - 如果“SWITCH”为“ENABLE”，请执行[3](#ZH-CN_OPI_0295090216__cmd103264131184656)。
    - 如果“SWITCH”为“DISABLE”，则执行 [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md) 命令打开本特性对应的License配置开关。
3. 在OM Portal上 [用户跟踪](../../../../../网络运维/日常维护/UNC基础运维操作/创建消息跟踪/创建用户跟踪/用户跟踪_72467812.md) ，在 “参数配置” 栏输入用户IMSI ，在 “消息类型” 栏选择GTPC消息类型。
  > **说明**
  > 如果用户处于限制服务模式 ，可以在参数配置栏输入用户IMEI进行跟踪。
4. 需要进行紧急呼叫的 测试终端 使用 “sos” “APN” 发起接入网络请求。
5. 查看用户跟踪任务，检查S/PGW-C是否收到了 MME 发送的 Create Session Request 消息。
  **图1** 用户跟踪任务结果

  <br>

  ![](调测VoLTE紧急呼叫（适用于SGW-C_PGW-C）_95090216.assets/zh-cn_image_0312324284_2.png)
    - 如果S/PGW-C收到MME发送的激活请求消息，如[图1](#ZH-CN_OPI_0295090216__fig1)所示，请执行[6](#ZH-CN_OPI_0295090216__cmd555754880184656)。
    - 如果S/PGW-C没有收到MME发送的激活请求消息，请确认S/PGW-C到MME的连接是否正常。
6. 查看用户跟踪任务，打开用户跟踪结果中的 Create Session Response 消息，查看消息的 “cause-result” 值是否为 “request-accepted (16)” 。
  **图2** Create Session Response 消息

  <br>

  ![](调测VoLTE紧急呼叫（适用于SGW-C_PGW-C）_95090216.assets/zh-cn_image_0311861157_2.png)
    - 如果“cause-result”值为“16”，如[图2](#ZH-CN_OPI_0295090216__fig4)所示，请执行[7](#ZH-CN_OPI_0295090216__cmd1833593302184656)。
    - 如果“cause-result”值不为“16”，请参考故障案例进行调测。
7. 执行 [**DSP PDUSESSION**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/查询PDP上下文信息/显示PDU会话（DSP PDUSESSION）_09653215.md) 命令，通过 测试终端 的IMSI查看 测试终端 用户信息。
  ```
  DSP PDUSESSION
  :QUERYTYPE=IMSI, IMSI="123000123456789", DSPINFOTYPE=DETAILED, WLNETWKTYPE=NW2G3G4G, EBIORNSAPI=5, ACCESSTYPE234G=AT_3GPP_ACCESS;
  ```
  ```
                          IMSI  =  123000123456789
  ```
  ```
                     APN or DNN  =  sos
  ```
  ```
   	                           ......
  ```
  ```
                   User IP Type  =  IPv4
  ```
  ```
            User IP Information  =  10.0.0.1
  ```
  ```
   	                           ......
  ```
  ```
  (Number of Results  =  1)
  ```
    - 如果测试终端使用的“PDP address”和“APN name”与规划值一致，请执行[8](#ZH-CN_OPI_0295090216__cmd711663491184656)。
    - 如果测试终端使用的“PDP address”和“APN name”与规划值不一致，请重新配置，然后重新执行[4](#ZH-CN_OPI_0295090216__cmd2041084976184656)。
8. 执行 [**LST APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/查询APN配置（LST APN）_09652599.md) :APN="sos";查看用户所属APN的紧急呼叫功能开关是否打开。
  ```
             APN  =  sos
  ```
  ```
                ......
  ```
  ```
  Emergency Call  =  DISABLE
  ```
  ```
                ......
  ```
    - 如果APN的“EMERGENCYSWITCH”为ENABLE，测试终端接入成功，调测结束。
    - 如果APN的“EMERGENCYSWITCH”为DISABLE（如上所示），请执行[9](#ZH-CN_OPI_0295090216__cmd1387007569184656)。
9. 收集信息并寻求技术支持。
    a. 在OM Portal上创建用户跟踪任务 ，执行 [4](#ZH-CN_OPI_0295090216__cmd2041084976184656) 并保存报文。
    b. 执行 **[EXP MML](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/配置管理/配置导出管理/导出MML文件（EXP MML）_47200033.md)** 命令查看当前配置并保存查询结果。
    c. 收集并保存上述所有查询信息。
    d. 收集归纳所有信息并联系华为技术支持解决。
