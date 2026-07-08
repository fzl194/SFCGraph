---
id: UNC@20.15.2@MMLCommand@SET SMSCHFGRP
type: MMLCommand
name: SET SMSCHFGRP（设置短消息计费CHF组）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: SMSCHFGRP
command_category: 配置类
applicable_nf:
- SMSF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- SMSF业务管理
- CHF管理
status: active
---

# SET SMSCHFGRP（设置短消息计费CHF组）

## 功能

**适用NF：SMSF**

在SMSF/VLR短消息计费的场景下，通过本命令配置计费CHF组，SMSF/VLR从计费CHF组中选择可用的CHF进行计费处理。

## 注意事项

- 该命令执行后立即生效。

- 该命令参数输入空格或者null（不区分大小写）清空参数值。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| PRIMARYCHFGRP | SECONDARYCHFGRP |
| --- | --- |
| null | null |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PRIMARYCHFGRP | 主CHF组的名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置主CHF组的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SMSCHFGRP查询当前参数配置值。<br>配置原则：<br>该参数使用ADD TNFGRP命令配置生成。 |
| SECONDARYCHFGRP | 备CHF组的名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置备CHF组的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SMSCHFGRP查询当前参数配置值。<br>配置原则：<br>该参数使用ADD TNFGRP命令配置生成。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SMSCHFGRP]] · 短消息计费CHF组（SMSCHFGRP）

## 使用实例

配置短消息计费的chf组主为“SMS CHF Group1”，备为“SMS CHF Group2”：

```
SET SMSCHFGRP: PRIMARYCHFGRP="SMS CHF Group1", SECONDARYCHFGRP="SMS CHF Group2";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置短消息计费CHF组（SET-SMSCHFGRP）_77419832.md`
