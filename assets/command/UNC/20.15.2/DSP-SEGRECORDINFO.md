---
id: UNC@20.15.2@MMLCommand@DSP SEGRECORDINFO
type: MMLCommand
name: DSP SEGRECORDINFO（显示NRF已导入号段数据）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: SEGRECORDINFO
command_category: 查询类
applicable_nf:
- NRF
effect_mode: ''
is_dangerous: false
max_records: 1000
category_path:
- 业务服务管理
- NRF业务及策略管理
- 对端NF管理
- 号段配置管理
- 号段导入管理
status: active
---

# DSP SEGRECORDINFO（显示NRF已导入号段数据）

## 功能

**适用NF：NRF**

该命令用于查询所有导入号段数据的A、B表信息。

当需要通过号段配置文件方式刷新NF支持的号段信息时，可以通过此命令查看导入号段数据的信息。

## 注意事项

该命令支持查询的最大记录数为1000。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SEGTYPE | 号段类型 | 可选必选说明：必选参数<br>参数含义：该参数用于表示号段类型。其中ALL代表IMSI、MSISDN、IMSIRT、MSISDNRT。<br>数据来源：本端规划<br>取值范围：<br>- IMSI（IMSI）<br>- MSISDN（MSISDN）<br>- IMSIRT（IMSIRT）<br>- MSISDNRT（MSISDNRT）<br>- ALL（ALL）<br>默认值：无<br>配置原则：无 |
| NFTYPEIMSI | NF类型 | 可选必选说明：该参数在"SEGTYPE"配置为"IMSI"、"IMSIRT"时为条件必选参数。<br>参数含义：该参数用于表示IMSI、IMSIRT号段作用的NF类型，即哪些NF类型支持号段文件中给出的IMSI、IMSIRT号段信息。<br>数据来源：本端规划<br>取值范围：<br>- AUSF（AUSF）<br>- PCF（PCF）<br>- UDM（UDM）<br>- UDR（UDR）<br>- CHF（CHF）<br>- CUSTOM_OCS（CUSTOM_OCS）<br>- AUSFUDM（AUSFUDM）<br>- ALL（ALL）<br>默认值：无<br>配置原则：无 |
| NFTYPEMSISDN | NF类型 | 可选必选说明：该参数在"SEGTYPE"配置为"MSISDN"、"MSISDNRT"时为条件必选参数。<br>参数含义：该参数用于表示MSISDN、MSISDNRT号段作用的NF类型，即哪些NF类型支持号段文件中给出的MSISDN、MSISDNRT号段信息。<br>数据来源：本端规划<br>取值范围：<br>- PCF（PCF）<br>- UDM（UDM）<br>- UDR（UDR）<br>- CHF（CHF）<br>- CUSTOM_OCS（CUSTOM_OCS）<br>- ALL（ALL）<br>默认值：无<br>配置原则：无 |
| NFTYPEALL | NF类型 | 可选必选说明：该参数在"SEGTYPE"配置为"ALL"时为条件必选参数。<br>参数含义：该参数用于表示IMSI、MSISDN、IMSIRT和MSISDNRT号段作用的NF类型，即哪些NF类型支持号段文件中给出的所有号段信息。<br>数据来源：本端规划<br>取值范围：<br>- AUSF（AUSF）<br>- PCF（PCF）<br>- UDM（UDM）<br>- UDR（UDR）<br>- CHF（CHF）<br>- CUSTOM_OCS（CUSTOM_OCS）<br>- AUSFUDM（AUSFUDM）<br>- ALL（ALL）<br>默认值：无<br>配置原则：无 |
| TBLTYPE | 号段表类型 | 可选必选说明：必选参数<br>参数含义：该参数用于表示号段的号段表类型，用于区分主、备两个表。<br>数据来源：本端规划<br>取值范围：<br>- ATABLE（A表）<br>- BTABLE（B表）<br>默认值：无<br>配置原则：无 |
| SEGSTART | 号段起始字符串 | 可选必选说明：可选参数<br>参数含义：该参数用于表示号段起始字符串。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是5~15。十进制数字，号段的起始号码必须与结束号码长度保持一致，数值必须小于或等于结束号码的数值。<br>默认值：无<br>配置原则：无 |
| SEGEND | 号段结束字符串 | 可选必选说明：可选参数<br>参数含义：该参数用于表示号段结束字符串。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是5~15。十进制数字，号段的结束号码必须与起始号码长度保持一致，数值大于或等于起始号码的数值。<br>默认值：无<br>配置原则：无 |
| NFGROUPID1 | NF组标识1 | 可选必选说明：该参数在"NFTYPEALL"配置为"AUSF"、"PCF"、"UDM"、"UDR"、"CHF"、"CUSTOM_OCS"、"AUSFUDM"、"ALL"时为条件可选参数。该参数在"NFTYPEIMSI"配置为"AUSF"、"PCF"、"AUSFUDM"、"UDM"、"UDR"、"CHF"、"CUSTOM_OCS"、"ALL"时为条件可选参数。该参数在"NFTYPEMSISDN"配置为"PCF"、"UDM"、"UDR"、"CHF"、"CUSTOM_OCS"、"ALL"时为条件可选参数。<br>参数含义：该参数用于表示特定号段配置的NF组标识，可以通过LST NFGROUP进行查询。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~128。<br>默认值：无<br>配置原则：无 |
| NFGROUPID2 | NF组标识2 | 可选必选说明：该参数在"NFTYPEALL"配置为"AUSFUDM"、"ALL"时为条件可选参数。该参数在"NFTYPEIMSI"配置为"AUSFUDM"、"ALL"时为条件可选参数。<br>参数含义：该参数用于表示特定号段配置的NF组标识，可以通过LST NFGROUP进行查询。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~128。<br>默认值：无<br>配置原则：无 |
| RECNUM | 记录条数 | 可选必选说明：可选参数<br>参数含义：该参数用于表示指定NF类型和号段类型对应导入文件的返回记录条数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~1000，单位是条。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [NRF已导入号段数据（SEGRECORDINFO）](configobject/UNC/20.15.2/SEGRECORDINFO.md)

## 使用实例

查询NRF上已经通过号段导入的AUSF支持的IMSI信息的A表信息。

```
%%DSP SEGRECORDINFO: SEGTYPE=IMSI, NFTYPEIMSI=AUSF, TBLTYPE=BTABLE, RECNUM=5;%%
RETCODE = 0  操作成功

结果如下
------------------------
号段类型   NF类型   号段表类型  号段起始字符串     号段结束字符串    NF组标识1  NF组标识2  

IMSI       ausf     B表         861520320000000    861520379999999   ausf-03    NULL           
IMSI       ausf     B表         861520330000000    861520389999999   ausf-04    NULL           
IMSI       ausf     B表         861520300000000    861520359999999   ausf-01    NULL           
IMSI       ausf     B表         861520310000000    861520369999999   ausf-02    NULL           
(结果个数 = 4)
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示NRF已导入号段数据（DSP-SEGRECORDINFO）_50738959.md`
