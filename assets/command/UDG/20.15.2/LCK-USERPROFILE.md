---
id: UDG@20.15.2@MMLCommand@LCK USERPROFILE
type: MMLCommand
name: LCK USERPROFILE（设置用户模板的锁定）
nf: UDG
version: 20.15.2
verb: LCK
object_keyword: USERPROFILE
command_category: 动作类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: true
category_path:
- 用户面服务管理
- 业务匹配策略
- 业务匹配公共配置
- 业务规则管理
- 用户模板
status: active
---

# LCK USERPROFILE（设置用户模板的锁定）

## 功能

**适用NF：PGW-U、UPF**

![](设置用户模板的锁定（LCK USERPROFILE）_97358675.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，正在改变用户模板的锁定状态，如果配置为锁定，会导致用户接入失败。

该命令用于设置用户模板的锁定。

## 注意事项

- 此命令用来设置UserProfile是否锁定，在锁定UserProfile后，禁止使用UserProfile。当需要按照UserProfile去活用户时，需先锁定该UserProfile。由ENABLE状态设置为DISABLE状态，需要判断是否已经将UserProfile下用户都去活成功，如果正在去活用户，则禁止修改。
- 对于每个UserProfile，初始的锁定标记为DISABLE。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| USERPROFILENAME | 用户模板名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定用户模板名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格及“,”、“;”、“"”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD USERPROFILE命令配置生成。 |
| LOCKFLAG | 锁定标记 | 可选必选说明：必选参数<br>参数含义：指定锁定标记。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能（关闭）。<br>- ENABLE：使能（开启）。<br>默认值：无<br>配置原则：<br>- 如果运营商不希望按照用户模板去活用户时，则配置该参数为DISABLE。<br>- 如果运营商希望按照用户模板去活用户时，则配置该参数为ENABLE。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/USERPROFILE]] · 用户模板（USERPROFILE）

## 使用实例

假如运营商需要锁定名称为“testuserprofilename”的用户模板：

```
LCK USERPROFILE:USERPROFILENAME="testuserprofilename",LOCKFLAG=ENABLE;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置用户模板的锁定（LCK-USERPROFILE）_97358675.md`
