---
id: UDG@20.15.2@MMLCommand@DSP FLOWSTATISTICS
type: MMLCommand
name: DSP FLOWSTATISTICS（查询业务统计信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: FLOWSTATISTICS
command_category: 查询类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务运维
- 业务统计管理
- 业务统计信息结果查询
status: active
---

# DSP FLOWSTATISTICS（查询业务统计信息）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用来查看指定用户的TCP/QUIC业务质量监控信息。

## 注意事项

- 单用户TCP/QUIC业务质量监控最多支持统计100条流。
- 当用户上下文在线时，通过该命令显示指定用户的TCP/QUIC业务质量监控信息（必须先启动此用户的TCP/QUIC业务质量监控）。开启指定用户的TCP/QUIC业务质量监控功能需要在CSP的用户跟踪界面上选择FLOW_STATISTICS消息类型。勾选FLOW_STATISTICS后，用户激活后，进行TCP/QUIC业务后每隔20秒会上报一个FLOW-STATISTICS消息，其中包含了该用户所需要上报的流信息。业务质量监控启动和停止（包括去激活）时分别上报一条EMS消息，表明此用户是否被选定进行业务质量监控，因此用户跟踪建议同时开启EMS。
- 系统设备割接、升级、扩容、参数调整、新业务部署（SA、TCP/QUIC/网页/视频优化等业务），以及单用户业务质量问题定位（速率慢、时延大等）等场景下，通过单用户TCP/QUIC业务质量监控的手段，能够方便的获取用户TCP/QUIC业务质量信息，用于评估业务质量，提升维护和定位效率。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| USERID | 用户标识 | 可选必选说明：必选参数<br>参数含义：用户标识类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- IMSI：用户的IMSI号。<br>- MSISDN：用户的MSISDN号。<br>- IMEI：用户的IMEI号。<br>默认值：无<br>配置原则：无 |
| IMSI | IMSI | 可选必选说明：条件必选参数<br>前提条件：该参数在“USERID”配置为“IMSI”时为必选参数。<br>参数含义：指定待查询用户的IMSI号。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～15。每个字符必须为0～9的数字。<br>默认值：无<br>配置原则：无 |
| MSISDN | MSISDN | 可选必选说明：条件必选参数<br>前提条件：该参数在“USERID”配置为“MSISDN”时为必选参数。<br>参数含义：指定待查询用户的MSISDN号。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～15。每个字符必须为0～9的数字。<br>默认值：无<br>配置原则：无 |
| IMEI | IMEI | 可选必选说明：条件必选参数<br>前提条件：该参数在“USERID”配置为“IMEI”时为必选参数。<br>参数含义：指定待查询用户的IMEI号。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～16。每个字符必须为0～9的数字。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [业务统计信息（FLOWSTATISTICS）](configobject/UDG/20.15.2/FLOWSTATISTICS.md)

## 使用实例

查询单用户的业务质量监控信息：

```
DSP FLOWSTATISTICS: USERID=IMSI,IMSI="2456789012342";
```

```

User Info
---------
Flow Statistics Info  =  
-----------------
User Info: IMSI = 2456789012342 MSISDN = 12341234 IMEI = 123456789012371
-----------------
TCP Flow Info:
---------

No.                           0
ipVer                         :4
msip[0]                       :0xd6025f01
msip[1]                       :0x00000000
msip[2]                       :0x00000000
msip[3]                       :0x00000000
serverip[0]                   :0x131e02b4
serverip[1]                   :0x00000000
serverip[2]                   :0x00000000
serverip[3]                   :0x00000000
msPort                        :554
serverPort                    :1079
teidc                         :2
creatDirFlag                  :1
useState                      :2
tcpConnectionStatus           :0
startTime                     :553746997
lastTime                      :553746997
onlineTime                    :<2
ueToCNRTT                     :65535
cnToServerRTT                 :65535
msMss                         :0
serverMss                     :0
msSackFlag                    :0
serverSackFlag                :0
msWinScale                    :0
serverWinScale                :0
msWinSize                     :0
serverWinSize                 :0
upRanDiscardPktNum            :0
upSPDiscardPktNum             :0
upRanSlowDisorderPktNum       :0
upRanFastDisorderPktNum       :0
dnRanDiscardPktNum            :0
dnSPDiscardPktNum             :0
dnSPSlowDisorderPktNum        :0
dnSPFastDisorderPktNum        :0
ranAverageRtt                 :<2
spAverageRtt                  :<2
upInPktNum                    :0
upOutPktNum                   :0
dnInPktNum                    :1
dnOutPktNum                   :1
upInFlowByte                  :0
dnInFlowByte                  :265
upOutFlowByte                 :0
dnOutFlowByte                 :265
upAvgPktLength                :0
dnAvgPktLength                :265
upInIpFragPktNum              :0
upOutIpFragPktNum             :0
dnInIpFragPktNum              :0
dnOutIpFragPktNum             :0
upFirstIpFragNum              :0
dnFirstIpFragNum              :0
upInDisorderPkt               :0
upOutDisorderPkt              :0
dnInDisorderPkt               :0
dnOutDisorderPkt              :0
maxUpPktDelay                 :<2
maxDnPktDelay                 :<2
upPktAvgDelay                 :<2
dnPktAvgDelay                 :<2
teidu                         :9502722
dpeRateMax                    :4
msRecvWnScale                 :0
msRecvWnZeroNum               :0
msRecvWnMax                   :0
msSendNum                     :0
msRecvWnTotal                 :0
msRecvWnAvg                   :0
spRecvWnScale                 :0
spRecvWnZeroNum               :0
spRecvWnMax                   :29920
spSendNum                     :1
spRecvWnTotal                 :29920
spRecvWnAvg                   :29920
upLastAckNumber               :0
dnLastAckNumber               :639411594
upByteInFlightMax             :0
dnByteInFlightMax             :0
upDupAckOne                   :0
upDupAckMax                   :0
upDupAckAll                   :0
dnDupAckOne                   :0
dnDupAckMax                   :0
dnDupAckAll                   :0
upInNotAckAveragePktByte      :0
dnInNotAckAveragePktByte      :265
upOutNotAckAveragePktByte     :0
dnOutNotAckAveragePktByte     :265
upBurstPktNum                 :0
dnBurstPktNum                 :1
upBurstPktByte                :0
dnBurstPktByte                :265
ranMaxJitter                  :0
spMaxJitter                   :0
ranSumJitter                  :0
spSumJitter                   :0
ranAvgJitter                  :0
spAvgJitter                   :0
upRetranPktNum                :0
dnRetranPktNum                :0
upRetranAverageDelay          :0
upRetranMaxDelay              :0
dnRetranAverageDelay          :0
dnRetranMaxDelay              :0

(Number of results = 1)

-----------------
User Info: IMSI = 2456789012342 MSISDN = 12341234 IMEI = 123456789012371
-----------------
QUIC Flow Info:
---------

No.                           0
ipVer                         :4
teidu                         :1
ulConnectionID                :6786571632704945195
dlConnectionID                :6786571632704945195
msip[0]                       :0xd6025f01
msip[1]                       :0x00000000
msip[2]                       :0x00000000
msip[3]                       :0x00000000
serverip[0]                   :0x131e02b4
serverip[1]                   :0x00000000
serverip[2]                   :0x00000000
serverip[3]                   :0x00000000
msPort                        :7716
serverPort                    :443
creatDirFlag                  :0
useState                      :2
startTime                     :185627871
lastTime                      :185629739
onlineTime                    :1868
ulInPkt                       :4
ulOutPkt                      :4
dlInPkt                       :4
dlOutPkt                      :4
ulInBytes                     :2284
ulOutBytes                    :4197
dlInBytes                     :2284
dlOutBytes                    :4197
upAvgPktLength                :571
dnAvgPktLength                :1049
ulInIpFragPkt                 :0
ulOutIpFragPkt                :0
dlInIpFragPkt                 :0
dlOutIpFragPkt                :0
ulInIpFragFirstPkt            :0
dlInIpFragFirstPkt            :0
ulAvgInnerDelay               :<2
dlAvgInnerDelay               :<2
ulMaxInnerDelay               :<2
dlMaxInnerDelay               :<2
ulRanDiscardPkt               :0
dlSPDiscardPkt                :0
ulRanDisorderPkt              :2
dlSPDisorderPkt               :2

(Number of results = 2)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询业务统计信息（DSP-FLOWSTATISTICS）_44865468.md`
