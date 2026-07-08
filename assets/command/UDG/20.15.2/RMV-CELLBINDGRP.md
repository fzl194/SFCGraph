---
id: UDG@20.15.2@MMLCommand@RMV CELLBINDGRP
type: MMLCommand
name: RMV CELLBINDGRP（删除小区和小区组绑定关系）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: CELLBINDGRP
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- TCP优化服务管理
- 小区组绑定
status: active
---

# RMV CELLBINDGRP（删除小区和小区组绑定关系）

## 功能

**适用NF：PGW-U、UPF**

该命令用于删除小区和小区组的绑定关系。当运行商希望删除小区和小区组的绑定关系时，则配置该命令。

## 注意事项

- 该命令执行后只对之后发生承载更新的用户或者新激活用户生效。
- 如果不输入小区名称只输入小区组名称，则批量删除系统中所有小区和该小区组之间的绑定关系。
- 如果不输入小区名称和小区组，则批量删除系统中所有小区与小区组之间的绑定关系。
- 如果小区组被TO策略匹配规则作为匹配条件，则不允许对该小区组进行批量删除操作。
- 如果小区组被TO策略匹配规则作为匹配条件，且只有一个小区和该小区组存在绑定关系时，不允许删除的该小区和该小区组之间的绑定关系。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CELLGROUPNAME | 小区组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置小区组名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD CELLBINDGRP命令配置生成。 |
| CELLNAME | 小区名称 | 可选必选说明：可选参数<br>参数含义：指定小区名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD CELL命令配置生成。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/CELLBINDGRP]] · 小区和小区组绑定关系（CELLBINDGRP）

## 使用实例

运营商需要删除名称为TestCellName的小区和名称为TestCellGroupName的小区组的绑定关系：

```
RMV CELLBINDGRP: CELLGROUPNAME="TestCellGroupName", CELLNAME="TestCellName";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-CELLBINDGRP.md`
