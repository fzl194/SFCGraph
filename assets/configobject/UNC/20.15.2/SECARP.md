---
id: UNC@20.15.2@ConfigObject@SECARP
type: ConfigObject
name: SECARP（ARP快回）
nf: UNC
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

- [[command/UNC/20.15.2/LST-SECARP]] · LST SECARP
- [[command/UNC/20.15.2/SET-SECARP]] · SET SECARP

## 证据

- 原始手册：`evidence/UNC/20.15.2/SECARP.md`
- 原始手册：`evidence/UNC/20.15.2/SECARP.md`
