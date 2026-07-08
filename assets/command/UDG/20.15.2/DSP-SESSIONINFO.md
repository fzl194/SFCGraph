---
id: UDG@20.15.2@MMLCommand@DSP SESSIONINFO
type: MMLCommand
name: DSP SESSIONINFO（显示用户上下文）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: SESSIONINFO
command_category: 查询类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 会话管理
- 会话信息管理
- 会话信息查询
status: active
---

# DSP SESSIONINFO（显示用户上下文）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

用来查看指定用户上下文信息。

## 注意事项

根据IMEI查询用户只匹配前14位。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QUERYTYPE | 查询方式 | 可选必选说明：必选参数<br>参数含义：查询方式。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- IMSI：指定待查询用户的IMSI号。<br>- MSISDN：指定待查询用户的MSISDN号。<br>- IPV4：指定待查询用户所使用的IPv4地址。<br>- IMEI：指定待查询用户的IMEI号。<br>- IPV6：指定待查询用户所使用的IPv6地址。<br>- VNINSTANCE：指定用VNINSTANCE的方式查询当前5GLAN的组会话信息。<br>- TRUNKGROUPID：宽带集群群组ID。<br>- MBS_SEID：指定查询用户的mbs会话标识。<br>- MBMS_TMGI：指定查询用户的MBMS会话TMGI。<br>- ToH_VNINSTANCE：按家庭组ID的方式查询当前家庭组下的会话信息。<br>默认值：无<br>配置原则：无 |
| IMSI | 用户IMSI号 | 可选必选说明：条件必选参数<br>前提条件：该参数在“QUERYTYPE”配置为“IMSI”时为必选参数。<br>参数含义：用户的IMSI信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～15。每个字符必须为0~9的数字。 IMSI由三部分组成： 1、Mobile Country Code (MCC)包含3个数字。MCC唯一标识移动用户的居住国家。 2、Mobile Network Code (MNC)包含2个或3个数字用于GSM/UMTS应用。MNC标识移动用户的归属PLMN。MNC的长度取决于MCC的值。 3、Mobile Subscriber Identification Number (MSIN)标识PLMN内的移动用户。<br>默认值：无<br>配置原则：无 |
| MSISDN | 用户MSISDN号 | 可选必选说明：条件必选参数<br>前提条件：该参数在“QUERYTYPE”配置为“MSISDN”时为必选参数。<br>参数含义：用户的MSISDN信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～15。每个字符必须为0~9的数字。 MSISDN号的组成： 1、用户注册的国家的Country Code (CC) 2、国家移动号，组成如下：National Destination Code (NDC)；Subscriber Number (SN)。<br>默认值：无<br>配置原则：无 |
| IMEI | 用户IMEI号 | 可选必选说明：条件必选参数<br>前提条件：该参数在“QUERYTYPE”配置为“IMEI”时为必选参数。<br>参数含义：用户的IMEI信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～16。每个字符必须为0~9的数字。 IMEI号的组成： 1、前6位或者8位是型号核准码(TAC)，用来区分手机品牌和型号。 2、接着2位是最后装配号(FAC)，代表最终装配地代码，仅在早期机型中存在。 3、后6位是串号(SNR)，代表生成顺序号。<br>默认值：无<br>配置原则：无 |
| IPV4ADDR | IPv4地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“QUERYTYPE”配置为“IPV4”时为必选参数。<br>参数含义：IPv4地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。点分十进制格式。<br>默认值：无<br>配置原则：无 |
| IPV6ADDR | IPv6地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“QUERYTYPE”配置为“IPV6”时为必选参数。<br>参数含义：IPv6地址。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。冒号分十六进制，格式为X:X:X:X:X:X:X:X。输入用户实际前缀长度的IP地址，后面补0查询。<br>默认值：无<br>配置原则：无 |
| DISPLAYMODE | 显示方式 | 可选必选说明：条件可选参数<br>前提条件：该参数在“QUERYTYPE”配置为“IMEI”、“IMSI”、“IPV4”、“IPV6”、“MSISDN” 或 “VNINSTANCE”时为可选参数。<br>参数含义：该参数用于指定显示方式。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- SIMPLE：使用简单显示模式进行查询会话信息。<br>- VERBOSE：使用详细显示模式进行查询会话信息。<br>默认值：无<br>配置原则：无 |
| VNINSTANCE | 5G LAN 组名称 | 可选必选说明：条件必选参数<br>前提条件：该参数在“QUERYTYPE”配置为“VNINSTANCE”时为必选参数。<br>参数含义：表示用户的5G Lan组会话实例信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～37。VNINSTANCE以连字号分为4段，形式为GroupServiceID-MCC-MNC-LocalGroupID。其中，GroupServiceID长度为8，只能输入数字或者范围为A到F或a-f的字母；MCC长度为3，只能输入数字；MNC长度为2~3，只能输入数字；LocalGroupID长度为2~10的偶数，只能输入数字或者范围为A到F或a-f的字母。例如，A0000001-460-003-01，A0000001-460-003-A000000001。不区分大小写。<br>默认值：无<br>配置原则：无 |
| APN | APN名称 | 可选必选说明：条件可选参数<br>前提条件：该参数在“QUERYTYPE”配置为“IMEI”、“IMSI” 或 “MSISDN”时为可选参数。<br>参数含义：该参数用于指定APN实例名。该APN必须在系统上已经配置。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格及部分特殊字符。可以支持的特殊字符有“.”和“-”，“.”不可以是第一个字符且不可以连续出现。<br>默认值：无<br>配置原则：无 |
| TRUNKGROUPID | 宽带集群群组ID | 可选必选说明：条件必选参数<br>前提条件：该参数在“QUERYTYPE”配置为“TRUNKGROUPID”时为必选参数。<br>参数含义：宽带集群群组会话ID。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1~11，只能包含字符0~9，f，F。<br>默认值：无<br>配置原则：无 |
| UEINFODISSW | UE信息显示开关 | 可选必选说明：条件可选参数<br>前提条件：该参数在“QUERYTYPE”配置为“VNINSTANCE”时为可选参数。<br>参数含义：该参数用于配置是否显示5G LAN组内UE会话的转发表项信息。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |
| UEIMSI | IMSI | 可选必选说明：条件必选参数<br>前提条件：该参数在“UEINFODISSW”配置为“ENABLE”时为必选参数。<br>参数含义：5G LAN用户的IMSI。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～15。每个字符必须为0~9的数字。 IMSI由三部分组成： 1、Mobile Country Code (MCC)包含3个数字。MCC唯一标识移动用户的居住国家。 2、Mobile Network Code (MNC)包含2个或3个数字用于GSM/UMTS应用。MNC标识移动用户的归属PLMN。MNC的长度取决于MCC的值。 3、Mobile Subscriber Identification Number (MSIN)标识PLMN内的移动用户。<br>默认值：无<br>配置原则：无 |
| IGMPGRPDISSW | IGMP组播组信息显示开关 | 可选必选说明：条件可选参数<br>前提条件：该参数在“QUERYTYPE”配置为“VNINSTANCE”时为可选参数。<br>参数含义：该参数用于配置是否显示5G LAN组内的IGMP组播组信息。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |
| MCC | 移动国家码 | 可选必选说明：条件必选参数<br>前提条件：该参数在“QUERYTYPE”配置为“MBS_SEID” 或 “MBMS_TMGI”时为必选参数。<br>参数含义：该参数用于指定移动国家码。<br>数据来源：全网规划<br>取值范围：字符串类型，为3位数字，000～999。<br>默认值：无<br>配置原则：无 |
| MNC | 移动网络号 | 可选必选说明：条件必选参数<br>前提条件：该参数在“QUERYTYPE”配置为“MBS_SEID” 或 “MBMS_TMGI”时为必选参数。<br>参数含义：该参数用于指定移动网络号。<br>数据来源：全网规划<br>取值范围：字符串类型，可为2或3位数字，00~99或000~999。<br>默认值：无<br>配置原则：无 |
| MBSSERVICEID | MBS Service ID | 可选必选说明：条件必选参数<br>前提条件：该参数在“QUERYTYPE”配置为“MBS_SEID”时为必选参数。<br>参数含义：MBS服务标识。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～6。每个字符必须为0~9的数字或者a~f/A~F的字母。MBS Service ID由3个八位字节组成，用于标识一个服务区。<br>默认值：无<br>配置原则：无 |
| MBMSSERVICEID | MBMS服务ID | 可选必选说明：条件必选参数<br>前提条件：该参数在“QUERYTYPE”配置为“MBMS_TMGI”时为必选参数。<br>参数含义：MBMS服务标识。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～6。每个字符必须为0~9的数字或者a~f/A~F的字母。MBMS Service ID由3个八位字节组成，用于标识一个服务区。<br>默认值：无<br>配置原则：无 |
| TOH_VNINSTANCE | 用户的家庭组ID | 可选必选说明：条件必选参数<br>前提条件：该参数在“QUERYTYPE”配置为“ToH_VNINSTANCE”时为必选参数。<br>参数含义：表示用户的家庭组ID。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～37。不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/SESSIONINFO]] · 用户上下文（SESSIONINFO）

## 使用实例

- 查询用户上下文，IMSI为“176456789012342”：
  ```
  DSP SESSIONINFO: QUERYTYPE=IMSI,IMSI="176456789012342";
  ```
  ```

  RETCODE = 0  操作成功

  上下文信息
  ------------
  Result  =
  PDP context on Pod: ssgpod-0131-30-0-240
  -------------------------------
                               IMSI  =  176456789012342
                               IMEI  =  123456789012371
                             MSISDN  =  12341234
                         Local Seid  =  0x0000000000840009
                          Peer Seid  =  0x0000000000000001
                    Local Signal IP  =  10.2.176.131
                     Peer Signal IP  =  10.70.176.15
                  IPv4 VPN instance  =  NULL
                  IPv6 VPN instance  =  NULL
                                APN  =  0176apn1.com
                           PDP Type  =  IPv4
                  IPv4 Address type  =  EXTERNAL ALLOC IP ADDRESS
                   IPv4 PDP address  =  10.2.0.1
               IPv4 Redundancy Flag  =  false
                           RAT Type  =  UNKNOWN
                          Role Type  =  SPGW-U
                          User Type  =  home
                         Proxy Type  =  ProxyUPF User
                          DNAI Flag  =  false
                      DNAI VPN Flag  =  false
                          DCNR Flag  =  false
                    Maintained Flag  =  false
       Session Activation Timestamp  =  16:32:34 08/18/2022(MM/DD/YYYY)
                 Common Policy Name  =  up1
                          Af Switch  =  DISABLE
             Ipv6InterfaceId Switch  =  DISABLE
                          L2TP Flag  =  false
      CU Configuration Inconsistent  =  false
           High-Bandwidth User Flag  =  false
                         Relay Flag  =  false
                          CP NodeID  =  0.0.0.0
                           UAC Flag  =  true
                       Network Type  =  public network
                           NAT Flag  =  false
                   Tethering Switch  =  DISABLE
               Online Charge Switch  =  Default
              OffLine Charge Switch  =  ON
                        Roaming Type = Inbound
            QoS Experience User Flag = false
     Common QoS Experience User Flag = false

                             PDR ID  =  1
                         Precedence  =  4294967280
                              Teidu  =  0x00000001
                   Source Interface  =  access
                 Local Interface IP  =  10.2.176.19
                    Classifier Flag  =  Disable
                           IMS FLAG  =  0
                      Linked FAR ID  =  1
                      Linked URR ID  =  49462(Dynamic)
                      Linked QER ID  =  1

                             PDR ID  =  2
                         Precedence  =  4294967280
                   Source Interface  =  core
                    Classifier Flag  =  Disable
                           IMS FLAG  =  0
                      Linked FAR ID  =  2
                      Linked URR ID  =  49462(Dynamic)
                      Linked QER ID  =  1

                             FAR ID  =  1
                       Apply Action  =  Forward
                Classifier To Local  =  Disable
              Destination Interface  =  core

                             FAR ID  =  2
                       Apply Action  =  Forward
                Classifier To Local  =  Disable
              Destination Interface  =  access
                         Peer Teidu  =  0x00000001
                       Peer Data IP  =  10.2.0.2

                             QER ID  =  1
                           QER Type  =  APN Session
                        UpLink Gate  =  Open
                      DownLink Gate  =  Open
                         Uplink MBR  =  1000000kbps
                       Downlink MBR  =  1000000kbps
                    Real Uplink MBR  =  1000000kbps
                  Real Downlink MBR  =  1000000kbps

                             URR ID  =  49462(Dynamic)
                 Measurement Method  =  Duration
                 Measurement Method  =  Volume
                 Reporting Triggers  =  Volume Threshold
                 Reporting Triggers  =  Time Threshold
             Total Volume Threshold  =  102400
                     Time Threshold  =  102400
  Rule information
  ----------------
  No    State     Priority    Name   Type  CRBN
  1     Active    1000        rule1  pcc   up1
  2     Active    1020        rule2  pcc   up1
  SRR Information
  ----------------
  SRR ID      QFI                 Requested QoS Monitoring  Reporting Frequency    DownlinkPktDelayThd  UplinkPktDelayThd  RoundTripPktDelayThd  Minimum Wait Time  Measurement Period
  1           -                   -                         -                      -                    -                  -                     -                  -
  SRR Direct Reporting Information
  ----------------
  SRR ID      Correlation ID             Reporting Flags        URI Status         URI
  1           132456987                  0                      Normal             Http://127.0.0.0:8836
  SRR QoS Experience Routing Information
  ----------------
  SRR ID      IPV4                IPV6
  1           -                   -
  SRR QoS Analysis Information
  ----------------
  SRR ID      No                  App Index                 App Name
  1           1                   0                         Appid01
  -           2                   1                         Appid02
  SRR QoS Experience AppId Information
  ----------------
  SRR ID      No                  App Index                 App Name
  1           -                   -                         -
  (结果个数 = 1)

  ---    END
  ```
- 查询用户上下文，TrunkGroupId为“12345678912”：
  ```
  DSP SESSIONINFO: QUERYTYPE=TRUNKGROUPID, TRUNKGROUPID="12345678912";
  ```
  ```

  RETCODE = 0  操作成功

  上下文信息
  ------------
  Result  =
  PDP context on Pod: ssgpod-0134-30-1-30
  -------------------------------
                        TM GROUP ID  =  12345678912
                         Local Teid  =  0x0000000064000016
                          Peer Teid  =  0x0000000000000000
                    Local Signal IP  =  10.2.48.49
                     Peer Signal IP  =  10.2.0.3
       Session Activation Timestamp  =  09:39:49 08/30/2022(MM/DD/YYYY)

              Trunk Flow Identifier  =  1
                 Trunk Bearer Flags  =  Transparent Video Bearer
          Pre-emption Vulnerability  =  1
                     Priority Level  =  1
             Pre-emption Capability  =  1
                                QCI  =  3
                       UL MBR(kbps)  =  0
                       DL MBR(kbps)  =  0
                       UL GBR(kbps)  =  0
                       DL GBR(kbps)  =  0
                       Tx-U Peer IP  =  10.2.0.4
                     Tx-U Peer Port  =  22100
                      Tx-U Local IP  =  10.2.48.51
                    Tx-U Local Port  =  30209
                      S1-U SGW IPv4  =  10.2.48.19
                     S1-U SGW Teidu  =  1677787465

              Trunk Flow Identifier  =  2
                 Trunk Bearer Flags  =  Transparent Audio Bearer
          Pre-emption Vulnerability  =  0
                     Priority Level  =  2
             Pre-emption Capability  =  1
                                QCI  =  4
                       UL MBR(kbps)  =  0
                       DL MBR(kbps)  =  0
                       UL GBR(kbps)  =  0
                       DL GBR(kbps)  =  0
                       Tx-U Peer IP  =  10.2.0.5
                     Tx-U Peer Port  =  22200
                      Tx-U Local IP  =  10.2.48.51
                    Tx-U Local Port  =  20209
                      S1-U SGW IPv4  =  10.2.48.19
                     S1-U SGW Teidu  =  1677787466

  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示用户上下文（DSP-SESSIONINFO）_86526407.md`
