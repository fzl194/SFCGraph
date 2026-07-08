---
id: UNC@20.15.2@MMLCommand@MOD GTPCT3N3
type: MMLCommand
name: MOD GTPCT3N3（修改GTP-C T3N3参数）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: GTPCT3N3
command_category: 配置类
applicable_nf:
- SGW-C
- PGW-C
- AMF
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- GTP-C接口配置管理
- GTP-C T3_N3参数
status: active
---

# MOD GTPCT3N3（修改GTP-C T3N3参数）

## 功能

**适用NF：SGW-C、PGW-C、AMF、GGSN**

该命令用于修改GTP-C T3N3参数配置。

## 注意事项

- 该命令执行后立即生效。

- 当SET AMFN26PLCY命令中N26ITFMODE取值为“COMBINE”时，当前命令无效，请使用命令SET T3N3配置。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NODETYPE | 网元类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定设置T3N3参数的网元类型。<br>数据来源：全网规划<br>取值范围：<br>- SGW（SGW）<br>- PGW（PGW）<br>- GGSN（GGSN）<br>- AMF（AMF）<br>- SPGW（SPGW）<br>默认值：无<br>配置原则：无 |
| SGWMSGTYPE | SGW网元消息类型 | 可选必选说明：该参数在"NODETYPE"配置为"SGW"时为条件必选参数。<br>参数含义：该参数用于指定设置T3N3的SGW网元的消息类型。<br>数据来源：全网规划<br>取值范围：<br>- CRT_SESSION_REQ（Create Session Request）<br>- MOD_BEARER_REQ（Modify Bearer Request）<br>- DEL_SESSION_REQ（Delete Session Request）<br>- MOD_BEARER_CMD（Modify Bearer Command）<br>- CRT_BEARER_REQ（Create Bearer Request）<br>- UPD_BEARER_REQ（Update Bearer Request）<br>- DEL_BEARER_CMD（Delete Bearer Command）<br>- DEL_BEARER_REQ（Delete Bearer Request）<br>- DWLNK_DATA_NOTF（Downlink Data Notification）<br>- RMT_UE_RPT_NOTF（Remote UE Report Notification）<br>- CHG_NOTIF_REQ（Change Notification Request）<br>- BEARER_RES_CMD（Bearer Resource Command）<br>- SUSPEND_NOTIF（Suspend Notification）<br>- RESUME_NOTIF（Resume Notification）<br>- PGW_RST_NOTF（PGW Restart Notification）<br>- PGWDN_TRIG_NOTF（PGW Downlink Triggering Notification）<br>- ALL（All Messages）<br>默认值：无<br>配置原则：无 |
| PGWMSGTYPE | PGW网元消息类型 | 可选必选说明：该参数在"NODETYPE"配置为"PGW"时为条件必选参数。<br>参数含义：参数用于指定设置T3N3的PGW网元的消息类型。<br>数据来源：全网规划<br>取值范围：<br>- CRT_BEARER_REQ（Create Bearer Request）<br>- UPD_BEARER_REQ（Update Bearer Request）<br>- DEL_BEARER_REQ（Delete Bearer Request）<br>- PGWDN_TRIG_NOTF（PGW Downlink Triggering Notification）<br>- ALL（All Messages）<br>默认值：无<br>配置原则：无 |
| GGSNMSGTYPE | GGSN网元消息类型 | 可选必选说明：该参数在"NODETYPE"配置为"GGSN"时为条件必选参数。<br>参数含义：该参数用于指定设置T3N3的GGSN网元的消息类型。<br>数据来源：全网规划<br>取值范围：<br>- UPD_PDP_CTX_REQ（Update PDP Context Request）<br>- DEL_PDP_CTX_REQ（Delete PDP Context Request）<br>- INT_PDP_CTX_REQ（Initiate PDP Context Activation Request）<br>- ALL（All Messages）<br>默认值：无<br>配置原则：无 |
| AMFMSGTYPE | AMF网元消息类型 | 可选必选说明：该参数在"NODETYPE"配置为"AMF"时为条件必选参数。<br>参数含义：该参数用于指定设置T3N3的AMF网元的消息类型。<br>数据来源：全网规划<br>取值范围：<br>- IDENTIF_REQ（Identification Request）<br>- CONTEXT_REQ（Context Request）<br>- CONTEXT_RSP（Context Response）<br>- FWDRELOCATE_REQ（Forward Relocation Request）<br>- FWRELO_COM_NOTF（Forward Relocation Complete Notification）<br>- RELOC_CANCL_REQ（Relocation Cancel Request）<br>- ALL（All Messages）<br>默认值：无<br>配置原则：无 |
| SPGWMSGTYPE | SPGW网元消息类型 | 可选必选说明：该参数在"NODETYPE"配置为"SPGW"时为条件必选参数。<br>参数含义：参数用于指定设置T3N3的SPGW网元的消息类型。<br>数据来源：全网规划<br>取值范围：<br>- CRT_BEARER_REQ（Create Bearer Request）<br>- UPD_BEARER_REQ（Update Bearer Request）<br>- DWLNK_DATA_NOTF（Downlink Data Notification）<br>- ALL（All Messages）<br>- DEL_BEARER_REQ（Delete Bearer Request）<br>默认值：无<br>配置原则：无 |
| T3 | 请求消息重发间隔 | 可选必选说明：可选参数<br>参数含义：该参数用于指定等待一条请求消息的响应消息的最大时长。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~20，单位是秒。<br>默认值：无<br>配置原则：无 |
| N3 | 请求消息发送次数 | 可选必选说明：可选参数<br>参数含义：该参数用于指定发送一条请求消息的最大尝试次数。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~6。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@GTPCT3N3]] · GTP-C T3N3参数（GTPCT3N3）

## 使用实例

修改网元类型为SGW的Create Session Request消息的重发间隔为5秒，发送次数4次：

```
MOD GTPCT3N3:  NODETYPE=SGW, SGWMSGTYPE=CRT_SESSION_REQ, T3=5, N3=4;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-GTPCT3N3.md`
