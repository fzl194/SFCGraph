---
id: UNC@20.15.2@MMLCommand@LST GTPCCMPT
type: MMLCommand
name: LST GTPCCMPT（查询GTP-C V0/V1协议兼容性配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: GTPCCMPT
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
- GTP-C V0 V1协议兼容性
status: active
---

# LST GTPCCMPT（查询GTP-C V0/V1协议兼容性配置）

## 功能

**适用网元：SGSN、MME**

此命令用于查询GTP-C V0/V1协议兼容性配置。

## 注意事项

此命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MSGCLS | 消息分类 | 可选必选说明：可选参数<br>参数含义：该参数用于指示消息分类。<br>取值范围：<br>- “PM(路径管理)”<br>- “TM(隧道管理)”<br>- “MM(移动管理)”<br>默认值：无<br>说明：暂时不支持<br>“PM(路径管理)”<br>的消息类别。 |
| MMMSGTYPE | 消息类型 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指示消息分类为移动管理时的消息类型。<br>前提条件：当<br>“MSGCLS”<br>取值为<br>“MM(移动管理)”<br>时，该参数有效。<br>取值范围：<br>- “SGSN_CONTEXT_RESP(SGSN Context Response)”<br>- “FWD_RLC_REQ(Forward Relocation Request)”<br>- “FORWARD_SRNS_CONTEXT(Forward Srns Context)”<br>默认值：无 |
| TMMSGTYPE | 消息类型 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指示消息分类为隧道管理时的消息类型。<br>前提条件：当<br>“MSGCLS”<br>取值为<br>“TM(隧道管理)”<br>时，该参数有效。<br>取值范围：<br>- “CREATE_PDP_CONTEXT_REQUEST(Create PDP Context Request)”<br>- “UPDATE_PDP_CONTEXT_REQUEST(Update PDP Context Request)”<br>- “UPDATE_PDP_CONTEXT_RESPONSE(Update PDP Context Response)”<br>- “DELETE_PDP_CONTEXT_RESPONSE(Delete PDP Context Response)”<br>- “DELETE_PDP_CONTEXT_REQUEST(Delete PDP Context Request)”<br>默认值：无 |
| CTXRSP | SGSN Context Response的信元类型 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指示消息类型为SGSN Context Response时的信元类型。<br>前提条件：当<br>“MMMSGTYPE”<br>取值为<br>“SGSN_CONTEXT_RESP(SGSN Context Response)”<br>时，该参数有效。<br>取值范围：<br>- “RAB_CONTEXT(RAB Context)”<br>- “CHR_CHARACTER(Charging Characteristics)”<br>- “IMEISV(IMEISV)”<br>- “PDP_CONTEXT(PDP Context)”<br>- “PDP_CONTEXT_PRIORITIZATION(PDP Context Prioritization)”<br>- “EVOL_ALLOC_RET_PRIORITY_II(Evolved Allocation/Retention Priority II)”<br>- “CO_LOC_GGSN_PGW_FQDN(Co-located GGSN-PGW FQDN)”<br>- “IMSI(IMSI)”<br>默认值：无 |
| FWDRLCREQ | Forward Relocation Request的信元类型 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指示消息类型为Forward Relocation Request时的信元类型。<br>前提条件：当<br>“MMMSGTYPE”<br>取值为<br>“FWD_RLC_REQ(Forward Relocation Request)”<br>时，该参数有效。<br>取值范围：<br>- “CHR_CHARACTER(Charging Characteristics)”<br>- “IMEISV(IMEISV)”<br>- “PDP_CONTEXT(PDP Context)”<br>- “PDP_CONTEXT_PRIORITIZATION(PDP Context Prioritization)”<br>- “SELECTED_PLMN_ID(Selected PLMN ID)”：控制LTE到UMTS的系统切换流程，Forward Relocation Request消息是否携带Selected PLMN字段。<br>- “EVOL_ALLOC_RET_PRIORITY_II(Evolved Allocation/Retention Priority II)”<br>- “CO_LOC_GGSN_PGW_FQDN(Co-located GGSN-PGW FQDN)”<br>- “UE_NETWORK_CAPABILITY(UE Network Capability)”<br>- “SRVCCMMCTXT(Additional MM context for SRVCC)”<br>- “SRVCCFLG(Additional flags for SRVCC)”<br>- “STN-SR(Session Transfer Number for SRVCC)”<br>- “C-MSISDN(Correlation MSISDN)”<br>- “EXTENDED_RANAP_CAUSE(Extended RANAP Cause)”<br>- “ENODEB_ID(eNodeB ID)”<br>默认值：无 |
| FWDSRNSCTX | Forward Srns Context的信元类型 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指示消息类型为Forward Srns Context时的信元类型。<br>前提条件：当<br>“MMMSGTYPE”<br>取值为<br>“FORWARD_SRNS_CONTEXT(Forward Srns Context)”<br>时，该参数有效。<br>取值范围：<br>“SOURCE_RNC_PDCP_CONTEXT(Source RNC PDCP Context)”<br>默认值：无 |
| CRTPDPREQ | Create PDP Context Request信元类型 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指示消息类型为Create PDP Context Request时的信元类型。<br>前提条件：当<br>“TMMSGTYPE”<br>取值为<br>“CREATE_PDP_CONTEXT_REQUEST(Create PDP Context Request)”<br>时，该参数有效。<br>取值范围：<br>“COMMON_FLAGS(Common Flags)”<br>默认值：无 |
| UPDPDPREQ | Update PDP Context Request信元类型 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指示消息类型为Update PDP Context Request时的信元类型。<br>前提条件：当<br>“TMMSGTYPE”<br>取值为<br>“UPDATE_PDP_CONTEXT_REQUEST(Update PDP Context Request)”<br>时，该参数有效。<br>取值范围：<br>“COMMON_FLAGS(Common Flags)”<br>默认值：无 |
| UPDPDPRES | Update PDP Context Response信元类型 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指示消息类型为Update PDP Context Response时的信元类型。<br>前提条件：当<br>“TMMSGTYPE”<br>取值为<br>“UPDATE_PDP_CONTEXT_RESPONSE(Update PDP Context Response)”<br>时，该参数有效。<br>数据来源：整网规划<br>取值范围：<br>- ULI(User Location Information)<br>- TZ(MS Time Zone)<br>默认值：无 |
| DELPDPRES | Delete PDP Context Response信元类型 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指示消息类型为Delete PDP Context Response时的信元类型。<br>前提条件：当<br>“TMMSGTYPE”<br>取值为<br>“DELETE_PDP_CONTEXT_RESPONSE(Delete PDP Context Response)”<br>时，该参数有效。<br>数据来源：整网规划<br>取值范围：<br>- ULI(User Location Information)<br>- TZ(MS Time Zone)<br>默认值：无 |
| DELPDPREQ | Delete PDP Context Request信元类型 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指示消息类型为Delete PDP Context Request时的信元类型。<br>前提条件：当<br>“TMMSGTYPE”<br>取值为<br>“DELETE_PDP_CONTEXT_REQUEST(Delete PDP Context Request)”<br>时，该参数有效。<br>数据来源：整网规划<br>取值范围：<br>- TZ(MS Time Zone)<br>默认值：无 |

## 操作的配置对象

- [GTP-C V0/V1协议兼容性配置（GTPCCMPT）](configobject/UNC/20.15.2/GTPCCMPT.md)

## 使用实例

查询GTP-C V0/V1协议兼容性配置：

LST GTPCCMPT:;

```
%%LST GTPCCMPT:;%%
RETCODE = 0  操作成功。

操作结果如下
------------
                    索引  =  0
                消息分类  =  移动管理
                消息类型  =  SGSN Context Response
                信元类型  =  PDP Context
                携带方式  =  NULL
             APNOI大小写  =  SGSN小写
是否支持Common Flags信元  =  NULL 
           UP功能选择指示 = NULL
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询GTP-C-V0_V1协议兼容性配置(LST-GTPCCMPT)_26145924.md`
