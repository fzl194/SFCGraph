---
id: UNC@20.15.2@MMLCommand@SET ONLZEROUSGRPTSW
type: MMLCommand
name: SET ONLZEROUSGRPTSW（设置在线业务零用量容器上报方式）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: ONLZEROUSGRPTSW
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
- 全局配置
status: active
---

# SET ONLZEROUSGRPTSW（设置在线业务零用量容器上报方式）

## 功能

**适用NF：PGW-C、SMF**

该命令用于设置在线业务零用量容器上报方式。

## 注意事项

- 该命令执行后立即生效。

- 如果上报CHF的请求消息中，没有PDU级Trigger，且各业务用量容器均不允许上报，则该消息不上报CHF。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| RPTMODE | RPTSRVTERM | RPTTARIFF | RPTQHT |
| --- | --- | --- | --- |
| REPORT | ENABLE | ENABLE | ENABLE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RPTMODE | 上报方式 | 可选必选说明：可选参数<br>参数含义：该参数用来控制SMF生成的在线业务零用量容器是否向CHF上报。<br>数据来源：本端规划<br>取值范围：<br>- “REPORT（上报）”：容器为零用量时，正常上报CHF。<br>- “ZEROUSAGENORPT（零用量不上报）”：容器为零流量且零时长时，不上报CHF。<br>- “ZEROVOLUMENORPT（零流量不上报）”：容器为零流量时（时长不做检查），不上报CHF。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST ONLZEROUSGRPTSW查询当前参数配置值。<br>配置原则：<br>本参数配置为零用量不上报或零流量不上报时，可能导致丢计费事件，在线业务会丢失部分时长用量；本参数配置为上报时，其余参数配置不生效。包含以下Trigger的容器不受本参数控制：START_OF_SERVICE_DATA_FLOW，FORCED_REAUTHORISATION，VALIDITY_TIME，QUOTA_EXHAUSTED，QUOTATHRESHOLD，REMOVAL_OF_UPF。 |
| RPTSRVTERM | 上报业务终结 | 可选必选说明：可选参数<br>参数含义：该参数用于配置包含FINAL、ABNORMAL_RELEASE Trigger的在线业务零用量容器是否上报。<br>数据来源：本端规划<br>取值范围：<br>- “ENABLE（使能）”：包含该Trigger的零用量容器允许上报。<br>- “DISABLE（不使能）”：包含该Trigger的零用量容器上报方式受RPTMODE参数控制。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST ONLZEROUSGRPTSW查询当前参数配置值。<br>配置原则：无 |
| RPTTARIFF | 上报费率切换 | 可选必选说明：可选参数<br>参数含义：该参数用于配置包含TARIFF_TIME_CHANGE Trigger的在线业务零用量容器是否上报。<br>数据来源：本端规划<br>取值范围：<br>- “ENABLE（使能）”：包含该Trigger的零用量容器允许上报。<br>- “DISABLE（不使能）”：包含该Trigger的零用量容器上报方式受RPTMODE参数控制。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST ONLZEROUSGRPTSW查询当前参数配置值。<br>配置原则：无 |
| RPTQHT | 上报QHT | 可选必选说明：可选参数<br>参数含义：该参数用于配置包含QHT Trigger的在线业务零用量容器是否上报。<br>数据来源：本端规划<br>取值范围：<br>- “ENABLE（使能）”：包含该Trigger的零用量容器允许上报。<br>- “DISABLE（不使能）”：包含该Trigger的零用量容器上报方式受RPTMODE参数控制。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST ONLZEROUSGRPTSW查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [在线业务零用量容器上报方式（ONLZEROUSGRPTSW）](configobject/UNC/20.15.2/ONLZEROUSGRPTSW.md)

## 使用实例

设置在线业务零用量容器上报方式为零流量不上报：

```
SET ONLZEROUSGRPTSW: RPTMODE=ZEROVOLUMENORPT;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置在线业务零用量容器上报方式（SET-ONLZEROUSGRPTSW）_43466960.md`
