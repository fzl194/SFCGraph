---
id: UNC@20.15.2@MMLCommand@ADD IUACCAREALST
type: MMLCommand
name: ADD IUACCAREALST（增加Iu模式区域漫游限制参数）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: IUACCAREALST
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
max_records: 2048
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 移动性管理
- 区域漫游限制管理
- Iu模式区域漫游限制参数
status: active
---

# ADD IUACCAREALST（增加Iu模式区域漫游限制参数）

## 功能

![](增加Iu模式区域漫游限制参数(ADD IUACCAREALST)_72345151.assets/notice_3.0-zh-cn_2.png)

- 执行该命令可能会导致用户接入异常，请谨慎操作。
- 参数（控制类型）：为防止误操作产生的业务影响，请确认命令中各参数取值合理有效。

**适用网元：SGSN**

此命令用于增加Iu模式区域漫游限制参数，根据用户当前所在的位置，控制是否允许进行漫游。

当针对不同的用户群在相应的区域群中设置对应的漫游控制策略时，需要执行此命令。

## 注意事项

- 此命令执行后立即生效。
- 此命令最大记录数为2048。
- 此命令配置后会根据用户当前所在的位置，控制是否允许进行漫游，对于已经接入的用户没有影响。
- 如果输入的AREAID在AREAGPMEM表中对应的记录IDTYPE选择了TA（可执行[**LST AREAGPMEM**](../区域群成员管理/查询区域群成员(LST AREAGPMEM)_72345143.md)查看），则不允许添加。
- 如果配置了多个用户群标识，且用户群标识分别关联了[**ADD SUBGPMEM**](../用户群成员管理/增加用户群成员(ADD SUBGPMEM)_26305374.md)和[**ADD MSISDNSUBGPMEM**](../MSISDN用户群成员管理/增加MSISDN用户群成员(ADD MSISDNSUBGPMEM)_72345167.md)，则系统优先使用IMSI进行匹配，对于同一用户，如果使用IMSI匹配成功则不会再使用MSISDN进行匹配。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| AREA | 区域范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定区域范围。<br>数据来源：整网规划<br>取值范围：<br>- “AG(区域组)”：表示该区域标识类型为区域组。<br>- “LA(指定位置区)”：表示该区域标识类型为指定位置区。<br>- “RA(指定路由区)”：表示该区域标识类型为指定路由区。<br>- “OTHER(其他)”：表示该区域标识类型为其他。<br>默认值：无<br>配置原则：本表中<br>“区域范围”<br>为<br>“OTHER(其他)”<br>的记录可以与<br>“区域范围”<br>为<br>“AG(区域组)”<br>的记录共存，也可以与<br>“区域范围”<br>为<br>“LA(指定位置区)”<br>或<br>“RA(指定路由区)”<br>的记录共存；但是<br>“区域范围”<br>为<br>“AG(区域组)”<br>的记录不能与<br>“区域范围”<br>为<br>“LA(指定位置区)”<br>或<br>“RA(指定路由区)”<br>的记录共存。<br>说明：- 区域范围表示进行接入控制所适用的位置区域。<br>- 区域范围按照粒度从粗到细分为以下几个级别：区域组，指定位置区，指定路由区，其他。<br>- 相同粒度区域范围的各记录的区域范围不能交迭。<br>- 使用时先按照位置区域查找记录，然后按照用户的IMSI查找是否存在对应记录，查找不到再使用较粗的区域粒度进行查找。<br>- 未配置在该表区域范围中的用户缺省允许接入。 |
| MCC | 移动国家码 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定移动国家代码。<br>前提条件：该参数在<br>“AREA(区域范围)”<br>参数设置为<br>“LA(位置区)”<br>或<br>“RA(路由区)”<br>时，才需要配置。<br>数据来源：整网规划<br>取值范围：3位的十进制数字<br>默认值：无 |
| MNC | 移动网号 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定移动网号。<br>前提条件：该参数在<br>“AREA(区域范围)”<br>参数设置为<br>“LA(位置区)”<br>或<br>“RA(路由区)”<br>时，才需要配置。<br>数据来源：整网规划<br>取值范围：2～3位的十进制数字<br>默认值：无 |
| LAC | 位置区域码 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定位置区域码。<br>前提条件：该参数在<br>“AREA(区域范围)”<br>参数设置为<br>“LA(位置区)”<br>或<br>“RA(路由区)”<br>时，才需要配置。<br>数据来源：整网规划<br>取值范围：0x0000～0xFFFF<br>默认值：无<br>说明：- 各记录的LAC区段不能交叉，但是同一个LAC区段可以配置多个IMSI记录。<br>- 各记录的IMSI不能重复，支持最长匹配的查询方式。<br>- 输入的起始IMSI和终止IMSI定义的IMSI号段范围不允许与其它记录定义的IMSI号段范围相互交叉、包含或重合。 |
| LACRANGE | 位置区域码范围 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定位置区域码范围。<br>前提条件：该参数在<br>“AREA(区域范围)”<br>参数设置为<br>“LA(位置区)”<br>时，才需要配置。<br>数据来源：整网规划<br>取值范围：0x0000～0xFFFF<br>默认值：无<br>配置原则：该参数的取值需要大于或等于<br>“LAC”<br>。<br>说明：- 该参数与“LAC”参数构成一个LAC区段，方便客户配置连续的位置区域。<br>- 如果不输入，表示配置单个LAC。 |
| RAC | 路由区域码 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定路由区域码。<br>前提条件：该参数在<br>“AREA(区域范围)”<br>参数设置为<br>“RA(路由区)”<br>时，才需要配置。<br>数据来源：整网规划<br>取值范围：0x00～0xFF<br>默认值：无<br>说明：- 各记录的RAC区段不能交叉，但是同一个RAC区段可以配置多种IMSI记录。<br>- 各记录的IMSI不能重复，支持最长匹配的查询方式。<br>- 输入的起始IMSI和终止IMSI定义的IMSI号段范围不允许与其它记录定义的IMSI号段范围相互交叉、包含或重合。 |
| RACRANGE | 路由区域码范围 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定路由区域码范围。<br>前提条件：该参数在<br>“AREA(区域范围)”<br>参数设置为<br>“RA(路由区)”<br>时，才需要配置。<br>数据来源：整网规划<br>取值范围：0x00～0xFF<br>默认值：无<br>配置原则：该参数的取值需要大于或等于<br>“RAC”<br>。<br>说明：- 该参数与“RAC”参数构成一个RAC区段，方便客户配置连续的路由区域。<br>- 如果不输入，表示配置单个RAC。 |
| AREAID | 区域群标识 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定用户的区域群标识。<br>前提条件：该参数在<br>“AREA(区域范围)”<br>参数设置为<br>“AG(区域组)”<br>时，才需要配置。<br>数据来源：整网规划<br>取值范围：1～50<br>配置原则：如果输入的<br>“AREAID”<br>在AREAGPMEM表中对应的记录<br>“IDTYPE”<br>选择了<br>“TA”<br>（可执行<br>[**LST AREAGPMEM**](../区域群成员管理/查询区域群成员(LST AREAGPMEM)_72345143.md)<br>查看），则不允许添加。<br>默认值：无<br>说明：该区域ID必须已经通过<br>[**ADD AREAGP**](../区域群管理/增加区域群(ADD AREAGP)_26145542.md)<br>命令添加成功，且在区域群成员表中的记录对应的IDTYPE只能为LA或RA。可执行<br>[**LST AREAGP**](../区域群管理/查询区域群(LST AREAGP)_72345141.md)<br>进行查看。 |
| SUBRANGE | 用户范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定用户范围。<br>数据来源：整网规划<br>取值范围：<br>- “ALL_USER(所有用户)”：表示用户范围为所有用户。<br>- “SPECIAL_IMSIPRE(指定IMSI前缀)”：表示该用户范围为指定IMSI前缀。<br>- “USER_GROUP(用户群)”：表示用户范围为用户群。<br>- “SPECIAL_IMSI_RANGE(指定IMSI范围)”：表示该用户范围为指定IMSI范围。<br>- “UE_TYPE(终端类型)”：保留，暂未实现。<br>默认值：无<br>配置原则：<br>- 当存在“用户范围”为“SPECIAL_IMSIPRE(指定IMSI前缀)”的记录时，不允许再添加“用户范围”为“SPECIAL_IMSI_RANGE(指定IMSI范围)”的记录。同理，当存在“用户范围”为“SPECIAL_IMSI_RANGE(指定IMSI范围) ”的记录时，不允许再添加“用户范围”为“SPECIAL_IMSIPRE(指定IMSI前缀)”的记录。<br>- 本表“用户范围”为“ALL_USER(所有用户)”的记录可以与“用户范围”为“USER_GROUP(用户群)”的记录共存，也可以与“用户范围”为“SPECIAL_IMSIPRE(指定IMSI前缀)”或“SPECIAL_IMSI_RANGE(指定IMSI范围)”的记录共存，但是“用户范围”为“USER_GROUP(用户群)”的记录，不能与“用户范围”为“SPECIAL_IMSIPRE(指定IMSI前缀)”或“SPECIAL_IMSI_RANGE(指定IMSI范围)”的记录共存。<br>- 当“区域范围”为“OTHER(其他)”时，“用户范围”只能是“SPECIAL_IMSIPRE(指定IMSI前缀)”，“SPECIAL_IMSI_RANGE(指定IMSI范围)”，“USER_GROUP(用户群)”或“UE_TYPE(终端类型)”。 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定用户的IMSI前缀。使用时按照IMSI最长匹配进行查询。<br>前提条件：该参数在<br>“SUBRANGE(用户范围)”<br>设置为<br>“SPECIAL_IMSIPRE(指定IMSI前缀)”<br>时，才需要配置。<br>数据来源：整网规划<br>取值范围：1～15位的十进制数字<br>默认值：无<br>说明：- 支持IMSI最长匹配的查询方式。<br>- 该参数在用户群成员管理配置中不能存在对应记录，可执行[**LST SUBGPMEM**](../用户群成员管理/查询用户群成员(LST SUBGPMEM)_26145564.md)进行查看。 |
| BEGIMSI | 起始IMSI | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定用户的起始IMSI。<br>前提条件：该参数在<br>“SUBRANGE(用户范围)”<br>设置为<br>“SPECIAL_IMSI_RANGE(指定IMSI范围)”<br>时，才需要配置。<br>数据来源：整网规划<br>取值范围：1～15位的十进制数字<br>默认值：无<br>配置原则：当起始IMSI与终止IMSI长度全为15位时，起始IMSI要小于等于终止IMSI，否则起始IMSI要小于终止IMSI。 |
| ENDIMSI | 终止IMSI | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定用户的终止IMSI。<br>前提条件：该参数在<br>“SUBRANGE(用户范围)”<br>设置为<br>“SPECIAL_IMSI_RANGE(指定IMSI范围)”<br>时，才需要配置。<br>数据来源：整网规划<br>取值范围：1～15位的十进制数字<br>默认值：无<br>配置原则：当终止IMSI与起始IMSI长度全为15位时，终止IMSI要大于等于起始IMSI，否则终止IMSI要大于起始IMSI。<br>说明：输入的起始IMSI必须小于或者等于终止IMSI。判断起始IMSI和终止IMSI大小的原则是：对于输入IMSI的长度小于系统规定IMSI长度时，将该IMSI补足0到规定长度后进行大小比较，且起始IMSI必须小于终止IMSI。只有输入IMSI长度等于系统规定长度时，起始IMSI才能等于终止IMSI。 对于系统规定IMSI长度为15的情况，请参考<br>[表1](#ZH-CN_MMLREF_0000001172345151__tab1)<br>。 |
| SUBID | 用户群标识 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定用户群标识。<br>前提条件：该参数在<br>“SUBRANGE(用户范围)”<br>参数设置为<br>“USER_GROUP(用户群)”<br>时，才需要配置。<br>数据来源：整网规划<br>取值范围：1～100<br>默认值：无<br>配置原则：<br>- 如果配置了多个用户群标识，且用户群标识分别关联了[**ADD SUBGPMEM**](../用户群成员管理/增加用户群成员(ADD SUBGPMEM)_26305374.md)和[**ADD MSISDNSUBGPMEM**](../MSISDN用户群成员管理/增加MSISDN用户群成员(ADD MSISDNSUBGPMEM)_72345167.md)，则系统优先使用IMSI进行匹配，对于同一用户，如果使用IMSI匹配成功则不会再使用MSISDN进行匹配。<br>说明：该参数需要在<br>[**ADD SUBGP**](../用户群管理/增加用户群(ADD SUBGP)_72225241.md)<br>中事先配置，可执行<br>[**LST SUBGP**](../用户群管理/查询用户群(LST SUBGP)_26145562.md)<br>进行查看。 |
| CTRLTYPE | 控制类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定控制类型。<br>数据来源：整网规划<br>取值范围：<br>- “ALLOW(允许)”：表示符合该规则的用户是允许接入。<br>- “REJECT(拒绝)”：表示符合该规则的用户是拒绝接入。<br>默认值：无<br>配置原则：当<br>“区域范围”<br>为<br>“OTHER(其他)”<br>或<br>“用户范围”<br>为<br>“ALL_USER(所有用户)”<br>时，<br>“控制类型”<br>只能是<br>“REJECT(REJECT)”<br>。 |
| CAUSE | 原因值 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定拒绝用户接入时使用的原因值。<br>前提条件：该参数在<br>“CTRLTYPE(控制类型)”<br>设置为<br>“REJECT(拒绝)”<br>时，才需要配置。<br>数据来源：整网规划<br>取值范围：<br>- “CUSTOMER_DEFINED(自定义)”：表示拒绝用户接入时使用的原因值为自定义。<br>- “GPRS_SERVICE_NOT_ALLOWED(GPRS服务被禁止)”：表示拒绝用户接入时使用的指定原因值为GPRS服务被禁止。<br>- “GPRS_NONGPRS_SRV_NOT_ALLOWED(GPRS和非GPRS服务都被禁止)”：表示拒绝用户接入时使用的原因值为GPRS和非GPRS服务都被禁止。<br>- “PLMN_NOT_ALLOWED(PLMN被禁止)”：表示拒绝用户接入时使用的原因值为PLMN被禁止。<br>- “LA_NOT_ALLOWED(本地区域被禁止)”：表示拒绝用户接入时使用的原因值为本地区域被禁止。<br>- “ROAMING_NOT_ALLOWED_IN_LA(本地漫游被禁止)”：表示拒绝用户接入时使用的原因值为本地漫游被禁止。<br>- “GPRS_SRV_NOT_ALLOWED_IN_PLMN(本PLMN内GPRS服务被禁止)”：表示拒绝用户接入时使用的原因值为本PLMN内GPRS服务被禁止。<br>- “NO_SUITABLE_CELLS_IN_LA(本地无合适小区)”：表示拒绝用户接入时使用的原因值为本地无合适单元。<br>默认值：<br>“NO_SUITABLE_CELLS_IN_LA(本地无合适小区)”<br>说明：附着或路由更新拒绝的原因值，请参考24008输入。 |
| SDCAUSE | 自定义原因值 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定自定义原因值。<br>前提条件：该参数在<br>“CAUSE(原因值)”<br>参数设置为<br>“CUSTOMER_DEFINED(自定义)”<br>时，才需要配置。<br>数据来源：整网规划<br>取值范围：1～254<br>默认值：无<br>说明：当原因值为自定义时显示，根据24008填写。如果需要拒绝用户接入时NAS消息的原因值。 |

## 操作的配置对象

- [Iu模式区域漫游限制参数（IUACCAREALST）](configobject/UNC/20.15.2/IUACCAREALST.md)

## 使用实例

1.增加一条Iu模式区域漫游限制参数记录，区域范围为区域组，区域群标识为1，用户范围为指定IMSI范围，起始IMSI为123456，终止IMSI为1234567，控制类型为拒绝，原因值为GPRS_SERVICE_NOT_ALLOWED：

ADD IUACCAREALST: AREA=AG, AREAID=1, SUBRANGE=SPECIAL_IMSI_RANGE, BEGIMSI="123456", ENDIMSI="1234567", CTRLTYPE=REJECT, CAUSE=GPRS_SERVICE_NOT_ALLOWED;

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加Iu模式区域漫游限制参数(ADD-IUACCAREALST)_72345151.md`
