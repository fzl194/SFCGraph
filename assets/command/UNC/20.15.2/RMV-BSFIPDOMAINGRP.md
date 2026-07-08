---
id: UNC@20.15.2@MMLCommand@RMV BSFIPDOMAINGRP
type: MMLCommand
name: RMV BSFIPDOMAINGRP（删除IPDOMAIN组）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: BSFIPDOMAINGRP
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 本局信息管理
- SMF
- BSF信息管理
status: active
---

# RMV BSFIPDOMAINGRP（删除IPDOMAIN组）

## 功能

该命令用于删除IPDOMAIN组。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GRPNAME | IPDOMAIN组名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定IPDOMAIN组名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~31。<br>默认值：无<br>配置原则：无 |
| IPDOMAIN | IPDOMAIN名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定IPDOMAIN名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~255。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/BSFIPDOMAINGRP]] · IPDOMAIN组（BSFIPDOMAINGRP）

## 使用实例

在IPDOMAIN组"ipdomaingroup1"中删除IPDOMAIN信息"Domain_0"：

```
RMV BSFIPDOMAINGRP: GRPNAME="ipdomaingroup1", IPDOMAIN="Domain_0";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-BSFIPDOMAINGRP.md`
