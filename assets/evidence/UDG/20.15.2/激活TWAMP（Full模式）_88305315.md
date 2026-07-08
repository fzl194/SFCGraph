# 激活TWAMP（Full模式）

- [操作场景](#ZH-CN_OPI_0000001188305315__1.3.1)
- [必备事项](#ZH-CN_OPI_0000001188305315__1.3.2)
- [操作步骤](#ZH-CN_OPI_0000001188305315__1.3.3)
- [任务示例](#ZH-CN_OPI_0000001188305315__1.3.4)

## [操作场景](#ZH-CN_OPI_0000001188305315)

IP传输场景下，线路带宽不稳定，运营商可以部署TWAMP功能检测网元间的传输网络QoS，如丢包、时延、抖动，实时在线监控传输网络QoS的变化。

> **说明**
> 适用于SGW-U、UPF。

## [必备事项](#ZH-CN_OPI_0000001188305315)

前提条件

- 请仔细阅读[GWFD-110921 支持TWAMP特性概述](GWFD-110921 支持TWAMP特性概述_42545190.md)。
- 完成 **加载license** （如果有需求，请联系华为技术支持工程师处理）。
- TWAMP功能由IPAPM服务承载，请完成IPAPM安装，参见[安装IPAPM服务](../../../../../网络部署/软件安装/基于VNF LCM安装UDG（非SDN）/安装可选服务/安装IPAPM服务_35204486.md)。

数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| VPN实例 | VPN实例名（VRFNAME） | VPN_CN | 全网规划 | **[ADD TWAMPVPNINST](../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPAPM功能管理/TWAMP/VPN实例/增加VPN实例名称（ADD TWAMPVPNINST）_27102474.md)**<br>“VRFNAME”<br>必须和外联口VPN实例一致。 |
| 逻辑接口 | 逻辑接口名称（NAME） | n3if1/1/1 | 全网规划 | [**ADD TWAMPLOGICINF**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPAPM功能管理/TWAMP/本端逻辑接口配置/增加本地逻辑接口（ADD TWAMPLOGICINF）_27262282.md)<br>- 逻辑接口使用N3/S1-U接口。<br>- “VRFNAME”已通过**[ADD TWAMPVPNINST](../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPAPM功能管理/TWAMP/VPN实例/增加VPN实例名称（ADD TWAMPVPNINST）_27102474.md)**配置。<br>- 如果与业务的N3/S1-U接口共用IP地址，[**ADD TWAMPLOGICINF**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPAPM功能管理/TWAMP/本端逻辑接口配置/增加本地逻辑接口（ADD TWAMPLOGICINF）_27262282.md)命令中“SHAREDTYPE”需设置为“TRUE”。<br>- 如果与业务的N3/S1-U接口不共用IP地址，[**ADD TWAMPLOGICINF**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPAPM功能管理/TWAMP/本端逻辑接口配置/增加本地逻辑接口（ADD TWAMPLOGICINF）_27262282.md)命令中“SHAREDTYPE”需设置为“FALSE”。 |
| 逻辑接口 | 地址族类型（AFTYPE） | IPV4 | 全网规划 | [**ADD TWAMPLOGICINF**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPAPM功能管理/TWAMP/本端逻辑接口配置/增加本地逻辑接口（ADD TWAMPLOGICINF）_27262282.md)<br>- 逻辑接口使用N3/S1-U接口。<br>- “VRFNAME”已通过**[ADD TWAMPVPNINST](../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPAPM功能管理/TWAMP/VPN实例/增加VPN实例名称（ADD TWAMPVPNINST）_27102474.md)**配置。<br>- 如果与业务的N3/S1-U接口共用IP地址，[**ADD TWAMPLOGICINF**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPAPM功能管理/TWAMP/本端逻辑接口配置/增加本地逻辑接口（ADD TWAMPLOGICINF）_27262282.md)命令中“SHAREDTYPE”需设置为“TRUE”。<br>- 如果与业务的N3/S1-U接口不共用IP地址，[**ADD TWAMPLOGICINF**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPAPM功能管理/TWAMP/本端逻辑接口配置/增加本地逻辑接口（ADD TWAMPLOGICINF）_27262282.md)命令中“SHAREDTYPE”需设置为“FALSE”。 |
| 逻辑接口 | 逻辑接口的IPv4地址（IPV4ADDRESS） | 10.1.1.10 | 全网规划 | [**ADD TWAMPLOGICINF**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPAPM功能管理/TWAMP/本端逻辑接口配置/增加本地逻辑接口（ADD TWAMPLOGICINF）_27262282.md)<br>- 逻辑接口使用N3/S1-U接口。<br>- “VRFNAME”已通过**[ADD TWAMPVPNINST](../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPAPM功能管理/TWAMP/VPN实例/增加VPN实例名称（ADD TWAMPVPNINST）_27102474.md)**配置。<br>- 如果与业务的N3/S1-U接口共用IP地址，[**ADD TWAMPLOGICINF**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPAPM功能管理/TWAMP/本端逻辑接口配置/增加本地逻辑接口（ADD TWAMPLOGICINF）_27262282.md)命令中“SHAREDTYPE”需设置为“TRUE”。<br>- 如果与业务的N3/S1-U接口不共用IP地址，[**ADD TWAMPLOGICINF**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPAPM功能管理/TWAMP/本端逻辑接口配置/增加本地逻辑接口（ADD TWAMPLOGICINF）_27262282.md)命令中“SHAREDTYPE”需设置为“FALSE”。 |
| 逻辑接口 | 逻辑接口掩码（IPV4MASK） | 255.255.255.255 | 全网规划 | [**ADD TWAMPLOGICINF**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPAPM功能管理/TWAMP/本端逻辑接口配置/增加本地逻辑接口（ADD TWAMPLOGICINF）_27262282.md)<br>- 逻辑接口使用N3/S1-U接口。<br>- “VRFNAME”已通过**[ADD TWAMPVPNINST](../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPAPM功能管理/TWAMP/VPN实例/增加VPN实例名称（ADD TWAMPVPNINST）_27102474.md)**配置。<br>- 如果与业务的N3/S1-U接口共用IP地址，[**ADD TWAMPLOGICINF**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPAPM功能管理/TWAMP/本端逻辑接口配置/增加本地逻辑接口（ADD TWAMPLOGICINF）_27262282.md)命令中“SHAREDTYPE”需设置为“TRUE”。<br>- 如果与业务的N3/S1-U接口不共用IP地址，[**ADD TWAMPLOGICINF**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPAPM功能管理/TWAMP/本端逻辑接口配置/增加本地逻辑接口（ADD TWAMPLOGICINF）_27262282.md)命令中“SHAREDTYPE”需设置为“FALSE”。 |
| 逻辑接口 | VPN实例名称（VRFNAME） | VPN_CN | 全网规划 | [**ADD TWAMPLOGICINF**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPAPM功能管理/TWAMP/本端逻辑接口配置/增加本地逻辑接口（ADD TWAMPLOGICINF）_27262282.md)<br>- 逻辑接口使用N3/S1-U接口。<br>- “VRFNAME”已通过**[ADD TWAMPVPNINST](../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPAPM功能管理/TWAMP/VPN实例/增加VPN实例名称（ADD TWAMPVPNINST）_27102474.md)**配置。<br>- 如果与业务的N3/S1-U接口共用IP地址，[**ADD TWAMPLOGICINF**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPAPM功能管理/TWAMP/本端逻辑接口配置/增加本地逻辑接口（ADD TWAMPLOGICINF）_27262282.md)命令中“SHAREDTYPE”需设置为“TRUE”。<br>- 如果与业务的N3/S1-U接口不共用IP地址，[**ADD TWAMPLOGICINF**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPAPM功能管理/TWAMP/本端逻辑接口配置/增加本地逻辑接口（ADD TWAMPLOGICINF）_27262282.md)命令中“SHAREDTYPE”需设置为“FALSE”。 |
| 逻辑接口 | 是否共地址（SHAREDTYPE） | TRUE | 全网规划 | [**ADD TWAMPLOGICINF**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPAPM功能管理/TWAMP/本端逻辑接口配置/增加本地逻辑接口（ADD TWAMPLOGICINF）_27262282.md)<br>- 逻辑接口使用N3/S1-U接口。<br>- “VRFNAME”已通过**[ADD TWAMPVPNINST](../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPAPM功能管理/TWAMP/VPN实例/增加VPN实例名称（ADD TWAMPVPNINST）_27102474.md)**配置。<br>- 如果与业务的N3/S1-U接口共用IP地址，[**ADD TWAMPLOGICINF**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPAPM功能管理/TWAMP/本端逻辑接口配置/增加本地逻辑接口（ADD TWAMPLOGICINF）_27262282.md)命令中“SHAREDTYPE”需设置为“TRUE”。<br>- 如果与业务的N3/S1-U接口不共用IP地址，[**ADD TWAMPLOGICINF**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPAPM功能管理/TWAMP/本端逻辑接口配置/增加本地逻辑接口（ADD TWAMPLOGICINF）_27262282.md)命令中“SHAREDTYPE”需设置为“FALSE”。 |
| TWAMP Full模式响应端参数 | 响应端索引（RESPONDERID） | 1 | 全网规划 | [**ADD TWAMPRESPONDER**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPAPM功能管理/TWAMP/TWAMP响应端配置/增加TWAMP响应端（ADD TWAMPRESPONDER）_73142131.md)<br>ServWait：控制连接建立时，如果本端在该时间内没有收到与该连接相关的数据包时，则本端删除与Client端建立的所有测试会话，并释放与Client端的控制连接。<br>RefWait：启动测试会话后，如果本端在该时间内，没有收到任何一个测试会话的Sender-Test报文，则认为故障，删除当前控制连接下的所有的测试会话。 |
| TWAMP Full模式响应端参数 | 地址族类型（AFTYPE） | IPV4 | 全网规划 | [**ADD TWAMPRESPONDER**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPAPM功能管理/TWAMP/TWAMP响应端配置/增加TWAMP响应端（ADD TWAMPRESPONDER）_73142131.md)<br>ServWait：控制连接建立时，如果本端在该时间内没有收到与该连接相关的数据包时，则本端删除与Client端建立的所有测试会话，并释放与Client端的控制连接。<br>RefWait：启动测试会话后，如果本端在该时间内，没有收到任何一个测试会话的Sender-Test报文，则认为故障，删除当前控制连接下的所有的测试会话。 |
| TWAMP Full模式响应端参数 | TWAMP架构（TWAMPARCH） | FULL | 固定取值 | [**ADD TWAMPRESPONDER**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPAPM功能管理/TWAMP/TWAMP响应端配置/增加TWAMP响应端（ADD TWAMPRESPONDER）_73142131.md)<br>ServWait：控制连接建立时，如果本端在该时间内没有收到与该连接相关的数据包时，则本端删除与Client端建立的所有测试会话，并释放与Client端的控制连接。<br>RefWait：启动测试会话后，如果本端在该时间内，没有收到任何一个测试会话的Sender-Test报文，则认为故障，删除当前控制连接下的所有的测试会话。 |
| TWAMP Full模式响应端参数 | 本端IPv4（LOCALIPV4） | 10.1.1.10 | 本端规划 | [**ADD TWAMPRESPONDER**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPAPM功能管理/TWAMP/TWAMP响应端配置/增加TWAMP响应端（ADD TWAMPRESPONDER）_73142131.md)<br>ServWait：控制连接建立时，如果本端在该时间内没有收到与该连接相关的数据包时，则本端删除与Client端建立的所有测试会话，并释放与Client端的控制连接。<br>RefWait：启动测试会话后，如果本端在该时间内，没有收到任何一个测试会话的Sender-Test报文，则认为故障，删除当前控制连接下的所有的测试会话。 |
| TWAMP Full模式响应端参数 | 协商等待时间（SERVWAIT） | 900 | 本端规划 | [**ADD TWAMPRESPONDER**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPAPM功能管理/TWAMP/TWAMP响应端配置/增加TWAMP响应端（ADD TWAMPRESPONDER）_73142131.md)<br>ServWait：控制连接建立时，如果本端在该时间内没有收到与该连接相关的数据包时，则本端删除与Client端建立的所有测试会话，并释放与Client端的控制连接。<br>RefWait：启动测试会话后，如果本端在该时间内，没有收到任何一个测试会话的Sender-Test报文，则认为故障，删除当前控制连接下的所有的测试会话。 |
| TWAMP Full模式响应端参数 | 测试等待时间（REFWAIT） | 900 | 本端规划 | [**ADD TWAMPRESPONDER**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPAPM功能管理/TWAMP/TWAMP响应端配置/增加TWAMP响应端（ADD TWAMPRESPONDER）_73142131.md)<br>ServWait：控制连接建立时，如果本端在该时间内没有收到与该连接相关的数据包时，则本端删除与Client端建立的所有测试会话，并释放与Client端的控制连接。<br>RefWait：启动测试会话后，如果本端在该时间内，没有收到任何一个测试会话的Sender-Test报文，则认为故障，删除当前控制连接下的所有的测试会话。 |
| 设置TWAMP的Full模式TCP保活参数配置 | 保活时间（KEEPALIVETIME） | 90 | 全网规划 | **[SET TCPKEEPALIVECFG](../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPAPM功能管理/TWAMP/TCP保活配置/设置TCP保活参数（SET TCPKEEPALIVECFG）_27102484.md)** |
| 设置TWAMP的Full模式TCP保活参数配置 | 保活间隔（INTERVAL） | 30 | 全网规划 | **[SET TCPKEEPALIVECFG](../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPAPM功能管理/TWAMP/TCP保活配置/设置TCP保活参数（SET TCPKEEPALIVECFG）_27102484.md)** |
| 设置TWAMP的Full模式TCP保活参数配置 | 保活重试（RETRY） | 9 | 全网规划 | **[SET TCPKEEPALIVECFG](../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPAPM功能管理/TWAMP/TCP保活配置/设置TCP保活参数（SET TCPKEEPALIVECFG）_27102484.md)** |

## [操作步骤](#ZH-CN_OPI_0000001188305315)

1. 检查IPAPM是否已安装，若未安装，请完成IPAPM安装，参见 [安装IPAPM服务](../../../../../网络部署/软件安装/基于VNF LCM安装UDG（非SDN）/安装可选服务/安装IPAPM服务_35204486.md) 。
  预期结果：“未就绪进程数”和“故障进程数”均为0。
  ```
  DSP CELLSTAT: OBJECT=PODTYPE, PODTYPE="ipapmctrl-pod";
  DSP CELLSTAT: OBJECT=PODTYPE, PODTYPE="ipapmexec-pod";
  ```
2. 打开本特性的Licence开关。
  [**SET LICENSESWITCH**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09587387.md)
3. 配置本端探测逻辑接口，UPF与gNodeB之间采用N3/S1-U接口进行探测。
  **[ADD TWAMPVPNINST](../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPAPM功能管理/TWAMP/VPN实例/增加VPN实例名称（ADD TWAMPVPNINST）_27102474.md)**
  [**ADD TWAMPLOGICINF**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPAPM功能管理/TWAMP/本端逻辑接口配置/增加本地逻辑接口（ADD TWAMPLOGICINF）_27262282.md)
  > **说明**
  > 使用命令 [**ADD TWAMPLOGICINF**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPAPM功能管理/TWAMP/本端逻辑接口配置/增加本地逻辑接口（ADD TWAMPLOGICINF）_27262282.md) 配置本端探测逻辑接口时，若与业务的N3/S1-U接口共用IP地址， [**ADD TWAMPLOGICINF**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPAPM功能管理/TWAMP/本端逻辑接口配置/增加本地逻辑接口（ADD TWAMPLOGICINF）_27262282.md) 命令中 “SHAREDTYPE” 参数取值需配置为 “TRUE” 。
4. 配置TWAMP Full模式响应端。
  [**ADD TWAMPRESPONDER**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPAPM功能管理/TWAMP/TWAMP响应端配置/增加TWAMP响应端（ADD TWAMPRESPONDER）_73142131.md)
5. 配置TCP保活参数。
  **[SET TCPKEEPALIVECFG](../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPAPM功能管理/TWAMP/TCP保活配置/设置TCP保活参数（SET TCPKEEPALIVECFG）_27102484.md)**

## [任务示例](#ZH-CN_OPI_0000001188305315)

任务描述

Full模式下gNodeB发起探测时，UPF支持作为响应端。

脚本

//打开本特性的License配置开关。

```
SET LICENSESWITCH:LICITEM="LKV3G5TWMP01",SWITCH=ENABLE;
```

//配置探测逻辑接口。

```
ADD TWAMPVPNINST: VRFNAME="VPN_CN";
ADD TWAMPLOGICINF: NAME="n3if1/1/1", AFTYPE=IPV4, IPV4ADDRESS="10.1.1.10", IPV4MASK="255.255.255.255", VRFNAME="VPN_CN", SHAREDTYPE=TRUE;
```

//配置TWAMP Full模式响应端。

```
ADD TWAMPRESPONDER:RESPONDERID=1,AFTYPE=IPV4,TWAMPARCH=FULL,LOCALIPV4="10.1.1.10",SERVWAIT=900,REFWAIT=900;
```

//设置TCP保活参数配置的实例：

```
SET TCPKEEPALIVECFG: KEEPALIVETIME=90, INTERVAL=30, RETRY=9;
```
