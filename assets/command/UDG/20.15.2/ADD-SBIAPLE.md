---
id: UDG@20.15.2@MMLCommand@ADD SBIAPLE
type: MMLCommand
name: ADD SBIAPLE（增加服务化接口本端实体）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: SBIAPLE
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- HTTP功能管理
- SBI管理
- 服务化接口本端实体管理
status: active
---

# ADD SBIAPLE（增加服务化接口本端实体）

## 功能

该命令用于增加本端服务化接口接入点信息，即本端服务化接口实体，供基于服务化接口的业务使用。当本端NF需要和目的NF之间建立服务化连接时，需要添加本配置。

> **说明**
> - 该命令执行后立即生效。
>
> - 本端服务化接口实体（SBIAPLE）引用的HTTP本端实体组（HTTPLEGRP）内必须存在一个作为Server端的HTTP本端实体和一个作为Client端的HTTP本端实体。
> - 如果不配置对端NF信息（目的NF类型、目的NF服务、CHF的目的NF类型），则只能配置一个服务化接口实体。
> - 如果配置对端NF信息（目的NF类型、目的NF服务、CHF的目的NF类型），则针对同一对端NF，只能配置一个服务化接口实体。
>
> - 最多可输入128条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INDEX | 索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定服务化接口本端实体的索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~128。<br>默认值：无<br>配置原则：无 |
| HTTPLEGRPIDX | HTTP本端实体组标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定服务化接口引用的HTTP本端实体组的索引。依赖于<br>[**ADD HTTPLEGRP**](../../HTTP管理/HTTP本端实体组管理/增加HTTP本端实体组（ADD HTTPLEGRP）_29213277.md)<br>的“INDEX”参数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~64。<br>默认值：无<br>配置原则：无 |
| NFTYPE | 本端NF类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定本端服务化接口服务的NF类型。如果配置NF类型为AMF，则该服务化接口服务于AMF；如果配置NF类型为SMF，则该服务化接口服务于SMF。<br>数据来源：全网规划<br>取值范围：<br>- “INVALID（INVALID）”：无效值<br>- “NFTypeNRF（NFTypeNRF）”：NF类型为NRF<br>- “NFTypeUDM（NFTypeUDM）”：NF类型为UDM<br>- “NFTypeAMF（NFTypeAMF）”：NF类型为AMF<br>- “NFTypeSMF（NFTypeSMF）”：NF类型为SMF<br>- “NFTypeAUSF（NFTypeAUSF）”：NF类型为AUSF<br>- “NFTypeNEF（NFTypeNEF）”：NF类型为NEF<br>- “NFTypePCF（NFTypePCF）”：NF类型为PCF<br>- “NFTypeSMSF（NFTypeSMSF）”：NF类型为SMSF<br>- “NFTypeNSSF（NFTypeNSSF）”：NF类型为NSSF<br>- “NFTypeUDR（NFTypeUDR）”：NF类型为UDR<br>- “NFTypeLMF（NFTypeLMF）”：NF类型为LMF<br>- “NFTypeGMLC（NFTypeGMLC）”：NF类型为GMLC<br>- “NFType5GEIR（NFType5GEIR）”：NF类型为5GEIR<br>- “NFTypeSEPP（NFTypeSEPP）”：NF类型为SEPP<br>- “NFTypeUPF（NFTypeUPF）”：NF类型为UPF<br>- “NFTypeN3IWF（NFTypeN3IWF）”：NF类型为N3IWF<br>- “NFTypeAF（NFTypeAF）”：NF类型为AF<br>- “NFTypeUDSF（NFTypeUDSF）”：NF类型为UDSF<br>- “NFTypeBSF（NFTypeBSF）”：NF类型为BSF<br>- “NFTypeCHF（NFTypeCHF）”：NF类型为CHF<br>- “NFTypeCUSTOM_OCS（NFTypeCUSTOM_OCS）”：NF类型为OCS<br>- “NFTypeSCP（NFTypeSCP）”：NF类型为SCP<br>- “NFTypeMBSMF（NFTypeMB_SMF）”：NF类型为MB_SMF<br>- “NFTypeNWDAF（NFTypeNWDAF）”：NF类型为NWDAF<br>- “NFTypeUDN（NFTypeUDN）”：NF类型为UDN<br>- “NFTypeSFC（NFTypeSFC）”：NF类型为SFC<br>- “NFTypeUCBC（NFTypeUCBC）”：NF类型为UCBC<br>- “NFTypeCBE（NFTypeCBE）”：NF类型为CBE<br>其中，INVALID为无效值，系统支持下发，但实际不生效。<br>默认值：无<br>配置原则：无 |
| PEERNFTYPE | 目的NF类型 | 可选必选说明：该参数在"NFTYPE"配置为"NFTypeSMF"、"NFTypeSMSF"时为条件可选参数。<br>参数含义：该参数用于指定本端在客户端模式下，需要访问的目的NF的类型。<br>数据来源：全网规划<br>取值范围：仅支持配置目的NF为Nchf。<br>- “Nchf（NFTypeCHF）”：NF类型为CHF<br>默认值：无<br>配置原则：<br>当本端设备为SMF或SMSF时，如果SMF和SMSF需要访问CHF的计费服务，且需要给CHF独立规划服务化接口，则需要配置目的NF为Nchf。<br>该配置指定到目的NF，即到该目的NF的所有服务均使用相同的服务化接口。 在不确定到目的NF的各个服务是否需要独立规划服务化接口的情况下建议配置到该目的NF。 |
| CHFPEERNFTYPE | CHF的目的NF类型 | 可选必选说明：该参数在"NFTYPE"配置为"NFTypeCHF"时为条件可选参数。<br>参数含义：该参数用于指定本端CHF在客户端模式下，需要访问的目的NF的类型。<br>数据来源：本端规划<br>取值范围：仅支持配置目的NF为Nnrf和Nocs<br>- “Nnrf（NFTypeNRF）”：NF类型为NRF<br>- “Nocs（NFTypeOCS）”：NF类型为OCS<br>默认值：无<br>配置原则：<br>当本端设备为CHF时，如果CHF需要访问NRF或OCS的服务，需要给NRF独立规划服务化接口，则需要配置目的NF为Nnrf，需要给OCS独立规划服务化接口，则需要配置目的NF为Nocs。如果需要给NRF和OCS规划共用一个HTTP本端实体组，则需要配置目的NF为Nnrf和目的NF为Nocs两个服务化接口，并指定使用同一个HTTP本端实体组标识。 |
| PEERSERVICE | 目的NF服务 | 可选必选说明：该参数在"PEERNFTYPE"配置为"Nchf"时为条件可选参数。<br>参数含义：该参数用于指定当本端为客户端模式时，需要访问的NF的具体服务。<br>数据来源：全网规划<br>取值范围：仅支持配置目的NF服务为Nchf_ConvCharg服务。<br>- “Nchf_ConvCharg（Nchf_ConvergedCharging）”：CHF提供的Nchf_ConvergedCharging服务<br>默认值：无<br>配置原则：<br>当本端设备为SMF或SMSF时，如果SMF和SMSF需要访问CHF的计费服务， 且需要给CHF提供的计费服务独立规划服务化接口，则需要配置目的NF服务为Nchf_ConvCharg。<br>该配置指定目的NF的服务，即该服务需要独立使用服务化接口。<br>只有在明确该服务需要独立规划服务化接口的情况下才能配置到该服务，未明确规划的建议配置到目的NF即可。 |
| DESCRIPTION | 描述 | 可选必选说明：可选参数<br>参数含义：该参数用于配置服务化接口本端实体的描述信息。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：无 |
| CHFPEERNFINSTID | CHF的目的NF实例ID | 可选必选说明：该参数在"CHFPEERNFTYPE"配置为"Nocs"时为条件可选参数。<br>参数含义：该参数用于当本端CHF在客户端模式下，指定目的NF的实例ID。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：<br>当本端设备为CHF，如果需要给不同的对端实例规划不同的服务化接口时，则需要配置目的NF实例ID。如果需要给多个对端实例规划共用一个HTTP本端实体组，则需要根据目的NF实例ID配置多个服务化接口，并指定使用同一个HTTP本端实体组标识。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@SBIAPLE]] · 服务化接口本端实体（SBIAPLE）

## 使用实例

- 若运营商想增加一个服务化接口本端实体，其索引是1，引用的HTTP本端实体组索引为1，NF类型为NFTypeNRF，描述信息为 “nrf”，可以执行如下命令：
  ```
  ADD SBIAPLE: INDEX=1, HTTPLEGRPIDX=1, NFTYPE=NFTypeNRF, DESCRIPTION="nrf";
  ```
- 若运营商想独立规划本端为SMF时到目的CHF的服务化接口本端实体，其索引是2，引用的HTTP本端实体组索引为2，NF类型为NFTypeSMF，目的NF类型为Nchf，可执行如下命令：
  ```
  ADD SBIAPLE: INDEX=2, HTTPLEGRPIDX=2,  NFTYPE=NFTypeSMF, PEERNFTYPE=Nchf;
  ```
- 若运营商想独立规划本端为SMF时到目的Nchf_ConvCharg服务的服务化接口本端实体，其索引是3，引用的HTTP本端实体组索引为3，NF类型为NFTypeSMF，目的NF类型为Nchf，目的NF服务为Nchf_ConvCharg，可执行如下命令：
  ```
  ADD SBIAPLE: INDEX=3, HTTPLEGRPIDX=2, NFTYPE=NFTypeSMF, PEERNFTYPE=Nchf, PEERSERVICE=Nchf_ConvCharg;
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/ADD-SBIAPLE.md`
