---
id: UDG@20.15.2@ConfigObject@GIREDIRECTFUNC
type: ConfigObject
name: GIREDIRECTFUNC（全局Gi重定向信息）
nf: UDG
version: 20.15.2
object_name: GIREDIRECTFUNC
object_kind: global_setting
applicable_nf:
- SGW-U
- PGW-U
- UPF
status: active
---

# GIREDIRECTFUNC（全局Gi重定向信息）

## 说明

**适用NF：SGW-U、PGW-U、UPF**

该命令用于设置Gi重定向全局开关，当需要控制UE之间互访的恶意攻击报文和需要通过网关将报文重定向来保证网络的安全的场景下使用此命令设置Gi重定向全局开关。当全局开关使能后，基于VPN的重定向配置才会生效，允许将用户报文重定向到指定地址或者丢弃。当全局开关不使能时，允许UE互访。

## 操作本对象的命令

- [[command/UDG/20.15.2/LST-GIREDIRECTFUNC]] · LST GIREDIRECTFUNC
- [[command/UDG/20.15.2/SET-GIREDIRECTFUNC]] · SET GIREDIRECTFUNC

## 证据

- 原始手册：`evidence/UDG/20.15.2/GIREDIRECTFUNC.md`
- 原始手册：`evidence/UDG/20.15.2/GIREDIRECTFUNC.md`
