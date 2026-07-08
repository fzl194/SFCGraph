---
id: UDG@20.15.2@MMLCommand@RMV APNOLQCBLACKLIST
type: MMLCommand
name: RMV APNOLQCBLACKLIST（删除过载限速APN黑名单）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: APNOLQCBLACKLIST
command_category: 配置类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 会话管理
- 过载限速
- 过载限速控制APN黑名单
status: active
---

# RMV APNOLQCBLACKLIST（删除过载限速APN黑名单）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于删除过载限速APN黑名单。

## 注意事项

该命令执行后只对之后发生承载更新的用户或者新激活用户生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN实例名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD APN命令配置生成。 |

## 操作的配置对象

- [过载限速APN黑名单（APNOLQCBLACKLIST）](configobject/UDG/20.15.2/APNOLQCBLACKLIST.md)

## 使用实例

从过载限速APN黑名单中删除名为“testapn”的APN：

```
RMV APNOLQCBLACKLIST: APN="testapn";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除过载限速APN黑名单（RMV-APNOLQCBLACKLIST）_96809506.md`
