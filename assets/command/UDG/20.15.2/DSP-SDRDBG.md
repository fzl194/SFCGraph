---
id: UDG@20.15.2@MMLCommand@DSP SDRDBG
type: MMLCommand
name: DSP SDRDBG（显示SDR调试信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: SDRDBG
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 服务通信管理
- 维测
status: active
---

# DSP SDRDBG（显示SDR调试信息）

## 功能

该命令用于显示SDR信息。

> **说明**
> - 如果调试信息发送对象下没有SDR模块，但是又查询该模块下的调试信息，则返回无数据。
> - 当前版本不支持此命令SDR Module参数的BDRA、FCA、SDRA_C取值；不支持操作类型参数的SDR策略、SDR传输速率取值。操作类型选择SDR有界邮箱计数统计时SDR Module参数必须选择SDRA。
> - 本命令只用于查询SDR丢包数量、SDR计数统计和SDR有界邮箱计数统计，若要查询SDR策略，请使用[**DSP SDRSAPPTYPE**](../策略查询/显示SDRS中的APPTYPE信息（DSP SDRSAPPTYPE）_05545720.md)、[**DSP SDRSMASTERNODE**](../策略查询/显示HAF向SDRS推送的主节点信息（DSP SDRSMASTERNODE）_05225906.md)、[**DSP SDRSROUTE**](../策略查询/显示SDRS中的APPROUTEINFO信息（DSP SDRSROUTE）_43960913.md)、[**DSP SDRSTOKEN**](../策略查询/显示SDRS中的TOKEN信息（DSP SDRSTOKEN）_45749059.md)、[**DSP SDRSVPN**](../策略查询/显示SDRS中的VPN信息（DSP SDRSVPN）_10972324.md)命令。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| OPRCOND | 调试类型 | 可选必选说明：必选参数<br>参数含义：该参数用于表示调试消息发送对象类型。<br>数据来源：本端规划<br>取值范围：<br>- “PodType（POD类型）”：POD类型<br>- “CellId（进程标识）”：进程标识<br>- “All（所有）”：所有<br>默认值：无<br>配置原则：无 |
| PODTYPE | POD类型 | 可选必选说明：该参数在"OPRCOND"配置为"PodType"时为条件必选参数。<br>参数含义：该参数用于调试信息表示发给同一类型的pod。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~127。<br>默认值：无<br>配置原则：无 |
| CELLID | 进程标识 | 可选必选说明：该参数在"OPRCOND"配置为"CellId"时为条件必选参数。<br>参数含义：该参数用于表示SDR调试消息发给某一个进程，进程标识可以通过使用命令<br>[**DSP MSPROCESS**](../../可靠性管理/微服务可靠性管理/显示微服务进程信息（DSP MSPROCESS）_09587887.md)<br>获取。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~127。<br>默认值：无<br>配置原则：无 |
| SDRMODULE | SDR Module | 可选必选说明：必选参数<br>参数含义：该参数用于标识SDR的模块信息。<br>数据来源：本端规划<br>取值范围：<br>- “SDRS（SDRS）”：SDRS<br>- “BDRS（BDRS）”：BDRS<br>- “SDRA（SDRA）”：SDRA<br>- “BDRA（BDRA）”：BDRA<br>- “FCA（FCA）”：FCA<br>- “SDRA_C（SDRA_C）”：SDRA_C<br>默认值：无<br>配置原则：<br>根据不同模块（SDRA、SDRS）查询对应模块的统计信息。 |
| OPRTYPE | 操作类型 | 可选必选说明：必选参数<br>参数含义：该参数用于表示SDR调试信息类别。<br>数据来源：本端规划<br>取值范围：<br>- “SdrDiscard（SdrDiscard）”：SDR丢包数量<br>- “SdrPolicy（SdrPolicy）”：SDR策略<br>- “SdrStat（SdrStat）”：SDR计数统计<br>- “SdrTransRate（SdrTransRate）”：SDR传输速率<br>- “SdrMailboxStat（SdrMailboxStat）”：SDR有界邮箱计数统计<br>默认值：无<br>配置原则：无 |
| OPROBJ | 操作对象 | 可选必选说明：该参数在"OPRTYPE"配置为"SdrMailboxStat"时为条件必选参数。该参数在"OPRTYPE"配置为"SdrDiscard"、"SdrStat"、"SdrTransRate"时为条件可选参数。<br>参数含义：该参数用于表示SDR调试信息统计方式。<br>数据来源：本端规划<br>取值范围：<br>- “ByTopic（按照Topic粒度）”：按照Topic粒度统计<br>- “ByInstanceId（按照实例Id粒度）”：按照实例Id粒度统计<br>- “ByTotal（按照汇总统计）”：按照汇总统计<br>- “ByChannel（按照Channel粒度统计）”：按照PAE Channel粒度统计<br>- “ByActor（按照Actor粒度）”：按照Actor粒度统计<br>- “ByTotalDetail（按照丢包原因汇总统计）”：按照丢包原因汇总统计<br>默认值：无<br>配置原则：无 |
| TOPICID | Topic ID | 可选必选说明：该参数在"OPROBJ"配置为"ByTopic"时为条件可选参数。<br>参数含义：该参数用于表示SDR调试信息统计的具体TOPIC。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~20。<br>默认值：无<br>配置原则：无 |
| INSTID | 实例ID | 可选必选说明：该参数在"OPROBJ"配置为"ByInstanceId"时为条件可选参数。<br>参数含义：该参数用于表示SDR调试信息统计的具体实例。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~63。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@SDRDBG]] · SDR调试信息（SDRDBG）

## 使用实例

DSP SDRDBG: OPRCOND=CellId, CELLID="vup-pod-010-104-1-24__103__0", SDRMODULE=SDRA, OPRTYPE=SdrDiscard, OPROBJ=ByTopic, TOPICID="208976";

```
%%DSP SDRDBG: OPRCOND=CellId, CELLID="vup-pod-010-104-1-24__103__0", SDRMODULE=SDRA, OPRTYPE=SdrDiscard, OPROBJ=ByTopic, TOPICID="208976";%%
RETCODE = 0  操作成功

结果如下
--------
        POD类型  =  vup-pod
        Cell ID  =  vup-pod-010-104-1-24__103__0
     SDR Module  =  SDRA
       操作对象  =  按照Topic粒度
     操作对象值  =  208976
       丢包原因  =  drop_no_topicInfo
         丢包数  =  53
最近30min丢包数  =  53
           说明  =  sdraCellld=vup-pod-010-30-1-35__121__0, srcCsType=2003,dstCsType=4294967295, dstInstid=0
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-SDRDBG.md`
