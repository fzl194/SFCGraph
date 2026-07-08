---
id: UNC@20.15.2@MMLCommand@DSP RESTOSMCTX
type: MMLCommand
name: DSP RESTOSMCTX（显示容灾用户SM上下文信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: RESTOSMCTX
command_category: 查询类
applicable_nf:
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- MME链式备份管理
- MME容灾管理
- 容灾功能调测
status: active
---

# DSP RESTOSMCTX（显示容灾用户SM上下文信息）

## 功能

**适用网元：MME**

- 本命令用于查询系统内容灾用户的SM上下文信息。
- 输出结果分为SM User上下文、SM PDN上下文、SM PDP上下文等报表。
- 当某一字段显示“NULL”时，表示该字段没有备份。

## 注意事项

- 输出结果中包含用户的某些个人数据，例如IMSI、IMEI、PDP地址等信息。建议您遵从国家的相关法律执行该任务，并采取足够的措施以确保用户的个人数据受到充分的保护。
- 由于无卡用户无签约数据，因此“查询条件”为“IMEI（指定IMEI）”时，按Context ID查询失败显示。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QRYTP | 查询方式 | 可选必选说明：可选参数<br>参数含义：该参数用于指定查询承载上下文的方式。<br>取值范围：<br>- “IMSI（指定IMSI）”<br>- “STMSI（指定S-TMSI）”<br>- “IMEI（指定IMEI）”<br>默认值：IMSI<br>说明：根据IMEI查询仅适用于无卡的紧急呼叫用户。 |
| IMSI | IMSI | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定国际移动用户标识。<br>前提条件：该参数在<br>“查询方式”<br>参数配置为<br>“IMSI（指定IMSI）”<br>时有效。<br>取值范围：1～15位数字<br>默认值：无 |
| STMSI | STMSI | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定用户临时签约标识。<br>前提条件：该参数在<br>“查询方式”<br>参数配置为<br>“STMSI（指定S-TMSI）”<br>时有效。<br>取值范围：1～10位十六进制字符串<br>默认值：无 |
| IMEI | IMEI | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定用户设备的国际移动设备标识。<br>前提条件：该参数在<br>“查询方式”<br>参数配置为<br>“IMEI（指定IMEI）”<br>后生效。<br>取值范围：1～16位数字<br>默认值：无 |
| DISPTYPE | 显示类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定显示类型。<br>取值范围：<br>- “BYBEARID/NSAPI（承载标识/网络层业务接入点标识）”：表示通过指定承载标识/网络层业务接入点标识显示。<br>- “BYCTXID（上下文标识）”：表示通过指定上下文标识显示。<br>默认值：BYBEARID/NSAPI（承载标识/网络层业务接入点标识） |
| BEARIDORNSAPI | 承载ID或网络层业务接入点标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定承载ID或网络层业务接入点标识，用于唯一标识一个承载。<br>前提条件：该参数在<br>“显示类型”<br>设置为<br>“BYBEARID/NSAPI（承载标识/网络层业务接入点标识）”<br>后生效。<br>取值范围：5～15<br>默认值：无<br>说明：- 若参数不输入，输出结果为承载的摘要信息。<br>- 若参数输入，输出结果为承载的详细信息。 |
| CTXID | 上下文标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定签约APN/PDP信息的上下文标识。<br>前提条件：该参数在<br>“显示类型”<br>设置为<br>“BYCTXID（上下文标识）”<br>后生效<br>取值范围：0～4294967294<br>默认值：无<br>说明：- 若参数不输入，输出结果为签约APN/PDP的摘要信息。<br>- 若参数输入，输出结果为签约APN/PDP的详细信息。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/RESTOSMCTX]] · 容灾用户SM上下文信息（RESTOSMCTX）

## 使用实例

1. 当 “IDTYPE” 选择 “BYCTXID（上下文标识）” 而不输入上下文标识时，只输出签约PDP的摘要信息：
  DSP RESTOSMCTX: QRYTP=IMSI, IMSI="123035201000001", DISPTYPE=BYCTXID;
  ```
  %%DSP RESTOSMCTX: QRYTP=IMSI, IMSI="123035201000001", DISPTYPE=BYCTXID;%%
  RETCODE = 0  操作成功

  SM上下文基本信息：
  ------------------
    IMSI  =  123035201000001
  RU名称  =  MCR_SP_RU_0064
  进程号  =  6
    TSUI  =  0000000B80090000
  （结果个数 = 1）

  仍有后续报告输出
  ---    END

  +++    mcr        2017-02-15 13:55:47
  O&M   #HWHandle=174
  %%DSP RESTOSMCTX: QRYTP=IMSI, IMSI="123035201000001", DISPTYPE=BYCTXID;%%
  RETCODE = 0  操作成功

  SM上下文基本信息：
  ------------------
   上下文标识  签约的APN    签约的PDN类型  签约的IPv4地址  签约的IPv6地址                         

   1           HUAWEI1.COM  IPv4v6地址     0.0.0.0         0000:0000:0000:0000:0000:0000:0000:0000
   2           IMS          IPv4v6地址     0.0.0.0         0000:0000:0000:0000:0000:0000:0000:0000
   3           HUAWEI3.COM  IPv4v6地址     0.0.0.0         0000:0000:0000:0000:0000:0000:0000:0000
  （结果个数 = 3）

  共有2个报告
  ---    END
  ```
2. 当 “IDTYPE” 选择 “BYBEARID/NSAPI（承载标识或网络层业务接入点标识）” 而不输入承载ID或网络层业务接入点标识时，只输出激活承载的摘要信息：
  DSP RESTOSMCTX: QRYTP=IMSI, IMSI="123035201000001", DISPTYPE=BYBEARID/NSAPI;
  ```
  %%DSP RESTOSMCTX: QRYTP=IMSI, IMSI="123035201000001", DISPTYPE=BYBEARID/NSAPI;%%
  RETCODE = 0  操作成功

  SM上下文基本信息：
  ------------------
    IMSI  =  123035201000001
  RU名称  =  MCR_SP_RU_0064
  进程号  =  9
    TSUI  =  0000000B80090000
  （结果个数 = 1）

  仍有后续报告输出
  ---    END

  +++    mcr        2017-02-15 13:56:21
  O&M   #HWHandle=175
  %%DSP RESTOSMCTX: QRYTP=IMSI, IMSI="123035201000001", DISPTYPE=BYBEARID/NSAPI;%%
  RETCODE = 0  操作成功

  SM上下文基本信息：
  -----------------------------
                       承载ID  =  5
                   缺省承载ID  =  5
        实际使用的APN网络标识  =  HUAWEI1.COM
       实际使用的运营商APN_OI  =  MNC003.MCC460.GPRS
            实际使用的PDN类型  =  IPv4地址
           实际使用的IPv4地址  =  10.10.10.10
           实际使用的IPv6地址  =  0000:0000:0000:0000:0000:0000:0000:0000
  （结果个数 = 1）

  共有2个报告
  ---    END
  ```
3. 当 “IDTYPE” 选择 “BYCTXID（上下文标识）” 且输入上下文标识时，输出签约PDN的详细信息，包括用户级、PDN级的相关信息：
  DSP RESTOSMCTX: QRYTP=IMSI, IMSI="123035201000001", DISPTYPE=BYCTXID, CTXID=1;
  ```
  %%DSP RESTOSMCTX: QRYTP=IMSI, IMSI="123035201000001", DISPTYPE=BYCTXID, CTXID=1;%%
  RETCODE = 0  操作成功

  SM上下文基本信息：
  ------------------
    IMSI  =  123035201000001
  RU名称  =  MCR_SP_RU_0064
  进程号  =  6
    TSUI  =  0000000B80090000
  （结果个数 = 1）

  仍有后续报告输出
  ---    END

  +++    mcr        2017-02-15 13:57:25
  O&M   #HWHandle=176
  %%DSP RESTOSMCTX: QRYTP=IMSI, IMSI="123035201000001", DISPTYPE=BYCTXID, CTXID=1;%%
  RETCODE = 0  操作成功

  SM签约上下文：
  --------------
                                签约的PDN类型  =  IPv4v6地址
                                    签约的APN  =  HUAWEI1.COM
                            用户签约的EPS QCI  =  5
             用户签约的EPS ARP Priority Level  =  1
     用户签约的EPS ARP Pre-emption Capability  =  不可以抢占其它承载的资源
  用户签约的EPS ARP Pre-emption Vulnerability  =  可以被其它承载抢占资源
                               默认上下文标识  =  1
                            VPLMN地址是否允许  =  允许
                          MIP Home Agent Host  =  NULL
                         MIP Home Agent Realm  =  NULL
                  MIP Home Agent IPv4 Address  =  0.0.0.0
                  MIP Home Agent IPv6 Address  =  0000:0000:0000:0000:0000:0000:0000:0000
                           签约的P-GW分配类型  =  动态
                               签约的计费属性  =  0x0000（None）
                        签约的APN级别的APN OI  =  NULL
                           签约的上行APN-AMBR  =  10000000
                           签约的下行APN-AMBR  =  10000000
                               签约的IPv4地址  =  0.0.0.0
                               签约的IPv6地址  =  0000:0000:0000:0000:0000:0000:0000:0000
  （结果个数 = 1）

  共有2个报告
  ---    END
  ```
4. 当 “IDTYPE” 选择 “BYBEARID/NSAPI” 且输入 “Bearer ID Or NSAPI” 时，输出激活承载的详细信息，包括用户级、PDN级、承载级的相关信息：
  DSP RESTOSMCTX:QRYTP=IMSI, IMSI="123035201000001", DISPTYPE=BYBEARID/NSAPI, BEARIDORNSAPI=5;
  ```
  %%DSP RESTOSMCTX:QRYTP=IMSI, IMSI="123035201000001", DISPTYPE=BYBEARID/NSAPI, BEARIDORNSAPI=5;%%
  RETCODE = 0  操作成功

  SM上下文基本信息：
  ------------------
    IMSI  =  123035201000001
  RU名称  =  MCR_SP_RU_0064
  进程号  =  6
    TSUI  =  0000000580060000
  （结果个数 = 1）

  仍有后续报告输出
  ---    END

  +++    mcr        2017-02-15 13:58:05
  O&M   #HWHandle=177
  %%DSP RESTOSMCTX:QRYTP=IMSI, IMSI="123035201000001", DISPTYPE=BYBEARID/NSAPI, BEARIDORNSAPI=5;%%
  RETCODE = 0  操作成功

  SM User上下文:
  --------------
    S-GW控制面IP地址（S11）  =  10.10.10.10
  S-GW控制面IPv6地址（S11）  =  0000:0000:0000:0000:0000:0000:0000:0000
      S-GW控制面TEID（S11）  =  0x989682
                   S-GW名称  =  TOPON.SGW.SGW1.NODES.EPC.ENVID52.MNC03.MCC460.3GPPNETWORK.ORG
  （结果个数 = 1）

  仍有后续报告输出
  ---    END

  +++    mcr        2017-02-15 13:58:05
  O&M   #HWHandle=177
  %%DSP RESTOSMCTX:QRYTP=IMSI, IMSI="123035201000001", DISPTYPE=BYBEARID/NSAPI, BEARIDORNSAPI=5;%%
  RETCODE = 0  操作成功

  SM PDN上下文:
  -------------
        实际使用的APN网络标识  =  HUAWEI1.COM
       实际使用的运营商APN_OI  =  MNC003.MCC460.GPRS
        APN Restriction Value  =  NULL
                  APN选择模式  =  签约的
           实际使用的IPv4地址  =  10.10.10.10
           实际使用的IPv6地址  =  0000:0000:0000:0000:0000:0000:0000:0000
                   缺省承载ID  =  5
    P-GW控制面IP地址（S5/S8）  =  10.10.10.10
  P-GW控制面IPv6地址（S5/S8）  =  0000:0000:0000:0000:0000:0000:0000:0000
      P-GW控制面TEID（S5/S8）  =  0x989683
                     P-GW名称  =  TOPON.PGW.GW1.NODES.EPC.MNC03.MCC460.3GPPNETWORK.ORG
       实际使用的上行APN-AMBR  =  10000000
       实际使用的下行APN-AMBR  =  10000000
                     计费属性  =  0x0000（None）
                 位置上报类型  =  NULL
                      PRA动作  =  启动PRA订阅
                      PRA标识  =  0x800000
  （结果个数 = 1）

  仍有后续报告输出
  ---    END

  +++    mcr        2017-02-15 13:58:05
  O&M   #HWHandle=177
  %%DSP RESTOSMCTX:QRYTP=IMSI, IMSI="123035201000001", DISPTYPE=BYBEARID/NSAPI, BEARIDORNSAPI=5;%%
  RETCODE = 0  操作成功

  SM承载上下文:
  -------------
                                           承载ID  =  5
                         S-GW用户面IP地址（S1-U）  =  10.10.10.10
                       S-GW用户面IPv6地址（S1-U）  =  0000:0000:0000:0000:0000:0000:0000:0000
                           S-GW用户面TEID（S1-U）  =  0x989684
                        P-GW用户面IP地址（S5/S8）  =  10.10.10.10
                      P-GW用户面IPv6地址（S5/S8）  =  0000:0000:0000:0000:0000:0000:0000:0000
                          P-GW用户面TEID（S5/S8）  =  0x989685
             用户实际使用的EPS ARP Priority Level  =  1
  用户实际使用的EPS ARP Pre-emption Vulnerability  =  可以被其它承载抢占资源
     用户实际使用的EPS ARP Pre-emption Capability  =  不可以抢占其它承载的资源
                            用户实际使用的EPS QCI  =  5
                         实际使用的上行最大比特率  =  0
                         实际使用的下行最大比特率  =  0
                         实际使用的上行保证比特率  =  0
                         实际使用的下行保证比特率  =  0
                                       激活发起方  =  MS发起的激活
                                               Ti  =  0
                        Packet Flow Context的标识  =  8
                                   业务接入点标识  =  3
                                       无线优先级  =  2
  （结果个数 = 1）

  共有4个报告
  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示容灾用户SM上下文信息（DSP-RESTOSMCTX）_26307108.md`
