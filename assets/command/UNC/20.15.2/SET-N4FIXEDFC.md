---
id: UNC@20.15.2@MMLCommand@SET N4FIXEDFC
type: MMLCommand
name: SET N4FIXEDFC（设置指定消息类型固定速率流控信息）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: N4FIXEDFC
command_category: 配置类
applicable_nf:
- SGW-C
- PGW-C
- SMF
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- PFCP接口管理
- UP管理
- N4接口固定速率
status: active
---

# SET N4FIXEDFC（设置指定消息类型固定速率流控信息）

## 功能

![](设置指定消息类型固定速率流控信息（SET N4FIXEDFC）_35374751.assets/notice_3.0-zh-cn_2.png)

存在较大操作风险，执行不当会导致业务受损或中断。

**适用NF：SGW-C、PGW-C、SMF、GGSN**

设置指定N4接口的消息的固定速率门限，减少其它网元对UNC的冲击，以及减少UNC对其它网元的冲击。

## 注意事项

- 该命令执行后立即生效。

- 当MSGTYPE值为MULTIDNN时，FCSWITCH初始值为“ON”，THRESHOLD初始值为2000。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| MSGTYPE | FCSWITCH | THRESHOLD |
| --- | --- | --- |
| ERRIND | ON | 500 |
| DLDATA | ON | 2000 |
| UPSDR | ON | 500 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MSGTYPE | 流控消息类型 | 可选必选说明：必选参数<br>参数含义：该参数用于设置N4接口被流控的消息类型。<br>数据来源：全网规划<br>取值范围：<br>- “ERRIND（错误指示）”：表示ERIR（Error Indication Report）类型的PFCP Session Report Request消息。<br>- “DLDATA（下行数据）”：表示DLDR（Downlink Data Report）类型的PFCP Session Report Request消息。<br>- “UPSDR（用户面发起的会话删除）”：表示UPDR（User Plane Session Delete Report）类型的PFCP Session Report Request消息。<br>- “MULTIDNN（基于多DNN的漫游分流）”：表示MultiDNN（基于多DNN的漫游分流）类型的PFCP Session Report Request消息<br>默认值：无。<br>配置原则：无 |
| FCSWITCH | 固定速率流控开关 | 可选必选说明：必选参数<br>参数含义：该参数用于控制N4接口指定消息类型固定速率流控功能。<br>数据来源：全网规划<br>取值范围：<br>- “OFF（关闭）”：关闭N4接口的“固定速率流控”功能。<br>- “ON（开启）”：开启N4接口的“固定速率流控”功能。<br>默认值：无。<br>配置原则：<br>当希望开启指定消息类型流控功能时，设置为"On"；当希望关闭指定消息类型流控功能时，设置为"Off"。 |
| THRESHOLD | 流控速率门限(个/秒) | 可选必选说明：该参数在"FCSWITCH"配置为"ON"时为条件可选参数。<br>参数含义：该参数用于设置N4接口指定消息的流控速率上限。该参数针对单POD指定消息类型进行流控。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~1000000。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST N4FIXEDFC查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/N4FIXEDFC]] · 指定消息类型固定速率流控信息（N4FIXEDFC）

## 使用实例

针对上报类型为DownlinkData的PFCP Session Report Request开启固定速率流控，速率门限是单POD 2000个/秒，执行如下命令：

```
SET N4FIXEDFC: MSGTYPE=DLDATA, FCSWITCH=ON, THRESHOLD=2000;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置指定消息类型固定速率流控信息（SET-N4FIXEDFC）_35374751.md`
