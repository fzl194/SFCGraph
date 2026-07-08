---
id: UNC@20.15.2@MMLCommand@LST GTPCT3N3
type: MMLCommand
name: LST GTPCT3N3（查询GTP-C T3N3参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: GTPCT3N3
command_category: 查询类
applicable_nf:
- SGW-C
- PGW-C
- AMF
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- GTP-C接口配置管理
- GTP-C T3_N3参数
status: active
---

# LST GTPCT3N3（查询GTP-C T3N3参数）

## 功能

**适用NF：SGW-C、PGW-C、AMF、GGSN**

该命令用于查询GTP-C T3N3参数配置。

## 注意事项

当SET AMFN26PLCY命令中N26ITFMODE取值为“COMBINE”时，当前命令无效，请使用命令LST T3N3查询。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NODETYPE | 网元类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定设置T3N3参数的网元类型。<br>数据来源：全网规划<br>取值范围：<br>- SGW（SGW）<br>- PGW（PGW）<br>- GGSN（GGSN）<br>- AMF（AMF）<br>- SPGW（SPGW）<br>默认值：无<br>配置原则：无 |
| SGWMSGTYPE | SGW网元消息类型 | 可选必选说明：该参数在"NODETYPE"配置为"SGW"时为条件可选参数。<br>参数含义：该参数用于指定设置T3N3的SGW网元的消息类型。<br>数据来源：全网规划<br>取值范围：<br>- CRT_SESSION_REQ（Create Session Request）<br>- MOD_BEARER_REQ（Modify Bearer Request）<br>- DEL_SESSION_REQ（Delete Session Request）<br>- MOD_BEARER_CMD（Modify Bearer Command）<br>- CRT_BEARER_REQ（Create Bearer Request）<br>- UPD_BEARER_REQ（Update Bearer Request）<br>- DEL_BEARER_CMD（Delete Bearer Command）<br>- DEL_BEARER_REQ（Delete Bearer Request）<br>- DWLNK_DATA_NOTF（Downlink Data Notification）<br>- RMT_UE_RPT_NOTF（Remote UE Report Notification）<br>- CHG_NOTIF_REQ（Change Notification Request）<br>- BEARER_RES_CMD（Bearer Resource Command）<br>- SUSPEND_NOTIF（Suspend Notification）<br>- RESUME_NOTIF（Resume Notification）<br>- PGW_RST_NOTF（PGW Restart Notification）<br>- PGWDN_TRIG_NOTF（PGW Downlink Triggering Notification）<br>- ALL（All Messages）<br>默认值：无<br>配置原则：无 |
| PGWMSGTYPE | PGW网元消息类型 | 可选必选说明：该参数在"NODETYPE"配置为"PGW"时为条件可选参数。<br>参数含义：该参数用于指定设置T3N3的PGW网元的消息类型。<br>数据来源：全网规划<br>取值范围：<br>- CRT_BEARER_REQ（Create Bearer Request）<br>- UPD_BEARER_REQ（Update Bearer Request）<br>- DEL_BEARER_REQ（Delete Bearer Request）<br>- PGWDN_TRIG_NOTF（PGW Downlink Triggering Notification）<br>- ALL（All Messages）<br>默认值：无<br>配置原则：无 |
| GGSNMSGTYPE | GGSN网元消息类型 | 可选必选说明：该参数在"NODETYPE"配置为"GGSN"时为条件可选参数。<br>参数含义：该参数用于指定设置T3N3的GGSN网元的消息类型。<br>数据来源：全网规划<br>取值范围：<br>- UPD_PDP_CTX_REQ（Update PDP Context Request）<br>- DEL_PDP_CTX_REQ（Delete PDP Context Request）<br>- INT_PDP_CTX_REQ（Initiate PDP Context Activation Request）<br>- ALL（All Messages）<br>默认值：无<br>配置原则：无 |
| AMFMSGTYPE | AMF网元消息类型 | 可选必选说明：该参数在"NODETYPE"配置为"AMF"时为条件可选参数。<br>参数含义：该参数用于指定设置T3N3的AMF网元的消息类型。<br>数据来源：全网规划<br>取值范围：<br>- IDENTIF_REQ（Identification Request）<br>- CONTEXT_REQ（Context Request）<br>- CONTEXT_RSP（Context Response）<br>- FWDRELOCATE_REQ（Forward Relocation Request）<br>- FWRELO_COM_NOTF（Forward Relocation Complete Notification）<br>- RELOC_CANCL_REQ（Relocation Cancel Request）<br>- ALL（All Messages）<br>默认值：无<br>配置原则：无 |
| SPGWMSGTYPE | SPGW网元消息类型 | 可选必选说明：该参数在"NODETYPE"配置为"SPGW"时为条件可选参数。<br>参数含义：该参数用于指定设置T3N3的SPGW网元的消息类型。<br>数据来源：全网规划<br>取值范围：<br>- CRT_BEARER_REQ（Create Bearer Request）<br>- UPD_BEARER_REQ（Update Bearer Request）<br>- DWLNK_DATA_NOTF（Downlink Data Notification）<br>- ALL（All Messages）<br>- DEL_BEARER_REQ（Delete Bearer Request）<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [GTP-C T3N3参数（GTPCT3N3）](configobject/UNC/20.15.2/GTPCT3N3.md)

## 使用实例

- 查询网元类型为SGW的Create Session Request消息的T3、N3值：LST GTPCT3N3: NODETYPE=SGW,SGWMSGTYPE=CRT_SESSION_REQ;
  ```
  %%LST GTPCT3N3: NODETYPE=SGW, SGWMSGTYPE=CRT_SESSION_REQ;%%
  RETCODE = 0  操作成功

  结果如下
  --------
              网元类型  =  SGW
       SGW网元消息类型  =  Create Session Request
  请求消息重发时间间隔  =  1
  请求消息最大发送次数  =  1
  (结果个数 = 1)

  ---    END
  ```
- 查询网元类型为SGW的所有消息的T3、N3值：LST GTPCT3N3: NODETYPE=SGW;
  ```
  %%LST GTPCT3N3: NODETYPE=SGW;%%
  RETCODE = 0  操作成功

  结果如下
  --------
  网元类型  SGW网元消息类型         请求消息重发时间间隔  请求消息最大发送次数  

  SGW       All Messages            3                     5                     
  SGW       Create Session Request  1                     1                     
  (结果个数 = 2)

  ---    END
  ```
- 查询配置的所有消息的T3、N3值：LST GTPCT3N3:;
  ```
  %%LST GTPCT3N3:;%%
  RETCODE = 0  操作成功

  结果如下
  --------
  网元类型  SGW网元消息类型         PGW网元消息类型  GGSN网元消息类型  AMF网元消息类型  请求消息重发时间间隔  请求消息最大发送次数  

  SGW       All Messages            All Messages     All Messages      All Messages     3                     5                     
  SGW       Create Session Request  All Messages     All Messages      All Messages     1                     1                     
  PGW       All Messages            All Messages     All Messages      All Messages     3                     5                     
  GGSN      All Messages            All Messages     All Messages      All Messages     3                     5                     
  AMF       All Messages            All Messages     All Messages      All Messages     3                     2                     
  (结果个数 = 5)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询GTP-C-T3N3参数（LST-GTPCT3N3）_09652994.md`
