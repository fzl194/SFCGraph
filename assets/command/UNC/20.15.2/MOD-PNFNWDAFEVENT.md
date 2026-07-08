---
id: UNC@20.15.2@MMLCommand@MOD PNFNWDAFEVENT
type: MMLCommand
name: MOD PNFNWDAFEVENT（修改对端NWDAF信息）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: PNFNWDAFEVENT
command_category: 配置类
applicable_nf:
- AMF
- SMF
- NSSF
- SMSF
- NCG
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 服务化接口管理
- 注册与服务发现
- 本地NRF功能管理
- 对端NWDAF信息管理
status: active
---

# MOD PNFNWDAFEVENT（修改对端NWDAF信息）

## 功能

**适用NF：AMF、SMF、NSSF、SMSF、NCG**

该命令用于修改本地配置的对端NWDAF的信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFINSTANCEID | NF实例标识 | 可选必选说明：必选参数<br>参数含义：该参数用于唯一指定某一个NWDAF实例。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~38。本参数的构成字符只能是字母A~Z或a~z、数字0~9、下划线“_”和中划线“-”，例如，NWDAF_Instance_0。<br>默认值：无<br>配置原则：无 |
| NWDAFINFOID | NwdafInfo标识 | 可选必选说明：可选参数<br>参数含义：该参数用于唯一标识NWDAF实例中的某个NwdafInfo。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~32。该参数大小写不敏感。<br>默认值：无<br>配置原则：无 |
| NWDAFEVENTS | NWDAF数据分析事件 | 可选必选说明：必选参数<br>参数含义：该参数用于指定NWDAF支持的分析事件类型。<br>数据来源：本端规划<br>取值范围：<br>- QOS_ANALYSIS（QOS分析）<br>- QOS_EXP_ANALYSIS（体验感知信息分析）<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PNFNWDAFEVENT]] · 对端NWDAF信息（PNFNWDAFEVENT）

## 使用实例

修改对端NWDAF信息，NF实例标识为NWDAF_Instance_1，NwdafInfo标识为central，NWDAF数据分析事件为QOS_ANALYSIS。

```
MOD PNFNWDAFEVENT: NFINSTANCEID="NWDAF_Instance_1", NWDAFINFOID="central", NWDAFEVENTS=QOS_ANALYSIS-1&QOS_EXP_ANALYSIS-0;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改对端NWDAF信息（MOD-PNFNWDAFEVENT）_56105694.md`
