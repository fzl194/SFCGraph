---
id: UNC@20.15.2@MMLCommand@MOD APNCHRFUNC
type: MMLCommand
name: MOD APNCHRFUNC（修改APN CHR功能配置）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: APNCHRFUNC
command_category: 配置类
applicable_nf:
- GGSN
- SGW-C
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- CHR管理
- APN CHR功能配置
status: active
---

# MOD APNCHRFUNC（修改APN CHR功能配置）

## 功能

**适用NF：GGSN、SGW-C、PGW-C、SMF**

该命令用于修改基于APN的CHR功能配置。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN实例名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数必须已经通过命令ADD APN配置。 |
| CHRREPORTSW | CHR上报开关 | 可选必选说明：可选参数<br>参数含义：该参数用于基于APN控制开启和关闭CHR上报功能。<br>数据来源：本端规划<br>取值范围：<br>- “INHERIT（继承全局）”：表示使用SET GLBCHRFUNC中配置的开关。<br>- “ENABLE（使能）”：表示基于APN控制开启CHR上报功能。<br>- “DISABLE（不使能）”：表示基于APN控制关闭CHR上报功能。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@APNCHRFUNC]] · APN CHR功能配置（APNCHRFUNC）

## 使用实例

打开“APN”为“HUAWEI.COM”的CHR上报开关：

```
MOD APNCHRFUNC: APN="HUAWEI.COM", CHRREPORTSW=ENABLE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-APNCHRFUNC.md`
