---
id: UDG@20.15.2@MMLCommand@SET FCSWITCH
type: MMLCommand
name: SET FCSWITCH（设置流控开关）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: FCSWITCH
command_category: 配置类
effect_mode: ''
is_dangerous: true
category_path:
- 平台服务管理
- 服务通信管理
- 流控管理
status: active
---

# SET FCSWITCH（设置流控开关）

## 功能

![](设置流控开关（SET FCSWITCH）_09587940.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，关闭流控功能后在接入业务量大的情况下可能导致系统过载和复位，请谨慎使用。如需使用本命令请联系华为技术支持协助操作。

该命令用于设置整系统的流控功能禁用/启用状态。在通过 [**ADD FCPARAM**](增加流控参数（ADD FCPARAM）_09587901.md) 命令完成流控参数配置后，可以通过本命令来开启流控功能。

> **说明**
> - 该命令执行后立即生效。
>
> - 此命令需要华为技术支持人员指导下才能执行，请慎重使用。
>
> - 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：
>
> | SWITCH |
> | --- |
> | ENABLE |

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SWITCH | 开关 | 可选必选说明：必选参数<br>参数含义：该参数用于配置流控功能的禁用/启用状态。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE（禁用）<br>- ENABLE（启用）<br>默认值：无。<br>配置原则：<br>系统初始值为“ENABLE(启用)”。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/FCSWITCH]] · 流控开关（FCSWITCH）

## 使用实例

启用流控功能。

```
SET FCSWITCH: SWITCH=ENABLE;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置流控开关（SET-FCSWITCH）_09587940.md`
