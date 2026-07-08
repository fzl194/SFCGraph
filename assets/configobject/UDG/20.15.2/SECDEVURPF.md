---
id: UDG@20.15.2@ConfigObject@SECDEVURPF
type: ConfigObject
name: SECDEVURPF（设备URPF）
nf: UDG
version: 20.15.2
object_name: SECDEVURPF
object_kind: global_setting
status: active
---

# SECDEVURPF（设备URPF）

## 说明

该命令用来配置安全策略URPF。

URPF通过获取报文的源地址和入接口，以源地址为目的地址，在转发表中查找源地址对应的接口是否与入接口匹配，如果不匹配，则认为源地址是伪装的，并丢弃该报文（松散模式URPF不会匹配入接口）。通过这种方式，URPF就能有效地防范网络中通过修改源地址而进行的恶意攻击行为的发生。

## 操作本对象的命令

- [LST SECDEVURPF](command/UDG/20.15.2/LST-SECDEVURPF.md)
- [SET SECDEVURPF](command/UDG/20.15.2/SET-SECDEVURPF.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询设备URPF（LST-SECDEVURPF）_00600413.md`
- 原始手册：`evidence/UDG/20.15.2/设置设备URPF（SET-SECDEVURPF）_50280794.md`
