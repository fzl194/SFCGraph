---
id: UNC@20.15.2@MMLCommand@RMV PERFREGAPN
type: MMLCommand
name: RMV PERFREGAPN（删除区域和APN性能统计对象）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: PERFREGAPN
command_category: 配置类
applicable_nf:
- SGW-C
- PGW-C
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 性能统计管理
- SMF性能对象管理
status: active
---

# RMV PERFREGAPN（删除区域和APN性能统计对象）

## 功能

**适用NF：SGW-C、PGW-C**

该命令用来删除指定的区域和APN的性能统计对象。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN | 可选必选说明：必选参数<br>参数含义：该参数用于指定与区域绑定的APN。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数使用ADD APN命令配置生成。 |
| REGNAME | 区域名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定与APN绑定的区域名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数使用ADD PERFREGION命令配置生成。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PERFREGAPN]] · 区域和APN性能统计对象（PERFREGAPN）

## 使用实例

当运营商需要删除指定区域和APN的性能统计对象，执行如下命令：

```
RMV PERFREGAPN: APN="test", REGNAME="beijing";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-PERFREGAPN.md`
