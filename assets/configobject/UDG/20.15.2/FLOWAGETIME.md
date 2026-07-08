---
id: UDG@20.15.2@ConfigObject@FLOWAGETIME
type: ConfigObject
name: FLOWAGETIME（五元组老化时间）
nf: UDG
version: 20.15.2
object_name: FLOWAGETIME
object_kind: global_setting
applicable_nf:
- PGW-U
- UPF
status: active
---

# FLOWAGETIME（五元组老化时间）

## 说明

**适用NF：PGW-U、UPF**

![](设置五元组老化时间（SET FLOWAGETIME）_82837291.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，可能会影响业务。

该命令用于配置头增强五元组、三四层五元组、TCP信令五元组、任意协议五元组和本地分流五元组的老化时间。

## 操作本对象的命令

- [LST FLOWAGETIME](command/UDG/20.15.2/LST-FLOWAGETIME.md)
- [RTR FLOWAGETIME](command/UDG/20.15.2/RTR-FLOWAGETIME.md)
- [SET FLOWAGETIME](command/UDG/20.15.2/SET-FLOWAGETIME.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/恢复五元组老化时间（RTR-FLOWAGETIME）_82837292.md`
- 原始手册：`evidence/UDG/20.15.2/查询五元组老化时间（LST-FLOWAGETIME）_82837293.md`
- 原始手册：`evidence/UDG/20.15.2/设置五元组老化时间（SET-FLOWAGETIME）_82837291.md`
