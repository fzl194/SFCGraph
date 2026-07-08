---
id: UNC@20.15.2@MMLCommand@LST HTTPFCMSG
type: MMLCommand
name: LST HTTPFCMSG（查询HTTP流控消息类型）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: HTTPFCMSG
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- HTTP功能管理
- HTTP流控管理
- HTTP流控消息管理
status: active
---

# LST HTTPFCMSG（查询HTTP流控消息类型）

## 功能

该命令用于查询HTTP流控消息类型。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFTYPE | 网元类型 | 可选必选说明：可选参数<br>参数含义：本参数用于指定NF类型。<br>数据来源：本端规划<br>取值范围：<br>- “INVALID（INVALID）”：无效值<br>- “NFTypeNRF（NFTypeNRF）”：NF类型为NRF<br>- “NFTypeUDM（NFTypeUDM）”：NF类型为UDM<br>- “NFTypeAMF（NFTypeAMF）”：NF类型为AMF<br>- “NFTypeSMF（NFTypeSMF）”：NF类型为SMF<br>- “NFTypeAUSF（NFTypeAUSF）”：NF类型为AUSF<br>- “NFTypeNEF（NFTypeNEF）”：NF类型为NEF<br>- “NFTypePCF（NFTypePCF）”：NF类型为PCF<br>- “NFTypeSMSF（NFTypeSMSF）”：NF类型为SMSF<br>- “NFTypeNSSF（NFTypeNSSF）”：NF类型为NSSF<br>- “NFTypeUDR（NFTypeUDR）”：NF类型为UDR<br>- “NFTypeLMF（NFTypeLMF）”：NF类型为LMF<br>- “NFTypeGMLC（NFTypeGMLC）”：NF类型为GMLC<br>- “NFType5GEIR（NFType5GEIR）”：NF类型为5GEIR<br>- “NFTypeSEPP（NFTypeSEPP）”：NF类型为SEPP<br>- “NFTypeUPF（NFTypeUPF）”：NF类型为UPF<br>- “NFTypeN3IWF（NFTypeN3IWF）”：NF类型为N3IWF<br>- “NFTypeAF（NFTypeAF）”：NF类型为AF<br>- “NFTypeUDSF（NFTypeUDSF）”：NF类型为UDSF<br>- “NFTypeBSF（NFTypeBSF）”：NF类型为BSF<br>- “NFTypeCHF（NFTypeCHF）”：NF类型为CHF<br>- “NFTypeCUSTOM_OCS（NFTypeCUSTOM_OCS）”：NF类型为CUSTOM_OCS<br>- “NFTypeSCP（NFTypeSCP）”：NF类型为SCP<br>- “NFTypeNWDAF（NFTypeNWDAF）”：NF类型为NWDAF<br>- “NFTypePCSCF（NFTypePCSCF）”：NF类型为PCSCF<br>- “NFTypeCBCF（NFTypeCBCF）”：NF类型为CBCF<br>- “NFTypeDRA（NFTypeDRA）”：NF类型为DRA<br>- “NFTypeMB_SMF（NFTypeMB_SMF）”：NF类型为MB_SMF<br>- “NFTypeUDN（NFTypeUDN）”：NF类型为UDN<br>- “NFTypeSFC（NFTypeSFC）”：NF类型为SFC<br>- “NFTypeUCBC（NFTypeUCBC）”：NF类型为UCBC<br>- “NFTypeCBE（NFTypeCBE）”：NF类型为CBE<br>其中，INVALID为无效值，系统支持下发，但实际不生效。<br>默认值：无<br>配置原则：无 |
| SBIPROTOCOL | SBI协议类型 | 可选必选说明：可选参数<br>参数含义：本参数用于指定SBI协议类型。<br>数据来源：本端规划<br>取值范围：<br>- “SBIProtocol29571（SBIProtocol29571）”：SBI协议为29571<br>- “SBIProtocolSMF29502（SBIProtocolSMF29502）”：SBI协议为SMF29502<br>- “SBIProtocolUDM29503（SBIProtocolUDM29503 ）”：SBI协议为UDM29503<br>- “SBIProtocolUDR29505（SBIProtocolUDR29505）”：SBI协议为UDR29505<br>- “SBIProtocolPCF29507（SBIProtocolPCF29507）”：SBI协议为PCF29507<br>- “SBIProtocolAUSF29509（SBIProtocolAUSF29509）”：SBI协议为AUSF29509<br>- “SBIProtocolNRF29510（SBIProtocolNRF29510）”：SBI协议为NRF29510<br>- “SBIProtocol5GEIR29511（SBIProtocol5GEIR29511）”：SBI协议为5GEIR29511<br>- “SBIProtocolPCF29512（SBIProtocolPCF29512）”：SBI协议为PCF29512<br>- “SBIProtocolPCF29514（SBIProtocolPCF29514）”：SBI协议为PCF29514<br>- “SBIProtocolAMF29518（SBIProtocolAMF29518）”：SBI协议为AMF29518<br>- “SBIProtocolUDR29519（SBIProtocolUDR29519）”：SBI协议为UDR29519<br>- “SBIProtocolBSF29521（SBIProtocolBSF29521）”：SBI协议为BSF29521<br>- “SBIProtocolNSSF29531（SBIProtocolNSSF29531）”：SBI协议为NSSF29531<br>- “SBIProtocolLMF29572（SBIProtocolLMF29572）”：SBI协议为LMF29572<br>- “SBIProtocolCHF32291（SBIProtocolCHF32291）”：SBI协议为CHF32291<br>- “SBIProtocolSMF29508（SBIProtocolSMF29508）”：SBI协议为SMF29508<br>- “SBIProtocolNWDAF29520（SBIProtocolNWDAF29520）”：SBI协议为NWDAF29520<br>- “SBIProtocolPCF29525（SBIProtocolPCF29525）”：SBI协议为PCF29525<br>- “SBIProtocolMEC20001（SBIProtocolMEC20001）”：SBI协议为MEC20001<br>- “SBIProtocolSMSF29540（SBIProtocolSMSF29540）”：SBI协议为SMSF29540<br>- “SBIProtocolGMLC29515（SBIProtocolGMLC29515）”：SBI协议为GMLC29515<br>- “SBIProtocolNEF29122（SBIProtocolNEF29122）”：SBI协议为NEF29122<br>- “SBIProtocolMBSMF29532（SBIProtocolMBSMF29532）”：SBI协议为MBSMF29532<br>- “SBIProtocolNEF29551（SBIProtocolNEF29551）”：SBI协议为NEF29551<br>- “SBIProtocolNEF29522（SBIProtocolNEF29522）”：SBI协议为NEF29522<br>- “SBIProtocolUPF29564（SBIProtocolUPF29564）”：SBI协议为UPF29564<br>- “SBIProtocolUDN10000（SBIProtocolUDN10000）”：SBI协议为UDN10000<br>- “SBIProtocolNEF29541（SBIProtocolNEF29541）”：SBI协议为NEF29541<br>- “SBIProtocolBSF10500（SBIProtocolBSF10500）”：SBI协议为BSF10500<br>- “SBIProtocolSFC20005（SBIProtocolSFC20005）”：SBI协议为SFC20005<br>- “SBIProtocolCBCF10000（SBIProtocolCBCF10000）”：SBI协议为CBCF10000<br>默认值：无<br>配置原则：无 |
| MSGINDEX | 消息索引 | 可选必选说明：可选参数<br>参数含义：本参数用于指定消息索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~4294967295。<br>默认值：无<br>配置原则：<br>由于此命令配置后影响较大，流控消息索引的配置规则请联系华为技术支持。 |
| FCTYPE | 流控类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定流控类型。<br>数据来源：全网规划<br>取值范围：<br>- “FIXSPDFCGRP（基于流控组固定速率流控）”：基于流控组固定速率流控<br>- “FIXBWFCGLB（全局固定带宽流控）”：全局固定带宽流控<br>- “SELFFC（自保流控）”：自保流控<br>- “PBUF（PBUF流控）”：PBUF流控<br>- “MEMORY（内存流控）”：内存流控<br>- “FIXSPDFCINTF（基于接口类型固定速率流控）”：基于接口类型固定速率流控<br>- “TCPBPFC（TCP反压流控）”：TCP反压流控<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@HTTPFCMSG]] · HTTP流控消息类型（HTTPFCMSG）

## 使用实例

例如查询AMF网元的所有流控消息

```
%%LST HTTPFCMSG: NFTYPE=NFTypeAMF;%%
RETCODE = 0  操作成功

结果如下
------------------------
        网元类型  =  NFTypeAMF
     SBI协议类型  =  SBIProtocolAMF29518
        消息索引  =  1
            角色  =  客户端
            方向  =  发送
        流控类型  =  PBUF流控
        流控开关  =  打开
      IP地址索引  =  0
          流控组  =  0
      流控优先级  =  0
        局向索引  =  0

(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-HTTPFCMSG.md`
