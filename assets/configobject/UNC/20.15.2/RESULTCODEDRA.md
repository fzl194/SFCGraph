---
id: UNC@20.15.2@ConfigObject@RESULTCODEDRA
type: ConfigObject
name: RESULTCODEDRA（DRA返回码控制）
nf: UNC
version: 20.15.2
object_name: RESULTCODEDRA
object_kind: entity
applicable_nf:
- PGW-C
- GGSN
status: active
---

# RESULTCODEDRA（DRA返回码控制）

## 说明

**适用NF：PGW-C、GGSN**

此命令用来配置当UNC收到DRA回复的指定结果码信息后执行何种操作。例如关闭PCC功能、执行缺省动作、执行宕机备份等。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-RESULTCODEDRA]] · ADD RESULTCODEDRA
- [[command/UNC/20.15.2/LST-RESULTCODEDRA]] · LST RESULTCODEDRA
- [[command/UNC/20.15.2/MOD-RESULTCODEDRA]] · MOD RESULTCODEDRA
- [[command/UNC/20.15.2/RMV-RESULTCODEDRA]] · RMV RESULTCODEDRA

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改DRA返回码控制（MOD-RESULTCODEDRA）_31943230.md`
- 原始手册：`evidence/UNC/20.15.2/删除DRA返回码控制（RMV-RESULTCODEDRA）_32101390.md`
- 原始手册：`evidence/UNC/20.15.2/增加DRA返回码控制（ADD-RESULTCODEDRA）_67382653.md`
- 原始手册：`evidence/UNC/20.15.2/查询DRA返回码控制（LST-RESULTCODEDRA）_67261101.md`
