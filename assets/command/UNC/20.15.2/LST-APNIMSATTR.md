---
id: UNC@20.15.2@MMLCommand@LST APNIMSATTR
type: MMLCommand
name: LST APNIMSATTR（查询APN的IMS属性）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: APNIMSATTR
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
- IMS管理
- IMS业务功能
- 基于APN的IMS属性
status: active
---

# LST APNIMSATTR（查询APN的IMS属性）

## 功能

**适用NF：PGW-C、SMF、GGSN**

该命令用于查询APN的IMS属性信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定APN实例名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数使用ADD APN命令配置生成。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@APNIMSATTR]] · APN的IMS属性（APNIMSATTR）

## 使用实例

查询“APN名称”为“HUAWEI.COM”的IMS属性信息。

```
%%LST APNIMSATTR: APN="huawei.com";%%
RETCODE = 0  操作成功

结果如下
--------
         APN名称  =  huawei.com
         IMS开关  =  使能
信令空口增强开关  =  使能
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-APNIMSATTR.md`
