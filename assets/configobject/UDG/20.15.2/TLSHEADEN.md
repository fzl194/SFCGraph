---
id: UDG@20.15.2@ConfigObject@TLSHEADEN
type: ConfigObject
name: TLSHEADEN（HTTPS头增强）
nf: UDG
version: 20.15.2
object_name: TLSHEADEN
object_kind: entity
applicable_nf:
- PGW-U
- UPF
status: active
---

# TLSHEADEN（HTTPS头增强）

## 说明

**适用NF：PGW-U、UPF**

该命令用于添加HTTPS头增强的相关配置。配置头增强功能，可以将用户相关信息插入协议头部，传递给Web服务器，Web服务器获取到这些信息以后可以用于结算、折扣、提示等，便于灵活开展业务。

## 操作本对象的命令

- [[command/UDG/20.15.2/ADD-TLSHEADEN]] · ADD TLSHEADEN
- [[command/UDG/20.15.2/LST-TLSHEADEN]] · LST TLSHEADEN
- [[command/UDG/20.15.2/MOD-TLSHEADEN]] · MOD TLSHEADEN
- [[command/UDG/20.15.2/RMV-TLSHEADEN]] · RMV TLSHEADEN

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改HTTPS头增强（MOD-TLSHEADEN）_82837522.md`
- 原始手册：`evidence/UDG/20.15.2/删除HTTPS头增强（RMV-TLSHEADEN）_82837523.md`
- 原始手册：`evidence/UDG/20.15.2/增加HTTPS头增强（ADD-TLSHEADEN）_82837521.md`
- 原始手册：`evidence/UDG/20.15.2/查询HTTPS头增强（LST-TLSHEADEN）_82837524.md`
