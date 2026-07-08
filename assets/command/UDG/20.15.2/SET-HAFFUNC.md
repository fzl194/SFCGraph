---
id: UDG@20.15.2@MMLCommand@SET HAFFUNC
type: MMLCommand
name: SET HAFFUNC（设置HAF服务内部功能的相关参数）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: HAFFUNC
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 可靠性管理
- 微服务可靠性管理
status: active
---

# SET HAFFUNC（设置HAF服务内部功能的相关参数）

## 功能

当前版本配置此命令不生效。

该命令用于设置HAF服务内部功能的相关参数。

> **说明**
> - 该命令执行后立即生效。
>
> - 当前版本参数MCENHANCED的配置不生效。
> - 为避免频繁执行对系统性能产生冲击，该命令在三分钟之内只能执行一次。
>
> - 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：
>
> | DOMAINFAULT | MCENHANCED |
> | --- | --- |
> | ON | ON |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DOMAINFAULT | 域故障开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定域故障功能的开关。<br>数据来源：本端规划<br>取值范围：<br>- “ON（打开）”：域故障功能打开<br>- “OFF（关闭）”：域故障功能关闭<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST HAFFUNC查询当前参数配置值。<br>配置原则：<br>FusionSphere分批升级活动中，如果某批次升级出现调整失败提示时，需要通过该命令配置为OFF。其他场景为ON。升级完成后，如果参数的取值为OFF，需要将其手动设置为ON。 |
| MCENHANCED | 多连接增强开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定是否开启多连接增强功能。<br>数据来源：本端规划<br>取值范围：<br>- “ON（打开）”：多连接增强功能打开<br>- “OFF（关闭）”：多连接增强功能关闭<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST HAFFUNC查询当前参数配置值。<br>配置原则：<br>该参数配置不生效。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/HAFFUNC]] · HAF服务内部功能的参数（HAFFUNC）

## 使用实例

- 打开域故障功能开关。
  ```
  SET HAFFUNC:DOMAINFAULT=ON;
  ```
- 打开多连接增强开关。
  ```
  SET HAFFUNC:MCENHANCED=ON;
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置HAF服务内部功能的相关参数（SET-HAFFUNC）_68321033.md`
