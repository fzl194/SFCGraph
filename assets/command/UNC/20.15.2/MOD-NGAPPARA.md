---
id: UNC@20.15.2@MMLCommand@MOD NGAPPARA
type: MMLCommand
name: MOD NGAPPARA（修改NGAP协议参数）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: NGAPPARA
command_category: 配置类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- N2接口管理
- NGAP协议参数管理
status: active
---

# MOD NGAPPARA（修改NGAP协议参数）

## 功能

**适用NF：AMF**

该命令用于修改NGAP的协议参数。

## 注意事项

- 该命令执行后立即生效。

- 该参数被NGAP本端实体引用以后不允许修改。
- 该命令不支持对NGAP协议参数索引为“0”的记录进行修改。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NGAPPARAIDX | NGAP协议参数索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定NGAP参数配置的索引。唯一表示一个NGAP实体的参数配置。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~31。<br>默认值：无<br>配置原则：无 |
| AMFCFGUPTTMR | AMF Configuration Update消息超时定时器(s) | 可选必选说明：可选参数<br>参数含义：该参数用于指定AMF配置变更消息的超时时长，当AMF发送AMF Configuration Request消息以后启动该定时器，等待对端NG RAN回AMF Configuration Acknowledge消息，在定时器超时时未收到该消息则认为AMF配置更新失败。AMF需要重发该消息。<br>数据来源：对端协商<br>取值范围：整数类型，取值范围是1~65534，单位是秒。<br>默认值：无<br>配置原则：无 |
| AMFCFGUPTCNT | AMF Configuration Update消息重发次数 (times) | 可选必选说明：可选参数<br>参数含义：该参数用于指定AMF配置更新消息的重发次数，当AMF发送AMF Configuration Request消息以后，等待对端NG RAN回AMF Configuration Acknowledge消息，在“AMFCFGUPTTMR”时间内未收到该消息或收到携带TimeToWait信元的AMF Configuration Update Failure消息，则AMF配置更新消息需要重发，重发的最大次数即为此参数的取值。<br>数据来源：对端协商<br>取值范围：整数类型，取值范围是1~3，单位是次。<br>默认值：无<br>配置原则：无 |
| RESETTMR | Reset超时定时器(s) | 可选必选说明：可选参数<br>参数含义：该参数用于指定Reset消息的超时时长。在AMF向NG RAN发送Reset消息以后，启动该定时器。在该定时器超时前没有收到NG-RAN回AMF Configuration Acknowledge消息，则AMF需要重新发送Reset消息。<br>数据来源：对端协商<br>取值范围：整数类型，取值范围是1~65534，单位是秒。<br>默认值：无<br>配置原则：无 |
| RESETCNT | Reset消息重发次数 (times) | 可选必选说明：可选参数<br>参数含义：该参数用于指定Reset消息的最大重发次数。当AMF向NG RAN发送Reset消息超时次数达到该配置值后将不再重发。<br>数据来源：对端协商<br>取值范围：整数类型，取值范围是1~3，单位是次。<br>默认值：无<br>配置原则：无 |
| TIMETOWAITTMR | 重发NG SETUP REQUEST时长 (s) | 可选必选说明：可选参数<br>参数含义：此参数用于设置NG Setup Failure消息中Time to Wait信元的值。该信元用于指示RAN再次发送NG Setup流程的等待时间。该参数在“等待时间指示器”参数设置为“YES(是)”时有效。<br>数据来源：全网规划<br>取值范围：<br>- “One（1）”：1<br>- “Two（2）”：2<br>- “Five（5）”：5<br>- “Ten（10）”：10<br>- “Twenty（20）”：20<br>- “Sixty（60）”：60<br>默认值：无<br>配置原则：无 |
| TIMETOWAITFLG | 等待时间指示器 | 可选必选说明：可选参数<br>参数含义：该参数用于指定是否在NGAP层的NG Setup Failure消息中携带Time to wait信元。<br>数据来源：对端协商<br>取值范围：<br>- “Yes（是）”：是<br>- “No（否）”：否<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [NGAP协议参数（NGAPPARA）](configobject/UNC/20.15.2/NGAPPARA.md)

## 使用实例

在索引为1的NGAP接口协议控制参数中，将Reset超时定时器修改为10s，执行如下命令：

```
MOD NGAPPARA: NGAPPARAIDX=1, RESETTMR=10;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改NGAP协议参数（MOD-NGAPPARA）_09654199.md`
