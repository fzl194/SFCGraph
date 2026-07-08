---
id: UNC@20.15.2@MMLCommand@LST AUTHNAMEPWDCTRL
type: MMLCommand
name: LST AUTHNAMEPWDCTRL（查询对鉴权信元用户名和密码的控制）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: AUTHNAMEPWDCTRL
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- APN管理
- APN鉴权属性
status: active
---

# LST AUTHNAMEPWDCTRL（查询对鉴权信元用户名和密码的控制）

## 功能

**适用NF：PGW-C、SMF、GGSN**

该命令用于查询对鉴权信元用户名和密码的控制。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| EFFECTIVESCOPE | 生效范围 | 可选必选说明：可选参数<br>参数含义：该参数用于指定单APN生效或全局生效。<br>数据来源：本端规划<br>取值范围：<br>- “GLOBAL（全局生效）”：全局生效<br>- “SINGLE_APN（单个APN生效）”：单个APN生效<br>默认值：无<br>配置原则：无 |
| APN | APN名称 | 可选必选说明：该参数在"EFFECTIVESCOPE"配置为"SINGLE_APN"时为条件必选参数。<br>参数含义：该参数用于指定APN实例名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@AUTHNAMEPWDCTRL]] · 对鉴权信元用户名和密码的控制（AUTHNAMEPWDCTRL）

## 使用实例

如果需要读取所有鉴权信元内用户名和密码的填写方式，可以使用该实例：

```
LST AUTHNAMEPWDCTRL:;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-AUTHNAMEPWDCTRL.md`
