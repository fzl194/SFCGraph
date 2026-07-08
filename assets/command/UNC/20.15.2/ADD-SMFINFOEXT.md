---
id: UNC@20.15.2@MMLCommand@ADD SMFINFOEXT
type: MMLCommand
name: ADD SMFINFOEXT（增加SMF扩展信息）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: SMFINFOEXT
command_category: 配置类
applicable_nf:
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 本局信息管理
- SMF
- SMF信息管理
status: active
---

# ADD SMFINFOEXT（增加SMF扩展信息）

## 功能

**适用NF：SMF**

该命令用于增加SMF实例扩展信息。

## 注意事项

- 该命令执行后立即生效。

- 最多可输入32条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SMFINSTANCENAME | SMF实例名称 | 可选必选说明：必选参数<br>参数含义：该参数用于在服务组（Service Group，简称SG）中唯一指定某个SMF实例。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~50。本参数的构成字符只能是字母A~Z或a~z、数字0~9、下划线“_”和中划线“-”，例如，SMF_Instance_0。<br>默认值：无<br>配置原则：<br>该参数可以参考LST SMFINFO中的SMFINSTANCENAME。 |
| ID | SMFINFOID | 可选必选说明：必选参数<br>参数含义：该参数用于唯一标识SMF实例中的某个SmfInfo。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~32。本参数的构成字符只能是字母A~Z或a~z、数字0~9、下划线“_”和中划线“-”。该参数大小写不敏感。<br>默认值：无<br>配置原则：无 |
| PRIORITY | 优先级 | 可选必选说明：可选参数<br>参数含义：该参数用于表示SMF实例中SmfInfo的优先级。为保证继承性，SMF服务发现流程中，NRF优先使用NFPROFILE中SmfInfo进行匹配，如果未匹配成功，再使用NFPROFILE中SmfInfoList中的SmfInfo进行匹配，最终向请求NF返回匹配的SMF信息，包括SmfInfo及SmfInfoList。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~65536。<br>默认值：65536<br>配置原则：<br>优先级数值配置越小，代表优先级越高。65536属于无效值。如果该参数取值为65536，则向NRF注册时，SmfInfoList里对应的SmfInfo中不携带PRIORITY字段。为保证NFPROFILE中SmfInfoList中SmfInfo的优先级低于SMF NFPROFILE中SmfInfo的优先级，请保证PRIORITY取值大于NFPROFILE/NFSERVICE的PRIORITY。 |
| PGWFQDN | PGW名称 | 可选必选说明：可选参数<br>参数含义：当SMF与PGW-C合一部署时，该参数表示PGW-C的FQDN名称，用于用户从EPC到5G互操作流程中，帮助AMF找到EPC承载所在的融合网关。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。该参数大小写不敏感。<br>默认值：无<br>配置原则：<br>- PGWFQDN由一个或多个LABEL构成，各LABEL间用“.”间隔。<br>- 每个LABEL的构成字符只能是字母A～Z或a～z、数字0～9和中划线“-”。<br>- PGWFQDN为空时，SmfInfoList中的SmfInfo中的PgwFqdn取值为SMFINFO配置中的PGWFQDN。如果该参数为空并且SMFINFO配置中的PGWFQDN也为空，SmfInfoList中的SmfInfo中的PgwFqdn为空。 |
| ACCESSTYPE | 接入类型 | 可选必选说明：可选参数<br>参数含义：该参数表示SMF支持的接入类型：3GPP、Non-3GPP或者都支持。<br>数据来源：本端规划<br>取值范围：<br>- “AccessTypeINVALID（无效接入类型）”：无效接入类型<br>- “AccessType3GPP_ACCESS（3GPP接入类型）”：3GPP接入类型<br>- “AccessTypeNON_3GPP_ACCESS（NON 3GPP接入类型）”：NON 3GPP接入类型<br>- “AccessTypeMAX（MAX接入类型）”：MAX接入类型<br>默认值：无<br>配置原则：<br>ACCESSTYPE为空时，SmfInfoList中的SmfInfo中的AccessType取值为SMFINFO配置中的ACCESSTYPE。如果该参数为空并且SMFINFO配置中的ACCESSTYPE也为空，SmfInfoList中的SmfInfo中的AccessType为空。 |
| ISMFSUPPORTIND | 是否支持作为I-SMF | 可选必选说明：可选参数<br>参数含义：该参数表示SMFINFO是否支持作为I-SMF。<br>数据来源：本端规划<br>取值范围：<br>- “INVALID（无效值）”：向NRF注册时不携带该参数。<br>- “SUPPORT（支持）”：向NRF注册时携带为true。<br>- “UNSUPPORT（不支持）”：向NRF注册时携带为false。<br>默认值：INVALID<br>配置原则：无 |

## 操作的配置对象

- [SMF扩展信息（SMFINFOEXT）](configobject/UNC/20.15.2/SMFINFOEXT.md)

## 使用实例

增加SMF扩展信息配置，SMF实例名称为SMF_Instance_0，ID是central，优先级是100：

```
ADD SMFINFOEXT: SMFINSTANCENAME="SMF_Instance_0", ID="central", PRIORITY=100;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加SMF扩展信息（ADD-SMFINFOEXT）_70462525.md`
