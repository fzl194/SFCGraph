---
id: UNC@20.15.2@ConfigObject@SDUPPATH
type: ConfigObject
name: SDUPPATH（测试SDUP路径）
nf: UNC
version: 20.15.2
object_name: SDUPPATH
object_kind: action
applicable_nf:
- MME
status: active
---

# SDUPPATH（测试SDUP路径）

## 说明

**适用网元：MME**

该命令用于通过发送Echo消息的方法测试本端与对端MME之间的SDUP路径是否正常。无论路径正常与否，都返回报文显示路径地址信息及路径状态；

## 操作本对象的命令

- [[command/UNC/20.15.2/TST-SDUPPATH]] · TST SDUPPATH

## 证据

- 原始手册：`evidence/UNC/20.15.2/SDUPPATH.md`
