---
id: UNC@20.15.2@MMLCommand@DEL SBILINKSET
type: MMLCommand
name: DEL SBILINKSET（删除服务化接口链路集）
nf: UNC
version: 20.15.2
verb: DEL
object_keyword: SBILINKSET
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- HTTP功能管理
- SBI管理
- 服务化接口链路集管理
status: active
---

# DEL SBILINKSET（删除服务化接口链路集）

## 功能

![](删除服务化接口链路集（DEL SBILINKSET）_83653654.assets/notice_3.0-zh-cn_2.png)

该命令用于删除SBI链路集，删除对应链路集后，可能会导致该链路集上业务受损。

该命令用于删除SBI链路集。

## 注意事项

- 该命令执行后立即生效。

- 该命令用于删除SBI链路集，删除对应链路集后，可能会导致该链路集上业务受损。该操作会清除所有被删除的链路集已上报的告警。
- 两个输入参数至少需要填写其中一个。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PEERNFTYPE | 对端NF类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定目的NF的类型。<br>数据来源：本端规划<br>取值范围：<br>- “INVALID（INVALID）”：无效值<br>- “NFTypeNRF（NFTypeNRF）”：NF类型为NRF<br>- “NFTypeUDM（NFTypeUDM）”：NF类型为UDM<br>- “NFTypeAMF（NFTypeAMF）”：NF类型为AMF<br>- “NFTypeSMF（NFTypeSMF）”：NF类型为SMF<br>- “NFTypeAUSF（NFTypeAUSF）”：NF类型为AUSF<br>- “NFTypeNEF（NFTypeNEF）”：NF类型为NEF<br>- “NFTypePCF（NFTypePCF）”：NF类型为PCF<br>- “NFTypeSMSF（NFTypeSMSF）”：NF类型为SMSF<br>- “NFTypeNSSF（NFTypeNSSF）”：NF类型为NSSF<br>- “NFTypeUDR（NFTypeUDR）”：NF类型为UDR<br>- “NFTypeLMF（NFTypeLMF）”：NF类型为LMF<br>- “NFTypeGMLC（NFTypeGMLC）”：NF类型为GMLC<br>- “NFType5GEIR（NFType5GEIR）”：NF类型为5GEIR<br>- “NFTypeSEPP（NFTypeSEPP）”：NF类型为SEPP<br>- “NFTypeUPF（NFTypeUPF）”：NF类型为UPF<br>- “NFTypeN3IWF（NFTypeN3IWF）”：NF类型为N3IWF<br>- “NFTypeAF（NFTypeAF）”：NF类型为AF<br>- “NFTypeUDSF（NFTypeUDSF）”：NF类型为UDSF<br>- “NFTypeBSF（NFTypeBSF）”：NF类型为BSF<br>- “NFTypeCHF（NFTypeCHF）”：NF类型为CHF<br>- “NFTypeCUSTOM_OCS（NFTypeCUSTOM_OCS）”：NF类型为OCS<br>- “NFTypeSCP（NFTypeSCP）”：NF类型为SCP<br>- “NFTypeMBSMF（NFTypeMB_SMF）”：NF类型为MB_SMF<br>- “NFTypeNWDAF（NFTypeNWDAF）”：NF类型为NWDAF<br>- “NFTypeUDN（NFTypeUDN）”：NF类型为UDN<br>- “NFTypeSFC（NFTypeSFC）”：NF类型为SFC<br>- “NFTypeUCBC（NFTypeUCBC）”：NF类型为UCBC<br>- “NFTypeCBE（NFTypeCBE）”：NF类型为CBE<br>其中，INVALID为无效值，系统支持下发，但实际不生效。<br>默认值：无<br>配置原则：<br>当NF类型为Callback或Location时，该参数设置为INVALID。 |
| LINKSETID | 链路集标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定需要删除的链路集标识。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~256。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SBILINKSET]] · 服务化接口链路集（SBILINKSET）

## 使用实例

若运营商想要删除NFTYPE为UDM的链路集，可以执行如下命令。

```
DEL SBILINKSET:PEERNFTYPE=NFTypeUDM;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DEL-SBILINKSET.md`
