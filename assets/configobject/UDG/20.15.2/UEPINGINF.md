---
id: UDG@20.15.2@ConfigObject@UEPINGINF
type: ConfigObject
name: UEPINGINF（UE Ping逻辑接口开关）
nf: UDG
version: 20.15.2
object_name: UEPINGINF
object_kind: global_setting
applicable_nf:
- SGW-U
- PGW-U
- UPF
status: active
---

# UEPINGINF（UE Ping逻辑接口开关）

## 说明

**适用NF：SGW-U、PGW-U、UPF**

![](设置UE Ping逻辑接口开关（SET UEPINGINF）_79568175.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，测试完成后，请及时删除该配置，否则存在安全风险。

该命令用于设置UE ping逻辑口的开关。如果开关使能，则系统会对UE ping逻辑口的报文回响应。

## 操作本对象的命令

- [[command/UDG/20.15.2/LST-UEPINGINF]] · LST UEPINGINF
- [[command/UDG/20.15.2/SET-UEPINGINF]] · SET UEPINGINF

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询UE-Ping逻辑接口开关（LST-UEPINGINF）_79568176.md`
- 原始手册：`evidence/UDG/20.15.2/设置UE-Ping逻辑接口开关（SET-UEPINGINF）_79568175.md`
