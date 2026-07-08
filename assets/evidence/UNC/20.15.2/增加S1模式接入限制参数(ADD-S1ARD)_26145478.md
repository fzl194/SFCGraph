# 增加S1模式接入限制参数(ADD S1ARD)

- [命令功能](#ZH-CN_MMLREF_0000001126145478__1.3.1.1)
- [注意事项](#ZH-CN_MMLREF_0000001126145478__1.3.2.1)
- [本地用户权限](#ZH-CN_MMLREF_0000001126145478__1.3.3.1)
- [网管用户权限](#ZH-CN_MMLREF_0000001126145478__1.3.4.1)
- [参数说明](#ZH-CN_MMLREF_0000001126145478__1.3.5.1)
- [使用实例](#ZH-CN_MMLREF_0000001126145478__1.3.6.1)
- [参考信息](#ZH-CN_MMLREF_0000001126145478__1.3.7.1)

#### [命令功能](#ZH-CN_MMLREF_0000001126145478)

**适用网元：MME**

该命令用于增加S1模式接入限制参数。该命令先根据IMSI号段将用户进行分类，再对每一类用户按照用户签约的ARD信息、签约的APN信息进行区分而控制用户接入E-UTRAN网络。

该命令适用于以下场景。若运营商希望拒绝某个号段接入E-UTRAN系统，则可以启用根据签约ARD控制用户接入特性；若运营商希望控制某类用户是否允许接入E-UTRAN，但HLR/HSS不支持ARD时，则可以启用根据签约APN控制用户接入特性。

#### [注意事项](#ZH-CN_MMLREF_0000001126145478)

- 本表的最大记录数为1024。
- 当本表记录中存在用户的IMSI对应的IMSI前缀或者所在的IMSI范围，且用户的属性（APNNI）与S1ARD配置的属性匹配时，按照该配置的控制类型（CTRLTYPE）对用户接入进行控制。
- 当本表记录中存在用户的IMSI对应的IMSI前缀或者所在的IMSI范围，且用户的属性（APNNI）与S1ARD配置的属性均不匹配时，按照与该配置相反的控制类型（CTRLTYPE）对用户接入进行控制。
- 当本表记录中不存在用户的IMSI对应的IMSI前缀或者所在的IMSI范围时，不限制用户接入。
- 此配置涉及用户接入控制功能特性（特性编号：WSFD-106003，License部件编码：LKV2ARD02），执行命令请使用[**DSP LICENSE**](../../../../../../平台服务管理/操作维护/License管理/显示License(DSP LICENSE)_00360098.md)命令确认对应特性license是否得到授权，执行[**LST LICENSESWITCH**](../../../../../../平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md)命令确认特性开关状态为“ENABLE(打开)”。
- 当该配置增加上百条记录时，对系统性能影响较大。

#### [本地用户权限](#ZH-CN_MMLREF_0000001126145478)

manage-ug；system-ug

#### [网管用户权限](#ZH-CN_MMLREF_0000001126145478)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_MMLREF_0000001126145478)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定用户范围。<br>数据来源：整网规划<br>取值范围：<br>- “ALL_USER(所有用户)”：表示该指定用户范围为所有用户。<br>- “SPECIAL_IMSIPRE(指定IMSI前缀)”：表示该用户范围为指定IMSI前缀。<br>- “SPECIAL_IMSI_RANGE(指定IMSI范围)”：表示该用户范围为指定IMSI范围。<br>默认值：无<br>配置原则：当存在<br>“用户范围”<br>为<br>“SPECIAL_IMSIPRE(指定IMSI前缀)”<br>的记录时，不允许再添加<br>“用户范围”<br>为<br>“SPECIAL_IMSI_RANGE(指定IMSI范围)”<br>的记录。同理，当存在<br>“用户范围”<br>为<br>“SPECIAL_IMSI_RANGE(指定IMSI范围)”<br>的记录时，不允许再添加<br>“用户范围”<br>为<br>“SPECIAL_IMSIPRE(指定IMSI前缀)”<br>的记录。<br>说明：匹配本表记录中的用户范围时，系统首先会匹配<br>“SPECIAL_IMSIPRE(指定IMSI前缀)”<br>或<br>“SPECIAL_IMSI_RANGE(指定IMSI范围)”<br>的记录，如果没有符合的记录，才会匹配<br>“ALL_USER(所有用户)”<br>的用户范围。 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定IMSI前缀。使用时按照IMSI最长匹配进行查询。<br>前提条件：该参数在<br>“SUBRANGE（用户范围）”<br>设置为<br>“SPECIAL_IMSIPRE(指定IMSI前缀)”<br>时生效。<br>数据来源：整网规划<br>取值范围：1～15位数字<br>默认值：无 |
| BEGIMSI | 起始IMSI | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定用户的起始IMSI。<br>前提条件：该参数在<br>“SUBRANGE(用户范围)”<br>设置为<br>“SPECIAL_IMSI_RANGE(指定IMSI范围)”<br>时生效。<br>数据来源：整网规划<br>取值范围：1～15位数字<br>默认值：无<br>配置原则：当<br>“起始IMSI”<br>与<br>“终止IMSI”<br>长度全为15位时，<br>“起始IMSI”<br>要小于等于<br>“终止IMSI”<br>，否则<br>“起始IMSI”<br>要小于<br>“终止IMSI”<br>。 |
| ENDIMSI | 终止IMSI | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定用户的终止IMSI。<br>前提条件：该参数在<br>“SUBRANGE(用户范围)”<br>设置为<br>“SPECIAL_IMSI_RANGE(指定IMSI范围)”<br>时生效。<br>数据来源：整网规划<br>取值范围：1～15位数字<br>默认值：无<br>配置原则：参见<br>[参考信息](#ZH-CN_MMLREF_0000001126145478__re1)<br>。 |
| APNNI | APNNI | 可选必选说明：可选参数<br>参数含义：该参数用于配置指定APNNI。<br>数据来源：整网规划<br>取值范围：1～62位字符串<br>默认值：<br>“*”<br>配置原则：<br>- APN网络标识地址由一个或多个LABEL构成，各LABEL间用“.”间隔。<br>- 每个LABEL的构成字符只能是字母A～Z或a～z、数字0～9和中划线“-”，字母不区分大小写。<br>- APN网络标识地址不能以“rac”、“lac”、“sgsn”或“rnc”开头，不能以“.gprs”结尾。<br>说明：如果APNNI配置为<br>“*”<br>，表示该记录适用于所有的APNNI。 |
| ARD | 启用签约ARD | 可选必选说明：可选参数<br>参数含义：该参数用于指定是否启用签约ARD。<br>数据来源：整网规划<br>取值范围：<br>- “NO(否)”<br>- “YES(是)”<br>默认值：<br>“NO(否)”<br>配置原则：<br>- 不启用签约ARD时，该参数设置为“NO(否)”；启用签约ARD时，该参数设置为“YES(是)”。<br>- 不建议同时使用签约ARD功能与签约APN NI功能。 |
| CTRLTYPE | 控制类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定是否允许用户接入。<br>数据来源：整网规划<br>取值范围：<br>- “ALLOW(允许)”<br>- “REJECT(拒绝)”<br>默认值：无<br>配置原则：当只使用ARD的功能时，该参数建议设置为<br>“ALLOW(允许)”<br>，以防止受到APNNI默认值的影响。 |
| CAUSE | 原因值 | 可选必选说明：可选参数<br>参数含义：该参数用于指定拒绝用户接入时使用的原因值。<br>数据来源：整网规划<br>取值范围：<br>- “CUSTOMER_DEFINED(自定义)”<br>- “EPS_SERVICE_NOT_ALLOWED(EPS_SERVICE_NOT_ALLOWED)”<br>- “EPS_NONEPS_SRV_NOT_ALLOWED(EPS_NONEPS_SRV_NOT_ALLOWED)”<br>- “PLMN_NOT_ALLOWED(PLMN_NOT_ALLOWED)”：<br>- “TA_NOT_ALLOWED(TA_NOT_ALLOWED)”<br>- “ROAMING_NOT_ALLOWED_IN_TA(ROAMING_NOT_ALLOWED_IN_TA)”<br>- “EPS_SRV_NOT_ALLOWED_IN_PLMN(EPS_SRV_NOT_ALLOWED_IN_PLMN)”<br>- “NO_SUITABLE_CELLS_IN_TA(NO_SUITABLE_CELLS_IN_TA)”<br>默认值：<br>“NO_SUITABLE_CELLS_IN_TA(NO_SUITABLE_CELLS_IN_TA)”<br>说明：附着或路由更新拒绝的原因值，请参考3GPP TS 24.301输入。 |
| SDCAUSE | 自定义原因值 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定自定义原因值。<br>前提条件：该参数在<br>“CAUSE(原因值)”<br>设置为<br>“CUSTOMER_DEFINED(自定义)”<br>时生效。<br>数据来源：整网规划<br>取值范围：1～254<br>默认值：无<br>说明：当原因值为自定义时，根据3GPP TS 24.301填写。 |

#### [使用实例](#ZH-CN_MMLREF_0000001126145478)

1. 增加一条S1模式接入限制参数记录，用户范围为ALL_USER，控制类型为拒绝，原因值为自定义，自定义原因值为22：
  ADD S1ARD: SUBRANGE=ALL_USER, CTRLTYPE=REJECT, CAUSE=CUSTOMER_DEFINED, SDCAUSE=22;
2. 增加一条S1模式接入限制参数记录，用户范围为SPECIAL_IMSIPRE，IMSIPRE为123456，控制类型为拒绝，原因值为自定义，自定义原因值为22：
  ADD S1ARD: SUBRANGE=SPECIAL_IMSIPRE, IMSIPRE="123456", CTRLTYPE=REJECT, CAUSE=CUSTOMER_DEFINED, SDCAUSE=22;

#### [参考信息](#ZH-CN_MMLREF_0000001126145478)

- 输入的起始IMSI必须小于或者等于终止IMSI。判断起始IMSI和终止IMSI大小的原则是：对于输入IMSI的长度小于系统规定IMSI长度时，将该IMSI补足0到规定长度后进行大小比较，且起始IMSI必须小于终止IMSI。只有输入IMSI长度等于系统规定长度时，起始IMSI才能等于终止IMSI。 对于系统规定IMSI长度为15的情况，如[表1](#ZH-CN_MMLREF_0000001126145478__tab1)所示：
  *表1 IMSI限定范围*

  | 起始IMSI | 终止IMSI | 实际限定IMSI范围 |
  | --- | --- | --- |
  | 123002666 | 123002 | 增加记录失败，起始IMSI大于终止IMSI |
  | 123002 | 123002666 | 123002000000000～123002666000000，即区间[123002000000000，123002666000000] |
  | 123002 | 123002 | 增加记录失败，起始IMSI不能等于终止IMSI |
  | 123002000000000 | 123002000000000 | 仅限定IMSI号码123002000000000 |
  | 123003000000000 | 123004000000000 | 123003000000000～123004000000000，即区间[123003000000000，123004000000000] |
- 输入的起始IMSI和终止IMSI定义的IMSI号段范围不允许与其它记录定义的IMSI号段范围相互交叉、包含或重合。
