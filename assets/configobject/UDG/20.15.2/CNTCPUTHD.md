---
id: UDG@20.15.2@ConfigObject@CNTCPUTHD
type: ConfigObject
name: CNTCPUTHD（容器CPU阈值）
nf: UDG
version: 20.15.2
object_name: CNTCPUTHD
object_kind: global_setting
status: active
---

# CNTCPUTHD（容器CPU阈值）

## 说明

该命令用于设置容器CPU告警阈值。

> **说明**
> - 该命令执行后立即生效。
>
> - 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：
>
> | WARNTHD | RECVTHD |
> | --- | --- |
> | 80 | 70 |

## 操作本对象的命令

- [LST CNTCPUTHD](command/UDG/20.15.2/LST-CNTCPUTHD.md)
- [SET CNTCPUTHD](command/UDG/20.15.2/SET-CNTCPUTHD.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询容器CPU阈值（LST-CNTCPUTHD）_32743960.md`
- 原始手册：`evidence/UDG/20.15.2/设置容器CPU告警阈值（SET-CNTCPUTHD）_32743962.md`
