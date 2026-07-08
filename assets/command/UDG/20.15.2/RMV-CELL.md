---
id: UDG@20.15.2@MMLCommand@RMV CELL
type: MMLCommand
name: RMV CELL（删除小区）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: CELL
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- TCP优化服务管理
- 小区配置
status: active
---

# RMV CELL（删除小区）

## 功能

**适用NF：PGW-U、UPF**

该命令用于删除小区信息。当运行商希望取消某些小区的TCP优化参数定制化功能时，则配置该命令。

## 注意事项

- 该命令执行后只对之后发生承载更新的用户或者新激活用户生效。
- 如果小区和小区组存在绑定关系，则不允许删除该小区。
- 如果不输入小区名称，批量删除系统中所有小区。
- 如果部分小区和小区组存在绑定关系，则批量删除不会删除任何小区。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CELLNAME | 小区名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置小区名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/CELL]] · 小区（CELL）

## 使用实例

假如运营商需要删除名称为TestCellName的小区信息：

```
RMV CELL: CELLNAME="TestCellName";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除小区（RMV-CELL）_87336170.md`
