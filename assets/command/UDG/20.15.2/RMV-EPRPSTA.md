---
id: UDG@20.15.2@MMLCommand@RMV EPRPSTA
type: MMLCommand
name: RMV EPRPSTA（删除EPRPSTA对象）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: EPRPSTA
command_category: 配置类
applicable_nf:
- SGW-U
- PGW-U
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务运维
- 业务性能统计管理
- EPRPSTA性能统计对象
status: active
---

# RMV EPRPSTA（删除EPRPSTA对象）

## 功能

**适用NF：SGW-U、PGW-U**

该命令用于删除EpRpSta对象。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| EPRPSTANAME | 对象名称 | 可选必选说明：必选参数<br>参数含义：对象名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@EPRPSTA]] · EPRPSTA对象（EPRPSTA）

## 使用实例

删除名为huawei的EpRpSta对象：

```
RMV EPRPSTA: EPRPSTANAME="huawei";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-EPRPSTA.md`
