---
id: UNC@20.15.2@MMLCommand@MOD CCT
type: MMLCommand
name: MOD CCT（修改融合计费模板）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: CCT
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 融合计费
- 融合计费模板
status: active
---

# MOD CCT（修改融合计费模板）

## 功能

**适用NF：PGW-C、SMF**

该命令用于修改融合计费模板（Converged Charging Template），用于配置融合计费相关参数。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CCTMPLTNAME | 融合计费模板名称 | 可选必选说明：必选参数<br>参数含义：该参数用于设置融合计费模板名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。不区分大小写。<br>默认值：无<br>配置原则：无 |
| QHT | 配额空闲时间门限值(秒) | 可选必选说明：可选参数<br>参数含义：该参数用于设置配额空闲时间门限值，数据包停止传送后，QHT立即开始计时，当数据包停止传送时间达到此门限值，向CHF上报使用的配额。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0，5~3600。<br>默认值：无<br>配置原则：<br>当同时满足下述条件时，该参数生效：<br>该业务QHT Trigger生效，未下发QHT或下发QHT为0。<br>该参数配置不为0。 |
| VQT | 流量阈值触发百分比(%) | 可选必选说明：可选参数<br>参数含义：该参数用于设置一个流量阈值，当有数据包到达时，SMF/PGW-C必须计算剩余的流量配额，如果剩余的配额小于等于流量阈值便触发一个Charging Data Request消息，消息中要包含已使用的数据流量。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~50。<br>默认值：无<br>配置原则：无 |
| TQT | 时间阈值触发百分比(%) | 可选必选说明：可选参数<br>参数含义：该参数用于设置一个时间阈值，当有数据包到达时，SMF/PGW-C必须计算剩余的时间配额，如果剩余的配额小于等于时间阈值便触发一个Charging Data Request消息，消息中要包含已使用的数据流量。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~50。<br>默认值：无<br>配置原则：无 |
| UQT | 事件阈值触发百分比(%) | 可选必选说明：可选参数<br>参数含义：该参数用于设置一个事件阈值，当有事件成功时，SMF/PGW-C必须计算剩余的事件配额，如果剩余的配额小于等于事件阈值便触发一个Charging Data Request消息，消息中要包含已使用的数据流量。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~50。<br>默认值：无<br>配置原则：无 |
| VT | 在线配额有效时长(分) | 可选必选说明：可选参数<br>参数含义：该参数用于设置RG级配额的有效时长；SMF/PGW-C收到CHF下发的配额后按有效时长启定时器，超时后SMF/PGW-C立即向CHF上报配额用量并申请新配额。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0，5~1440。<br>默认值：无<br>配置原则：无 |
| MAXNUMOFCCC | 计费条件改变阈值 | 可选必选说明：可选参数<br>参数含义：该参数用于指定计费条件改变几次后会触发Charging Data Request Update消息。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~10。<br>默认值：无<br>配置原则：无 |
| PDUVOLUMELIMIT | PDU流量阈值(MB) | 可选必选说明：可选参数<br>参数含义：该参数用于指定PDU级触发Charging Data Request Update消息的流量阈值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~2147483647，单位是兆字节。备注：1兆字节为1048576字节。<br>默认值：无<br>配置原则：无 |
| PDUTIMELIMIT | PDU时长阈值(分钟) | 可选必选说明：可选参数<br>参数含义：该参数用于指定PDU级别触发Charging Data Request Update消息的时长阈值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~1440。<br>默认值：无<br>配置原则：无 |
| RGVOLUMELIMIT | 业务级流量阈值(MB) | 可选必选说明：可选参数<br>参数含义：该参数用于指定RG级别触发Charging Data Request Update消息的流量阈值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~2147483647，单位是兆字节。备注：1兆字节为1048576字节。<br>默认值：无<br>配置原则：无 |
| RGTIMELIMIT | 业务级时长阈值(分钟) | 可选必选说明：可选参数<br>参数含义：该参数用于指定RG级别触发Charging Data Request Update消息的时长阈值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~1440。<br>默认值：无<br>配置原则：无 |
| QFVOLUMELIMIT | QF流量阈值(MB) | 可选必选说明：可选参数<br>参数含义：该参数用于指定QF级别触发Charging Data Request Update消息的流量阈值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~2147483647，单位是兆字节。备注：1兆字节为1048576字节。<br>默认值：无<br>配置原则：无 |
| QFTIMELIMIT | QF时长阈值(分钟) | 可选必选说明：可选参数<br>参数含义：该参数用于指定QF级别触发Charging Data Request Update消息的时长阈值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~1440。<br>默认值：无<br>配置原则：无 |
| UCITIMER | 业务停止时长(分钟) | 可选必选说明：可选参数<br>参数含义：该参数用于配置PDU会话业务停止时长，超过该时长后SMF/PGW-C会向CHF发送Charging Data Request Release消息释放会话。<br>数据来源：对端协商<br>取值范围：整数类型，取值范围是0~1440。<br>默认值：无<br>配置原则：<br>当前版本暂不支持UCITIMER参数。 |
| FUATERMINATE | 最终配额动作指示终结方式 | 可选必选说明：可选参数<br>参数含义：该参数用于配置融合计费模板中最终配额动作指示终结方式。<br>数据来源：本端规划<br>取值范围：<br>- “TERM_SERVICE（阻塞业务）”：阻塞业务<br>- “TERM_SESSION（去活用户）”：去活用户<br>默认值：无<br>配置原则：无 |
| TIMEFORMAT | 时间格式 | 可选必选说明：可选参数<br>参数含义：该参数用于指定融合计费消息的时间格式。<br>数据来源：本端规划<br>取值范围：<br>- “LocalTime（本地时间）”：指定发给CHF的消息中的时间格式为localtime。localtime表示本地时间，是指根据时区或者当地的夏令时规定而设置的时间<br>- “UTC（世界协调时间）”：指定发给CHF的消息中的时间格式为UTC。UTC表示（Universal Time Coordinated）世界协调时间，时区的改变以及夏令时的实施都不会改变UTC时间。<br>默认值：无<br>配置原则：无 |
| MAXSVCCONTAINER | 最大携带的业务容器数量 | 可选必选说明：可选参数<br>参数含义：用于指定N40接口消息中最大携带的业务容器数量。当消息中业务容器数量大于等于该值，会强制发送一个N40接口更新消息给CHF，并携带TriggerType为“MANAGEMENT_INTERVENTION”。取值0表示对消息中的业务容器数量不做限制。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~100。<br>默认值：无<br>配置原则：无 |
| SECRUTHRESHOLD | RAN-SecondaryRAT-Usage-Report上报CHF的阈值 | 可选必选说明：可选参数<br>参数含义：用于指定RAN-SecondaryRAT-Usage-Report上报CHF更新消息的阈值。取值0表示对消息中的RAN-SecondaryRAT-Usage-Report个数不做限制。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~100。<br>默认值：无<br>配置原则：无 |
| MAXUSEDSRVNUM | 最大可使用的业务个数 | 可选必选说明：可选参数<br>参数含义：用于配置用户最多可以同时访问的业务（RG/RG+SID）个数，当用户访问的业务超过该配置时，用户会被去活。取值0表示用户同时访问的业务个数不受本命令限制。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~100。<br>默认值：无<br>配置原则：无 |
| QHTRPTTRIGGER | QHT超时触发的容器中Trigger的值 | 可选必选说明：可选参数<br>参数含义：该参数用于控制业务QHT超时触发的NCHF消息容器中Trigger的值。<br>数据来源：本端规划<br>取值范围：<br>- “QHT（上报QHT）”：Nchf消息容器中Trigger的值填写QHT。<br>- “FINAL（上报FINAL）”：Nchf消息容器中Trigger的值填写FINAL。<br>默认值：无<br>配置原则：<br>在话单缓存场景下，QHT超时触发的NCHF消息容器中Trigger的值直接填写FINAL，不受该参数控制。 |
| ROAMFUATERMACT | 漫游用户最终配额动作指示终结方式 | 可选必选说明：该参数在"FUATERMINATE"配置为"TERM_SERVICE"时为条件可选参数。<br>参数含义：该字段用于配置漫游用户最终配额动作指示终结方式。<br>数据来源：本端规划<br>取值范围：<br>- “TERM_SERVICE（阻塞业务）”：阻塞业务<br>- “TERM_SESSION（去活用户）”：去活用户<br>默认值：无<br>配置原则：无 |
| ROAMVOLUMELIMIT | 漫游用户的PDU流量阈值(MB) | 可选必选说明：可选参数<br>参数含义：该参数用于指定漫游用户的PDU级触发Charging Data Request Update消息的流量阈值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~2147483647，单位是兆字节。<br>默认值：无<br>配置原则：<br>取值为0时，默认PDU阈值取自参数PDUVOLUMELIMIT。<br>取值为1~20时，漫游用户流量阈值取值为20MB。<br>取值为21~2147483647时，漫游用户流量阈值取值为具体参数值。 |
| BLKFREESRV | 会话层异常返回码动作为Block时阻塞免费业务 | 可选必选说明：可选参数<br>参数含义：该参数用于配置会话层异常返回码动作为Block时是否阻塞免费业务。<br>数据来源：本端规划<br>取值范围：<br>- “PASS（不阻塞）”：不阻塞免费业务。<br>- “BLOCK（阻塞）”：阻塞免费业务。<br>默认值：无<br>配置原则：无 |
| NOQUOTATRIGGER | 无配额更新开关 | 可选必选说明：可选参数<br>参数含义：该参数用于控制业务无配额（阻塞或重定向）场景，是否允许在接入侧更新或PDU会话级阈值到触发上报时发起配额更新请求。<br>数据来源：本端规划<br>取值范围：<br>- “ENABLE（使能）”：允许在接入侧更新或PDU会话级阈值到触发上报时发起配额更新请求。<br>- “DISABLE（不使能）”：不允许在接入侧更新或PDU会话级阈值到触发上报时发起配额更新请求，保持阻塞状态。<br>默认值：无<br>配置原则：<br>当该业务处于Block Timer期间时，该参数不生效。<br>当NOQUOTATRIGGER配置为DISABLE时，如果待上报的更新消息中没有MultipleUnitUsage时，是否上报CHF受CNVRGDCHGPARA命令NOSRVRPTSW参数控制。 |
| QHTEXPIREDRSU | QHT超时触发的N40消息的MUU中是否携带RSU | 可选必选说明：可选参数<br>参数含义：该参数用于配置QHT超时触发的N40 ChargingDataUpdateRequest消息中的MultipleUnitUsage是否携带RequestedUnit。<br>数据来源：本端规划<br>取值范围：<br>- “WITH_RSU（携带RSU）”：QHT超时触发的N40请求消息中携带RSU。<br>- “WITHOUT_RSU（不携带RSU）”：QHT超时触发的N40请求消息中不携带RSU。<br>默认值：无<br>配置原则：<br>如果此参数设置为WITH_RSU，则不建议SET CNVRGDCHGPARA中的DELDYNRULENTYUP设置为DISABLE，否则会导致动态规则创建的动态URR无法通过QHT功能老化。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/CCT]] · 融合计费模板（CCT）

## 使用实例

修改名为“Cct”的CCT融合计费模板，业务级流量阈值为1800MB：

```
MOD CCT: CCTMPLTNAME="Cct", RGVOLUMELIMIT=1800;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-CCT.md`
