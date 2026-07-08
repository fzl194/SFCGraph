---
id: UNC@20.15.2@MMLCommand@RMV MULDNNPRILIST
type: MMLCommand
name: RMV MULDNNPRILIST（删除本地专网DNN就近接入优先级）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: MULDNNPRILIST
command_category: 配置类
applicable_nf:
- SMF
- PGW-C
effect_mode: 对新用户生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 智能分流专网DNN管理
status: active
---

# RMV MULDNNPRILIST（删除本地专网DNN就近接入优先级）

## 功能

**适用NF：SMF、PGW-C**

该命令用于删除指定智能分流专网DNN接入省/市的优先级。

## 注意事项

该命令执行后只对新激活用户生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DEDDNN | 智能分流专网DNN | 可选必选说明：必选参数<br>参数含义：该参数用于指定智能分流专网DNN。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。<br>默认值：无<br>配置原则：<br>字符串类型，输入长度范围是1~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。 |

## 操作的配置对象

- [本地专网DNN就近接入优先级（MULDNNPRILIST）](configobject/UNC/20.15.2/MULDNNPRILIST.md)

## 使用实例

删除本地专网DNN就近接入优先级，智能分流专网DNN为“special.dnn”。

```
RMV MULDNNPRILIST: DEDDNN="special.dnn";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除本地专网DNN就近接入优先级（RMV-MULDNNPRILIST）_87893234.md`
