---
id: UDG@20.15.2@MMLCommand@SET CHRFILESAVETIME
type: MMLCommand
name: SET CHRFILESAVETIME（设置文件存留期）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: CHRFILESAVETIME
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- Chr管理
- Chr文件管理
status: active
---

# SET CHRFILESAVETIME（设置文件存留期）

## 功能

该命令用于设置文件存留期。

> **说明**
> - 该命令执行后立即生效。
>
> - 该命令最大实例数为1。
>
> - 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：
>
> | STATUS | MAXKEEPDAYS |
> | --- | --- |
> | ENABLE | 180 |

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| STATUS | 是否开启存留期功能 | 可选必选说明：必选参数<br>参数含义：该参数用于描述存留期设置是否生效。<br>数据来源：本端规划<br>取值范围：<br>- ENABLE（启用存留期控制）<br>- DISABLE（关闭存留期控制）<br>默认值：无。<br>配置原则：无 |
| MAXKEEPDAYS | 文件最大保留天数 | 可选必选说明：该参数在"STATUS"配置为"ENABLE"时为条件必选参数。<br>参数含义：该参数用于描述文件最大存留期限。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~4294967295。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CHRFILESAVETIME查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/CHRFILESAVETIME]] · 文件存留期设置（CHRFILESAVETIME）

## 使用实例

- 当用户需要给chr文件加一个存留期的时候，需要调用该命令，将STATUS参数设置成ENABLE，在MAXKEEPDAYS的参数上填写需要存留的天数，执行该命令。
  ```
  SET CHRFILESAVETIME: STATUS=ENABLE, MAXKEEPDAYS=100;
  ```
- 当用户需要取消chr文件存留期时，用户需要调用该命令，将STATUS参数设置成DISABLE。
  ```
  SET CHRFILESAVETIME: STATUS=DISABLE;
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置文件存留期（SET-CHRFILESAVETIME）_14567105.md`
