# 增加SM原因值映射配置（ADD SMCAUSEMAP）

- [命令功能](#ZH-CN_MMLREF_0209652445__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0209652445__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0209652445__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0209652445__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0209652445)

**适用NF：SMF、PGW-C、SGW-C、GGSN**

此命令用于增加一个原因值映射配置记录。原因值映射就是将原接口消息中的原因值直接映射到目标接口消息中下发的原因值。

## [注意事项](#ZH-CN_MMLREF_0209652445)

- 该命令执行后立即生效。

- 此命令的最大记录数为1024。
- 执行此命令可能会改变通过该映射配置进行原因值控制的异常场景中下发给终端的拒绝原因值，从而导致相应拒绝类话统指标的变化。
- 当外部NF发送的消息中携带的原因值有多种情况时，将采用ADD SMCAUSEMAP命令配置对应的原因值映射规则。
- 配置下发的原因值可能会对终端行为产生影响，在配置前评估影响。关于不同原因值的含义及对终端行为的影响请参见协议3GPP TS 24.008、3GPP TS 24.301或3GPP TS 24.501。
- 当CAUSERANGE为DEFAULT时， BGCAUSE、 EDCAUSE和APPERROR默认为65535。当CAUSERANGE为SPECIAL时，APPERROR默认为65535。

#### [操作用户权限](#ZH-CN_MMLREF_0209652445)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0209652445)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CAUSEGRPID | 原因值组标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定表示一个原因值映射规则集合的唯一数字ID。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~127。<br>默认值：无<br>配置原则：<br>该参数必须通过命令ADD SMCAUSEGRP配置。 |
| CAUSERANGE | 原因值范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定原因值范围。<br>数据来源：全网规划<br>取值范围：<br>- “DEFAULT（缺省）”：表示无需指定某一特定接口的起始和终止原始原因值。<br>- “SPECIAL（特定）”：表示需指定某一特定接口的起始原始原因值。<br>- “SPECIAL_APP_ERR（特定应用层错误）”：表示需指定某一特定接口的起始http层状态码以及应用层错误<br>默认值：无<br>配置原则：<br>- 一个“CAUSEGRPID(原因值组标识)”只能对应一个“DEFAULT(缺省)”配置。“SPECIAL(特定)”可以配置多个。“SPECIAL_APP_ERR(特定应用层错误)”针对服务化接口触发的NAS原因值，可以配置多个。<br>- 在实际使用时，CAUSERANGE下各个枚举的优先级顺序： SPECIAL_APP_ERR > SPECIAL > DEFAULT。如果同时配置了“DEFAULT(缺省)”、“SPECIAL(特定)”和“SPECIAL_APP_ERR(特定应用层错误)”的记录，则优先使用“SPECIAL_APP_ERR(特定应用层错误)”记录。如果同时配置了“DEFAULT(缺省)”和“SPECIAL(特定)”的记录，则优先使用“SPECIAL(特定)”记录。<br>- 同一原因值组标识下，原因值范围为SPECIAL时，输入的原始原因值范围不允许相互交叉、包含或重合。同一原因值组标识下，原因值范围为SPECIAL_APP_ERR时，若APPERROR相同，输入的原始原因值范围不允许相互交叉、包含或重合。 |
| BGCAUSE | 起始原始原因值 | 可选必选说明：该参数在"CAUSERANGE"配置为"SPECIAL"、"SPECIAL_APP_ERR"时为条件必选参数。<br>参数含义：该参数用于指定某一特定接口的起始原始原因值。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~65535。<br>默认值：无<br>配置原则：<br>“BGCAUSE(起始原始原因值)”小于等于“EDCAUSE(终止原始原因值)”。 |
| EDCAUSE | 终止原始原因值 | 可选必选说明：该参数在"CAUSERANGE"配置为"SPECIAL"、"SPECIAL_APP_ERR"时为条件可选参数。<br>参数含义：该参数用于指定某一特定接口的终止原始原因值。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~65535。<br>默认值：无<br>配置原则：<br>“EDCAUSE(终止原始原因值)”大于等于“BGCAUSE(起始原始原因值)”。EDCAUSE不配置时，默认为BGCAUSE的值。 |
| APPERROR | 应用层错误 | 可选必选说明：该参数在"CAUSERANGE"配置为"SPECIAL_APP_ERR"时为条件必选参数。<br>参数含义：该参数表示服务化接口下对端网元返回的应用层错误，与BGCAUSE以及EDCAUSE参数一起进行原因值映射。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~65535。<br>默认值：无<br>配置原则：<br>该参数对应协议应用层含义如下：<br>1 USER_NOT_FOUND：用户不存在。<br>2 ROAMING_NOT_ALLOWED：用户不允许漫游。<br>3 DNN_NOT_ALLOWED：DNN未鉴权。<br>4 DATA_NOT_FOUND：未找到签约数据。<br>5 UNSUPPORTED_RESOURCE_URI：签约数据中存在不支持的资源URI。<br>6 UNKNOWN_5GS_SUBSCRIPTION：用户未签约5G业务。<br>7 NO_PS_SUBSCRIPTION：用户未签约PS业务。<br>8 ACCESS_NOT_ALLOWED：用户接入类型不允许。<br>9 RAT_NOT_ALLOWED：RAT不允许。<br>10 REAUTHENTICATION_REQUIRED：重新鉴权。<br>11 NF_CONSUMER_REDIRECT_ONE_TXN：请求重定向。<br>12 CONTEXT_NOT_FOUND：用户上下文不存在。<br>13 GROUP_IDENTIFIER_NOT_FOUND：请求groupId不存在。<br>14 SUBSCRIPTION_NOT_FOUND：签约数据不存在。<br>15 SERVICE_NOT_PROVISIONED：该服务未签约。<br>16 SERVICE_NOT_ALLOWED：签约数据不允许该服务。<br>17 TEMPORARY_REJECT_REGISTRATION：注册流程正在进行。<br>18 TEMPORARY_REJECT_HANDOVER_ONGOING_ONGOING：N2切换正在进行。<br>19 UNPROCESSABLE_REQUEST：语义错误。<br>20 USER_UNKNOWN：未知用户。<br>21 ERROR_INITIAL_PARAMETERS：会话或用户信息异常。<br>22 ERROR_TRIGGER_EVENT：trigger类型与实际不一致。<br>23 ERROR_TRAFFIC_MAPPING_INFO_REJECTED：PCF不接受SMF在PCC请求中提供的一个或多个流量映射过滤器。<br>24 ERROR_CONFLICTING_REQUEST：网络侧触发的资源分配正在进行，且已经涵盖UE请求的资源。<br>25 LATE_OVERLAPPING_REQUEST：与已有的策略关联冲突。<br>26 POLICY_CONTEXT_DENIED：由于操作策略和本地配置导致拒绝。<br>27 VALIDATION_CONDITION_NOT_MET：不满足数据传输策略的生效条件。<br>28 PENDING_TRANSACTION：PCF收到一个策略关联的传入请求，但该策略关联上有一个正在进行的事务。<br>29 CHARGING_FAILED：计费需要签约信息不完整或错误。<br>30 RE_AUTHORIZATION_FAILED：CTF提供的流量报告不完整或错误。<br>31 CHARGING_NOT_APPLICABLE：终端用户无需使用计费服务。<br>32 END_USER_REQUEST_DENIED：终端用户受限。<br>33 QUOTA_LIMIT_REACHED：余额不足。<br>34 END_USER_REQUEST_REJECTED：终端用户受限。<br>35 INVALID_API：无效的API。<br>36 INVALID_MSG_FORMAT：无效的消息格式。<br>37 INVALID_QUERY_PARAM：无效的查询参数。<br>38 MANDATORY_QUERY_PARAM_INCORRECT：必选查询参数错误。<br>39 OPTIONAL_QUERY_PARAM_INCORRECT：可选查询参数错误。<br>40 MANDATORY_QUERY_PARAM_MISSING：必选查询参数丢失。<br>41 MANDATORY_IE_INCORRECT：必选信元错误。<br>42 OPTIONAL_IE_INCORRECT：可选信元错误。<br>43 MANDATORY_IE_MISSING：必选信元丢失。<br>44 UNSPECIFIED_MSG_FAILURE：未指定的客户端错误。<br>45 NF_DISCOVERY_FAILURE：NF服务发现失败。<br>46 INVALID_DISCOVERY_PARAM：无效的Discovery参数。<br>47 RESOURCE_CONTEXT_NOT_FOUND：资源上下文不存在。<br>48 MODIFICATION_NOT_ALLOWED：请求修改不允许修改的信元。<br>49 RESOURCE_URI_STRUCTURE_NOT_FOUND：Resource URI中的固定字段在NF中不存在。<br>50 INCORRECT_LENGTH：长度非法。<br>51 NF_CONGESTION_RISK：存在NF拥塞风险。<br>52 INSUFFICIENT_RESOURCES：资源不足。<br>53 UNSPECIFIED_NF_FAILURE：未指定原因。<br>54 SYSTEM_FAILURE：系统错误。<br>55 NF_FAILOVER：NF不可用。<br>56 NF_SERVICE_FAILOVER：NF服务不可用。<br>57 NF_CONGESTION：NF拥塞。<br>58 TIMED_OUT_REQUEST：客户端请求超时。<br>59 SCP_REDIRECTION：请求被重定向到其他SCP。<br>60 END_USER REQUEST_DENIED：终端用户受限。 |
| TCAUSE | 目标原因值 | 可选必选说明：必选参数<br>参数含义：该参数用于指定下发到目标网元的原因值，下发的NAS原因值参考3GPP TS 24.501，下发的GTP原因值参考3GPP TS 29.060、3GPP TS 29.274。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~65535。<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0209652445)

增加原因值映射配置：CAUSEGRPID（原因值组标识）为126，CAUSERANGE（原因值范围）为DEFAULT（缺省），TCAUSE（目标原因值）为27：

```
ADD SMCAUSEMAP: CAUSEGRPID=126, CAUSERANGE=DEFAULT, TCAUSE=27;
```
