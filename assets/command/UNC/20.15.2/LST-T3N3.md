---
id: UNC@20.15.2@MMLCommand@LST T3N3
type: MMLCommand
name: LST T3N3（查询GTP-C T3/N3参数配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: T3N3
command_category: 查询类
applicable_nf:
- SGSN
- MME
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- GTP-C接口管理
- GTP-C协议管理
- GTP-C协议参数配置
status: active
---

# LST T3N3（查询GTP-C T3/N3参数配置）

## 功能

**适用网元：SGSN、MME、AMF**

该命令用来查询GTP路径的T3和N3参数。

## 注意事项

- 当命令**[SET AMFN26PLCY](../../../../../接口管理/GTP-C接口配置管理/N26接口管理/N26策略管理/设置AMF N26接口策略（SET AMFN26PLCY）_62817114.md)**的参数“N26ITFMODE”取值为“COMBINE”时，该命令适用于SGSN、MME、AMF，否则，该命令仅适用于SGSN、MME。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GTPVER | GTP版本 | 可选必选说明：必选参数<br>参数含义：该参数用于指定的GTP版本。<br>取值范围：<br>- “GTPv0(GTPv0)”<br>- “GTPv1(GTPv1)”<br>- “GTPv2(GTPv2)”<br>默认值：无 |
| V0MSGCLS | V0消息分类 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定GTP版本为V0时的消息分类。<br>前提条件：该参数在<br>“GTPVER”<br>设置为<br>“GTPv0(GTPv0)”<br>时，才需要配置。<br>取值范围：<br>- “PM(路径管理)”<br>- “TM(隧道管理)”<br>- “LM(位置管理)”<br>- “MM(移动管理)”<br>默认值：无 |
| V0SPMMSGTYPE | V0 PM消息类型 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定GTP版本为V0时路径管理的消息类型。<br>前提条件：该参数在<br>“V0MSGCLS”<br>设置为<br>“PM(路径管理)”<br>时，才需要配置。<br>取值范围：<br>“ECHO_REQ(Echo Request)”<br>默认值：无 |
| V0STMMSGTYPE | V0 TM消息类型 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定GTP版本为V0时隧道管理的消息类型。<br>前提条件：该参数在<br>“V0MSGCLS”<br>设置为<br>“TM(隧道管理)”<br>时，才需要配置。<br>取值范围：<br>- “CREATE_PDP(生成PDP上下文请求)”<br>- “UPDATE_PDP(更新PDP上下文请求)”<br>- “DELETE_PDP(删除PDP上下文请求)”<br>- “CREATE_AA_PDP(生成AA PDP上下文请求)”<br>- “DELETE_AA_PDP(删除AA PDP上下文请求)”<br>- “PDP_NOTIF_REJECT(PDU Notification拒绝请求)”<br>默认值：无 |
| V0SLMMSGTYPE | V0 LM消息类型 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定GTP版本为V0时位置管理的消息类型。<br>前提条件：该参数在<br>“V0MSGCLS”<br>设置为<br>“LM(位置管理)”<br>时，才需要配置。<br>取值范围：<br>- “SEND_ROUTE_INFO(Send Routeing Information for GPRS Request)”<br>- “FAILURE_REPORT(Failure Report Request)”<br>- “NOTE_GPRS_PRESENT(Note MS GPRS Present Request)”<br>默认值：无 |
| V0SMMMSGTYPE | V0 MM消息类型 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定GTP版本为V0时移动管理的消息类型。<br>前提条件：该参数在<br>“V0MSGCLS”<br>设置为<br>“MM(移动管理)”<br>时，才需要配置。<br>取值范围：<br>- “IDENDIF_REQ(Identification Request)”<br>- “SGSN_CONTEXT_REQ(SGSN Context Request)”<br>- “SGSN_CONTEXT_RESP(SGSN Context Response)”<br>默认值：无 |
| V1MSGCLS | V1消息分类 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定GTP版本为V1时的消息分类。<br>前提条件：该参数在<br>“GTPVER”<br>取值为<br>“GTPv1(GTPv1)”<br>时，才需要配置。<br>取值范围：<br>- “PM(路径管理)”<br>- “TM(隧道管理)”<br>- “LM(位置管理)”<br>- “MM(移动管理)”<br>- “MBMS(多媒体广播和多播业务)”<br>默认值：无 |
| V1SPMMSGTYPE | V1 PM消息类型 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定GTP版本为V1时路径管理的消息类型。<br>前提条件：该参数在<br>“V1MSGCLS”<br>设置为<br>“PM(路径管理)”<br>时，才需要配置。<br>取值范围：<br>“ECHO_REQ(Echo Request)”<br>默认值：无 |
| V1STMMSGTYPE | V1 TM消息类型 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定GTP版本为V1时隧道管理的消息类型。<br>前提条件：该参数在<br>“V1MSGCLS”<br>设置为<br>“TM(隧道管理)”<br>时，才需要配置。<br>取值范围：<br>- “CREATE_PDP(生成PDP上下文请求)”<br>- “UPDATE_PDP(更新PDP上下文请求)”<br>- “DELETE_PDP(删除PDP上下文请求)”<br>- “PDP_NOTIF_REJECT(PDU Notification拒绝请求)”<br>默认值：无 |
| V1SLMMSGTYPE | V1 LM消息类型 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定GTP版本为V1时位置管理的消息类型。<br>前提条件：该参数在<br>“V1MSGCLS”<br>设置为<br>“LM(位置管理)”<br>时，才需要配置。<br>取值范围：<br>- “SEND_ROUTE_INFO(Send Routeing Information for GPRS Request)”<br>- “FAILURE_REPORT(Failure Report Request)”<br>- “NOTE_GPRS_PRESENT(Note MS GPRS Present Request)”<br>默认值：无 |
| V1SMMMSGTYPE | V1 MM消息类型 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定GTP版本为V1时移动管理的消息类型。<br>前提条件：该参数在<br>“V1MSGCLS”<br>设置为<br>“MM(移动管理)”<br>时，才需要配置。<br>取值范围：<br>- “IDENDIF_REQ(Identification Request)”<br>- “SGSN_CONTEXT_REQ(SGSN Context Request)”<br>- “SGSN_CONTEXT_RESP(SGSN Context Response)”<br>- “FORRELOCATE_REQ(Forward Relocation Request)”<br>- “FORRELOCATE_COMPLETE(Forward Relocation Complete)”<br>- “RELOCATE_CANCEL_REQ(Relocation Cancel Request)”<br>- “FORSRNS_CONTEXT(Forward SRNS Context)”<br>默认值：无 |
| V1SMBMSMSGTYPE | V1 MBMS消息类型 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定GTP版本为V1时消息类型。<br>前提条件：该参数在<br>“V1MSGCLS”<br>设置为<br>“MBMS(多媒体广播和多播业务)”<br>时，才需要配置。<br>取值范围：<br>- “MBMS_START_RESP(MBMS Session Start Response)”<br>- “MBMS_NOTIF_REJECT(MBMS Notification Reject Request)”<br>- “CREATE_MBMS_CONTEXT(Create MBMS Context Request)”<br>- “UPDATE_MBMS_CONTEXT(Update MBMS Context Request)”<br>- “DELETE_MBMS_CONTEXT(Delete MBMS Context Request)”<br>- “MBMS_REGIST(MBMS Registration Request)”<br>- “MBMS_DE_REGIST(MBMS De-Registration Request)”<br>- “MBMS_SESSION_STOP(MBMS Session Stop Response)”<br>- “MBMS_SESSION_UPDATE(MBMS Session Update Response)”<br>- “INFO_CHANGE_NOTIF_REQ(MS Info Change Notification Request)”<br>默认值：无 |
| V2MSGCLS | V2消息分类 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定GTP版本为V2时的消息分类。<br>前提条件：该参数在<br>“GTPVER”<br>设置为<br>“GTPv2(GTPv2)”<br>时，才需要配置。<br>取值范围：<br>- “PM(路径管理)”<br>- “TM(隧道管理)”<br>- “MM(移动管理)”<br>- “CS_FALLBACK(CS Fallback相关)”<br>- “Non_3GPP_ACCESS(Non-3GPP access相关)”<br>- “AM(AMF移动管理)”<br>默认值：无 |
| V2SPMMSGTYPE | V2 PM消息类型 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定GTP版本为V2时路径管理的消息类型。<br>前提条件：该参数在<br>“V2MSGCLS”<br>设置为<br>“PM(路径管理)”<br>时，才需要配置。<br>取值范围：<br>“ECHO_REQ(Echo Request)”<br>默认值：无 |
| V2STMMSGTYPE | V2 TM消息类型 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定GTP版本为V2时隧道管理的消息类型。<br>前提条件：该参数在<br>“V2MSGCLS”<br>设置为<br>“TM(隧道管理)”<br>时，才需要配置。<br>取值范围：<br>- “CREATE_SESSION(Create Session Request)”<br>- “UPDATE_USER_PLANE(Update User Plane Request)”<br>- “MOD_BEARER_REQ(Modify Bearer Request)”<br>- “DEL_SESSION_REQ(Delete Session Request)”<br>- “MOD_BEARER_CMD(Modify Bearer Command)”<br>- “DEL_BEARER_CMD(Delete Bearer Command)”<br>- “BEARER_RES_CMD(Bearer Resource Command)”<br>- “CREATE_INDIRECT_DATA(Create Indirect Data Forwarding Tunnel Request)”<br>- “DELETE_INDIRECT_DATA(Delete Indirect Data Forwarding Tunnel Request)”<br>- “RELEASE_ACCESS_BEARER_REQ(Release Access Bearers Request)”<br>默认值：无 |
| V2SMMMSGTYPE | V2 MM消息类型 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定GTP版本为V2时移动管理的消息类型。<br>前提条件：该参数在<br>“V2MSGCLS”<br>设置为<br>“MM(移动管理)”<br>时，才需要配置。<br>取值范围：<br>- “SRVCC_PS_CS_REQ(SRVCC PS to CS Request)”<br>- “SRVCC_PS_CS_COMPLETE_NOTIFY(SRVCC PS to CS Complete Notification)”<br>- “SRVCC_PS_CS_CANCEL_NOTIFY(SRVCC PS to CS Cancel Notification)”<br>- “CHANGE_NOTIF_REQ(Change Notification Request)”<br>- “IDENTIF_REQ(Identification Request)”<br>- “CONTEXT_REQ(Context Request)”<br>- “CONTEXT_RESP(Context Response)”<br>- “FORRELOCATE_REQ(Forward Relocation Request)”<br>- “FORRELOCATE_COMPLETE_NOTIF(Forward Relocation Complete Notification)”<br>- “FORSRNS_CONTEXT_NOTIF(Forward SRNS Context Notification)”<br>- “RELOCATE_CANCEL_REQ(Relocation Cancel Request)”<br>- “DETACH_NOTIF(Detach Notification)”<br>- “CONTEXT_REQ_EX(Context Request Extended)”<br>默认值：无<br>说明：- 当取值为“SRVCC_PS_CS_REQ(SRVCC PS to CS Request)”时：- 在SRVCC流程中，[**SET T3N3**](设置GTP-C T3_N3参数配置(SET T3N3)_26305730.md)设置的定时器用于等待PS to CS Response消息。<br>- 在基于SRVCC的数据语音双切换流程中，[**SET T3N3**](设置GTP-C T3_N3参数配置(SET T3N3)_26305730.md)设置的定时器用于同时等待PS to CS Response和Forward Relocation Response消息。<br>- 当取值为“SRVCC_PS_CS_COMPLETE_NOTIFY(SRVCC PS to CS Complete Notification)”时：- 在SRVCC流程中，[**SET T3N3**](设置GTP-C T3_N3参数配置(SET T3N3)_26305730.md)设置的定时器用于等待PS to CS Complete Notification消息。<br>- 在基于SRVCC的数据语音双切换流程中，[**SET T3N3**](设置GTP-C T3_N3参数配置(SET T3N3)_26305730.md)设置的定时器用于同时等待PS to CS Complete Notification和Forward Relocation Complete消息。<br>- “CONTEXT_REQ_EX(Context Request Extended)”设置的定时器用于在POOL内TAU流程中等待Context Response消息。其他场景，使用“CONTEXT_REQ(Context Request)”的配置。 |
| V2CS_FALLBACKMSGTYPE | V2 CS_FALLBACK消息类型 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定消息类型。<br>前提条件：该参数在<br>“V2MSGCLS”<br>设置为<br>“CS_FALLBACK(CS Fallback相关)”<br>时，才需要配置。<br>取值范围：<br>- “GMT_SUSPEND_NOTIFICATION(GMT暂停通知)”<br>- “GMT_RESUME_NOTIFICATION(GMT重新开始)”<br>默认值：无 |
| V2NON_3GPP_ACCESSTYPE | V2 NON_3GPP_ACCESS消息类型 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定GTP版本为V2时NON_3GPP_ACCESS消息类型。<br>前提条件：该参数在<br>“V2MSGCLS”<br>设置为<br>“Non_3GPP_ACCESS(Non-3GPP access相关)”<br>时，才需要配置。<br>取值范围：<br>“GMT_CREATE_FORWARD_TUNNEL_REQ(GMT创建转发隧道)”<br>默认值：无 |
| V2SAMMSGTYPE | V2 AM消息类型 | 可选必选说明：条件可选参数<br>参数含义：该参数用于控制如果AMF N26接口采用融合部署模式时（SET AMFN26PLCY命令“N26ITFMOD”配置为“COMBINE”），指定GTP版本为V2时AMF移动管理的消息类型。<br>前提条件：该参数在<br>“V2MSGCLS”<br>设置为<br>“AM(AMF移动管理)”<br>时，该参数有效。<br>取值范围：<br>- “NG_IDENTIF_REQ(Identification Request(NG))”<br>- “NG_CONTEXT_REQ(Context Request(NG))”<br>- “NG_CONTEXT_RESP(Context Response(NG))”<br>- “NG_FORRELOCATE_REQ(Forward Relocation Request(NG))”<br>- “NG_FORRELOCATE_COMPLETE_NOTIF(Forward Relocation Complete Notification(NG))”<br>- “NG_RELOCATE_CANCEL_REQ(Relocation Cancel Request(NG))”<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@T3N3]] · GTP-C T3/N3参数配置（T3N3）

## 使用实例

查询GTP版本为GTPv1，V1消息分类为TM隧道管理的参数配置。

LST T3N3: GTPVER=GTPv1, V1MSGCLS=TM;

```
%%LST T3N3： GTPVER=GTPv1, V1MSGCLS=TM;%%
RETCODE = 0  操作成功。

操作结果如下
-------------------------
 GTP版本       V1消息类型                     T3-RESPONSE(s)  多跳消息T3增量       N3-REQUEST(times)    多跳消息N3增量

 GTPv1        生成PDP上下文请求               7               0                    2                    0                         
 GTPv1        更新PDP上下文请求               7               0                    2                    0                         
 GTPv1        删除PDP上下文请求               7               0                    2                    0                         
 GTPv1        PDU Notification拒绝请求        7               0                    2                    0                         
(结果个数 = 4)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-T3N3.md`
