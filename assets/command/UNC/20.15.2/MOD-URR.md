---
id: UNC@20.15.2@MMLCommand@MOD URR
type: MMLCommand
name: MOD URR（修改URR）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: URR
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费和策略的业务管理
- 业务策略
- 内容计费标识
status: active
---

# MOD URR（修改URR）

## 功能

**适用NF：PGW-C、SMF**

该命令用于修改使用量上报规则信息。

## 注意事项

- 该命令执行后立即生效。
- 如果引用了该使用量上报规则信息的计费属性记录存在，则当使用量上报模式USAGERPTMODE为在线计费ONLINE时，只允许修改ONLMETERINGTYPE；当使用量上报模式USAGERPTMODE为离线计费OFFLINE时，只允许修改OFFMETERINGTYPEE。
- 当同时配置UPSID、DOWNSID且不配置离线RG时，离线计费话单中RG取值使用配置的DOWNSID值。
- 配置在线计费URR时，如果DCCTEMPLATE的EVENTCHGMOD参数配置为ECUR，则该命令的ONLMETERINGTYPE参数不能配置为EVENT_VOLUME，EVENT_TIME，EVENT_VOLUME_TIME。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| URRNAME | 使用量上报规则名称 | 可选必选说明：必选参数<br>参数含义：该参数用于设置URR名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| URRID | URR标识 | 可选必选说明：可选参数<br>参数含义：该参数用于设置URR标识。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～2147483646。<br>默认值：无<br>配置原则：无 |
| USAGERPTMODE | 使用量上报模式 | 可选必选说明：可选参数<br>参数含义：该参数用于设置计费模式。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- OFFLINE：离线计费，表示该URR为离线计费应用的URR。<br>- ONLINE：在线计费，表示该URR为在线计费应用的URR。<br>- MONITORINGKEY：监控属性值，表示该URR为流量累计应用的Monitoring-Key。<br>- QOS：QoS，表示该URR为QoS保证。<br>默认值：无<br>配置原则：无 |
| OFFCOMPOUNDTYPE | 离线计费标识组成类型 | 可选必选说明：条件必选参数<br>前提条件：该参数在“USAGERPTMODE”配置为“OFFLINE”时为必选参数。<br>参数含义：该参数用于设置离线计费标识组成类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ONLYRG：费率组，表示仅设置离线计费的费率组。<br>- ONLYSID：业务ID，表示仅设置离线计费的业务ID。<br>- UPDOWNSID：上下行业务ID，表示设置离线计费的上下行业务ID。<br>- RGSID：费率组加业务ID，表示设置离线计费的费率组加业务ID。<br>默认值：无<br>配置原则：融合计费场景下，该参数不支持配置为ONLYSID和UPDOWNSID。 |
| ONLCOMPOUNDTYPE | 在线计费标识组成类型 | 可选必选说明：条件必选参数<br>前提条件：该参数在“USAGERPTMODE”配置为“ONLINE”时为必选参数。<br>参数含义：该参数用于设置在线计费标识组成类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ONLYRG：费率组，表示设置在线计费的费率组。<br>- RGSID：费率组加业务ID，表示设置在线计费的费率组加业务ID。<br>默认值：无<br>配置原则：无 |
| RG | 离线计费组 | 可选必选说明：条件必选参数<br>前提条件：该参数在“OFFCOMPOUNDTYPE”配置为“ONLYRG” 或 “RGSID”时为必选参数。<br>参数含义：该参数用于设置离线计费组。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967294。<br>默认值：无<br>配置原则：无 |
| SID | 离线业务标识 | 可选必选说明：条件必选参数<br>前提条件：该参数在“OFFCOMPOUNDTYPE”配置为“ONLYSID” 或 “RGSID”时为必选参数。<br>参数含义：该参数用于设置离线业务标识。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967294。<br>默认值：无<br>配置原则：无 |
| UPSID | 离线上行业务标识 | 可选必选说明：条件必选参数<br>前提条件：该参数在“OFFCOMPOUNDTYPE”配置为“UPDOWNSID”时为必选参数。<br>参数含义：该参数用于设置离线上行业务标识。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967294。<br>默认值：无<br>配置原则：无 |
| DOWNSID | 离线下行业务标识 | 可选必选说明：条件必选参数<br>前提条件：该参数在“OFFCOMPOUNDTYPE”配置为“UPDOWNSID”时为必选参数。<br>参数含义：该参数用于设置离线下行业务标识。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967294。<br>默认值：无<br>配置原则：无 |
| ONLINERG | 在线计费组 | 可选必选说明：条件必选参数<br>前提条件：该参数在“ONLCOMPOUNDTYPE”配置为“ONLYRG” 或 “RGSID”时为必选参数。<br>参数含义：该参数用于设置在线计费组。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967294。<br>默认值：无<br>配置原则：无 |
| ONLINESID | 在线业务标识 | 可选必选说明：条件必选参数<br>前提条件：该参数在“ONLCOMPOUNDTYPE”配置为“RGSID”时为必选参数。<br>参数含义：该参数用于设置在线业务标识。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967294。<br>默认值：无<br>配置原则：无 |
| OFFMETERINGTYPE | 离线计费统计类型 | 可选必选说明：条件可选参数<br>前提条件：该参数在“USAGERPTMODE”配置为“OFFLINE”时为可选参数。<br>参数含义：该参数用于设置离线计费统计类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- VOLUME：按流量计费。<br>- TIME：按时长计费。<br>- EVENT：按事件计费。<br>- FREE：免费。<br>- VOLUME_TIME：按流量和时长计费。<br>- EVENT_VOLUME：按事件和流量计费。<br>- EVENT_TIME：按事件和时长计费。<br>- EVENT_VOLUME_TIME：按事件、流量和时长计费。<br>默认值：无<br>配置原则：如果运营商希望采取计费方式为离线计费。 |
| ONLMETERINGTYPE | 在线计费统计类型 | 可选必选说明：条件可选参数<br>前提条件：该参数在“USAGERPTMODE”配置为“ONLINE”时为可选参数。<br>参数含义：该参数用于设置在线计费统计类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- VOLUME：按流量计费。<br>- TIME：按时长计费。<br>- EVENT：按事件计费。<br>- FREE：免费。<br>- VOLUME_TIME：按流量和时长计费。<br>- EVENT_VOLUME：按事件和流量计费。<br>- EVENT_TIME：按事件和时长计费。<br>- EVENT_VOLUME_TIME：按事件、流量和时长计费。<br>默认值：无<br>配置原则：如果运营商希望采取计费方式为在线计费。 |
| TIMERSUVALUE | 时间配额值（秒） | 可选必选说明：条件可选参数<br>前提条件：该参数在“ONLMETERINGTYPE”配置为“TIME”、“VOLUME_TIME”、“EVENT_TIME” 或 “EVENT_VOLUME_TIME”时为可选参数。<br>参数含义：该参数用于设置计费方式为时长计费，并指定该计费方式与OCS/CHF交互消息中默认请求的时间配额值。<br>数据来源：对端协商<br>取值范围：整数类型，取值范围为0～3600000。<br>默认值：无<br>配置原则：当运营商希望SMF向OCS/CHF申请配额的时候，请求消息中的Requested-Service-Unit中就会携带想要申请的秒数发送到OCS/CHF，则配置该参数。 |
| VOLUMERSUVALUE | 流量配额值（字节） | 可选必选说明：条件可选参数<br>前提条件：该参数在“ONLMETERINGTYPE”配置为“VOLUME”、“VOLUME_TIME”、“EVENT_VOLUME” 或 “EVENT_VOLUME_TIME”时为可选参数。<br>参数含义：该参数用于设置计费方式为流量计费，并指定该计费方式在与OCS/CHF交互消息中默认请求的流量配额值。<br>数据来源：对端协商<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无<br>配置原则：当运营商希望SMF向OCS/CHF申请配额的时候，请求消息中的Requested-Service-Unit中就会携带想要申请的字节数发送到OCS/CHF，则配置该参数。 |
| OFCSRVTMPLNAME | 离线业务模板名 | 可选必选说明：条件可选参数<br>前提条件：该参数在“USAGERPTMODE”配置为“OFFLINE”时为可选参数。<br>参数含义：该参数用于设置离线计费模板名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：<br>- 该参数使用ADD OFCSRVTEMPLATE命令配置生成。<br>- 如果运营商希望基于某种业务配置计费方式，时间阈值，流量阈值等计费属性，可以配置离线模板名称。设置的OFCSRVTMPLNAME必须是系统已经存在的离线模板名称。 |
| REDIRENDTOKEN | Gy重定向结束Token | 可选必选说明：条件可选参数<br>前提条件：该参数在“USAGERPTMODE”配置为“ONLINE”时为可选参数。<br>参数含义：该参数用于设置Gy重定向结束Token。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：如果运营商希望支持Gy接口欠费重定向Token检测上报功能，则配置该参数。 |
| MONITORINGKEY | 监控属性值 | 可选必选说明：条件必选参数<br>前提条件：该参数在“USAGERPTMODE”配置为“MONITORINGKEY”时为必选参数。<br>参数含义：指定监控属性值。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。4294967295是无效值，初始化时MonitoringKey是无效值，不生效。区分大小写。<br>默认值：无<br>配置原则：无 |
| EVENTRSUVALUE | 事件配额值（次） | 可选必选说明：条件可选参数<br>前提条件：该参数在“ONLMETERINGTYPE”配置为“EVENT”、“EVENT_TIME”、“EVENT_VOLUME” 或 “EVENT_VOLUME_TIME”时为可选参数。<br>参数含义：该参数用于设置当业务处于事件计费方式时，与OCS/CHF交互消息中默认请求的事件计费配额值。<br>数据来源：对端协商<br>取值范围：整数类型，取值范围为0～5000。<br>默认值：无<br>配置原则：当运营商希望SMF向OCS/CHF申请配额的时候，请求消息就会携带想要申请的事件计费配额数量发送到OCS/CHF，则配置该参数。 |
| N40AGESW | N40接口场景下是否允许老化 | 可选必选说明：条件可选参数<br>前提条件：该参数在“USAGERPTMODE”配置为“OFFLINE” 或 “ONLINE”时为可选参数。<br>参数含义：该参数用于控制N40接口计费场景，QHT或RG老化功能开启时，是否允许该URR被老化。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- ENABLE：允许该URR被老化。<br>- DISABLE：不允许该URR被老化。<br>默认值：无<br>配置原则：如果配置为“DISABLE”，CHF下发或本地配置的QHT Trigger会被忽略。通过ADD URR/MOD URR命令配置RG关联的SID时，建议RG级URR及其关联的SID级URR都保持该配置参数一致。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/URR]] · URR（URR）

## 使用实例

假如运营商需要修改一个使用量上报规则信息用于在线计费，在线计费统计类型为费率组，计费组设为100，修改在线计费方式为按流量计费：

```
MOD URR: URRNAME="onlineURR", USAGERPTMODE=ONLINE, ONLCOMPOUNDTYPE=ONLYRG, ONLINERG=100, ONLMETERINGTYPE=VOLUME;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改URR（MOD-URR）_09897159.md`
