---
id: UNC@20.15.2@MMLCommand@SET INTERAMFFC
type: MMLCommand
name: SET INTERAMFFC（设置Inter-AMF流控参数）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: INTERAMFFC
command_category: 配置类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- 拥塞控制
- Inter-AMF流控参数
status: active
---

# SET INTERAMFFC（设置Inter-AMF流控参数）

## 功能

![](设置Inter-AMF流控参数（SET INTERAMFFC）_96243129.assets/notice_3.0-zh-cn_2.png)

存在较大操作风险，执行不当会导致业务受损或中断。

**适用NF：AMF**

设置Inter-AMF接入流控功能的相关参数。

AMF组Pool时，如果某个AMF故障，则故障AMF上的用户会接入到Pool内正常的AMF上，可能对正常AMF造成较大冲击，导致其过载。为了防止这类AMF间的新接入用户影响在网用户的正常业务，控制非本AMF用户的接入消息允许处理速率。这些消息包括：Registration Request(Initial类型携带5G-GUTI)、Service Request消息。

## 注意事项

- 该命令执行后立即生效。

- 流控阈值设置过低可能会导致流程失败，设置过高可能导致系统不能对消息进行合理流控，建议保持初始值。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| FCSWITCH | REGSCOPE | REGTHD | SRSCOPE | SRTHD | STARTALMTIMES |
| --- | --- | --- | --- | --- | --- |
| ON | POD | 300 | POD | 300 | 3 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FCSWITCH | Inter-AMF接入流控功能开关 | 可选必选说明：可选参数<br>参数含义：用于开启或关闭Inter-AMF接入流控功能。<br>数据来源：全网规划<br>取值范围：<br>- ON（开启）<br>- OFF（关闭）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST INTERAMFFC查询当前参数配置值。<br>配置原则：无 |
| REGSCOPE | Registration Request流控阈值作用范围 | 可选必选说明：可选参数<br>参数含义：该参数用于设置Registration Request消息流控阈值的作用范围。<br>数据来源：全网规划<br>取值范围：<br>- “POD（单POD）”：表示REGTHD参数指定的值是单POD每秒钟可以通过的消息数。<br>- “SYSTEM（整系统）”：表示REGTHD参数指定的值是整系统每秒钟可以通过的消息数。每个POD独立进行流控，整系统的流控阈值除以POD个数作为每个POD的流控阈值。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST INTERAMFFC查询当前参数配置值。<br>配置原则：<br>建议配置为“SYSTEM（整系统）”，AMF扩缩容场景下可以保持整系统对后端的流控能力保持不变。 |
| REGTHD | Registration Request速率门限(个/秒) | 可选必选说明：可选参数<br>参数含义：用于设置Registration Request速率门限。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~640000，单位是个每秒。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST INTERAMFFC查询当前参数配置值。<br>配置原则：<br>当参数“REGSCOPE”取值为“POD（单POD）”时，本参数的取值范围为0-10000。<br>当参数“REGSCOPE”取值为“SYSTEM（整系统）”时，本参数的取值范围为0-640000。 |
| SRSCOPE | Service Request流控阈值作用范围 | 可选必选说明：可选参数<br>参数含义：该参数用于设置Service Request消息流控阈值的作用范围。<br>数据来源：全网规划<br>取值范围：<br>- “POD（单POD）”：表示SRTHD参数指定的值是单POD每秒钟可以通过的消息数。<br>- “SYSTEM（整系统）”：表示SRTHD参数指定的值是整系统每秒钟可以通过的消息数。每个POD独立进行流控，整系统的流控阈值除以POD个数作为每个POD的流控阈值。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST INTERAMFFC查询当前参数配置值。<br>配置原则：<br>建议配置为“SYSTEM（整系统）”，AMF扩缩容场景下可以保持整系统对后端的流控能力保持不变。 |
| SRTHD | Service Request速率门限(个/秒) | 可选必选说明：可选参数<br>参数含义：用于设置Service Request速率门限。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~640000，单位是个每秒。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST INTERAMFFC查询当前参数配置值。<br>配置原则：<br>当参数“SRSCOPE”取值为“POD（单POD）”时，本参数的取值范围为0-10000。<br>当参数“SRSCOPE”取值为“SYSTEM（整系统）”时，本参数的取值范围为0-640000。 |
| STARTALMTIMES | 告警上报周期数 | 可选必选说明：可选参数<br>参数含义：该参数用于设置连续几个5秒周期处于流控态上报“ALM-100251 Inter-AMF流控起控”告警。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~255。如果值为0，则因流控而导致丢包后立即上报告警。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST INTERAMFFC查询当前参数配置值。<br>配置原则：<br>该参数设置过低，可能导致Inter-AMF消息突发而触发“Inter-AMF流控起控告警”，设置过高，会导致长时间流控但不上报告警。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@INTERAMFFC]] · Inter-AMF流控参数（INTERAMFFC）

## 使用实例

设置Registration Request接入速率门限为100个/秒，Service Request接入速率门限为200个/秒，按单POD粒度进行阈值控制：

```
SET INTERAMFFC:FCSWITCH=ON,REGTHD=100,SRTHD=200,REGSCOPE=POD,SRSCOPE=POD;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-INTERAMFFC.md`
