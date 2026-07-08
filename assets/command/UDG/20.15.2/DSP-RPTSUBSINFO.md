---
id: UDG@20.15.2@MMLCommand@DSP RPTSUBSINFO
type: MMLCommand
name: DSP RPTSUBSINFO（显示报表订阅信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: RPTSUBSINFO
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务报表管理
- 报表订阅管理
- 报表业务订阅信息
status: active
---

# DSP RPTSUBSINFO（显示报表订阅信息）

## 功能

**适用NF：PGW-U、UPF**

该命令用于显示报表订阅信息。

## 注意事项

- 该命令执行后立即生效。
- 该命令每次查询结果可能显示不全，多次查询显示结果从上一次查询到的最后一条记录的下一条记录开始。查询不同类型、或者5分钟不执行该命令，再次查询从第一条记录开始。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TYPE | 类型 | 可选必选说明：必选参数<br>参数含义：查询类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- SUBS_POLICY：查询规则类型的订阅信息。<br>- SUBS_CONFIG：查询配置类型的订阅信息。<br>- LOCAL_RPT_EVT：查询本地可以支持订阅的RPT event信息。<br>- LOCAL_FLT_EVT：查询本地可以支持订阅的过滤Event信息。<br>- LOCAL_AGGR_EVT：查询本地可以支持订阅的汇聚Event信息。<br>- LOCAL_TOPN_EVT：查询本地可以支持订阅的Topn Event信息。<br>默认值：无<br>配置原则：无 |
| SUBSPOLICYID | 订阅规则ID | 可选必选说明：条件可选参数<br>前提条件：该参数在“TYPE”配置为“SUBS_POLICY”时为可选参数。<br>参数含义：条件可选，type参数是SubsPolicy时可选，用于输入要查询的订阅规则ID，如果没有输入，会显示所有Policy类型的订阅规则信息。<br>数据来源：本端规划<br>取值范围：{{0~4294967295}}。<br>默认值：无<br>配置原则：无 |
| SUBSCONFIGTYPE | 配置信息类型 | 可选必选说明：条件必选参数<br>前提条件：该参数在“TYPE”配置为“SUBS_CONFIG”时为必选参数。<br>参数含义：条件可选，type参数是SubsConfig时可选，用于输入要查询的配置信息类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- CONFIG_TYPE_REALRPT：实时报表。<br>- CONFIG_TYPE_FILTERGROUP：配置过滤器组。<br>- CONFIG_TYPE_QOSMONITOR：Qos Monitor规则。<br>- CONFIG_TYPE_HIGHBAND：高带宽用户规则。<br>- CONFIG_TYPE_VVIP：VVIP用户GRB保障策略。<br>- CONFIG_TYPE_USRTATS：直播业务的用户统计信息。<br>- CONFIG_TYPE_CCO_CELLSPEC：CCO小区及web应用规则。<br>- CONFIG_TYPE_CCO_ABRVIDEO：CCO视频应用规则。<br>- CONFIG_TYPE_CCO_CELLLEVEL：CCO小区分级规则。<br>- CONFIG_TYPE_CCO_CTRL：CCO控制规则。<br>- CONFIG_TYPE_QOE：客户感知体验。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/RPTSUBSINFO]] · 报表订阅信息（RPTSUBSINFO）

## 使用实例

显示运营商查阅报表订阅信息：

```
DSP RPTSUBSINFO: TYPE=LOCAL_FLT_EVT;
```

```

RETCODE = 0  操作成功

Display Report Subscribe Information
------------------------------------
显示结果  =  
Supported Aggregate Event:

Rat : 201
Sever IP type : 202
Cell ID : 203
L34 Protocol : 204
L7 Protocol : 205
L7 Sub Protocol : 206
L7 Protocol Category : 207
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-RPTSUBSINFO.md`
