---
id: UDG@20.15.2@MMLCommand@ADD DRINST
type: MMLCommand
name: ADD DRINST（配置容灾实例）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: DRINST
command_category: 配置类
effect_mode: ''
is_dangerous: false
max_records: 1
category_path:
- 平台服务管理
- CSDB功能管理
- CSDB管理
- 容灾管理
status: active
---

# ADD DRINST（配置容灾实例）

## 功能

该命令用于配置本端容灾实例信息。

## 注意事项

本表最大记录数为1。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DRINSTID | 容灾实例ID | 可选必选说明：必选参数。<br>参数含义：该参数用于配置容灾实例标识。<br>数据来源：全网规划。<br>取值范围：整型，0~63。<br>默认值：无。 |
| DRINSTNAME | 容灾实例名称 | 可选必选说明：可选参数。<br>参数含义：该参数用于配置容灾实例名称。<br>数据来源：全网规划。<br>取值范围：字符串，输入范围1~31。不支持空格，区分大小写。<br>默认值：无。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/DRINST]] · 容灾实例（DRINST）

## 使用实例

增加 “容灾实例ID” 为 “2” 的容灾实例：

```
ADD DRINST: DRINSTID=2;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/ADD-DRINST.md`
