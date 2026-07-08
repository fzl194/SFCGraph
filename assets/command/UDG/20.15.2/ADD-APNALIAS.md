---
id: UDG@20.15.2@MMLCommand@ADD APNALIAS
type: MMLCommand
name: ADD APNALIAS（添加ApnAlias配置）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: APNALIAS
command_category: 配置类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: 对新用户生效
is_dangerous: false
max_records: 3000
category_path:
- 用户面服务管理
- DN管理
- APN管理
- 别名APN
status: active
---

# ADD APNALIAS（添加ApnAlias配置）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于添加ApnAlias配置。为了兼容多个APN使用完全相同资源的情况，使用该命令配置APN别名，把它映射到真实APN上，这样多个别名APN就能共用一个真实APN的系统资源。别名APN主要适用于以下两种场景：

1、运营商合并和重组时，为了兼容现网中使用相同资源的多个APN，可将某APN的业务映射到另一APN上。

2、网络改建时新规划了APN，为了不影响原规划APN的使用，只需将原规划的APN映射到新规划APN上即可。

## 注意事项

- 该命令执行后只对新激活用户生效。
- 该命令最大记录数为3000。
- 一个APN下最多可以配置500个APN别名。
- 一个APN别名只能对应一个APN，不能在不同的APN下配置相同的APN别名。
- 要配置的别名已经配置或该别名是真实APN时，不允许配置，配置APN别名时，须关联已配置的APN名称。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ALIASNAME | APN别名的配置 | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN别名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格及特殊字符“_”、“#”、“$”和“&”，不区分大小写。<br>默认值：无<br>配置原则：无 |
| APN | APN名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格及特殊字符“_”、“#”、“$”和“&”，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [ApnAlias配置（APNALIAS）](configobject/UDG/20.15.2/APNALIAS.md)

## 使用实例

假设运营商希望指定APN“test2”与已配置的真实APN“mtest”使用相同资源时，需要添加ApnAlias配置，使用该命令：

```
ADD APNALIAS: ALIASNAME="test2", APN="mtest";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/添加ApnAlias配置（ADD-APNALIAS）_82837023.md`
