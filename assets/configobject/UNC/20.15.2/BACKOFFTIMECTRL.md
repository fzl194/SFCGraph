---
id: UNC@20.15.2@ConfigObject@BACKOFFTIMECTRL
type: ConfigObject
name: BACKOFFTIMECTRL（异常场景的Back-off Time开关）
nf: UNC
version: 20.15.2
object_name: BACKOFFTIMECTRL
object_kind: global_setting
applicable_nf:
- GGSN
- PGW-C
- SGW-C
status: active
---

# BACKOFFTIMECTRL（异常场景的Back-off Time开关）

## 说明

**适用NF：GGSN、PGW-C、SGW-C**

该命令用来指定异常场景下激活响应中是否携带Back-off Time字段。

## 操作本对象的命令

- [LST BACKOFFTIMECTRL](command/UNC/20.15.2/LST-BACKOFFTIMECTRL.md)
- [SET BACKOFFTIMECTRL](command/UNC/20.15.2/SET-BACKOFFTIMECTRL.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询异常场景的Back-off-Time开关（LST-BACKOFFTIMECTRL）_96242091.md`
- 原始手册：`evidence/UNC/20.15.2/设置异常场景的Back-off-Time开关（SET-BACKOFFTIMECTRL）_96243091.md`
