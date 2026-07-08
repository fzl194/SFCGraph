---
id: UNC@20.15.2@ConfigObject@UPFADDRATTR
type: ConfigObject
name: UPFADDRATTR（UPF地址属性）
nf: UNC
version: 20.15.2
object_name: UPFADDRATTR
object_kind: entity
applicable_nf:
- SMF
status: active
---

# UPFADDRATTR（UPF地址属性）

## 说明

![](增加UPF地址属性（ADD UPFADDRATTR）_49289393.assets/notice_3.0-zh-cn_2.png)

ISPROXY参数设置错误会导致UPG热备特性和双UPG故障bypass功能失效。

SMF与UPF之间只允许配置1条直连路径（ISPROXY参数只能设置1条非代理路径），误配置可能会导致双UPG故障bypass功能不可用。

**适用NF：SMF**

该命令用于增加UPF地址属性。

## 操作本对象的命令

- [ADD UPFADDRATTR](command/UNC/20.15.2/ADD-UPFADDRATTR.md)
- [LST UPFADDRATTR](command/UNC/20.15.2/LST-UPFADDRATTR.md)
- [MOD UPFADDRATTR](command/UNC/20.15.2/MOD-UPFADDRATTR.md)
- [RMV UPFADDRATTR](command/UNC/20.15.2/RMV-UPFADDRATTR.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改UPF地址属性（MOD-UPFADDRATTR）_21742361.md`
- 原始手册：`evidence/UNC/20.15.2/删除UPF地址属性（RMV-UPFADDRATTR）_99049128.md`
- 原始手册：`evidence/UNC/20.15.2/增加UPF地址属性（ADD-UPFADDRATTR）_49289393.md`
- 原始手册：`evidence/UNC/20.15.2/查询UPF地址属性（LST-UPFADDRATTR）_99209112.md`
