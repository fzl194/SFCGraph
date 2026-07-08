---
id: UDG@20.15.2@MMLCommand@LST APNDROPFINALPKT
type: MMLCommand
name: LST APNDROPFINALPKT（显示指定APN配额耗尽末包动作）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: APNDROPFINALPKT
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 计费控制
- 指定APN配额耗尽末包动作
status: active
---

# LST APNDROPFINALPKT（显示指定APN配额耗尽末包动作）

## 功能

**适用NF：PGW-U、UPF**

本命令用于查询指定APN，当配额耗尽时，UPF是否阻塞最后一个超出配额范围的数据报文。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN | 可选必选说明：可选参数<br>参数含义：该参数用于指定APN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”特殊字符，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [指定APN配额耗尽末包动作（APNDROPFINALPKT）](configobject/UDG/20.15.2/APNDROPFINALPKT.md)

## 使用实例

查询指定APN，UPF是否阻塞最后一个超出配额范围的数据报文：

```
LST APNDROPFINALPKT: APN="net";
```

```

RETCODE = 0  操作成功

显示配额耗尽时APN粒度末包动作
-------------------------
开关 =  继承
APN  =  net
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示指定APN配额耗尽末包动作（LST-APNDROPFINALPKT）_93973679.md`
