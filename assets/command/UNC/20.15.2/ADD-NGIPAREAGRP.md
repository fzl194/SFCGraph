---
id: UNC@20.15.2@MMLCommand@ADD NGIPAREAGRP
type: MMLCommand
name: ADD NGIPAREAGRP（增加5G IP区域群）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: NGIPAREAGRP
command_category: 配置类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- IP细分管理
- 5G IP细分区域组管理
status: active
---

# ADD NGIPAREAGRP（增加5G IP区域群）

## 功能

**适用NF：AMF**

该命令用于增加5G IP区域群。IP区域群是“基于位置的地址分配”功能的一个基本概念，由TAC组成，在同一个IP区域群中的用户具有相同的IP地址分配策略。

## 注意事项

- 命令执行后只对新接入用户生效。

- 最多可输入256条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| AREAID | 区域群标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定区域群标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~64。<br>默认值：无<br>配置原则：无 |
| IPAREASW | IP区域开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定打开或者关闭IP区域群管理功能。<br>“IPAREASW(IP区域开关)”开启后，用户移动符合如下情况时，用户的PDU会话将会被强制释放：<br>从IP区域群外移动到IP区域群内。<br>从IP区域群内移动到IP区域群外。<br>从一个IP区域群移动到另一个IP区域群。<br>数据来源：全网规划<br>取值范围：<br>- “OFF（关闭）”：关闭<br>- “ON（开启）”：开启<br>默认值：OFF<br>配置原则：无 |
| ROAMUSRSW | 漫游用户开关 | 可选必选说明：该参数在"IPAREASW"配置为"ON"时为条件可选参数。<br>参数含义：该参数用于设置漫游用户接入限制开关。如果设置为ON，漫游用户在本区域不允许接入。<br>数据来源：全网规划<br>取值范围：<br>- “OFF（关闭）”：关闭<br>- “ON（开启）”：开启<br>默认值：OFF<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NGIPAREAGRP]] · 5G IP区域群（NGIPAREAGRP）

## 使用实例

增加一个IP区域群，打开IP区域管理功能，执行如下命令：

```
ADD NGIPAREAGRP: AREAID="SomeCity", IPAREASW=ON;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加5G-IP区域群（ADD-NGIPAREAGRP）_09653204.md`
