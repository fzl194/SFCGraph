---
id: UNC@20.15.2@ConfigObject@GTPCPATHDP
type: ConfigObject
name: GTPCPATHDP（GTP-C路径管理自定义策略）
nf: UNC
version: 20.15.2
object_name: GTPCPATHDP
object_kind: entity
applicable_nf:
- SGSN
status: active
---

# GTPCPATHDP（GTP-C路径管理自定义策略）

## 说明

**适用网元：SGSN**

该命令用于增加GTP-C路径管理自定义策略。

该命令引入一个系数钝化GTP-C路径故障的判定，每次T3*N3探测为一个判定周期，需要连续X个判定周期的Echo探测都没有响应后，才判定为GTP-C路径故障。

引入的这个系数会较大地钝化GTP-C路径故障的判定，若闪断频繁发生，钝化GTP-C路径故障判定条件会掩盖闪断的问题，此时GTP-C路径故障告警定位为反映对端长时间故障不通的问题。若未出现GTP-C路径故障告警但出现激活成功率下降，可以通过GTP-C接口跟踪，或者将故障判定条件调得更加灵敏来临时定位。

使用场景举例：

漫游路径的GTP-C路径故障告警较多，故障状态的GTP-C路径持续时长90%在4~10分钟内分布。通过调大漫游路径的故障判定条件高于10分钟，减少GTP-C路径故障告警。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-GTPCPATHDP]] · ADD GTPCPATHDP
- [[command/UNC/20.15.2/LST-GTPCPATHDP]] · LST GTPCPATHDP
- [[command/UNC/20.15.2/MOD-GTPCPATHDP]] · MOD GTPCPATHDP
- [[command/UNC/20.15.2/RMV-GTPCPATHDP]] · RMV GTPCPATHDP

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改GTP-C路径管理自定义策略(MOD-GTPCPATHDP)_72225593.md`
- 原始手册：`evidence/UNC/20.15.2/删除GTP-C路径管理自定义策略(RMV-GTPCPATHDP)_26145914.md`
- 原始手册：`evidence/UNC/20.15.2/增加GTP-C路径管理自定义策略(ADD-GTPCPATHDP)_72345513.md`
- 原始手册：`evidence/UNC/20.15.2/查询GTP-C路径管理自定义策略(LST-GTPCPATHDP)_26305724.md`
