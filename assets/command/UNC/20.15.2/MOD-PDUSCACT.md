---
id: UNC@20.15.2@MMLCommand@MOD PDUSCACT
type: MMLCommand
name: MOD PDUSCACT（修改PDU异常返回码动作）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: PDUSCACT
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
- PDU级结果码处理动作
status: active
---

# MOD PDUSCACT（修改PDU异常返回码动作）

## 功能

**适用NF：PGW-C、SMF**

该命令用于修改PDU异常返回码动作。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CCTMPLTNAME | 融合计费模板名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定融合计费模板的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。不区分大小写。<br>默认值：无<br>配置原则：<br>该参数使用<br>[**ADD CCT**](../融合计费模板/增加融合计费模板（ADD CCT）_09653176.md)<br>命令配置生成。 |
| CODETYPE | 返回码类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定PDU异常返回码类型。<br>数据来源：本端规划<br>取值范围：<br>- “DEFAULT（针对未指定的异常返回码设置处理动作）”：当收到配置指定之外的结果码时需要执行的动作<br>- “VALUE（针对指定异常返回码设置处理动作）”：当收到配置指定的结果码时需要执行的动作<br>默认值：无<br>配置原则：无 |
| STATUSCODE | 状态码 | 可选必选说明：该参数在"CODETYPE"配置为"VALUE"时为条件必选参数。<br>参数含义：该参数用于配置PDU级异常状态返回码。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是300~999，65535。<br>默认值：无<br>配置原则：<br>返回码500,502,504,601,602,603,605的默认动作为FAILOVER。<br>返回码604的默认动作需参考ADD CCT命令中FHACTION的动作，FHACTION为CONTINUE时，604的默认动作为CONTINUE，其余情况的默认动作为TERM_WITH_REL。<br>内部异常码606默认动作：主备Chf在同一个SCP组时，动作同604，否则，默认动作为FAILOVER。<br>其他返回码的默认动作为TERM_WITH_REL。<br>异常码604/605，内部异常码606动作优先级：通过命令ADD PDUSCACT中的参数SCACT配置的异常码动作 > 上述的默认动作 > 通过命令ADD PDUSCACT中参数CODETYPE配置的DEFAULT动作 > 未配置的异常码默认动作。<br>其他异常码动作优先级：通过命令ADD PDUSCACT中的参数SCACT配置的异常码动作 > 通过命令ADD PDUSCACT中参数CODETYPE配置的DEFAULT动作 > 未配置的异常码默认动作。 |
| SCACT | 处理动作 | 可选必选说明：必选参数<br>参数含义：该参数用于指定PDU异常返回码的处理动作。<br>数据来源：本端规划<br>取值范围：<br>- “FAILOVER（进行Failover处理）”：进行Failover处理时，优先按照CHF下发的sessionFailover与failureHandling信元处理，CHF无下发则通过SET FAILHANDLING命令配置的Failover动作处理。<br>- “CONTINUE（允许业务继续进行）”：允许业务继续进行，不再进行配额管理。SMF/PGW-C在PDU会话去活时向CHF上报执行continue动作之后的配额用量。<br>- “TERM_WITH_REL（去活PDU会话，发送Charging Data Request Release消息）”：去活PDU会话，发送Charging Data Request Release消息。<br>- “TERM_NO_REL（去活PDU会话，不发送Charging Data Request Release消息）”：去活PDU会话，不发送Charging Data Request Release消息。<br>- “BLOCK（阻塞业务，使业务不能继续进行）”：阻塞业务，使业务不能继续进行。<br>- “REDIRECT（将当前业务重定向到指定的地址）”：将当前业务重定向到指定的地址。<br>默认值：无<br>配置原则：无 |
| RDVIRTIP | 重定向IPV4地址 | 可选必选说明：该参数在"SCACT"配置为"REDIRECT"时为条件可选参数。<br>参数含义：该参数用于指定PDU异常返回码重定向动作的IPv4地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：<br>不配置此参数时值默认为0.0.0.0。 |
| RDVIRTIPV6 | 重定向IPV6地址 | 可选必选说明：该参数在"SCACT"配置为"REDIRECT"时为条件可选参数。<br>参数含义：该参数用于指定PDU异常返回码重定向动作的IPv6地址。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：<br>不配置此参数时值默认为::。 |
| BLKTIMER | 阻塞处理时间间隔 | 可选必选说明：该参数在"SCACT"配置为"BLOCK"、"REDIRECT"时为条件可选参数。<br>参数含义：该参数用于指定PDU异常返回码阻塞/重定向动作的业务阻塞/重定向时间，从阻塞/重定向开始经过配置时长以后，业务再来时可以重新触发配额申请。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~1440，单位是分钟。<br>默认值：无<br>配置原则：<br>不配置此参数时值默认为0。 |
| GTPV01CAUSE | 原因值GtpV0-1 | 可选必选说明：该参数在"SCACT"配置为"TERM_WITH_REL"、"TERM_NO_REL"时为条件可选参数。<br>参数含义：该参数用于配置当用户因PDU异常结果码被激活失败或更新失败时，在GTPv0或GTPv1消息中传递给左侧网元的Cause值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~255。<br>默认值：无<br>配置原则：<br>不配置此参数时值默认为0。 |
| GTPV2CAUSE | 原因值GtpV2 | 可选必选说明：该参数在"SCACT"配置为"TERM_WITH_REL"、"TERM_NO_REL"时为条件可选参数。<br>参数含义：该参数用于配置当用户因PDU异常结果码被激活失败或更新失败时，在GTPv2消息中传递给左侧网元的Cause值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~255。<br>默认值：无<br>配置原则：<br>不配置此参数时值默认为0。 |
| REACTREQ | 重新激活请求 | 可选必选说明：该参数在"SCACT"配置为"TERM_WITH_REL"、"TERM_NO_REL"时为条件可选参数。<br>参数含义：该参数用于指示当用户因PDU异常结果码被激活失败或更新失败时，SMF是否通知用户重新激活。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE（不使能）<br>- ENABLE（使能）<br>默认值：无<br>配置原则：<br>不配置此参数时值默认为DISABLE（0）。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PDUSCACT]] · PDU异常返回码动作（PDUSCACT）

## 使用实例

修改PDU异常返回码动作配置，CCT名称为“test”，指定异常返回码为400，动作为continue：

```
MOD PDUSCACT: CCTMPLTNAME="test", CODETYPE=VALUE, STATUSCODE=300, SCACT=CONTINUE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-PDUSCACT.md`
