---
id: UNC@20.15.2@MMLCommand@ADD MSCCRCACT
type: MMLCommand
name: ADD MSCCRCACT（增加MSCC层异常返回码处理动作）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: MSCCRCACT
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
max_records: 2020
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 在线计费
- 信用控制
- Mscc层返回码控制
status: active
---

# ADD MSCCRCACT（增加MSCC层异常返回码处理动作）

## 功能

**适用NF：PGW-C、SMF**

该命令用于增加MSCC层异常返回码的处理动作配置。当OCS返回的CCA消息携带MSCC层异常返回码时，根据此配置进行处理。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为2020。
- 该命令基于在线计费模板设置MSCC层异常返回码的动作配置，单个在线计费模板中最多配置20个MSCC层异常返回码处理动作。
- 当MSCC层异常返回码处理动作配置为重定向时，MSCCRDVIRTIP和MSCCRDVIRTIPV6之间至少配置一个参数。
- 返回码DIAMETER_SUCCESS（2001），DIAMETER_LIMITED_SUCCESS（2002）的动作不可以使用ADD MSCCRCACT命令配置。当收到没有使用ADD MSCCRCACT命令配置处理动作的返回码时，按照SET MSCCLEVDFTBEH命令配置的缺省处理动作处理。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DCCTMPLTNAME | 在线计费模板名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定在线计费模板名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：<br>- 该参数使用ADD DCCTEMPLATE命令配置生成。<br>- 配置该参数前，需要先使用ADD DCCTEMPLATE命令配置在线计费模板。如果配置为global则表示全局在线计费模板。 |
| MSCCRC | MSCC层异常返回码 | 可选必选说明：必选参数<br>参数含义：该参数用于指定MSCC层异常返回码。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～4。<br>默认值：无<br>配置原则：<br>- MSCC层异常返回码参数可以指定单个异常返回码或范围异常返回码，当参数指定为1xxx时，代表1000~1999范围内所有异常返回码。配置的单个异常返回码落在一个范围异常返回码内时，单个异常返回码的优先级高。<br>- 返回码DIAMETER_SUCCESS （2001），DIAMETER_LIMITED_SUCCESS （2002）的动作不可配置，都对应成功，正常转发报文并计费。<br>- 返回码DIAMETER_CREDIT_CONTROL_NOT_APPLICABLE （4011）的默认动作为免费使用业务。 |
| MSCCRCACT | MSCC层异常返回码动作 | 可选必选说明：必选参数<br>参数含义：该参数用于指定MSCC层异常返回码的处理动作。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- BLOCK：阻塞业务。<br>- BLCK_TRG_RPT：阻塞业务，后续有Trigger触发时，上报该业务。Trigger主要是指PDP上下文更新、RAR、VT等。<br>- BLCK_IMMED_RPT：阻塞业务，立即触发一条原因为Final的CCR-U消息，后续该业务是否上报受参数MSCCBLKTIMER控制。<br>- BLCK_NO_RPT：阻塞业务，后续该业务是否上报受参数MSCCBLKTIMER控制。<br>- CONTINUE：允许业务继续进行，不进行在线计费控制。如果离线计费使能，则产生话单。如果离线计费不使能，则允许业务继续进行，只是不进行在线计费控制。<br>- TERMINATE：去活PDP上下文。<br>- REDIRECT：将当前业务重定向到指定的地址。<br>- INHERIT：指定继承全局在线计费模板中的配置。<br>默认值：无<br>配置原则：<br>- 该参数配置为INHERIT时，表示继承全局在线计费模板中相同返回码的动作。在线计费模板名称参数配置为global时，该参数不能配置为INHERIT。<br>- 当激活触发的CCA-I消息携带的异常返回码动作为TERM_WITH_CCRT，如果byte116 bit4或者bit5没有开启，则会去活PDP上下文，不发送CCR-T。<br>- 当CCA异常结果码动作配置为BLCK_IMMED_RPT，没有配置MSCCBLKTIMER时： 1）SESSIONMODE设置为MULTIPLE，业务不会受阻，新业务会触发CCR-I。 2）SESSIONMODE设置为SINGLE，业务会受阻。 |
| MSCCBLKTIMER | MSCC层阻塞处理时间间隔 | 可选必选说明：条件可选参数<br>前提条件：该参数在“MSCCRCACT”配置为“BLCK_IMMED_RPT” 或 “BLCK_NO_RPT”时为可选参数。<br>参数含义：该参数用于指定MSCC层异常返回码阻塞动作的业务阻塞时间。从阻塞开始经过配置时长以后，业务再来时可以重新触发配额申请。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～1440，单位是分钟。<br>默认值：无<br>配置原则：不配置此参数时值默认为0。 |
| MSCCRDVIRTIP | MSCC层重定向处理重定向IPv4地址 | 可选必选说明：条件可选参数<br>前提条件：该参数在“MSCCRCACT”配置为“REDIRECT”时为可选参数。<br>参数含义：该参数用于指定MSCC层异常返回码重定向动作的IPv4地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：<br>- 有效的IPv4地址，不允许配置为0.0.0.0或255.255.255.255。<br>- 不配置此参数时值默认为0.0.0.0。 |
| MSCCRDVIRTIPV6 | MSCC层重定向处理重定向IPv6地址 | 可选必选说明：条件可选参数<br>前提条件：该参数在“MSCCRCACT”配置为“REDIRECT”时为可选参数。<br>参数含义：该参数用于指定MSCC层异常返回码重定向动作的IPv6地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：<br>- 有效的IPv6地址，不允许配置为全0或全F。<br>- 不配置此参数时值默认为::。 |
| MSCCREACTREQ | MSCC层重新激活请求 | 可选必选说明：条件可选参数<br>前提条件：该参数在“MSCCRCACT”配置为“TERMINATE”时为可选参数。<br>参数含义：该参数用于指示当用户因MSCC层异常结果码被去活时，UNC是否通知用户重新激活。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：否。<br>- ENABLE：是。<br>默认值：DISABLE<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/MSCCRCACT]] · MSCC层异常返回码处理动作（MSCCRCACT）

## 使用实例

如果希望OCS返回MSCC层异常返回码5012时，去活PDP上下文，可以在全局在线计费模板中配置MSCC层异常返回码5012的动作为TERMINATE：

```
ADD MSCCRCACT:DCCTMPLTNAME="global",MSCCRC="5012",MSCCRCACT=TERMINATE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加MSCC层异常返回码处理动作（ADD-MSCCRCACT）_09896940.md`
