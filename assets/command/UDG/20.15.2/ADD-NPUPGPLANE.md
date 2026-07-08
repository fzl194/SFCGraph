---
id: UDG@20.15.2@MMLCommand@ADD NPUPGPLANE
type: MMLCommand
name: ADD NPUPGPLANE（增加NP升级平面）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: NPUPGPLANE
command_category: 配置类
effect_mode: 立即生效
is_dangerous: true
category_path:
- 平台服务管理
- VNRS功能管理
- 系统管理
- NP升级管理
- NP平面管理
status: active
---

# ADD NPUPGPLANE（增加NP升级平面）

## 功能

![](增加NP升级平面（ADD NPUPGPLANE）_92175826.assets/notice_3.0-zh-cn.png)

该命令是高危命令，操作不当可能会影响灰度升级。

该命令用来增加NP升级平面。

如果灰度升级前平面不是按照奇数和偶数槽位进行划分，则需要执行此命令，划分原则请从网设文档中获取。

## 注意事项

- 该命令执行后立即生效。
- 该命令仅适用于NP卡省交换组网模式。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUID | RU编号 | 可选必选说明：必选参数。<br>参数含义：该参数用于指定RU编号。<br>数据来源：本端规划。<br>取值范围：整数类型，取值范围为0～4294967294。<br>默认值：无。<br>配置原则：使用<br>**[DSP RU](../../../../单体服务公共功能管理/系统管理/资源管理/RU管理/显示资源单元信息（DSP RU）_59103857.md)**<br>命令查询RU类型不是VNRS_OM_RU以及VNRS_IPCTRL_RU的RU编号。 |
| PLANEID | 平面编号 | 可选必选说明：必选参数。<br>参数含义：该参数用于设置升级平面。<br>数据来源：本端规划。<br>取值范围：<br>- “plane_1”：升级平面一。<br>- “plane_2”：升级平面二。<br>默认值：无。<br>配置原则：无。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/NPUPGPLANE]] · NP升级平面（NPUPGPLANE）

## 使用实例

增加RUID为66到升级平面plane_1：

```
ADD NPUPGPLANE: RUID=66, PLANEID=plane_1;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/ADD-NPUPGPLANE.md`
