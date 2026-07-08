---
id: UNC@20.15.2@MMLCommand@LST GTPCV2CMPT
type: MMLCommand
name: LST GTPCV2CMPT（查询GTP-C V2协议兼容性）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: GTPCV2CMPT
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
- GTP-C接口管理
- GTP-C协议管理
- GTP-C V2协议兼容性
status: active
---

# LST GTPCV2CMPT（查询GTP-C V2协议兼容性）

## 功能

**适用网元：SGSN、MME**

该命令用于查询GTP-C V2协议兼容性配置，相关配置可以控制 UNC 发送的GTPCv2消息是否携带特定信元以及定义相关信元的格式。

## 注意事项

此命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MSGCLS | 消息分类 | 可选必选说明：可选参数<br>参数含义：该参数用于指示消息分类。<br>取值范围：<br>- “PM(路径管理)”<br>- “TM(隧道管理)”<br>- “MM(移动管理)”<br>- “SV(SV接口)”<br>默认值：无 |
| MMMSGTYPE | 消息类型 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指示消息分类为移动管理时的消息类型。<br>前提条件：当<br>“MSGCLS”<br>取值为<br>“MM(移动管理)”<br>时，该参数有效。<br>取值范围：<br>- “FWD_RLC_REQ(Forward Relocation Request)”<br>- “CTX_RSP(Context Response)”<br>默认值：无 |
| FWDRLCREQ | Forward Relocation Request的信元类型 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指示消息类型为Forward Relocation Request时的信元类型。<br>前提条件：当<br>“MMMSGTYPE”<br>取值为<br>“FWD_RLC_REQ(Forward Relocation Request)”<br>时，该参数有效。<br>取值范围：<br>- “SERNET(Serving Network)”：该信元标识源MME/S4 SGSN选择的服务网络。用于多HPLMN特性中将源MME/S4-SGSN选择的服务网络通知对端。<br>- “SRVCCMMCTXT(Additional MM context for SRVCC)”：源MME/S4-SGSN获取了可用的MS Classmark2，MS Classmark3 and the Supported Codec，源MME/S4-SGSN应该发送此信元到目标MME/S4-SGSN。用于目标MME/S4-SGSN获取签约数据前发起SRVCC场景。<br>- “SRVCCFLG(Additional flags for SRVCC)”：源MME/S4-SGSN获取了可用的ICS Indicator信元，源MME/S4-SGSN应该发送此信元到目标MME/S4-SGSN。用于目标MME/S4-SGSN获取签约数据前发起SRVCC场景。<br>- “STN-SR(Session Transfer Number for SRVCC)”：源MME/S4-SGSN获取了可用的Session Transfer Number for SRVCC，源MME/S4-SGSN应该发送此信元到目标MME/S4-SGSN。用于目标MME/S4-SGSN获取签约数据前发起SRVCC场景。<br>- “C-MSISDN(Correlation MSISDN)”：源MME/S4-SGSN获取了可用的Correlation MSISDN，源MME/S4-SGSN应该发送此信元到目标MME/S4-SGSN。用于目标MME/S4-SGSN获取签约数据前发起SRVCC场景。<br>- “INDICATION(Indication)”：源MME/S4-SGSN发送给目标MME/S4-SGSN的一组处理指示。用于目标MME/S4-SGSN根据标识进行处理，处理策略参见[**ADD GTPCV2CMPT**](增加GTP-C V2协议兼容性(ADD GTPCV2CMPT)_26305734.md)命令的“FWDRLCREQIND”。<br>默认值：无 |
| CTXRSP | Context Response的信元类型 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指示消息类型为Context Response时的信元类型。<br>前提条件：当<br>“MMMSGTYPE”<br>取值为<br>“CTX_RSP(Context Response)”<br>时，该参数有效。<br>数据来源：整网规划<br>取值范围：<br>- “INDICATION(Indication)”：源MME/S4-SGSN发送给目标MME/S4-SGSN的一组处理指示。用于目标MME/S4-SGSN根据标识进行处理，处理策略参见[**ADD GTPCV2CMPT**](增加GTP-C V2协议兼容性(ADD GTPCV2CMPT)_26305734.md)命令的“CTXRSPIND”。<br>默认值：无 |
| SVMSGTYPE | 消息类型 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指示消息分类为SV接口时的消息类型。SV接口是MME或SGSN和MSC之间用于SRVCC的接口。<br>前提条件：当<br>“MSGCLS”<br>取值为<br>“SV(SV接口)”<br>时，该参数有效。<br>数据来源：整网规划<br>取值范围：<br>“PS_TO_CS_REQ(SRVCC PS to CS Request)”<br>默认值：无 |
| PSTOCSREQ | SRVCC PS to CS Request的信元类型 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指示消息类型为SRVCC PS to CS Request时的信元类型。<br>前提条件：当<br>“SVMSGTYPE”<br>取值为<br>“PS_TO_CS_REQ(SRVCC PS to CS Request)”<br>时，该参数有效。<br>数据来源：整网规划<br>取值范围：<br>“STN-SR(Session Transfer Number for SRVCC)”<br>默认值：无 |
| TMMSGTYPE | 消息类型 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指示消息分类为隧道管理时的消息类型。<br>前提条件：当<br>“MSGCLS”<br>取值为<br>“TM(隧道管理)”<br>时，该参数有效。<br>数据来源：整网规划<br>取值范围：<br>- “CRT_SES_REQ(Create Session Request)”<br>- “MOD_BR_REQ(Modify Bearer Request)”<br>默认值：无 |
| CRTSESREQ | Create Session Request的信元类型 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指示消息类型为Create Session Request时的信元类型<br>前提条件：该参数在<br>“消息类型”<br>参数配置为<br>“Create Session Request”<br>后生效。<br>数据来源：整网规划<br>取值范围：<br>“INDICATION(Indication)”<br>默认值：无 |
| MODBRREQ | Modify Bearer Request的信元类型 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指示消息类型为Modify Bearer Request时的信元类型<br>前提条件：当<br>“TMMSGTYPE”<br>取值为<br>“MOD_BR_REQ(Modify Bearer Request)”<br>时，该参数有效。<br>数据来源：整网规划<br>取值范围：<br>“BCMOD(Bearer Contexts to be modified)”<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/GTPCV2CMPT]] · GTP-C V2协议兼容性（GTPCV2CMPT）

## 使用实例

查询GTP-C V2协议兼容性的配置：

LST GTPCV2CMPT:;

```
%%LST GTPCV2CMPT:;%%
RETCODE = 0  操作成功。

操作结果如下
--------------
                                  索引  =  1
                              消息分类  =  隧道管理
                              消息类型  =  Create Session Request
                              信元类型  =  UP Function Selection Indication Flags
                              携带方式  =  NULL
                              编码方式  =  NULL
                      Indication Bit位  =  NULL
                            F-TEID取值  =  NULL
UP Function Selection Indication Flags  =  Dual connectivity with NR
           是否支持LTE-M类型的RAT TYPE  =  不支持

(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-GTPCV2CMPT.md`
