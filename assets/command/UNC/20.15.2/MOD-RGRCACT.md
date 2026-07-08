---
id: UNC@20.15.2@MMLCommand@MOD RGRCACT
type: MMLCommand
name: MOD RGRCACT（修改RG级异常返回码处理动作）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: RGRCACT
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
- RG级结果码处理动作
status: active
---

# MOD RGRCACT（修改RG级异常返回码处理动作）

## 功能

**适用NF：PGW-C、SMF**

该命令用于修改RG级异常返回码的处理动作配置。

## 注意事项

- 该命令执行后立即生效。

- 当异常返回码处理动作配置为重定向时，RDVIRTIP和RDVIRTIPV6之间至少配置一个参数。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CCTMPLTNAME | 融合计费模板名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定融合计费模板名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。不区分大小写。<br>默认值：无<br>配置原则：<br>该参数使用<br>[**ADD CCT**](../融合计费模板/增加融合计费模板（ADD CCT）_09653176.md)<br>命令配置生成。 |
| RCCODE | RG级异常返回码 | 可选必选说明：必选参数<br>参数含义：该参数用于指定RG级异常返回码。<br>数据来源：全网规划<br>取值范围：<br>- “DEFAULT（缺省值）”：当收到配置指定之外的结果码时需要执行的动作。<br>- “SERVICEDENIED（因终端用户限制拒绝服务）”：因为终端用户业务限制而拒绝服务。<br>- “QUOTAMNOTAPPL（转离线计费）”：业务不再做配额管理。<br>- “QUOTALIMITRCH（配额不足）”：配额不足。<br>- “SERVICEREJECT（拒绝服务）”：拒绝服务请求，以终止请求信用的服务。<br>- “USERUNKNOWN（未知用户）”：未知用户。<br>- “RATINGFAILED（计费失败）”：计费失败。<br>默认值：无<br>配置原则：无 |
| RCACT | RG级异常返回码动作 | 可选必选说明：必选参数<br>参数含义：该参数用于指定RG级异常返回码的处理动作。<br>数据来源：全网规划<br>取值范围：<br>- BLCK_TRG_RPT（阻塞业务，后续有Trigger触发时，上报Charging Data Request Update消息）<br>- BLCK_IMMED_RPT（阻塞业务，立即触发一条原因为Final的Charging Data Request Update消息）<br>- BLCK_NO_RPT（阻塞业务）<br>- CONTINUE（允许业务继续进行，不再进行配额管理。SMF/PGW-C在PDU会话去活时向CHF上报执行continue动作之后的配额用量）<br>- TERMINATE（去活PDU会话）<br>- REDIRECT（将当前业务重定向到指定的地址）<br>默认值：无<br>配置原则：无 |
| BLKTIMER | RG级阻塞处理时间间隔(分钟) | 可选必选说明：该参数在"RCACT"配置为"BLCK_IMMED_RPT"、"BLCK_NO_RPT"、"REDIRECT"时为条件可选参数。<br>参数含义：该参数用于指定RG级异常返回码阻塞动作的业务阻塞时间。从阻塞开始经过配置时长以后，业务再来时可以重新触发配额申请。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~1440，单位是分钟。<br>默认值：无<br>配置原则：<br>不配置此参数时值默认为0。 |
| RDVIRTIP | RG级重定向处理重定向IPv4地址 | 可选必选说明：该参数在"RCACT"配置为"REDIRECT"时为条件可选参数。<br>参数含义：该参数用于指定RG级异常返回码重定向动作的IPv4地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：<br>有效的IPv4地址，不允许配置为0.0.0.0~0.255.255.255或255.255.255.255。<br>不配置此参数时值默认为0.0.0.0。 |
| RDVIRTIPV6 | RG级重定向处理重定向IPv6地址 | 可选必选说明：该参数在"RCACT"配置为"REDIRECT"时为条件可选参数。<br>参数含义：该参数用于指定RG级异常返回码重定向动作的IPv6地址。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：<br>有效的IPv6地址，不允许配置为全0或全F。<br>不配置此参数时值默认为::。 |
| REACTREQ | RG级重新激活请求 | 可选必选说明：该参数在"RCACT"配置为"TERMINATE"时为条件可选参数。<br>参数含义：该参数用于指示当用户因RG级异常结果码激活失败或更新失败时，SMF是否通知用户重新激活。<br>数据来源：全网规划<br>取值范围：不配置此参数时值默认为DISABLE（0）。<br>- “DISABLE（不使能）”：不通知用户重新激活<br>- “ENABLE（使能）”：通知用户重新激活<br>默认值：无<br>配置原则：<br>不配置此参数时值默认为DISABLE（0）。 |
| HOLDINGTIME | 用户保持时长(分钟) | 可选必选说明：该参数在"RCACT"配置为"CONTINUE"时为条件可选参数。<br>参数含义：该参数用于指定RG级异常返回码动作是CONTINUE时，允许用户保持业务的时长。超出该时长则去活用户。当取值为0时，不主动去活用户。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~2880，单位是分钟。<br>默认值：无<br>配置原则：<br>该参数在"RCACT"配置为"CONTINUE"时，默认值为30。<br>不配置此参数时值默认为0。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/RGRCACT]] · RG级异常返回码处理动作（RGRCACT）

## 使用实例

如果希望CHF返回RG级异常返回码“SERVICEDENIED”时，执行重定向动作到192.168.10.16，可以使用该命令，修改全局融合计费模板中RG级异常返回码“SERVICEDENIED”的动作为REDIRECT：

```
MOD RGRCACT: CCTMPLTNAME="global", RCCODE=SERVICEDENIED, RCACT=REDIRECT, RDVIRTIP="192.168.10.16";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改RG级异常返回码处理动作（MOD-RGRCACT）_09651367.md`
