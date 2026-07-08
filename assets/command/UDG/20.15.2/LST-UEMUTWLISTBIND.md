---
id: UDG@20.15.2@MMLCommand@LST UEMUTWLISTBIND
type: MMLCommand
name: LST UEMUTWLISTBIND（查询APN绑定PA口UE互访白名单）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: UEMUTWLISTBIND
command_category: 查询类
applicable_nf:
- UPF
- PGW-U
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务安全防护
- 用户攻击防护
- 用户互访控制
- UE互访白名单绑定APN
status: active
---

# LST UEMUTWLISTBIND（查询APN绑定PA口UE互访白名单）

## 功能

**适用NF：UPF、PGW-U**

该命令用于查询APN下绑定的PA口UE互访白名单。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APNNAME | APN名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定APN实例名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”特殊字符，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/UEMUTWLISTBIND]] · APN绑定PA口UE互访白名单（UEMUTWLISTBIND）

## 使用实例

查询APN名称为testapn的APN下绑定的PA口UE互访白名单：

```
LST UEMUTWLISTBIND:APNNAME="testapn";
```

```

```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-UEMUTWLISTBIND.md`
