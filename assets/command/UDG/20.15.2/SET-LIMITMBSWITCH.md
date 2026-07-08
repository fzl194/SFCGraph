---
id: UDG@20.15.2@MMLCommand@SET LIMITMBSWITCH
type: MMLCommand
name: SET LIMITMBSWITCH（设置有界邮箱开关）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: LIMITMBSWITCH
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 服务通信管理
- 邮箱配置
status: active
---

# SET LIMITMBSWITCH（设置有界邮箱开关）

## 功能

该命令用于设置SDRC有界邮箱开关，默认开启，表示SDRC将使用有界邮箱功能。

> **说明**
> - 该命令执行后需要重新启动系统才能生效。
>
> - 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：
>
> | SWITCH |
> | --- |
> | ON |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SWITCH | 有界邮箱开关 | 可选必选说明：必选参数<br>参数含义：有界邮箱开关，ON表示sdrc将使用有界邮箱功能，OFF表示sdrc使用无界邮箱。<br>数据来源：本端规划<br>取值范围：<br>- ON（开启）<br>- OFF（关闭）<br>默认值：无。<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/LIMITMBSWITCH]] · 有界邮箱开关配置状态（LIMITMBSWITCH）

## 使用实例

开启有界邮箱功能

```
*MEID:0 MENAME:*/        2021-01-19 09:56:57+8:00
O&M    #55
%%SET LIMITMBSWITCH: SWITCH=ON;%%
RETCODE = 0  操作成功

---    结束
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置有界邮箱开关（SET-LIMITMBSWITCH）_24062794.md`
