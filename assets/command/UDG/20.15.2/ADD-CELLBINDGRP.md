---
id: UDG@20.15.2@MMLCommand@ADD CELLBINDGRP
type: MMLCommand
name: ADD CELLBINDGRP（增加小区和小区组绑定关系）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: CELLBINDGRP
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
max_records: 10000
category_path:
- TCP优化服务管理
- 小区组绑定
status: active
---

# ADD CELLBINDGRP（增加小区和小区组绑定关系）

## 功能

**适用NF：PGW-U、UPF**

该命令用于增加小区和小区组的绑定关系，实现基于小区的TCP优化参数定制化功能。

## 注意事项

- 该命令执行后只对之后发生承载更新的用户或者新激活用户生效。
- 该命令最大记录数为10000。
- 一个小区只能绑定到一个小区组中。
- 系统内最多存在10个小区组。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CELLGROUPNAME | 小区组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于设置小区组名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该命令最多可配置10个CELLGROUPNAME。 |
| CELLNAME | 小区名称 | 可选必选说明：必选参数<br>参数含义：指定小区名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD CELL命令配置生成。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/CELLBINDGRP]] · 小区和小区组绑定关系（CELLBINDGRP）

## 使用实例

假如运营商需要将名称为TestCellName的小区绑定到名称为TestCellGroupName的小区组：

```
ADD CELLBINDGRP: CELLGROUPNAME="TestCellGroupName",CELLNAME="TestCellName";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/ADD-CELLBINDGRP.md`
