---
id: UNC@20.15.2@MMLCommand@STP OFFLOAD
type: MMLCommand
name: STP OFFLOAD（停止迁移任务）
nf: UNC
version: 20.15.2
verb: STP
object_keyword: OFFLOAD
command_category: 动作类
applicable_nf:
- SGSN
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 网络管理
- 迁移控制
status: active
---

# STP OFFLOAD（停止迁移任务）

## 功能

**适用网元：SGSN、MME**

此命令用于停止当前正在进行的迁移任务。

## 注意事项

- 当由[**STR OFFLOADBYMME**](启动MME迁移任务（STR OFFLOADBYMME）_72345693.md)命令启动的迁移任务结束后，如果需要MME继续接入新用户，则需通过[**SET SYS**](../../系统管理/系统参数管理/设置系统参数(SET SYS)_72345947.md)命令将MME的“设备能力”设置成对应的值。
- 当由[**STR OFFLOADBYSGSN**](启动SGSN迁移任务（STR OFFLOADBYSGSN）_26305904.md)、[**STR OFFLOADBYRNC**](启动RNC迁移任务（STR OFFLOADBYRNC）_72225773.md)、[**STR OFFLOADBYBSC**](启动BSC迁移任务（STR OFFLOADBYBSC）_72225771.md)命令启动的迁移任务结束后，如果需要本SGSN通过指定RNC/BSC继续接入新用户，则需在相应RNC/BSC上将本SGSN的状态恢复为“Normal”。
- 此命令对类型为“IMSI(IMSI)”的迁移任务不生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

无。

## 操作的配置对象

- [迁移任务（OFFLOAD）](configobject/UNC/20.15.2/OFFLOAD.md)

## 使用实例

停止迁移任务：

STP OFFLOAD:;

## 证据

- 原始手册：`evidence/UNC/20.15.2/停止迁移任务(STP-OFFLOAD)_26146092.md`
