---
id: UDG@20.15.2@ConfigObject@LSPVGLOBALCFG
type: ConfigObject
name: LSPVGLOBALCFG（LSPV全局属性）
nf: UDG
version: 20.15.2
object_name: LSPVGLOBALCFG
object_kind: global_setting
status: active
---

# LSPVGLOBALCFG（LSPV全局属性）

## 说明

该命令用于配置LSPV全局属性。

当设备作为标签转发路径检测的响应端时，可能收到大量MPLS ECHO-REQUEST报文需要处理，可以执行SET LSPVGLOBALCFG命令使能设备LSPV模块和配置LSPV模块的MPLS ECHO-REQUEST报文处理速率，从而保证设备能够接收MPLS ECHO-REQUEST报文，并回应MPLS ECHO-REPLY报文。

## 操作本对象的命令

- [LST LSPVGLOBALCFG](command/UDG/20.15.2/LST-LSPVGLOBALCFG.md)
- [SET LSPVGLOBALCFG](command/UDG/20.15.2/SET-LSPVGLOBALCFG.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询LSPV全局属性（LST-LSPVGLOBALCFG）_00866665.md`
- 原始手册：`evidence/UDG/20.15.2/设置LSPV全局属性（SET-LSPVGLOBALCFG）_50280878.md`
