---
id: UDG@20.15.2@MMLCommand@ADD CONTCATEGROUP
type: MMLCommand
name: ADD CONTCATEGROUP（增加内容分类组）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: CONTCATEGROUP
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 20200
category_path:
- 用户面服务管理
- 业务控制策略
- 内容过滤
- 内容分类组配置
status: active
---

# ADD CONTCATEGROUP（增加内容分类组）

## 功能

**适用NF：PGW-U、UPF**

该命令用于配置内容分类（content category）分组。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为20200。
- 整机支持200个内容分类组。每个内容分类组最多可配置101条内容分类记录，其中RANGE类型、SPECIFIC类型与NAME类型的内容分类记录数量不超过100个，PRIORITY类型的内容分类记录数量限制为1个。
- CATEGORYTYPE取值PRIORITY的内容分类组，其PRIORITY全局唯一。
- CATEGORYTYPE取值RANGE的内容分类组，其STARTID取值不能超过ENDID。
- 同一个内容分类组中，CATEGORYTYPE取值RANGE的所有记录对应的[STARTID, ENDID]不能有重叠。
- 若内容分类组名称为系统首次添加，且内容分类类型不是PRIORITY，添加该条记录的同时，会默认添加一条PRIORITY类型的记录，对应优先级为默认值65535。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CONTCATEGNAME | 内容分类组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于设置内容分类组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| CATEGORYTYPE | 内容分类类型 | 可选必选说明：必选参数<br>参数含义：该参数用于设置内容分类类型。<br>数据来源：本端规划<br>取值范围：<br>- SPECIFIC：特定内容分类ID。<br>- RANGE：分类ID范围。<br>- PRIORITY：优先级。<br>- NAME：内容分类名称。<br>默认值：无<br>配置原则：无 |
| STARTID | 内容分类起始值 | 可选必选说明：条件必选参数<br>前提条件：该参数在“CATEGORYTYPE”配置为“RANGE”时为必选参数。<br>参数含义：该参数用于设置内容分类起始值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～65535。<br>默认值：无<br>配置原则：无 |
| ENDID | 内容分类结束值 | 可选必选说明：条件必选参数<br>前提条件：该参数在“CATEGORYTYPE”配置为“RANGE”时为必选参数。<br>参数含义：该参数用于设置内容分类结束值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～65535。<br>默认值：无<br>配置原则：无 |
| CATEGORYID | 内容分类值 | 可选必选说明：条件必选参数<br>前提条件：该参数在“CATEGORYTYPE”配置为“SPECIFIC” 或 “NAME”时为必选参数。<br>参数含义：该参数用于设置内容分类值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～65535。<br>默认值：无<br>配置原则：无 |
| PRIORITY | 优先级 | 可选必选说明：条件必选参数<br>前提条件：该参数在“CATEGORYTYPE”配置为“PRIORITY”时为必选参数。<br>参数含义：该参数用于设置优先级。值越小优先级越高。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～65535。<br>默认值：无<br>配置原则：无 |
| CATEGORYNAME | 内容分类名称 | 可选必选说明：条件必选参数<br>前提条件：该参数在“CATEGORYTYPE”配置为“NAME”时为必选参数。<br>参数含义：该参数用于设置内容分类名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| CFGDOMAINNAME | 配置域名称 | 可选必选说明：可选参数<br>参数含义：该参数表示命令所属公共配置域的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [内容分类组（CONTCATEGROUP）](configobject/UDG/20.15.2/CONTCATEGROUP.md)

## 关联任务

- [0-00256](task/UDG/20.15.2/0-00256.md)

## 使用实例

假如运营商需要增加SPECIFIC类型的内容分类组，内容分类组名称为“cf_contcategrprange1”，内容分类值为100：

```
ADD CONTCATEGROUP: CONTCATEGNAME="cf_contcategrprange1", CATEGORYTYPE=SPECIFIC, CATEGORYID=100;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/增加内容分类组（ADD-CONTCATEGROUP）_39478824.md`
