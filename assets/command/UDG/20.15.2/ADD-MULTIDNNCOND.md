---
id: UDG@20.15.2@MMLCommand@ADD MULTIDNNCOND
type: MMLCommand
name: ADD MULTIDNNCOND（增加多DNN条件）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: MULTIDNNCOND
command_category: 配置类
applicable_nf:
- UPF
effect_mode: 对新流生效
is_dangerous: false
max_records: 10
category_path:
- 用户面服务管理
- 业务控制策略
- MultiDNN业务控制
- 多DNN条件
status: active
---

# ADD MULTIDNNCOND（增加多DNN条件）

## 功能

**适用NF：UPF**

该命令用于设置多DNN的名称条件，命中此条件的DNN，其业务进行domain学习时基于园区隔离。

## 注意事项

- 该命令执行后对新数据流生效。
- 该命令最大记录数为10。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DNNCONDTYPE | DNN条件类型 | 可选必选说明：必选参数<br>参数含义：该参数用于设置DNN名称的条件。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- IS：如果DNN名称等于DNNCONDVAL，则匹配中该条件。<br>- STARTS_WITH：如果DNN名称以DNNCONDVAL开始，则匹配中该条件。<br>- ENDS_WITH：如果DNN名称以DNNCONDVAL结束，则匹配中该条件。<br>- CONTAINS：如果DNN名称包含DNNCONDVAL，则匹配中该条件。<br>- ALL_DNN：所有DNN名称均能匹配中该条件。<br>默认值：无<br>配置原则：无 |
| DNNCONDVAL | DNN条件值 | 可选必选说明：条件必选参数<br>前提条件：该参数在“DNNCONDTYPE”配置为“STARTS_WITH”、“ENDS_WITH”、“CONTAINS” 或 “IS”时为必选参数。<br>参数含义：该参数用于设置DNN条件值。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不区分大小写, 只能由“-”、数字、大小写字母和“.”组成，不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”。当DNN条件类型为STARTS_WITH或IS时，该值不能以“.”开头。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/MULTIDNNCOND]] · 多DNN条件（MULTIDNNCOND）

## 使用实例

使用ADD MULTIDNNCOND命令添加DNN条件：

```
ADD MULTIDNNCOND: DNNCONDTYPE=ENDS_WITH, DNNCONDVAL="dnn1";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/ADD-MULTIDNNCOND.md`
