---
id: UNC@20.15.2@MMLCommand@EXP SEGFILE
type: MMLCommand
name: EXP SEGFILE（导出号段文件）
nf: UNC
version: 20.15.2
verb: EXP
object_keyword: SEGFILE
command_category: 动作类
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

# EXP SEGFILE（导出号段文件）

## 功能

**适用NF：NRF**

该命令用于将已经导入到NRF系统中的号段数据导出成二进制文件并打包成压缩文件，导出的文件通过“系统->文件传输->NRF号段导出文件”下载。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SEGTYPE | 号段类型 | 可选必选说明：必选参数<br>参数含义：该参数用于表示号段类型。<br>数据来源：本端规划<br>取值范围：<br>- IMSI（IMSI）<br>- MSISDN（MSISDN）<br>- IMSIRT（IMSIRT）<br>- MSISDNRT（MSISDNRT）<br>- ALL（ALL）<br>默认值：无<br>配置原则：无 |
| NFTYPEIMSI | NF类型 | 可选必选说明：该参数在"SEGTYPE"配置为"IMSI"、"IMSIRT"时为条件必选参数。<br>参数含义：该参数用于表示IMSI、IMSIRT号段作用的NF类型，即哪些NF类型支持号段文件中给出的IMSI、IMSIRT号段信息。<br>数据来源：本端规划<br>取值范围：<br>- AUSF（AUSF）<br>- PCF（PCF）<br>- UDM（UDM）<br>- UDR（UDR）<br>- CHF（CHF）<br>- CUSTOM_OCS（CUSTOM_OCS）<br>- AUSFUDM（AUSFUDM）<br>- ALL（ALL）<br>默认值：无<br>配置原则：无 |
| NFTYPEMSISDN | NF类型 | 可选必选说明：该参数在"SEGTYPE"配置为"MSISDN"、"MSISDNRT"时为条件必选参数。<br>参数含义：该参数用于表示MSISDN、MSISDNRT号段作用的NF类型，即哪些NF类型支持号段文件中给出的MSISDN、MSISDNRT号段信息。<br>数据来源：本端规划<br>取值范围：<br>- PCF（PCF）<br>- UDM（UDM）<br>- UDR（UDR）<br>- CHF（CHF）<br>- CUSTOM_OCS（CUSTOM_OCS）<br>- ALL（ALL）<br>默认值：无<br>配置原则：无 |
| NFTYPEALL | NF类型 | 可选必选说明：该参数在"SEGTYPE"配置为"ALL"时为条件必选参数。<br>参数含义：该参数用于表示所有类型的号段。<br>数据来源：本端规划<br>取值范围：<br>- AUSF（AUSF）<br>- PCF（PCF）<br>- UDM（UDM）<br>- UDR（UDR）<br>- CHF（CHF）<br>- CUSTOM_OCS（CUSTOM_OCS）<br>- AUSFUDM（AUSFUDM）<br>- ALL（ALL）<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SEGFILE]] · 号段文件（SEGFILE）

## 使用实例

导出号段类型为IMSI的号段文件：

```
EXP SEGFILE: SEGTYPE=IMSI, NFTYPEIMSI=AUSF;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/EXP-SEGFILE.md`
