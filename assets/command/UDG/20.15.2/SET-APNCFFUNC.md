---
id: UDG@20.15.2@MMLCommand@SET APNCFFUNC
type: MMLCommand
name: SET APNCFFUNC（设置APN内容过滤开关）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: APNCFFUNC
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 内容过滤
- APN内容过滤开关配置
status: active
---

# SET APNCFFUNC（设置APN内容过滤开关）

## 功能

**适用NF：PGW-U、UPF**

该命令用来配置指定APN是否启用内容过滤功能。

## 注意事项

- 该命令执行后只对之后发生承载更新的用户或者新激活用户生效。
- 系统最多支持配置10000个APN内容过滤开关。
- 该命令会导致用户匹配数发生变化，可能导致性能下降。执行命令前请评估对性能的影响，如果无法评估请联系华为技术支持。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APNNAME | APN名称 | 可选必选说明：必选参数<br>参数含义：该参数用于设置APN名称。<br>数据来源：本端规划<br>取值范围：只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”特殊字符，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD APN命令配置生成。 |
| CFSWITCHVALUE | 内容过滤功能开关 | 可选必选说明：必选参数<br>参数含义：该参数用于设置内容过滤功能开关。<br>数据来源：全网规划<br>取值范围：<br>- DISABLE：不使能APN的内容过滤功能。<br>- ENABLE：使能APN的内容过滤功能。<br>- INHERIT：继承SET GLBCFFUNC的全局配置。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/APNCFFUNC]] · APN内容过滤开关（APNCFFUNC）

## 关联任务

- [[UDG@20.15.2@Task@0-00251]]

## 使用实例

配置huawei.com这个APN开启内容过滤：

```
SET APNCFFUNC: APNNAME="huawei.com", CFSWITCHVALUE=ENABLE;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-APNCFFUNC.md`
