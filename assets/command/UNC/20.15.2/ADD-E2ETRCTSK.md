---
id: UNC@20.15.2@MMLCommand@ADD E2ETRCTSK
type: MMLCommand
name: ADD E2ETRCTSK（增加端到端跟踪任务）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: E2ETRCTSK
command_category: 配置类
applicable_nf:
- AMF
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 扩展调测
- OM调测
status: active
---

# ADD E2ETRCTSK（增加端到端跟踪任务）

## 功能

**适用NF：AMF、MME**

此命令用于增加端到端跟踪任务，用以模拟信令类端到端跟踪，AMF/MME把跟踪任务相关参数仅传递给NG-RAN/eNodeB。

端到端跟踪任务分为管理类和信令类，所谓管理类跟踪是由无线网络或者核心网的网管向网元下发的跟踪任务，网元之间不传输跟踪任务相关参数；而信令类则是由核心网网管下发给UDM/HSS，通过UDM/HSS将跟踪任务相关参数传递给AMF/MME，进而再传递给SMF、SGW、PCF、NG-RAN、eNodeB等周边网元的跟踪任务。

## 注意事项

- 该命令执行后立即生效。

- 增加端到端跟踪任务时，系统将自动删除已失效的跟踪任务。
- 如果同时存在网管向网元下发的端到端跟踪任务，该命令创建的任务不生效。
- 通过本命令同时在AMF和MME上创建跟踪任务时，AMF和MME跟踪任务的跟踪参考号都为本命令中的参数TRCID。

- 最多可输入128条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IMSI | IMSI | 可选必选说明：必选参数<br>参数含义：该参数用于指定用户的IMSI。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是5~15。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |
| TRCID | 跟踪参考号 | 可选必选说明：必选参数<br>参数含义：该参数用于全局唯一标识一个跟踪任务，由MCC、MNC和Trace ID三部分组成。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是12~13。本参数的格式是<MCC><MNC>-<Trace ID>，其中MCC是3个十进制数字，MNC是2或3个十进制数字，Trace ID则是使用字符串表示的3字节长的十六进制数。比如MCC是123，MNC是45，Trace ID是100，那么本参数表示为12345-000064。<br>默认值：无<br>配置原则：无 |
| NGRAN | NGRAN | 可选必选说明：可选参数<br>参数含义：该参数用于指定NGRAN是否上报跟踪消息。<br>数据来源：全网规划<br>取值范围：<br>- “NORPT（不上报）”：不上报<br>- “RPT（上报）”：上报<br>默认值：无<br>配置原则：无 |
| TRCINTERFACE | NGRAN接口 | 可选必选说明：可选参数<br>参数含义：该参数用于指定NGRAN上报跟踪消息的接口列表。<br>数据来源：全网规划<br>取值范围：<br>- “NGC（NGC）”：NGC<br>- “XNC（XN-C）”：XN-C<br>- “UU（Uu）”：Uu<br>- “F1C（F1-C）”：F1-C<br>- “E1（E1）”：E1<br>默认值：无<br>配置原则：无 |
| TRCDPTH | 跟踪深度 | 可选必选说明：可选参数<br>参数含义：该参数用于指定网元上报跟踪消息的级别，值越大，级别越高。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~5。<br>默认值：无<br>配置原则：无 |
| ENB | ENODEB | 可选必选说明：可选参数<br>参数含义：该参数用于指定eNodeB是否上报跟踪消息。<br>数据来源：全网规划<br>取值范围：<br>- “NORPT（不上报）”：不上报<br>- “RPT（上报）”：上报<br>默认值：无<br>配置原则：无 |
| ENBINTERFACE | eNodeB接口 | 可选必选说明：可选参数<br>参数含义：该参数用于指定eNodeB上报跟踪消息的接口列表。<br>数据来源：全网规划<br>取值范围：<br>- “S1MME（S1-MME）”：S1-MME<br>- “X2（X2）”：X2<br>- “UU（Uu）”：Uu<br>默认值：无<br>配置原则：无 |
| ENBTRCDPTH | eNodeB跟踪深度 | 可选必选说明：可选参数<br>参数含义：该参数用于指定网元上报跟踪消息的级别，值越大，级别越高。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~5。<br>默认值：无<br>配置原则：无 |
| TRCVALIDTM | 跟踪任务有效时长(天) | 可选必选说明：可选参数<br>参数含义：该参数用于指定跟踪任务的有效时长。跟踪任务累计生效天数大于此参数设置的值时则跟踪任务失效。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~30，单位是天。<br>默认值：0<br>配置原则：<br>参数取值为0，表示跟踪任务永不失效。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/E2ETRCTSK]] · 端到端跟踪任务（E2ETRCTSK）

## 使用实例

增加端到端跟踪任务，配置SUPI为123030912121001，TRCID为12345-000064，NGRAN配置为上报，接口使用NGC，跟踪深度为1，跟踪任务有效时长为1天，执行如下命令：

```
ADD E2ETRCTSK: IMSI="123030912121001", TRCID="12345-000064", NGRAN=RPT, TRCINTERFACE=NGC-1&XNC-0&UU-0&F1C-0&E1-0, TRCDPTH=1,TRCVALIDTM=1;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-E2ETRCTSK.md`
