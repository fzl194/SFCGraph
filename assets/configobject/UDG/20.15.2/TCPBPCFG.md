---
id: UDG@20.15.2@ConfigObject@TCPBPCFG
type: ConfigObject
name: TCPBPCFG（TCP过载反压HTTP流控配置）
nf: UDG
version: 20.15.2
object_name: TCPBPCFG
object_kind: global_setting
status: active
---

# TCPBPCFG（TCP过载反压HTTP流控配置）

## 说明

![](设置TCP过载反压HTTP流控配置（SET TCPBPCFG）_94795792.assets/notice_3.0-zh-cn.png)

该命令是高危命令，误开启可能会引起HTTP进程流控，请谨慎使用并联系华为技术支持协助操作。

该命令用于设置传输层TCP过载反压到应用层HTTP流控配置。

> **说明**
> - 该命令执行后立即生效。
>
> - 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：
>
> | SWITCH | STARTTHD | STARTDU | STOPTHD | STOPDU | FCDIRECT |
> | --- | --- | --- | --- | --- | --- |
> | OFF | 80 | 5 | 75 | 60 | CLIENT |

## 操作本对象的命令

- [[command/UDG/20.15.2/LST-TCPBPCFG]] · LST TCPBPCFG
- [[command/UDG/20.15.2/SET-TCPBPCFG]] · SET TCPBPCFG

## 证据

- 原始手册：`evidence/UDG/20.15.2/TCPBPCFG.md`
- 原始手册：`evidence/UDG/20.15.2/TCPBPCFG.md`
