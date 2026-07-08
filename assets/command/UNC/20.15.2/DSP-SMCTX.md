---
id: UNC@20.15.2@MMLCommand@DSP SMCTX
type: MMLCommand
name: DSP SMCTX（显示承载上下文）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: SMCTX
command_category: 查询类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 系统管理
- 用户数据库管理
status: active
---

# DSP SMCTX（显示承载上下文）

## 功能

**适用网元：SGSN、MME**

该命令用于查看指定用户的承载上下文信息。

## 注意事项

- 该命令执行后立即生效。
- 此功能用于快速定位问题和解决故障，在使用过程中不可避免的使用到用户的某些个人数据，如IMSI、IP地址。建议您遵从国家的相关法律执行该任务，并采取足够的措施以确保用户的个人数据受到充分的保护。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QUERYOPT | 查询方式 | 可选必选说明：可选参数<br>参数含义：该参数用于指定查询承载上下文的方式。<br>取值范围：<br>- “BYIMSI(指定IMSI)”：表示通过IMSI来查询承载上下文。<br>- “BYMSISDN(指定MSISDN)”：表示通过MSISDN来查询承载上下文。<br>- “BYPTMSI(指定PTMSI)”：表示通过P-TMSI来查询承载上下文。<br>- “BYIMEI(指定IMEI)”:表示在无卡用户发起紧急呼叫业务场景下，通过IMEI来查询承载上下文。- 在紧急呼叫场景下，通过IMEI查询无卡用户的承载上下文，IMSI显示NULL。<br>- 非紧急呼叫场景下，通过IMEI查询用户承载上下文，或者紧急呼叫场景下，通过IMEI查询有卡用户的承载上下文，命令执行失败。<br>默认值：<br>“BYIMSI(指定IMSI)”<br>说明：针对开启一号多卡功能的用户，此命令不支持根据MSISDN直接查询用户移动上下文。如需根据MSISDN查询，可通过<br>[**DSP IMSI**](显示指定MSISDN用户IMSI(DSP IMSI)_72345951.md)<br>查询MSISDN对应的IMSI，再通过此命令根据IMSI查询对应的用户移动性管理上下文。 |
| IMSI | IMSI | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定国际移动用户标识。<br>前提条件：该参数在<br>“查询方式”<br>设置为<br>“BYIMSI(指定IMSI)”<br>时有效。<br>取值范围：1~15位数字<br>默认值：无 |
| MSISDN | MSISDN | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定移动台国际ISDN号码。<br>前提条件：该参数在<br>“查询方式”<br>设置为<br>“BYMSISDN(指定MSISDN)”<br>时有效。<br>取值范围：1~15位数字<br>默认值：无 |
| PTMSI | PTMSI | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定分组临时移动用户标识。<br>前提条件：该参数在<br>“查询方式”<br>设置为<br>“BYPTMSI(指定PTMSI)”<br>时有效。<br>取值范围：1~10位16进制码字符串<br>默认值：无 |
| IMEI | IMEI | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定国际移动设备标识。<br>前提条件：该参数在<br>“查询方式”<br>设置为<br>“BYIMEI(指定IMEI)”<br>时有效。<br>取值范围：1~16位数字<br>默认值：无 |
| IDTYPE | 显示类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定ID类型，可以选择通过承载ID或网络层业务接入点标识，或者上下文标示查询承载上下文。<br>数据来源：本端规划<br>取值范围：<br>- “BYBEARID/NSAPI（承载标识/网络层业务接入点标识）”：表示指定查询的ID类型为承载标识/网络层业务接入点标识。<br>- “BYCTXID（上下文标识）”：表示指定查询的ID类型为上下文标识。<br>默认值：<br>“BYBEARID/NSAPI（承载标识/网络层业务接入点标识）” |
| BEARIDORNSAPI | 承载ID或网络层业务接入点标识 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定承载ID或网络层业务接入点标识，用来唯一标识一个承载。<br>前提条件：该参数在<br>“显示类型”<br>设置为<br>“BYBEARID/NSAPI（承载标识/网络层业务接入点标识）”<br>时生效。<br>取值范围：5~15<br>默认值：无 |
| CTXID | 上下文标识 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定签约PDP信息的上下文标识。<br>前提条件：该参数在<br>“显示类型”<br>设置为<br>“BYCTXID（上下文标识）”<br>时生效。<br>取值范围：0～4294967294<br>默认值：无<br>说明：由于无卡用户无签约数据，因此查询条件为<br>“BYIMEI(指定IMEI)”<br>时，按Context ID查询失败。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SMCTX]] · 承载上下文（SMCTX）

## 使用实例

1. 当IDTYPE选择BYCTXID（上下文标识）而不输入上下文标识时，只输出签约PDP的摘要信息：
  DSP SMCTX: QUERYOPT=BYIMSI, IMSI="123031100000007", IDTYPE=BYCTXID;
  ```
  %%DSP SMCTX: QUERYOPT=BYIMSI, IMSI="123031100000007", IDTYPE=BYCTXID;%%
  RETCODE = 0  操作成功。

  结果如下
  -------------------------
                上下文标识  =  6
                 签约的APN  =  HUAWEI11
             签约的PDN类型  =  IPv4
        签约的静态IPv4地址  =  10.141.149.100
        签约的静态IPv6地址  =  2001:db8:10:19:44:55:10:12 
  (结果个数 = 1)

  ---    END
  ```
2. 当IDTYPE选择BYBEARID/NSAPI（承载标识或网络层业务接入点标识）而不输入承载ID或网络层业务接入点标识时，只输出激活承载的摘要信息：
  DSP SMCTX:QUERYOPT=BYMSISDN, MSISDN="861390000001126", IDTYPE=BYBEARID/NSAPI;
  ```
  %%DSP SMCTX:QUERYOPT=BYMSISDN, MSISDN="861390000001126", IDTYPE=BYBEARID/NSAPI;%%
  RETCODE = 0  操作成功。

  结果如下
  -------------------------
                     接入类型  =  Iu
                        NSAPI  =  5
                   激活发起方  =  Activation initiated by MS
                           Ti  =  0
        实际使用的APN网络标识  =  AM.COM
       实际使用的运营商APN_OI  =  MNC010.MCC123.GPRS
            实际使用的PDN类型  =  IPv4
           实际使用的IPv4地址  =  10.141.149.100
           实际使用的IPv6地址  =  2001:db8:10:19:44:55:10:13
         关联的签约上下文标识  =  1
  (结果个数 = 1)

  ---    END
  ```
3. 当IDTYPE选择BYCTXID（上下文标识）且输入上下文标识时，输出签约PDN的详细信息，包括用户级、PDN级的相关信息：
  DSP SMCTX:QUERYOPT=BYMSISDN, MSISDN="861390000001126", IDTYPE=BYCTXID, CTXID=1;
  ```
  %%DSP SMCTX:QUERYOPT=BYMSISDN, MSISDN="861390000001126", IDTYPE=BYCTXID, CTXID=1;%%
  RETCODE = 0  操作成功。

  结果如下
  -------------------------
                                  IMSI  =  123100000001126
                                MSISDN  =  861390000001126
                          签约数据类型  =  GPRS
                            上下文标识  =  1
                             签约的APN  =  AM.COM
                         签约的PDN类型  =  IPv4
                    签约的静态IPv4地址  =  10.141.149.100
                    签约的静态IPv6地址  =  2001:db8:10:19:44:55:10:35
                     允许使用VPLMN地址  =  Yes
                        签约的计费属性  =  0x0800(Normal Billing)
                         签约的QoS版本  =  QOSR99
                        签约的延迟等级  =  Delay class 1
                          签约的可靠性  =  Ack GTP/LLC/RLC Protected
             签约的最大吞吐量(octet/s)  =  1000
                          签约的优先级  =  High priority
             签约的平均吞吐量(octet/h)  =  100
                  签约的分配保留优先级  =  NormalLevelUser
                        签约的流量等级  =  Background class
                        签约的发送次序  =  Without delivery order
                     签约的发送错误SDU  =  No detect
                     签约的最大SDU长度  =  1500octets
                         签约的保留BER  =  5*10^-2
                       签约的SDU误码率  =  1*10^-2
                        签约的传递时延  =  30ms
                        发送控制优先级  =  Priority level 1
                    签约的上行最大速率  =  8640kbit/s
                    签约的上行保证速率  =  2816kbit/s
                    签约的下行最大速率  =  8640kbit/s
                    签约的下行保证速率  =  2944kbit/s
  	        缺省Non-IP上下文标识  =  NULL
  (结果个数 = 1)

  ---    END
  ```
4. 当IDTYPE选择BYBEARID/NSAPI且输入Bearer ID Or NSAPI时，输出激活承载的详细信息，包括用户级、PDN级、承载级的相关信息：
  DSP SMCTX:QUERYOPT=BYMSISDN, MSISDN="8613958000007", IDTYPE=BYBEARID/NSAPI, BEARIDORNSAPI=5;
  ```
  %%DSP SMCTX:QUERYOPT=BYMSISDN, MSISDN="8613958000007", IDTYPE=BYBEARID/NSAPI, BEARIDORNSAPI=5;%%
  RETCODE = 0  操作成功。

  结果如下
  -------------------------
                                                        IMSI  =  123032801000001
                                                      MSISDN  =  8613528000001
                                                      承载ID  =  5
                                                  缺省承载ID  =  5
                                                  激活发起方  =  MS发起的激活
                                                          Ti  =  0
                               Maximum APN Restriction Value  =  0
                                       APN Restriction Value  =  NULL
                                       实际使用的APN网络标识  =  HUAWEI1.COM
                                      实际使用的运营商APN_OI  =  MNC003.MCC123.GPRS
                                                 APN选择模式  =  签约的
                                           实际使用的PDN类型  =  IPv4
                                          实际使用的IPv4地址  =  10.141.149.108
                                          实际使用的IPv6地址  =  2001:db8:10:19:44:55:10:15
                                        关联的签约上下文标识  =  1
                                          控制面上游接口类型  =  S11
                                       S-GW控制面IP地址(S11)  =  172.27.28.49
                                     S-GW控制面IPv6地址(S11)  =  2001:db8:10:19:44:55:10:12
                                         S-GW控制面TEID(S11)  =  0x989682
                                       本端控制面IP地址(S11)  =  172.21.28.3
                                         本端控制面TEID(S11)  =  0x8281203C
                                             协议类型(S5/S8)  =  GTP
                                   P-GW控制面IP地址（S5/S8）  =  10.141.149.100
                                 P-GW控制面IPv6地址（S5/S8）  =  2001:db8:10:19:44:55:10:16
                                     P-GW控制面TEID（S5/S8）  =  0x989683
                                                    接入类型  =  NB-S1
                                              用户面接口类型  =  S11_U
                                      MME用户面IP地址(S11-U)  =  172.21.28.7
                                    MME用户面IPv6地址(S11-U)  =  2001:db8:10:19:44:55:10:41
                                        MME用户面TEID(S11-U)  =  0x54011000
                                     S-GW用户面IP地址(S11-U)  =  172.27.28.49
                                   S-GW用户面IPv6地址(S11-U)  =  2001:db8:10:19:44:55:10:43
                                       S-GW用户面TEID(S11-U)  =  0x989684
                                     P-GW用户面IP地址(S5/S8)  =  172.27.28.49
                                   P-GW用户面IPv6地址(S5/S8)  =  2001:db8:10:19:44:55:10:52
                                       P-GW用户面TEID(S5/S8)  =  0x989685
                                                    计费标识  =  0x2
                                       实际使用的上行UE-AMBR  =  10000000
                                       实际使用的下行UE-AMBR  =  10000000
                                       实际使用的上行APN-MBR  =  10000000
                                       实际使用的下行APN-MBR  =  10000000
                        用户实际使用的EPS ARP Priority Level  =  1
             用户实际使用的EPS ARP Pre-emption Vulnerability  =  可以被其它承载抢占资源
                用户实际使用的EPS ARP Pre-emption Capability  =  可以抢占其它承载的资源
                                       用户实际使用的EPS QCI  =  5
                                    实际使用的上行最大比特率  =  0
                                    实际使用的下行最大比特率  =  0
                                    实际使用的上行保证比特率  =  0
                                    实际使用的下行保证比特率  =  0
                                              业务接入点标识  =  3
                                   Packet Flow Context的标识  =  NULL
                                                位置上报类型  =  NULL
                                               P-GW 重选标识  =  NO
                                             S-GW主机名(S11)  =  TOPON.SGW.SGW2.NODES.EPC.ENVID28.MNC03.MCC123.3GPPNETWORK.ORG
                                           P-GW主机名(S5/S8)  =  TOPON.PGW.GW1.NODES.EPC.MNC03.MCC123.3GPPNETWORK.ORG
                                                     PRA动作  =  NULL
                                                     PRA标识  =  NULL
                                                     PRA状态  =  NULL
                                              CP上行数传速率  =  0
                                              CP下行数传速率  =  0
  基于服务PLMN速率控制正常传输的上行ESM Data Transport报文数  =  0
  基于服务PLMN速率控制正常传输的下行ESM Data Transport报文数  =  0
        因服务PLMN速率控制丢弃的上行ESM Data Transport报文数  =  0
        因服务PLMN速率控制丢弃的下行ESM Data Transport报文数  =  0
                                                数据传输类型  =  NULL
                                             NAS信令低优先级  =  否
                                              S1连接释放时间  =  NULL
                                                 PDN重建标识  =  否
                                              接入S-GW的时间  =  2017-04-27 19:57:11
                                              接入P-GW的时间  =  2017-04-27 19:57:11
                                          是否选择到高速网关  =  否
											
  (结果个数 = 1)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-SMCTX.md`
