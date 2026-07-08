---
id: UDG@20.15.2@ConfigObject@PODALMTH
type: ConfigObject
name: PODALMTH（POD资源告警阈值）
nf: UDG
version: 20.15.2
object_name: PODALMTH
object_kind: entity
status: active
---

# PODALMTH（POD资源告警阈值）

## 说明

该命令用于增加POD资源告警阈值。

该命令的使用场景：POD根据本命令配置的阈值上报和恢复ALM-100441 POD CPU过载告警、ALM-100442 POD内存过载告警。

> **说明**
> - 该命令执行后立即生效。
>
> - 该命令仅在FusionStage裸机场景下生效。
>
> - 最多可输入65535条记录。

## 操作本对象的命令

- [ADD PODALMTH](command/UDG/20.15.2/ADD-PODALMTH.md)
- [LST PODALMTH](command/UDG/20.15.2/LST-PODALMTH.md)
- [MOD PODALMTH](command/UDG/20.15.2/MOD-PODALMTH.md)
- [RMV PODALMTH](command/UDG/20.15.2/RMV-PODALMTH.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改POD资源告警阈值（MOD-PODALMTH）_87324062.md`
- 原始手册：`evidence/UDG/20.15.2/删除POD资源告警阈值（RMV-PODALMTH）_35442893.md`
- 原始手册：`evidence/UDG/20.15.2/增加POD资源告警阈值（ADD-PODALMTH）_87483778.md`
- 原始手册：`evidence/UDG/20.15.2/查询POD资源告警阈值（LST-PODALMTH）_35442889.md`
