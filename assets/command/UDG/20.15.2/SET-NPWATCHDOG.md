---
id: UDG@20.15.2@MMLCommand@SET NPWATCHDOG
type: MMLCommand
name: SET NPWATCHDOG（设置喂狗功能配置）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: NPWATCHDOG
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- FEMF
status: active
---

# SET NPWATCHDOG（设置喂狗功能配置）

## 功能

![](设置喂狗功能配置（SET NPWATCHDOG）_18818232.assets/notice_3.0-zh-cn.png)

如果修改喂狗检测周期，周期值过大或者过小，可能影响系统的可靠性。

该命令用于设置喂狗相关配置：包括喂狗检测周期，喂狗超时时长。

> **说明**
> - 该命令执行后立即生效。
>
> - 该命令仅适用于NP卡加速模式场景。
>
> - 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：
>
> | INTERVAL | TIMEOUT |
> | --- | --- |
> | 500 | 24 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INTERVAL | 喂狗检测周期 | 可选必选说明：必选参数<br>参数含义：该参数用于表示喂狗检测周期。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是400~60000，单位是毫秒。<br>默认值：无。<br>配置原则：<br>有效取值为100毫秒的倍数。 |
| TIMEOUT | 喂狗超时时长 | 可选必选说明：必选参数<br>参数含义：该参数用于表示喂狗检测周期的倍数，当检测时间超过喂狗检测周期乘以喂狗超时时长时即认为喂狗超时。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是3~100。<br>默认值：无。<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/NPWATCHDOG]] · 喂狗功能相关配置（NPWATCHDOG）

## 使用实例

设置喂狗检测周期为500，喂狗超时时长为24：

```
SET NPWATCHDOG: INTERVAL=500, TIMEOUT=24;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-NPWATCHDOG.md`
