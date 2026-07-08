# 激活TWAMP（Light模式）

- [操作场景](#ZH-CN_OPI_0000001142385398__1.3.1)
- [对系统的影响](#ZH-CN_OPI_0000001142385398__1.3.2)
- [必备事项](#ZH-CN_OPI_0000001142385398__1.3.3)
- [操作步骤](#ZH-CN_OPI_0000001142385398__1.3.4)
- [任务示例](#ZH-CN_OPI_0000001142385398__1.3.5)

## [操作场景](#ZH-CN_OPI_0000001142385398)

IP传输场景下，线路带宽不稳定，运营商可以部署TWAMP功能检测网元间的传输网络QoS，如丢包、时延、抖动，实时在线监控传输网络QoS的变化。在Light模式下，N3/S1-U接口的IP性能检测仅可以由本网元发起，才能对N3/S1-U接口的IP性能进行检测。

> **说明**
> 适用于SGW-U、UPF。

## [对系统的影响](#ZH-CN_OPI_0000001142385398)

本特性对系统无影响。

## [必备事项](#ZH-CN_OPI_0000001142385398)

前提条件

- 请仔细阅读[GWFD-110921 支持TWAMP特性概述](GWFD-110921 支持TWAMP特性概述_42545190.md)。
- 完成 **加载license** （如果有需求，请联系华为技术支持工程师处理）。
- TWAMP功能由IPAPM服务承载，请完成IPAPM安装，参见[安装IPAPM服务](../../../../../网络部署/软件安装/基于VNF LCM安装UDG（非SDN）/安装可选服务/安装IPAPM服务_35204486.md)。

数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| VPN实例 | VPN实例名（VRFNAME） | VPN_CN | 全网规划 | **[ADD TWAMPVPNINST](../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPAPM功能管理/TWAMP/VPN实例/增加VPN实例名称（ADD TWAMPVPNINST）_27102474.md)**<br>“VRFNAME”<br>必须和外联口VPN实例一致。 |
| 逻辑接口 | 逻辑接口名称（NAME） | n3if1/1/0 | 全网规划 | [**ADD TWAMPLOGICINF**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPAPM功能管理/TWAMP/本端逻辑接口配置/增加本地逻辑接口（ADD TWAMPLOGICINF）_27262282.md)<br>- 逻辑接口使用N3/S1-U接口。<br>- “VRFNAME”已通过**[ADD TWAMPVPNINST](../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPAPM功能管理/TWAMP/VPN实例/增加VPN实例名称（ADD TWAMPVPNINST）_27102474.md)**配置。<br>- 如果逻辑接口与业务的N3/S1-U接口共用IP地址，[**ADD TWAMPLOGICINF**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPAPM功能管理/TWAMP/本端逻辑接口配置/增加本地逻辑接口（ADD TWAMPLOGICINF）_27262282.md)命令中“SHAREDTYPE”需设置为“TRUE”。<br>- 如果逻辑接口与业务的N3/S1-U接口不共用IP地址，[**ADD TWAMPLOGICINF**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPAPM功能管理/TWAMP/本端逻辑接口配置/增加本地逻辑接口（ADD TWAMPLOGICINF）_27262282.md)命令中“SHAREDTYPE”需设置为“FALSE”。 |
| 逻辑接口 | 地址族类型（AFTYPE） | IPV4 | 全网规划 | [**ADD TWAMPLOGICINF**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPAPM功能管理/TWAMP/本端逻辑接口配置/增加本地逻辑接口（ADD TWAMPLOGICINF）_27262282.md)<br>- 逻辑接口使用N3/S1-U接口。<br>- “VRFNAME”已通过**[ADD TWAMPVPNINST](../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPAPM功能管理/TWAMP/VPN实例/增加VPN实例名称（ADD TWAMPVPNINST）_27102474.md)**配置。<br>- 如果逻辑接口与业务的N3/S1-U接口共用IP地址，[**ADD TWAMPLOGICINF**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPAPM功能管理/TWAMP/本端逻辑接口配置/增加本地逻辑接口（ADD TWAMPLOGICINF）_27262282.md)命令中“SHAREDTYPE”需设置为“TRUE”。<br>- 如果逻辑接口与业务的N3/S1-U接口不共用IP地址，[**ADD TWAMPLOGICINF**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPAPM功能管理/TWAMP/本端逻辑接口配置/增加本地逻辑接口（ADD TWAMPLOGICINF）_27262282.md)命令中“SHAREDTYPE”需设置为“FALSE”。 |
| 逻辑接口 | 逻辑接口的IPv4地址（IPV4ADDRESS） | 10.1.1.5 | 全网规划 | [**ADD TWAMPLOGICINF**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPAPM功能管理/TWAMP/本端逻辑接口配置/增加本地逻辑接口（ADD TWAMPLOGICINF）_27262282.md)<br>- 逻辑接口使用N3/S1-U接口。<br>- “VRFNAME”已通过**[ADD TWAMPVPNINST](../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPAPM功能管理/TWAMP/VPN实例/增加VPN实例名称（ADD TWAMPVPNINST）_27102474.md)**配置。<br>- 如果逻辑接口与业务的N3/S1-U接口共用IP地址，[**ADD TWAMPLOGICINF**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPAPM功能管理/TWAMP/本端逻辑接口配置/增加本地逻辑接口（ADD TWAMPLOGICINF）_27262282.md)命令中“SHAREDTYPE”需设置为“TRUE”。<br>- 如果逻辑接口与业务的N3/S1-U接口不共用IP地址，[**ADD TWAMPLOGICINF**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPAPM功能管理/TWAMP/本端逻辑接口配置/增加本地逻辑接口（ADD TWAMPLOGICINF）_27262282.md)命令中“SHAREDTYPE”需设置为“FALSE”。 |
| 逻辑接口 | 逻辑接口掩码（IPV4MASK） | 255.255.255.255 | 全网规划 | [**ADD TWAMPLOGICINF**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPAPM功能管理/TWAMP/本端逻辑接口配置/增加本地逻辑接口（ADD TWAMPLOGICINF）_27262282.md)<br>- 逻辑接口使用N3/S1-U接口。<br>- “VRFNAME”已通过**[ADD TWAMPVPNINST](../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPAPM功能管理/TWAMP/VPN实例/增加VPN实例名称（ADD TWAMPVPNINST）_27102474.md)**配置。<br>- 如果逻辑接口与业务的N3/S1-U接口共用IP地址，[**ADD TWAMPLOGICINF**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPAPM功能管理/TWAMP/本端逻辑接口配置/增加本地逻辑接口（ADD TWAMPLOGICINF）_27262282.md)命令中“SHAREDTYPE”需设置为“TRUE”。<br>- 如果逻辑接口与业务的N3/S1-U接口不共用IP地址，[**ADD TWAMPLOGICINF**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPAPM功能管理/TWAMP/本端逻辑接口配置/增加本地逻辑接口（ADD TWAMPLOGICINF）_27262282.md)命令中“SHAREDTYPE”需设置为“FALSE”。 |
| 逻辑接口 | VPN实例名称（VRFNAME） | VPN_CN | 全网规划 | [**ADD TWAMPLOGICINF**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPAPM功能管理/TWAMP/本端逻辑接口配置/增加本地逻辑接口（ADD TWAMPLOGICINF）_27262282.md)<br>- 逻辑接口使用N3/S1-U接口。<br>- “VRFNAME”已通过**[ADD TWAMPVPNINST](../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPAPM功能管理/TWAMP/VPN实例/增加VPN实例名称（ADD TWAMPVPNINST）_27102474.md)**配置。<br>- 如果逻辑接口与业务的N3/S1-U接口共用IP地址，[**ADD TWAMPLOGICINF**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPAPM功能管理/TWAMP/本端逻辑接口配置/增加本地逻辑接口（ADD TWAMPLOGICINF）_27262282.md)命令中“SHAREDTYPE”需设置为“TRUE”。<br>- 如果逻辑接口与业务的N3/S1-U接口不共用IP地址，[**ADD TWAMPLOGICINF**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPAPM功能管理/TWAMP/本端逻辑接口配置/增加本地逻辑接口（ADD TWAMPLOGICINF）_27262282.md)命令中“SHAREDTYPE”需设置为“FALSE”。 |
| 逻辑接口 | 是否共地址（SHAREDTYPE） | TRUE | 全网规划 | [**ADD TWAMPLOGICINF**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPAPM功能管理/TWAMP/本端逻辑接口配置/增加本地逻辑接口（ADD TWAMPLOGICINF）_27262282.md)<br>- 逻辑接口使用N3/S1-U接口。<br>- “VRFNAME”已通过**[ADD TWAMPVPNINST](../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPAPM功能管理/TWAMP/VPN实例/增加VPN实例名称（ADD TWAMPVPNINST）_27102474.md)**配置。<br>- 如果逻辑接口与业务的N3/S1-U接口共用IP地址，[**ADD TWAMPLOGICINF**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPAPM功能管理/TWAMP/本端逻辑接口配置/增加本地逻辑接口（ADD TWAMPLOGICINF）_27262282.md)命令中“SHAREDTYPE”需设置为“TRUE”。<br>- 如果逻辑接口与业务的N3/S1-U接口不共用IP地址，[**ADD TWAMPLOGICINF**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPAPM功能管理/TWAMP/本端逻辑接口配置/增加本地逻辑接口（ADD TWAMPLOGICINF）_27262282.md)命令中“SHAREDTYPE”需设置为“FALSE”。 |
| 探测路径 | 客户端会话ID（CLIENTID） | 1 | 全网规划 | [**ADD TWAMPCLIENT**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPAPM功能管理/TWAMP/TWAMP客户端配置/增加TWAMP客户端（ADD TWAMPCLIENT）_27102472.md)<br>“LOCALIPV4”<br>必须和用于探测的逻辑接口IP地址一致。<br>“VRFNAME”<br>已通过<br>**[ADD TWAMPVPNINST](../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPAPM功能管理/TWAMP/VPN实例/增加VPN实例名称（ADD TWAMPVPNINST）_27102474.md)**<br>配置。 |
| 探测路径 | TWAMP架构（TWAMPARCH） | LIGHT | 全网规划 | [**ADD TWAMPCLIENT**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPAPM功能管理/TWAMP/TWAMP客户端配置/增加TWAMP客户端（ADD TWAMPCLIENT）_27102472.md)<br>“LOCALIPV4”<br>必须和用于探测的逻辑接口IP地址一致。<br>“VRFNAME”<br>已通过<br>**[ADD TWAMPVPNINST](../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPAPM功能管理/TWAMP/VPN实例/增加VPN实例名称（ADD TWAMPVPNINST）_27102474.md)**<br>配置。 |
| 探测路径 | 地址族类型（AFTYPE） | IPV4 | 全网规划 | [**ADD TWAMPCLIENT**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPAPM功能管理/TWAMP/TWAMP客户端配置/增加TWAMP客户端（ADD TWAMPCLIENT）_27102472.md)<br>“LOCALIPV4”<br>必须和用于探测的逻辑接口IP地址一致。<br>“VRFNAME”<br>已通过<br>**[ADD TWAMPVPNINST](../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPAPM功能管理/TWAMP/VPN实例/增加VPN实例名称（ADD TWAMPVPNINST）_27102474.md)**<br>配置。 |
| 探测路径 | 本端IPv4地址（LOCALIPV4） | 10.1.1.5 | 全网规划 | [**ADD TWAMPCLIENT**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPAPM功能管理/TWAMP/TWAMP客户端配置/增加TWAMP客户端（ADD TWAMPCLIENT）_27102472.md)<br>“LOCALIPV4”<br>必须和用于探测的逻辑接口IP地址一致。<br>“VRFNAME”<br>已通过<br>**[ADD TWAMPVPNINST](../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPAPM功能管理/TWAMP/VPN实例/增加VPN实例名称（ADD TWAMPVPNINST）_27102474.md)**<br>配置。 |
| 探测路径 | 对端IPv4地址（PEERIPV4） | 10.2.2.5 | 全网规划 | [**ADD TWAMPCLIENT**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPAPM功能管理/TWAMP/TWAMP客户端配置/增加TWAMP客户端（ADD TWAMPCLIENT）_27102472.md)<br>“LOCALIPV4”<br>必须和用于探测的逻辑接口IP地址一致。<br>“VRFNAME”<br>已通过<br>**[ADD TWAMPVPNINST](../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPAPM功能管理/TWAMP/VPN实例/增加VPN实例名称（ADD TWAMPVPNINST）_27102474.md)**<br>配置。 |
| 探测路径 | 本端UDP端口（LLOCALUDPPORT） | 65450 | 全网规划 | [**ADD TWAMPCLIENT**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPAPM功能管理/TWAMP/TWAMP客户端配置/增加TWAMP客户端（ADD TWAMPCLIENT）_27102472.md)<br>“LOCALIPV4”<br>必须和用于探测的逻辑接口IP地址一致。<br>“VRFNAME”<br>已通过<br>**[ADD TWAMPVPNINST](../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPAPM功能管理/TWAMP/VPN实例/增加VPN实例名称（ADD TWAMPVPNINST）_27102474.md)**<br>配置。 |
| 探测路径 | 对端UDP端（LPEERUDPPORT） | 1025 | 全网规划 | [**ADD TWAMPCLIENT**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPAPM功能管理/TWAMP/TWAMP客户端配置/增加TWAMP客户端（ADD TWAMPCLIENT）_27102472.md)<br>“LOCALIPV4”<br>必须和用于探测的逻辑接口IP地址一致。<br>“VRFNAME”<br>已通过<br>**[ADD TWAMPVPNINST](../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPAPM功能管理/TWAMP/VPN实例/增加VPN实例名称（ADD TWAMPVPNINST）_27102474.md)**<br>配置。 |
| 探测路径 | VPN实例名称（VRFNAME） | VPN_CN | 全网规划 | [**ADD TWAMPCLIENT**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPAPM功能管理/TWAMP/TWAMP客户端配置/增加TWAMP客户端（ADD TWAMPCLIENT）_27102472.md)<br>“LOCALIPV4”<br>必须和用于探测的逻辑接口IP地址一致。<br>“VRFNAME”<br>已通过<br>**[ADD TWAMPVPNINST](../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPAPM功能管理/TWAMP/VPN实例/增加VPN实例名称（ADD TWAMPVPNINST）_27102474.md)**<br>配置。 |
| 探测报文参数 | 客户端会话ID（CLIENTID） | 1 | 全网规划 | [**ADD TWAMPSENDER**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPAPM功能管理/TWAMP/TWAMP发送端配置/增加TWAMP发送端（ADD TWAMPSENDER）_73302045.md) |
| 探测报文参数 | 超时时间（TIMEOUT） | 5 | 全网规划 | [**ADD TWAMPSENDER**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPAPM功能管理/TWAMP/TWAMP发送端配置/增加TWAMP发送端（ADD TWAMPSENDER）_73302045.md) |
| TWAMP的Light模式“链路丢包率过高告警”配置 | 阈值（THRESHOLD） | 30 | 全网规划 | [**SET LINKALMCFG**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPAPM功能管理/TWAMP/IPAPM链路告警配置/设置TWAMP的Light模式“链路丢包率过高告警”配置（SET LINKALMCFG）_73302055.md) |
| TWAMP的Light模式“链路丢包率过高告警”配置 | 恢复阈值（CLEARTHRESHOLD） | 10 | 全网规划 | [**SET LINKALMCFG**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPAPM功能管理/TWAMP/IPAPM链路告警配置/设置TWAMP的Light模式“链路丢包率过高告警”配置（SET LINKALMCFG）_73302055.md) |
| TWAMP的Light模式“链路丢包率过高告警”配置 | 检测周期（PERIOD） | 40 | 全网规划 | [**SET LINKALMCFG**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPAPM功能管理/TWAMP/IPAPM链路告警配置/设置TWAMP的Light模式“链路丢包率过高告警”配置（SET LINKALMCFG）_73302055.md) |

## [操作步骤](#ZH-CN_OPI_0000001142385398)

1. 检查IPAPM是否已安装，若未安装，请完成IPAPM安装，参见 [安装IPAPM服务](../../../../../网络部署/软件安装/基于VNF LCM安装UDG（非SDN）/安装可选服务/安装IPAPM服务_35204486.md) 。
  预期结果：“未就绪进程数”和“故障进程数”均为0。
  ```
  DSP CELLSTAT: OBJECT=PODTYPE, PODTYPE="ipapmctrl-pod";
  DSP CELLSTAT: OBJECT=PODTYPE, PODTYPE="ipapmexec-pod";
  ```
2. 打开本特性的Licence开关。
  [**SET LICENSESWITCH**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09587387.md)
3. 配置本端探测逻辑接口。
  **[ADD TWAMPVPNINST](../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPAPM功能管理/TWAMP/VPN实例/增加VPN实例名称（ADD TWAMPVPNINST）_27102474.md)**
  [**ADD TWAMPLOGICINF**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPAPM功能管理/TWAMP/本端逻辑接口配置/增加本地逻辑接口（ADD TWAMPLOGICINF）_27262282.md)
  > **说明**
  > 使用命令 [**ADD TWAMPLOGICINF**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPAPM功能管理/TWAMP/本端逻辑接口配置/增加本地逻辑接口（ADD TWAMPLOGICINF）_27262282.md) 配置本端探测逻辑接口时，若与业务的N3/S1-U接口共用IP地址， [**ADD TWAMPLOGICINF**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPAPM功能管理/TWAMP/本端逻辑接口配置/增加本地逻辑接口（ADD TWAMPLOGICINF）_27262282.md) 命令中 “SHAREDTYPE” 参数取值需配置为 “TRUE” 。
4. 配置本端对端设备的探测路径。
  [**ADD TWAMPCLIENT**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPAPM功能管理/TWAMP/TWAMP客户端配置/增加TWAMP客户端（ADD TWAMPCLIENT）_27102472.md)
5. 配置探测路径对应的报文参数。
  [**ADD TWAMPSENDER**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPAPM功能管理/TWAMP/TWAMP发送端配置/增加TWAMP发送端（ADD TWAMPSENDER）_73302045.md)
6. 配置“ [ALM-100395 链路丢包率过高告警](../../../../../网络运维/故障处理/Framework告警/ALM-100395 链路丢包率过高告警_80156359.md) ”上报的相关阈值。
  [**SET LINKALMCFG**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPAPM功能管理/TWAMP/IPAPM链路告警配置/设置TWAMP的Light模式“链路丢包率过高告警”配置（SET LINKALMCFG）_73302055.md)

## [任务示例](#ZH-CN_OPI_0000001142385398)

任务描述

检测本端网元与对端设备的网络传输质量，激活TWAMP功能，激活后丢包、时延、抖动等性能统计结果会实时上报网管系统。

脚本

//打开本特性的License配置开关。

```
SET LICENSESWITCH:LICITEM="LKV3G5TWMP01",SWITCH=ENABLE;
```

//配置探测逻辑接口。

```
ADD TWAMPVPNINST: VRFNAME="VPN_CN";
ADD TWAMPLOGICINF: NAME="n3if1/1/0", AFTYPE=IPV4, IPV4ADDRESS="10.1.1.5", IPV4MASK="255.255.255.255", VRFNAME="VPN_CN", SHAREDTYPE=TRUE;
```

//配置探测路径。

```
ADD TWAMPCLIENT:CLIENTID=1,TWAMPARCH=LIGHT,AFTYPE=IPV4,LOCALIPV4="10.1.1.5",PEERIPV4="10.2.2.5",LLOCALUDPPORT=65450,LPEERUDPPORT=1025,VRFNAME="VPN_CN";
```

//配置探测报文参数。

```
ADD TWAMPSENDER:CLIENTID=1,TIMEOUT=5;
```

//设置TWAMP的Light模式“ [ALM-100395 链路丢包率过高告警](../../../../../网络运维/故障处理/Framework告警/ALM-100395 链路丢包率过高告警_80156359.md) ”参数。

```
SET LINKALMCFG: THRESHOLD=30, CLEARTHRESHOLD=10, PERIOD=40;
```
