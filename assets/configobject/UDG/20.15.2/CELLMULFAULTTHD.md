---
id: UDG@20.15.2@ConfigObject@CELLMULFAULTTHD
type: ConfigObject
name: CELLMULFAULTTHD（进程频繁故障监控参数）
nf: UDG
version: 20.15.2
object_name: CELLMULFAULTTHD
object_kind: entity
status: active
---

# CELLMULFAULTTHD（进程频繁故障监控参数）

## 说明

该命令用于设置进程频繁故障监控参数值。

> **说明**
> - 该命令执行后立即生效。
>
> - 当系统不存在CELL_SSG的监控配置时，CELL_SSG默认开启监控，故障告警监控时间为1440分钟，故障告警故障次数为5次，恢复告警监控时间为10分钟，恢复告警监控次数为0次。
> - 当执行本命令为CELL_SSG配置服务进程频繁告警参数时，以本命令配置参数生效。
> - 一旦通过本命令为某进程配置了服务进程频繁告警参数，后续只能通过[**MOD CELLMULFAULTTHD**](修改进程频繁故障监控参数（MOD CELLMULFAULTTHD）_88226716.md)命令对参数进行修改。
> - 配置的进程类型需要遵循[**DSP MSPROCTYPE**](显示微服务进程类型（DSP MSPROCTYPE）_09587905.md)显示的进程类型，如果进程类型配置错误，则期望的进程发生故障时不会上报告警。
> - 参数“故障告警故障次数”取值需大于参数“恢复告警监控次数”的取值。
>
> - 最多可输入1024条记录。

## 操作本对象的命令

- [[command/UDG/20.15.2/ADD-CELLMULFAULTTHD]] · ADD CELLMULFAULTTHD
- [[command/UDG/20.15.2/LST-CELLMULFAULTTHD]] · LST CELLMULFAULTTHD
- [[command/UDG/20.15.2/MOD-CELLMULFAULTTHD]] · MOD CELLMULFAULTTHD
- [[command/UDG/20.15.2/RMV-CELLMULFAULTTHD]] · RMV CELLMULFAULTTHD

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改进程频繁故障监控参数（MOD-CELLMULFAULTTHD）_88226716.md`
- 原始手册：`evidence/UDG/20.15.2/删除进程频繁故障监控参数（RMV-CELLMULFAULTTHD）_35065901.md`
- 原始手册：`evidence/UDG/20.15.2/增加进程频繁故障监控参数（ADD-CELLMULFAULTTHD）_35065893.md`
- 原始手册：`evidence/UDG/20.15.2/查询进程频繁故障监控参数（LST-CELLMULFAULTTHD）_35065897.md`
