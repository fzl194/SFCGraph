---
id: UDG@20.15.2@ConfigObject@UEINJECTPKT
type: ConfigObject
name: UEINJECTPKT（UE灌包参数）
nf: UDG
version: 20.15.2
object_name: UEINJECTPKT
object_kind: entity
applicable_nf:
- SGW-U
- PGW-U
- UPF
status: active
---

# UEINJECTPKT（UE灌包参数）

## 说明

**适用NF：SGW-U、PGW-U、UPF**

![](设置UE灌包参数（SET UEINJECTPKT）_82837091.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，请确保SRCPORT参数不要配置保留端口1～1023，否则可能导致通用业务无法正常进行。

该命令用于配置UE下行灌包功能的UE灌包参数。

## 操作本对象的命令

- [[command/UDG/20.15.2/LST-UEINJECTPKT]] · LST UEINJECTPKT
- [[command/UDG/20.15.2/RMV-UEINJECTPKT]] · RMV UEINJECTPKT
- [[command/UDG/20.15.2/SET-UEINJECTPKT]] · SET UEINJECTPKT

## 证据

- 原始手册：`evidence/UDG/20.15.2/UEINJECTPKT.md`
- 原始手册：`evidence/UDG/20.15.2/UEINJECTPKT.md`
- 原始手册：`evidence/UDG/20.15.2/UEINJECTPKT.md`
