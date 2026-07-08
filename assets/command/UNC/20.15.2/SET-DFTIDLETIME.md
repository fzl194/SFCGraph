---
id: UNC@20.15.2@MMLCommand@SET DFTIDLETIME
type: MMLCommand
name: SET DFTIDLETIME（设置默认空闲上下文定时器配置）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: DFTIDLETIME
command_category: 配置类
applicable_nf:
- SGW-C
- PGW-C
- SMF
- GGSN
effect_mode: 对新用户生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 接入管理运维
- SMF公共配置
- 空闲上下文定时器
status: active
---

# SET DFTIDLETIME（设置默认空闲上下文定时器配置）

## 功能

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用于设置全局的默认空闲上下文定时器和不活动上下文定时器开关和时长。

- 空闲上下文定时器：会话无数据传输的时长超过定时器时长后，删除会话、承载或Qos Flow。对2G、3G、4G和5G用户都生效。
- 不活动上下文定时器：会话无数据传输的时长超过定时器时长后，释放会话的用户面资源。仅对5G用户生效。

## 注意事项

- 该命令执行后只对新激活用户生效。

- 该命令不适用于NB-IoT终端，因为此类终端很长时间才和网络交互一次，NB-IoT终端的空闲上下文功能参考软参BYTE801。
- SMF会话不活动定时器时长配置值需小于等于SMF会话空闲定时器时长。
- 当GUL承载级别参数指定为会话级时，对于4G用户，与GUL承载级别参数指定承载级且缺省承载和默认GBR的定时器指定使用承载定时器的效果相同。
- I-SMF/V-SMF下不存在辅锚点UPF时，锚点SMF支持空闲上下文核查，I-SMF/V-SMF只支持会话级空闲上下文核查。
- 参数DFTBEARPOLICY和DFTBRPLCYGGSN不支持枚举值USESPECIFICVAL。
- 当H-SMF空闲上下文核查级别指定为会话级时，专有QoS Flow空闲定时器时长和缺省QoS Flow空闲定时器时长均不生效；当H-SMF空闲上下文核查级别指定为QoS Flow级时，专有QoS Flow空闲定时器时长和缺省QoS Flow空闲定时器时长生效。
- 该命令不适用于2B2C漫游双DNN特性的专用DNN会话，专用DNN会话请使用SET MULTIDNNCTRL: MULDNNIDLETIMER。
- 当SET RDSAUTHRSPATTR的参数SESSIDLETIMESW设置值是ENABLE时，AAA下发的最大会话在线时长和空闲上下文时长比本端配置（APNIDLETIME或DFTIDLETIME）的优先级高。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| SCTXCHKSW | PCTXCHKSW | GCTXCHKSW | HCTXCHKSW | HCTXINACHKSW | ICTXCHKSW | ICTXINACHKSW | GULTIMERLEVEL | DFTBEARPOLICY | BEARERTIMER | SESSIONTIMER | SMFSESIDLETIMER | SMFSESINATIMER | IDLEUPDATEMSG | HSMFTIMERLEVEL | DEDQFIDLETIMER | DFTQFIDLETIMER | DFTBRPLCYGGSN | PROS8CTXCHKSW | PROXYSMFCHKSW |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ENABLE | ENABLE | ENABLE | ENABLE | ENABLE | ENABLE | ENABLE | SESSION | ONEDAY | 1440 | 1440 | 1440 | 40 | DISABLE | SESSION | 1440 | 1440 | ONEDAY | ENABLE | ENABLE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SCTXCHKSW | SGW-C空闲上下文核查开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SGW-C空闲上下文的使能状态。<br>数据来源：本端规划<br>取值范围：<br>- “DISABLE（去使能）”：去使能<br>- “ENABLE（使能）”：使能<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST DFTIDLETIME查询当前参数配置值。<br>配置原则：<br>如果开关由去使能修改为使能，则对新创建的上下文进行检查。 |
| PCTXCHKSW | PGW-C和SGW-C/PGW-C网元的上下文核查开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定PGW-C或者SGW-C/PGW-C合一部署时空闲上下文的使能状态。<br>数据来源：本端规划<br>取值范围：<br>- “DISABLE（去使能）”：去使能<br>- “ENABLE（使能）”：使能<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST DFTIDLETIME查询当前参数配置值。<br>配置原则：<br>如果开关由去使能修改为使能，则对新创建的上下文进行检查。 |
| GCTXCHKSW | GGSN空闲上下文核查开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定GGSN空闲上下文的使能状态。<br>数据来源：本端规划<br>取值范围：<br>- “DISABLE（去使能）”：去使能<br>- “ENABLE（使能）”：使能<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST DFTIDLETIME查询当前参数配置值。<br>配置原则：<br>如果开关由去使能修改为使能，则对新创建的上下文进行检查。 |
| HCTXCHKSW | H-SMF空闲上下文核查开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定H-SMF空闲上下文的使能状态。<br>数据来源：本端规划<br>取值范围：<br>- “DISABLE（去使能）”：去使能<br>- “ENABLE（使能）”：使能<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST DFTIDLETIME查询当前参数配置值。<br>配置原则：<br>如果开关由去使能修改为使能，则对新创建的上下文进行检查。 |
| HCTXINACHKSW | H-SMF不活动上下文核查开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定H-SMF不活动上下文的使能状态。<br>数据来源：本端规划<br>取值范围：<br>- “ENABLE（使能）”：使能<br>- “DISABLE（去使能）”：去使能<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST DFTIDLETIME查询当前参数配置值。<br>配置原则：<br>如果开关由去使能修改为使能，则对新创建的上下文进行检查。 |
| ICTXCHKSW | I-SMF/V-SMF空闲上下文核查开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定I-SMF/V-SMF空闲上下文的使能状态。<br>数据来源：本端规划<br>取值范围：<br>- “DISABLE（去使能）”：去使能<br>- “ENABLE（使能）”：使能<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST DFTIDLETIME查询当前参数配置值。<br>配置原则：<br>如果开关由去使能修改为使能，则对新创建的上下文进行检查。 |
| ICTXINACHKSW | I-SMF/V-SMF不活动上下文核查开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定I-SMF/V-SMF不活动上下文的使能状态。<br>数据来源：本端规划<br>取值范围：<br>- “ENABLE（使能）”：使能<br>- “DISABLE（去使能）”：去使能<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST DFTIDLETIME查询当前参数配置值。<br>配置原则：<br>如果开关由去使能修改为使能，则对新创建的上下文进行检查。 |
| GULTIMERLEVEL | GUL承载级别参数 | 可选必选说明：可选参数<br>参数含义：该参数用于指定定时器级别，仅对2G、3G、4G用户生效。<br>数据来源：本端规划<br>取值范围：<br>- “SESSION（会话级）”：会话级<br>- “BEARER（承载级）”：承载级<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST DFTIDLETIME查询当前参数配置值。<br>配置原则：<br>当GUL承载级别参数指定为会话级时，参数会话定时器时长生效。对2G、3G用户，当GUL承载级别参数指定为承载级时，参数GGSN一次激活上下文定时器和参数承载定时器时长生效；当GUL承载级别参数指定为会话级时，与GUL承载级别参数指定承载级且GGSN一次激活上下文定时器指定使用承载定时器的效果相同。对于4G用户，当GUL承载级别参数指定为承载级时，参数缺省承载和默认GBR的定时器、参数承载定时器时长生效；当GUL承载级别参数指定为会话级时，与GUL承载级别参数指定承载级且缺省承载和默认GBR的定时器指定使用承载定时器的效果相同。 |
| DFTBEARPOLICY | 缺省承载和默认GBR的定时器 | 可选必选说明：可选参数<br>参数含义：该参数用于指定缺省承载和默认GBR的空闲上下文定时器时长，仅对4G用户生效。<br>数据来源：本端规划<br>取值范围：<br>- “ONEDAY（一天）”：一天<br>- “OFF（关闭）”：关闭<br>- “USEBEARERTIMER（使用承载定时器）”：使用承载定时器<br>- “USESPECIFICVAL（使用指定值）”：使用指定值<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST DFTIDLETIME查询当前参数配置值。<br>配置原则：<br>如果修改该参数，仅对新激活的用户生效。当缺省承载和默认GBR的定时器参数配置为使用承载定时器时，取值为参数承载定时器时长的配置值。 |
| BEARERTIMER | 承载定时器时长(min) | 可选必选说明：可选参数<br>参数含义：该参数用于指定承载级空闲定时器时长，仅对2G、3G、4G用户生效。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是5~12000，单位是分钟。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST DFTIDLETIME查询当前参数配置值。<br>配置原则：<br>与GUL承载级别参数相关联，当GUL承载级别参数设置为承载级时该参数生效。如果修改该参数，对新激活的用户生效。对2G、3G用户，GGSN一次激活上下文定时器取值不为使用承载定时器时，承载定时器时长用于指定二次上下文的空闲上下文定时器时长。对于4G用户，缺省承载和默认GBR的定时器取值不为使用承载定时器时，承载定时器时长用于指定专载的空闲上下文定时器时长。 |
| SESSIONTIMER | 会话定时器时长(min) | 可选必选说明：可选参数<br>参数含义：该参数用于指定会话级空闲定时器时长，仅对2G、3G、4G用户生效。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是5~12000，单位是分钟。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST DFTIDLETIME查询当前参数配置值。<br>配置原则：<br>与GUL承载级别参数相关联，当GUL承载级别参数设置为会话级时该参数生效。如果修改该参数，对新激活的用户生效。 |
| SMFSESIDLETIMER | SMF会话空闲定时器时长(min) | 可选必选说明：可选参数<br>参数含义：该参数用于指定SMF的PDU会话的空闲定时器时长，仅对5G用户生效。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是5~12000，单位是分钟。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST DFTIDLETIME查询当前参数配置值。<br>配置原则：<br>如果修改该参数，仅对新激活的用户生效。 |
| SMFSESINATIMER | SMF会话不活动定时器时长(min) | 可选必选说明：可选参数<br>参数含义：该参数用于指定SMF的PDU会话的不活动定时器时长，仅对5G用户生效。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是5~12000，单位是分钟。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST DFTIDLETIME查询当前参数配置值。<br>配置原则：<br>如果修改该参数，仅对新激活的用户生效。 |
| IDLEUPDATEMSG | 空闲超时发送更新消息 | 可选必选说明：可选参数<br>参数含义：该参数用于指定当用户持续没有流量的时长超过配置时长后是否发送更新消息，仅对2G、3G、4G用户生效。<br>数据来源：本端规划<br>取值范围：<br>- “DISABLE（去使能）”：去使能<br>- “ENABLE（使能）”：使能<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST DFTIDLETIME查询当前参数配置值。<br>配置原则：<br>如果修改该参数，仅对新激活的用户生效。 |
| HSMFTIMERLEVEL | H-SMF空闲上下文核查级别 | 可选必选说明：可选参数<br>参数含义：该参数用于指定H-SMF空闲上下文核查级别，仅对5G用户生效。<br>数据来源：本端规划<br>取值范围：<br>- SESSION（会话级）<br>- QOSFLOW（QoS Flow级）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST DFTIDLETIME查询当前参数配置值。<br>配置原则：<br>如果修改该参数，仅对新激活的用户生效。当H-SMF空闲上下文核查级别指定为会话级时，SMF会话空闲定时器时长生效，专有QoS Flow空闲定时器时长和缺省QoS Flow空闲定时器时长均不生效；当H-SMF空闲上下文核查级别指定为QoS Flow级时，SMF会话空闲定时器时长不生效，专有QoS Flow空闲定时器时长和缺省QoS Flow空闲定时器时长生效。 |
| DEDQFIDLETIMER | 专有QoS Flow空闲定时器时长(min) | 可选必选说明：该参数在"HSMFTIMERLEVEL"配置为"QOSFLOW"时为条件可选参数。<br>参数含义：该参数用于指定SMF的专有QoS Flow空闲定时器时长，仅对5G用户生效。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是5~12000。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST DFTIDLETIME查询当前参数配置值。<br>配置原则：<br>如果修改该参数，仅对新激活的用户生效。 |
| DFTQFIDLETIMER | 缺省QoS Flow空闲定时器时长(min) | 可选必选说明：该参数在"HSMFTIMERLEVEL"配置为"QOSFLOW"时为条件可选参数。<br>参数含义：该参数用于指示SMF的缺省QoS Flow空闲定时器时长，仅对5G用户生效。当该参数设置为0时，表示不开启缺省QoS Flow空闲上下文核查。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0，5~12000。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST DFTIDLETIME查询当前参数配置值。<br>配置原则：<br>如果修改该参数，仅对新激活的用户生效。 |
| DFTBRPLCYGGSN | GGSN一次激活上下文定时器 | 可选必选说明：可选参数<br>参数含义：该参数用于指定GGSN一次激活上下文空闲定时器时长。<br>数据来源：本端规划<br>取值范围：<br>- “ONEDAY（一天）”：一天<br>- “OFF（关闭）”：关闭<br>- “USEBEARERTIMER（使用承载定时器）”：使用承载定时器<br>- “USESPECIFICVAL（使用指定值）”：使用指定值<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST DFTIDLETIME查询当前参数配置值。<br>配置原则：<br>当GGSN一次激活上下文定时器参数配置为使用承载定时器时，取值为参数承载定时器时长的配置值。 |
| PROS8CTXCHKSW | Proxy-SMF S8空闲上下文核查开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定Proxy-SMF S8空闲上下文的使能状态。<br>数据来源：本端规划<br>取值范围：<br>- “DISABLE（去使能）”：去使能<br>- “ENABLE（使能）”：使能<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST DFTIDLETIME查询当前参数配置值。<br>配置原则：<br>如果开关由去使能修改为使能，则对新创建的上下文进行检查，SMF会话空闲定时器时长生效。 |
| PROXYSMFCHKSW | Proxy-SMF 空闲上下文检查开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定Proxy-SMF 空闲上下文的使能状态。<br>数据来源：本端规划<br>取值范围：如果开关由去使能修改为使能，则对新创建的上下文进行检查，SMF会话空闲定时器时长生效。<br>- “DISABLE（去使能）”：去使能<br>- “ENABLE（使能）”：使能<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST DFTIDLETIME查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [默认空闲上下文定时器配置（DFTIDLETIME）](configobject/UNC/20.15.2/DFTIDLETIME.md)

## 使用实例

假设开启SGW、PGW和SGW/PGW合一部署网元的空闲上下文核查开关，并将缺省承载和默认GBR的定时器设置为1440时，使用如下命令：

```
SET DFTIDLETIME: SCTXCHKSW=ENABLE, PCTXCHKSW=ENABLE, DFTBEARPOLICY=ONEDAY, BEARERTIMER=1440;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置默认空闲上下文定时器配置（SET-DFTIDLETIME）_09654414.md`
