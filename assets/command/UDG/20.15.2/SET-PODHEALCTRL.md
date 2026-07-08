---
id: UDG@20.15.2@MMLCommand@SET PODHEALCTRL
type: MMLCommand
name: SET PODHEALCTRL（设置自愈功能开关状态）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: PODHEALCTRL
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 可靠性管理
- 微服务可靠性管理
status: active
---

# SET PODHEALCTRL（设置自愈功能开关状态）

## 功能

该命令用于设置是否启动pod自愈，若开关打开，则按照 [**SET PODHEALPLY**](设置Pod自愈策略（SET PODHEALPLY）_09587937.md) 命令配置的pod自愈策略进行自愈；若开关关闭，则不进行pod自愈。

> **说明**
> - 该命令执行后立即生效。
>
> - 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：
>
> | SWITCH |
> | --- |
> | ENABLE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SWITCH | 自愈开关 | 可选必选说明：必选参数<br>参数含义：该参数用于表示自愈开关。<br>数据来源：本端规划<br>取值范围：<br>- “ENABLE（打开）”：自愈使能<br>- “DISABLE（不使能）”：自愈不使能<br>默认值：无。<br>配置原则：<br>升级时建议关闭，升级结束运行正常后建议开启。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/PODHEALCTRL]] · 自愈功能配置信息（PODHEALCTRL）

## 使用实例

关闭自愈功能开关。

```
SET PODHEALCTRL: SWITCH=DISABLE;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置自愈功能开关状态（SET-PODHEALCTRL）_09587383.md`
