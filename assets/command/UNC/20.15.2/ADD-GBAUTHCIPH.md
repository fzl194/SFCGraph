---
id: UNC@20.15.2@MMLCommand@ADD GBAUTHCIPH
type: MMLCommand
name: ADD GBAUTHCIPH（增加Gb模式用户安全参数）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: GBAUTHCIPH
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
max_records: 1024
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- 用户安全管理
- Gb模式用户安全参数
status: active
---

# ADD GBAUTHCIPH（增加Gb模式用户安全参数）

## 功能

**适用网元：SGSN**

该命令用于增加2G鉴权加密的配置。 UNC 可以结合运营商的配置要求和协议规范决定是否使用鉴权加密。针对SGSN节点可能遇到的所有需要鉴权的流程， UNC 均设置了开关加以控制，运营商可以通过配置决定这些流程是否需要鉴权。

## 注意事项

- 该命令执行后立即生效。
- 指定号段的用户群采用对应的安全配置参数，未指定的用户群采用默认的安全配置参数。
- 此命令最大记录数为1024。
- 该命令部分参数与相关特性license共同完成该特性的开启，请在设置参数前使用[**DSP LICENSE**](../../../../../../平台服务管理/操作维护/License管理/显示License(DSP LICENSE)_00360098.md)命令确认对应特性license是否得到授权，执行[**LST LICENSESWITCH**](../../../../../../平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md)命令确认特性开关状态为“ENABLE(打开)”，具体相关特性请参考参数的说明。
- 系统中缺省生成一条记录用于控制所有用户的安全策略，配置导出时通过将IMSI前缀取值设置成ALL_USER来表示缺省记录。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IMSIPRE | IMSI前缀 | 可选必选说明：必选参数<br>参数含义：该参数用于系统根据指定用户的IMSI进行匹配，从而区分不同的用户群。<br>数据来源：整网规划<br>取值范围：5～15位十进制数字字符串，或字符串<br>“ALL_USER”<br>默认值：无<br>说明：- 按照IMSI最长匹配进行查询，相同IMSI前缀只能配置一条记录。<br>- IMSI前缀的匹配方式采取由前向后的最长匹配，即若用户可以匹配到多个用户群，则使用IMSI前缀最长的用户群配置。<br>- 当IMSIPRE为字符串“ALL_USER”时，可以通过[**MOD GBAUTHCIPH**](修改Gb模式用户安全参数（MOD GBAUTHCIPH）_26305454.md)命令对“SUBRANGE（用户范围）”为“ALL_USER（所有用户）”的记录进行修改。 |
| SECPLC | 安全策略 | 可选必选说明：可选参数<br>参数含义：该参数用于指定采取的安全策略。<br>数据来源：整网规划<br>取值范围：<br>- “NEVER（不鉴权不保护）”<br>- “AUTHONLY（只鉴权）”<br>- “AUTHANDPROTECTED（鉴权并保护）”<br>默认值：<br>“AUTHANDPROTECTED（鉴权并保护）”<br>配置原则：<br>- “NEVER（不鉴权不保护）”，表示不启用安全功能。<br>- “AUTHONLY（只鉴权）”，表示只鉴权不进行加密算法和完整性算法的检查。<br>- “AUTHANDPROTECTED（鉴权并保护）”，表示同时开启鉴权和保护功能。 |
| AUTHEVENT | 鉴权事件 | 可选必选说明：可选参数<br>参数含义：该参数用于指定设置哪些流程属于灵活鉴权事件。<br>前提条件：只有<br>“安全策略”<br>为<br>“AUTHONLY”<br>或<br>“AUTHANDPROTECTED”<br>时，该参数才有效。<br>数据来源：整网规划<br>取值范围：<br>- “PROD_RAU（周期RAU）”<br>- “SMS_MT（短消息MT）”<br>- “SMS_MO（短消息MO）”<br>- “DETACH（分离）”<br>- “INTER_RAU（INTER位置更新）”<br>- “INTRA_RAU（INTRA位置更新）”<br>- “PTMSI_ATTACH（PTMSI附着）”<br>- “IMSI_ATTACH（IMSI附着）”<br>- “PTMSI_SIG_NOMATCH（PTMSI签名不匹配）”<br>- “PTMSI_SIG_NOSIG（不带PTMSI签名）”<br>- “SM_PDP（PDP激活）”<br>- “SM_DEA_PDP（PDP去激活）”<br>- “LCS（位置业务LCS）”<br>- “SYSTEM_CHANGE_INTRA_RAU（系统间切换类型的INTRA位置更新）”<br>默认值：<br>“INTER_RAU-1”<br>、<br>“PTMSI_ATTACH-1”<br>、<br>“IMSI_ATTACH-1”<br>、<br>“PTMSI_SIG_NOMATCH-1”<br>、<br>“PTMSI_SIG_NOSIG-1”<br>、<br>“SYSTEM_CHANGE_INTRA_RAU-1”<br>说明：- “IMSI_ATTACH-1”：表示此流程属于灵活鉴权事件，其他参数取值相同。<br>- “IMSI_ATTACH-0”：表示此流程不属于灵活鉴权事件，其他参数取值相同。 |
| RNUM | 鉴权集重用次数 | 可选必选说明：可选参数<br>参数含义：该参数用于指定鉴权集采取的安全策略超时，再次使用原来的鉴权集的次数。<br>前提条件：只有<br>“安全策略”<br>为<br>“AUTHONLY”<br>或<br>“AUTHANDPROTECTED”<br>该参数才有效。<br>数据来源：本端规划<br>取值范围：0～255<br>默认值：0 |
| AUTHPERIOD | 鉴权周期 | 可选必选说明：可选参数<br>参数含义：该参数用于指定用户注册时间达到设定的值后，将在鉴权事件中发起鉴权。<br>前提条件：<br>- 只有“安全策略”为“AUTHONLY”或“AUTHANDPROTECTED”该参数才有效。<br>- 该参数配置受License控制，在激活相应License项(基于用户群的灵活鉴权)后，配置才能生效。<br>数据来源：本端规划<br>取值范围：0～24小时<br>默认值：24<br>说明：若取值为“0”，表示不启用周期鉴权功能。该参数单位为小时。 |
| AUTHEVENTTHRESHOLD | 鉴权事件上限 | 可选必选说明：可选参数<br>参数含义：该参数用于指定对<br>“鉴权事件”<br>不鉴权的次数上限。当指定<br>“鉴权事件”<br>计数达到上限时，将在对应的流程中进行一次鉴权。<br>前提条件：<br>- 只有“安全策略”为“AUTHONLY”或“AUTHANDPROTECTED”该参数才有效。<br>- 该参数配置受License控制，在激活相应License项(基于用户群的灵活鉴权)后，配置才能生效。<br>数据来源：整网规划<br>取值范围：0～1023<br>默认值：1<br>配置原则：<br>- 取值为“0”，表示不启用该项功能，所有的可选鉴权流程都不触发。<br>- 取值为“1”，表示每次“鉴权事件”中配置的可选鉴权事件发生都会触发鉴权流程。 |
| ATTSAUTH | 是否支持附着流程的二次鉴权功能 | 可选必选说明：可选参数<br>参数含义：该参数用于指定<br>UNC<br>网元是否启用附着流程的二次鉴权功能。<br>前提条件：只有<br>“安全策略”<br>为<br>“AUTHONLY”<br>或<br>“AUTHANDPROTECTED”<br>该参数才有效。<br>数据来源：整网规划<br>取值范围：<br>- “NO（否）”<br>- “YES（是）”<br>默认值：<br>“NO（否）”<br>。<br>配置原则：<br>- “NO（否）”，表示UNC网元不启用附着流程中一次鉴权失败后进行二次鉴权的功能。<br>- “YES（是）”，表示UNC网元启用附着流程中一次鉴权失败后进行二次鉴权的功能。 |
| RAUSAUTH | 是否支持路由更新流程的二次鉴权功能 | 可选必选说明：可选参数<br>参数含义：该参数用于指定<br>UNC<br>网元是否启用路由更新流程的二次鉴权功能。<br>前提条件：只有<br>“安全策略”<br>为<br>“AUTHONLY”<br>或<br>“AUTHANDPROTECTED”<br>该参数才有效。<br>数据来源：整网规划<br>取值范围：<br>- “NO（否）”<br>- “YES（是）”<br>默认值：<br>“NO（否）”<br>配置原则：<br>- “NO（否）”，表示UNC网元不启用路由更新流程中一次鉴权失败后进行二次鉴权的功能。<br>- “YES（是）”，表示UNC网元启用路由更新流程中一次鉴权失败后进行二次鉴权的功能。 |
| AUTHSETV2 | 是否支持V2取鉴权集功能 | 可选必选说明：可选参数<br>参数含义：该参数指示<br>UNC<br>网元取鉴权集时是否首选使用MAP协议版本为V2。<br>前提条件：只有<br>“安全策略”<br>为<br>“AUTHONLY”<br>或<br>“AUTHANDPROTECTED”<br>该参数才有效。<br>数据来源：整网规划<br>取值范围：<br>- “NO（否）”：表示首选使用MAP协议版本为V3。<br>- “YES（是）”：表示首选使用MAP协议版本为V2。<br>默认值：<br>“NO（否）” |
| AUTHSETSNUMBER | 鉴权集数量 | 可选必选说明：可选参数<br>参数含义：该参数用于指定向HLR请求的数量。<br>前提条件：只有<br>“安全策略”<br>为<br>“AUTHONLY”<br>或<br>“AUTHANDPROTECTED”<br>该参数才有效。<br>数据来源：整网规划<br>取值范围：1～5<br>默认值：5<br>说明：系统支持每个用户最多持有5组鉴权集数，因此建议配置“预先取鉴权集门限值”与该参数之和不大于5，若大于5，每次取满5组鉴权集为止，即每次取的鉴权集数实际为5减去“预先取鉴权集门限值”。 |
| PREGETAUTHSETS | 是否预取鉴权集 | 可选必选说明：可选参数<br>参数含义：该参数用于指定是否在鉴权集使用完时主动发起预取鉴权集流程。<br>前提条件：只有<br>“安全策略”<br>为<br>“AUTHONLY”<br>或<br>“AUTHANDPROTECTED”<br>该参数才有效。<br>数据来源：整网规划<br>取值范围：<br>- “NO（否）”<br>- “YES（是）”<br>默认值：<br>“YES（是）”<br>配置原则：<br>- “NO（否）”，表示不需要预取鉴权集。<br>- “YES（是）”，表示需要预取鉴权集。 |
| GETAUTHADVTH | 预先取鉴权集门限值 | 可选必选说明：可选参数<br>参数含义：该参数用于指定系统中最少持有的鉴权集。当系统检测到系统内鉴权集数小于等于该数，会自动向HLR获取鉴权集，获取数为“鉴权集数量”配置的值。<br>前提条件：只有<br>“安全策略”<br>为<br>“AUTHONLY”<br>或<br>“AUTHANDPROTECTED”<br>该参数才有效。<br>数据来源：整网规划。<br>取值范围：0～4<br>默认值：0 |
| CAFTIMES | 用户鉴权失败次数临界值 | 可选必选说明：可选参数<br>参数含义：该参数用于指定在清除用户鉴权失败记录的临界值内，允许用户鉴权失败的最大次数。如果用户鉴权失败次数超过该临界值，则触发鉴权事件告警。<br>前提条件：只有<br>“安全策略”<br>为<br>“AUTHONLY”<br>或<br>“AUTHANDPROTECTED”<br>该参数才有效。<br>数据来源：整网规划<br>取值范围：3～20<br>默认值：3 |
| CIPHALG | 加密算法 | 可选必选说明：可选参数<br>参数含义：该参数用于指定网络侧支持的加密算法。<br>前提条件：只有<br>“安全策略”<br>为<br>“AUTHANDPROTECTED”<br>该参数才有效。<br>数据来源：整网规划<br>取值范围：<br>- “GEA_3（GEA_3）”<br>- “GEA_2（GEA_2）”<br>- “GEA_1（GEA_1）”<br>默认值：<br>“GEA_3（GEA_3）”<br>、<br>“GEA_2（GEA_2）”<br>、<br>“GEA_1（GEA_1）”<br>说明：- “GEA_1”、“GEA_2”和“GEA_3”三种算法，可以选其一，也可以选两种或全选。<br>- 当参数设置为“GEA_1（GEA_1）”时，“支持GPRS加密功能：GEA-1(仅用于Gb模式)”特性的相关license授权并开启后，此参数配置才生效（特性编号：WSFD-103001，License项：LKV2GEA102）。<br>- 当参数设置为“GEA_2（GEA_2）”时，“支持GPRS加密功能：GEA-2(仅用于Gb模式)”特性的相关license授权并开启后，此参数配置才生效（特性编号：WSFD-103002，License项：LKV2GEA202）。<br>- 当参数设置为“GEA_3（GEA_3）”时，“支持GPRS加密功能：GEA-3(仅用于Gb模式)”特性的相关license授权并开启后，此参数配置才生效（特性编号：WSFD-103003，License项：LKV2GEA302）。<br>- 当参数设置为“GEA_1（GEA_1）”或者“GEA_2 （GEA_2）”时为不安全加密算法，存在安全风险，请谨慎设置。 |
| NCIPH | 版本协商失败允许不加密 | 可选必选说明：可选参数<br>参数含义：该参数用于指定网络与用户协商加密版本失败后，是否允许用户不加密接入网络。也用于指示在已配置加密License的情况下，网络侧协商加密版本失败后是否允许用户不加密接入网络，如果网络允许不加密，则用户可以无需加密接入网络，否则网络将拒绝用户的接入。<br>前提条件：只有<br>“安全策略”<br>为<br>“AUTHANDPROTECTED”<br>该参数才有效。<br>数据来源：整网规划<br>取值范围：<br>- “NO（否）”<br>- “YES（是）”<br>默认值：<br>“YES（是）”<br>说明：如果LICENSE不支持加密，则该参数无效。 |
| XIDRESET | Rau Accept无响应后是否启用XID Reset流程 | 可选必选说明：可选参数<br>参数含义：该参数用于指示加密功能启用时，如果手机对Intra Rau Accept没有响应，则SGSN再次收到手机的Intra Rau Request后，是否发起XID Reset流程。 如果设置为是，则SGSN会发起XID RESET流程。<br>前提条件：只有<br>“安全策略”<br>为<br>“AUTHANDPROTECTED”<br>时，该参数才有效。<br>数据来源：整网规划<br>取值范围：<br>- “NO（否）”<br>- “YES（是）”<br>默认值：<br>“NO（否）” |
| IDRQ | 强制身份识别 | 可选必选说明：可选参数<br>参数含义：该参数用于指定是否强制获取用户身份标识。对于2G使用PTMSI附着，控制是否发送IDENTITY REQUEST消息。<br>在启用“WSFD-<br>207001<br>网络共享（MOCN）”特性的情况下，附着请求层二消息UL-UNITDATA携带了IMSI，则本参数配置不生效，即系统不会发送IDENTITY REQUEST消息。<br>数据来源：整网规划<br>取值范围：<br>- “NO（否）”<br>- “YES（是）”<br>默认值：<br>“NO（否）”<br>配置原则：<br>- “NO（否）”，表示系统信任曾经保存的IMSI，不再强制发起Identity流程获取用户的IMSI。<br>- “YES（是）”，表示系统不信任以前曾经保存的用户IMSI，当MS发起以PTMSI为标识的Attach流程时，系统需要强制通过Identity流程重新获取用户的IMSI。 |

## 操作的配置对象

- [Gb模式用户安全参数（GBAUTHCIPH）](configobject/UNC/20.15.2/GBAUTHCIPH.md)

## 使用实例

增加IMSI前缀为"123456＂的用户2G鉴权加密配置，加密算法选择GEA1：

ADD GBAUTHCIPH: IMSIPRE="123456", SECPLC=AUTHANDPROTECTED, CIPHALG=GEA_1-1;

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加Gb模式用户安全参数（ADD-GBAUTHCIPH）_26145642.md`
