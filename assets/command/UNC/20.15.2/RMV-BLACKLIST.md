---
id: UNC@20.15.2@MMLCommand@RMV BLACKLIST
type: MMLCommand
name: RMV BLACKLIST（删除黑名单地址列表）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: BLACKLIST
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
- GGSN
effect_mode: 对新用户生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- UE地址管理
- 静态地址黑名单管理
status: active
---

# RMV BLACKLIST（删除黑名单地址列表）

## 功能

**适用NF：PGW-C、SMF、GGSN**

该命令用于删除静态地址IP黑名单。

## 注意事项

该命令执行后只对新激活用户生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NAME | 名称 | 可选必选说明：必选参数<br>参数含义：黑名单地址段名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~79。不支持空格及特殊字符“#”、“$”和“&”等，由“-”、“_”、数字、字母和“.”组成，不能以“.”开头或结尾，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [黑名单地址列表（BLACKLIST）](configobject/UNC/20.15.2/BLACKLIST.md)

## 使用实例

删除名称为testblacklist的静态地址黑名单：

```
RMV BLACKLIST:NAME="testblacklist";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除黑名单地址列表（RMV-BLACKLIST）_44007543.md`
