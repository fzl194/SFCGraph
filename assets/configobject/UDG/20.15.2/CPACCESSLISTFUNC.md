---
id: UDG@20.15.2@ConfigObject@CPACCESSLISTFUNC
type: ConfigObject
name: CPACCESSLISTFUNC（CP白名单开关）
nf: UDG
version: 20.15.2
object_name: CPACCESSLISTFUNC
object_kind: global_setting
applicable_nf:
- SGW-U
- PGW-U
- UPF
status: active
---

# CPACCESSLISTFUNC（CP白名单开关）

## 说明

**适用NF：SGW-U、PGW-U、UPF**

![](配置CP白名单开关（SET CPACCESSLISTFUNC）_86530396.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，请使用ADD CPACCESSLIST配置完整的白名单后再使用该功能，白名单外的设备将无法建立偶联。

该命令用于配置是否支持CP白名单功能。配置白名单后，将对CP发来的PFCP Association Setup Request消息进行控制，只有白名单范围内的CP才能和UPF建立偶联连接，才允许激活用户。

## 操作本对象的命令

- [LST CPACCESSLISTFUNC](command/UDG/20.15.2/LST-CPACCESSLISTFUNC.md)
- [SET CPACCESSLISTFUNC](command/UDG/20.15.2/SET-CPACCESSLISTFUNC.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询CP白名单开关（LST-CPACCESSLISTFUNC）_86530397.md`
- 原始手册：`evidence/UDG/20.15.2/配置CP白名单开关（SET-CPACCESSLISTFUNC）_86530396.md`
