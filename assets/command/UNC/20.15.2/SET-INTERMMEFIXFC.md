---
id: UNC@20.15.2@MMLCommand@SET INTERMMEFIXFC
type: MMLCommand
name: SET INTERMMEFIXFC（设置Inter-MME接入固定速率流控功能相关参数）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: INTERMMEFIXFC
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
max_records: 1
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 操作维护
- 设备管理
- 流控管理
- 业务流控管理
- Inter-MME接入流控管理
status: active
---

# SET INTERMMEFIXFC（设置Inter-MME接入固定速率流控功能相关参数）

## 功能

**适用网元：MME**

该命令设置Inter-MME接入固定速率流控功能的相关参数。

MME组Pool时，如果某个MME故障，则故障MME上的用户会接入到Pool内正常的MME上，可能造成对正常MME、S6a接口、HSS的冲击，导致相关网元过载。为了防止这类MME间的新接入用户影响在网用户的正常业务，控制非本MME用户的接入消息允许处理速率。这些消息包括：Attach Request消息、Service Request消息。

## 注意事项

- 该命令执行后立即生效。

- 此命令的最大记录数为1。
- 流控阈值设置过低可能会导致流程失败，建议单SGP进程阈值(或整系统平均到单SGP进程的阈值)不低于30个/秒，设置过高可能导致系统不能对消息进行合理流控。
- SET INTERMMEFC和SET INTERMMEFIXFC不建议同时开启，同时开启时SET INTERMMEFIXFC优先级高于SET INTERMMEFC。

## 权限

manage-ug;system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FCTYPE | 流控粒度 | 可选必选说明：可选参数<br>参数含义：该参数用于设置Inter-MME流程流控粒度。<br>数据来源：全网规划<br>取值范围：<br>- PROCESS（单进程）：表示Inter-MME消息按照单SGP进程粒度进行流控。<br>- POD（POD）：表示Inter-MME消息按照单POD粒度进行流控。<br>系统初始设置值：PROCESS（单进程）<br>配置原则：无 |
| ATTACHFCSWITCH | Attach接入流控功能开关 | 可选必选说明：可选参数<br>参数含义：该参数用于开启或关闭Inter-MME Attach流程S1接口流控。<br>数据来源：全网规划<br>取值范围：<br>- OFF（关闭）<br>- ON（开启）<br>系统初始设置值：OFF（关闭）<br>配置原则：无 |
| ATTACHSCOPE | Attach Request流控阈值作用范围 | 可选必选说明：条件可选参数<br>参数含义：该参数用于设置Attach消息流控阈值的作用范围。<br>前提条件：该参数在“Attach接入流控功能开关”参数配置为“ON（开启）”时生效。<br>数据来源：全网规划<br>取值范围：<br>- PROCESS（单进程）：当“流控类型”为“PROCESS（单进程）”时，表示ATTACHTHD参数指定的值是单SGP进程每秒钟可以通过的消息数。当“流控类型”为“POD（POD）”时，表示ATTACHTHD参数指定的值乘以LINK-POD中SGP进程个数，作为每个LINK-POD的流控阈值。<br>- SYSTEM（整系统）：当“流控类型”为“PROCESS（单进程）”时，表示ATTACHTHD参数指定的值是整系统每秒钟可以通过的消息数。每个SGP进程独立进行流控，整系统的流控阈值除以SGP进程个数作为每个SGP进程的流控阈值。当“流控类型”为“POD（POD）”时，表示ATTACHTHD参数指定的值是整系统每秒钟可以通过的消息数。每个LINK-POD独立进行流控，整系统的流控阈值除以LINK-POD个数作为每个LINK-POD的流控阈值。<br>系统初始设置值：PROCESS（单进程）<br>配置原则：无 |
| ATTACHTHD | Attach Request速率门限(个/秒) | 可选必选说明：条件可选参数<br>参数含义：该参数用于设置Attach Request速率门限。<br>前提条件：该参数在“Attach接入流控功能开关”参数配置为“ON（开启）”时生效。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为1~3133440，单位是个每秒。<br>系统初始设置值：4080<br>配置原则：<br>- 当参数“ATTACHSCOPE”取值为“PROCESS（单进程）”时，本参数的取值范围为1-4080。<br>- 当参数“ATTACHSCOPE”取值为“SYSTEM（整系统）”时，本参数的取值范围为1-3133440。<br>说明：如果设置了<br>“Attach Request流控阈值作用范围”<br>参数， 则该参数为必选参数。<br>当参数<br>“ATTACHSCOPE”<br>取值为<br>“SYSTEM（整系统）”<br>且系统中有LINK-POD故障时，其余正常LINK-POD流控阈值不变，整系统阈值缩小。 |
| SRFCSWITCH | SR接入流控功能开关 | 可选必选说明：可选参数<br>参数含义：该参数用于开启或关闭Inter-MME Service Request流程S1接口流控。<br>数据来源：全网规划<br>取值范围：<br>- OFF（关闭）<br>- ON（开启）<br>系统初始设置值：OFF（关闭）<br>配置原则：无 |
| SRSCOPE | Service Request流控阈值作用范围 | 可选必选说明：条件可选参数<br>参数含义：该参数用于设置Service Request消息流控阈值的作用范围。<br>前提条件：该参数在“SR接入流控功能开关”参数配置为“ON（开启）”时生效。<br>数据来源：全网规划<br>取值范围：<br>- PROCESS（单进程）：当“流控类型”为“PROCESS（单进程）”时，表示SRTHD参数指定的值是单SGP进程每秒钟可以通过的消息数。当“流控类型”为“POD（POD）”时，表示REGTHD参数指定的值乘以LINK-POD中SGP进程个数，作为每个LINK-POD的流控阈值。<br>- SYSTEM（整系统）：当“流控类型”为“PROCESS（单进程）”时，表示SRTHD参数指定的值是整系统每秒钟可以通过的消息数。每个SGP进程独立进行流控，整系统的流控阈值除以SGP进程个数作为每个SGP进程的流控阈值。当“流控类型”为“POD（POD）”时，表示REGTHD参数指定的值乘以LINK-POD中SGP进程个数，数作为每个LINK-POD的流控阈值。<br>系统初始设置值：PROCESS（单进程）<br>配置原则：无 |
| SRTHD | Service Request速率门限(个/秒) | 可选必选说明：条件可选参数<br>参数含义：该参数用于设置Service Request速率门限。<br>前提条件：该参数在“SR接入流控功能开关”参数配置为“ON（开启）”时生效。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为1~3133440，单位是个每秒。<br>系统初始设置值：4080<br>配置原则：<br>- 当参数“SRSCOPE”取值为“PROCESS（单进程）”时，本参数的取值范围为1-4080。<br>- 当参数“SRSCOPE”取值为“SYSTEM（整系统）”时，本参数的取值范围为1-3133440。<br>说明：如果设置了<br>“Service Request流控阈值作用范围”<br>参数， 则该参数为必选参数。<br>当参数<br>“ATTACHSCOPE”<br>取值为<br>“SYSTEM（整系统）”<br>且系统中有LINK-POD故障时，其余正常LINK-POD流控阈值不变，整系统阈值缩小。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@INTERMMEFIXFC]] · Inter-MME接入固定速率流控功能相关参数（INTERMMEFIXFC）

## 使用实例

设置Inter-MME接入固定速率流控功能的相关参数，Attach接入流控功能开关设置为"ON（开启）"：

```
SET INTERMMEFIXFC: ATTACHFCSWITCH=ON;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-INTERMMEFIXFC.md`
