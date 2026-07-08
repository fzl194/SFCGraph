---
id: UDG@20.15.2@ConfigObject@HTTPCCACONF
type: ConfigObject
name: HTTPCCACONF（HTTP CCA属性）
nf: UDG
version: 20.15.2
object_name: HTTPCCACONF
object_kind: global_setting
status: active
---

# HTTPCCACONF（HTTP CCA属性）

## 说明

![](设置HTTP CCA属性（SET HTTPCCACONF）_54538297.assets/notice_3.0-zh-cn.png)

开启CCA校验以及修改CCA的有效时长，会影响消息的合法性校验结果，导致消息被丢弃。

该命令用于设置HTTP CCA属性，该属性设置后整系统生效。

> **说明**
> - 该命令执行后立即生效。
>
> - 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：
>
> | CCACHECKSW | CCAPERIOD |
> | --- | --- |
> | OFF | 86400 |

## 操作本对象的命令

- [LST HTTPCCACONF](command/UDG/20.15.2/LST-HTTPCCACONF.md)
- [SET HTTPCCACONF](command/UDG/20.15.2/SET-HTTPCCACONF.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询HTTP-CCA属性（LST-HTTPCCACONF）_54738721.md`
- 原始手册：`evidence/UDG/20.15.2/设置HTTP-CCA属性（SET-HTTPCCACONF）_54538297.md`
