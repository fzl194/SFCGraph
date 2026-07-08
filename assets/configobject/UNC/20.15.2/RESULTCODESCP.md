---
id: UNC@20.15.2@ConfigObject@RESULTCODESCP
type: ConfigObject
name: RESULTCODESCP（配置MODELC/D组网的SCP原因码控制）
nf: UNC
version: 20.15.2
object_name: RESULTCODESCP
object_kind: entity
applicable_nf:
- SMF
- PGW-C
- GGSN
status: active
---

# RESULTCODESCP（配置MODELC/D组网的SCP原因码控制）

## 说明

**适用NF：SMF、PGW-C、GGSN**

此命令用来配置当UNC收到指定组网场景结果码信息后执行何种操作。例如关闭PCC功能、执行缺省动作、执行宕机备份等。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-RESULTCODESCP]] · ADD RESULTCODESCP
- [[command/UNC/20.15.2/LST-RESULTCODESCP]] · LST RESULTCODESCP
- [[command/UNC/20.15.2/MOD-RESULTCODESCP]] · MOD RESULTCODESCP
- [[command/UNC/20.15.2/RMV-RESULTCODESCP]] · RMV RESULTCODESCP

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改配置MODELC_D组网的SCP原因码控制（MOD-RESULTCODESCP）_16763161.md`
- 原始手册：`evidence/UNC/20.15.2/删除配置MODELC_D组网的SCP原因码控制（RMV-RESULTCODESCP）_81322862.md`
- 原始手册：`evidence/UNC/20.15.2/增加配置MODELC_D组网的SCP原因码控制（ADD-RESULTCODESCP）_81322858.md`
- 原始手册：`evidence/UNC/20.15.2/查询配置MODELC_D组网的SCP原因码（LST-RESULTCODESCP）_16808737.md`
