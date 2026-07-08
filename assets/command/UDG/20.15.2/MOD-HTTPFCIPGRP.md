---
id: UDG@20.15.2@MMLCommand@MOD HTTPFCIPGRP
type: MMLCommand
name: MOD HTTPFCIPGRP（修改HTTP流控组）
nf: UDG
version: 20.15.2
verb: MOD
object_keyword: HTTPFCIPGRP
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- HTTP功能管理
- HTTP流控管理
- HTTP流控组管理
status: active
---

# MOD HTTPFCIPGRP（修改HTTP流控组）

## 功能

该命令用于修改HTTP固定速率流控组的IP地址组信息。

> **说明**
> 该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INDEX | IP地址索引 | 可选必选说明：必选参数<br>参数含义：该参数用于标识具有相同前缀的一组IP地址。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~4095。<br>默认值：无<br>配置原则：无 |
| DESC | 描述 | 可选必选说明：可选参数<br>参数含义：该参数用于填写HTTP固定速率流控地址组的描述信息，建议包含NF类型，实例名等，例如UDM_UDM001。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/HTTPFCIPGRP]] · HTTP流控组（HTTPFCIPGRP）

## 使用实例

修改索引为1的HTTP固定速率流控地址组信息，描述信息由"HTTPFCIPGRP"改为"MODHTTPFCIPGRP"：

```
MOD HTTPFCIPGRP:INDEX=1,DESC="MODHTTPFCIPGRP";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改HTTP流控组（MOD-HTTPFCIPGRP）_29291773.md`
