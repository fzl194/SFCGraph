---
id: UNC@20.15.2@MMLCommand@SET LOGIFDSCP
type: MMLCommand
name: SET LOGIFDSCP（设置逻辑接口DSCP值）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: LOGIFDSCP
command_category: 配置类
applicable_nf:
- SGW-C
- PGW-C
- AMF
- SMF
- NRF
- NSSF
- SMSF
- NCG
effect_mode: 立即生效
is_dangerous: false
max_records: 23
category_path:
- 业务服务管理
- QOS管理
- 逻辑接口DSCP管理
status: active
---

# SET LOGIFDSCP（设置逻辑接口DSCP值）

## 功能

**适用NF：SGW-C、PGW-C、AMF、SMF、NRF、NSSF、SMSF、NCG**

该命令用于设置信令报文的DSCP值。在IP承载网络中，通常使用DSCP标记来进行业务优先级的区分和QoS保证。为区分不同信令在IP承载网络中不同的转发优先级，UNC支持设置具体信令流报文的DSCP值，使不同的信令按照DSCP值进行优先级转发。

有关DSCP的内容请参见RFC2474。DSCP总共分成了4类：Class Selector(CS)、Expedited Forwarding(EF)、Assured Forwarding(AF)和Best Effort(BE)。CS（类选择器）的DSCP值后三位为0，EF（加速转发）的DSCP值为101110(46)，AF（确保转发）的DSCP值最后一位为0，BE（默认）的DSCP值为000000(0)。

## 注意事项

- 该命令执行后立即生效。

- 该命令最大记录数为23。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

> **说明**
> 此处仅展示前20条初始记录值，您可以通过相关查询命令查看全部记录值。

| NFTYPE | AMFIFTYPE | SMFCGWIFTYPE | NRFIFTYPE | SMSFIFTYPE | NSSFIFTYPE | GIMSGTYPE | NCGIFTYPE | DSCPVALUE |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| AMF | DEFAULT | NULL | NULL | NULL | NULL | NULL | NULL | 46 |
| AMF | N26 | NULL | NULL | NULL | NULL | NULL | NULL | 46 |
| AMF | Namf | NULL | NULL | NULL | NULL | NULL | NULL | 46 |
| AMF | N2 | NULL | NULL | NULL | NULL | NULL | NULL | 46 |
| SMF | NULL | DEFAULT | NULL | NULL | NULL | NULL | NULL | 46 |
| SMF | NULL | N4 | NULL | NULL | NULL | NULL | NULL | 46 |
| SMF | NULL | Nsmf | NULL | NULL | NULL | NULL | NULL | 46 |
| SMF | NULL | Gi | NULL | NULL | NULL | DEFAULT | NULL | 46 |
| SMF | NULL | Gi | NULL | NULL | NULL | RADIUS | NULL | 46 |
| SMF | NULL | Gx | NULL | NULL | NULL | NULL | NULL | 46 |
| SMF | NULL | Gy | NULL | NULL | NULL | NULL | NULL | 46 |
| SMF | NULL | Ga | NULL | NULL | NULL | NULL | NULL | 46 |
| SMF | NULL | GTPCIF | NULL | NULL | NULL | NULL | NULL | 46 |
| NSSF | NULL | NULL | NULL | NULL | DEFAULT | NULL | NULL | 46 |
| NSSF | NULL | NULL | NULL | NULL | Nnssf | NULL | NULL | 46 |
| SMSF | NULL | NULL | NULL | DEFAULT | NULL | NULL | NULL | 46 |
| SMSF | NULL | NULL | NULL | Nsmsf | NULL | NULL | NULL | 46 |
| NCG | NULL | NULL | NULL | NULL | NULL | NULL | DEFAULT | 46 |
| NCG | NULL | NULL | NULL | NULL | NULL | NULL | Nchf | 46 |
| NRF | NULL | NULL | DEFAULT | NULL | NULL | NULL | NULL | 46 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFTYPE | NF类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定逻辑接口DSCP的NF类型。<br>数据来源：本端规划<br>取值范围：<br>- “AMF（AMF）”：AMF<br>- “SMF（SMF/PGW-C/SGW-C/GGSN-C）”：融合2345G功能，包含SMF/PGW-C/SGW-C/GGSN-C独立或融合的NF形态<br>- “NRF（NRF）”：NRF<br>- “NSSF（NSSF）”：NSSF<br>- “SMSF（SMSF）”：SMSF<br>- “NCG（NCG）”：NCG<br>默认值：无。<br>配置原则：<br>UNC产品包含多个NF，如AMF、SMF、NRF、NCG、NSSF、SMSF，这些NF中有些可以融合部署，也可以独立部署，有些必须独立部署，该配置中对部署不敏感。即只需要按NF类型配置，如果需要指定AMF的逻辑接口DSCP，则该参数需要选择为AMF。 |
| AMFIFTYPE | AMF接口类型 | 可选必选说明：该参数在"NFTYPE"配置为"AMF"时为条件必选参数。<br>参数含义：该参数用于指定AMF的接口类型。逻辑接口DSCP按逻辑接口进行配置，指定AMF的接口类型即为给指定接口配置DSCP值。<br>数据来源：本端规划<br>取值范围：<br>- “DEFAULT（未指定接口）”：未指定接口<br>- “N26（N26）”：N26<br>- “Namf（Namf）”：AMF的服务化接口，包括N8/N11/N12/N15/N22等<br>- “N2（N2）”：N2<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST LOGIFDSCP查询当前参数配置值。<br>配置原则：<br>如果接口类型选择为DEFAULT，即未指定的接口的DSCP值按该默认接口的DSCP值生效。如果指定了具体接口类型，则按指定的接口类型的DSCP值生效。 |
| SMFCGWIFTYPE | SMF接口类型 | 可选必选说明：该参数在"NFTYPE"配置为"SMF"时为条件必选参数。<br>参数含义：该参数用于指定SMF的接口类型。逻辑接口DSCP按逻辑接口进行配置，指定SMF的接口类型即为给指定接口配置DSCP值。<br>数据来源：本端规划<br>取值范围：<br>- “DEFAULT（未指定接口）”：未指定接口<br>- “N4（N4）”：N4<br>- “Nsmf（Nsmf）”：SMF的服务化接口，包括N11/N16a/N10/N7/N40等<br>- “Gi（Gi）”：Gi<br>- “Gx（Gx）”：Gx<br>- “Gy（Gy）”：Gy<br>- “Ga（Ga）”：Ga<br>- “GTPCIF（GTPC协议接口）”：GTPC协议接口包括Gn/Gp/S2b/S4/S11/S5/S8接口<br>- “S6b（S6b）”：S6b<br>- “DHCP（DHCP）”：DHCP<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST LOGIFDSCP查询当前参数配置值。<br>配置原则：<br>如果接口类型选择为DEFAULT，即未指定的接口的DSCP值按该默认接口的DSCP值生效。如果指定了具体接口类型，则按指定的接口类型的DSCP值生效。 |
| NRFIFTYPE | NRF接口类型 | 可选必选说明：该参数在"NFTYPE"配置为"NRF"时为条件必选参数。<br>参数含义：该参数用于指定NRF的逻辑接口类型。当前NRF仅支持服务化接口一种逻辑接口。<br>数据来源：本端规划<br>取值范围：<br>- “DEFAULT（未指定接口）”：未指定接口<br>- “Nnrf（Nnrf）”：NRF的服务化接口<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST LOGIFDSCP查询当前参数配置值。<br>配置原则：<br>如果接口类型选择为DEFAULT，即未指定的接口的DSCP值按该默认接口的DSCP值生效。如果指定了具体接口类型，则按指定的接口类型的DSCP值生效。 |
| SMSFIFTYPE | SMSF接口类型 | 可选必选说明：该参数在"NFTYPE"配置为"SMSF"时为条件必选参数。<br>参数含义：该参数用于指定SMSF的逻辑接口类型。当前SMSF仅支持服务化接口一种逻辑接口类型。<br>数据来源：本端规划<br>取值范围：<br>- “DEFAULT（未指定接口）”：未指定接口<br>- “Nsmsf（Nsmsf）”：SMSF的服务化接口<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST LOGIFDSCP查询当前参数配置值。<br>配置原则：<br>如果接口类型选择为DEFAULT，即未指定的接口的DSCP值按该默认接口的DSCP值生效。如果指定了具体接口类型，则按指定的接口类型的DSCP值生效。 |
| NSSFIFTYPE | NSSF接口类型 | 可选必选说明：该参数在"NFTYPE"配置为"NSSF"时为条件必选参数。<br>参数含义：该参数用于指定NSSF的逻辑接口类型。当前NSSF仅支持服务化接口一种逻辑接口类型。<br>数据来源：本端规划<br>取值范围：<br>- “DEFAULT（未指定接口）”：未指定接口<br>- “Nnssf（Nnssf）”：NSSF的服务化接口<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST LOGIFDSCP查询当前参数配置值。<br>配置原则：<br>如果接口类型选择为DEFAULT，即未指定的接口的DSCP值按该默认接口的DSCP值生效。如果指定了具体接口类型，则按指定的接口类型的DSCP值生效。 |
| GIMSGTYPE | Gi接口消息类型 | 可选必选说明：该参数在"SMFCGWIFTYPE"配置为"Gi"时为条件必选参数。<br>参数含义：该参数用于指定服务化接口的消息类型。服务化接口消息包括了注册消息、服务发现消息、心跳消息和信令消息。<br>数据来源：本端规划<br>取值范围：<br>- “DEFAULT（DEFAULT）”：未指定消息类型<br>- “RADIUS（RADIUS）”：Gi接口的Radius计费和鉴权信令<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST LOGIFDSCP查询当前参数配置值。<br>配置原则：<br>该参数指定为DEFAULT时，表示Gi接口下的指定消息按设置的DSCP值生效，未指定的消息按该DEFAULT配置的DSCP值生效。 |
| NCGIFTYPE | NCG接口类型 | 可选必选说明：该参数在"NFTYPE"配置为"NCG"时为条件必选参数。<br>参数含义：该参数用于指定NCG的接口类型。当前NCG仅支持服务化接口一种逻辑接口类型。<br>数据来源：本端规划<br>取值范围：<br>- “DEFAULT（未指定接口）”：未指定接口<br>- “Nchf（Nchf）”：NCG的服务化接口<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST LOGIFDSCP查询当前参数配置值。<br>配置原则：<br>如果接口类型选择为DEFAULT，即未指定的接口的DSCP值按该默认接口的DSCP值生效。如果指定了具体接口类型，则按指定的接口类型的DSCP值生效。 |
| DSCPVALUE | DSCP值 | 可选必选说明：可选参数<br>参数含义：该参数用于指定设置的DSCP值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~63。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST LOGIFDSCP查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/LOGIFDSCP]] · 逻辑接口DSCP配置（LOGIFDSCP）

## 使用实例

若运营商想设置AMF的逻辑接口N26的DSCP值为60，则可以使用如下命令：

```
SET LOGIFDSCP: NFTYPE=AMF, AMFIFTYPE=N26, DSCPVALUE=60；
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-LOGIFDSCP.md`
