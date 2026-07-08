---
id: UNC@20.15.2@MMLCommand@SET AMFNASFIXEDFC
type: MMLCommand
name: SET AMFNASFIXEDFC（设置指定消息类型的AMF NAS固定速率流控信息）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: AMFNASFIXEDFC
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
- AMF NAS固定速率流控
status: active
---

# SET AMFNASFIXEDFC（设置指定消息类型的AMF NAS固定速率流控信息）

## 功能

![](设置指定消息类型的AMF NAS固定速率流控信息（SET AMFNASFIXEDFC）_53830207.assets/notice_3.0-zh-cn_2.png)

存在较大操作风险，执行不当会导致业务受损或中断。

**适用NF：AMF**

设置指定NAS消息类型的固定速率门限，减少其它网元对UNC的冲击，以及减少UNC对其它网元的冲击。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| MSGTYPE | FCSWITCH | THRESHOLD | SCOPE |
| --- | --- | --- | --- |
| PDUSESSIONEST | ON | 1500 | POD |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MSGTYPE | 流控消息类型 | 可选必选说明：必选参数<br>参数含义：该参数用于设置AMF被流控的NAS消息类型。<br>数据来源：全网规划<br>取值范围：<br>- PDUSESSIONEST（PDU Session Establishment Request）<br>默认值：无。<br>配置原则：无 |
| FCSWITCH | 固定速率流控开关 | 可选必选说明：可选参数<br>参数含义：该参数用于控制AMF指定NAS消息类型固定速率流控功能。<br>数据来源：全网规划<br>取值范围：<br>- “OFF（关闭）”：关闭<br>- “ON（打开）”：打开<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST AMFNASFIXEDFC查询当前参数配置值。<br>配置原则：无 |
| THRESHOLD | 流控速率门限(个/秒) | 可选必选说明：该参数在"FCSWITCH"配置为"ON"时为条件可选参数。<br>参数含义：该参数用于设置AMF指定NAS消息的接收流控速率上限。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~1000000。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST AMFNASFIXEDFC查询当前参数配置值。<br>配置原则：无 |
| SCOPE | 流控阈值作用范围 | 可选必选说明：该参数在"FCSWITCH"配置为"ON"时为条件可选参数。<br>参数含义：该参数用于设置AMF NAS消息流控阈值的作用范围。<br>数据来源：全网规划<br>取值范围：<br>- “SYSTEM（整系统）”：表示THRESHOLD参数指定的值是整系统每秒钟可以通过的消息数。<br>- “POD（单usn-pod）”：表示THRESHOLD参数指定的值是单usn-pod每秒钟可以通过的消息数。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST AMFNASFIXEDFC查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/AMFNASFIXEDFC]] · 指定消息类型的AMF NAS固定速率流控信息（AMFNASFIXEDFC）

## 使用实例

针对PDU Session Establisthment Request开启固定速率流控，按照单usn-pod配置速率门限是1000个/秒，执行如下命令：

```
SET AMFNASFIXEDFC: MSGTYPE=PDUSESSIONEST, FCSWITCH=ON, THRESHOLD=1000, SCOPE=POD;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置指定消息类型的AMF-NAS固定速率流控信息（SET-AMFNASFIXEDFC）_53830207.md`
