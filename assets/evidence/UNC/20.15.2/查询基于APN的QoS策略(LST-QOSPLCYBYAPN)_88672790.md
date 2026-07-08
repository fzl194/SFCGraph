# 查询基于APN的QoS策略(LST QOSPLCYBYAPN)

- [命令功能](#ZH-CN_TOPIC_0000001388672790__1.3.1.1)
- [注意事项](#ZH-CN_TOPIC_0000001388672790__1.3.2.1)
- [本地用户权限](#ZH-CN_TOPIC_0000001388672790__1.3.3.1)
- [网管用户权限](#ZH-CN_TOPIC_0000001388672790__1.3.4.1)
- [参数说明](#ZH-CN_TOPIC_0000001388672790__1.3.5.1)
- [使用实例](#ZH-CN_TOPIC_0000001388672790__1.3.6.1)
- [输出结果说明](#ZH-CN_TOPIC_0000001388672790__1.3.7.1)

#### [命令功能](#ZH-CN_TOPIC_0000001388672790)

**适用网元：MME**

该命令用于查询基于APN的QoS策略配置。

#### [注意事项](#ZH-CN_TOPIC_0000001388672790)

无。

#### [本地用户权限](#ZH-CN_TOPIC_0000001388672790)

manage-ug；system-ug；monitor-ug

#### [网管用户权限](#ZH-CN_TOPIC_0000001388672790)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_TOPIC_0000001388672790)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RATTYPE | RAT类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定用户的接入类型，系统优先匹配与当前用户所处网络类型相同的配置数据，当相同RAT类型配置中不包含该用户时，再进行<br>“ALL”<br>类型的匹配。<br>数据来源：整网规划<br>取值范围：<br>- “ALL(ALL)”<br>- “GERAN(GERAN)”<br>- “UTRAN(UTRAN)”<br>- “E-UTRAN(E-UTRAN)”<br>- “NB-IoT(NB-IoT)”<br>默认值：无 |
| SUBRANGE | 用户范围 | 可选必选说明：可选参数<br>参数含义：该参数用于指定基于APN的QoS策略配置的用户范围。<br>数据来源：整网规划<br>取值范围：<br>- “IMSI_PREFIX(指定IMSI前缀)”：指网络中与指定的IMSI前缀匹配的用户。<br>- “HOME_USER(本网用户)”：指网络中的本网签约用户。<br>- “FOREIGN_USER(外网用户)”：指网络中的漫游用户。<br>- “ALL_USER(所有用户)”：指网络中的所有用户。<br>默认值：无 |
| NOID | 运营商标识 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定运营商标识。<br>前提条件：该参数在<br>“SUBRANGE（用户范围）”<br>配置为<br>“FOREIGN_USER（外网用户）”<br>或<br>“HOME_USER（本网用户）”<br>后生效。<br>该参数必须先由<br>[**ADD QOSPLCYBYAPN**](增加基于APN的QoS策略(ADD QOSPLCYBYAPN)_88832402.md)<br>命令定义，才能在此处引用。<br>对于外网用户，该参数用于指定与互联PLMN签订漫游协议的本局运营商标识，对于本网用户，该参数是本网用户对应的运营商标识。<br>数据来源：整网规划<br>取值范围：0～64，128～254。<br>默认值：无 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定进行匹配的IMSI前缀。系统根据该参数值对用户的IMSI进行匹配，从而区分不同的用户群。<br>前提条件：该参数在<br>“SUBRANGE（用户范围）”<br>配置为<br>“IMSI_PREFIX（指定IMSI前缀）”<br>后生效。<br>该参数必须先由<br>[**ADD QOSPLCYBYAPN**](增加基于APN的QoS策略(ADD QOSPLCYBYAPN)_88832402.md)<br>命令定义，才能在此处引用。<br>数据来源：整网规划<br>取值范围：5~15位十进制数字字符串<br>默认值：无 |
| APNNI | APNNI | 可选必选说明：可选参数<br>参数含义：该参数用于指定APNNI。<br>前提条件：该参数必须先由<br>[**ADD QOSPLCYBYAPN**](增加基于APN的QoS策略(ADD QOSPLCYBYAPN)_88832402.md)<br>命令定义，才能在此处引用。<br>数据来源：整网规划<br>取值范围：1～62位字符串<br>默认值：无 |

#### [使用实例](#ZH-CN_TOPIC_0000001388672790)

1. 不输入 “RAT类型” ， “用户范围” 及 “APNNI” ，查询所有基于APN的QoS策略配置。
  LST QOSPLCYBYAPN:;
  ```
  %%LST QOSPLCYBYAPN:;%%
  RETCODE = 0  Operation succeeded
 
  The result is as follows
  ------------------------
  RAT Type  Subscriber Range  Network Operator Identity  IMSI Prefix  APNNI        QoS of Non-GBR Bearers Is Controlled by Local Policies  QCI-based QoS Is Controlled by Local Policies  QoS of GBR Bearers Is Controlled by Local Policies  Control Setup of Dedicated Bearers for Specific QCIs  QCI Value  NAS Cause Value for Rejecting GBR Bearer Establishment  GTP-C Cause Value for Rejecting GBR Bearer Establishment  
 
  E-UTRAN   IMSI Prefix       NULL                       3080107000   HUAWEI1.COM  YES                                                     YES                                            YES                                                 NO                                                    0          37                                                      88                                                        
  E-UTRAN   IMSI Prefix       NULL                       3080108000   HUAWEI1.COM  NO                                                      NO                                             NO                                                  YES                                                   2          37                                                      88                                                        
  (Number of results = 2)
 
  ---    END
  ```
2. 输入 “IMSI前缀” ，查询所有 “IMSI前缀” 为 “3080107000” 的QoS策略配置。
  LST QOSPLCYBYAPN: SUBRANGE=IMSI_PREFIX, IMSIPRE="3080107000";
  ```
  %%LST QOSPLCYBYAPN: SUBRANGE=IMSI_PREFIX, IMSIPRE="3080107000";%%
  RETCODE = 0  Operation succeeded
 
  The result is as follows
  ------------------------
                                                  RAT Type  =  E-UTRAN
                                          Subscriber Range  =  IMSI Prefix
                                 Network Operator Identity  =  NULL
                                               IMSI Prefix  =  3080107000
                                                     APNNI  =  HUAWEI1.COM
    QoS of Non-GBR Bearers Is Controlled by Local Policies  =  YES
             QCI-based QoS Is Controlled by Local Policies  =  YES
        QoS of GBR Bearers Is Controlled by Local Policies  =  YES
      Control Setup of Dedicated Bearers for Specific QCIs  =  NO
                                                 QCI Value  =  0
    NAS Cause Value for Rejecting GBR Bearer Establishment  =  37
  GTP-C Cause Value for Rejecting GBR Bearer Establishment  =  88
  (Number of results = 1)
 
  ---    END
  ```

#### [输出结果说明](#ZH-CN_TOPIC_0000001388672790)

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见 [**ADD QOSPLCYBYAPN**](增加基于APN的QoS策略(ADD QOSPLCYBYAPN)_88832402.md) 命令的参数说明。
