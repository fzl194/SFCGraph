---
id: UNC@20.15.2@MMLCommand@SET APNIMSATTR
type: MMLCommand
name: SET APNIMSATTR（设置APN的IMS属性）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: APNIMSATTR
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- IMS管理
- IMS业务功能
- 基于APN的IMS属性
status: active
---

# SET APNIMSATTR（设置APN的IMS属性）

## 功能

**适用NF：PGW-C、SMF、GGSN**

该命令用于建立IMS承载时，设置APN绑定的IMS相关属性。

## 注意事项

- 该命令执行后立即生效。

- 在每次执行ADD APN命令时会自动为本命令增加一条记录，记录中参数的初始设置值如下：IMSSWITCH：INHERIT，SIGNALRADIOPRE：DISABLE。
- 当前版本不支持此命令的SIGNALRADIOPRE参数。
- 当IMSSWITCH的值为INHERIT时，GLOBALIMS必须要配置缺省P-CSCF组。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN实例名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无。<br>配置原则：<br>该参数使用ADD APN命令配置生成。 |
| IMSSWITCH | IMS开关 | 可选必选说明：可选参数<br>参数含义：该参数用于配置IMS互通相关的设置。<br>数据来源：本端规划<br>取值范围：<br>- “DISABLE（不使能）”：关闭IMS。<br>- “ENABLE（使能）”：打开IMS。<br>- “INHERIT（继承）”：设置IMS功能，设置后继承GLOBALIMS的IMSSWITCH参数配置。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST APNIMSATTR查询当前参数配置值。<br>配置原则：无 |
| SIGNALRADIOPRE | 信令空口增强开关 | 可选必选说明：该参数在"IMSSWITCH"配置为"ENABLE"时为条件可选参数。<br>参数含义：该参数用于设置IMS信令空口增强开关。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE（不使能）<br>- ENABLE（使能）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST APNIMSATTR查询当前参数配置值。<br>配置原则：<br>该参数已弃用。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/APNIMSATTR]] · APN的IMS属性（APNIMSATTR）

## 使用实例

需要设置“APN名称”为“HUAWEI.COM”的IMS属性，打开IMS功能和IMS信令空口增强开关。

```
SET APNIMSATTR:APN="huawei.com",IMSSWITCH=ENABLE,SIGNALRADIOPRE=ENABLE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-APNIMSATTR.md`
