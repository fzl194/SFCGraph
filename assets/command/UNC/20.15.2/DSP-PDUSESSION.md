---
id: UNC@20.15.2@MMLCommand@DSP PDUSESSION
type: MMLCommand
name: DSP PDUSESSION（显示PDU会话）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: PDUSESSION
command_category: 查询类
applicable_nf:
- SMF
- PGW-C
- SGW-C
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 接入管理运维
- 查询PDP上下文信息
status: active
---

# DSP PDUSESSION（显示PDU会话）

## 功能

**适用NF：SMF、PGW-C、SGW-C、GGSN**

该命令用于查询2G/3G/4G/5G的会话上下文信息。

如需查询QoS详细信息请参阅DSP SESSIONQOSINFO命令。

如需查询签约详细信息请参阅DSP SESSIONSUBDATA命令。

## 注意事项

- I-SMF/V-SMF不支持DSP PDUSESSION命令中指定地址（QUERYTYPE为IPV4ADDR或IPV6ADDR）查询会话信息。
- 使用SIMPLE（简约信息呈现）方式查询时，如果当前用户是2B2C漫游双DNN特性用户，且通用DNN会话是4G，专用DNN会话是5G场景，此时查询结果中，针对专用DNN会话的查询记录，EBI字段表示专用DNN会话的PDU Session ID，LBI（即Linked EPS Bearer ID）字段表示专用DNN会话的QFI。
- 使用DETAILED（详细信息呈现）方式查询时，针对只签约了2B2C多DNN漫游分流业务用户的会话，查询结果中ULCL标识不会置为TRUE；针对同时签约了2B2C多DNN漫游分流业务和基于DNAI的ULCL分流业务用户的会话，基于DNAI的ULCL分流业务不生效时，查询结果中ULCL标识不会置为TRUE。
- 以下输出项名称当前版本不支持:Delegated IPv6 Prefix（代理IPv6前缀）、PCRF HOSTNAME（PCRF标识）、Session Charging ID（会话级计费ID）和I-SMF Identifier（I-SMF ID）。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QUERYTYPE | 查询方式 | 可选必选说明：必选参数<br>参数含义：该参数用于指定查询方式。<br>数据来源：本端规划<br>取值范围：<br>- IMSI（用户IMSI号）<br>- MSISDN（用户MSISDN号）<br>- IMEI（用户IMEI号）<br>- IPV4ADDR（IPv4地址）<br>- IPV6ADDR（IPv6地址）<br>默认值：无<br>配置原则：无 |
| IMSI | IMSI | 可选必选说明：该参数在"QUERYTYPE"配置为"IMSI"时为条件必选参数。<br>参数含义：该参数用于指定用户永久标识或者国际移动用户标识。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是5~15。<br>默认值：无<br>配置原则：<br>该参数为2G/3G/4G的输出参数。5G时对应输出为SUPI。 |
| MSISDN | MSISDN | 可选必选说明：该参数在"QUERYTYPE"配置为"MSISDN"时为条件必选参数。<br>参数含义：该参数用于指定一般公共订阅标识或移动台国际ISDN号码。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~15。<br>默认值：无<br>配置原则：无 |
| MEI | IMEI | 可选必选说明：该参数在"QUERYTYPE"配置为"IMEI"时为条件必选参数。<br>参数含义：该参数用于指定永久设备标识、国际移动设备标识或国际移动台设备标识和软件版本。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~16。<br>默认值：无<br>配置原则：无 |
| DSPINFOTYPE | 信息呈现方式 | 可选必选说明：该参数在"QUERYTYPE"配置为"MSISDN"、"IMSI"、"IMEI"时为条件可选参数。<br>参数含义：该参数用于指定信息呈现方式。<br>数据来源：本端规划<br>取值范围：<br>- SIMPLE（简约信息呈现）<br>- DETAILED（详细信息呈现）<br>默认值：SIMPLE<br>配置原则：<br>在"QUERYTYPE"配置为"IMEI"的情况下，此时只有PDU会话请求类型为"Emergency Request"，并且用户的IMSI非法时，本参数才能取值为"DETAILED"。 |
| WLNETWKTYPE | 无线网络类型 | 可选必选说明：该参数在"DSPINFOTYPE"配置为"DETAILED"时为条件必选参数。<br>参数含义：该参数用于指定无线网络类型。<br>数据来源：本端规划<br>取值范围：<br>- NW2G3G4G（2/3/4G网络）<br>- NW5G（5G网络）<br>默认值：无<br>配置原则：无 |
| EBIORNSAPI | EBI或者NSAPI | 可选必选说明：该参数在"WLNETWKTYPE"配置为"NW2G3G4G"时为条件必选参数。<br>参数含义：该参数用于指定链接的EPS承载标识或者网络层服务接入点标识。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~15。<br>默认值：无<br>配置原则：<br>若EBI值为0，表示没有EPS承载标识被分配。 |
| PDUSESSIONID | PDU会话ID | 可选必选说明：该参数在"WLNETWKTYPE"配置为"NW5G"时为条件必选参数。<br>参数含义：该参数用于指定PDU会话ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~255。<br>默认值：无<br>配置原则：<br>可以通过简单查询获取到后作为详细查询的输入参数。 |
| QFI | QoS流ID | 可选必选说明：该参数在"WLNETWKTYPE"配置为"NW5G"时为条件必选参数。<br>参数含义：该参数用于指定QoS流ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~63。<br>默认值：无<br>配置原则：<br>可以通过简单查询获取到后作为详细查询的输入参数。 |
| UEIPV4ADDR | 用户IPv4地址 | 可选必选说明：该参数在"QUERYTYPE"配置为"IPV4ADDR"时为条件必选参数。<br>参数含义：该参数用于表示用户IPv4地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。UE IPV4仅支持SIMPLE查询方式。<br>默认值：无<br>配置原则：无 |
| UEIPV6ADDR | 用户IPv6地址 | 可选必选说明：该参数在"QUERYTYPE"配置为"IPV6ADDR"时为条件必选参数。<br>参数含义：该参数用于表示用户IPv6地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。UE IPV6仅支持SIMPLE查询方式。<br>默认值：无<br>配置原则：无 |
| IPDOMAIN | 用户IP域 | 可选必选说明：该参数在"QUERYTYPE"配置为"IPV4ADDR"时为条件可选参数。<br>参数含义：该参数用于表示用户IPv4地址段归属的域。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。请根据运营商的规划，如果为IPv4类型的地址段划分了域，则需要通过该参数指定。<br>默认值：无<br>配置原则：无 |
| ACCESSTYPE234G | 接入方式 | 可选必选说明：该参数在"WLNETWKTYPE"配置为"NW2G3G4G"时为条件必选参数。<br>参数含义：该参数用于指定接入类型。<br>数据来源：本端规划<br>取值范围：<br>- AT_3GPP_ACCESS（3GPP_ACCESS）<br>- AT_UNTRUSTED_NON_3GPP_ACCESS（UNTRUSTED_NON_3GPP_ACCESS）<br>- AT_TRUSTED_NON_3GPP_ACCESS（TRUSTED_NON_3GPP_ACCESS）<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PDUSESSION]] · PDU会话（PDUSESSION）

## 使用实例

- 查询类型为IMSI，查询方式为简单查询，IMSI为123031700100001：
  ```
  %%DSP PDUSESSION: QUERYTYPE=IMSI, IMSI="123031700100001", DSPINFOTYPE=SIMPLE;%%
  RETCODE = 0  操作成功

  pdusession info
  ---------------
  IMSI             PDU会话ID  APN或者DNN  请求的APN名称/DNN名称  无线接入类型  QoS流ID  QCI或者5QI  QoS流ARP优先级  QoS流ARP抢占能力  QoS流ARP被抢占能力  SNssaiSst/SNssaiSd  QosFlow 5QI 优先级  

  123031700100001  5          huawei.com  huawei.com             NR            1        5           1               MAY_PREEMPT       PREEMPTABLE         1/010101            NULL
  123031700100001  6          huawei.com  huawei.com             NR            1        5           1               MAY_PREEMPT       PREEMPTABLE         1/010101            NULL
  (结果个数 = 2)

  ---    END
  ```
- 查询类型为IMSI，查询方式为详细查询，IMSI为123031700100001，PDUSESIONID为6，无线网络类型为5G，QFI为1的PDU会话信息：
  ```
  %%DSP PDUSESSION: QUERYTYPE=IMSI, IMSI="123031700100001", DSPINFOTYPE=DETAILED, WLNETWKTYPE=NW5G, PDUSESSIONID=5, QFI=1;%%
  RETCODE = 0  操作成功

  pdusession info
  ---------------
                                               IMSI  =  123031700100001
                                             MSISDN  =  8613517000001
                                               IMEI  =  NULL
                                          PDU会话ID  =  6
                                         APN或者DNN  =  huawei.com
                              请求的APN名称/DNN名称  =  huawei.com
                                            虚拟APN  =  NULL
                                           选择方式  =  VERIFIED
                                    最大APN约束信息  =  NoExistingContextsOrRestriction
                                           用户类型  =  Home
                                           服务网络  =  12303
                                       无线接入类型  =  NR
                                           接入类型  =  3GPP_ACCESS
                                             计费ID  =  29360143
                                         用户IP类型  =  IPv4
                                         用户IP信息  =  10.0.0.1
                                           用户IP域  =  NULL
                                     用户IP分配来源  =  SMF
                              当前会话归属的POD编号  =  uncpod-0
                                            PCC模式  =  StaticPcc
                                            QoS流ID  =  1
                                         QCI或者5QI  =  5
                                     QoS流ARP优先级  =  1
                                   QoS流ARP抢占能力  =  MAY_PREEMPT
                                 QoS流ARP被抢占能力  =  PREEMPTABLE
                                 协商的上行最大速率  =  NULL
                                 协商的下行最大速率  =  NULL
                                     本端节点的角色  =  SMF
                               控制面接入连接左端IP  =  10.0.0.2
                               控制面接入连接右端IP  =  10.0.0.3
                               用户面接入隧道左端IP  =  10.0.0.4
                             用户面接入隧道左端TEID  =  0x2
                               用户面接入隧道右端IP  =  10.0.0.5
                             用户面接入隧道右端TEID  =  0x8000903b
                               控制面锚点连接左端IP  =  NULL
                               控制面锚点连接右端IP  =  NULL
                               用户面锚点隧道左端IP  =  NULL
                             用户面锚点隧道左端TEID  =  NULL
                               用户面锚点隧道右端IP  =  NULL
                             用户面锚点隧道右端TEID  =  NULL
                                 SNssaiSst/SNssaiSd  =  1/010101
                                       AMF服务NF ID  =  00000000-0000-0000-0000-000000000011
                                              GUAMI  =  12303000041
                                       用户位置信息  =  TAI:12303760101;NCGI:12303760110201
                                    SM上下文状态URI  =  http://10.0.0.2:33176/nsmf-pdusession/smcontextstatus/v1/sm-contexts/0881be18120a08fd101205003a07d506-#6#00000000-0000-0000-0
                                       UP上下文状态  =  ACTIVATED
                                             PCF ID  =  NULL
                                            SSC模式  =  1
                                          5G SM能力  =  00
                                       SM上下文参考  =  SmfContextRef: <idx: 4, rand: 13, token: 59, value: 2147799099, isInitialLocator:false>
                                           位置状态  =  INVALID
                                   分组数据离线状态  =  NULL
                                  IMS信令上下文标识  =  FALSE
                                     主P-CSCFIP地址  =  NULL
                                     备P-CSCFIP地址  =  NULL
                                             UPF ID  =  upf_instance_1
                                           LADN标识  =  不支持LADN
                                           ULCL标识  =  否
                                 IPv6地址多归属标识  =  否
                      IPv6多归属的PDU会话的IPv6地址  =  NULL
                                           用户时区  =  +08:00
                                       用户激活时间  =  2021-08-23 20:13:44
                       指示终端是否具有NR双连接能力  =  否
                                     协商的发送等级  =  NULL
                                     协商的传递时延  =  NULL
                                       在线计费标识  =  否
                                       离线计费标识  =  否
                               协商的分配保留优先级  =  NULL
                                        PDU会话参考  =  NULL
                       协商后的会话AMBR上行比特速率  =  4000000000 Kbps
                       协商后的会话AMBR下行比特速率  =  20000000 Kbps
                                       会话级计费ID  =  NULL
                                       内容计费标识  =  否
                                           H-SMF ID  =  NULL
                                           I-SMF ID  =  NULL
                                           V-SMF ID  =  NULL
                                       协商计费特征  =  0111
                                      主DNS服务器IP  =  NULL
                                      备DNS服务器IP  =  NULL
                             标识用户是否是L2TP接入  =  否
                              IPv4 P-CSCF Group名称  =  NULL
                              IPv6 P-CSCF Group名称  =  NULL
                              APN AMBR 上行比特速率  =  4000000000 Kbps
                              APN AMBR 下行比特速率  =  20000000 Kbps
                          QoS流可保证的上行比特速率  =  NULL
                              QoS流最大上行比特速率  =  NULL
                              QoS流最大下行比特速率  =  NULL
                          QoS流可保证的下行比特速率  =  NULL
                      从策略而来的反射QoS定时器信息  =  0
                                          签约的DNN  =  huawei.com
                                签约的QoS ARP优先级  =  1
                              签约的默认PDU会话类型  =  IPv4
                              签约的允许PDU会话类型  =  IPv6 IPv4v6
                                      签约的QoS 5QI  =  5
                                签约QoS ARP抢占能力  =  MAY_PREEMPT
                            签约的QoS ARP被抢占能力  =  PREEMPTABLE
                         签约的会话AMBR上行比特速率  =  4000000000 Kbps
                         签约的会话AMBR下行比特速率  =  20000000 Kbps
                                 签约的静态IPv4地址  =  NULL
                             签约的静态IPv6地址前缀  =  NULL
                                 签约的静态IPv6地址  =  NULL
                               当前使用的P-CSCF地址  =  NULL
                                       签约计费特征  =  1111
                                 QosFlow 5QI 优先级  =  NULL
                                       平均窗口大小  =  NULL
                                       最大数据峰值  =  NULL
                              Routing Behind MS标识  =  否
                                       代理IPv6前缀  =  NULL
  SGW计费 Secondary RAT Usage上报的5G上行总流量(KB)  =  0
  SGW计费 Secondary RAT Usage上报的5G下行总流量(KB)  =  0
  PGW计费 Secondary RAT Usage上报的5G上行总流量(KB)  =  0
  PGW计费 Secondary RAT Usage上报的5G下行总流量(KB)  =  0
                                     完整性保护指示  =  不需要
                                       加密保护指示  =  优选
                                       加密保护状态  =  已执行
                       请求的最大上行完整性保护速率  =  64 kbps
                       请求的最大下行完整性保护速率  =  64 kbps
                                       惯性运行状态  =  否
                                   实时位置订阅信息  =  NULL
                          Parking APN激活上下文标记  =  否
                                           PRA信息  =  NULL
                                         5G LAN组ID  =  NULL
                                        QoS监测状态  =  未监测
                                    QoS监测启动时间  =  NULL
                              选择的APN名称/DNN名称  =  NULL
               基于漫游地动态签约的分流策略控制标识  =  否
                                      QoS监测触发源  =  本地配置
                                           业务规则  =  NULL
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-PDUSESSION.md`
