---
id: UNC@20.15.2@MMLCommand@CHK SEGFILE
type: MMLCommand
name: CHK SEGFILE（检查导入号段配置文件合法性）
nf: UNC
version: 20.15.2
verb: CHK
object_keyword: SEGFILE
command_category: 调测类
applicable_nf:
- NRF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- 对端NF管理
- 号段配置管理
- 号段导入管理
status: active
---

# CHK SEGFILE（检查导入号段配置文件合法性）

## 功能

**适用NF：NRF**

该命令用于核查号段导入文件的数据合法性，建议核查成功后再加载号段文件，否则存在不合法数据时，加载号段文件会失败。

号段文件需要符合一定格式要求，详细请联系华为技术支持。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SEGPACKAGENAME | 号段文件名称 | 可选必选说明：必选参数<br>参数含义：该参数用于表示号段文件的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~64。<br>默认值：无<br>配置原则：无 |
| SEGTYPE | 号段类型 | 可选必选说明：必选参数<br>参数含义：该参数用于表示号段文件中支持的号段类型。其中ALL代表IMSI、MSISDN、IMSIRT和MSISDNRT。<br>数据来源：本端规划<br>取值范围：<br>- IMSI（IMSI）<br>- MSISDN（MSISDN）<br>- IMSIRT（IMSIRT）<br>- MSISDNRT（MSISDNRT）<br>- ALL（ALL）<br>默认值：无<br>配置原则：无 |
| NFTYPEIMSI | NF类型 | 可选必选说明：该参数在"SEGTYPE"配置为"IMSI"、"IMSIRT"时为条件必选参数。<br>参数含义：该参数用于表示IMSI、IMSIRT号段作用的NF类型，即哪些NF类型支持号段文件中给出的IMSI、IMSIRT号段信息。<br>数据来源：本端规划<br>取值范围：<br>- AUSF（AUSF）<br>- PCF（PCF）<br>- UDM（UDM）<br>- UDR（UDR）<br>- CHF（CHF）<br>- CUSTOM_OCS（CUSTOM_OCS）<br>- AUSFUDM（AUSFUDM）<br>- ALL（ALL）<br>默认值：无<br>配置原则：无 |
| NFTYPEMSISDN | NF类型 | 可选必选说明：该参数在"SEGTYPE"配置为"MSISDN"、"MSISDNRT"时为条件必选参数。<br>参数含义：该参数用于表示MSISDN、MSISDNRT号段作用的NF类型，即哪些NF类型支持号段文件中给出的MSISDN、MSISDNRT号段信息。<br>数据来源：本端规划<br>取值范围：<br>- PCF（PCF）<br>- UDM（UDM）<br>- UDR（UDR）<br>- CHF（CHF）<br>- CUSTOM_OCS（CUSTOM_OCS）<br>- ALL（ALL）<br>默认值：无<br>配置原则：无 |
| NFTYPEALL | NF类型 | 可选必选说明：该参数在"SEGTYPE"配置为"ALL"时为条件必选参数。<br>参数含义：该参数用于表示IMSI和MSISDN号段作用的NF类型，即哪些NF类型支持号段文件中给出的所有号段信息。<br>数据来源：本端规划<br>取值范围：<br>- AUSF（AUSF）<br>- PCF（PCF）<br>- UDM（UDM）<br>- UDR（UDR）<br>- CHF（CHF）<br>- CUSTOM_OCS（CUSTOM_OCS）<br>- AUSFUDM（AUSFUDM）<br>- ALL（ALL）<br>默认值：无<br>配置原则：无 |
| RECNUM | 错误信息条数 | 可选必选说明：可选参数<br>参数含义：该参数用于表示指定核查NF类型和号段类型对应导入文件的错误信息条数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~1000，单位是条。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [号段文件（SEGFILE）](configobject/UNC/20.15.2/SEGFILE.md)

## 使用实例

运营商导入号段文件segdata1591149233424568600.zip后在加载号段文件之前核查压缩包中ausf-imsi.dat文件及其数据文件合法性时，执行此命令。

```
%%CHK SEGFILE: SEGPACKAGENAME="segdata1591149233424568600.zip", SEGTYPE=IMSI, NFTYPEIMSI=AUSF, RECNUM=5;%%
RETCODE = 0  操作成功

结果如下
------------------------
号段文件名称                    号段类型  NF类型   核查结果

segdata1591149233424568600.zip  IMSI      ausf     download zip file err,please check file name is right   
(结果个数 = 1)
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/检查导入号段配置文件合法性（CHK-SEGFILE）_50738958.md`
