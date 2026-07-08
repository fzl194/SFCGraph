---
id: UNC@20.15.2@MMLCommand@SET APNNONIPFUNC
type: MMLCommand
name: SET APNNONIPFUNC（设置APN Non-IP功能配置）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: APNNONIPFUNC
command_category: 配置类
applicable_nf:
- SGW-C
- PGW-C
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- M2M
- APN的Non-IP配置
status: active
---

# SET APNNONIPFUNC（设置APN Non-IP功能配置）

## 功能

**适用NF：SGW-C、PGW-C**

此命令用于开启或关闭指定APN的网关Non-IP功能。

## 注意事项

- 该命令执行后立即生效。

- 在每次执行ADD APN命令时会自动为本命令增加一条记录，记录中参数的初始设置值如下：NONIPSWITCH：INHERIT。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN实例名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无。<br>配置原则：<br>该参数使用ADD APN命令配置生成。 |
| NONIPSWITCH | APN Non-IP功能开关 | 可选必选说明：可选参数<br>参数含义：该参数用于基于APN控制开启和关闭Non-IP功能。<br>数据来源：本端规划<br>取值范围：<br>- INHERIT（继承全局）<br>- DISABLE（不使能）<br>- ENABLE（使能）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST APNNONIPFUNC查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/APNNONIPFUNC]] · APN Non-IP功能配置（APNNONIPFUNC）

## 使用实例

使能apn isp的Non-IP功能：

```
SET APNNONIPFUNC:APN="isp",NONIPSWITCH=ENABLE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-APNNONIPFUNC.md`
