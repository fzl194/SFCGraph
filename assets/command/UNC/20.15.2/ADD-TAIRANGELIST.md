---
id: UNC@20.15.2@MMLCommand@ADD TAIRANGELIST
type: MMLCommand
name: ADD TAIRANGELIST（增加NF TAI区域信息）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: TAIRANGELIST
command_category: 配置类
applicable_nf:
- AMF
- SMF
- NRF
- NSSF
- SMSF
- NCG
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 服务化接口管理
- 注册与服务发现
- NF TAI区域信息管理
status: active
---

# ADD TAIRANGELIST（增加NF TAI区域信息）

## 功能

**适用NF：AMF、SMF、NRF、NSSF、SMSF、NCG**

该命令用于添加NF实例支持的TAI信息。

- 当NF实例只支持为某些TAI服务时，需要对支持的TAI进行配置。
- 当SMF向NRF注册时，如果BINDSMFINFOID不为空或者“null”，则必须在ADD SMFINFOEXT中配置ID与BINDSMFINFOID相同的记录，否则该命令将不生效。
- 当NWDAF向NRF注册时，如果BINDNWDAFINFOID不为空或者“null”，则必须在ADD NWDAFINFOEXT中配置ID与BINDNWDAFINFOID相同的记录，否则该命令将不生效。

## 注意事项

- 该命令执行后立即生效。

- 最多可输入2048条记录。
- 当NF类型为SMF时，TAC号段需要精确配置。如果配置成通用号段，如000000~FFFFFF，注册到NRF后，消费者NF带着TAI参数（此TAI在通用号段内，但是不在此SMF支持的号段内）到NRF进行服务发现时，此SMF也会被返回。这样可能会导致消费者NF选错SMF，业务流程达不到预期。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFINSTANCENAME | NF实例名称 | 可选必选说明：必选参数<br>参数含义：本参数用于指定NF实例名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~50。<br>默认值：无<br>配置原则：<br>本参数需要与ADD NFUUID命令中的NFINSTANCENAME值保持一致。 |
| NFTYPE | NF类型 | 可选必选说明：必选参数<br>参数含义：本参数用于指定NF类型。<br>数据来源：全网规划<br>取值范围：<br>- NfInvalid（NfInvalid）<br>- NfNRF（NfNRF）<br>- NfUDM（NfUDM）<br>- NfAMF（NfAMF）<br>- NfSMF（NfSMF）<br>- NfAUSF（NfAUSF）<br>- NfNEF（NfNEF）<br>- NfPCF（NfPCF）<br>- NfSMSF（NfSMSF）<br>- NfNSSF（NfNSSF）<br>- NfUDR（NfUDR）<br>- NfLMF（NfLMF）<br>- NfGMLC（NfGMLC）<br>- Nf5G_EIR（Nf5G_EIR）<br>- NfSEPP（NfSEPP）<br>- NfUPF（NfUPF）<br>- NfN3IWF（NfN3IWF）<br>- NfAF（NfAF）<br>- NfUDSF（NfUDSF）<br>- NfBSF（NfBSF）<br>- NfCHF（NfCHF）<br>- NfNWDAF（NfNWDAF）<br>- “NfTypeMAX（NfTypeMAX）”：已废弃。<br>- NfMBSMF（NfMBSMF）<br>- NfCBCF（NfCBCF）<br>- NfSCF（NfSCF）<br>- NfSPF（NfSPF）<br>默认值：无<br>配置原则：无 |
| MCC | 移动国家代码 | 可选必选说明：必选参数<br>参数含义：本参数用于指定移动国家代码。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是3。<br>默认值：无<br>配置原则：<br>本参数由3个十进制数字组成。 |
| MNC | 移动网号 | 可选必选说明：必选参数<br>参数含义：本参数用于指定移动网号。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是2~3。<br>默认值：无<br>配置原则：<br>本参数由2~3个十进制数字组成。 |
| TACRANGEINDEX | TAC区域标识 | 可选必选说明：必选参数<br>参数含义：本参数用于指定TAC区域标识。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~2047。<br>默认值：无<br>配置原则：<br>本参数与ADD TACRANGE命令中的INDEX值一致时生效。 |
| BINDSMFINFOID | 绑定的SMFINFO ID | 可选必选说明：可选参数<br>参数含义：该参数用于指定绑定的SMFINFOEXT记录。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~32。该参数大小写不敏感。<br>默认值：无<br>配置原则：<br>BINDSMFINFOID需要与SMFINFOEXT中的SMFINFOID一致。 |
| BINDNWDAFINFOID | 绑定的NWDAFINFO ID | 可选必选说明：可选参数<br>参数含义：该参数用于指定绑定的NWDAFINFOEXT记录。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~32。该参数大小写不敏感。<br>默认值：无<br>配置原则：<br>BINDNWDAFINFOID需要与NWDAFINFOEXT中的ID一致。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/TAIRANGELIST]] · NF TAI区域信息（TAIRANGELIST）

## 使用实例

运营商A需要给NF实例名称为SMF_Instance_0，类型为NfSMF的NF实例增加MCC为460，MNC为01，TACRANGEINDEX为0的TAI区域。

```
ADD TAIRANGELIST: NFINSTANCENAME="SMF_Instance_0", NFTYPE=NfSMF, MCC="460", MNC="01", TACRANGEINDEX=0;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-TAIRANGELIST.md`
