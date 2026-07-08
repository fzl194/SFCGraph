---
id: UDG@20.15.2@MMLCommand@SET FEHEALCTRL
type: MMLCommand
name: SET FEHEALCTRL（设置FE自愈功能配置）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: FEHEALCTRL
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- FEMF
status: active
---

# SET FEHEALCTRL（设置FE自愈功能配置）

## 功能

该命令用来设置FE自愈功能开关：包括Mesh网口故障自愈功能开关和FE服务丢失心跳自愈开关。

> **说明**
> - 该命令执行后立即生效。
>
> - 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：
>
> | MESHFAULTSW | FEFAULTSW |
> | --- | --- |
> | Enable | Enable |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MESHFAULTSW | Mesh网口故障自愈功能开关 | 可选必选说明：可选参数<br>参数含义：Mesh网口故障自愈功能开关。<br>数据来源：本端规划<br>取值范围：<br>- Disable（去使能）<br>- Enable（使能）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST FEHEALCTRL查询当前参数配置值。<br>配置原则：无 |
| FEFAULTSW | FE服务丢失心跳自愈开关 | 可选必选说明：可选参数<br>参数含义：FE服务丢失心跳自愈开关。<br>数据来源：本端规划<br>取值范围：<br>- Disable（去使能）<br>- Enable（使能）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST FEHEALCTRL查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/FEHEALCTRL]] · FE自愈功能配置（FEHEALCTRL）

## 使用实例

设置Mesh网口故障自愈使能，FE服务丢失心跳自愈使能：

```
SET FEHEALCTRL: MESHFAULTSW=Enable, FEFAULTSW=Enable;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置FE自愈功能配置（SET-FEHEALCTRL）_10913261.md`
