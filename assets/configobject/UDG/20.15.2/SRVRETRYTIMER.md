---
id: UDG@20.15.2@ConfigObject@SRVRETRYTIMER
type: ConfigObject
name: SRVRETRYTIMER（服务重试等待时间）
nf: UDG
version: 20.15.2
object_name: SRVRETRYTIMER
object_kind: global_setting
applicable_nf:
- PGW-U
- UPF
status: active
---

# SRVRETRYTIMER（服务重试等待时间）

## 说明

**适用NF：PGW-U、UPF**

此命令用于设置服务上报出现上报失败/上报响应超时/响应失败的异常场景后重新发起上报需要等待的时间。

## 操作本对象的命令

- [[command/UDG/20.15.2/LST-SRVRETRYTIMER]] · LST SRVRETRYTIMER
- [[command/UDG/20.15.2/SET-SRVRETRYTIMER]] · SET SRVRETRYTIMER

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询服务重试等待时间（LST-SRVRETRYTIMER）_06055000.md`
- 原始手册：`evidence/UDG/20.15.2/设置服务重试等待时间（SET-SRVRETRYTIMER）_06054999.md`
