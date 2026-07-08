---
id: UNC@20.15.2@MMLCommand@ADD BSFAPNGROUP
type: MMLCommand
name: ADD BSFAPNGROUP（增加APN组）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: BSFAPNGROUP
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 本局信息管理
- SMF
- BSF信息管理
status: active
---

# ADD BSFAPNGROUP（增加APN组）

## 功能

该命令用于配置APN组。

## 注意事项

- 该命令执行后立即生效。

- 最多可输入25000条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GRPNAME | APN组名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN组名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~31。<br>默认值：无<br>配置原则：无 |
| APN | APN名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：<br>输入的APN名称需要符合APN命名规则。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/BSFAPNGROUP]] · APN组（BSFAPNGROUP）

## 使用实例

在APN组"apngroup1"中新增APN信息"huawei.com"：

```
ADD BSFAPNGROUP: GRPNAME="apngroup1", APN="huawei.com";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-BSFAPNGROUP.md`
