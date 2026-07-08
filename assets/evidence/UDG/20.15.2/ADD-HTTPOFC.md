# 增加HTTP局向（ADD HTTPOFC）

- [命令功能](#ZH-CN_MMLREF_0000001535230482__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001535230482__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001535230482__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001535230482__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0000001535230482)

该命令用于增加HTTP局向。

局向是信令与外部设备交互的方向。例如本端AMF到对端SMF可以定义为一个局向。可通过两种方式标识一个局向：（1）对端IP，IP可以是单个IP也可以是一组IP；（2）对端网元类型。

> **说明**
> - 该命令执行后立即生效。
>
> - "PEERNFTYPE"为NFTypeSCP或NFTypeSEPP时不支持"NFITEM"设置基于接口类型HTR流控或基于接口类型固定速率流控。
> - IP组的地址配置为SCP或SEPP的IP，HTR流控功能不生效。
>
> - 最多可输入4096条记录。

#### [操作用户权限](#ZH-CN_MMLREF_0000001535230482)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001535230482)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| OFCIDX | 局向索引 | 可选必选说明：必选参数<br>参数含义：该参数用于设置局向索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~4095。<br>默认值：无<br>配置原则：无 |
| OFCTYPE | 局向类型 | 可选必选说明：必选参数<br>参数含义：该参数用于设置局向类型。<br>数据来源：本端规划<br>取值范围：<br>- “NFTYPE（基于网元类型）”：基于网元类型<br>- “IPGROUP（基于IP组）”：基于IP组<br>默认值：无<br>配置原则：<br>该参数不支持修改。 |
| PEERNFTYPE | 对端网元类型 | 可选必选说明：该参数在"OFCTYPE"配置为"NFTYPE"时为条件必选参数。<br>参数含义：该参数用于设置对端网元类型。<br>数据来源：全网规划<br>取值范围：<br>- “INVALID（INVALID）”：无效值<br>- “NFTypeNRF（NFTypeNRF）”：NF类型为NRF<br>- “NFTypeUDM（NFTypeUDM）”：NF类型为UDM<br>- “NFTypeAMF（NFTypeAMF）”：NF类型为AMF<br>- “NFTypeSMF（NFTypeSMF）”：NF类型为SMF<br>- “NFTypeAUSF（NFTypeAUSF）”：NF类型为AUSF<br>- “NFTypeNEF（NFTypeNEF）”：NF类型为NEF<br>- “NFTypePCF（NFTypePCF）”：NF类型为PCF<br>- “NFTypeSMSF（NFTypeSMSF）”：NF类型为SMSF<br>- “NFTypeNSSF（NFTypeNSSF）”：NF类型为NSSF<br>- “NFTypeUDR（NFTypeUDR）”：NF类型为UDR<br>- “NFTypeLMF（NFTypeLMF）”：NF类型为LMF<br>- “NFTypeGMLC（NFTypeGMLC）”：NF类型为GMLC<br>- “NFType5GEIR（NFType5GEIR）”：NF类型为5GEIR<br>- “NFTypeSEPP（NFTypeSEPP）”：NF类型为SEPP<br>- “NFTypeUPF（NFTypeUPF）”：NF类型为UPF<br>- “NFTypeN3IWF（NFTypeN3IWF）”：NF类型为N3IWF<br>- “NFTypeAF（NFTypeAF）”：NF类型为AF<br>- “NFTypeUDSF（NFTypeUDSF）”：NF类型为UDSF<br>- “NFTypeBSF（NFTypeBSF）”：NF类型为BSF<br>- “NFTypeCHF（NFTypeCHF）”：NF类型为CHF<br>- “NFTypeCUSTOM_OCS（NFTypeCUSTOM_OCS）”：NF类型为CUSTOM_OCS<br>- “NFTypeSCP（NFTypeSCP）”：NF类型为SCP<br>- “NFTypeNWDAF（NFTypeNWDAF）”：NF类型为NWDAF<br>- “NFTypePCSCF（NFTypePCSCF）”：NF类型为PCSCF<br>- “NFTypeCBCF（NFTypeCBCF）”：NF类型为CBCF<br>- “NFTypeDRA（NFTypeDRA）”：NF类型为DRA<br>- “NFTypeMB_SMF（NFTypeMB_SMF）”：NF类型为MB_SMF<br>- “NFTypeUDN（NFTypeUDN）”：NF类型为UDN<br>- “NFTypeSFC（NFTypeSFC）”：NF类型为SFC<br>- “NFTypeUCBC（NFTypeUCBC）”：NF类型为UCBC<br>- “NFTypeCBE（NFTypeCBE）”：NF类型为CBE<br>其中，INVALID为无效值，系统支持下发，但实际不生效。<br>默认值：无<br>配置原则：无 |
| IPGROUP | IP组 | 可选必选说明：该参数在"OFCTYPE"配置为"IPGROUP"时为条件必选参数。<br>参数含义：该参数用于指定局向IP组。该参数来源于<br>[**ADD HTTPFCIPGRP**](../../HTTP流控管理/HTTP流控组管理/增加HTTP流控组（ADD HTTPFCIPGRP）_29053323.md)<br>命令的“GROUP”参数，可通过<br>[**LST HTTPFCIPGRP**](../../HTTP流控管理/HTTP流控组管理/查询HTTP流控组（LST HTTPFCIPGRP）_83813632.md)<br>命令查询获取。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~4095。<br>默认值：无<br>配置原则：无 |
| NFITEM | 基于NFTYPE控制项 | 可选必选说明：该参数在"OFCTYPE"配置为"NFTYPE"时为条件必选参数。<br>参数含义：该参数用于设置局向类型为"NFTYPE"时流控类型。<br>数据来源：本端规划<br>取值范围：<br>- “HTRINTF（HTRINTF）”：基于接口类型HTR流控<br>- “FIXSPDFCINTF（FIXSPDFCINTF）”：基于接口类型固定速率流控<br>默认值：无<br>配置原则：<br>该参数支持单独勾选和全选，其中基于接口类型HTR流控和基于接口类型固定速率流控要生效，需要满足对应的生效条件。 |
| IPGRPITEM | 基于IP组控制项 | 可选必选说明：该参数在"OFCTYPE"配置为"IPGROUP"时为条件必选参数。<br>参数含义：该参数用于设置局向类型为"IPGROUP"时流控类型。<br>数据来源：本端规划<br>取值范围：<br>- “HTRIPGRP（HTRIPGRP）”：基于IP组HTR流控<br>默认值：无<br>配置原则：无 |
| LOCALNFTYPE | 本端网元类型 | 可选必选说明：可选参数<br>参数含义：该参数用于设置本端网元类型。<br>数据来源：本端规划<br>取值范围：<br>- “INVALID（INVALID）”：无效值<br>- “NFTypeNRF（NFTypeNRF）”：NF类型为NRF<br>- “NFTypeUDM（NFTypeUDM）”：NF类型为UDM<br>- “NFTypeAMF（NFTypeAMF）”：NF类型为AMF<br>- “NFTypeSMF（NFTypeSMF）”：NF类型为SMF<br>- “NFTypeAUSF（NFTypeAUSF）”：NF类型为AUSF<br>- “NFTypeNEF（NFTypeNEF）”：NF类型为NEF<br>- “NFTypePCF（NFTypePCF）”：NF类型为PCF<br>- “NFTypeSMSF（NFTypeSMSF）”：NF类型为SMSF<br>- “NFTypeNSSF（NFTypeNSSF）”：NF类型为NSSF<br>- “NFTypeUDR（NFTypeUDR）”：NF类型为UDR<br>- “NFTypeLMF（NFTypeLMF）”：NF类型为LMF<br>- “NFTypeGMLC（NFTypeGMLC）”：NF类型为GMLC<br>- “NFType5GEIR（NFType5GEIR）”：NF类型为5GEIR<br>- “NFTypeSEPP（NFTypeSEPP）”：NF类型为SEPP<br>- “NFTypeUPF（NFTypeUPF）”：NF类型为UPF<br>- “NFTypeN3IWF（NFTypeN3IWF）”：NF类型为N3IWF<br>- “NFTypeAF（NFTypeAF）”：NF类型为AF<br>- “NFTypeUDSF（NFTypeUDSF）”：NF类型为UDSF<br>- “NFTypeBSF（NFTypeBSF）”：NF类型为BSF<br>- “NFTypeCHF（NFTypeCHF）”：NF类型为CHF<br>- “NFTypeCUSTOM_OCS（NFTypeCUSTOM_OCS）”：NF类型为CUSTOM_OCS<br>- “NFTypeSCP（NFTypeSCP）”：NF类型为SCP<br>- “NFTypeNWDAF（NFTypeNWDAF）”：NF类型为NWDAF<br>- “NFTypePCSCF（NFTypePCSCF）”：NF类型为PCSCF<br>- “NFTypeCBCF（NFTypeCBCF）”：NF类型为CBCF<br>- “NFTypeDRA（NFTypeDRA）”：NF类型为DRA<br>- “NFTypeMB_SMF（NFTypeMB_SMF）”：NF类型为MB_SMF<br>- “NFTypeUDN（NFTypeUDN）”：NF类型为UDN<br>- “NFTypeSFC（NFTypeSFC）”：NF类型为SFC<br>- “NFTypeUCBC（NFTypeUCBC）”：NF类型为UCBC<br>- “NFTypeCBE（NFTypeCBE）”：NF类型为CBE<br>其中，INVALID为无效值，系统支持下发，但实际不生效。<br>默认值：无<br>配置原则：<br>本端存在多个NF共部署时，需要输入该参数分别设置到对端的局向；否则系统会把共部署的多个NF作为整体设置到对端的局向。 |
| OFCNAME | 局向名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置局向名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~31。<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0000001535230482)

- 增加接口类型的HTTP局向配置，可以用如下命令：
  ```
  ADD HTTPOFC: OFCIDX=1, OFCTYPE=NFTYPE, PEERNFTYPE=NFTypeSMF, NFITEM=HTRINTF-1&FIXSPDFCINTF-0, OFCNAME="N11";
  ```
- 增加IP组类型的HTTP局向配置，可以用如下命令：
  ```
  ADD HTTPOFC: OFCIDX=2, OFCTYPE=IPGROUP, IPGROUP=1, IPGRPITEM=HTRIPGRP-1, OFCNAME="AMF2SMFIPGRP";
  ```
