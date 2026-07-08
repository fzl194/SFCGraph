---
id: UDG@20.15.2@MMLCommand@SET NPLINKCHECK
type: MMLCommand
name: SET NPLINKCHECK（设置NP交换网口检测配置）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: NPLINKCHECK
command_category: 配置类
effect_mode: ''
is_dangerous: true
category_path:
- 平台服务管理
- VNRS功能管理
- FEMF
status: active
---

# SET NPLINKCHECK（设置NP交换网口检测配置）

## 功能

![](设置NP交换网口检测配置（SET NPLINKCHECK）_94730516.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，请合理设置相关参数，关闭网口检测开关会影响系统可靠性，检测周期太短会导致误检，检测周期太长会导致端口故障无法及时隔离，请谨慎使用并联系华为技术支持协助操作。

该命令用来设置NP交换网口检测配置：包括端口检测使能、端口检测周期、端口检测超时检测倍数。

> **说明**
> - 该命令执行后立即生效。
>
> - 该命令仅适用于NP卡加速模式场景。
>
> - 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：
>
> | SWITCH | INTERVAL | MULTIPLIER |
> | --- | --- | --- |
> | Enable | 100 | 15 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SWITCH | NP交换网口检测功能 | 可选必选说明：必选参数<br>参数含义：NP交换网口检测功能。<br>数据来源：本端规划<br>取值范围：<br>- Disable（去使能）<br>- Enable（使能）<br>默认值：无。<br>配置原则：无 |
| INTERVAL | NP交换网口检测周期 | 可选必选说明：该参数在"SWITCH"配置为"Enable"时为条件必选参数。<br>参数含义：NP交换网口检测周期。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是100~60000，单位是毫秒。取值范围为100～60000，且有效取值为100毫秒的倍数。<br>默认值：100。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NPLINKCHECK查询当前参数配置值。<br>配置原则：无 |
| MULTIPLIER | NP交换网口检测超时检测倍数 | 可选必选说明：该参数在"SWITCH"配置为"Enable"时为条件必选参数。<br>参数含义：NP交换网口检测超时检测倍数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是10~100。<br>默认值：15。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NPLINKCHECK查询当前参数配置值。<br>配置原则：<br>NP交换网口检测周期太短，容易造成误检，导致NP和NP交换网口的端口错误被隔离。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@NPLINKCHECK]] · 全局NP交换网口检测配置（NPLINKCHECK）

## 使用实例

设置NP交换网口检测使能，检测周期为100，超时检测倍数为15：

```
SET NPLINKCHECK: SWITCH=Enable, INTERVAL=100, MULTIPLIER=15;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-NPLINKCHECK.md`
