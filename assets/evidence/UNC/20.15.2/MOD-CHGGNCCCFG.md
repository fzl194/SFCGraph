# 修改Gn接口计费属性选择策略(MOD CHGGNCCCFG)

- [命令功能](#ZH-CN_MMLREF_0000001172225051__1.3.1.1)
- [注意事项](#ZH-CN_MMLREF_0000001172225051__1.3.2.1)
- [本地用户权限](#ZH-CN_MMLREF_0000001172225051__1.3.3.1)
- [网管用户权限](#ZH-CN_MMLREF_0000001172225051__1.3.4.1)
- [参数说明](#ZH-CN_MMLREF_0000001172225051__1.3.5.1)
- [使用实例](#ZH-CN_MMLREF_0000001172225051__1.3.6.1)

#### [命令功能](#ZH-CN_MMLREF_0000001172225051)

**适用网元：SGSN**

该命令用于修改“SPECIAL_USER(指定用户)”和“ALL_USER(所有用户)”的Gn接口计费属性选择策略。SGSN在向GGSN发出的CREATE PDP CONTEXT REQ消息中，会携带计费属性这个信元。该命令用于修改填充Gn口计费属性信元的规则，对于签约用户级计费属性和签约APN级计费属性，根据签约有效、签约无效和未签约三种场景分别进行处理。Gn接口的消息是CREATE PDP CONTEXT REQ。匹配原理请参见ADD CHGGNCCCFG命令中的介绍。

#### [注意事项](#ZH-CN_MMLREF_0000001172225051)

该命令执行后立即生效。

#### [本地用户权限](#ZH-CN_MMLREF_0000001172225051)

manage-ug；system-ug

#### [网管用户权限](#ZH-CN_MMLREF_0000001172225051)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_MMLREF_0000001172225051)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定需要修改所包含的用户范围。<br>数据来源：整网规划<br>取值范围：<br>- “ALL_USER(所有用户)”<br>- “SPECIAL_USER(指定用户)”<br>默认值：无 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定需要修改<br>“SPECIAL_USER(指定用户)”<br>的IMSI前缀，系统根据该参数与用户的IMSI进行匹配，以区分不同的用户群。<br>数据来源：整网规划<br>取值范围：5～15位十进制数字<br>默认值：无<br>说明：- 相同IMSI前缀只能配置一条记录。<br>- IMSI前缀的匹配方式采取由前向后的最长匹配，即若对于用户可以匹配到多个用户群，则使用IMSI前缀最长的用户群配置。 |
| APNCC | 有效的APN CC | 可选必选说明：可选参数<br>参数含义：该参数用于指定<br>“有效的APN CC”<br>。当有签约的计费属性时，如果签约的APN级计费属性在该配置的范围内，则SGSN在向GGSN发送的CREATE PDP CONTEXT REQ消息中直接携带签约的APN级的计费属性；否则根据<br>“SUBCC(有效的用户CC)”<br>进行匹配。<br>数据来源：整网规划<br>取值范围：<br>- “NONE(无)-0000”说明：有效的APN CC中NONE当前在系统中尚未启用，预留为扩展项<br>- “HB(实时计费)-0100”<br>- “FR(包月制)-0200”<br>- “HB_FR(实时计费 & 包月制)-0300”<br>- “PS(预付费)-0400”<br>- “HB_PS(实时计费 & 预付费)-0500”<br>- “FR_PS(包月制 & 预付费)-0600”<br>- “HB_FR_PS(实时计费 & 包月制 & 预付费)-0700”<br>- “NB(普通计费)-0800”<br>- “HB_NB(实时计费 & 普通计费)-0900”<br>- “FR_NB(包月制 & 普通计费)-0A00”<br>- “HB_FR_NB(实时计费 & 包月制 & 普通计费)-0B00”<br>- “PS_NB(预付费 & 普通计费)-0C00”<br>- “HB_PS_NB(实时计费 & 预付费 & 普通计费)-0D00”<br>- “FR_PS_NB(包月制 & 预付费 & 普通计费)-0E00”<br>- “HB_FR_PS_NB(实时计费 & 包月制 & 预付费 & 普通计费)-0F00”<br>默认值：无 |
| SUBCC | 有效的用户CC | 可选必选说明：可选参数<br>参数含义：该参数用于指定<br>“有效的用户CC”<br>。当有签约的计费属性时，如果签约的用户级计费属性在该配置的范围内，则SGSN在向GGSN发出的CREATE PDP CONTEXT REQ消息中直接携带签约的用户级的计费属性；否则根据<br>“签约无效CC携带策略”<br>处理。<br>数据来源：整网规划<br>取值范围：<br>- “NONE(无)-0000”说明：有效的用户CC中NONE当前在系统中尚未启用，预留为扩展项<br>- “HB(实时计费)-0100”<br>- “FR(包月制)-0200”<br>- “HB_FR(实时计费 & 包月制)-0300”<br>- “PS(预付费)-0400”<br>- “HB_PS(实时计费 & 预付费)-0500”<br>- “FR_PS(包月制 & 预付费)-0600”<br>- “HB_FR_PS(实时计费 & 包月制 & 预付费)-0700”<br>- “NB(普通计费)-0800”<br>- “HB_NB(实时计费 & 普通计费)-0900”<br>- “FR_NB(包月制 & 普通计费)-0A00”<br>- “HB_FR_NB(实时计费 & 包月制 & 普通计费)-0B00”<br>- “PS_NB(预付费 & 普通计费)-0C00”<br>- “HB_PS_NB(实时计费 & 预付费 & 普通计费)-0D00”<br>- “FR_PS_NB(包月制 & 预付费 & 普通计费)-0E00”<br>- “HB_FR_PS_NB(实时计费 & 包月制 & 预付费 & 普通计费)-0F00”<br>默认值：无 |
| INVLDCCRULE | 签约无效CC携带策略 | 可选必选说明：可选参数<br>参数含义：该参数用于指定<br>“签约无效CC携带策略”<br>。 按照<br>“有效的APN CC ”<br>和<br>“有效的用户CC”<br>配置，检查签约的APN级CC和用户级CC都无效时，就使用该参数的配置策略处理。<br>数据来源：整网规划<br>取值范围：<br>- “TRANSMIT_ZERO(带0)”：Create PDP Context Request消息中携带的CC为0000。<br>- “TRANSMIT_NONE(不带CC)”：Create PDP Context Request消息中不携带CC。<br>- “TRANSMIT_DEFAULT_VALUE(带缺省CC)”：Create PDP Context Request消息中携带“DFTCCINVLD(签约无效CC时的缺省CC)”。<br>- “APN_CC_FIRST(APN CC优先)”：如果用户签约了APN级CC和用户级CC，则Create PDP Context Request消息中优先携带签约的APN级CC。<br>- “SUBSCRIBER_CC_ONLY(只选用户CC)”：如果用户签约了APN级CC和用户级CC，则Create PDP Context Request消息中携带签约的用户级CC。<br>默认值：无 |
| DFTCCINVLD | 签约无效CC时的缺省CC | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定签约无效CC时系统使用的缺省CC。<br>该参数在<br>“INVLDCCRULE(签约无效CC携带策略)”<br>参数设置为<br>“TRANSMIT_DEFAULT_VALUE(带缺省CC)”<br>时，才需要配置。<br>数据来源：整网规划<br>取值范围：<br>- “NONE(无)-0000”<br>- “HB(实时计费)-0100”<br>- “FR(包月制)-0200”<br>- “HB_FR(实时计费 & 包月制)-0300”<br>- “PS(预付费)-0400”<br>- “HB_PS(实时计费 & 预付费)-0500”<br>- “FR_PS(包月制 & 预付费)-0600”<br>- “HB_FR_PS(实时计费 & 包月制 & 预付费)-0700”<br>- “NB(普通计费)-0800”<br>- “HB_NB(实时计费 & 普通计费)-0900”<br>- “FR_NB(包月制 & 普通计费)-0A00”<br>- “HB_FR_NB(实时计费 & 包月制 & 普通计费)-0B00”<br>- “PS_NB(预付费 & 普通计费)-0C00”<br>- “HB_PS_NB(实时计费 & 预付费 & 普通计费)-0D00”<br>- “FR_PS_NB(包月制 & 预付费 & 普通计费)-0E00”<br>- “HB_FR_PS_NB(实时计费 & 包月制 & 预付费 & 普通计费)-0F00”<br>默认值：无 |
| NOCCRULE | 未签约CC携带策略 | 可选必选说明：可选参数<br>参数含义：该参数用于指定未签约CC时系统使用的携带策略。<br>数据来源：整网规划<br>取值范围：<br>- “TRANSMIT_ZERO(带0)”：Create PDP Context Request消息中携带的CC为0000。<br>- “TRANSMIT_NONE(不带CC)”：Create PDP Context Request消息中不携带CC。<br>- “TRANSMIT_DEFAULT_VALUE(带缺省CC)”：Create PDP Context Request消息中携带“未签约CC时系统使用的缺省CC”<br>默认值：无 |
| DFTCCNO | 未签约CC时的缺省CC | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定未签约CC时系统使用的缺省CC。<br>该参数在<br>“NOCCRULE(未签约CC携带策略 )”<br>参数设置为<br>“TRANSMIT_DEFAULT_VALUE(带缺省CC)”<br>时，才需要配置。<br>数据来源：整网规划<br>取值范围：<br>- “NONE(无)-0000”<br>- “HB(实时计费)-0100”<br>- “FR(包月制)-0200”<br>- “HB_FR(实时计费 & 包月制)-0300”<br>- “PS(预付费)-0400”<br>- “HB_PS(实时计费 & 预付费)-0500”<br>- “FR_PS(包月制 & 预付费)-0600”<br>- “HB_FR_PS(实时计费 & 包月制 & 预付费)-0700”<br>- “NB(普通计费)-0800”<br>- “HB_NB(实时计费 & 普通计费)-0900”<br>- “FR_NB(包月制 & 普通计费)-0A00”<br>- “HB_FR_NB(实时计费 & 包月制 & 普通计费)-0B00”<br>- “PS_NB(预付费 & 普通计费)-0C00”<br>- “HB_PS_NB(实时计费 & 预付费 & 普通计费)-0D00”<br>- “FR_PS_NB(包月制 & 预付费 & 普通计费)-0E00”<br>- “HB_FR_PS_NB(实时计费 & 包月制 & 预付费 & 普通计费)-0F00”<br>默认值：无 |
| ZEROCCRULE | 签约0值CC携带策略 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定签约0值CC时系统使用的携带策略。<br>该参数在<br>“INVLDCCRULE(签约无效CC携带策略)”<br>参数设置为<br>“APN_CC_FIRST(APN CC优先)”<br>或<br>“SUBSCRIBER_CC_ONLY(只选用户CC)”<br>时，才需要配置。<br>数据来源：整网规划<br>取值范围：<br>- “TRANSMIT_ZERO(带0)”：Create PDP Context Request消息中携带的CC为0000。<br>- “TRANSMIT_NONE(不带CC)”：Create PDP Context Request消息中不携带CC。<br>- “TRANSMIT_DEFAULT_VALUE(带缺省CC)”：Create PDP Context Request消息中携带“DFTCCZERO（签约0值CC时的缺省CC）”。<br>默认值：无 |
| DFTCCZERO | 签约0值CC时的缺省CC | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定签约0值CC时系统使用的缺省CC。<br>该参数在<br>“ZEROCCRULE(签约0值CC携带策略)”<br>参数设置为<br>“TRANSMIT_DEFAULT_VALUE(带缺省CC)”<br>时，才需要配置。<br>数据来源：整网规划<br>取值范围：<br>- “NONE(无)-0000”<br>- “HB(实时计费)-0100”<br>- “FR(包月制)-0200”<br>- “HB_FR(实时计费 & 包月制)-0300”<br>- “PS(预付费)-0400”<br>- “HB_PS(实时计费 & 预付费)-0500”<br>- “FR_PS(包月制 & 预付费)-0600”<br>- “HB_FR_PS(实时计费 & 包月制 & 预付费)-0700”<br>- “NB(普通计费)-0800”<br>- “HB_NB(实时计费 & 普通计费)-0900”<br>- “FR_NB(包月制 & 普通计费)-0A00”<br>- “HB_FR_NB(实时计费 & 包月制 & 普通计费)-0B00”<br>- “PS_NB(预付费 & 普通计费)-0C00”<br>- “HB_PS_NB(实时计费 & 预付费 & 普通计费)-0D00”<br>- “FR_PS_NB(包月制 & 预付费 & 普通计费)-0E00”<br>- “HB_FR_PS_NB(实时计费 & 包月制 & 预付费 & 普通计费)-0F00”<br>默认值：无 |
| CCINSCDR | S-CDR中的计费属性 | 可选必选说明：可选参数<br>参数含义：该参数用于指定S-CDR中的计费属性是否与Gn接口中的计费属性保持一致。<br>数据来源：整网规划<br>取值范围：<br>- “YES（是）”<br>- “NO（否）”<br>默认值：无<br>说明：- “YES（是）”：S-CDR中的计费属性取Gn接口中的计费属性。但当HLR中计费属性未签约或签约无效，且Gn接口不携带计费属性字段，则S-CDR中携带的计费属性无法和Gn接口中的计费属性一致。<br>- “NO（否）”:S-CDR中的计费属性由用户在HLR中签约的计费属性，和[**ADD CHGAPN**](../APN计费属性/增加APN计费属性(ADD CHGAPN)_72344965.md)、[**ADD CHGDCHAR**](../缺省计费属性参数配置/增加缺省计费属性参数(ADD CHGDCHAR)_26145380.md)、[**SET CHGCDR**](../计费控制/设置计费CDR参数（SET CHGCDR）_26145372.md)命令配置的计费属性确定。 |

#### [使用实例](#ZH-CN_MMLREF_0000001172225051)

修改 “SUBRANGE（用户范围）” 为 “SPECIAL_USER（指定用户）” 的， “IMSIPRE（IMSI前缀）” 为 “10010” 的记录， “APNCC（有效的APN CC）” 修改为 “FR（包月制）” ， “SUBCC（有效的用户 CC）” 修改为 “HB（实时计费）” ， “INVLDCCRULE（签约无效CC携带策略）” 修改为 “TRANSMIT_ZERO（带0）” ， “NOCCRULE（未签约CC携带策略）” 修改为 “TRANSMIT_NONE（不带CC）” ：

MOD CHGGNCCCFG: SUBRANGE=SPECIAL_USER, IMSIPRE="10010", APNCC=FR-1, SUBCC=HB-1, INVLDCCRULE=TRANSMIT_ZERO, NOCCRULE=TRANSMIT_NONE;
