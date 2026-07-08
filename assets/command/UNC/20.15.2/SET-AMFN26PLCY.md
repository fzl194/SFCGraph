---
id: UNC@20.15.2@MMLCommand@SET AMFN26PLCY
type: MMLCommand
name: SET AMFN26PLCY（设置AMF N26接口策略）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: AMFN26PLCY
command_category: 配置类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- GTP-C接口配置管理
- N26接口管理
- N26策略管理
status: active
---

# SET AMFN26PLCY（设置AMF N26接口策略）

## 功能

**适用NF：AMF**

该命令用于设置AMF的N26接口部署策略相关参数。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| N26ITFMODE | INTRAIWK | INTRAHOQRYMODE |
| --- | --- | --- |
| SEPARATE | NO | DNS_QUERY |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| N26ITFMODE | AMF N26接口部署方式 | 可选必选说明：可选参数<br>参数含义：该参数用于指示AMF的N26接口部署方式。<br>数据来源：全网规划<br>取值范围：<br>- “SEPARATE（N26接口独立部署）”：AMF的N26接口和MME的S10接口使用不同的IP地址。<br>- “COMBINE（N26接口融合部署）”：AMF的N26接口和MME的S10支持使用同一IP地址。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST AMFN26PLCY查询当前参数配置值。<br>配置原则：无 |
| INTRAIWK | 是否支持UAM内部互操作 | 可选必选说明：该参数在"N26ITFMODE"配置为"SEPARATE"时为条件可选参数。<br>参数含义：该参数用于指示AMF N26接口部署方式为独立部署时，UAM内部的4/5G互操作场景是否直接在UAM内部处理，不再对外发送GTPC消息。<br>数据来源：全网规划<br>取值范围：<br>- “YES（是）”：是<br>- “NO（否）”：否<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST AMFN26PLCY查询当前参数配置值。<br>配置原则：无 |
| INTRAHOQRYMODE | UAM内切换识别模式 | 可选必选说明：可选参数<br>参数含义：该参数用于控制UAM识别4/5G切换流程是否为UAM内部切换流程时的识别模式。<br>数据来源：全网规划<br>取值范围：<br>- “DNS_QUERY（通过DNS查询结果识别）”：查询DNS，如果查询结果包含本网元IP地址，则为UAM内部切换流程。<br>- “PAGTBL_QUERY（通过查询寻呼表识别）”：优先通过查询目标ID在寻呼表中是否存在，如果存在则识别为UAM内部切换流程。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST AMFN26PLCY查询当前参数配置值。<br>配置原则：<br>本参数在如下两种场景下生效：1、“N26ITFMODE”配置为“COMBINE”时；2、“N26ITFMODE”配置为“SEPARATE”时，并且“INTRAIWK”配置为“YES”。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/AMFN26PLCY]] · AMF N26接口策略（AMFN26PLCY）

## 使用实例

设置AMF N26接口为融合部署模式，UAM内部4/5G互操作不使用内部交互方式，UAM识别45G切换流程通过DNS查询结果识别，执行如下命令：

```
SET AMFN26PLCY:N26ITFMODE=SEPARATE,INTRAIWK=NO,INTRAHOQRYMODE=DNS_QUERY;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置AMF-N26接口策略（SET-AMFN26PLCY）_62817114.md`
