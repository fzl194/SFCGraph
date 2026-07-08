---
id: UNC@20.15.2@MMLCommand@ADD GBARD
type: MMLCommand
name: ADD GBARD（增加Gb模式接入限制参数）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: GBARD
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: ''
is_dangerous: false
max_records: 2048
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 移动性管理
- 接入限制管理
- Gb模式接入限制参数
status: active
---

# ADD GBARD（增加Gb模式接入限制参数）

## 功能

**适用网元：SGSN**

该命令用于增加Gb模式接入限制参数。该命令先根据IMSI号段将用户进行分类，再对每一类用户按照用户使用的卡类型（SIM/USIM）、签约的ARD信息、签约的APN信息进行区分而控制用户接入GERAN网络。

此命令适用于以下场景。若运营商希望拒绝某个号段接入GERAN系统，则可以启用根据签约ARD控制用户接入特性；若运营商希望控制某类用户是否允许接入GERAN，但HLR/HSS不支持ARD时，则可以启用根据签约APN控制用户接入特性；若运营商已经强制要求对GERAN用户使用SIM卡，UTRAN用户使用USIM卡，并希望对不同卡进行灵活的接入控制，就需要启用按SIM卡/USIM卡控制用户接入特性。

## 注意事项

- 该表的最大记录数为2048。
- 当本表记录中存在用户的IMSI对应的IMSI前缀或者所在的IMSI范围，且用户的属性（APNNI/卡类型）至少有一项与GBARD配置的属性匹配时，按照该配置的控制类型（CTRLTYPE）对用户接入进行控制。
- 当本表记录中存在用户的IMSI对应的IMSI前缀或者所在的IMSI范围，且用户的属性（APNNI/卡类型）与GBARD配置的属性均不匹配时，按照与该配置相反的控制类型（CTRLTYPE）对用户接入进行控制。
- 当本表记录中不存在用户的IMSI对应的IMSI前缀或者所在的IMSI范围时，不限制用户接入。
- 此配置涉及用户接入控制功能特性（特性编号：WSFD-106003，License项：LKV2ARD02），执行命令请使用[**DSP LICENSE**](../../../../../../平台服务管理/操作维护/License管理/显示License(DSP LICENSE)_00360098.md)命令确认对应特性license是否得到授权，执行[**LST LICENSESWITCH**](../../../../../../平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md)命令确认特性开关状态为“ENABLE(打开)”。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定用户范围。<br>数据来源：整网规划<br>取值范围：<br>- “ALL_USER(所有用户)”：表示该指定用户范围为所有用户。<br>- “SPECIAL_IMSIPRE(指定IMSI前缀)”：表示该用户范围为指定IMSI前缀。<br>- “SPECIAL_IMSI_RANGE(指定IMSI范围)”：表示该用户范围为指定IMSI范围。<br>默认值：无<br>配置原则：当存在<br>“用户范围”<br>为<br>“SPECIAL_IMSIPRE(指定IMSI前缀)”<br>的记录时，不允许再添加<br>“用户范围”<br>为<br>“SPECIAL_IMSI_RANGE(指定IMSI范围)”<br>的记录。同理，当存在<br>“用户范围”<br>为<br>“SPECIAL_IMSI_RANGE(指定IMSI范围)”<br>的记录时，不允许再添加<br>“用户范围”<br>为<br>“SPECIAL_IMSIPRE(指定IMSI前缀)”<br>的记录。<br>说明：匹配本表记录中的用户范围时，系统首先会匹配<br>“SPECIAL_IMSIPRE(指定IMSI前缀)”<br>或<br>“SPECIAL_IMSI_RANGE(指定IMSI范围)”<br>的记录，如果没有符合的记录，才会匹配<br>“ALL_USER(所有用户)”<br>的用户范围。 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定IMSI前缀。使用时按照IMSI最长匹配进行查询。<br>前提条件：该参数在<br>“SUBRANGE(用户范围)”<br>设置为<br>“SPECIAL_IMSIPRE(指定IMSI前缀)”<br>时生效。<br>数据来源：整网规划<br>取值范围：1~15位数字<br>默认值：无 |
| BEGIMSI | 起始IMSI | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定用户的起始IMSI。<br>前提条件：该参数在<br>“SUBRANGE(用户范围)”<br>设置为<br>“SPECIAL_IMSI_RANGE(指定IMSI范围)”<br>时生效。<br>数据来源：整网规划<br>取值范围：1~15位数字<br>默认值：无<br>配置原则：当起始IMSI与终止IMSI长度全为15位时，起始IMSI要小于等于终止IMSI，否则起始IMSI要小于终止IMSI。 |
| ENDIMSI | 终止IMSI | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定用户的终止IMSI。<br>前提条件：该参数在<br>“SUBRANGE(用户范围)”<br>设置为<br>“SPECIAL_IMSI_RANGE(指定IMSI范围)”<br>时生效。<br>数据来源：整网规划<br>取值范围：1~15位数字<br>默认值：无<br>配置原则：参见<br>[参考信息](#ZH-CN_MMLREF_0000001126305284__re1)<br>。 |
| APNNI | APNNI | 可选必选说明：可选参数<br>参数含义：该参数用于配置指定APNNI。<br>数据来源：整网规划<br>取值范围：1~62位字符串<br>默认值：<br>“*”<br>配置原则：<br>- APN网络标识地址由一个或多个LABEL构成，各LABEL间用“.”间隔。<br>- 每个LABEL的构成字符只能是字母A~Z或a~z、数字0~9和中划线“-”，字母不区分大小写。<br>- APN网络标识地址不能以“rac”、“lac”、“sgsn”或“rnc”开头，不能以“.gprs”结尾。<br>说明：如果APNNI配置为“*”，表示该记录适用于所有的APNNI。 |
| CARDTYPE | 卡类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定用户的卡类型。<br>数据来源：整网规划<br>取值范围：<br>- “SIM(SIM)”<br>- “USIM(USIM)”<br>默认值：无<br>配置原则：<br>- 如果选中全部清空，表示不根据用户签约的SIM卡或USIM卡作为用户的附加属性进行接入限制判断条件。<br>- 如果选中其中之一或都全选，表示SIM卡和/或USIM卡将作为用户的附加属性作为接入限制的判断条件，不符合条件的用户将采取与“控制类型”相反的控制策略。<br>- 如果选中“SIM”卡，控制类型为“REJECT(拒绝)”，表示非SIM卡的用户都将被允许接入。<br>- 如果选中“USIM”卡，控制类型为“ALLOW(允许)”，表示非USIM卡的用户都将被拒绝接入。<br>- 如果选中“SIM”卡和“USIM”卡，控制类型为“ALLOW(允许)”，表示不根据用户卡类型控制用户接入。<br>- 如果选中“SIM”卡和“USIM”卡，控制类型为“REJECT(拒绝)”，表示该记录中指定的用户范围内的用户都不能接入。<br>- 如果用户不配置鉴权(可执行[**LST GBAUTHCIPH**](../../../业务安全管理/用户安全管理/Gb模式用户安全参数/查询Gb模式用户安全参数(LST GBAUTHCIPH)_72345241.md)命令查看)，本命令中关于卡类型限制的判断不生效，此时不会对不鉴权的用户做卡类型的接入限制。 |
| ARD | 启用签约ARD | 可选必选说明：可选参数<br>参数含义：该参数用于指定是否启用签约ARD。<br>数据来源：整网规划<br>取值范围：<br>- “NO(否)”<br>- “YES(是)”<br>默认值：<br>“NO(否)”<br>配置原则：<br>- 不启用签约ARD时，该参数设置为“NO(否)”；启用签约ARD时，该参数设置为“YES(是)”。<br>- 不建议同时使用签约ARD功能与签约APN NI功能。 |
| CTRLTYPE | 控制类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定是否允许用户接入。<br>数据来源：整网规划<br>取值范围：<br>- “ALLOW(允许)”<br>- “REJECT(拒绝)”<br>默认值：无<br>配置原则：当只使用ARD的功能时，该参数建议设置为<br>“ALLOW(允许)”<br>，以防止受到APNNI默认值的影响。 |
| CAUSE | 原因值 | 可选必选说明：可选参数<br>参数含义：该参数用于指定原因值。<br>数据来源：整网规划<br>取值范围：<br>- “CUSTOMER_DEFINED(自定义)”：表示指定原因值为自定义。<br>- “GPRS_SERVICE_NOT_ALLOWED(GPRS服务被禁止)”：表示指定原因值为GPRS服务被禁止。<br>- “GPRS_NONGPRS_SRV_NOT_ALLOWED(GPRS和非GPRS服务都被禁止)”：表示指定原因值为GPRS和非GPRS服务都被禁止。<br>- “PLMN_NOT_ALLOWED(PLMN被禁止)”：表示指定原因值为PLMN被禁止。<br>- “LA_NOT_ALLOWED(本地区域被禁止)”：表示指定原因值为本地区域被禁止。<br>- “ROAMING_NOT_ALLOWED_IN_LA(本地漫游被禁止)”：表示指定原因值为本地漫游被禁止。<br>- “GPRS_SRV_NOT_ALLOWED_IN_PLMN(本PLMN内GPRS服务被禁止)”：表示指定原因值为本PLMN内GPRS服务被禁止。<br>- “NO_SUITABLE_CELLS_IN_LA(本地无合适小区)”：表示指定原因值为本地无合适单元。<br>默认值：<br>“NO_SUITABLE_CELLS_IN_LA(本地无合适小区)”<br>说明：附着或路由更新拒绝的原因值，请参考3GPP TS 24.008输入。 |
| SDCAUSE | 自定义原因值 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定自定义原因值。<br>前提条件：该参数在<br>“CAUSE(原因值)”<br>设置为<br>“CUSTOMER_DEFINED(自定义)”<br>时生效。<br>数据来源：整网规划<br>取值范围：1~254<br>默认值：无<br>说明：当原因值为自定义时，根据3GPP TS 24.008填写。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/GBARD]] · Gb模式接入限制参数（GBARD）

## 使用实例

1. 增加一条Gb模式接入限制参数记录，用户范围为ALL_USER，控制类型为拒绝，原因值为自定义，自定义原因值为2：
  ADD GBARD: SUBRANGE=ALL_USER, CTRLTYPE=REJECT, CAUSE=CUSTOMER_DEFINED, SDCAUSE=2;
2. 增加一条Gb模式接入限制参数记录，用户范围为SPECIAL_IMSIPRE，IMSIPRE为123456，控制类型为拒绝，原因值为GPRS_SERVICE_NOT_ALLOWED：
  ADD GBARD: SUBRANGE=SPECIAL_IMSIPRE, IMSIPRE="123456", CTRLTYPE=REJECT, CAUSE=GPRS_SERVICE_NOT_ALLOWED;

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-GBARD.md`
