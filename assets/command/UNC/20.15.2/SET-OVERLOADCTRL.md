---
id: UNC@20.15.2@MMLCommand@SET OVERLOADCTRL
type: MMLCommand
name: SET OVERLOADCTRL（设置信令抑制功能开关以及老化定时器时长）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: OVERLOADCTRL
command_category: 配置类
applicable_nf:
- SGW-C
- PGW-C
- SMF
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 接入管理运维
- 流控管理
- 信令抑制
status: active
---

# SET OVERLOADCTRL（设置信令抑制功能开关以及老化定时器时长）

## 功能

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用来配置GiGn联动信令抑制功能的开关以及老化定时器时长。配置针对业务触发的信令导致的用户去活场景是否开启信令抑制功能。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| CTRLENABLE | AGINGTIME | SRVTRIGCCRI | SRVTRIGACCT | NASCAUSE | APNCTRLSWITCH | CHECKPERIOD | APNFAULTCAUSE | APNFAULTWAL | ALARMSWITCH | GXCTLSWITCH | GYCTLSWITCH | GIAUTHCTLSWITCH | GIACCTCTLSWITCH | DRACTLSWITCH | GACTLSWITCH |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DISABLE | 60 | DISABLE | DISABLE | INSUFFICIENT_RESOURCES | DISABLE | 20 | SERVICE_OPTION_NOT_SUPPORTED | 1 | DISABLE | DISABLE | DISABLE | DISABLE | DISABLE | DISABLE | DISABLE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CTRLENABLE | 信令抑制功能开关 | 可选必选说明：可选参数<br>参数含义：信令抑制功能的开关。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE（不使能）<br>- ENABLE（使能）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST OVERLOADCTRL查询当前参数配置值。<br>配置原则：<br>当CTRLENABLE功能打开后，UNC系统过载情况下，可能造成用户短时间内无法上线。<br>当CTRLENABLE功能关闭后，对于业务触发的信令，在线计费的CCR-I和AAA计费的Accounting Start消息导致的去活不会进行信令抑制。 |
| AGINGTIME | 信令抑制记录的老化定时器时长(秒) | 可选必选说明：该参数在"CTRLENABLE"配置为"ENABLE"时为条件可选参数。<br>参数含义：表示信令抑制记录的老化定时器时长。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是30~180。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST OVERLOADCTRL查询当前参数配置值。<br>配置原则：无 |
| SRVTRIGCCRI | OCS CCR-I去活是否开启信令抑制 | 可选必选说明：可选参数<br>参数含义：业务触发的OCS CCR-I导致的用户去活是否开启信令抑制功能。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE（不使能）<br>- ENABLE（使能）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST OVERLOADCTRL查询当前参数配置值。<br>配置原则：无 |
| SRVTRIGACCT | ACCT去活是否开启信令抑制 | 可选必选说明：可选参数<br>参数含义：指定因Gi接口智能流控导致的去活是否开启信令抑制功能。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE（不使能）<br>- ENABLE（使能）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST OVERLOADCTRL查询当前参数配置值。<br>配置原则：无 |
| NASCAUSE | NAS消息失败原因值 | 可选必选说明：可选参数<br>参数含义：指定5G会话因信令抑制激活失败回复NAS原因值。<br>数据来源：本端规划<br>取值范围：<br>- INSUFFICIENT_RESOURCES（资源不足）<br>- OPERATOR_DETERMINED_BARRING（运营商决定的闭锁）<br>- MISSING_OR_UNKNOWN_DNN（DNN未知或缺失）<br>- UNKNOWN_PDU_SESSION_TYPE（未知的PDU会话类型）<br>- USER_AUTHENTICATION_OR_AUTHORIZATION_FAILED（用户鉴权或授权失败）<br>- REQUEST_REJECTED_UNSPECIFIED（请求被拒绝，原因未指定）<br>- SERVICE_OPTION_NOT_SUPPORTED（不支持该服务）<br>- REQUESTED_SERVICE_OPTION_NOT_SUBSCRIBED（该服务未订阅）<br>- PTI_ALREADY_IN_USE（PTI正在使用）<br>- REGULAR_DEACTIVATION（常规去激活）<br>- FIVEGS_QOS_NOT_ACCEPTED（不接受的5G QoS）<br>- NETWORK_FAILURE（网络故障）<br>- REACTIVATION_REQUESTED（请求重激活）<br>- SEMANTIC_ERROR_IN_THE_TFT_OPERATION（TFT操作中的语义错误）<br>- SYNTACTICAL_ERROR_IN_THE_TFT_OPERATION（TFT操作中的语法错误）<br>- INVALID_PDU_SESSION_IDENTITY（无效的PDU会话标识）<br>- SEMANTIC_ERRORS_IN_PACKET_FILTERS（数据包过滤器中的语义错误）<br>- SYNTACTICAL_ERROR_IN_PACKET_FILTER（数据包过滤器中的语法错误）<br>- OUT_OF_LADN_SERVICE_AREA（移出LADN服务区）<br>- PTI_MISMATCH（PTI正在使用）<br>- PDU_SESSION_TYPE_IPV4_ONLY_ALLOWED（仅允许IPV4 PDU会话）<br>- PDU_SESSION_TYPE_IPV6_ONLY_ALLOWED（仅允许IPV6 PDU会话）<br>- PDU_SESSION_TYPE_DOES_NOT_EXIST（PDU会话类型不存在）<br>- PDU_SESSION_TYPE_IPV4V6_ONLY_ALLOWED（仅允许IPV4和IPV6 PDU会话）<br>- PDU_TYPE_UNSTRUCTURED_ONLY_ALLOWED（仅允许非结构化的PDU会话）<br>- PDU_SESSION_TYPE_ETHERNET_ONLY_ALLOWED（仅允许以太网类型的PDU会话）<br>- INSUFFICIENT_RESOURCES_FOR_SPECIFIC_SLICE_AND_DNN（特定切片和DNN的资源不足）<br>- INSUFFICIENT_RESOURCES_FOR_SPECIFIC_SLICE（特定切片资源不足）<br>- MISSING_OR_UNKNOWN_DNN_IN_A_SLICE（切片中DNN缺失或未知）<br>- INVALID_PTI_VALUE（无效的PTI值）<br>- MAX_DATA_RATE_FOR_UP_INTEGRITY_PROTECTION_TOO_LOW（用户面完整性保护单用户最大数据速率过低）<br>- SEMANTIC_ERROR_IN_THE_QOS_OPERATION（QoS操作中的语义错误）<br>- SYNTACTICAL_ERROR_IN_THE_QOS_OPERATION（QoS操作中的语法错误）<br>- INVALID_MAPPED_EPS_BEARER_IDENTITY（映射的EPS承载标识无效）<br>- SEMANTICALLY_INCORRECT_MESSAGE（消息中语义不正确）<br>- INVALID_MANDATORY_INFORMATION（必要信息无效）<br>- MESSAGE_TYPE_NONEXIST_OR_NOT_IMPLEMENTED（消息类型不存在或未实施）<br>- MESSAGE_TYPE_NOT_COMPATIBLE_WITH_PROTOCOL_STATE（消息类型与协议状态不兼容）<br>- INFORMATION_ELEMENT_NONEXISTENT_OR_NOT_IMPLEMENTED（信息元素不存在或未实施）<br>- CONDITIONAL_IE_ERROR（条件信元错误）<br>- MESSAGE_NOT_COMPATIBLE_WITH_THE_PROTOCOL_STATE（消息与协议状态不兼容）<br>- PROTOCOL_ERROR_UNSPECIFIED（其它的协议相关错误）<br>- UNSUPPORTED_5QI_VALUE（不支持的5QI值）<br>- NOT_SUPPORTED_SSC_MODE（不支持该SSC模式）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST OVERLOADCTRL查询当前参数配置值。<br>配置原则：无 |
| APNCTRLSWITCH | APN故障检测开关 | 可选必选说明：可选参数<br>参数含义：该功能主要控制在用户接入时是否基于APN进行故障流控，一旦启用APN故障流控，某个APN由于外部设备故障导致连续激活失败时，UNC进行流控处理。开关关闭则不进行APN故障检测和流控。<br>配置APN的故障流控的全局总开关，针对整机配置后立即生效。<br>APN故障流控功能是指UNC定期检查在一段时间内，是否出现由于APN所对应的外部网元（AAA、PCRF、PCF、OCS、CHF）故障而导致用户连续激活失败的情况。当出现这种情况后，UNC认为该APN故障。对于后续使用该APN激活的用户，UNC直接拒绝大部分激活请求，只允许少量激活请求和外部网元交互，以探测外部网元状态是否恢复。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE（不使能）<br>- ENABLE（使能）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST OVERLOADCTRL查询当前参数配置值。<br>配置原则：无 |
| CHECKPERIOD | APN故障检测时间(秒) | 可选必选说明：该参数在"APNCTRLSWITCH"配置为"ENABLE"时为条件可选参数。<br>参数含义：表示APN故障检测时间。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~60。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST OVERLOADCTRL查询当前参数配置值。<br>配置原则：<br>若数值设置过小，UNC对故障判断时间不充分，导致故障误判；若数值设置过大，UNC等待判断时间过长，导致故障拥塞，建议配置时长为10秒~30秒之间。 |
| APNFAULTCAUSE | APN故障NAS消息失败原因值 | 可选必选说明：该参数在"APNCTRLSWITCH"配置为"ENABLE"时为条件可选参数。<br>参数含义：指定5G会话因APN故障激活失败回复NAS原因值。<br>数据来源：本端规划<br>取值范围：<br>- INSUFFICIENT_RESOURCES（资源不足）<br>- OPERATOR_DETERMINED_BARRING（运营商决定的闭锁）<br>- MISSING_OR_UNKNOWN_DNN（DNN未知或缺失）<br>- UNKNOWN_PDU_SESSION_TYPE（未知的PDU会话类型）<br>- USER_AUTHENTICATION_OR_AUTHORIZATION_FAILED（用户鉴权或授权失败）<br>- REQUEST_REJECTED_UNSPECIFIED（请求被拒绝，原因未指定）<br>- SERVICE_OPTION_NOT_SUPPORTED（不支持该服务）<br>- REQUESTED_SERVICE_OPTION_NOT_SUBSCRIBED（该服务未订阅）<br>- PTI_ALREADY_IN_USE（PTI正在使用）<br>- REGULAR_DEACTIVATION（常规去激活）<br>- FIVEGS_QOS_NOT_ACCEPTED（不接受的5G QoS）<br>- NETWORK_FAILURE（网络故障）<br>- REACTIVATION_REQUESTED（请求重激活）<br>- SEMANTIC_ERROR_IN_THE_TFT_OPERATION（TFT操作中的语义错误）<br>- SYNTACTICAL_ERROR_IN_THE_TFT_OPERATION（TFT操作中的语法错误）<br>- INVALID_PDU_SESSION_IDENTITY（无效的PDU会话标识）<br>- SEMANTIC_ERRORS_IN_PACKET_FILTERS（数据包过滤器中的语义错误）<br>- SYNTACTICAL_ERROR_IN_PACKET_FILTER（数据包过滤器中的语法错误）<br>- OUT_OF_LADN_SERVICE_AREA（移出LADN服务区）<br>- PTI_MISMATCH（PTI正在使用）<br>- PDU_SESSION_TYPE_IPV4_ONLY_ALLOWED（仅允许IPV4 PDU会话）<br>- PDU_SESSION_TYPE_IPV6_ONLY_ALLOWED（仅允许IPV6 PDU会话）<br>- PDU_SESSION_TYPE_DOES_NOT_EXIST（PDU会话类型不存在）<br>- PDU_SESSION_TYPE_IPV4V6_ONLY_ALLOWED（仅允许IPV4和IPV6 PDU会话）<br>- PDU_TYPE_UNSTRUCTURED_ONLY_ALLOWED（仅允许非结构化的PDU会话）<br>- PDU_SESSION_TYPE_ETHERNET_ONLY_ALLOWED（仅允许以太网类型的PDU会话）<br>- INSUFFICIENT_RESOURCES_FOR_SPECIFIC_SLICE_AND_DNN（特定切片和DNN的资源不足）<br>- INSUFFICIENT_RESOURCES_FOR_SPECIFIC_SLICE（特定切片资源不足）<br>- MISSING_OR_UNKNOWN_DNN_IN_A_SLICE（切片中DNN缺失或未知）<br>- INVALID_PTI_VALUE（无效的PTI值）<br>- MAX_DATA_RATE_FOR_UP_INTEGRITY_PROTECTION_TOO_LOW（用户面完整性保护单用户最大数据速率过低）<br>- SEMANTIC_ERROR_IN_THE_QOS_OPERATION（QoS操作中的语义错误）<br>- SYNTACTICAL_ERROR_IN_THE_QOS_OPERATION（QoS操作中的语法错误）<br>- INVALID_MAPPED_EPS_BEARER_IDENTITY（映射的EPS承载标识无效）<br>- SEMANTICALLY_INCORRECT_MESSAGE（消息中语义不正确）<br>- INVALID_MANDATORY_INFORMATION（必要信息无效）<br>- MESSAGE_TYPE_NONEXIST_OR_NOT_IMPLEMENTED（消息类型不存在或未实施）<br>- MESSAGE_TYPE_NOT_COMPATIBLE_WITH_PROTOCOL_STATE（消息类型与协议状态不兼容）<br>- INFORMATION_ELEMENT_NONEXISTENT_OR_NOT_IMPLEMENTED（信息元素不存在或未实施）<br>- CONDITIONAL_IE_ERROR（条件信元错误）<br>- MESSAGE_NOT_COMPATIBLE_WITH_THE_PROTOCOL_STATE（消息与协议状态不兼容）<br>- PROTOCOL_ERROR_UNSPECIFIED（其它的协议相关错误）<br>- UNSUPPORTED_5QI_VALUE（不支持的5QI值）<br>- NOT_SUPPORTED_SSC_MODE（不支持该SSC模式）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST OVERLOADCTRL查询当前参数配置值。<br>配置原则：无 |
| APNFAULTWAL | APN故障后单进程接入速率(个/秒) | 可选必选说明：该参数在"APNCTRLSWITCH"配置为"ENABLE"时为条件可选参数。<br>参数含义：表示APN故障后单进程接入速率。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~127，单位是个每秒。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST OVERLOADCTRL查询当前参数配置值。<br>配置原则：无 |
| ALARMSWITCH | APN故障告警开关 | 可选必选说明：该参数在"APNCTRLSWITCH"配置为"ENABLE"时为条件可选参数。<br>参数含义：表示APN故障时是否上报告警，当APN故障需要上报告警时，对应的告警为ALM-100449 APN启动故障流控。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE（不使能）<br>- ENABLE（使能）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST OVERLOADCTRL查询当前参数配置值。<br>配置原则：无 |
| GXCTLSWITCH | Gx接口智能流控开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定是否开启Gx接口PCRF智能流控功能。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE（不使能）<br>- ENABLE（使能）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST OVERLOADCTRL查询当前参数配置值。<br>配置原则：无 |
| GYCTLSWITCH | Gy接口智能流控开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定是否开启Gy接口OCS智能流控功能。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE（不使能）<br>- ENABLE（使能）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST OVERLOADCTRL查询当前参数配置值。<br>配置原则：无 |
| GIAUTHCTLSWITCH | AAA鉴权智能流控开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定是否开启AAA鉴权智能流控功能。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE（不使能）<br>- ENABLE（使能）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST OVERLOADCTRL查询当前参数配置值。<br>配置原则：无 |
| GIACCTCTLSWITCH | AAA计费智能流控开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定是否开启AAA计费智能流控功能。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE（不使能）<br>- ENABLE（使能）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST OVERLOADCTRL查询当前参数配置值。<br>配置原则：无 |
| DRACTLSWITCH | GxGy应用的DRA智能流控开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定是否开启Gx/Gy应用的DRA智能流控功能。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE（不使能）<br>- ENABLE（使能）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST OVERLOADCTRL查询当前参数配置值。<br>配置原则：无 |
| GACTLSWITCH | Ga接口智能流控开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定是否开启Ga接口CG智能流控功能。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE（不使能）<br>- ENABLE（使能）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST OVERLOADCTRL查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/OVERLOADCTRL]] · 过载控制的配置信息（OVERLOADCTRL）

## 使用实例

修改配置，CTRLENABLE为：ENABLE,AGINGTIME为：34，SRVTRIGCCRI为：ENABLE，SRVTRIGACCT为：ENABLE，NASCAUSE为：INSUFFICIENT_RESOURCES：

```
SET OVERLOADCTRL: CTRLENABLE=ENABLE,AGINGTIME=34,SRVTRIGCCRI=ENABLE,SRVTRIGACCT=ENABLE,NASCAUSE=INSUFFICIENT_RESOURCES;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-OVERLOADCTRL.md`
