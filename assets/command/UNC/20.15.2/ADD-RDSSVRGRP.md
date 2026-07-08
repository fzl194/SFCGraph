---
id: UNC@20.15.2@MMLCommand@ADD RDSSVRGRP
type: MMLCommand
name: ADD RDSSVRGRP（增加Radius服务器组）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: RDSSVRGRP
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
max_records: 1600
category_path:
- 业务服务管理
- 会话管理
- RADIUS管理
- 连接管理
- Radius服务器组
status: active
---

# ADD RDSSVRGRP（增加Radius服务器组）

## 功能

**适用NF：PGW-C、SMF**

该命令用来配置RADIUS服务器组信息，具体为：

1、配置RADIUS服务器组名称。

2、配置RADIUS服务器组工作模式。

3、配置RADIUS服务器组可选计费消息属性。

4、配置RADIUS服务器组是否支持利用鉴权服务器计费特性。

5、配置RADIUS消息的超时时间和重发次数。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1600。当配置记录数大于规格的98%时，会上报“ALM-135602215 配置数量超阈值”告警。当配置记录数小于等于配置规格95%时，恢复“ALM-135602215 配置数量超阈值”告警。阈值可以通过MOD CFGTHRESHOLD命令修改。
- 没有配置主备服务器的情况下不能配置抄送服务器。
- 在前期规划时，建议产品配置的等待右侧网元的最大时长小于左侧（MME\SGSN等）的T3N3时长，避免右侧网元无响应造成激活响应的总时长过长。如果涉及产品与多个右侧网元交互的场景，请联系华为公司研发人员给出推荐值。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RDSSVRGRPNAME | Radius Server Group名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定RADIUS服务器组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：无 |
| MODE | 模式 | 可选必选说明：可选参数<br>参数含义：该参数用于指定RADIUS服务器组模式。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- MASTER_SLAVE：配置RADIUS服务器组为主备模式。<br>- ROUND_ROBIN：配置RADIUS服务器组为负荷分担模式。<br>默认值：MASTER_SLAVE<br>配置原则：无 |
| ACCTONACTIVE | Accounting Request ON应答之前是否激活用户 | 可选必选说明：条件可选参数<br>前提条件：该参数在“SIGOPTACCTMSG”配置为“ENABLE”时为可选参数。<br>参数含义：该参数用于指定Accounting Request ON应答之前是否允许激活用户。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- DISABLE：Accounting Request ON应答之前不允许激活用户。<br>- ENABLE：Accounting Request ON应答之前允许激活用户。<br>默认值：DISABLE<br>配置原则：在锁APN去活用户的场景下，该参数不生效。 |
| ACCTTOAUTH | 利用鉴权服务器计费 | 可选必选说明：可选参数<br>参数含义：该参数用于指定RADIUS服务器组是否支持利用鉴权服务器计费特性。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- DISABLE：表示RADIUS服务器组不支持利用鉴权服务器计费特性。<br>- ENABLE：表示RADIUS服务器组支持利用鉴权服务器计费特性。<br>默认值：DISABLE<br>配置原则：无 |
| DSCPV | DSCP值 | 可选必选说明：可选参数<br>参数含义：该参数用于指定信令报文的DSCP值。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为0～63，255。<br>默认值：255<br>配置原则：无 |
| SIGOPTACCTMSG | 支持可选计费消息 | 可选必选说明：可选参数<br>参数含义：该参数用于指定是否支持可选计费消息。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- DISABLE：表示不支持可选计费消息。即UNC重新启动后不发送Accounting Request OFF消息和Accounting Request ON消息。<br>- ENABLE：表示支持可选计费消息，即UNC重新启动后先发Accounting Request OFF消息，再发送Accounting Request ON消息通知已配置的AAA计费服务器。<br>默认值：DISABLE<br>配置原则：无 |
| ONOFFWAITTIME | Accounting Request On/Off消息间的时间间隔（秒） | 可选必选说明：条件可选参数<br>前提条件：该参数在“SIGOPTACCTMSG”配置为“ENABLE”时为可选参数。<br>参数含义：该参数用于指定Accounting Request On/Off消息间的时间间隔。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为0～999。<br>默认值：9<br>配置原则：该参数在“SIGOPTACCTMSG”配置为“ENABLE”时为条件可选参数。 |
| ONRETRANSMIT | Accounting Request On重发次数 | 可选必选说明：条件可选参数<br>前提条件：该参数在“SIGOPTACCTMSG”配置为“ENABLE”时为可选参数。<br>参数含义：该参数用于指定Accounting Request On重发次数。当取值为255时表示不限制重发次数。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为0～5，255。<br>默认值：3<br>配置原则：该参数在“SIGOPTACCTMSG”配置为“ENABLE”时为条件可选参数。 |
| ONTIMEOUT | Accounting Request On超时时间 (秒) | 可选必选说明：条件可选参数<br>前提条件：该参数在“SIGOPTACCTMSG”配置为“ENABLE”时为可选参数。<br>参数含义：该参数用于指定Accounting Request On超时时间。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为3～120，单位是秒。<br>默认值：3<br>配置原则：该参数在“SIGOPTACCTMSG”配置为“ENABLE”时为条件可选参数。 |
| OFFRETRANSMIT | Accounting Request Off重发次数 | 可选必选说明：条件可选参数<br>前提条件：该参数在“SIGOPTACCTMSG”配置为“ENABLE”时为可选参数。<br>参数含义：该参数用于指定Accounting Request Off重发次数。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为0～5。<br>默认值：3<br>配置原则：该参数在“SIGOPTACCTMSG”配置为“ENABLE”时为条件可选参数。 |
| OFFTIMEOUT | Accounting Request Off超时时间(秒) | 可选必选说明：条件可选参数<br>前提条件：该参数在“SIGOPTACCTMSG”配置为“ENABLE”时为可选参数。<br>参数含义：该参数用于指定Accounting Request Off超时时间。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为3～120，单位是秒。<br>默认值：3<br>配置原则：该参数在“SIGOPTACCTMSG”配置为“ENABLE”时为条件可选参数。 |
| ACCTTIMEOUT | Radius Accounting Request超时时间 (秒) | 可选必选说明：可选参数<br>参数含义：该参数用于指定Radius计费消息超时时间。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为1～10，单位是秒。<br>默认值：3<br>配置原则：无 |
| ACCTRETRANSMIT | Radius Accounting Request重发次数 | 可选必选说明：可选参数<br>参数含义：该参数用于指定UNC在未收到Radius计费响应消息时的重发请求消息最大次数，重发次数为0表示不重发。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为0～5。<br>默认值：3<br>配置原则：无 |
| AUTHTIMEOUT | Radius Authentication Request超时时间 (秒) | 可选必选说明：可选参数<br>参数含义：该参数用于指定Radius鉴权消息超时时间。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为1～10，单位是秒。<br>默认值：3<br>配置原则：无 |
| AUTHRETRANSMIT | Radius Authentication Request重发次数 | 可选必选说明：可选参数<br>参数含义：该参数用于指定UNC在未收到Radius鉴权响应消息时的重发请求消息最大次数，重发次数为0表示不重发。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为0～5。<br>默认值：3<br>配置原则：无 |
| ACCTSVRTOUT | Radius Accounting超时时长 (秒) | 可选必选说明：可选参数<br>参数含义：该参数用于指定Radius计费服务器超时时长。在该时间内如果未收到Radius计费服务器任何响应，UNC则将该Radius计费服务器状态设置为DOWN。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为1～60，单位是秒。<br>默认值：12<br>配置原则：无 |
| ACCTSVRDTIME | Radius计费服务器Down状态保持时长 (秒) | 可选必选说明：可选参数<br>参数含义：该参数用于指定Radius计费服务器Down状态的保持时长。超时后，UNC会认为该Radius计费服务器状态恢复可继续向其发送消息。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为1～3600，单位是秒。<br>默认值：180<br>配置原则：无 |
| AUTHSVRTOUT | Radius鉴权服务器超时时长 (秒) | 可选必选说明：可选参数<br>参数含义：该参数用于指定Radius鉴权服务器超时时长。在该时间内如果未收到Radius鉴权服务器任何响应，UNC则将该Radius鉴权服务器状态设置为DOWN。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为1～60，单位是秒。<br>默认值：12<br>配置原则：无 |
| AUTHSVRDTIME | Radius鉴权服务器Down状态保持时长 (秒) | 可选必选说明：可选参数<br>参数含义：该参数用于指定Radius鉴权服务器Down状态的保持时长。超时后，UNC会认为该Radius鉴权服务器状态恢复可继续向其发送消息。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为1～3600，单位是秒。<br>默认值：180<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/RDSSVRGRP]] · Radius服务器组（RDSSVRGRP）

## 使用实例

增加名为rsg的RADIUS服务器组：

```
ADD RDSSVRGRP:RDSSVRGRPNAME="rsg",SIGOPTACCTMSG=ENABLE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-RDSSVRGRP.md`
