---
id: UNC@20.15.2@MMLCommand@ADD ALLOWEDPLMN
type: MMLCommand
name: ADD ALLOWEDPLMN（增加NF或NF服务支持的PLMN）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: ALLOWEDPLMN
command_category: 配置类
applicable_nf:
- AMF
- SMF
- NRF
- NSSF
- NCG
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 服务化接口管理
- 注册与服务发现
- 服务支持的PLMN配置管理
status: active
---

# ADD ALLOWEDPLMN（增加NF或NF服务支持的PLMN）

## 功能

**适用NF：AMF、SMF、NRF、NSSF、NCG**

该命令用于添加NF实例或NF服务实例所支持的PLMN。当NF实例或NF服务实例只支持为某些PLMN服务时，需要对支持的PLMN进行配置。配置后，其他NF只能通过本NF支持的PLMN来访问本NF的服务实例。

如果仅配置某个NF实例支持的PLMN，表示该NF实例下的所有服务实例支持的PLMN相同。

## 注意事项

- 该命令执行后立即生效。

- 如果某个NF服务实例下没有配置支持的PLMN，表示该NF服务实例支持所有的PLMN。
- 如果NF实例或该NF下的所有服务实例均未配置支持的PLMN，则表示该NF支持所有的PLMN。

- 最多可输入4096条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INDEX | 索引标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定索引标识。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~4095。<br>默认值：无<br>配置原则：无 |
| REGTYPE | 注册类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定注册类型。<br>数据来源：全网规划<br>取值范围：<br>- RegInvalid（RegInvalid）<br>- RegNfProfile（RegNfProfile）<br>- RegService（RegService）<br>- RegMAX（RegMAX）<br>默认值：无<br>配置原则：<br>- 如果注册类型为REGINVALID(RegInvalid)，则配置无效。通常不需要配置。<br>- 如果注册类型为REGNFPROFILE(RegNfProfile)，表示配置NF实例支持的PLMN。<br>- 如果注册类型为REGSERVICE(RegService) ，表示配置NF服务实例支持的PLMN。<br>- 如果注册类型为REGMAX(RegMAX) ，则配置无效。通常不需要配置。 |
| NFINSTANCENAME | NF实例名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定NF实例名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~50。<br>默认值：无<br>配置原则：<br>该参数需要与ADD NFUUID命令中的NFINSTANCENAME值保持一致。 |
| SRVINSTANCEID | 服务实例标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定服务实例标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~50。<br>默认值：无<br>配置原则：<br>- 本参数与ADD NFSERVICE命令中的SRVINSTANCEID值一致时生效。<br>- 本参数构成字符只能是字母A～Z或a～z、数字0～9、中划线"-"和下划线"_"，且不能以中划线"-"或下划线"_"开头和结尾，例如，Service_Instance_0。 |
| MCC | 移动国家代码 | 可选必选说明：可选参数<br>参数含义：该参数用于指定移动国家代码。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是3。<br>默认值：无<br>配置原则：<br>该参数由3个十进制数字组成。 |
| MNC | 移动网号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定移动网号。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是2~3。<br>默认值：无<br>配置原则：<br>该参数由2~3个十进制数字组成。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/ALLOWEDPLMN]] · NF或NF服务支持的PLMN（ALLOWEDPLMN）

## 使用实例

运营商A需要配置NF实例SMF_Instance_0的服务实例Service_Instance_0支持PLMN“46001”。

```
ADD ALLOWEDPLMN: INDEX=0, REGTYPE= RegService, NFINSTANCENAME="SMF_Instance_0", SRVINSTANCEID="Service_Instance_0", MCC="460", MNC="01";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加NF或NF服务支持的PLMN（ADD-ALLOWEDPLMN）_09652458.md`
