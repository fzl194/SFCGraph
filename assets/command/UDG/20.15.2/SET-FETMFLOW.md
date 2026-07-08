---
id: UDG@20.15.2@MMLCommand@SET FETMFLOW
type: MMLCommand
name: SET FETMFLOW（设置FETM流控配置）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: FETMFLOW
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 系统管理
- FE表管理
- FETM流控
status: active
---

# SET FETMFLOW（设置FETM流控配置）

## 功能

![](设置FETM流控配置（SET FETMFLOW）_58971168.assets/notice_3.0-zh-cn.png)

流控阈值配置不合理可能会导致CPU占有率升高。

该命令用来设置FETM流控配置。

## 注意事项

- 该命令执行后立即生效。
- 该命令仅适用于NP卡加速CSLB卸载模式场景。
- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：
  | SWITCH | THRESHOLD |
  | --- | --- |
  | 启用 | 70 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SWITCH | 流控开关 | 可选必选说明：必选参数。<br>参数含义：该参数用于设置FETM流控开关。<br>数据来源：本端规划。<br>取值范围：枚举类型。<br>- OFF(关闭)：表示流控关闭。<br>- ON(启用)：表示流控开启。<br>默认值：无。<br>配置原则：建议值为"ON(启用)"。 |
| THRESHOLD | 流控阈值 | 可选必选说明：条件可选参数。<br>前提条件：该参数在"SWITCH"配置为"ON"时为可选参数。<br>参数含义：该参数用于设置FETM流控阈值。<br>数据来源：本端规划。<br>取值范围：整数类型，取值范围为30～100，其中1个单位代表1000次下表操作。<br>默认值：无。执行命令并不输入该参数时，系统默认为参数的初始设置值。<br>配置原则：无。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@FETMFLOW]] · FETM流控配置（FETMFLOW）

## 使用实例

设置FETM流控开关为启用，流控阈值为80：

```
SET FETMFLOW: SWITCH=ON, THRESHOLD=80;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-FETMFLOW.md`
