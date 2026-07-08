---
id: UDG@20.15.2@MMLCommand@RMV CONTCATEGROUP
type: MMLCommand
name: RMV CONTCATEGROUP（删除内容分类组）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: CONTCATEGROUP
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 内容过滤
- 内容分类组配置
status: active
---

# RMV CONTCATEGROUP（删除内容分类组）

## 功能

**适用NF：PGW-U、UPF**

该命令用于删除内容分类组。

## 注意事项

- 该命令执行后立即生效。
- 当内容分类组下配置了优先级时，输入内容分类组名称，同时将内容分类类型设置为PRIORITY，表示将该内容分类组下对应的优先级值赋值为默认优先级65535。
- 如果内容分类组下只存在两条记录，且内容分类类型分别为PRIORITY与非PRIORITY，执行RMV CONTCATEGROUP指定删除非PRIORITY类型的那一条记录时，PRIORITY类型的记录会同时被删除。
- 如果CONTCATEGROUP被CONTCATEGBIND引用，支持删除CONTCATEGROUP部分记录，但不支持删除该CONTCATEGROUP下配置的所有记录。若想要删除该CONTCATEGROUP下配置的所有记录，请先解除绑定关系。
- 指定条件删除（即不删除所有记录）时，必须要输入CONTCATEGNAME。
- 如果不输入任何参数，表示删除系统中所有的内容分类组配置。当配置量较大时单次执行可能无法删除全部记录，需要执行多次。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CONTCATEGNAME | 内容分类组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置内容分类组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| CATEGORYTYPE | 内容分类类型 | 可选必选说明：可选参数<br>参数含义：该参数用于设置内容分类类型。<br>数据来源：本端规划<br>取值范围：<br>- SPECIFIC：特定内容分类ID。<br>- RANGE：分类ID范围。<br>- PRIORITY：优先级。<br>- NAME：内容分类名称。<br>默认值：无<br>配置原则：无 |
| CATEGORYID | 内容分类值 | 可选必选说明：条件必选参数<br>前提条件：该参数在“CATEGORYTYPE”配置为“SPECIFIC” 或 “NAME”时为必选参数。<br>参数含义：该参数用于设置内容分类值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～65535。<br>默认值：无<br>配置原则：无 |
| STARTID | 内容分类起始值 | 可选必选说明：条件必选参数<br>前提条件：该参数在“CATEGORYTYPE”配置为“RANGE”时为必选参数。<br>参数含义：该参数用于设置内容分类起始值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～65535。<br>默认值：无<br>配置原则：无 |
| ENDID | 内容分类结束值 | 可选必选说明：条件必选参数<br>前提条件：该参数在“CATEGORYTYPE”配置为“RANGE”时为必选参数。<br>参数含义：该参数用于设置内容分类结束值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～65535。<br>默认值：无<br>配置原则：无 |
| CATEGORYNAME | 内容分类名称 | 可选必选说明：条件必选参数<br>前提条件：该参数在“CATEGORYTYPE”配置为“NAME”时为必选参数。<br>参数含义：该参数用于设置内容分类名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [内容分类组（CONTCATEGROUP）](configobject/UDG/20.15.2/CONTCATEGROUP.md)

## 使用实例

删除内容分类组名称为“cf_contcategrprange1”，内容分类类型为SPECIFIC，内容分类值为100的内容分类组：

```
RMV CONTCATEGROUP: CONTCATEGNAME="cf_contcategrprange1", CATEGORYTYPE=SPECIFIC, CATEGORYID=100;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除内容分类组（RMV-CONTCATEGROUP）_43076791.md`
