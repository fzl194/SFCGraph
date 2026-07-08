---
id: UDG@20.15.2@ConfigObject@TOKENDELAY
type: ConfigObject
name: TOKENDELAY（Token延时迁移时间）
nf: UDG
version: 20.15.2
object_name: TOKENDELAY
object_kind: global_setting
status: active
---

# TOKENDELAY（Token延时迁移时间）

## 说明

![](设置Token延时迁移时间（SET TOKENDELAY）_79244269.assets/notice_3.0-zh-cn.png)

执行此命令可能导致系统没有可用的实例。

执行此命令可能导致扩容、服务实例故障恢复的时间延长。

本次命令将修改TokenDelay，请务必在华为技术支持人员的指导下使用该命令。

该命令用于修改Token的延时迁移时间，对整系统生效。可以用于在某个服务实例状态转为Normal，并准备分配或迁移Token时，实现延时定时器功能。当超过定时器时长时，再将Token迁入到该实例。

Token可以理解为NF内部服务使用的短期令牌，当且仅当手持令牌时，才能获取所需服务。

> **说明**
> - 该命令执行后立即生效。
>
> - 整系统生效。
> - 对于某个服务来说，如果系统配置了延时迁移，又使能了就绪静默功能，则就绪静默功能生效，延时迁移不生效。
> - 因服务频繁复位，在配置的延时时长内，可能导致没有可用的实例用于分配Token。
> - 使用了该功能，对正常扩容的Pod、灰度升级/分批升级场景下回迁的Pod也存在影响，会影响扩容、升级的时长。
> - 如果系统已设置了延时迁移时间，再次设置后会根据当前的延时迁移时间更新定时器
>
> - 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：
>
> | DELAYTIME |
> | --- |
> | 0 |

## 操作本对象的命令

- [[command/UDG/20.15.2/LST-TOKENDELAY]] · LST TOKENDELAY
- [[command/UDG/20.15.2/SET-TOKENDELAY]] · SET TOKENDELAY

## 证据

- 原始手册：`evidence/UDG/20.15.2/TOKENDELAY.md`
- 原始手册：`evidence/UDG/20.15.2/TOKENDELAY.md`
