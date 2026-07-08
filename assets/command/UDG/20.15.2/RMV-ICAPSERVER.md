---
id: UDG@20.15.2@MMLCommand@RMV ICAPSERVER
type: MMLCommand
name: RMV ICAPSERVER（删除ICAP服务器）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: ICAPSERVER
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- ICAPC管理
- ICAP服务器
status: active
---

# RMV ICAPSERVER（删除ICAP服务器）

## 功能

**适用NF：PGW-U、UPF**

该命令用于删除指定名称的ICAP Server配置。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ICAPSERVERNAME | ICAP服务器名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定ICAP Server的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格。不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [ICAP服务器（ICAPSERVER）](configobject/UDG/20.15.2/ICAPSERVER.md)

## 使用实例

删除指定名称为is1的ICAP Server配置：

```
RMV ICAPSERVER: ICAPSERVERNAME="is1";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除ICAP服务器（RMV-ICAPSERVER）_29222370.md`
