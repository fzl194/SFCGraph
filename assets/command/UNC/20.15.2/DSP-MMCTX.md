---
id: UNC@20.15.2@MMLCommand@DSP MMCTX
type: MMLCommand
name: DSP MMCTX（显示MM上下文）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: MMCTX
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

# DSP MMCTX（显示MM上下文）

## 功能

**适用网元：SGSN、MME**

该命令用于查看移动性管理(MM)上下文的相关信息，包括用户信息、用户状态、当前跟踪区、安全信息等。

## 注意事项

- 该命令执行后立即生效。
- 此功能用于快速定位问题和解决故障，在使用过程中不可避免的使用到用户的某些个人数据，如IMSI、IP地址。建议您遵从国家的相关法律执行该任务，并采取足够的措施以确保用户的个人数据受到充分的保护。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QUERYOPT | 查询方式 | 可选必选说明：可选参数<br>参数说明：该参数用于指定查询MM上下文的查询方式。<br>取值范围：<br>- “BYIMSI(指定IMSI)”：表示根据IMSI查询用户的MM上下文。<br>- “BYMSISDN(指定MSISDN)”：表示根据MSISDN查询用户的MM上下文。<br>- “BYGUTI(指定GUTI)”：表示根据GUTI查询用户的MM上下文。<br>- “BYPTMSI(指定PTMSI)”：表示根据P-TMSI查询用户的MM上下文。<br>- “BYIMEI(指定IMEI)”：表示根据IMEI查询用户的MM上下文。<br>默认值：<br>“BYIMSI(指定IMSI)”<br>说明：- 针对开启一号多卡功能的用户，此命令不支持根据MSISDN直接查询用户移动上下文。如需根据MSISDN查询，可通过[**DSP IMSI**](显示指定MSISDN用户IMSI(DSP IMSI)_72345951.md)查询MSISDN对应的IMSI，再通过此命令根据IMSI查询对应的用户移动性管理上下文。<br>- 根据IMEI查询仅适用于无USIM卡的紧急呼叫用户。 |
| IMSI | IMSI | 可选必选说明：条件必选参数<br>参数说明：该参数用于指定国际移动用户标识。<br>前提条件：此参数在<br>“查询方式”<br>设置为<br>“BYIMSI(指定IMSI)”<br>后生效。<br>取值范围：1～15位数字<br>默认值：无 |
| MSISDN | MSISDN | 可选必选说明：条件必选参数<br>参数说明：该参数用于指定移动台国际ISDN号码。<br>前提条件：此参数在<br>“查询方式”<br>设置为<br>“BYMSISDN(指定MSISDN)”<br>后生效。<br>取值范围：1～15位数字<br>默认值：无 |
| GUTI | GUTI | 可选必选说明：条件必选参数<br>参数说明：该参数用于指定GUTI号。<br>前提条件：此参数在<br>“查询方式”<br>设置为<br>“BYGUTI(指定GUTI)”<br>后生效。<br>取值范围：19～20位16进制码字符串<br>默认值：无 |
| PTMSI | PTMSI | 可选必选说明：条件必选参数<br>参数说明：该参数用于指定P-TMSI号。<br>前提条件：此参数在<br>“查询方式”<br>设置为<br>“BYPTMSI(指定PTMSI)”<br>后生效。<br>取值范围：1～10位16进制码字符串<br>默认值：无 |
| IMEI | ME标识 | 可选必选说明：条件必选参数<br>参数说明：该参数用于指定用户设备的国际移动设备标识。<br>前提条件：此参数在<br>“查询方式”<br>设置为<br>“BYIMEI(指定IMEI)”<br>后生效。<br>取值范围：1～15位数字<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/MMCTX]] · MM上下文（MMCTX）

## 使用实例

1. 2G:
  DSP MMCTX: QUERYOPT=BYIMSI, IMSI="123031600000002";
  ```
  %%DSP MMCTX: QUERYOPT=BYIMSI, IMSI="123031600000002";%%
  RETCODE = 0  操作成功。
  MM静态上下文信息：
  ------------------
                                  RU名称  =  USN_SP_RU_0065
  				进程号  =  3
                                    IMSI  =  123031600000002
                                  MSISDN  =  8613916000002
                                  ME标识  =  NULL
                                    GUTI  =  NULL
                                   PTMSI  =  0xC0C326CB
                        PTMSI 所在路由区  =  12303160101
                               PTMSI签名  =  0x7a5740
                                  时间戳  =  NULL
                            网络接入模式  =  混合用户
       禁止漫游用户通过VPLMN的接入点接入  =  否
       禁止漫游用户通过HPLMN的接入点接入  =  否
                  禁止用户所有分组域业务  =  否
                        禁止用户所有呼出  =  否
                            ODBHPLMNData  =  0x0
                              区域码数目  =  0
                              区域码列表  =  NULL
          是否因为未支持特性禁止漫游标识  =  否
                       是否禁止UTRAN接入  =  否
                       是否禁止GERAN接入  =  否
                                  STN-SR  =  NULL
                                计费属性  =  0x0000(None)
           签约的无线管理策略（RFSP ID）  =  NULL
  	是否因为未支持特性禁止漫游标识  =  否
            ODB General数据被HLR/HSS证实  =  否
              HPLMNData是否被HLR/HSS证实  =  否
   GPRS用户签约数据是否被HLR/HSS证实标志  =  是
           SGSN位置信息是否被HLR/HSS证实  =  是
    EPS用户签约数据是否被HLR/HSS证实标志  =  否
            MME位置信息是否被HLR/HSS证实  =  否
                        移动用户是否可达  =  是
                         GSM鉴权向量个数  =  0
                     剩余EPS鉴权向量个数  =  0
                EPS鉴权向量服务网络标识   =  NULL
                  保存的UMTS鉴权向量个数  =  0
          保存的UMTS鉴权向量对应SGSN标识  =  NULL
                            移动管理状态  =  READY
                              运营商标识  =  0
                              运营商类型  =  0
                            永久在线标志  =  否
                UE上次接入时间(SGSN side) = 2016-09-23 16:27:13
                      用户当前所在路由区  =  12303160101
                            用户所在小区  =  0x1011
                           GERAN加密算法  =  No encryption
                          加密密钥序列号  =  7
              可选鉴权事件发生次数(GERAN) =  0
                  HLR是否支持SuperCharge  =  否
                                 HLR编号  =  8613916101
                                SGSN号码  =  861390211601
  			    Qchat 用户  =  否
                            寻呼是否继续  =  是
                              UE挂起状态  =  否
                              UE DRX参数  =  0001
                              UE网络能力  =  NULL
                              MS网络能力  =  E540112233445566
                                使用RFSP  =  NULL
              Mobile Station Classmark 2  =  NULL
              Mobile Station Classmark 3  =  NULL
                    Supported codec list  =  NULL
                                 ISR状态  =  未激活
                                 ARD参数  =  0000
                              UE无线能力  =  14F382334C03263CA060
                               VLR可靠性  =  不可靠
                                 VLR编号  =  NULL
                          非GPRS提醒标志  =  否
                              Gs关联状态  =  不关联
                                终端类型  =  未知类型
                    智能终端激活抑制类型  =  NULL
                            智能手机状态  =  否
  	   签约的周期RAU/TAU定时器(秒)  =  0
         UE请求的长周期RAU/TAU定时器(秒)  =  0
         使用的长周期RAU/TAU定时器(分钟)  =  0
                          UE无线寻呼能力  =  NULL
                          推荐的小区数目  =  0
                          推荐的小区列表  =  NULL
                          上次驻留的ECGI  =  NULL
                      上次驻留的覆盖等级  =  NULL
                      用户HSS Bypass状态  =  FALSE
                      用户HLR Bypass状态  =  FALSE
                             PSCell 信息  =  NULL
  (结果个数 = 1)

  ---    END
  ```
2. 3G:
  DSP MMCTX: QUERYOPT=BYIMSI, IMSI="123031600000002";
  ```
  %%DSP MMCTX: QUERYOPT=BYIMSI, IMSI="123031600000002";%%
  RETCODE = 0  操作成功。

  MM静态上下文信息：
  ----------------
                                  RU名称  =  USN_SP_RU_0064
  				进程号  =  4
                                    IMSI  =  123031600000002
                                  MSISDN  =  8613916000002
                                  ME标识  =  NULL
                                    GUTI  =  NULL
                                   PTMSI  =  0xC056AD53
                        PTMSI 所在路由区  =  12303160101
                               PTMSI签名  =  0x6ece2a
                                  时间戳  =  NULL
                            网络接入模式  =  混合用户
       禁止漫游用户通过VPLMN的接入点接入  =  否
       禁止漫游用户通过HPLMN的接入点接入  =  否
                  禁止用户所有分组域业务  =  否
                        禁止用户所有呼出  =  否
                            ODBHPLMNData  =  0x0
                              区域码数目  =  0
                              区域码列表  =  NULL
          是否因为未支持特性禁止漫游标识  =  否
                       是否禁止UTRAN接入  =  否
                       是否禁止GERAN接入  =  否
                                  STN-SR  =  NULL
                                计费属性  =  0x0000(None)
           签约的无线管理策略（RFSP ID）  =  NULL
            ODB General数据被HLR/HSS证实  =  否
  	是否因为未支持特性禁止漫游标识  =  否
              HPLMNData是否被HLR/HSS证实  =  否
   GPRS用户签约数据是否被HLR/HSS证实标志  =  是
           SGSN位置信息是否被HLR/HSS证实  =  是
    EPS用户签约数据是否被HLR/HSS证实标志  =  否
            MME位置信息是否被HLR/HSS证实  =  否
                        移动用户是否可达  =  是
                         GSM鉴权向量个数  =  0
                     剩余EPS鉴权向量个数  =  0
                 EPS鉴权向量服务网络标识  =  NULL
                  保存的UMTS鉴权向量个数  =  1
          保存的UMTS鉴权向量对应SGSN标识  =  NULL
                            移动管理状态  =  PMM-IDLE
                              运营商标识  =  0
                              运营商类型  =  0
                            永久在线标志  =  否
               UE上次接入时间(SGSN side)  =  2016-09-23 18:26:41
                      用户当前所在路由区  =  12303160101
                          用户所属服务区  =  1230316010101
                                 RNC标识  =  1161
                           UMTS 加密算法  =  标准UEA1
                         UMTS 完整性算法  =  标准UIA-1
                          加密密钥序列号  =  1
              可选鉴权事件发生次数(UMTS)  =  0
                  HLR是否支持SuperCharge  =  否
                                 HLR编号  =  8613916101
                                SGSN号码  =  861390211601
                              Qchat 用户  =  否
                            寻呼是否继续  =  是
                             UE 挂起状态  =  是
                              UE DRX参数  =  0001
                              UE网络能力  =  NULL
                              MS网络能力  =  E540
                                使用RFSP  =  NULL
              Mobile Station Classmark 2  =  NULL
              Mobile Station Classmark 3  =  NULL
                    Supported codec list  =  NULL
                                 ISR状态  =  未激活
                                 ARD参数  =  0000
                              UE无线能力  =  14F382334C03263CA060
                               VLR可靠性  =  不可靠
                                 VLR编号  =  NULL
                          非GPRS提醒标志  =  否
                              Gs关联状态  =  不关联
                                终端类型  =  未知类型
                    智能终端激活抑制类型  =  NULL
                            智能手机状态  =  否
                              选择的PLMN  =  12303
             签约的周期RAU/TAU定时器(秒)  =  0
         UE请求的长周期RAU/TAU定时器(秒)  =  0
         使用的长周期RAU/TAU定时器(分钟)  =  0
                          UE无线寻呼能力  =  NULL
                          推荐的小区数目  =  0
                          推荐的小区列表  =  NULL
                        推荐的eNodeB数目  =  0
                        推荐的eNodeB列表  =  NULL
                          上次驻留的ECGI  =  NULL
                      上次驻留的覆盖等级  =  NULL
                      用户HSS Bypass状态  =  FALSE
                      用户HLR Bypass状态  =  FALSE
                             PSCell 信息  =  NULL
  (结果个数 = 1)

  ---    END
  ```
3. 4G:
  DSP MMCTX: QUERYOPT=BYIMSI, IMSI="123031601000001";

  ```
  %%DSP MMCTX: QUERYOPT=BYIMSI, IMSI="123031601000001";%%
  RETCODE = 0  操作成功。

  MM静态上下文信息：
  ------------------
  				进程号  =  1
                                    IMSI  =  123031601000001
                                  MSISDN  =  8613516000001
                                    GUTI  =  12303800116c3666c8c
                                  ME标识  =  NULL
                                   PTMSI  =  NULL
                        PTMSI 所在路由区  =  NULL
                               PTMSI签名  =  NULL
                                  时间戳  =  NULL
                            网络接入模式  =  混合用户
       禁止漫游用户通过VPLMN的接入点接入  =  否
       禁止漫游用户通过HPLMN的接入点接入  =  否
                  禁止用户所有分组域业务  =  否
                        禁止用户所有呼出  =  否
                            ODBHPLMNData  =  0x0
                              区域码数目  =  0
                              区域码列表  =  NULL
                      根据区域码漫游禁止  =  否
                       是否禁止UTRAN接入  =  否
                       是否禁止GERAN接入  =  否
                                  STN-SR  =  NULL
                                计费属性  =  0xffff
                 无线管理策略（RFSP ID）  =  NULL
              是否因为未支持特性禁止漫游  =  否
            ODB General数据被HLR/HSS证实  =  否
              HPLMNData是否被HLR/HSS证实  =  否
   GPRS用户签约数据是否被HLR/HSS证实标志  =  否
           SGSN位置信息是否被HLR/HSS证实  =  否
    EPS用户签约数据是否被HLR/HSS证实标志  =  是
            MME位置信息是否被HLR/HSS证实  =  是
                        移动用户是否可达  =  是
                         GSM鉴权向量个数  =  0
                     剩余EPS鉴权向量个数  =  0
                 EPS鉴权向量服务网络标识  =  NULL
                  保存的UMTS鉴权向量个数  =  0
          保存的UMTS鉴权向量对应SGSN标识  =  NULL
                            移动管理状态  =  ECM-CONNECTED
                              运营商标识  =  0
                              运营商类型  =  0
                            永久在线标志  =  否
                UE上次接入时间(MME side)  =  2016-09-23 11:36:02
  	            用户当前所在位置区  =  NULL
                              跟踪区列表  =  123031601; 123031602
                     E-UTRAN小区全局标识  =  123031601101
                          全球eNodeB标识  =  1230316011
                        E-UTRAN 加密算法  =  NULL
                      E-UTRAN 完整性算法  =  NULL
                                 当前KSI  =  NULL
                           上行NAS count  =  0
                           下行NAS count  =  0
           可选鉴权事件发生次数(E-UTRAN)  =  0
                                     NCC  =  0
                      最近一次TAU时的TAI  =  123031601
                     计算AS密钥使用的KSI  =  NULL
                               非当前KSI  =  NULL
                               HSS主机名  =  hss1601.huawei03.com
                                 HSS域名  =  huawei03.com
                          UE可达请求参数  =  否
                           MPS优先级签约  =  0x0（未签约）
                            寻呼是否继续  =  是
                              UE挂起状态  =  否
  			     UEDRX参数  =  NULL
                              UE网络能力  =   FF7FFFFF0E0000 (EEA0; EEA1; EEA2; EEA3; EEA4; EEA5; EEA6; EEA7; EIA1; EIA2; EIA3; EIA4; EIA5; EIA6; EIA7; UEA0; UEA1; UEA2; UEA3; UEA4; UEA5; UEA6; UEA7; UCS2; UIA1; UIA2; UIA3; UIA4; UIA5; UIA6; UIA7; LPP; LCS; 1xSRVCC)
                              MS网络能力  =  000000E541
                                使用RFSP  =  NULL
              Mobile Station Classmark 2  =  NULL
              Mobile Station Classmark 3  =  NULL
                    Supported codec list  =  NULL
                                 ISR状态  =  未激活
                                 ARD参数  =  2000 (Hotonon3gppaccessForbid)
                              UE无线能力  =  NULL
                               VLR可靠性  =  不可靠
                                 VLR编号  =  1230301
                           非EPS提醒标志  =  否
                             SGs关联状态  =  关联未建立
  			 仅支持SMS功能  =  否
                          IMSI未鉴权指示  =  否
                         MME紧急服务状态  =  非紧急呼叫用户
                          用户是否被抑制  =  否
           签约的周期RAU/TAU定时器（秒）  =  0
         UE请求的长周期RAU/TAU定时器(秒)  =  0
         使用的长周期RAU/TAU定时器(分钟)  =  0
             使用的Active timer定时器(秒) =  NULL
  	                UE无线寻呼能力  =  NULL
  		        推荐的小区数目  =  0
  		        推荐的小区列表  =  NULL
  		      推荐的eNodeB数目  =  0
  		      推荐的eNodeB列表  =  NULL
  		        上次驻留的ECGI  =  NULL
  		    上次驻留的覆盖等级  =  NULL
                    UE请求的寻呼周期(秒)  =  NULL
            UE请求的寻呼时间窗口时长(秒)  =  NULL
                      使用的寻呼周期(秒)  =  NULL
              使用的寻呼时间窗口时长(秒)  =  NULL
                       是否支持CE Mode B  =  否
                     签约的UE USAGE TYPE  =  NULL
                     使用的UE USAGE TYPE  =  NULL
                            是否支持DCNR  =  否
                           UE附加安全能力 =  NULL
               签约的P-GW紧急IP地址(IPv4) =  255.255.255.255
               签约的P-GW紧急IP地址(IPv6) =  FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF
                       签约的P-GW紧急FQDN =  NULL
                      用户HSS Bypass状态  =  TRUE
                  进入HSS Bypass状态时间  =  2022-06-16 11:50:02
                      用户HLR Bypass状态  =  FALSE
                             PSCell 信息  =  NULL
     PCRF上签约的无线管理策略（RFSP ID）  =  NULL
  (结果个数 = 1)

  ---    END
  ```
4. NB-IoT用户:
  DSP MMCTX: QUERYOPT=BYIMSI, IMSI="123031601000001";
  ```
  %%DSP MMCTX: QUERYOPT=BYIMSI, IMSI="123031601000001";%%
  RETCODE = 0  操作成功。

  MM静态上下文信息：
  ------------------
                                  RU名称  =  USN_SP_RU_0064
  				进程号  =  1
                                    IMSI  =  123031601000001
                                  MSISDN  =  8613516000001
                                  ME标识  =  NULL
                                    GUTI  =  12303800116c3666c8c
                                   PTMSI  =  NULL
                        PTMSI 所在路由区  =  NULL
                               PTMSI签名  =  NULL
                                  时间戳  =  NULL
                            网络接入模式  =  混合用户
       禁止漫游用户通过VPLMN的接入点接入  =  否
       禁止漫游用户通过HPLMN的接入点接入  =  否
                  禁止用户所有分组域业务  =  否
                        禁止用户所有呼出  =  否
                            ODBHPLMNData  =  0x0
                              区域码数目  =  0
                              区域码列表  =  NULL
                      根据区域码漫游禁止  =  否
                       是否禁止UTRAN接入  =  否
                       是否禁止GERAN接入  =  否
                                  STN-SR  =  NULL
                                计费属性  =  0xffff
                 无线管理策略（RFSP ID）  =  NULL
              是否因为未支持特性禁止漫游  =  否
            ODB General数据被HLR/HSS证实  =  否
              HPLMNData是否被HLR/HSS证实  =  否
   GPRS用户签约数据是否被HLR/HSS证实标志  =  否
           SGSN位置信息是否被HLR/HSS证实  =  否
    EPS用户签约数据是否被HLR/HSS证实标志  =  是
            MME位置信息是否被HLR/HSS证实  =  是
                        移动用户是否可达  =  是
                         GSM鉴权向量个数  =  0
                     剩余EPS鉴权向量个数  =  0
                 EPS鉴权向量服务网络标识  =  NULL
                  保存的UMTS鉴权向量个数  =  0
          保存的UMTS鉴权向量对应SGSN标识  =  NULL
                            移动管理状态  =  ECM-CONNECTED
                              运营商标识  =  0
                              运营商类型  =  0
                            永久在线标志  =  否
                UE上次接入时间(MME side)  =  2016-09-23 11:36:02
  	            用户当前所在位置区  =  NULL
                              跟踪区列表  =  123031601; 123031602
                     E-UTRAN小区全局标识  =  123031601101
                          全球eNodeB标识  =  1230316011
                        E-UTRAN 加密算法  =  NULL
                      E-UTRAN 完整性算法  =  NULL
                                 当前KSI  =  NULL
                           上行NAS count  =  0
                           下行NAS count  =  0
           可选鉴权事件发生次数(E-UTRAN)  =  0
                                     NCC  =  0
                      最近一次TAU时的TAI  =  123031601
                     计算AS密钥使用的KSI  =  NULL
                               非当前KSI  =  NULL
                               HSS主机名  =  hss1601.huawei03.com
                                 HSS域名  =  huawei03.com
                          UE可达请求参数  =  否
                           MPS优先级签约  =  0x0（未签约）
                            寻呼是否继续  =  是
                              UE挂起状态  =  否
  			     UEDRX参数  =  NULL
                              UE网络能力  =   FF7FFFFF0E0000 (EEA0; EEA1; EEA2; EEA3; EEA4; EEA5; EEA6; EEA7; EIA1; EIA2; EIA3; EIA4; EIA5; EIA6; EIA7; UEA0; UEA1; UEA2; UEA3; UEA4; UEA5; UEA6; UEA7; UCS2; UIA1; UIA2; UIA3; UIA4; UIA5; UIA6; UIA7; LPP; LCS; 1xSRVCC)
                              MS网络能力  =  000000E541
                                使用RFSP  =  NULL
              Mobile Station Classmark 2  =  NULL
              Mobile Station Classmark 3  =  NULL
                    Supported codec list  =  NULL
                                 ISR状态  =  未激活
                                 ARD参数  =  2000 (Hotonon3gppaccessForbid)
                              UE无线能力  =  NULL
                               VLR可靠性  =  不可靠
                                 VLR编号  =  1230301
                           非EPS提醒标志  =  否
                             SGs关联状态  =  关联未建立
  			 仅支持SMS功能  =  否
                          IMSI未鉴权指示  =  否
                         MME紧急服务状态  =  非紧急呼叫用户
                          用户是否被抑制  =  否
           签约的周期RAU/TAU定时器（秒）  =  0
         UE请求的长周期RAU/TAU定时器(秒)  =  0
         使用的长周期RAU/TAU定时器(分钟)  =  0
            使用的Active timer定时器(秒)  =  NULL
  	                UE无线寻呼能力  =  NULL
  		        推荐的小区数目  =  0
  		        推荐的小区列表  =  NULL
  		      推荐的eNodeB数目  =  0
  		      推荐的eNodeB列表  =  NULL
  		        上次驻留的ECGI  =  NULL
  		    上次驻留的覆盖等级  =  NULL
                    UE请求的寻呼周期(秒)  =  NULL
            UE请求的寻呼时间窗口时长(秒)  =  NULL
                      使用的寻呼周期(秒)  =  NULL
              使用的寻呼时间窗口时长(秒)  =  NULL
                                是否挂起  =  否
                                优选指示  =  NULL
               MME支持该UE的数据传输能力  =  CP CIoT Only
                      建议缓存下行包数量  =  0
                     签约的UE USAGE TYPE  =  NULL
                     使用的UE USAGE TYPE  =  NULL
  	            T3448剩余时长（秒） =  0
                      用户HSS Bypass状态  =  FALSE
                      用户HLR Bypass状态  =  FALSE
                             PSCell 信息  =  NULL
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-MMCTX.md`
