---
id: UDG@20.15.2@ConfigObject@INTFURPF
type: ConfigObject
name: INTFURPF（安全接口URPF）
nf: UDG
version: 20.15.2
object_name: INTFURPF
object_kind: entity
status: active
---

# INTFURPF（安全接口URPF）

## 说明

该命令用来增加接口的URPF配置。

URPF通过获取报文的源地址和入接口，以源地址为目的地址，在转发表中查找源地址对应的接口是否与入接口匹配，如果不匹配，则认为源地址是伪装的，并丢弃该报文（松散模式URPF不会匹配入接口）。通过这种方式，URPF就能有效地防范网络中通过修改源地址而进行的恶意攻击行为的发生。

## 操作本对象的命令

- [[command/UDG/20.15.2/ADD-INTFURPF]] · ADD INTFURPF
- [[command/UDG/20.15.2/LST-INTFURPF]] · LST INTFURPF
- [[command/UDG/20.15.2/MOD-INTFURPF]] · MOD INTFURPF
- [[command/UDG/20.15.2/RMV-INTFURPF]] · RMV INTFURPF

## 证据

- 原始手册：`evidence/UDG/20.15.2/INTFURPF.md`
- 原始手册：`evidence/UDG/20.15.2/INTFURPF.md`
- 原始手册：`evidence/UDG/20.15.2/INTFURPF.md`
- 原始手册：`evidence/UDG/20.15.2/INTFURPF.md`
