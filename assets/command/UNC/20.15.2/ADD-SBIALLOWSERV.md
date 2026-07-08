---
id: UNC@20.15.2@MMLCommand@ADD SBIALLOWSERV
type: MMLCommand
name: ADD SBIALLOWSERV（增加基于服务的白名单）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: SBIALLOWSERV
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- HTTP功能管理
- 白名单管理
- 基于服务的白名单管理
status: active
---

# ADD SBIALLOWSERV（增加基于服务的白名单）

## 功能

该命令用于增加基于服务类型的白名单，当系统作为服务端时，添加到白名单的服务只允许白名单中指定的网元类型的对端访问。未添加到白名单的服务则允许所有对端访问。

## 注意事项

- 该命令执行后立即生效。

- 命令中的网元实例ID参数目前不生效。

- 最多可输入255条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INDEX | 索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定配置的白名单索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~255。<br>默认值：无<br>配置原则：无 |
| SERVICENAME | 服务名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定添加到白名单的服务。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：无 |
| NFTYPE | 网元类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定允许访问白名单中服务的对端网元类型。<br>数据来源：本端规划<br>取值范围：<br>- “INVALID（INVALID）”：无效值<br>- “NFTypeNRF（NFTypeNRF）”：NF类型为NRF<br>- “NFTypeUDM（NFTypeUDM）”：NF类型为UDM<br>- “NFTypeAMF（NFTypeAMF）”：NF类型为AMF<br>- “NFTypeSMF（NFTypeSMF）”：NF类型为SMF<br>- “NFTypeAUSF（NFTypeAUSF）”：NF类型为AUSF<br>- “NFTypeNEF（NFTypeNEF）”：NF类型为NEF<br>- “NFTypePCF（NFTypePCF）”：NF类型为PCF<br>- “NFTypeSMSF（NFTypeSMSF）”：NF类型为SMSF<br>- “NFTypeNSSF（NFTypeNSSF）”：NF类型为NSSF<br>- “NFTypeUDR（NFTypeUDR）”：NF类型为UDR<br>- “NFTypeLMF（NFTypeLMF）”：NF类型为LMF<br>- “NFTypeGMLC（NFTypeGMLC）”：NF类型为GMLC<br>- “NFType5GEIR（NFType5GEIR）”：NF类型为5GEIR<br>- “NFTypeSEPP（NFTypeSEPP）”：NF类型为SEPP<br>- “NFTypeUPF（NFTypeUPF）”：NF类型为UPF<br>- “NFTypeN3IWF（NFTypeN3IWF）”：NF类型为N3IWF<br>- “NFTypeAF（NFTypeAF）”：NF类型为AF<br>- “NFTypeUDSF（NFTypeUDSF）”：NF类型为UDSF<br>- “NFTypeBSF（NFTypeBSF）”：NF类型为BSF<br>- “NFTypeCHF（NFTypeCHF）”：NF类型为CHF<br>- “NFTypeCUSTOM_OCS（NFTypeCUSTOM_OCS）”：NF类型为CUSTOM_OCS<br>- “NFTypeSCP（NFTypeSCP）”：NF类型为SCP<br>- “NFTypeNWDAF（NFTypeNWDAF）”：NF类型为NWDAF<br>- “NFTypePCSCF（NFTypePCSCF）”：NF类型为PCSCF<br>- “NFTypeCBCF（NFTypeCBCF）”：NF类型为CBCF<br>- “NFTypeDRA（NFTypeDRA）”：NF类型为DRA<br>- “NFTypeMB_SMF（NFTypeMB_SMF）”：NF类型为MB_SMF<br>- “NFTypeUDN（NFTypeUDN）”：NF类型为UDN<br>- “NFTypeSFC（NFTypeSFC）”：NF类型为SFC<br>- “NFTypeUCBC（NFTypeUCBC）”：NF类型为UCBC<br>- “NFTypeCBE（NFTypeCBE）”：NF类型为CBE<br>其中，INVALID为无效值，系统支持下发，但实际不生效。<br>默认值：无<br>配置原则：无 |
| NFID | 网元实例ID | 可选必选说明：可选参数<br>参数含义：该参数用于指定允许访问白名单中服务的对端网元实例ID。目前本参数不生效。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SBIALLOWSERV]] · 基于服务的白名单（SBIALLOWSERV）

## 使用实例

若运营商想要指定只有nrf类型的网元可以访问“nnrf-nfm”服务，则执行如下命令。

```
ADD SBIALLOWSERV: INDEX=1, SERVICENAME="nnrf-nfm", NFTYPE=NFTypeNRF; 
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-SBIALLOWSERV.md`
