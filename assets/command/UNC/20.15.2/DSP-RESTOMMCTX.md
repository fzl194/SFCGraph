---
id: UNC@20.15.2@MMLCommand@DSP RESTOMMCTX
type: MMLCommand
name: DSP RESTOMMCTX（显示容灾用户MM上下文信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: RESTOMMCTX
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

# DSP RESTOMMCTX（显示容灾用户MM上下文信息）

## 功能

**适用网元：MME**

- 本命令用于查询系统内容灾用户的MM上下文信息。
- 当某一字段显示“NULL”时，表示该字段没有备份。

## 注意事项

输出结果中包含用户的某些个人数据，如IMSI、IMEI、PDP地址等信息。建议您遵从国家的相关法律执行该任务，并采取足够的措施以确保用户的个人数据受到充分的保护。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QRYTP | 查询方式 | 可选必选说明：可选参数<br>参数含义：该参数用于指定查询备份用户信息的查询方式。<br>取值范围：<br>- “IMSI(指定IMSI)”<br>- “STMSI(指定S-TMSI)”<br>- “IMEI(指定IMEI)”<br>默认值：<br>“IMSI(指定IMSI)”<br>说明：根据IMEI查询仅适用于无卡的紧急呼叫用户。 |
| IMSI | IMSI | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定国际移动用户标识。<br>前提条件：此参数在<br>“查询方式”<br>设置为<br>“IMSI(指定IMSI)”<br>后生效。<br>取值范围：1~15位数字<br>默认值：无 |
| STMSI | STMSI | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定S-TMSI。<br>前提条件：此参数在<br>“查询方式”<br>设置为<br>“STMSI(指定S-TMSI)”<br>后生效。<br>取值范围：1~10位十六进制字符串<br>默认值：无<br>说明：当前系统不支持使用S-TMSI查询用户的<br>“MMSUBCTX(MM签约上下文)”<br>。 |
| IMEI | IMEI | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定用户设备的国际移动设备标识。<br>前提条件：此参数在<br>“查询方式”<br>设置为<br>“IMEI(指定IMEI)”<br>后生效。<br>取值范围：1~16位数字<br>默认值：无 |
| DISPINFO | 输出信息选择 | 可选必选说明：可选参数<br>参数含义：本参数用于指定查询结果输出内容的范围。<br>取值范围：<br>- “BRIEF_RESTO(二次呼叫恢复所需信息)”<br>- “MMCTX(MM上下文)”：MM动态上下文<br>- “MMSUBCTX(MM签约上下文)”：MM签约上下文<br>- “ALL(所有信息)”<br>默认值：ALL |

## 操作的配置对象

- [[configobject/UNC/20.15.2/RESTOMMCTX]] · 容灾用户MM上下文信息（RESTOMMCTX）

## 使用实例

查询IMSI号为123031501000001的系统内容灾用户的MM上下文信息：

DSP RESTOMMCTX: QRYTP=IMSI, IMSI="123031501000001";

```
%%DSP RESTOMMCTX: QRYTP=IMSI, IMSI="123031501000001";%%
RETCODE = 0  操作成功

MM签约上下文基本信息：
----------------------
IMSI   =  123031501000001
RU名称  =  MCR_SP_RU_0064
进程号  =  4
TSUI   =  007E000080050000
(结果个数 = 1)

仍有后续报告输出
---    END

%%DSP RESTOMMCTX: QRYTP=IMSI, IMSI="123031501000001";%%
RETCODE = 0  操作成功

MM签约上下文：
--------------
                         签约状态  =  可服务
                           MSISDN  =  500680
                         A-MSISDN  =  NULL
                           STN-SR  =  NULL
                          ICS指示  =  NULL
                     网络接入模式  =  混合用户
禁止漫游用户通过VPLMN的接入点接入  =  NULL
禁止漫游用户通过HPLMN的接入点接入  =  NULL
           禁止用户所有分组域业务  =  NULL
                 禁止用户所有呼出  =  NULL
                     ODBHPLMNData  =  0x0
                       区域码数目  =  NULL
                       区域码列表  =  NULL
                          ARD参数  =  0x20 (Hotonon3gppaccessForbid)
           签约的用户级别的APN OI  =  NULL
                         计费属性  =  0x0000(None)
          无线管理策略（RFSP ID）  =  NULL
       是否因为未支持特性禁止漫游  =  NULL
                    MPS优先级签约  =  NULL
                      MDT用户许可  =  NULL
                      上行UE-AMBR  =  20000000
                      下行UE-AMBR  =  20000000
          Teleservice Code Number  =  NULL
                 Teleservice Code  =  NULL(结果个数 = 1)

仍有后续报告输出
---    END

%%DSP RESTOMMCTX: QRYTP=IMSI, IMSI="123031501000001";%%
RETCODE = 0  操作成功

MM动态上下文基本信息：
----------------------
	IMSI  =  123031501000001
    RU名称  =  MCR_SP_RU_0064
      进程号  =  6
        GUTI  =  12303800142C0010000
        TSUI  =  00C2000580060000
(结果个数 = 1)

仍有后续报告输出
---    END

%%DSP RESTOMMCTX: QRYTP=IMSI, IMSI="123031501000001";%%
RETCODE = 0  操作成功

二次呼叫恢复信息:
-------------
UE上次接入时间(MME side)  =  2015-03-17 09:16:41+08:00
                 RAT类型  =  EUTRAN
        是否支持IMS VoPS  =  不支持
             MME用户状态  =  Connected Reachable For Paging
     E-UTRAN小区全局标识  =  123030000700
      最近一次TAU时的TAI  =  123037000
              跟踪区列表  =  123037000
              UE DRX参数  =  0A00
          UE无线寻呼能力  =  NULL
(结果个数 = 1)

仍有后续报告输出
---    END

%%DSP RESTOMMCTX: QRYTP=IMSI, IMSI="123031501000001";%%
RETCODE = 0  操作成功

MM上下文：
----------
                                     附着类型  =  EPS附着
                                 上行NAS count  =  1
                                    UE网络能力  =  FF7FFFFF0E (EEA0; EEA1; EEA2; EEA3; EEA4; EEA5; EEA6; EEA7; EIA1; EIA2; EIA3; EIA4; EIA5; EIA6; EIA7; UEA0; UEA1; UEA2; UEA3; UEA4; UEA5; UEA6; UEA7; UCS2; UIA1; UIA2; UIA3; UIA4; UIA5; UIA6; UIA7; LPP; LCS; 1xSRVCC)
                                   MS 网络能力  =  000008
Voice Domain Preference and UE's Usage Setting  =  0x03 (Voice centric; IMS PS voice preferred, CS Voice as secondary)
                    Mobile Station Classmark 2  =  5359A6
                    Mobile Station Classmark 3  =  NULL
                          Supported codec list  =  10028080
                             签约的上行UE-AMBR  =  20000000
                             签约的下行UE-AMBR  =  20000000
                         实际使用的上行UE-AMBR  =  10000000
                         实际使用的下行UE-AMBR  =  10000000
                                          IMEI  =  NULL
                               S102 IWS IP地址  =  0.0.0.0
                       无线管理策略（RFSP ID）  =  NULL
                                      使用RFSP  =  NULL
                                          时区  =  GMT-09:00
                                是否实行夏令时  =  是
                              时间偏移量(小时)  =  2
(结果个数 = 1)

仍有后续报告输出
---    END

%%DSP RESTOMMCTX: QRYTP=IMSI, IMSI="123031501000001";%%
RETCODE = 0  操作成功

GMLC列表
--------
查询结果  =  GMLC List Does Not Exist
(结果个数 = 1)

共有6个报告
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-RESTOMMCTX.md`
