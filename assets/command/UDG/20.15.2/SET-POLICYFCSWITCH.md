---
id: UDG@20.15.2@MMLCommand@SET POLICYFCSWITCH
type: MMLCommand
name: SET POLICYFCSWITCH（设置策略流控开关）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: POLICYFCSWITCH
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 服务通信管理
- 策略流控管理
status: active
---

# SET POLICYFCSWITCH（设置策略流控开关）

## 功能

该命令用于设置策略流控开关。

> **说明**
> - 该命令执行后立即生效。
>
> - 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：
>
> | FCSWITCH |
> | --- |
> | ON |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FCSWITCH | 策略流控开关 | 可选必选说明：必选参数<br>参数含义：该参数用于显示策略流控开关状态。<br>数据来源：本端规划<br>取值范围：<br>- ON（策略流控开关打开）<br>- OFF（策略流控开关关闭）<br>默认值：无。<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/POLICYFCSWITCH]] · 策略流控开关状态（POLICYFCSWITCH）

## 使用实例

设置策略流控开关为开。

```
%%SET POLICYFCSWITCH: FCSWITCH=ON;%%
RETCODE = 0  操作成功

---    结束
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-POLICYFCSWITCH.md`
