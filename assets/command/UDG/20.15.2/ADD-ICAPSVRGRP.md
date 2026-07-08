---
id: UDG@20.15.2@MMLCommand@ADD ICAPSVRGRP
type: MMLCommand
name: ADD ICAPSVRGRP（增加ICAP服务器组）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: ICAPSVRGRP
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 30
category_path:
- 用户面服务管理
- ICAPC管理
- ICAP服务器组
status: active
---

# ADD ICAPSVRGRP（增加ICAP服务器组）

## 功能

**适用NF：PGW-U、UPF**

该命令用于增加一个ICAP Server Group实例。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为30。
- 每种类型下最大为30。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ICAPSVRGRPNAME | ICAP服务器组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定ICAP Server Group的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格。不区分大小写。<br>默认值：无<br>配置原则：无 |
| ICAPSERVERTYPE | ICAP服务器类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定ICAP Server服务器类型。<br>数据来源：本端规划<br>取值范围：<br>- URL_FILTERING：支持URL过滤的ICAP服务器。<br>默认值：无<br>配置原则：无 |
| CFGDOMAINNAME | 配置域名称 | 可选必选说明：可选参数<br>参数含义：该参数表示命令所属公共配置域的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@ICAPSVRGRP]] · ICAP服务器组（ICAPSVRGRP）

## 关联任务

- [[UDG@20.15.2@Task@0-00260]]

## 使用实例

增加一个ICAP Server Group实例：

```
ADD ICAPSVRGRP: ICAPSVRGRPNAME="isg1",ICAPSERVERTYPE=URL_FILTERING;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/ADD-ICAPSVRGRP.md`
