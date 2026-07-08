---
id: UDG@20.15.2@MMLCommand@LST PRINETPOLICY
type: MMLCommand
name: LST PRINETPOLICY（显示专网控制策略）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: PRINETPOLICY
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 专网策略配置
- 专网控制策略
status: active
---

# LST PRINETPOLICY（显示专网控制策略）

## 功能

**适用NF：PGW-U、UPF**

该命令用来查看指定APN下的专网控制策略。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定APN实例名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/PRINETPOLICY]] · 专网控制策略（PRINETPOLICY）

## 使用实例

显示已配置的专网控制策略：

```
LST PRINETPOLICY:;
```

```

RETCODE = 0 操作成功。

专网控制策略信息
------------------------------------------
APN名称 数据网络接入标识 单网通功能开关

test 123456 DISABLE
test 123457 DISABLE
(结果个数  = 2)

--- END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-PRINETPOLICY.md`
