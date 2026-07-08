---
id: UNC@20.15.2@MMLCommand@ADD SMACTCTRL
type: MMLCommand
name: ADD SMACTCTRL（增加激活过程控制参数）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: SMACTCTRL
command_category: 配置类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- 会话管理
- 激活过程管理
status: active
---

# ADD SMACTCTRL（增加激活过程控制参数）

## 功能

**适用网元：SGSN、MME**

该命令用于增加在PDP激活流程（ UNC 作为SGSN网元）和PDN连接建立流程（ UNC 作为MME网元）中使用签约数据匹配的纠正功能涉及到的相关参数。PDP激活包括UE发起的PDP上下文激活过程和GGSN发起的网络侧PDP上下文激活过程，不包括二次激活过程。PDN连接建立包括UE发起的ATTACH流程和UE请求的PDN连接建立流程。

当纠正所有用户激活请求中错误的APN时，需要执行此命令。

## 注意事项

- 该命令执行后立即生效。
- 该表最多可以输入1024条记录。
- 此配置涉及请求信息纠正功能特性（特性编号：WSFD- 106004，License部件编码：LKV2RINCOR02），执行命令请使用[**DSP LICENSE**](../../../../../../平台服务管理/操作维护/License管理/显示License(DSP LICENSE)_00360098.md)命令确认对应特性license是否得到授权，执行[**LST LICENSESWITCH**](../../../../../../平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md)命令确认特性开关状态为“ENABLE(打开)”。
- 当“用户范围”设置为“SPECIAL_USER(指定用户)”时，如果IMSI和UE请求的APNNI的组合同时匹配到多条记录，使用“UE请求的APNNI”优先级高的记录。例如用户999880000000001使用HUAWEI1.COM，在[表1](#ZH-CN_MMLREF_0000001126305472__tab1)所示场景下，匹配到记录1。
  *表1 示例1*

  | 记录 | 用户范围 | IMSI前缀 | UE请求的APNNI | APNNI |
  | --- | --- | --- | --- | --- |
  | 记录1 | “SPECIAL_USER(指定用户)” | 99988 | 指定APN | HUAWEI1.COM |
  | 记录2 | “SPECIAL_USER(指定用户)” | 999880000 | 非空APN | - |
  | 记录3 | “SPECIAL_USER(指定用户)” | 999880000000001 | 所有APN | - |

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定启用功能的用户范围。<br>数据来源：整网规划<br>取值范围：<br>- “ALL_USER(所有用户)”<br>- “SPECIAL_USER(指定用户)”<br>- “SPECIAL_UETYPE(指定终端类型)”<br>默认值：无<br>配置原则：<br>- “用户范围”+“IMSI前缀”+“请求APNNI”不能重复。<br>- “用户范围”+“终端类型”+“请求APNNI”不能重复。 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定IMSI前缀。<br>前提条件：该参数在<br>“用户范围”<br>参数设置为<br>“SPECIAL_USER(指定用户)”<br>时，才需要配置。<br>数据来源：整网规划<br>取值范围：5~15位数字<br>默认值：无<br>配置原则：使用时按照IMSI最长匹配进行查询，相同IMSI前缀的原始原因值配置不能相同。 |
| UETYPE | 终端类型 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定终端类型。<br>UNC<br>需要为这些类型终端设置特定请求信息纠正策略。<br>前提条件：该参数在<br>“用户范围”<br>参数设置为<br>“SPECIAL_UETYPE(指定终端类型)”<br>时，才需要配置。<br>数据来源：整网规划<br>取值范围：<br>- “ANDROID(Android)”<br>- “BLACKBERRY(Black Berry)”<br>- “IOS(iOS)”<br>- “WINDOWS(Windows)”<br>- “CUSTOM_TYPE_1(自定义类型1)”<br>- “CUSTOM_TYPE_2(自定义类型2)”<br>- “CUSTOM_TYPE_3(自定义类型3)”<br>- “CUSTOM_TYPE_4(自定义类型4)”<br>- “CUSTOM_TYPE_5(自定义类型5)”<br>- “CUSTOM_TYPE_6(自定义类型6)”<br>- “CUSTOM_TYPE_7(自定义类型7)”<br>- “CUSTOM_TYPE_8(自定义类型8)”<br>- “CUSTOM_TYPE_9(自定义类型9)”<br>- “CUSTOM_TYPE_10(自定义类型10)”<br>- “CUSTOM_TYPE_11(自定义类型11)”<br>- “CUSTOM_TYPE_12(自定义类型12)”<br>默认值：无<br>说明：“终端类型”<br>需要在<br>[**ADD SMACTIMEILIB**](增加IMEI库记录（ADD SMACTIMEILIB）_26305474.md)<br>中配置。 |
| APNTYPE | UE请求的APNNI | 可选必选说明：必选参数<br>参数含义：该参数用于指定请求APNNI类型。<br>数据来源：整网规划<br>取值范围：<br>- “ALL_APN(所有APN)”<br>- “NULL_APN(空APN)”<br>- “NOT_NULL_APN(非空APN)”<br>- “SPECIAL_APN(指定APN)”<br>默认值：无<br>配置原则：<br>- 请求APNNI为空时，选择“NULL_APN”。<br>- 请求APNNI为非空时，选择“NOT_NULL_APN”。<br>- 请求APNNI为指定APN时，选择“SPECIAL_APN”。<br>- 请求APNNI包括空APN和非空APN时，选择“ALL_APN”。<br>- 优先级关系：“SPECIAL_APN(指定APN)”=“NULL_APN(空APN)”>“NOT_NULL_APN(非空APN)”>“ALL_APN(所有APN)”。 |
| APNNI | APNNI | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定APN网络标识。<br>前提条件：该参数在<br>“APNTYPE”<br>参数设置为<br>“SPECIAL_APN(指定APN)”<br>时，才需要配置。<br>数据来源：整网规划<br>取值范围：1~62位字符串<br>默认值：无<br>配置原则：<br>- APN网络标识地址由一个或多个LABEL构成，各LABEL间用“.”间隔。<br>- 每个LABEL的构成字符只能是字母A～Z或a～z、数字0～9和中划线“-”。<br>- APN网络标识地址不能以“rac”、“lac”、“sgsn”或“rnc”开头，不能以“.gprs”结尾。 |
| POLICY | 处理策略 | 可选必选说明：可选参数<br>参数含义：该参数用于控制整体策略，是直接拒绝激活，还是在签约数据匹配失败后进行纠正处理。<br>数据来源：整网规划<br>取值范围：<br>- “REJECT(直接拒绝)”<br>- “MATCH_FAIL_NOTCORRECT(签约数据匹配失败后不进行纠正)”<br>- “MATCH_FAIL_CORRECT(签约数据匹配失败后进行纠正)”<br>默认值：<br>“MATCH_FAIL_CORRECT(签约数据匹配失败后进行纠正)”<br>配置原则：<br>- 禁止UE使用签约数据进行激活选择“REJECT”。<br>- 如果签约数据匹配失败后不进行纠正选择“MATCH_FAIL_NOTCORRECT”。<br>- 如果签约数据匹配失败后进行纠正则选择“MATCH_FAIL_CORRECT”。 |
| CORRPDPTYPE | PDP Type纠正 | 可选必选说明：条件可选参数<br>参数含义：该参数用于控制PDP Type是否纠正。<br>前提条件：该参数在<br>“POLICY”<br>参数设置为<br>“MATCH_FAIL_CORRECT(签约数据匹配失败后进行纠正)”<br>时，才需要配置。<br>数据来源：整网规划<br>取值范围：<br>- “NO(否)”<br>- “YES(是)”<br>默认值：<br>“NO(否)”<br>配置原则：<br>- 如果签约数据匹配失败后进行PDP Type纠正，选择“YES”。<br>- 如果签约数据匹配失败后不进行PDP Type纠正，选择“NO”。 |
| CORRTIP | PDP Address纠正 | 可选必选说明：条件可选参数<br>参数含义：该参数用于控制PDP Adrress是否纠正。<br>前提条件：该参数在<br>“POLICY”<br>参数设置为<br>“MATCH_FAIL_CORRECT(签约数据匹配失败后进行纠正)”<br>时，才需要配置。<br>数据来源：整网规划<br>取值范围：<br>- “NO(否)”<br>- “YES(是)”<br>默认值：<br>“NO(否)”<br>配置原则：<br>- 如果签约数据匹配失败后进行PDP Address纠正，选择“YES”。<br>- 如果签约数据匹配失败后不进行PDP Address纠正，选择“NO”。 |
| SINGLESUB | 单组签约数据 | 可选必选说明：条件可选参数<br>参数含义：该参数用于控制单组签约数据匹配失败后的APN纠正方式。<br>前提条件：该参数在<br>“POLICY”<br>参数设置为<br>“MATCH_FAIL_CORRECT(签约数据匹配失败后进行纠正)”<br>时，才需要配置。<br>数据来源：整网规划<br>取值范围：<br>- “NO(不纠正)”<br>- “SELECT_LOC_APN_ONLY(只选Local APNNI)”<br>- “SELECT_LOC_APN_FIRST(优选Local APNNI)”<br>默认值：<br>“NO(不纠正)”<br>配置原则：<br>- 如果单组签约数据匹配失败后不进行纠正，选择“NO”。<br>- 如果单组签约数据匹配失败后只选择Local APNNI进行纠正，选择“SELECT_LOC_APN_ONLY”。<br>- 如果单组签约数据匹配失败后优选Local APNNI进行纠正，选择“SELECT_LOC_APN_FIRST”。 |
| CORRMAPNSUB | 多组签约数据 | 可选必选说明：条件可选参数<br>参数含义：该参数用于控制多组签约数据匹配失败后的APN纠正方式。<br>前提条件：该参数在<br>“POLICY”<br>参数设置为<br>“MATCH_FAIL_CORRECT(签约数据匹配失败后进行纠正)”<br>时，才需要配置。<br>数据来源：整网规划<br>取值范围：<br>- “NO(不纠正)”<br>- “SELECT_LOC_APN_ONLY(只选Local APNNI)”<br>- “SELECT_LOC_APN_FIRST(优选Local APNNI)”<br>- “SELECT_DEF_APN_FIRST(优选Default APNNI)”<br>默认值：<br>“NO(不纠正)”<br>配置原则：<br>- 如果多组签约数据匹配失败后不进行纠正，选择“NO”。<br>- 如果多组签约数据匹配失败后只选择Local APNNI进行纠正，则查看签约数据列表Sublist中是否有Local APN的签约数据。如果有，选择该组签约数据。如果没有，则拒绝PDP/PDN激活请求。<br>- 如果多组签约数据匹配失败后优选Local APNNI进行纠正，则查看签约数据列表Sublist中是否存在Local APN的签约数据。如果有，选择该组签约数据。如果没有，选择Sublist中的Context ID最小的一组签约数据。<br>- 如果多组签约数据匹配失败后优选Default APNNI进行纠正，则查看签约数据列表Sublist中是否存在Default APNNI的签约数据。如果有，选择该组签约数据。如果没有，按“优选Local APNNI”进行处理。<br>说明：“优选Default APNNI”选项仅对E-UTRAN/NB-IoT接入用户生效，如果用户是GERAN接入用户或U-TRAN接入用户，按照“优选Local APNNI”进行处理。 |
| WILDCARDPLCY | 野卡签约数据策略 | 可选必选说明：条件可选参数<br>参数含义：该参数用于控制是否禁止UE使用野卡签约数据进行激活，或者使用其它定制的野卡签约数据策略。<br>前提条件：该参数在<br>“POLICY”<br>参数不设置为<br>“REJECT(直接拒绝)”<br>时，才需要配置。<br>数据来源：整网规划<br>取值范围：<br>- “STANDARD(标准)”<br>- “REJECT(拒绝)”<br>- “CUSTOMIZATION(定制)”<br>默认值：<br>“STANDARD(标准)”<br>配置原则：<br>- 野卡签约数据策略为标准的选择“STANDARD”。<br>- 野卡签约数据策略为直接拒绝的选择“REJECT”。<br>- 野卡签约数据策略为定制的选择“CUSTOMIZATION”。 |
| APNNIREQ | 请求APNNI的处理策略 | 可选必选说明：条件可选参数<br>参数含义：该参数用于描述UE请求了APNNI，又匹配到野卡签约数据后的处理策略。<br>前提条件：该参数在<br>“WILDCARDPLCY”<br>参数设置为<br>“CUSTOMIZATION(定制)”<br>时，才需要配置。<br>数据来源：整网规划<br>取值范围：<br>- “STANDARD_MODEL(标准方式)”<br>- “IGNORE(直接忽略)”<br>- “IGNORE_DNS_FAIL(DNS解析失败后忽略)”<br>默认值：<br>“STANDARD_MODEL(标准方式)”<br>配置原则：<br>- 如果请求APNNI的处理策略为按标准方式的选择“STANDARD_MODEL”。<br>- 如果请求APNNI的处理策略为直接忽略UE请求的APNNI，则选择“IGNORE”。<br>- 如果DNS解析失败后使用Local APNNI选择“IGNORE_DNS_FAIL”。 |
| WILDCARD | 优选非野卡签约数据 | 可选必选说明：条件可选参数<br>参数含义：该参数用于对同时存在野卡和非野卡签约数据的用户，是否优先选择非野卡签约数据进行激活以及选择非野卡时的选择策略。<br>前提条件：该参数在<br>“WILDCARDPLCY”<br>参数设置为<br>“CUSTOMIZATION(定制)”<br>时，才需要配置。<br>数据来源：整网规划<br>取值范围：<br>- “NO(否)”<br>- “SELECT_LOC_APN_ONLY(只选Local APNNI)”<br>- “SELECT_LOC_APN_FIRST(优选Local APNNI)”<br>- “SELECT_DEF_APN_FIRST(优选Default APNNI)”<br>默认值：<br>“NO(否)”<br>配置原则：<br>- 不是优选非野卡签约数据的选择“NO”。<br>- 如果选择非野卡时的选择策略为只选Local APNNI，在用户签约多个APN，并且包含野卡的场景下，当本地配置Local APNNI在签约数据列表中，就选择Local APNNI进行激活，当本地没有配置Local APNNI或者Local APNNI不在签约数据列表中，如果用户请求携带了APN，使用请求的APN进行激活，否则拒绝激活。<br>- 如果选择非野卡时的选择策略为优选Local APNNI，在用户签约多个APN，并且包含野卡的场景下，当本地配置Local APNNI在签约数据列表中，使用Local APNNI进行激活，若本地没有配置Local APNNI或者Local APNNI不在签约数据列表中，则选择签约数据列表中Context ID最小的一组签约数据进行激活。<br>- 如果选择非野卡时的选择策略为优选Default APNNI，在根据PDP TYPE匹配到多组签约数据，并且包含野卡的场景下，当签约的Default APNNI在匹配的签约数据列表中，使用Default APNNI进行激活，若Default APNNI不在匹配的签约数据列表中，则按照“优选Local APNNI”的处理原则进行激活。<br>说明：“优选Default APNNI”选项仅对E-UTRAN/NB-IoT接入用户生效，如果用户是GERAN接入用户或U-TRAN接入用户，按照“优选Local APNNI”进行处理。 |
| MINCID | 使用Context ID最小的非野卡签约数据 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定当<br>“优选非野卡签约数据”<br>为<br>“NO(否)”<br>时，使用UE请求的APNNI查询DNS失败后，如果未配置Local APNNI，是否重新匹配Context ID最小的非野卡签约数据。<br>前提条件：该参数在<br>“请求APNNI的处理策略”<br>参数配置为<br>“IGNORE_DNS_FAIL(DNS解析失败后忽略)”<br>后生效。<br>数据来源：全网规划<br>取值范围：<br>- “NO(否)”<br>- “YES(是)”<br>默认值：<br>“NO(否)” |
| PUBLICAPN | 只允许使用公共APNNI | 可选必选说明：条件可选参数<br>参数含义：该参数用于显示使用野卡的用户，是否只能使用<br>[**ADD PUBLICAPNNI**](../公共APNNI管理/增加公共APN NI配置(ADD PUBLICAPNNI)_26145682.md)<br>命令中添加的APNNI。<br>前提条件：该参数在<br>“WILDCARDPLCY”<br>参数设置为<br>“CUSTOMIZATION(定制)”<br>时，才需要配置。<br>数据来源：整网规划<br>取值范围：<br>- “NO(否)”<br>- “YES(是)”<br>默认值：<br>“NO(否)”<br>配置原则：<br>- 只允许使用公共APNNI的选择“YES”。<br>- 不只允许使用公共APNNI的选择“NO”。 |
| WCLIMIT | 限制野卡激活数目 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定对于野卡签约用户，是否要限制其使用野卡进行激活的PDP个数。<br>前提条件：该参数在<br>“WILDCARDPLCY”<br>参数设置为<br>“CUSTOMIZATION(定制)”<br>时，才需要配置。<br>数据来源：整网规划<br>取值范围：<br>- “NO(否)”<br>- “YES(是)”<br>默认值：<br>“NO(否)”<br>配置原则：<br>- 限制野卡激活数目的选择“YES”。<br>- 不限制野卡激活数目的选择“NO”。 |
| PDPTYPE | PDP/PDN Type策略 | 可选必选说明：条件可选参数<br>参数含义：该参数主要用于签约数据是IPv4/IPv6的场景下，如果必须使用单栈PDP地址时的优选策略。<br>前提条件：该参数在<br>“POLICY”<br>参数不设置为<br>“REJECT(直接拒绝)”<br>时，才需要配置。<br>取值范围：<br>- “IPv4(IPv4)”<br>- “IPv6(IPv6)”<br>默认值：<br>“IPv4(IPv4)”<br>配置原则：<br>- PDP/PDN Type策略为IPV4的选择“IPV4”。<br>- PDP/PDN Type策略为IPV6的选择“IPV6”。 |
| APNCORRCHRRPT | APN纠错CHR上报 | 可选必选说明：条件可选参数<br>参数含义：该参数主要用于激活请求信息纠正是否上报成CHR。<br>前提条件：该参数在<br>“POLICY”<br>参数设置为<br>“MATCH_FAIL_CORRECT(签约数据匹配失败后进行纠正)”<br>时，才需要配置。<br>取值范围：<br>- “NO(否)”<br>- “YES(是)”<br>默认值：<br>“NO(否)” |
| RQDSUBAPNNI | 要求签约APNNI | 可选必选说明：条件可选<br>前提条件：<br>“单组签约数据”<br>参数设置为<br>“只选Local APNNI”<br>或者<br>“优选Local APNNI”<br>时，或<br>“多组签约数据”<br>参数设置为<br>“只选Local APNNI”<br>或者<br>“优选Local APNNI”<br>或者<br>“优选Default APNNI”<br>时，或<br>“是否启用本地APNNI列表匹配策略”<br>参数设置为<br>“YES”<br>时，本参数生效。<br>参数含义：该参数用于控制只有HLR签约了本参数对应的APN时，Local APNNI才允许使用。未配置代表该参数功能不生效。该参数只针对用户接入2G/3G时生效。<br>取值范围：0~62位字符串<br>默认值：无<br>配置原则：<br>- ·APN网络标识地址由一个或多个LABEL构成，各LABEL间用“.”间隔。<br>- ·每个LABEL的构成字符只能是字母A～Z或a～z、数字0～9和中划线“-”。<br>- ·APN网络标识地址不能以“rac”、“lac”、“sgsn”或“rnc”开头，不能以“.gprs”结尾。 |
| FALLBACKAPNNI | 回落APNNI | 可选必选说明：条件可选<br>前提条件：<br>“单组签约数据”<br>参数设置为<br>“只选Local APNNI”<br>或者<br>“优选Local APNNI”<br>时，或<br>“多组签约数据”<br>参数设置为<br>“只选Local APNNI”<br>或者<br>“优选Local APNNI”<br>或者<br>“优选Default APNNI”<br>时，或<br>“是否启用本地APNNI列表匹配策略”<br>参数设置为<br>“YES”<br>时，本参数生效。<br>参数含义：该参数用于控制在APN纠错场景下，尝试纠正为Local APNNI时，如果Local APNNI未签约，则使用回落APNNI作为用户激活APNNI。未配置代表该参数功能不生效。该参数只针对用户接入2G/3G时生效。<br>取值范围：0~62位字符串<br>默认值：无<br>配置原则：<br>- ·APN网络标识地址由一个或多个LABEL构成，各LABEL间用“.”间隔。<br>- ·每个LABEL的构成字符只能是字母A～Z或a～z、数字0～9和中划线“-”。<br>- ·APN网络标识地址不能以“rac”、“lac”、“sgsn”或“rnc”开头，不能以“.gprs”结尾。 |
| REJPLYEXT | 是否启用扩展拒绝策略 | 可选必选说明：条件可选参数<br>前提条件：该参数在“处理策略”设置为“REJECT(直接拒绝)”后生效。<br>参数含义：该参数用于控制是否开启扩展拒绝策略。参数设置为“YES”时对于“受限APN是否允许接入”将由Gb模式扩展拒绝流程、Iu模式扩展拒绝流程、S1模式扩展拒绝流程参数中的选项控制，同时携带原因值#66 requested apn not supported in current rat and plmn combination。<br>说明：当启用扩展拒绝策略时，Inter TAU、Inter RAU、Inter HO、Inter SRNS Relocation流程中的新侧会对用户使用中的全部APN进行匹配。<br>数据来源：本端规划<br>取值范围：<br>- “YES(是)”<br>- “NO(否)”<br>默认值：“NO(否)” |
| REJPROEXT_GB | Gb模式扩展拒绝流程 | 可选必选说明：条件可选参数<br>前提条件：该参数在“是否启用扩展拒绝策略”设置为“YES”后生效。<br>参数含义：该参数用于控制开启扩展拒绝策略时，Gb模式中需要拒绝的流程。<br>数据来源：本端规划<br>取值范围：<br>- “ACTPDP(PDP Context Activation)”<br>- “INTER_RAU(Inter RAU)”<br>- “RESERVE1(RESERVE1)”<br>- “RESERVE2(RESERVE2)”<br>- “RESERVE3(RESERVE3)”<br>- “RESERVE4(RESERVE4)”<br>默认值：“ACTPDP-1”、“INTER_RAU-1”<br>配置原则：<br>- 选中的流程会在匹配到该条件时被拒绝接入。<br>- 未选中的流程则会在匹配到该条件时被允许接入。<br>- 未列出的流程不受该配置影响。 |
| REJPROEXT_IU | Iu模式扩展拒绝流程 | 可选必选说明：条件可选参数<br>前提条件：该参数在“是否启用扩展拒绝策略”设置为“YES”后生效。<br>参数含义：该参数用于控制开启扩展拒绝策略时，Iu模式中需要拒绝的流程。<br>数据来源：本端规划<br>取值范围：<br>- “ACTPDP(PDP Context Activation)”<br>- “INTER_RAU(Inter RAU)”<br>- “INTER_SRNS_RELOCATION(Inter SRNS Relocation)”<br>- “RESERVE1(RESERVE1)”<br>- “RESERVE2(RESERVE2)”<br>- “RESERVE3(RESERVE3)”<br>- “RESERVE4(RESERVE4)”<br>默认值：“ACTPDP-1”、“INTER_RAU-1”、“INTER_SRNS_RELOCATION-1”<br>配置原则：<br>- 选中的流程会在匹配到该条件时被拒绝接入。<br>- 未选中的流程则会在匹配到该条件时被允许接入。<br>- 未列出的流程不受该配置影响。 |
| REJPROEXT_S1 | S1模式扩展拒绝流程 | 可选必选说明：条件可选参数<br>前提条件：该参数在“是否启用扩展拒绝策略”设置为“YES”后生效。<br>参数含义：该参数用于控制开启扩展拒绝策略时，S1模式中需要拒绝的流程。<br>数据来源：本端规划<br>取值范围：<br>- “ATTACH(Attach)”<br>- “PDNCON(UE Requested PDN Connectivity)”<br>- “INTER_TAU(Inter TAU)”<br>- “INTER_HO(Inter HO)”<br>- “RESERVE1(RESERVE1)”<br>- “RESERVE2(RESERVE2)”<br>- “RESERVE3(RESERVE3)”<br>- “RESERVE4(RESERVE4)”<br>默认值：“ATTACH-1”、“PDNCON-1”、“INTER_TAU-1”、“INTER_HO-1”<br>配置原则：<br>- 选中的流程会在匹配到该条件时被拒绝接入。<br>- 未选中的流程则会在匹配到该条件时被允许接入。<br>- 未列出的流程不受该配置影响。 |
| APNNILSTPLY | 是否启用定制APN纠正策略 | 可选必选说明：可选参数<br>参数含义：该参数用于控制是否启用定制APN纠正策略。<br>数据来源：本端规划<br>取值范围：<br>- “NO(否)”<br>- “YES(是)”<br>默认值：<br>“NO(否)”<br>配置原则：<br>- 该参数只针对用户接入2G/3G时生效。<br>- 该参数只适用于GPRS签约，对于EPS签约不生效。<br>- 当定制APN纠正策略的上述两个条件满足之后，单签约APN纠正和多签约APN纠正将失效。具体详见**WSFD-106004请求信息纠正功能**的“**定制APN纠正**”章节说明。 |
| APNNIGRPID | 本地APNNI组号 | 可选必选说明：条件必选参数<br>前提条件:本参数在<br>“是否启用定制APN纠正策略”<br>参数配置为<br>“YES(是)”<br>后生效。<br>参数含义：该参数用于设置定制APN纠正策略的本地APNNI组号。<br>数据来源：本端规划<br>取值范围：0～127<br>系统初始设置值：无<br>配置原则：组号需要引用<br>**[ADD LOCALAPNNIGP](../本地APNNI组管理/增加本地APNNI组(ADD LOCALAPNNIGP)_16438089.md)**<br>命令中已配置的组号。 |

## 操作的配置对象

- [激活过程控制参数（SMACTCTRL）](configobject/UNC/20.15.2/SMACTCTRL.md)

## 使用实例

增加一条记录， “IMSI前缀” 为 “123007551111111” ， “APNNI” 为huawei.com， “处理策略” 为 “REJECT(直接拒绝)” 。

```
ADD SMACTCTRL: SUBRANGE=SPECIAL_USER, IMSIPRE="123007551111111", APNTYPE=SPECIAL_APN, APNNI="huawei.com", POLICY=REJECT;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加激活过程控制参数（ADD-SMACTCTRL）_26305472.md`
