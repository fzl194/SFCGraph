---
id: UNC@20.15.2@MMLCommand@MOD IUAUTHCIPH
type: MMLCommand
name: MOD IUAUTHCIPH（修改Iu模式用户安全参数）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: IUAUTHCIPH
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- 用户安全管理
- Iu模式用户安全参数
status: active
---

# MOD IUAUTHCIPH（修改Iu模式用户安全参数）

## 功能

![](修改Iu模式用户安全参数(MOD IUAUTHCIPH)_72345245.assets/notice_3.0-zh-cn_2.png)

不开启鉴权功能将导致身份未被鉴别的UE接入系统，引发系统内UE发生串号，计费错误等问题。

**适用网元：SGSN**

该命令用于修改3G的加密鉴权配置信息。

## 注意事项

- 此命令对于当前系统内已存在签约数据的用户不立即生效，在用户再次触发安全流程后生效。
- Uplink NAS类型的Detach不会鉴权。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定所包含的用户范围。<br>前提条件：如果系统开工时就增加了<br>“用户范围”<br>为<br>“所有用户”<br>的记录，<br>[**ADD IUAUTHCIPH**](增加Iu模式用户安全参数(ADD IUAUTHCIPH)_72225327.md)<br>命令可以不需要该参数。否则按照IMSI最长匹配进行查询，相同IMSI前缀只能配置一条记录。<br>数据来源：整网规划<br>取值范围：<br>- “ALL_USER（所有用户）”<br>- “SPECIAL_USER（指定用户）”<br>默认值：无 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件必选参数<br>参数含义：该参数用于系统根据指定用户的IMSI进行匹配，从而区分不同的用户群。<br>数据来源：整网规划<br>取值范围：5～15位十进制数字字符串<br>默认值：无<br>说明：- 按照IMSI最长匹配进行查询，相同IMSI前缀只能配置一条记录。<br>- IMSI前缀的匹配方式采取由前向后的最长匹配，即若对于用户可以匹配到多个用户群，则使用IMSI前缀最长的用户群配置。 |
| SECPLC | 安全策略 | 可选必选说明：可选参数<br>参数含义：该参数用于指定采取的安全策略。<br>数据来源：整网规划<br>取值范围：<br>- “NEVER（不鉴权不保护）”<br>- “AUTHONLY（只鉴权）”<br>- “AUTHANDPROTECTED（鉴权并保护）”<br>默认值：无<br>配置原则：建议值为<br>“AUTHANDPROTECTED(鉴权并保护)”<br>。<br>说明：“AUTHANDPROTECTED(鉴权并保护)”<br>，<br>“NEVER(不鉴权不保护)”<br>和<br>“AUTHONLY(只鉴权)”<br>仅用于测试场景，不允许在实际场景中使用。由于3G业务对安全性要求高，如果强制修改为<br>“NEVER(不鉴权不保护)”<br>或<br>“AUTHONLY(只鉴权)”<br>，可能会导致UE业务处理失败。 |
| AUTHEVENT | 鉴权事件 | 可选必选说明：可选参数<br>参数含义：该参数用于指定设置哪些流程属于灵活鉴权事件。<br>前提条件：只有<br>“安全策略”<br>为<br>“AUTHONLY”<br>或<br>“AUTHANDPROTECTED”<br>时，该参数才有效。<br>数据来源：整网规划<br>取值范围：<br>- “PROD_RAU（周期性RAU）”<br>- “PAGING_RSP（寻呼响应）”<br>- “MS_SERVICE_REQ（MS发起的服务请求）”<br>- “DETACH（分离）”<br>- “INTER_RAU（INTER位置更新）”<br>- “INTRA_RAU（INTRA位置更新）”<br>- “PTMSI_ATTACH（使用PTMSI的附着）”<br>- “IMSI_ATTACH（使用IMSI的附着）”<br>- “PTMSI_SIG_NOMATCH（PTMSI签名不匹配）”<br>- “PTMSI_SIG_NOSIG（不带PTMSI签名）”<br>- “INTRA_RAU_AFTER_RELOCATOIN（重分配后的INTRA位置更新）”<br>- “INTER_RAU_AFTER_RELOCATOIN（重分配后的INTER 位置更新）”<br>- “SMS_MT（短消息MT）”<br>- “SMS_MO（短消息MO）”<br>- “LCS（位置业务LCS）”<br>- “SYSTEM_CHANGE_INTRA_RAU（系统间切换类型的INTRA位置更新）”<br>默认值：无<br>配置原则：以下流程建议执行鉴权：<br>- “INTER_RAU（INTER位置更新）”<br>- “PTMSI_ATTACH（使用PTMSI的附着）”<br>- “IMSI_ATTACH（使用IMSI的附着）”<br>- “PTMSI_SIG_NOMATCH（PTMSI签名不匹配）”<br>- “PTMSI_SIG_NOSIG（不带PTMSI签名）”<br>- “INTER_RAU_AFTER_RELOCATOIN（重分配后的INTER 位置更新）”<br>- “SYSTEM_CHANGE_INTRA_RAU（系统间切换类型的INTRA位置更新）” |
| AUTHPERIOD | 鉴权周期 | 可选必选说明：可选参数<br>参数含义：该参数用于指定用户注册时间达到设定的值后，将在可选鉴权事件中发起鉴权。<br>前提条件：<br>- 只有“安全策略”为“AUTHONLY”或“AUTHANDPROTECTED”该参数才有效。<br>- 该参数配置受License控制，在激活相应License项(基于用户群的灵活鉴权)后，配置才能生效。<br>数据来源：本端规划<br>取值范围：0～24小时<br>默认值：无<br>配置原则：建议值为24。<br>说明：若取值为“0”，表示不启用周期鉴权功能。 |
| AUTHEVENTTHRESHOLD | 鉴权事件上限 | 可选必选说明：可选参数<br>参数含义：该参数用于指定对<br>“鉴权事件”<br>不鉴权的次数上限。当指定<br>“鉴权事件”<br>计数达到上限时，将在对应的流程中进行一次鉴权。<br>前提条件：<br>- 只有“安全策略”为“AUTHONLY”或“AUTHANDPROTECTED”时，该参数才有效。<br>- 该参数配置受License控制，在激活相应License项(基于用户群的灵活鉴权)后，配置才能生效。<br>数据来源：整网规划<br>取值范围：0～1023<br>默认值：无<br>配置原则：建议值为1。<br>说明：- 取值为“0”，表示不启用该项功能，所有的可选鉴权流程都不触发。<br>- 取值为“1”，表示每次“鉴权事件”中配置的可选鉴权事件发生都会触发鉴权流程。 |
| ATTSAUTH | 是否支持附着流程的二次鉴权功能 | 可选必选说明：可选参数<br>参数含义：该参数用于指定<br>UNC<br>是否启用附着流程的二次鉴权功能。<br>前提条件：只有<br>“安全策略”<br>为<br>“AUTHONLY”<br>或<br>“AUTHANDPROTECTED”<br>时，该参数才有效。<br>数据来源：整网规划<br>取值范围：<br>- “NO（否）”——UNC不启用附着流程中一次鉴权失败后进行二次鉴权的功能。<br>- “YES（是）”——UNC启用附着流程中一次鉴权失败后进行二次鉴权的功能。<br>默认值：无<br>配置原则：建议值为<br>“NO（否）”<br>。 |
| RAUSAUTH | 是否支持路由更新流程的二次鉴权功能 | 可选必选说明：可选参数<br>参数含义：该参数用于指定<br>UNC<br>是否启用路由更新流程的二次鉴权功能。<br>前提条件：只有<br>“安全策略”<br>为<br>“AUTHONLY”<br>或<br>“AUTHANDPROTECTED”<br>时，该参数才有效。<br>数据来源：整网规划<br>取值范围：<br>- “NO（否）”——UNC不启用路由更新流程中一次鉴权失败后进行二次鉴权的功能。<br>- “YES（是）”——UNC启用路由更新流程中一次鉴权失败后进行二次鉴权的功能。<br>默认值：无<br>配置原则：建议值为<br>“NO（否）”<br>。 |
| AUTHSETV2 | 是否支持V2取鉴权集功能 | 可选必选说明：可选参数<br>参数含义：该参数指示<br>UNC<br>网元取鉴权集时是否首选使用MAP协议版本为V2。<br>前提条件：只有<br>“安全策略”<br>为<br>“AUTHONLY”<br>或<br>“AUTHANDPROTECTED”<br>该参数才有效。<br>数据来源：整网规划<br>取值范围：<br>- “NO（否）”——首选使用MAP协议版本为V3。<br>- “YES（是）”——首选使用MAP协议版本为V2。<br>默认值：无<br>配置原则：建议值为<br>“NO（否）”<br>。 |
| AUTHSETSNUMBER | 鉴权集数量 | 可选必选说明：可选参数<br>参数含义：该参数用于指定每次取的鉴权集数。<br>前提条件：只有<br>“安全策略”<br>为<br>“AUTHONLY”<br>或<br>“AUTHANDPROTECTED”<br>该参数才有效。<br>数据来源：整网规划<br>取值范围：1～5<br>默认值：无<br>配置原则：建议值为5。<br>说明：系统支持每个用户最多持有5组鉴权集数，因此建议配置“预先取鉴权集门限值”与该参数之和不大于5。若大于5，每次取满5组鉴权集为止，即每次取的鉴权集数实际为5减去“预先取鉴权集门限值”。 |
| PREGETAUTHSETS | 是否预取鉴权集 | 可选必选说明：可选参数<br>参数含义：该参数用于指定在鉴权集只有一个未使用时，是否预先获取鉴权集。<br>前提条件：只有<br>“安全策略”<br>为<br>“AUTHONLY”<br>或<br>“AUTHANDPROTECTED”<br>该参数才有效。<br>数据来源：整网规划<br>取值范围：<br>- “NO（否）”——不需要预取鉴权集。<br>- “YES（是）”——需要预取鉴权集。<br>默认值：无<br>配置原则：建议值为<br>“YES（是）”<br>。 |
| GETAUTHADVTH | 预先取鉴权集门限值 | 可选必选说明：可选参数<br>参数含义：该参数用于指定系统中最少持有的鉴权集。<br>前提条件：只有<br>“安全策略”<br>为<br>“AUTHONLY”<br>或<br>“AUTHANDPROTECTED”<br>该参数才有效。<br>数据来源：整网规划<br>取值范围：0～4<br>默认值：无<br>配置原则：建议值为0<br>说明：当系统检测到系统内鉴权集数小于等于该数，会自动向HLR获取鉴权集，获取数为“鉴权集数量”配置的值。 |
| REAUTH | 重复鉴权 | 可选必选说明：可选参数<br>参数含义：该参数用于指定控制寻呼响应后的短消息鉴权行为。<br>前提条件：只有<br>“安全策略”<br>为<br>“AUTHONLY”<br>或<br>“AUTHANDPROTECTED”<br>时，该参数才有效。<br>数据来源：整网规划<br>取值范围：<br>- “NO（否）”——不重复鉴权。<br>- “YES（是）”——重复鉴权。<br>默认值：无<br>配置原则：建议值为<br>“NO（否）”<br>。<br>说明：在3G短消息或LCS鉴权流程中，如果当前用户处于IDLE态，MM接收到MAP或LCS的鉴权请求后将触发寻呼。寻呼流程结束后，如果SERVICE REQUEST流程中没有鉴权，MM将直接对用户进行鉴权，不受本开关控制；如果SERVICE REQUEST流程中已经鉴权，将判断本开关的值。 |
| CAFTIMES | 用户鉴权失败次数临界值 | 可选必选说明：可选参数<br>参数含义：该参数用于指定在清除记录时间临界值内，允许用户鉴权失败的最大次数。<br>前提条件：只有<br>“安全策略”<br>为<br>“AUTHONLY”<br>或<br>“AUTHANDPROTECTED”<br>该参数才有效。<br>数据来源：整网规划<br>取值范围：3～20<br>默认值：无<br>配置原则：建议值为3。<br>说明：如果用户鉴权失败次数超过该临界值，则触发事件告警。 |
| CIPHALG | 加密算法 | 可选必选说明：可选参数<br>参数含义：该参数用于选择需要使用的加密算法。<br>前提条件：只有<br>“安全策略”<br>为<br>“AUTHANDPROTECTED”<br>该参数才有效。<br>数据来源：整网规划<br>取值范围：<br>- “UEA1（UEA1）”<br>- “UEA2（UEA2）”<br>- “NO_ENCRYPTION(NO_ENCRYPTION)”<br>默认值：无<br>配置原则：建议配置所有加密算法。<br>说明：“NO_ENCRYPTION”<br>、<br>“UEA1”<br>和<br>“UEA2”<br>三种算法，可以选其一，也可以选两种或全选。 |
| INTALG | 完整性算法 | 可选必选说明：可选参数<br>参数含义：该参数用于选择需要使用的完整性算法。完整性算法用于手机和RNC之间消息的完整性保护。<br>前提条件：只有<br>“安全策略”<br>为<br>“AUTHANDPROTECTED”<br>该参数才有效。<br>数据来源：整网规划<br>取值范围：<br>- “UIA1（UIA1）”<br>- “UIA2（UIA2）”<br>默认值：无<br>配置原则：建议配置所有完整性算法。<br>说明：“UIA1”<br>和<br>“UIA2”<br>两种算法，可以选其一，也可以全选。 |
| IDRQ | 强制身份识别 | 可选必选说明：可选参数<br>参数含义：该参数用于指定是否强制获取用户身份标识。对于3G使用PTMSI附着，控制是否发送IDENTITY REQUEST消息。<br>数据来源：整网规划<br>取值范围：<br>- “NO（否）”——系统信任曾经保存的IMSI，不再强制发起IDENTITY流程获取用户的IMSI。<br>- “YES（是）”——系统不信任以前曾经保存的用户IMSI，当MS发起以PTMSI为标识的ATTACH流程时，系统需要强制通过IDENTITY流程重新获取用户的IMSI。<br>默认值：无<br>配置原则：建议值为<br>“YES（是）”<br>。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/IUAUTHCIPH]] · Iu模式用户安全参数（IUAUTHCIPH）

## 使用实例

1. 修改所有用户的加密算法为UEA1：
  MOD IUAUTHCIPH: SUBRANGE=ALL_USER, SECPLC=AUTHANDPROTECTED, CIPHALG=UEA1-0;
2. 修改IMSI前缀为“012544”的用户的加密算法为UEA1：
  MOD IUAUTHCIPH: SUBRANGE=SPECIAL_USER, IMSIPRE="012544", SECPLC=AUTHANDPROTECTED, CIPHALG=UEA1-0;

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-IUAUTHCIPH.md`
