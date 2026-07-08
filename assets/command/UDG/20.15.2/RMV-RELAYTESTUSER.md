---
id: UDG@20.15.2@MMLCommand@RMV RELAYTESTUSER
type: MMLCommand
name: RMV RELAYTESTUSER（删除媒体中继拨测用户）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: RELAYTESTUSER
command_category: 配置类
applicable_nf:
- UPF
- PGW-U
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 媒体中继
- 媒体中继拨测用户配置
status: active
---

# RMV RELAYTESTUSER（删除媒体中继拨测用户）

## 功能

**适用NF：UPF、PGW-U**

该命令用于删除媒体中继拨测用户。

## 注意事项

该命令执行后只对之后发生承载更新的用户或者新激活用户生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TESTUSERNAME | 拨测用户名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定拨测用户名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [媒体中继拨测用户（RELAYTESTUSER）](configobject/UDG/20.15.2/RELAYTESTUSER.md)

## 使用实例

删除媒体中继拨测用户：

```
RMV RELAYTESTUSER:TESTUSERNAME="user01";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除媒体中继拨测用户（RMV-RELAYTESTUSER）_43992618.md`
