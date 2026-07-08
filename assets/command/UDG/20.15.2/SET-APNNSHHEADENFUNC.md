---
id: UDG@20.15.2@MMLCommand@SET APNNSHHEADENFUNC
type: MMLCommand
name: SET APNNSHHEADENFUNC（设置NSH头增强功能开关）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: APNNSHHEADENFUNC
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 对新流生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 头增强控制
- NSH头增强
- APN开关
status: active
---

# SET APNNSHHEADENFUNC（设置NSH头增强功能开关）

## 功能

**适用NF：PGW-U、UPF**

该命令用于设置NSH头增强功能开关。

## 注意事项

- 该命令执行后，开关值修改为关，对新数据流生效；开关值修改为开，对用户激活或更新后的新数据流生效。
- 系统最多支持配置10000条。
- 初始值均为DISABLE。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD APN命令配置生成。 |
| SWITCH | 功能开关 | 可选必选说明：必选参数<br>参数含义：该参数用于配置指定APN的NSH头增强功能开关。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能（关闭）。<br>- ENABLE：使能（开启）。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/APNNSHHEADENFUNC]] · NSH头增强功能开关（APNNSHHEADENFUNC）

## 使用实例

为了开启APN NSH头增强功能，设置APN为apn的NSH头增强功能开关为ENABLE：

```
SET APNNSHHEADENFUNC: APN="apn", SWITCH=ENABLE;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置NSH头增强功能开关（SET-APNNSHHEADENFUNC）_19641388.md`
