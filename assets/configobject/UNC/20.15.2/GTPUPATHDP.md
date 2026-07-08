---
id: UNC@20.15.2@ConfigObject@GTPUPATHDP
type: ConfigObject
name: GTPUPATHDP（GTP-U路径管理自定义策略）
nf: UNC
version: 20.15.2
object_name: GTPUPATHDP
object_kind: entity
applicable_nf:
- SGSN
status: active
---

# GTPUPATHDP（GTP-U路径管理自定义策略）

## 说明

**适用网元：SGSN**

该命令用于增加GTP-U路径管理自定义策略。

该命令引入一个系数钝化GTP-U路径故障的判定，每次T3*N3探测为一个判定周期，需要连续X个判定周期的Echo探测都没有响应后，才判定为GTP-U路径故障。

引入的这个系数会较大地钝化GTP-U路径故障的判定，若闪断频繁发生，钝化GTP-U路径故障判定条件会掩盖闪断的问题，此时GTP-U路径故障告警定位为反映对端长时间故障不通的问题。若未出现GTP-U路径故障告警但出现激活成功率下降，可以通过GTP-U接口跟踪，或者将故障判定条件调得更加灵敏来临时定位。

使用场景举例：

漫游路径的GTP-U路径故障告警较多，故障状态的GTP-U路径持续时长90%在4~10分钟内分布。通过调大漫游路径的故障判定条件高于10分钟，减少GTP-U路径故障告警。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-GTPUPATHDP]] · ADD GTPUPATHDP
- [[command/UNC/20.15.2/LST-GTPUPATHDP]] · LST GTPUPATHDP
- [[command/UNC/20.15.2/MOD-GTPUPATHDP]] · MOD GTPUPATHDP
- [[command/UNC/20.15.2/RMV-GTPUPATHDP]] · RMV GTPUPATHDP

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改GTP-U路径管理自定义策略(MOD-GTPUPATHDP)_72345443.md`
- 原始手册：`evidence/UNC/20.15.2/删除GTP-U路径管理自定义策略(RMV-GTPUPATHDP)_26305652.md`
- 原始手册：`evidence/UNC/20.15.2/增加GTP-U路径管理自定义策略(ADD-GTPUPATHDP)_72225521.md`
- 原始手册：`evidence/UNC/20.15.2/查询GTP-U路径管理自定义策略(LST-GTPUPATHDP)_26145844.md`
