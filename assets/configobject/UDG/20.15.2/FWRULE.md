---
id: UDG@20.15.2@ConfigObject@FWRULE
type: ConfigObject
name: FWRULE（转发规则）
nf: UDG
version: 20.15.2
object_name: FWRULE
object_kind: entity
status: active
---

# FWRULE（转发规则）

## 说明

![](增加转发规则（ADD FWRULE）_01524840.assets/notice_3.0-zh-cn.png)

该命令执行后可能会影响到目的IP的转发，请谨慎操作。

此命令用于增加指定IP的原端口到目的端口的转发规则，可用于SFTP端口的转换。

> **说明**
> - 该命令仅限角色为Administrators的用户执行。
>
> - 同一目的IP和端口只能配置一条规则，若需修改，请先使用**[RMV FWRULE](删除转发规则（RMV FWRULE）_01844648.md)**命令删除该规则后使用本命令重新配置。

## 操作本对象的命令

- [[command/UDG/20.15.2/ADD-FWRULE]] · ADD FWRULE
- [[command/UDG/20.15.2/LST-FWRULE]] · LST FWRULE
- [[command/UDG/20.15.2/RMV-FWRULE]] · RMV FWRULE

## 证据

- 原始手册：`evidence/UDG/20.15.2/FWRULE.md`
- 原始手册：`evidence/UDG/20.15.2/FWRULE.md`
- 原始手册：`evidence/UDG/20.15.2/FWRULE.md`
