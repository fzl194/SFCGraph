---
id: UDG@20.15.2@MMLCommand@SET PODHEALPLY
type: MMLCommand
name: SET PODHEALPLY（设置Pod自愈策略）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: PODHEALPLY
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 可靠性管理
- 微服务可靠性管理
status: active
---

# SET PODHEALPLY（设置Pod自愈策略）

## 功能

该命令用于设置Pod自愈策略。

> **说明**
> - 该命令执行后立即生效。
>
> - 若HAFG服务发生了主备切换，需要重新计算Pod自愈升级到Node自愈前的Pod自愈次数，当满足参数“自愈次数”的设置值时，才能升级到Node自愈。
>
> - 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：
>
> | STATUS | PREWAITTIME | HEALWAITTIME | HEALNUM |
> | --- | --- | --- | --- |
> | NORMAL | 300 | 210 | 3 |
> | FAULT | 300 | 420 | 3 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| STATUS | Pod状态 | 可选必选说明：必选参数<br>参数含义：该参数用于表示Pod状态信息。<br>数据来源：本端规划<br>取值范围：<br>- “NORMAL（正常）”：状态正常<br>- “FAULT（故障）”：状态故障<br>默认值：无。<br>配置原则：无 |
| PREWAITTIME | 预等待时间(秒) | 可选必选说明：必选参数<br>参数含义：该参数用于表示Pod故障后进行首次自愈前的等待时间。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~4294967295，单位是秒。<br>默认值：无。<br>配置原则：无 |
| HEALWAITTIME | 自愈等待时间(秒) | 可选必选说明：必选参数<br>参数含义：该参数用于表示如果Pod自愈后没有恢复，等待下次Pod自愈的时间。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~4294967295，单位是秒。<br>默认值：无。<br>配置原则：无 |
| HEALNUM | 自愈次数 | 可选必选说明：必选参数<br>参数含义：虚机场景下，该参数用于表示Pod自愈升级到Node自愈前，Pod自愈的最大次数。Pod自愈升级到Node自愈通过<br>[**SET NODEHEALCTRL**](设置Node自愈策略控制参数（SET NODEHEALCTRL）_48332256.md)<br>命令开启或关闭。<br>裸机场景下，该参数表示Pod一轮自愈中的自愈操作次数（一轮自愈中可触发Pod普通重建自愈操作、Pod异地重建自愈操作，交替进行；如果Node状态正常，优先触发“普通重建自愈”操作，再触发“异地重建自愈操作”；如果Node状态异常，则优先触发“异地重建自愈操作”）。当次轮自愈操作超过指定次数后，会等待一段时间再触发下一轮自愈。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~4294967295，单位是次。<br>默认值：无。<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/PODHEALPLY]] · Pod自愈策略（PODHEALPLY）

## 使用实例

配置的Pod自愈策略，状态为NORMAL，预等待时间为300，自愈等待时间为210，自愈次数为3次。

```
SET PODHEALPLY: STATUS=NORMAL, PREWAITTIME=300, HEALWAITTIME=210, HEALNUM=3;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-PODHEALPLY.md`
