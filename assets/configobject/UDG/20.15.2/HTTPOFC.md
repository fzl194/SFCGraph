---
id: UDG@20.15.2@ConfigObject@HTTPOFC
type: ConfigObject
name: HTTPOFC（HTTP局向）
nf: UDG
version: 20.15.2
object_name: HTTPOFC
object_kind: entity
status: active
---

# HTTPOFC（HTTP局向）

## 说明

该命令用于增加HTTP局向。

局向是信令与外部设备交互的方向。例如本端AMF到对端SMF可以定义为一个局向。可通过两种方式标识一个局向：（1）对端IP，IP可以是单个IP也可以是一组IP；（2）对端网元类型。

> **说明**
> - 该命令执行后立即生效。
>
> - "PEERNFTYPE"为NFTypeSCP或NFTypeSEPP时不支持"NFITEM"设置基于接口类型HTR流控或基于接口类型固定速率流控。
> - IP组的地址配置为SCP或SEPP的IP，HTR流控功能不生效。
>
> - 最多可输入4096条记录。

## 操作本对象的命令

- [[command/UDG/20.15.2/ADD-HTTPOFC]] · ADD HTTPOFC
- [[command/UDG/20.15.2/LST-HTTPOFC]] · LST HTTPOFC
- [[command/UDG/20.15.2/MOD-HTTPOFC]] · MOD HTTPOFC
- [[command/UDG/20.15.2/RMV-HTTPOFC]] · RMV HTTPOFC

## 证据

- 原始手册：`evidence/UDG/20.15.2/HTTPOFC.md`
- 原始手册：`evidence/UDG/20.15.2/HTTPOFC.md`
- 原始手册：`evidence/UDG/20.15.2/HTTPOFC.md`
- 原始手册：`evidence/UDG/20.15.2/HTTPOFC.md`
