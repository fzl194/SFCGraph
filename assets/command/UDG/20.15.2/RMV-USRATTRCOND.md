---
id: UDG@20.15.2@MMLCommand@RMV USRATTRCOND
type: MMLCommand
name: RMV USRATTRCOND（删除用户属性过滤条件）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: USRATTRCOND
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 对新用户生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务匹配策略
- 业务过滤器管理
- 用户属性管理
- 配置用户属性过滤条件
status: active
---

# RMV USRATTRCOND（删除用户属性过滤条件）

## 功能

**适用NF：PGW-U、UPF**

该命令用于删除用户属性过滤条件。当运营商希望删除用户属性过滤条件时，则配置该命令。

## 注意事项

- 该命令执行后只对新激活用户生效。
- 如果不输入过滤条件名称，表示删除系统中所有过滤条件。
- 如果过滤条件被用户属性引用，则不允许删除用户属性过滤条件。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CONDNAME | 过滤条件名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置过滤条件名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| ITEMID | 过滤条件项目索引 | 可选必选说明：可选参数<br>参数含义：该参数用于设置用户过滤条件项目索引。<br>数据来源：本端规划<br>取值范围：整数类型 ，取值范围是1~4294967295。<br>默认值：无<br>配置原则：如需使用该参数，请先输入CONDNAME。 |
| CONTENTTYPE | 内容类型 | 可选必选说明：可选参数<br>参数含义：该参数用于设置过滤条件内容类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- USER_PROFILE：用户模板。<br>- APN：APN。<br>- RAT：RAT类型。<br>- MSISDN：MSISDN。<br>默认值：无<br>配置原则：如需使用该参数，请先输入ITEMID。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@USRATTRCOND]] · 用户属性过滤条件（USRATTRCOND）

## 使用实例

运营商需要删除名称为user_cond1的过滤器：

```
RMV USRATTRCOND: CONDNAME="user_cond1";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-USRATTRCOND.md`
