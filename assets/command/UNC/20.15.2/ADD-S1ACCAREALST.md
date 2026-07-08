---
id: UNC@20.15.2@MMLCommand@ADD S1ACCAREALST
type: MMLCommand
name: ADD S1ACCAREALST（增加S1模式接入控制配置）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: S1ACCAREALST
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
max_records: 1024
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 移动性管理
- 区域漫游限制管理
- S1模式区域漫游限制参数
status: active
---

# ADD S1ACCAREALST（增加S1模式接入控制配置）

## 功能

![](增加S1模式接入控制配置（ADD S1ACCAREALST）_72345153.assets/notice_3.0-zh-cn_2.png)

- 执行该命令可能会导致用户接入异常，请谨慎操作。
- 参数（控制类型）：为防止误操作产生的业务影响，请确认命令中各参数取值合理有效。

**适用网元：MME**

此命令用于增加S1模式区域漫游限制参数，根据用户当前所在的位置，控制是否允许进行漫游。

当针对不同的用户群在相应的区域群中设置对应的漫游控制策略时，需要执行此命令。

## 注意事项

- 此命令执行后立即生效。
- 此命令最大记录数为1024。
- 此命令配置后会根据用户当前所在的位置，控制是否允许进行漫游。对于已经接入的用户，配置策略随后续业务流程（如：service request或TAU流程）生效；对于新接入的用户，配置策略随当前业务流程（attach和Inter TAU流程）立即生效。
- 如果输入的AREAID在AREAGPMEM表中对应的记录IDTYPE选择了RA或者LA（可执行[**LST AREAGPMEM**](../区域群成员管理/查询区域群成员(LST AREAGPMEM)_72345143.md)查看），则不允许添加。
- 此配置涉及区域漫游限制特性（特性编号：WSFD-105003，License部件编码：LKV2RRR02），执行命令前请使用[**DSP LICENSE**](../../../../../../平台服务管理/操作维护/License管理/显示License(DSP LICENSE)_00360098.md)命令确认对应特性license是否得到授权，执行[**LST LICENSESWITCH**](../../../../../../平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md)命令确认特性开关状态为“ENABLE(打开)”。
- 如果需要把禁止UE接入的TA从下发给UE的TA List中删除，以严格禁止UE接入指定的TA区域，请执行[**SET MMFUNC**](../../MM扩展功能管理/设置移动性管理扩展功能(SET MMFUNC)_26145512.md)设置“TALIST(TA List过滤)”参数。
- 如果需要把禁止UE接入的区域信息发送给eNodeB，避免eNodeB把ECM-CONNECTED状态的用户切换到被禁止接入的区域，请执行[**SET MMFUNC**](../../MM扩展功能管理/设置移动性管理扩展功能(SET MMFUNC)_26145512.md)命令设置“FORBIDTA(Forbidden TAs)”参数。
- 当“SPECSUB（拒绝特征用户接入）”为“YES(是)”时，“SUBRFSP（拒绝特征RFSP用户接入）”和“SUBCSFB（拒绝CSFB用户接入）”两个参数至少有一个需要配置为“YES(是)”。
- 如果配置了多个用户群标识，且用户群标识分别关联了[**ADD SUBGPMEM**](../用户群成员管理/增加用户群成员(ADD SUBGPMEM)_26305374.md)和[**ADD MSISDNSUBGPMEM**](../MSISDN用户群成员管理/增加MSISDN用户群成员(ADD MSISDNSUBGPMEM)_72345167.md)，则系统优先使用IMSI进行匹配，对于同一用户，如果使用IMSI匹配成功则不会再使用MSISDN进行匹配。
- 当“SPECSUB（拒绝特征用户接入）”配置为“YES(是)”，或“ENBIND（指示特征RFSP索引）”配置为“HORL(切换限制列表)”或“RFSP_ID(RFSP ID)”时，如果配置了“SUBID（用户群标识）”，则配置的“SUBID（用户群标识）”不能是已被[**ADD MSISDNSUBGPMEM**](../MSISDN用户群成员管理/增加MSISDN用户群成员(ADD MSISDNSUBGPMEM)_72345167.md)引用的。
- 当该命令增加上百条记录时，对系统性能影响程度为中等。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| AREA | 区域范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定区域范围。<br>数据来源：整网规划<br>取值范围：<br>- “AG(区域组)”：表示该区域标识类型为区域组。<br>- “TA(指定跟踪区)”：表示该区域标识类型为指定跟踪区。<br>- “OTHER(其他)”：表示该区域标识类型为其他。<br>配置原则：<br>- 本表“区域范围”为“OTHER(其他)”的记录可以与“区域范围”为“AG(区域组)”的记录共存，也可以与“区域范围”为“TA(指定跟踪区)”的记录共存；但是“区域范围”为“AG(区域组)”的记录不能与“区域范围”为“TA(指定跟踪区)”的记录共存。<br>默认值：无<br>说明：- 区域范围表示进行接入控制所适用的位置区域。<br>- 区域范围按照粒度从粗到细分为以下几个级别：区域组，指定跟踪区，其他。<br>- 相同粒度区域范围的各记录的区域范围不能交迭。<br>- 用户接入网络时，MME根据用户所在**区域范围**的**控制类型**拒绝或允许用户接入。<br>- 如果在**AG(区域组)**或**TA(指定跟踪区)**内，继续判断用户IMSI是否在**用户范围**内。如果在**用户范围**内，则根据配置的**控制类型**拒绝或允许用户接入。如果不在**用户范围**内，则允许用户接入。<br>- 如果不在**AG(区域组)**或**TA(指定跟踪区)**内，MME判断用户IMSI是否在**OTHER(其他)**配置中，如果在，则拒绝用户接入。如果不在，则允许用户接入。 |
| MCC | 移动国家码 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定移动国家代码。<br>前提条件：该参数在<br>“AREA(区域范围)”<br>参数设置为<br>“TA(跟踪区)”<br>时，才需要配置。<br>数据来源：整网规划<br>取值范围：3位的十进制数字<br>默认值：无 |
| MNC | 移动网号 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定移动网号。<br>前提条件：该参数在<br>“AREA(区域范围)”<br>参数设置为<br>“TA(跟踪区)”<br>时，才需要配置。<br>数据来源：整网规划<br>取值范围：2～3位的十进制数字<br>默认值：无 |
| TAC | 跟踪区域码 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定跟踪区域码。<br>前提条件：该参数在<br>“AREA(区域范围)”<br>参数设置为<br>“TA(跟踪区)”<br>时，才需要配置。<br>数据来源：整网规划<br>取值范围：0x0000～0xFFFF<br>默认值：无 |
| TACRANGE | 跟踪区域码范围 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定跟踪区域码范围。<br>前提条件：该参数在当<br>“AREA(区域范围)”<br>参数设置为<br>“TA(跟踪区)”<br>时，才需要配置。<br>数据来源：整网规划<br>取值范围：0x0000～0xFFFF<br>默认值：无<br>配置原则：该参数的取值需要大于或等于<br>“TAC”<br>。<br>说明：- 该参数与“TAC”参数构成一个TAC区段，方便客户配置连续的跟踪区域。<br>- 如果不输入，表示配置单个TAC。 |
| AREAID | 区域群标识 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定用户的区域群标识。<br>前提条件：该参数在<br>“AREA(区域范围)”<br>参数设置为<br>“AG(区域组)”<br>时，才需要配置。<br>数据来源：整网规划<br>取值范围：1～50<br>默认值：无<br>说明：该区域ID必须已经通过<br>[**ADD AREAGPMEM**](../区域群成员管理/增加区域群成员(ADD AREAGPMEM)_72225225.md)<br>命令添加成功，且在区域群成员表中的记录对应的<br>“IDTYPE”<br>只能为<br>“TA”<br>。可执行<br>[**LST AREAGPMEM**](../区域群成员管理/查询区域群成员(LST AREAGPMEM)_72345143.md)<br>进行查看。 |
| SUBRANGE | 用户范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定用户范围。<br>数据来源：整网规划<br>取值范围：<br>- “ALL_USER(所有用户)”：表示用户范围为所有用户。<br>- “SPECIAL_IMSIPRE(指定IMSI前缀)”：表示该用户范围为指定IMSI前缀。<br>- “USER_GROUP(用户群)”：表示用户范围为用户群。<br>- “SPECIAL_IMSI_RANGE(指定IMSI范围)”：表示该用户范围为指定IMSI范围。<br>- “UE_TYPE(终端类型)”:用于设置设备型号核准号码对应的终端类型。<br>- “FOREIGN_USER（外网用户）”：表示该用户范围为外网用户。<br>- “HOME_USER（本网用户）”：表示该用户范围为本网用户。<br>默认值：无<br>配置原则：<br>- 当存在“用户范围”为“SPECIAL_IMSIPRE(指定IMSI前缀)”、“USER_GROUP(用户群)”或“SPECIAL_IMSI_RANGE(指定IMSI范围)”中任意一种的记录时，不允许再添加另外两种用户范围的记录。<br>- 本表“用户范围”为“FOREIGN_USER(外网用户)”或“HOME_USER(本网用户)”的记录可以与“用户范围”为“USER_GROUP(用户群)”的记录共存，也可以与“用户范围”为“SPECIAL_IMSIPRE(指定IMSI前缀)”或“SPECIAL_IMSI_RANGE(指定IMSI范围)”的记录共存。<br>- 本表“用户范围”为“ALL_USER(所有用户)”的记录可以与“用户范围”为“USER_GROUP(用户群)”的记录共存，也可以与“用户范围”为“SPECIAL_IMSIPRE(指定IMSI前缀)”或“SPECIAL_IMSI_RANGE(指定IMSI范围)”的记录共存，也可以与“用户范围”为“FOREIGN_USER(外网用户)”或“HOME_USER(本网用户)”的记录共存。<br>- 当“区域范围”为“OTHER(其他)”时，“用户范围”只能是“SPECIAL_IMSIPRE(指定IMSI前缀)”，“SPECIAL_IMSI_RANGE(指定IMSI范围)”，“UE_TYPE(终端类型)”，“USER_GROUP(用户群)”，“FOREIGN_USER(外网用户)”或“HOME_USER(本网用户)”。<br>说明：当系统内存在多种用户范围的记录时，匹配的优先级由高到低为： SPECIAL_IMSIPRE/USER_GROUP/IMSI_RANGE ，FOREIGN_USER/HOME_USER，ALL USER，UE_TYPE的优先级是最低的。 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定用户的IMSI前缀。使用时按照IMSI最长匹配进行查询。<br>前提条件：该参数在<br>“SUBRANGE(用户范围)”<br>参数设置为<br>“SPECIAL_IMSIPRE(指定IMSI前缀)”<br>时，才需要配置。<br>数据来源：整网规划<br>取值范围：1～15位十进制数字<br>默认值：无<br>说明：- 支持IMSI最长匹配的查询方式。<br>- 该参数在用户群成员管理配置中不能存在对应记录，可执行[**LST SUBGPMEM**](../用户群成员管理/查询用户群成员(LST SUBGPMEM)_26145564.md)进行查看。 |
| BEGIMSI | 起始IMSI | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定用户的起始IMSI。<br>前提条件：该参数在<br>“SUBRANGE(用户范围)”<br>参数设置为<br>“SPECIAL_IMSI_RANGE(指定IMSI范围)”<br>时，才需要配置。<br>数据来源：整网规划<br>取值范围：1～15位十进制数字<br>默认值：无<br>配置原则：当起始IMSI与终止IMSI长度全为15位时，起始IMSI要小于等于终止IMSI，否则起始IMSI要小于终止IMSI。 |
| ENDIMSI | 终止IMSI | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定用户的终止IMSI。<br>前提条件：该参数在<br>“SUBRANGE(用户范围)”<br>参数设置为<br>“SPECIAL_IMSI_RANGE(指定IMSI范围)”<br>时，才需要配置。<br>数据来源：整网规划<br>取值范围：1～15位十进制数字<br>默认值：无<br>配置原则：当终止IMSI与起始IMSI长度全为15位时，终止IMSI要大于等于起始IMSI，否则终止IMSI要大于起始IMSI。<br>说明：输入的起始IMSI必须小于或者等于终止IMSI。判断起始IMSI和终止IMSI大小的原则是：对于输入IMSI的长度小于系统规定IMSI长度时，将该IMSI补足0到规定长度后进行大小比较，且起始IMSI必须小于终止IMSI。只有输入IMSI长度等于系统规定长度时，起始IMSI才能等于终止IMSI。 对于系统规定IMSI长度为15的情况，请参考<br>[表1](#ZH-CN_MMLREF_0000001172345153__tab1)<br>。 |
| SUBID | 用户群标识 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定用户群标识。<br>前提条件：该参数在<br>“SUBRANGE(用户范围)”<br>参数设置<br>“USER_GROUP(用户群)”<br>时，才需要配置。<br>数据来源：整网规划<br>取值范围：1～100<br>默认值：无<br>配置原则：<br>- 如果配置了多个用户群标识，且用户群标识分别关联了[**ADD SUBGPMEM**](../用户群成员管理/增加用户群成员(ADD SUBGPMEM)_26305374.md)和[**ADD MSISDNSUBGPMEM**](../MSISDN用户群成员管理/增加MSISDN用户群成员(ADD MSISDNSUBGPMEM)_72345167.md)，则系统优先使用IMSI进行匹配，对于同一用户，如果使用IMSI匹配成功则不会再使用MSISDN进行匹配。<br>- 本参数如果被[**ADD MSISDNSUBGPMEM**](../MSISDN用户群成员管理/增加MSISDN用户群成员(ADD MSISDNSUBGPMEM)_72345167.md)引用，“SPECSUB（拒绝特征用户接入）”不能配置为“YES(是)”，且“ENBIND（指示特征RFSP索引）”不能配置为“HORL(切换限制列表)”或“RFSP_ID(RFSP ID)”。<br>说明：- 该用户群标识必须已经通过[**ADD SUBGPMEM**](../用户群成员管理/增加用户群成员(ADD SUBGPMEM)_26305374.md)或[**ADD MSISDNSUBGPMEM**](../MSISDN用户群成员管理/增加MSISDN用户群成员(ADD MSISDNSUBGPMEM)_72345167.md)命令添加成功，可执行[**LST SUBGPMEM**](../用户群成员管理/查询用户群成员(LST SUBGPMEM)_26145564.md)或[**LST MSISDNSUBGPMEM**](../MSISDN用户群成员管理/查询MSISDN用户群成员(LST MSISDNSUBGPMEM)_72225251.md)进行查看。<br>- SUBID（用户群标识）基于IMSI前缀只会匹配一次，如果配置了多个SUBID（用户群标识），且不同SUBID（用户群标识）关联的[**ADD SUBGPMEM**](../用户群成员管理/增加用户群成员(ADD SUBGPMEM)_26305374.md)中IMSI号段前缀相同但长度不同，则只能匹配到最长IMSI前缀的SUBID（用户群标识），如果SUBID（用户群标识）匹配成功，但是跟踪区域未匹配成功，则只能匹配ALL_USER记录。 |
| NOID | 运营商标识 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定运营商标识。<br>前提条件：该参数在<br>“SUBRANGE（用户范围）”<br>配置为<br>“FOREIGN_USER（外网用户）”<br>或<br>“HOME_USER（本网用户）”<br>后生效。<br>数据来源：整网规划<br>取值范围：0～64，128～254<br>默认值：无<br>配置原则：<br>- 当用户为MNO用户时，该参数需要配置为0或128～254之间的值，该取值必须和[**ADD MNO**](../../../网络管理/归属网络运营商管理/MNO管理/MNO配置表/增加MNO配置信息(ADD MNO)_72345671.md)中配置的“MNOID”参数取值相同。<br>- 若该参数需要配置为1～64之间的值时，须先在[**ADD MVNO**](../../../网络管理/归属网络运营商管理/MVNO管理/MVNO配置表/增加MVNO配置信息(ADD MVNO)_72225747.md)中配置取值相同的“MVNOID”参数。 |
| CTRLTYPE | 控制类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定控制类型。<br>数据来源：整网规划<br>取值范围：<br>- “ALLOW(允许)”<br>- “REJECT(拒绝)”<br>默认值：无<br>配置原则：当<br>“区域范围”<br>为<br>“OTHER(其他)”<br>或<br>“用户范围”<br>为<br>“ALL_USER(所有用户)”<br>时，<br>“控制类型”<br>只能是<br>“REJECT(REJECT)”<br>。 |
| SPECSUB | 拒绝特征用户接入 | 可选必选说明：条件可选参数<br>参数含义：该参数用来设置是否拒绝特征用户接入。<br>前提条件：该参数在“CTRLTYPE（控制类型）”参数设置为“ALLOW（允许）”时，才需要配置。<br>数据来源：整网规划<br>取值范围：<br>- “NO(否)”<br>- “YES(是)”<br>默认值：“NO(否)”<br>配置原则：当目标区域仅限制具备某类特征的（如特定RFSP）特定用户接入时，需要将该参数设置成为“YES(是)”。<br>说明：该选项配置为“YES(是)”时，“AREA（区域范围）”必须配置为“AG(区域组)”，且“SUBRANGE(用户范围)”不可以配置为“UE_TYPE(终端类型)”。 |
| SUBRFSP | 拒绝特征RFSP用户接入 | 可选必选说明：条件可选参数<br>参数含义：该参数表示系统是否拒绝签约了特征RFSP的用户接入特征区域。<br>前提条件：该参数在“SPECSUB（拒绝特征用户接入）”参数配置为“YES(是)”后生效。<br>数据来源：整网规划<br>取值范围：<br>- “NO(否)”<br>- “YES(是)”<br>默认值：<br>“NO(否)”<br>配置原则：<br>- “NO(否)”：系统不拒绝签约了特征RFSP的用户接入指定区域。<br>- “YES(是)”：系统拒绝签约了特征RFSP的用户接入指定区域，但允许未签约特征RFSP的用户接入该区域。使用该选项时，“AREA（区域范围）”必须配置为“AG(区域组)”。另外，运营商需要为希望受控的用户签约特征RFSP，并通过[**ADD SPECRFSPVALUE**](../../RFSP管理/特征RFSP管理/特征RFSP取值范围管理/增加特征RFSP取值(ADD SPECRFSPVALUE)_26145534.md)命令设置特征RFSP的取值范围。 |
| REJRFSPIDX | 拒绝特征RFSP索引 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定禁止接入该区域的特征RFSP索引。<br>前提条件：该参数在“SUBRFSP（拒绝特征RFSP用户接入）”参数配置为"YES(是)"后生效。<br>数据来源：本端规划<br>取值范围：0~49<br>默认值：无<br>说明：该特征RFSP索引必须已经通过<br>[**ADD SPECRFSPVALUE**](../../RFSP管理/特征RFSP管理/特征RFSP取值范围管理/增加特征RFSP取值(ADD SPECRFSPVALUE)_26145534.md)<br>命令添加，且其“TYPE（类型）”为“ACC_REJECT（区域接入控制）”。可执行<br>[**LST SPECRFSPVALUE**](../../RFSP管理/特征RFSP管理/特征RFSP取值范围管理/查询特征RFSP取值(LST SPECRFSPVALUE)_26305346.md)<br>进行查看。 |
| SUBCSFB | 拒绝CSFB用户接入 | 可选必选说明：条件可选参数<br>参数含义：该参数用来设置是否拒绝CSFB用户接入本区域。<br>前提条件：该参数在“SPECSUB（拒绝特征用户接入）”参数配置为"YES(是)"后生效。<br>数据来源：整网规划<br>取值范围：<br>- “NO(否)”<br>- “YES(是)”<br>默认值：“NO(否)”<br>说明：只具备CSFB能力或虽然同时具备CSFB和VoPS能力但是指示CSFB优先的用户都将被判定为CSFB用户。 CSFB用户的具体判断规则请见<br>[图1](#ZH-CN_MMLREF_0000001172345153__csfb_judge_method)<br>。 |
| SRVCCCAP | SRVCC能力 | 可选必选说明：条件可选参数<br>参数含义：该参数用来设置是否根据用户的SRVCC能力来判断用户是否为CSFB用户。<br>前提条件：该参数在“SUBCSFB（拒绝CSFB用户接入）”参数配置为"YES(是)"后生效。<br>数据来源：本端规划<br>取值范围：<br>- “NO(否)”：无论UE是否备SRVCC能力都不会被系统判定成CSFB用户。<br>- “YES(是)”：如果UE不具备SRVCC能力则会被系统判定成CSFB用户。<br>默认值：“YES(是)” |
| CHKSTNSR | 匹配STN-SR | 可选必选说明：条件可选参数<br>参数含义：该参数用来设置是否根据用户有无签约STN-SR来判断是否为CSFB用户。<br>前提条件：该参数在“SUBCSFB（拒绝CSFB用户接入）”参数配置为"YES(是)"后生效。<br>数据来源：整网规划<br>取值范围：<br>- “NO(否)”：不根据用户有无签约STN-SR来判断用户是否为CSFB用户。<br>- “YES(是)”：没有签约STN-SR的用户即为CSFB用户。<br>默认值：“NO(否)” |
| REJCAUSE | 拒绝原因值 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定系统因用户签约了特征RFSP而禁止其接入时使用的拒绝原因值。<br>前提条件：该参数在“SPECSUB(拒绝特征用户接入)”参数设置为“YES(是)”时，才需要配置。<br>数据来源：整网规划<br>取值范围：<br>- “CUSTOMER_DEFINED(自定义)”：表示拒绝用户接入时使用的原因值为自定义。<br>- “EPS_SERVICE_NOT_ALLOWED(EPS服务被禁止)”：表示拒绝用户接入时使用的指定原因值为EPS服务被禁止。<br>- “EPS_NONEPS_SRV_NOT_ALLOWED(EPS和非EPS服务都被禁止)”：表示拒绝用户接入时使用的原因值为EPS和非EPS服务都被禁止。<br>- “PLMN_NOT_ALLOWED(PLMN被禁止)”：表示拒绝用户接入时使用的原因值为PLMN被禁止。<br>- “TA_NOT_ALLOWED(本地区域被禁止)”：表示拒绝用户接入时使用的原因值为本地区域被禁止。<br>- “ROAMING_NOT_ALLOWED_IN_TA(本地漫游被禁止)”：表示拒绝用户接入时使用的原因值为本地漫游被禁止。<br>- “EPS_SRV_NOT_ALLOWED_IN_PLMN(本PLMN内EPS服务被禁止)”：表示拒绝用户接入时使用的原因值为本PLMN内EPS服务被禁止。<br>- “NO_SUITABLE_CELLS_IN_TA(本地无合适小区)”：表示拒绝用户接入时使用的原因值为本地无合适小区。<br>默认值：<br>“NO_SUITABLE_CELLS_IN_TA(本地无合适小区)”<br>说明：附着或跟踪区更新拒绝的原因值，请参考3GPP TS 24.301输入。 |
| SDREJCAUSE | 自定义拒绝原因值 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定自定义原因值，请根据3GPP TS 24.301选择拒绝用户接入时NAS消息的原因值。<br>前提条件：该参数在<br>“REJCAUSE(拒绝原因值)”<br>参数设置为<br>“CUSTOMER_DEFINED(自定义)”<br>时，才需要配置。<br>数据来源：整网规划<br>取值范围：1～254<br>默认值：无 |
| CAUSE | 原因值 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定拒绝用户接入时使用的原因值。<br>前提条件：该参数在<br>“CTRLTYPE(控制类型)”<br>参数设置为<br>“REJECT(拒绝)”<br>时，才需要配置。<br>数据来源：整网规划<br>取值范围：<br>- “CUSTOMER_DEFINED(自定义)”：表示拒绝用户接入时使用的原因值为自定义。<br>- “EPS_SERVICE_NOT_ALLOWED(EPS服务被禁止)”：表示拒绝用户接入时使用的指定原因值为EPS服务被禁止。<br>- “EPS_NONEPS_SRV_NOT_ALLOWED(EPS和非EPS服务都被禁止)”：表示拒绝用户接入时使用的原因值为EPS和非EPS服务都被禁止。<br>- “PLMN_NOT_ALLOWED(PLMN被禁止)”：表示拒绝用户接入时使用的原因值为PLMN被禁止。<br>- “TA_NOT_ALLOWED(本地区域被禁止)”：表示拒绝用户接入时使用的原因值为本地区域被禁止。<br>- “ROAMING_NOT_ALLOWED_IN_TA(本地漫游被禁止)”：表示拒绝用户接入时使用的原因值为本地漫游被禁止。<br>- “EPS_SRV_NOT_ALLOWED_IN_PLMN(本PLMN内EPS服务被禁止)”：表示拒绝用户接入时使用的原因值为本PLMN内EPS服务被禁止。<br>- “NO_SUITABLE_CELLS_IN_TA(本地无合适小区)”：表示拒绝用户接入时使用的原因值为本地无合适小区。<br>默认值：<br>“NO_SUITABLE_CELLS_IN_TA(本地无合适小区)”<br>说明：附着或跟踪区更新拒绝的原因值，请参考24301输入。 |
| SDCAUSE | 自定义原因值 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定自定义原因值。<br>前提条件：该参数在<br>“CAUSE(原因值)”<br>参数设置为<br>“CUSTOMER_DEFINED(自定义)”<br>时，才需要配置。<br>数据来源：整网规划<br>取值范围：1～254<br>默认值：无<br>说明：当原因值为自定义时显示，根据24301填写。如果需要拒绝用户接入时NAS消息的原因值。 |
| UETYPE | 终端类型 | 可选必选说明：条件必选参数<br>参数含义：该参数用于设置需要进行接入限制的终端类型。<br>前提条件：该参数在<br>“SUBRANGE(用户范围)”<br>设置为<br>“UE_TYPE(终端类型)”<br>时，才需要配置。<br>数据来源：本端规划<br>取值范围：<br>- “ANDROID(Android)”<br>- “BLACKBERRY(Black Berry)”<br>- “IOS(iOS)”<br>- “WINDOWS(Windows)”<br>- “CUSTOM_TYPE_1(自定义类型1)”<br>- “CUSTOM_TYPE_2(自定义类型2)”<br>- “CUSTOM_TYPE_3(自定义类型3)”<br>- “CUSTOM_TYPE_4(自定义类型4)”<br>- “CUSTOM_TYPE_5(自定义类型5)”<br>- “CUSTOM_TYPE_6(自定义类型6)”<br>- “CUSTOM_TYPE_7(自定义类型7)”<br>- “CUSTOM_TYPE_8(自定义类型8)”<br>- “CUSTOM_TYPE_9(自定义类型9)”<br>- “CUSTOM_TYPE_10(自定义类型10)”<br>- “CUSTOM_TYPE_11(自定义类型11)”<br>- “CUSTOM_TYPE_12(自定义类型12)”<br>- “ALL_IMEI(所有IMEI)”<br>默认值：无<br>说明：- 除“ALL_IMEI(所有IMEI)”以外的其他参数均需要事先通过[**ADD IMEILIB**](../../../业务安全管理/Smartphone管理/终端类型识别/IMEI库管理/增加IMEI库记录（ADD IMEILIB）_26145734.md)命令完成配置。 |
| ENBIND | eNodeB指示方式 | 可选必选说明：可选参数<br>参数含义：该参数用于设置是否将区域接入限制信息指示给eNodeB及指示方式。<br>数据来源：整网规划<br>取值范围：<br>- “NO(不指示)”：不给eNodeB指示接入限制信息。<br>- “HORL(切换限制列表)”：通过Handover Restriction List信元将拒绝接入的区域携带给eNodeB。<br>- “RFSP_ID(RFSP ID)”：通过Subscriber Profile ID for RAT/Frequency priority信元指示eNodeB区域接入控制策略。<br>默认值：“NO(不指示)”<br>配置原则：当用户禁止接入的TAI个数超过50，且eNodeB支持通过SPID进行区域限制时，则建议通过“RFSP_ID(RFSP ID)”方式指示eNodeB区域接入限制信息。<br>说明：- 当设置成通过RFSP ID方式指示eNodeB时，本命令设置的RFSP优先级高于[**ADD EXTRFSP**](../../RFSP管理/扩展RFSP策略管理/增加扩展RFSP策略组成员(ADD EXTRFSP)_26145536.md)和[**ADD RFSP**](../../RFSP管理/RFSP策略管理/RFSP参数配置/增加RFSP配置(ADD RFSP)_26305350.md)命令设置的RFSP优先级。<br>- “AREA（区域范围）”配置为“AG(区域组)”，且“SUBRANGE(用户范围)”不为“UE_TYPE(终端类型)”时，该参数才会生效。<br>- 当参数设置为“RFSP_ID(RFSP ID)”时，“基于SPID的UE驻留和切换策略管理”特性的相关license授权并开启后，此参数配置才生效（特性编号：WSFD-106207，license部件编码：LKV2SPID01）。 |
| ENBRFSPIDX | 指示特征RFSP索引 | 可选必选说明：条件必选参数<br>参数含义：该参数用于设置将用户签约RFSP映射成SPID时所引用的RFSP索引，具体映射规则参见<br>[表2](#ZH-CN_MMLREF_0000001172345153__tab2)<br>前提条件：该参数在“ENBIND(eNodeB指示方式)”参数配置为“RFSP_ID(RFSP ID)”后生效。<br>数据来源：本端规划<br>取值范围：0~49<br>默认值：无<br>说明：该特征RFSP索引必须已经通过<br>[**ADD SPECRFSPVALUE**](../../RFSP管理/特征RFSP管理/特征RFSP取值范围管理/增加特征RFSP取值(ADD SPECRFSPVALUE)_26145534.md)<br>命令添加，且其“TYPE（类型）”为“ENODEB_IND（eNodeB指示）”。可执行<br>[**LST SPECRFSPVALUE**](../../RFSP管理/特征RFSP管理/特征RFSP取值范围管理/查询特征RFSP取值(LST SPECRFSPVALUE)_26305346.md)<br>进行查看。 |

## 操作的配置对象

- [S1模式接入控制配置（S1ACCAREALST）](configobject/UNC/20.15.2/S1ACCAREALST.md)

## 使用实例

增加一条S1模式接入控制参数记录，区域范围为其他，用户范围为SPECIAL_IMSIPRE，IMSI前缀为12345，控制类型为拒绝，原因值为EPS_SERVICE_NOT_ALLOWED：

ADD S1ACCAREALST: AREA=OTHER, SUBRANGE=SPECIAL_IMSIPRE, IMSIPRE="12345", CTRLTYPE=REJECT, CAUSE=EPS_SERVICE_NOT_ALLOWED;

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加S1模式接入控制配置（ADD-S1ACCAREALST）_72345153.md`
