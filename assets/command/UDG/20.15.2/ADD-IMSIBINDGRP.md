---
id: UDG@20.15.2@MMLCommand@ADD IMSIBINDGRP
type: MMLCommand
name: ADD IMSIBINDGRP（增加IMSI和IMSI组绑定关系）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: IMSIBINDGRP
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
max_records: 64
category_path:
- TCP优化服务管理
- IMSI组配置
status: active
---

# ADD IMSIBINDGRP（增加IMSI和IMSI组绑定关系）

## 功能

**适用NF：PGW-U、UPF**

该命令用于增加IMSI和IMSI组的绑定关系，实现基于ISMI的TCP优化参数定制化功能。

## 注意事项

- 该命令执行后只对之后发生承载更新的用户或者新激活用户生效。
- 该命令最大记录数为64。
- 一个IMSI只能绑定到一个IMSI组中。
- 一个IMSI组最多允许绑定8个IMSI。
- 系统内最多存在8个IMSI组。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IMSI | IMSI | 可选必选说明：必选参数<br>参数含义：该参数用于表示用户的IMSI号。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～15。每个字符必须为0~9的数字。<br>默认值：无<br>配置原则：无 |
| IMSIGROUPNAME | IMSI 组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于设置IMSI组名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/IMSIBINDGRP]] · IMSI和IMSI组绑定关系（IMSIBINDGRP）

## 使用实例

假如运营商需要将名称为123456789的IMSI绑定到名称为TestIMSIGroupName的IMSI组：

```
ADD IMSIBINDGRP: IMSIGROUPNAME="TestIMSIGroupName",IMSI="123456789";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/增加IMSI和IMSI组绑定关系（ADD-IMSIBINDGRP）_93335769.md`
