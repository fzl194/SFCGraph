---
id: UNC@20.15.2@MMLCommand@RMV PERFEPRPDYN
type: MMLCommand
name: RMV PERFEPRPDYN（删除EpRpDyn性能统计对象）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: PERFEPRPDYN
command_category: 配置类
applicable_nf:
- SGW-C
- PGW-C
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 性能统计管理
- SMF性能对象管理
status: active
---

# RMV PERFEPRPDYN（删除EpRpDyn性能统计对象）

## 功能

**适用NF：SGW-C、PGW-C、GGSN**

该命令用于删除EpRpDyn性能统计对象。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| EPRPDYNNAME | 对象名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定EpRpDyn性能统计对象名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~31。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PERFEPRPDYN]] · EpRpDyn性能统计对象（PERFEPRPDYN）

## 使用实例

当删除对象名为pgw1的EpRpDyn对象时，执行如下命令：

```
RMV PERFEPRPDYN: EPRPDYNNAME="pgw1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-PERFEPRPDYN.md`
