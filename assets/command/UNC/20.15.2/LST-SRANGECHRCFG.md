---
id: UNC@20.15.2@MMLCommand@LST SRANGECHRCFG
type: MMLCommand
name: LST SRANGECHRCFG（查询小范围CHR生成规则）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SRANGECHRCFG
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
- 移动性管理
- CHR管理
- 小范围CHR流程配置
status: active
---

# LST SRANGECHRCFG（查询小范围CHR生成规则）

## 功能

**适用网元：SGSN、MME**

该命令用于查询小范围CHR单据的生成规则。

## 注意事项

- 该命令执行后立即生效。
- 如果不输入任何参数，执行该命令会显示所有记录。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：可选参数<br>参数含义：该参数用于指定启用功能的用户范围。<br>数据来源：本端规划<br>取值范围：枚举类型<br>- “E_SPECIAL_IMSI(用户IMSI生成小范围CHR单据)”：指定用户IMSI前缀生成小范围CHR单据。<br>- “E_SPECIAL_IMEI(终端IMEI生成小范围CHR单据)”：指定终端IMEI前缀生成小范围CHR单据。<br>- “E_SPECIAL_ENB(该eNodeB下的4G用户生成小范围CHR单据)”：指定该eNodeB下的4G用户生成小范围CHR单据。<br>- “E_SPECIAL_TAI(该TAI下的4G用户生成小范围CHR单据)”：指定该TAI下的4G用户生成小范围CHR单据。<br>- “E_SPECIAL_RAI(该RAI下的2/3G用户生成小范围CHR单据)”：指定该RAI下的2/3G用户生成小范围CHR单据。<br>- “E_SPECIAL_APNQCI(签约特定APNNI和QCI的4G用户生成小范围CHR单据)”: 签约特定APNNI和QCI的4G用户生成小范围CHR单据。<br>默认值：无 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定IMSI前缀。<br>前提条件：该参数在<br>“用户范围”<br>设置为<br>“E_SPECIAL_IMSI”<br>后生效。<br>数据来源：全网规划<br>取值范围：11～15位十进制数字字符串<br>默认值：无 |
| IMEIPRE | IMEI前缀 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定IMEI前缀。<br>前提条件：该参数在<br>“用户范围”<br>设置为<br>“E_SPECIAL_IMEI”<br>后生效。<br>数据来源：全网规划<br>取值范围：11～15位十进制数字字符串<br>默认值：无 |
| MCC | 移动国家码 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定生成单据的移动国家码。<br>前提条件： 该参数在<br>“用户范围”<br>设置为<br>“E_SPECIAL_ENB”<br>，<br>“E_SPECIAL_TAI”<br>或<br>“E_SPECIAL_RAI”<br>后生效。<br>数据来源：全网规划<br>取值范围：长度为3的十进制数字<br>默认值：无 |
| MNC | 移动网号 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定生成单据的移动网号。<br>前提条件： 该参数在<br>“用户范围”<br>设置为<br>“E_SPECIAL_ENB”<br>，<br>“E_SPECIAL_TAI”<br>或<br>“E_SPECIAL_RAI”<br>后生效。<br>数据来源：全网规划<br>取值范围：长度为2～3的十进制数字<br>默认值：无 |
| ENODEBID | eNodeB标识 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定eNodeB的ID。<br>前提条件：该参数在<br>“用户范围”<br>设置为<br>“E_SPECIAL_ENB”<br>后生效。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为0~268435455。<br>默认值：无 |
| TAC | 跟踪区域码 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定跟踪区域码<br>前提条件：该参数在<br>“用户范围”<br>设置为<br>“E_SPECIAL_TAI”<br>后生效。<br>数据来源：全网规划<br>取值范围：0x0000～0xFFFF 。<br>默认值：无 |
| LAC | 位置区域码 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定位置区域码<br>前提条件：该参数在<br>“用户范围”<br>设置为<br>“E_SPECIAL_RAI”<br>后生效。<br>数据来源：全网规划<br>取值范围：0x0000～0xFFFF 。<br>默认值：无 |
| RAC | 寻呼范围路由区域码 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定路由区域码<br>前提条件：该参数在<br>“用户范围”<br>设置为<br>“E_SPECIAL_RAI”<br>后生效。<br>数据来源：全网规划<br>取值范围：0x00～0xFF 。<br>默认值：无 |
| APNNI | APN网络标识 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定签约的APNNI。<br>前提条件：该参数在<br>“用户范围”<br>设置为<br>“E_SPECIAL_APNQCI”<br>后生效。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1~62。<br>默认值：无 |
| QCI | QCI值 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定签约的QCI。<br>前提条件：该参数在<br>“用户范围”<br>设置为<br>“E_SPECIAL_APNQCI”<br>后生效。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为1~254。<br>默认值：无 |

## 操作的配置对象

- [小范围CHR生成规则（SRANGECHRCFG）](configobject/UNC/20.15.2/SRANGECHRCFG.md)

## 使用实例

查询小范围CHR生成规则：

LST SRANGECHRCFG:;

```
%%LST SRANGECHRCFG:;%%
RETCODE = 0  操作成功

操作结果如下
------------------------
                 用户范围 = 用户IMSI生成小范围CHR单据
                 IMSI前缀 = 123456000000000
                 IMEI前缀 = NULL
               移动国家码 = NULL
                 移动网号 = NULL
               eNodeB标识 = NULL
               跟踪区域码 = NULL
               位置区域码 = NULL
       寻呼范围路由区域码 = NULL
              APN网络标识 = NULL
                    QCI值 = NULL
Gb模式流程成功时上报选项  =  Other Procedure & Attach & Detach & Routing Area Update & Inter System Change & PDP Context Activation & PDP Context Deactivation & PDP Context Modification & Paging & Suspend & Cancel Location & RESERVED1 & RESERVED2 & RESERVED3 & RESERVED4 & RESERVED5 & RESERVED6 & RESERVED7 & RESERVED8 & RESERVED9 & RESERVED10 & RESERVED11 & RESERVED12 & RESERVED13 & RESERVED14 & RESERVED15
Gb模式流程失败时上报选项  =  Other Procedure & Attach & Detach & Routing Area Update & Inter System Change & PDP Context Activation & PDP Context Deactivation & PDP Context Modification & Paging & Suspend & Cancel Location & RESERVED1 & RESERVED2 & RESERVED3 & RESERVED4 & RESERVED5 & RESERVED6 & RESERVED7 & RESERVED8 & RESERVED9 & RESERVED10 & RESERVED11 & RESERVED12 & RESERVED13 & RESERVED14 & RESERVED15
Iu模式流程成功时上报选项  =  Other Procedure & Attach & Detach & Routing Area Update & SRNS Relocation & Inter System Change & IU Release & Service Request & PDP Context Activation & PDP Context Deactivation & PDP Context Modification & Paging & RAB Assignment in Service Request & Suspend & Location Report & Cancel Location & RESERVED1 & RESERVED2 & RESERVED3 & RESERVED4 & RESERVED5 & RESERVED6 & RESERVED7 & RESERVED8 & RESERVED9 & RESERVED10 & RESERVED11 & RESERVED12 & RESERVED13 & RESERVED14
Iu模式流程失败时上报选项  =  Other Procedure & Attach & Detach & Routing Area Update & SRNS Relocation & Inter System Change & IU Release & Service Request & PDP Context Activation & PDP Context Deactivation & PDP Context Modification & Paging & RAB Assignment in Service Request & Suspend & Location Report & Cancel Location & RESERVED1 & RESERVED2 & RESERVED3 & RESERVED4 & RESERVED5 & RESERVED6 & RESERVED7 & RESERVED8 & RESERVED9 & RESERVED10 & RESERVED11 & RESERVED12 & RESERVED13 & RESERVED14
S1模式流程成功时上报选项  =  Other Procedure & Attach & Detach & Tracking Area Update & Inter System Change & S1 Handover & X2 Handover & Service Request & Paging & S1 Release & UE Requested PDN Connectivity & UE or MME Requested PDN Disconnection & Dedicated Bearer Activation & Bearer Modification & Dedicated Bearer Deactivation & SGS Paging & SRVCC & Location Report & Control Plane Service Request & P-GW-initiated PDN Disconnect & Connection Suspend & Reroute NAS & RESERVED2 & RESERVED3 & RESERVED6 
S1模式流程失败时上报选项  =  Other Procedure & Attach & Detach & Tracking Area Update & Inter System Change & S1 Handover & X2 Handover & Service Request & Paging & Bearer Modification & Dedicated Bearer Deactivation & SGS Paging & SRVCC & Location Report & Control Plane Service Request & Reroute NAS & E-RAB Modification Indication & RESERVED2 & RESERVED4 & RESERVED5  
      冲突流程时上报选项  =  LTE(4G)接入用户 & NBIOT接入用户 & RESERVED1 & RESERVED2 & RESERVED3 & RESERVED4 & RESERVED5 & RESERVED6
     CHR单据附加流程消息  =  NULL
                失效时间  =  2018-01-25 22:06:55

(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询小范围CHR生成规则（LST-SRANGECHRCFG）_26305430.md`
