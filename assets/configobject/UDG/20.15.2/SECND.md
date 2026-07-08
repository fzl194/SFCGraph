---
id: UDG@20.15.2@ConfigObject@SECND
type: ConfigObject
name: SECND（ND快回）
nf: UDG
version: 20.15.2
object_name: SECND
object_kind: global_setting
status: active
---

# SECND（ND快回）

## 说明

该命令用来设置ND快回使能配置。

大量客户端发送ND请求报文会造成CPU负载过高。为了降低CPU负载，可通过配置此命令，使设备接收到ND请求报文后不上送CPU处理，直接转发ND响应报文给客户端。

## 操作本对象的命令

- [[command/UDG/20.15.2/LST-SECND]] · LST SECND
- [[command/UDG/20.15.2/SET-SECND]] · SET SECND

## 证据

- 原始手册：`evidence/UDG/20.15.2/SECND.md`
- 原始手册：`evidence/UDG/20.15.2/SECND.md`
