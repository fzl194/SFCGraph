---
id: UDG@20.15.2@MMLCommand@MOD NPUPGPLANE
type: MMLCommand
name: MOD NPUPGPLANE（修改NP升级平面）
nf: UDG
version: 20.15.2
verb: MOD
object_keyword: NPUPGPLANE
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 系统管理
- NP升级管理
- NP平面管理
status: active
---

# MOD NPUPGPLANE（修改NP升级平面）

## 功能

该命令用来修改NP升级平面。

## 注意事项

- 该命令执行后立即生效。
- 该命令仅适用于NP卡省交换组网模式。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUID | RU编号 | 可选必选说明：必选参数。<br>参数含义：RU编号。<br>数据来源：本端规划。<br>取值范围：整数类型，取值范围为0～4294967294。<br>默认值：无。<br>配置原则：使用<br>**[LST NPUPGPLANE](查询NP升级平面（LST NPUPGPLANE）_43297437.md)**<br>命令查询RU编号。 |
| PLANEID | 平面编号 | 可选必选说明：必选参数。<br>参数含义：该参数用于设置升级平面。<br>数据来源：本端规划。<br>取值范围：<br>- “plane_1”：升级平面一。<br>- “plane_2”：升级平面二。<br>默认值：无。<br>配置原则：无。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/NPUPGPLANE]] · NP升级平面（NPUPGPLANE）

## 使用实例

修改RUID为66的升级平面为plane_2：

```
MOD NPUPGPLANE: RUID=66, PLANEID=plane_2;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/MOD-NPUPGPLANE.md`
