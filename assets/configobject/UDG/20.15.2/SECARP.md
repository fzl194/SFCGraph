---
id: UDG@20.15.2@ConfigObject@SECARP
type: ConfigObject
name: SECARP（ARP快回）
nf: UDG
version: 20.15.2
object_name: SECARP
object_kind: global_setting
status: active
---

# SECARP（ARP快回）

## 说明

该命令用来设置ARP快回使能配置。

大量客户端发送ARP请求报文会造成CPU负载过高。为了降低CPU负载，可通过配置此命令，使设备接收到ARP请求报文后不上送CPU处理，直接转发ARP响应报文给客户端。

## 操作本对象的命令

- [LST SECARP](command/UDG/20.15.2/LST-SECARP.md)
- [SET SECARP](command/UDG/20.15.2/SET-SECARP.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询ARP快回（LST-SECARP）_50121366.md`
- 原始手册：`evidence/UDG/20.15.2/设置ARP快回配置（SET-SECARP）_49961622.md`
