---
id: UNC@20.15.2@MMLCommand@MOD E2ETRCTSK
type: MMLCommand
name: MOD E2ETRCTSK（修改端到端跟踪任务）
nf: UNC
version: 20.15.2
verb: MOD
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

# MOD E2ETRCTSK（修改端到端跟踪任务）

## 功能

**适用NF：AMF、MME**

该命令用于修改跟踪任务信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IMSI | IMSI | 可选必选说明：必选参数<br>参数含义：该参数用于指定用户的IMSI。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是5~15。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |
| NGRAN | NGRAN | 可选必选说明：可选参数<br>参数含义：该参数用于指定NGRAN是否上报跟踪消息。<br>数据来源：全网规划<br>取值范围：<br>- “NORPT（不上报）”：不上报<br>- “RPT（上报）”：上报<br>默认值：无<br>配置原则：无 |
| TRCINTERFACE | NGRAN接口 | 可选必选说明：可选参数<br>参数含义：该参数用于指定NGRAN上报跟踪消息的接口列表。<br>数据来源：全网规划<br>取值范围：<br>- “NGC（NGC）”：NGC<br>- “XNC（XN-C）”：XN-C<br>- “UU（Uu）”：Uu<br>- “F1C（F1-C）”：F1-C<br>- “E1（E1）”：E1<br>默认值：无<br>配置原则：无 |
| TRCDPTH | 跟踪深度 | 可选必选说明：可选参数<br>参数含义：该参数用于指定网元上报跟踪消息的级别，值越大，级别越高。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~5。<br>默认值：无<br>配置原则：无 |
| ENB | ENODEB | 可选必选说明：可选参数<br>参数含义：该参数用于指定eNodeB是否上报跟踪消息。<br>数据来源：全网规划<br>取值范围：<br>- “NORPT（不上报）”：不上报<br>- “RPT（上报）”：上报<br>默认值：无<br>配置原则：无 |
| ENBINTERFACE | eNodeB接口 | 可选必选说明：可选参数<br>参数含义：该参数用于指定eNodeB上报跟踪消息的接口列表。<br>数据来源：全网规划<br>取值范围：<br>- “S1MME（S1-MME）”：S1-MME<br>- “X2（X2）”：X2<br>- “UU（Uu）”：Uu<br>默认值：无<br>配置原则：无 |
| ENBTRCDPTH | eNodeB跟踪深度 | 可选必选说明：可选参数<br>参数含义：该参数用于指定网元上报跟踪消息的级别，值越大，级别越高。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~5。<br>默认值：无<br>配置原则：无 |
| TRCVALIDTM | 跟踪任务有效时长(天) | 可选必选说明：可选参数<br>参数含义：该参数用于指定跟踪任务的有效时长。跟踪任务累计生效天数大于此参数设置的值时则跟踪任务失效。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~30，单位是天。<br>默认值：无<br>配置原则：<br>参数取值为0，表示跟踪任务永不失效。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/E2ETRCTSK]] · 端到端跟踪任务（E2ETRCTSK）

## 使用实例

修改SUPI为123030912121001的跟踪任务的NGRAN参数为不上报，执行如下命令：

```
MOD E2ETRCTSK: IMSI="123030912121001", NGRAN=NORPT;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-E2ETRCTSK.md`
