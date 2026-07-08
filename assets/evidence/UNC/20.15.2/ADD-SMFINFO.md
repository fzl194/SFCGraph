# 增加SMF信息（ADD SMFINFO）

- [命令功能](#ZH-CN_MMLREF_0209653991__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0209653991__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0209653991__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0209653991__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0209653991)

**适用NF：SMF**

该命令用以配置SMF实例信息，如SMF的名称。SMF实例信息属于基础配置，在SMF向NRF注册时会用到本命令的配置数据。

## [注意事项](#ZH-CN_MMLREF_0209653991)

- 该命令执行后立即生效。

- 一个服务组（Service Group，简称SG）内只允许配置一个SMF实例。

- 最多可输入1条记录。

#### [操作用户权限](#ZH-CN_MMLREF_0209653991)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0209653991)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SMFINSTANCENAME | SMF实例名称 | 可选必选说明：必选参数<br>参数含义：该参数用于在服务组（Service Group，简称SG）中唯一指定某个SMF实例。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~50。本参数的构成字符只能是字母A~Z或a~z、数字0~9、下划线“_”和中划线“-”，例如，SMF_Instance_0。<br>默认值：无<br>配置原则：无 |
| SMFNAME | SMF名称 | 可选必选说明：可选参数<br>参数含义：该参数用于在运营商网络中唯一标识本SMF实例。当SMF向NRF注册时，如果未携带IP地址，则要携带本参数；如果携带了IP地址，则本参数可选携带。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。该参数大小写不敏感。<br>默认值：无<br>配置原则：<br>- SMFNAME由一个或多个LABEL构成，各LABEL间用“.”间隔。<br>- 每个LABEL的构成字符只能是字母A～Z或a～z、数字0～9和中划线“-”。 |
| INTERPLMNFQDN | PLMN间SMF名称 | 可选必选说明：可选参数<br>参数含义：该参数表示本SMF实例开放给互联运营商的名称，用于互联运营商的NF访问本SMF提供的服务。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。该参数大小写不敏感。<br>默认值：无<br>配置原则：<br>- INTERPLMNFQDN由一个或多个LABEL构成，各LABEL间用“.”间隔。<br>- 每个LABEL的构成字符只能是字母A～Z或a～z、数字0～9、中划线“-”和下划线“_” 。 |
| PGWFQDN | PGW名称 | 可选必选说明：可选参数<br>参数含义：当SMF与PGW-C合一部署时，该参数表示PGW-C的FQDN名称，用于用户从EPC到5G互操作流程中，帮助AMF找到EPC承载所在的融合网关。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。该参数大小写不敏感。<br>默认值：无<br>配置原则：<br>- PGWFQDN由一个或多个LABEL构成，各LABEL间用“.”间隔。<br>- 每个LABEL的构成字符只能是字母A～Z或a～z、数字0～9和中划线“-”。 |
| ACCESSTYPE | 接入类型 | 可选必选说明：可选参数<br>参数含义：该参数表示SMF支持的接入类型：3GPP、Non-3GPP或者都支持。<br>数据来源：本端规划<br>取值范围：<br>- “AccessTypeINVALID（无效接入类型）”：无效接入类型<br>- “AccessType3GPP_ACCESS（3GPP接入类型）”：3GPP接入类型<br>- “AccessTypeNON_3GPP_ACCESS（NON 3GPP接入类型）”：NON 3GPP接入类型<br>- “AccessTypeMAX（MAX接入类型）”：MAX接入类型<br>默认值：无<br>配置原则：无 |
| DESC | 描述信息 | 可选必选说明：可选参数<br>参数含义：该参数表示对本SMF实例的描述信息，在运维过程中起助记作用。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~32。<br>默认值：无<br>配置原则：无 |
| ISMFSUPPORTIND | 是否支持作为I-SMF | 可选必选说明：可选参数<br>参数含义：该参数表示SMFINFO是否支持作为I-SMF。<br>数据来源：本端规划<br>取值范围：<br>- “INVALID（无效值）”：向NRF注册时不携带该参数。<br>- “SUPPORT（支持）”：向NRF注册时携带为true。<br>- “UNSUPPORT（不支持）”：向NRF注册时携带为false。<br>默认值：INVALID<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0209653991)

增加SMF的信息配置，SMF名称为smf1.cluster1.net1.smf.5gc，提供给互联运营商的SMF名称是smf1.cluster1.net1.smf.5gc.mnc012.mcc345.3gppnetwork.org，支持3GPP接入：

```
ADD SMFINFO: SMFINSTANCENAME="SMF_Instance_0", SMFNAME="smf1.cluster1.net1.smf.5gc", INTERPLMNFQDN="smf1.cluster1.net1.smf.5gc.mnc012.mcc345.3gppnetwork.org", ACCESSTYPE=AccessType3GPP_ACCESS;
```
