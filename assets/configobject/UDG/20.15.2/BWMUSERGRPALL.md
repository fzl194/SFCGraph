---
id: UDG@20.15.2@ConfigObject@BWMUSERGRPALL
type: ConfigObject
name: BWMUSERGRPALL（所有带宽管理用户组）
nf: UDG
version: 20.15.2
object_name: BWMUSERGRPALL
object_kind: entity
applicable_nf:
- PGW-U
- UPF
status: active
---

# BWMUSERGRPALL（所有带宽管理用户组）

## 说明

**适用NF：PGW-U、UPF**

![](删除所有带宽管理用户组（RMV BWMUSERGRPALL）_08574047.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，会删除带宽管理用户组下所有绑定关系。

该命令用于删除所有的带宽管理用户组。当运营商希望删除已配置的默认用户组或具体用户组时，则执行该命令。

## 操作本对象的命令

- [[command/UDG/20.15.2/RMV-BWMUSERGRPALL]] · RMV BWMUSERGRPALL

## 证据

- 原始手册：`evidence/UDG/20.15.2/BWMUSERGRPALL.md`
