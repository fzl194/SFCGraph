---
id: UDG@20.15.2@MMLCommand@ADD CELL
type: MMLCommand
name: ADD CELL（增加小区）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: CELL
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
max_records: 10000
category_path:
- TCP优化服务管理
- 小区配置
status: active
---

# ADD CELL（增加小区）

## 功能

**适用NF：PGW-U、UPF**

该命令用于增加小区信息，实现基于小区的TCP优化策略管理。

## 注意事项

- 该命令执行后只对之后发生承载更新的用户或者新激活用户生效。
- 该命令最大记录数为10000。
- 小区名称不区分大小写，配置的多条小区名称之间不允许存在重复关系。
- 一个小区ID只能对应一个小区名称。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CELLNAME | 小区名称 | 可选必选说明：必选参数<br>参数含义：该参数用于设置小区名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该命令最多可配置10000个CELLNAME。 |
| CELLID | 小区ID | 可选必选说明：必选参数<br>参数含义：该参数用于指定小区ID。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/CELL]] · 小区（CELL）

## 使用实例

假如运营商需要增加一个小区，小区名称是TestCellName,小区ID是123456789：

```
ADD CELL: CELLNAME="TestCellName",CELLID=123456789;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/增加小区（ADD-CELL）_93415785.md`
