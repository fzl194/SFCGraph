---
id: UNC@20.15.2@MMLCommand@MOD CMDRCACT
type: MMLCommand
name: MOD CMDRCACT（修改命令层异常返回码处理动作）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: CMDRCACT
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
- 在线计费
- 信用控制
- 命令层返回码控制
status: active
---

# MOD CMDRCACT（修改命令层异常返回码处理动作）

## 功能

**适用NF：PGW-C、SMF**

该命令用于修改命令层异常返回码的处理动作配置。

## 注意事项

- 该命令执行后立即生效。
- 当命令层异常返回码处理动作配置为重定向时，CMDRDVIRTIP和CMDRDVIRTIPV6之间至少配置一个参数。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DCCTMPLTNAME | 在线计费模板名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定在线计费模板名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：<br>- 该参数使用ADD DCCTEMPLATE命令配置生成。<br>- 配置该参数前，需要先使用ADD DCCTEMPLATE命令配置在线计费模板。如果配置为global则表示全局在线计费模板。 |
| CMDRC | 命令层异常返回码 | 可选必选说明：必选参数<br>参数含义：该参数用于指定命令层异常返回码。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～4。<br>默认值：无<br>配置原则：<br>- 命令层异常返回码参数可以指定单个异常返回码或范围异常返回码，当参数指定为1xxx时，代表1000~1999范围内所有异常返回码。配置的单个异常返回码落在一个范围异常返回码内时，单个异常返回码的优先级高。<br>- 返回码DIAMETER_SUCCESS （2001），DIAMETER_LIMITED_SUCCESS （2002）的动作不可配置，都对应成功，正常转发报文并计费。<br>- 返回码DIAMETER_UNABLE_TO_DELIVER （3002）的默认动作为选择其他的可用Gy对端重发CCR消息。<br>- 返回码DIAMETER_TOO_BUSY （3004）的默认动作为选择其他的可用Gy对端重发CCR消息。<br>- 返回码DIAMETER_LOOP_DETECTED （3005）的默认动作为选择其他的可用Gy对端重发CCR消息。<br>- 返回码DIAMETER_UNKNOWN_PEER （3010）的默认动作为选择其他的可用Gy对端重发CCR消息。<br>- 返回码DIAMETER_OUT_OF_SPACE （4002）的默认动作为选择其他的可用Gy对端重发CCR消息。<br>- 返回码DIAMETER_CREDIT_CONTROL_NOT_APPLICABLE （4011）的默认动作为免费使用业务。<br>- 返回码DIAMETER_UNKNOWN_SESSION_ID （5002）的默认动作为去激活PDP上下文。<br>- 返回码DIAMETER_AUTHORIZATION_REJECTED （5003）的默认动作为PDP上下文激活后，去激活PDP上下文并发送CCR消息。PDP上下文激活过程中，激活失败。<br>- 返回码DIAMETER_USER_UNKNOWN （5030）的默认动作为PDP上下文激活后，去激活PDP上下文并发送CCR消息。PDP上下文激活过程中，激活失败。 |
| CMDRCACT | 命令层异常返回码处理动作 | 可选必选说明：必选参数<br>参数含义：该参数用于指定命令层异常返回码的处理动作。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- FAILOVER：进行Failover处理。<br>- CONTINUE：允许业务继续进行，不进行在线计费控制。如果离线计费使能，则产生话单。如果离线计费不使能，则允许业务继续进行，只是不进行在线计费控制。<br>- TERM_NO_CCRT：去活PDP上下文，不发送CCR-T消息。<br>- TERM_WITH_CCRT：去活PDP上下文，发送CCR-T消息。<br>- BLOCK：阻塞业务，使业务不能继续进行。<br>- REDIRECT：将当前业务重定向到指定的地址。<br>- INHERIT：指定继承全局在线计费模板中的配置。<br>默认值：无<br>配置原则：<br>- 该参数配置为INHERIT时，表示继承全局在线计费模板中相同返回码的动作。在线计费模板名称参数配置为global时，该参数不能配置为INHERIT。<br>- 当激活触发的CCA-I消息携带的异常返回码动作为TERM_WITH_CCRT，如果byte116 bit4或者bit5没有开启，则会去活PDP上下文，不发送CCR-T。 |
| CMDRCGTPV01 | 命令层去活原因值GtpV0-1 | 可选必选说明：条件可选参数<br>前提条件：该参数在“CMDRCACT”配置为“TERM_NO_CCRT” 或 “TERM_WITH_CCRT”时为可选参数。<br>参数含义：该参数用于指定Gy接口对端返回命令层异常返回码导致PDP激活失败或更新失败时，UNC通过左侧接口（Pa）在GTPv0或GTPv1消息中传递给左侧网元（SGSN）的Cause值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0，192～255。<br>默认值：无<br>配置原则：不配置此参数时Cause值按照系统默认方式填写：PDP更新失败Cause值填写System Failure 204。GTPv0和GTPv1 Cause值定义参考3GPP协议TS 29.061。 |
| CMDRCGTPV2 | 命令层去活原因值GtpV2 | 可选必选说明：条件可选参数<br>前提条件：该参数在“CMDRCACT”配置为“TERM_NO_CCRT” 或 “TERM_WITH_CCRT”时为可选参数。<br>参数含义：该参数用于指定Gy接口对端返回命令层异常返回码导致承载激活失败或更新失败时，UNC通过左侧接口（S5/S8，S11）在GTPv2消息中传递给左侧网元（SGW，MME）的Cause值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0，64～239。<br>默认值：无<br>配置原则：不配置此参数时Cause值按照系统默认方式填写：承载更新失败Cause值填写System Failure 72。GTPv2 Cause值定义参考3GPP协议TS 29.274。 |
| CMDRDVIRTIP | 命令层重定向处理重定向IPv4地址 | 可选必选说明：条件可选参数<br>前提条件：该参数在“CMDRCACT”配置为“REDIRECT”时为可选参数。<br>参数含义：该参数用于指定命令层异常返回码重定向动作的IPv4地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：有效的IPv4地址，不允许配置为0.0.0.0或255.255.255.255。 |
| CMDRDVIRTIPV6 | 命令层重定向处理重定向IPv6地址 | 可选必选说明：条件可选参数<br>前提条件：该参数在“CMDRCACT”配置为“REDIRECT”时为可选参数。<br>参数含义：该参数用于指定命令层异常返回码重定向动作的IPv6地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：有效的IPv6地址，不允许配置为全0或全F。 |
| CMDLEVREACTREQ | 命令层重新激活请求 | 可选必选说明：条件可选参数<br>前提条件：该参数在“CMDRCACT”配置为“TERM_NO_CCRT” 或 “TERM_WITH_CCRT”时为可选参数。<br>参数含义：该参数用于指示当用户因命令层异常结果码被去活时，UNC是否通知用户重新激活。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：否。<br>- ENABLE：是。<br>默认值：无<br>配置原则：无 |
| CCAHOLDTIME | CCA Holding Timer开关 | 可选必选说明：条件可选参数<br>前提条件：该参数在“CMDRCACT”配置为“CONTINUE”时为可选参数。<br>参数含义：该参数用于指定CCA返回码动作为Continue时，是否开启Holding Timer控制用户在线时间。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：关闭。<br>- ENABLE：打开。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [命令层异常返回码处理动作（CMDRCACT）](configobject/UNC/20.15.2/CMDRCACT.md)

## 使用实例

如果希望OCS返回命令层异常返回码5012时，执行重定向动作到192.168.10.16，可以使用该命令，修改全局在线计费模板中命令层异常返回码5012的动作为REDIRECT：

```
MOD CMDRCACT:DCCTMPLTNAME="global",CMDRC="5012",CMDRCACT=REDIRECT, CMDRDVIRTIP="192.168.10.16";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改命令层异常返回码处理动作（MOD-CMDRCACT）_09896946.md`
