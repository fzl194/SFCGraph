---
id: UDG@20.15.2@MMLCommand@SET NPFABRICOAM
type: MMLCommand
name: SET NPFABRICOAM（设置全局OAM相关配置）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: NPFABRICOAM
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- FEMF
status: active
---

# SET NPFABRICOAM（设置全局OAM相关配置）

## 功能

![](设置全局OAM相关配置（SET NPFABRICOAM）_94730515.assets/notice_3.0-zh-cn.png)

如果修改Fabric-OAM开关，影响系统可靠性，如果修改检测间隔，间隔过小或者过大，会导致丢包率上升或者检测能力降低。

该命令用来设置全局OAM相关配置：包括OAM使能，OAM报文检测周期，OAM报文超时检测倍数。

> **说明**
> - 该命令执行后立即生效。
>
> - 如果修改Fabric-OAM检测间隔，需要注意：间隔过小，会影响性能，导致丢包率上升；间隔过大，会导致检测能力降低。
> - 该命令仅适用于NP卡加速模式场景。
>
> - 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：
>
> | OAMSWITCH | OAMINTERVAL | OAMMULTIPLIER |
> | --- | --- | --- |
> | Enable | 100 | 30 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| OAMSWITCH | OAM使能 | 可选必选说明：必选参数<br>参数含义：该参数用于表示OAM使能开关。<br>数据来源：本端规划<br>取值范围：<br>- Disable（去使能）<br>- Enable（使能）<br>默认值：无。<br>配置原则：无 |
| OAMINTERVAL | OAM报文发送周期(ms) | 可选必选说明：该参数在"OAMSWITCH"配置为"Enable"时为条件必选参数。<br>参数含义：该参数用于表示OAM报文发送周期，单位为毫秒。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是100~60000，单位是毫秒。有效取值为100毫秒的倍数。<br>默认值：100。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NPFABRICOAM查询当前参数配置值。<br>配置原则：无 |
| OAMMULTIPLIER | OAM报文超时检测倍数 | 可选必选说明：该参数在"OAMSWITCH"配置为"Enable"时为条件必选参数。<br>参数含义：该参数用于表示OAM报文超时检测倍数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是3~50。<br>默认值：30。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NPFABRICOAM查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [全局OAM相关配置（NPFABRICOAM）](configobject/UDG/20.15.2/NPFABRICOAM.md)

## 使用实例

设置OAM开关为使能，OAM报文发送周期为100，OAM报文超时检测倍数为30：

```
SET NPFABRICOAM: OAMSWITCH=Enable, OAMINTERVAL=100, OAMMULTIPLIER=30;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置全局OAM相关配置（SET-NPFABRICOAM）_94730515.md`
