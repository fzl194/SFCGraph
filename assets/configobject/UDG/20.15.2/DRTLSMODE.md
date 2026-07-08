---
id: UDG@20.15.2@ConfigObject@DRTLSMODE
type: ConfigObject
name: DRTLSMODE（容灾控制通道TLS模式）
nf: UDG
version: 20.15.2
object_name: DRTLSMODE
object_kind: global_setting
status: active
---

# DRTLSMODE（容灾控制通道TLS模式）

## 说明

![](设置容灾控制通道TLS模式（SET DRTLSMODE）_55919521.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，主备网元配置不同可能会导致容灾控制通道通信故障，影响现网业务，请谨慎使用并联系华为技术支持协助操作。

该命令用于设置容灾控制通道TLS模式。

> **说明**
> - 该命令执行后立即生效。
>
> - 该命令要求主备网元配置相同的TLS模式，否则会导致容灾控制通道通信故障。
> - 当执行本命令变更网元TLS模式时，必须在容灾心跳控制时间内对其主备网元完成同样的TLS模式变更。
>
> - 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：
>
> | TLSMODE |
> | --- |
> | OFF |

## 操作本对象的命令

- [[command/UDG/20.15.2/LST-DRTLSMODE]] · LST DRTLSMODE
- [[command/UDG/20.15.2/SET-DRTLSMODE]] · SET DRTLSMODE

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询容灾控制通道TLS模式（LST-DRTLSMODE）_56001165.md`
- 原始手册：`evidence/UDG/20.15.2/设置容灾控制通道TLS模式（SET-DRTLSMODE）_55919521.md`
