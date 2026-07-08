---
id: UNC@20.15.2@MMLCommand@DEL SEGDATA
type: MMLCommand
name: DEL SEGDATA（删除号段数据）
nf: UNC
version: 20.15.2
verb: DEL
object_keyword: SEGDATA
command_category: 配置类
applicable_nf:
- NRF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- 对端NF管理
- 号段配置管理
- 号段导入管理
status: active
---

# DEL SEGDATA（删除号段数据）

## 功能

**适用NF：NRF**

该命令用于删除某一NF支持的特定类型的备表中的号段数据，仅适用于号段文件的方式。

当运营商不想再使用规划好待使用的号段数据时，可以使用此命令删除规划数据。

## 注意事项

- 该命令执行后立即生效。

- 执行此命令不影响当前使用的主表中的数据，删除的内容仅为备表中规划待使用的数据。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SEGTYPE | 号段类型 | 可选必选说明：必选参数<br>参数含义：该参数用于表示号段类型。<br>数据来源：本端规划<br>取值范围：<br>- IMSI（IMSI）<br>- MSISDN（MSISDN）<br>- IMSIRT（IMSIRT）<br>- MSISDNRT（MSISDNRT）<br>- ALL（ALL）<br>默认值：无<br>配置原则：无 |
| NFTYPEIMSI | NF类型 | 可选必选说明：该参数在"SEGTYPE"配置为"IMSI"、"IMSIRT"时为条件必选参数。<br>参数含义：该参数用于表示IMSI、IMSIRT号段作用的NF类型，即哪些NF类型支持号段文件中给出的IMSI、IMSIRT号段信息。<br>数据来源：本端规划<br>取值范围：<br>- AUSF（AUSF）<br>- PCF（PCF）<br>- UDM（UDM）<br>- UDR（UDR）<br>- CHF（CHF）<br>- CUSTOM_OCS（CUSTOM_OCS）<br>- AUSFUDM（AUSFUDM）<br>- ALL（ALL）<br>默认值：无<br>配置原则：无 |
| NFTYPEMSISDN | NF类型 | 可选必选说明：该参数在"SEGTYPE"配置为"MSISDN"、"MSISDNRT"时为条件必选参数。<br>参数含义：该参数用于表示MSISDN、MSISDNRT号段作用的NF类型，即哪些NF类型支持号段文件中给出的MSISDN、MSISDNRT号段信息。<br>数据来源：本端规划<br>取值范围：<br>- PCF（PCF）<br>- UDM（UDM）<br>- UDR（UDR）<br>- CHF（CHF）<br>- CUSTOM_OCS（CUSTOM_OCS）<br>- ALL（ALL）<br>默认值：无<br>配置原则：无 |
| NFTYPEALL | NF类型 | 可选必选说明：该参数在"SEGTYPE"配置为"ALL"时为条件必选参数。<br>参数含义：该参数用于表示IMSI、MSISDN、IMSIRT和MSISDNRT号段作用的NF类型，即哪些NF类型支持号段文件中给出的所有号段信息。<br>数据来源：本端规划<br>取值范围：<br>- AUSF（AUSF）<br>- PCF（PCF）<br>- UDM（UDM）<br>- UDR（UDR）<br>- CHF（CHF）<br>- CUSTOM_OCS（CUSTOM_OCS）<br>- AUSFUDM（AUSFUDM）<br>- ALL（ALL）<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [号段数据（SEGDATA）](configobject/UNC/20.15.2/SEGDATA.md)

## 使用实例

运营商之前规划了UDM支持的IMSI号段信息，规划数据已加载未激活。运营商想重新规划UDM支持的号段信息，不再使用之前的规划数据，需要执行此命令删除之前规划的号段数据。

```
DEL SEGDATA: SEGTYPE=IMSI, NFTYPEIMSI=UDM;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除号段数据（DEL-SEGDATA）_09651798.md`
