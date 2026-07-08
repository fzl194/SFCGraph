---
id: UDG@20.15.2@MMLCommand@ADD HTTPFCMSG
type: MMLCommand
name: ADD HTTPFCMSG（增加HTTP流控消息类型）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: HTTPFCMSG
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- HTTP功能管理
- HTTP流控管理
- HTTP流控消息管理
status: active
---

# ADD HTTPFCMSG（增加HTTP流控消息类型）

## 功能

![](增加HTTP流控消息类型（ADD HTTPFCMSG）_01544142.assets/notice_3.0-zh-cn.png)

新增流控消息需谨慎，建议只针对业务流程首消息开启流控，避免影响E2E业务成功率。

该命令用于增加HTTP流控消息类型。

> **说明**
> - 该命令执行后立即生效。
>
> - 参数FCTYPE取值为TCPBPFC时，执行该命令会导致TCP CPU反压流控暂时停止。
>
> - 最多可输入512条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFTYPE | 网元类型 | 可选必选说明：必选参数<br>参数含义：本参数用于指定NF类型。<br>数据来源：本端规划<br>取值范围：<br>- “INVALID（INVALID）”：无效值<br>- “NFTypeNRF（NFTypeNRF）”：NF类型为NRF<br>- “NFTypeUDM（NFTypeUDM）”：NF类型为UDM<br>- “NFTypeAMF（NFTypeAMF）”：NF类型为AMF<br>- “NFTypeSMF（NFTypeSMF）”：NF类型为SMF<br>- “NFTypeAUSF（NFTypeAUSF）”：NF类型为AUSF<br>- “NFTypeNEF（NFTypeNEF）”：NF类型为NEF<br>- “NFTypePCF（NFTypePCF）”：NF类型为PCF<br>- “NFTypeSMSF（NFTypeSMSF）”：NF类型为SMSF<br>- “NFTypeNSSF（NFTypeNSSF）”：NF类型为NSSF<br>- “NFTypeUDR（NFTypeUDR）”：NF类型为UDR<br>- “NFTypeLMF（NFTypeLMF）”：NF类型为LMF<br>- “NFTypeGMLC（NFTypeGMLC）”：NF类型为GMLC<br>- “NFType5GEIR（NFType5GEIR）”：NF类型为5GEIR<br>- “NFTypeSEPP（NFTypeSEPP）”：NF类型为SEPP<br>- “NFTypeUPF（NFTypeUPF）”：NF类型为UPF<br>- “NFTypeN3IWF（NFTypeN3IWF）”：NF类型为N3IWF<br>- “NFTypeAF（NFTypeAF）”：NF类型为AF<br>- “NFTypeUDSF（NFTypeUDSF）”：NF类型为UDSF<br>- “NFTypeBSF（NFTypeBSF）”：NF类型为BSF<br>- “NFTypeCHF（NFTypeCHF）”：NF类型为CHF<br>- “NFTypeCUSTOM_OCS（NFTypeCUSTOM_OCS）”：NF类型为CUSTOM_OCS<br>- “NFTypeSCP（NFTypeSCP）”：NF类型为SCP<br>- “NFTypeNWDAF（NFTypeNWDAF）”：NF类型为NWDAF<br>- “NFTypePCSCF（NFTypePCSCF）”：NF类型为PCSCF<br>- “NFTypeCBCF（NFTypeCBCF）”：NF类型为CBCF<br>- “NFTypeDRA（NFTypeDRA）”：NF类型为DRA<br>- “NFTypeMB_SMF（NFTypeMB_SMF）”：NF类型为MB_SMF<br>- “NFTypeUDN（NFTypeUDN）”：NF类型为UDN<br>- “NFTypeSFC（NFTypeSFC）”：NF类型为SFC<br>- “NFTypeUCBC（NFTypeUCBC）”：NF类型为UCBC<br>- “NFTypeCBE（NFTypeCBE）”：NF类型为CBE<br>其中，INVALID为无效值，系统支持下发，但实际不生效。<br>默认值：无<br>配置原则：无 |
| SBIPROTOCOL | SBI协议类型 | 可选必选说明：必选参数<br>参数含义：本参数用于指定SBI协议类型。<br>数据来源：本端规划<br>取值范围：<br>- “SBIProtocol29571（SBIProtocol29571）”：SBI协议为29571<br>- “SBIProtocolSMF29502（SBIProtocolSMF29502）”：SBI协议为SMF29502<br>- “SBIProtocolUDM29503（SBIProtocolUDM29503 ）”：SBI协议为UDM29503<br>- “SBIProtocolUDR29505（SBIProtocolUDR29505）”：SBI协议为UDR29505<br>- “SBIProtocolPCF29507（SBIProtocolPCF29507）”：SBI协议为PCF29507<br>- “SBIProtocolAUSF29509（SBIProtocolAUSF29509）”：SBI协议为AUSF29509<br>- “SBIProtocolNRF29510（SBIProtocolNRF29510）”：SBI协议为NRF29510<br>- “SBIProtocol5GEIR29511（SBIProtocol5GEIR29511）”：SBI协议为5GEIR29511<br>- “SBIProtocolPCF29512（SBIProtocolPCF29512）”：SBI协议为PCF29512<br>- “SBIProtocolPCF29514（SBIProtocolPCF29514）”：SBI协议为PCF29514<br>- “SBIProtocolAMF29518（SBIProtocolAMF29518）”：SBI协议为AMF29518<br>- “SBIProtocolUDR29519（SBIProtocolUDR29519）”：SBI协议为UDR29519<br>- “SBIProtocolBSF29521（SBIProtocolBSF29521）”：SBI协议为BSF29521<br>- “SBIProtocolNSSF29531（SBIProtocolNSSF29531）”：SBI协议为NSSF29531<br>- “SBIProtocolLMF29572（SBIProtocolLMF29572）”：SBI协议为LMF29572<br>- “SBIProtocolCHF32291（SBIProtocolCHF32291）”：SBI协议为CHF32291<br>- “SBIProtocolSMF29508（SBIProtocolSMF29508）”：SBI协议为SMF29508<br>- “SBIProtocolNWDAF29520（SBIProtocolNWDAF29520）”：SBI协议为NWDAF29520<br>- “SBIProtocolPCF29525（SBIProtocolPCF29525）”：SBI协议为PCF29525<br>- “SBIProtocolMEC20001（SBIProtocolMEC20001）”：SBI协议为MEC20001<br>- “SBIProtocolSMSF29540（SBIProtocolSMSF29540）”：SBI协议为SMSF29540<br>- “SBIProtocolGMLC29515（SBIProtocolGMLC29515）”：SBI协议为GMLC29515<br>- “SBIProtocolNEF29122（SBIProtocolNEF29122）”：SBI协议为NEF29122<br>- “SBIProtocolMBSMF29532（SBIProtocolMBSMF29532）”：SBI协议为MBSMF29532<br>- “SBIProtocolNEF29551（SBIProtocolNEF29551）”：SBI协议为NEF29551<br>- “SBIProtocolNEF29522（SBIProtocolNEF29522）”：SBI协议为NEF29522<br>- “SBIProtocolUPF29564（SBIProtocolUPF29564）”：SBI协议为UPF29564<br>- “SBIProtocolUDN10000（SBIProtocolUDN10000）”：SBI协议为UDN10000<br>- “SBIProtocolNEF29541（SBIProtocolNEF29541）”：SBI协议为NEF29541<br>- “SBIProtocolBSF10500（SBIProtocolBSF10500）”：SBI协议为BSF10500<br>- “SBIProtocolSFC20005（SBIProtocolSFC20005）”：SBI协议为SFC20005<br>- “SBIProtocolCBCF10000（SBIProtocolCBCF10000）”：SBI协议为CBCF10000<br>默认值：无<br>配置原则：无 |
| MSGINDEX | 消息索引 | 可选必选说明：必选参数<br>参数含义：本参数用于指定消息索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~4294967295。<br>默认值：无<br>配置原则：<br>由于此命令配置后影响较大，流控消息索引的配置规则请联系华为技术支持。 |
| ROLE | 角色 | 可选必选说明：必选参数<br>参数含义：该参数用于指定本端NF角色。<br>数据来源：全网规划<br>取值范围：<br>- “SERVER（服务端）”：服务端<br>- “CLIENT（客户端）”：客户端<br>默认值：无<br>配置原则：无 |
| DIRECTION | 方向 | 可选必选说明：必选参数<br>参数含义：该参数用于指定消息方向。<br>数据来源：全网规划<br>取值范围：<br>- “SEND（发送）”：发送方向<br>- “RECV（接收）”：接收方向<br>默认值：无<br>配置原则：无 |
| FCTYPE | 流控类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定流控类型。<br>数据来源：全网规划<br>取值范围：<br>- “FIXSPDFCGRP（基于流控组固定速率流控）”：基于流控组固定速率流控<br>- “FIXBWFCGLB（全局固定带宽流控）”：全局固定带宽流控<br>- “SELFFC（自保流控）”：自保流控<br>- “PBUF（PBUF流控）”：PBUF流控<br>- “MEMORY（内存流控）”：内存流控<br>- “FIXSPDFCINTF（基于接口类型固定速率流控）”：基于接口类型固定速率流控<br>- “TCPBPFC（TCP反压流控）”：TCP反压流控<br>默认值：无<br>配置原则：无 |
| FCSWITCH | 流控开关 | 可选必选说明：必选参数<br>参数含义：该参数用于控制流控功能是否开启。<br>数据来源：全网规划<br>取值范围：<br>- “ON（打开）”：打开<br>- “OFF（关闭）”：关闭<br>默认值：无<br>配置原则：无 |
| IPINDEX | IP地址索引 | 可选必选说明：该参数在"FCTYPE"配置为"FIXSPDFCGRP"时为条件可选参数。<br>参数含义：该参数用于标识具有相同前缀的一组IP地址。此参数无需配置，配置后也无实际意义。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~4095。<br>默认值：无<br>配置原则：无 |
| GROUP | 流控组 | 可选必选说明：该参数在"FCTYPE"配置为"FIXSPDFCGRP"时为条件可选参数。<br>参数含义：该参数用于指定HTTP固定速率流控组的唯一标识。该参数来源于<br>[**ADD HTTPFCIPGRP**](../HTTP流控组管理/增加HTTP流控组（ADD HTTPFCIPGRP）_29053323.md)<br>命令的“流控组”参数，可通过<br>[**LST HTTPFCIPGRP**](../HTTP流控组管理/查询HTTP流控组（LST HTTPFCIPGRP）_83813632.md)<br>命令查询获取。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~4095。<br>默认值：无<br>配置原则：<br>"FCSWITCH"配置为"ON"时，必须输入该参数，否则命令会执行失败。 |
| PRIORITY | 流控优先级 | 可选必选说明：该参数在"FCTYPE"配置为"SELFFC"时为条件可选参数。<br>参数含义：该参数用于指定自保流控消息优先级。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~5。<br>默认值：无<br>配置原则：<br>"FCSWITCH"配置为"ON"时，必须输入该参数，否则命令会执行失败。 |
| OFCIDX | 局向索引 | 可选必选说明：该参数在"FCTYPE"配置为"FIXSPDFCINTF"时为条件可选参数。<br>参数含义：该参数用于指定基于接口类型固定速率流控的局向索引。该参数来源于<br>[**ADD HTTPFIXEDFCINF**](../HTTP接口类型固定速率流控管理/增加HTTP接口类型固定速率流控信息（ADD HTTPFIXEDFCINF）_52121330.md)<br>命令的“局向索引”参数，可通过<br>[**LST HTTPFIXEDFCINF**](../HTTP接口类型固定速率流控管理/查询HTTP接口类型固定速率流控信息（LST HTTPFIXEDFCINF）_52121334.md)<br>命令查询获取。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~4095。<br>默认值：无<br>配置原则：<br>"FCSWITCH"配置为"ON"时，必须输入该参数，否则命令会执行失败。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@HTTPFCMSG]] · HTTP流控消息类型（HTTPFCMSG）

## 使用实例

例如当AMF作为Server端接收消息时，基于SBIProtocolAMF29518协议增加消息索引为1的固定速率流控，IP地址索引为1，流控组为1。

```
ADD HTTPFCMSG: NFTYPE=NFTypeAMF, SBIPROTOCOL=SBIProtocolAMF29518, MSGINDEX=1, ROLE=SERVER, DIRECTION=RECV, FCTYPE=FIXSPDFCGRP, FCSWITCH=ON, IPINDEX=1, GROUP=1;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/ADD-HTTPFCMSG.md`
