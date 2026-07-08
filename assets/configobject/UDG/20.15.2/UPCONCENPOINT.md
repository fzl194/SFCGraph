---
id: UDG@20.15.2@ConfigObject@UPCONCENPOINT
type: ConfigObject
name: UPCONCENPOINT（集中点部署模式）
nf: UDG
version: 20.15.2
object_name: UPCONCENPOINT
object_kind: global_setting
applicable_nf:
- UPF
status: active
---

# UPCONCENPOINT（集中点部署模式）

## 说明

**适用NF：UPF**

![](设置集中点部署模式（SET UPCONCENPOINT）_97314577.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，修改集中点模式可能导致Diameter链路重建或中断，进而影响用户使用业务，比如用户被去活等。涉及Diameter链路的接口为Swm接口。

此命令用于设置信令集中点的部署模式。

## 操作本对象的命令

- [[command/UDG/20.15.2/LST-UPCONCENPOINT]] · LST UPCONCENPOINT
- [[command/UDG/20.15.2/SET-UPCONCENPOINT]] · SET UPCONCENPOINT

## 证据

- 原始手册：`evidence/UDG/20.15.2/UPCONCENPOINT.md`
- 原始手册：`evidence/UDG/20.15.2/UPCONCENPOINT.md`
