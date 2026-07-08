---
id: UNC@20.15.2@MMLCommand@SET KUBEPROBE
type: MMLCommand
name: SET KUBEPROBE（设置是否放通就绪状态检测）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: KUBEPROBE
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 可靠性管理
- 微服务可靠性管理
status: active
---

# SET KUBEPROBE（设置是否放通就绪状态检测）

## 功能

该命令用于设置是否放通就绪状态检测。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| READINESS | READINESSFE | READINESSRU |
| --- | --- | --- |
| DISABLE | DISABLE | ENABLE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| READINESS | 是否检测就绪状态 | 可选必选说明：可选参数<br>参数含义：该参数用于表示是否放通就绪状态检测。<br>数据来源：本端规划<br>取值范围：<br>- “ENABLE（开启）”：检测真实就绪状态<br>- “DISABLE（关闭）”：放通就绪状态检测<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST KUBEPROBE查询当前参数配置值。<br>配置原则：无 |
| READINESSFE | 特定网元下是否检测就绪状态 | 可选必选说明：可选参数<br>参数含义：该参数用于表示特定网元下是否放通就绪状态检测。<br>数据来源：本端规划<br>取值范围：<br>- “ENABLE（开启）”：检测真实就绪状态<br>- “DISABLE（关闭）”：放通就绪状态检测<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST KUBEPROBE查询当前参数配置值。<br>配置原则：无 |
| READINESSRU | PSP平台大颗粒服务是否检测就绪状态 | 可选必选说明：可选参数<br>参数含义：该参数用于表示PSP平台大颗粒服务是否放通就绪状态检测。<br>数据来源：本端规划<br>取值范围：<br>- “ENABLE（开启）”：放通就绪状态检测<br>- “DISABLE（关闭）”：检测真实就绪状态<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST KUBEPROBE查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/KUBEPROBE]] · 是否放通就绪状态检测（KUBEPROBE）

## 使用实例

使能就绪状态检测并使能特定网元下就绪状态检测。

```
SET KUBEPROBE:READINESS=ENABLE,READINESSFE=ENABLE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-KUBEPROBE.md`
