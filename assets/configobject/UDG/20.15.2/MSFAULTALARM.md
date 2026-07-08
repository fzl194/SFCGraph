---
id: UDG@20.15.2@ConfigObject@MSFAULTALARM
type: ConfigObject
name: MSFAULTALARM（告警开关配置数据）
nf: UDG
version: 20.15.2
object_name: MSFAULTALARM
object_kind: global_setting
status: active
---

# MSFAULTALARM（告警开关配置数据）

## 说明

该命令功能不可用，"ALM-100001进程故障告警"是否抑制及抑制时长，请使用OM Portal上“告警配置”进行相关抑制配置操作。

> **说明**
> - 该命令执行后立即生效。
>
> - 当前版本配置此命令不生效。
> - 默认进程故障持续超过告警抑制时间上报ALM-100001 进程故障告警，如果关闭告警抑制开关，则此告警立即上报。
>
> - 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：
>
> | SUPPRESSENABLE | SUPPRESSTIME |
> | --- | --- |
> | TRUE | 300 |

## 操作本对象的命令

- [LST MSFAULTALARM](command/UDG/20.15.2/LST-MSFAULTALARM.md)
- [SET MSFAULTALARM](command/UDG/20.15.2/SET-MSFAULTALARM.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询告警开关配置数据（LST-MSFAULTALARM）_09587938.md`
- 原始手册：`evidence/UDG/20.15.2/设置告警开关（SET-MSFAULTALARM）_09587862.md`
