---
id: UNC@20.15.2@ConfigObject@SECCARSTAT
type: ConfigObject
name: SECCARSTAT（安全CAR功能丢弃上送CPU报文的详细信息）
nf: UNC
version: 20.15.2
object_name: SECCARSTAT
object_kind: action
status: active
---

# SECCARSTAT（安全CAR功能丢弃上送CPU报文的详细信息）

## 说明

该命令用来显示丢弃的报文的和上送CPU的报文的详细情况。当CPU利用率很高时，通过执行此命令，可以显示各个协议上送CPU的报文被丢弃的数目，从而关闭那些上送报文过多且无需启动的协议。

## 操作本对象的命令

- [DSP SECCARSTAT](command/UNC/20.15.2/DSP-SECCARSTAT.md)
- [RTR SECCARSTAT](command/UNC/20.15.2/RTR-SECCARSTAT.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示安全CAR功能丢弃上送CPU报文的详细信息（DSP-SECCARSTAT）_00600781.md`
- 原始手册：`evidence/UNC/20.15.2/清除承诺访问速率具体信息（RTR-SECCARSTAT）_50280698.md`
