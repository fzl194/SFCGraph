---
id: UNC@20.15.2@MMLCommand@SET N2FIXEDFCBYMSG
type: MMLCommand
name: SET N2FIXEDFCBYMSG（设置指定消息类型固定速率流控信息）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: N2FIXEDFCBYMSG
command_category: 配置类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- N2接口管理
- N2接口固定速率流控管理
status: active
---

# SET N2FIXEDFCBYMSG（设置指定消息类型固定速率流控信息）

## 功能

![](设置指定消息类型固定速率流控信息（SET N2FIXEDFCBYMSG）_96805504.assets/notice_3.0-zh-cn_2.png)

存在较大操作风险，执行不当会导致业务受损或中断。

**适用NF：AMF**

设置指定消息类型的固定速率门限，减少其它网元对UNC的冲击，以及减少UNC对其它网元的冲击。

## 注意事项

- 该命令执行后立即生效。

- 如果消息类型是寻呼，由于区分高低优先级进行流控，可能导致寻呼消息速率略低于阈值时被流控。
- 系统部署完成后，首次下发该命令将新增1条配置记录：MSGTYPE默认值为PFI，FCSWITCH默认值为On，THRESHOLD默认值为1000。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| MSGTYPE | FCSWITCH | THRESHOLD |
| --- | --- | --- |
| NGSETUP | On | 500 |
| PAGING | On | 2000 |
| REGISTER | On | 1800 |
| SERVICEREQUEST | On | 3000 |
| PATHSWITCH | On | 8000 |
| WPWR | On | 1000 |
| PCR | On | 1000 |
| PRI | On | 1000 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MSGTYPE | 流控消息类型 | 可选必选说明：必选参数<br>参数含义：该参数用于设置N2接口被流控的消息类型。<br>数据来源：全网规划<br>取值范围：<br>- “NGSETUP（NG Setup Request）”：表示NG Setup Request消息。<br>- “PAGING（Paging）”：表示Paging消息。<br>- “REGISTER（Registration Request）”：表示Registration Request消息。<br>- “SERVICEREQUEST（Service Request）”：表示Service Request消息。<br>- “PATHSWITCH（Path Switch Request）”：表示Path Switch Request消息。<br>- “WPWR（Write-Replace Warning Response）”：表示Write-Replace Warning Response消息。<br>- “PCR（PWS Cancel Response）”：表示PWS Cancel Response消息。<br>- “PRI（PWS Restart Indication）”：表示PWS Restart Indication消息。<br>- “PFI（PWS Failure Indication）”：表示PWS Failure Indication消息。<br>默认值：无。<br>配置原则：无 |
| FCSWITCH | 固定速率流控开关 | 可选必选说明：必选参数<br>参数含义：该参数用于控制N2接口指定消息类型固定速率流控功能。<br>数据来源：全网规划<br>取值范围：<br>- “On（开启）”：开启N2接口的“固定速率流控”功能。<br>- “Off（关闭）”：关闭N2接口的“固定速率流控”功能。<br>默认值：无。<br>配置原则：<br>当希望开启指定消息类型流控功能时，设置为"On"；当希望关闭指定消息类型流控功能时，设置为"Off"。 |
| THRESHOLD | 流控速率门限(个/秒) | 可选必选说明：该参数在"FCSWITCH"配置为"On"时为条件可选参数。<br>参数含义：该参数用于设置N2接口指定消息的接收/发送流控速率上限。该参数针对单Pod指定消息类型进行流控。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~1000000，单位是个每秒。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST N2FIXEDFCBYMSG查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/N2FIXEDFCBYMSG]] · 指定消息类型固定速率流控信息（N2FIXEDFCBYMSG）

## 使用实例

针对的Registration Request开启固定速率流控，速率门限是单Pod 4000个/秒。执行如下命令：

```
SET N2FIXEDFCBYMSG:MSGTYPE=REGISTER,FCSWITCH=On,THRESHOLD=4000;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置指定消息类型固定速率流控信息（SET-N2FIXEDFCBYMSG）_96805504.md`
