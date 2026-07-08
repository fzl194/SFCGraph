---
id: UNC@20.15.2@MMLCommand@ADD USRPROFGROUP
type: MMLCommand
name: ADD USRPROFGROUP（增加用户模板组）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: USRPROFGROUP
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
max_records: 10000
category_path:
- 业务服务管理
- 会话管理
- 计费和策略的业务管理
- 业务模板
- 用户模板组
status: active
---

# ADD USRPROFGROUP（增加用户模板组）

## 功能

**适用NF：PGW-C、SMF**

该命令用于配置一个用户模板组。可使用该用户模板组绑定多个PccProfile和UserProfile，并将该用户模板组绑定到用户APN。用户激活时，可根据APN选择到用户模板组，从而选择可用策略。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为10000。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| USERPROFGNAME | 用户模板组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定用户模板组的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [用户模板组（USRPROFGROUP）](configobject/UNC/20.15.2/USRPROFGROUP.md)

## 使用实例

增加一个名为userprofg1的用户模板组配置：

```
ADD USRPROFGROUP:USERPROFGNAME="userprofg1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加用户模板组（ADD-USRPROFGROUP）_09897220.md`
