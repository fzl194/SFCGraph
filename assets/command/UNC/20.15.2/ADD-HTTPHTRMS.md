---
id: UNC@20.15.2@MMLCommand@ADD HTTPHTRMS
type: MMLCommand
name: ADD HTTPHTRMS（增加HTR流控安全边界配置）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: HTTPHTRMS
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- HTTP功能管理
- HTTP流控管理
- HTTP HTR流控管理
- HTTP HTR流控安全边界管理
status: active
---

# ADD HTTPHTRMS（增加HTR流控安全边界配置）

## 功能

该命令用于增加HTR流控安全边界配置。

## 注意事项

- 该命令执行后立即生效。

- 已经处于HTR过载状态的局向仍按照修改前安全边界值生效，解控后重新起控按照新增的安全边界值生效。

- 最多可输入64条记录。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| LOCALNFTYPE | PEERNFTYPE | MINTHD | MAXTHD |
| --- | --- | --- | --- |
| NFTypeAMF | NFTypeAUSF | 210 | 1500 |
| NFTypeAMF | NFTypeUDM | 210 | 1500 |
| NFTypeSMF | NFTypeUDM | 160 | 1200 |
| NFTypeSMF | NFTypePCF | 160 | 1200 |
| NFTypeCHF | NFTypeCUSTOM_OCS | 1000 | 3000 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LOCALNFTYPE | 本端网元类型 | 可选必选说明：必选参数<br>参数含义：该参数用于设置本端NF类型。<br>数据来源：本端规划<br>取值范围：<br>- “INVALID（INVALID）”：无效值<br>- “NFTypeNRF（NFTypeNRF）”：NF类型为NRF<br>- “NFTypeUDM（NFTypeUDM）”：NF类型为UDM<br>- “NFTypeAMF（NFTypeAMF）”：NF类型为AMF<br>- “NFTypeSMF（NFTypeSMF）”：NF类型为SMF<br>- “NFTypeAUSF（NFTypeAUSF）”：NF类型为AUSF<br>- “NFTypeNEF（NFTypeNEF）”：NF类型为NEF<br>- “NFTypePCF（NFTypePCF）”：NF类型为PCF<br>- “NFTypeSMSF（NFTypeSMSF）”：NF类型为SMSF<br>- “NFTypeNSSF（NFTypeNSSF）”：NF类型为NSSF<br>- “NFTypeUDR（NFTypeUDR）”：NF类型为UDR<br>- “NFTypeLMF（NFTypeLMF）”：NF类型为LMF<br>- “NFTypeGMLC（NFTypeGMLC）”：NF类型为GMLC<br>- “NFType5GEIR（NFType5GEIR）”：NF类型为5GEIR<br>- “NFTypeSEPP（NFTypeSEPP）”：NF类型为SEPP<br>- “NFTypeUPF（NFTypeUPF）”：NF类型为UPF<br>- “NFTypeN3IWF（NFTypeN3IWF）”：NF类型为N3IWF<br>- “NFTypeAF（NFTypeAF）”：NF类型为AF<br>- “NFTypeUDSF（NFTypeUDSF）”：NF类型为UDSF<br>- “NFTypeBSF（NFTypeBSF）”：NF类型为BSF<br>- “NFTypeCHF（NFTypeCHF）”：NF类型为CHF<br>- “NFTypeCUSTOM_OCS（NFTypeCUSTOM_OCS）”：NF类型为CUSTOM_OCS<br>- “NFTypeSCP（NFTypeSCP）”：NF类型为SCP<br>- “NFTypeNWDAF（NFTypeNWDAF）”：NF类型为NWDAF<br>- “NFTypePCSCF（NFTypePCSCF）”：NF类型为PCSCF<br>- “NFTypeCBCF（NFTypeCBCF）”：NF类型为CBCF<br>- “NFTypeDRA（NFTypeDRA）”：NF类型为DRA<br>- “NFTypeMB_SMF（NFTypeMB_SMF）”：NF类型为MB_SMF<br>- “NFTypeUDN（NFTypeUDN）”：NF类型为UDN<br>- “NFTypeSFC（NFTypeSFC）”：NF类型为SFC<br>- “NFTypeUCBC（NFTypeUCBC）”：NF类型为UCBC<br>- “NFTypeCBE（NFTypeCBE）”：NF类型为CBE<br>其中，INVALID为无效值，系统支持下发，但实际不生效。<br>默认值：无<br>配置原则：无 |
| PEERNFTYPE | 对端网元类型 | 可选必选说明：必选参数<br>参数含义：该参数用于设置对端NF类型。<br>数据来源：全网规划<br>取值范围：<br>- “INVALID（INVALID）”：无效值<br>- “NFTypeNRF（NFTypeNRF）”：NF类型为NRF<br>- “NFTypeUDM（NFTypeUDM）”：NF类型为UDM<br>- “NFTypeAMF（NFTypeAMF）”：NF类型为AMF<br>- “NFTypeSMF（NFTypeSMF）”：NF类型为SMF<br>- “NFTypeAUSF（NFTypeAUSF）”：NF类型为AUSF<br>- “NFTypeNEF（NFTypeNEF）”：NF类型为NEF<br>- “NFTypePCF（NFTypePCF）”：NF类型为PCF<br>- “NFTypeSMSF（NFTypeSMSF）”：NF类型为SMSF<br>- “NFTypeNSSF（NFTypeNSSF）”：NF类型为NSSF<br>- “NFTypeUDR（NFTypeUDR）”：NF类型为UDR<br>- “NFTypeLMF（NFTypeLMF）”：NF类型为LMF<br>- “NFTypeGMLC（NFTypeGMLC）”：NF类型为GMLC<br>- “NFType5GEIR（NFType5GEIR）”：NF类型为5GEIR<br>- “NFTypeSEPP（NFTypeSEPP）”：NF类型为SEPP<br>- “NFTypeUPF（NFTypeUPF）”：NF类型为UPF<br>- “NFTypeN3IWF（NFTypeN3IWF）”：NF类型为N3IWF<br>- “NFTypeAF（NFTypeAF）”：NF类型为AF<br>- “NFTypeUDSF（NFTypeUDSF）”：NF类型为UDSF<br>- “NFTypeBSF（NFTypeBSF）”：NF类型为BSF<br>- “NFTypeCHF（NFTypeCHF）”：NF类型为CHF<br>- “NFTypeCUSTOM_OCS（NFTypeCUSTOM_OCS）”：NF类型为CUSTOM_OCS<br>- “NFTypeSCP（NFTypeSCP）”：NF类型为SCP<br>- “NFTypeNWDAF（NFTypeNWDAF）”：NF类型为NWDAF<br>- “NFTypePCSCF（NFTypePCSCF）”：NF类型为PCSCF<br>- “NFTypeCBCF（NFTypeCBCF）”：NF类型为CBCF<br>- “NFTypeDRA（NFTypeDRA）”：NF类型为DRA<br>- “NFTypeMB_SMF（NFTypeMB_SMF）”：NF类型为MB_SMF<br>- “NFTypeUDN（NFTypeUDN）”：NF类型为UDN<br>- “NFTypeSFC（NFTypeSFC）”：NF类型为SFC<br>- “NFTypeUCBC（NFTypeUCBC）”：NF类型为UCBC<br>- “NFTypeCBE（NFTypeCBE）”：NF类型为CBE<br>其中，INVALID为无效值，系统支持下发，但实际不生效。<br>默认值：无<br>配置原则：无 |
| MINTHD | 最小流控速率(个/秒) | 可选必选说明：必选参数<br>参数含义：该参数用于设置单HTTP POD放通阈值动态调整的最小速率。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~4294967295，单位是个每秒。<br>默认值：无<br>配置原则：<br>配置为0时安全边界功能不生效。<br>建议根据HTTP Pod用户规格和期望最长上线时间来配置此参数，即“最小流控速率（个/秒）”为：单HTTP Pod用户规格 / 最长上线时长(秒)。例如：系统HTTP单虚机最大支持30万用户，需要在1800秒内接入所有用户，那么最小流控速率需要设置为：300000个 / 1800秒 ~= 160(个/秒)。 |
| MAXTHD | 最大流控速率(个/秒) | 可选必选说明：必选参数<br>参数含义：该参数用于设置单HTTP POD放通阈值动态调整的最大速率。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~4294967295，单位是个每秒。<br>默认值：无<br>配置原则：<br>配置为0时安全边界功能不生效。<br>该值不为0时需大于等于"最小流控速率"；当“最大流控速率”等于“最小流控速率”时，流控效果相当于固定速率流控功能。<br>建议根据HTTP Pod用户规格和期望最短上线时间来配置此参数，即“最大流控速率（个/秒）”为：单HTTP Pod用户规格 / 最短上线时长(秒)。例如：系统HTTP单虚机最大支持30万用户，需要在600秒内接入所有用户，那么最大流控速率需要设置为：300000个 / 600秒 = 500(个/秒)。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/HTTPHTRMS]] · HTR流控安全边界配置（HTTPHTRMS）

## 使用实例

配置本端网元类型为NFTypeAMF，对端网元类型为NFTypeUDM的HTR流控安全边界，最小流控速率为160（个/秒），最大流控速率为500（个/秒），可以用如下命令：

```
ADD HTTPHTRMS: LOCALNFTYPE=NFTypeAMF, PEERNFTYPE=NFTypeUDM, MINTHD=160, MAXTHD=500;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-HTTPHTRMS.md`
