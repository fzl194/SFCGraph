---
id: UNC@20.15.2@MMLCommand@MOD NWDAFINFO
type: MMLCommand
name: MOD NWDAFINFO（修改NWDAF信息）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: NWDAFINFO
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 本局信息管理
- NWDAF
status: active
---

# MOD NWDAFINFO（修改NWDAF信息）

## 功能

该命令用于修改NWDAF实例信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INSTANCENAME | NWDAF实例名称 | 可选必选说明：必选参数<br>参数含义：该参数用于唯一指定某一个NWDAF实例。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~50。本参数的构成字符只能是字母A~Z或a~z、数字0~9、下划线“_”和中划线“-”，例如，NWDAF_Instance_0。<br>默认值：无<br>配置原则：<br>本参数来源于ADD NFUUID命令中的“NF实例名称”参数。 |
| NWDAFEVENTS | NWDAF数据分析事件 | 可选必选说明：可选参数<br>参数含义：该参数用于指定NWDAF支持的分析事件类型。<br>数据来源：本端规划<br>取值范围：<br>- QOS_ANALYSIS（QOS分析）<br>- QOS_EXP_ANALYSIS（体验感知信息分析）<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NWDAFINFO]] · NWDAF信息（NWDAFINFO）

## 使用实例

修改NWDAF信息，NWDAF实例名称为nwdaf_Instance_1，支持的NWADFEVENTS类型为QOS_ANALYSIS。

```
MOD NWDAFINFO: INSTANCENAME="nwdaf_Instance_1", NWDAFEVENTS=QOS_ANALYSIS-1&QOS_EXP_ANALYSIS-0;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-NWDAFINFO.md`
