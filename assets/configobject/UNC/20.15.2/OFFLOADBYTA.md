---
id: UNC@20.15.2@ConfigObject@OFFLOADBYTA
type: ConfigObject
name: OFFLOADBYTA（TA迁移任务）
nf: UNC
version: 20.15.2
object_name: OFFLOADBYTA
object_kind: action
applicable_nf:
- MME
status: active
---

# OFFLOADBYTA（TA迁移任务）

## 说明

**适用网元：MME**

此命令用于启动基于TA的迁移任务。

当LTE网络需做调整时，如将MME下的一个或几个TA的用户割接至其它MME时，可使用此命令启动基于TA的迁移任务。此命令一次性最多指定10个TAI启动迁移任务。

启动基于TA的迁移任务前，需要手动通过 **[ADD MMECAPBYTA](../../S1接口管理/基于跟踪区的MME相对权重/增加基于跟踪区的MME相对权重配置(ADD MMECAPBYTA)_72345865.md)** 或者 **[MOD MMECAPBYTA](../../S1接口管理/基于跟踪区的MME相对权重/修改基于跟踪区的MME相对权重配置(MOD MMECAPBYTA)_26146266.md)** 配置指定TA下，本MME的MME负荷能力在MME Pool区内的相对权重值为0。结束基于TA的迁移任务后，期望指定的TA下的eNodeB的用户仍可以接入本MME时，需要通过 **[RMV MMECAPBYTA](../../S1接口管理/基于跟踪区的MME相对权重/删除基于跟踪区的MME相对权重配置(RMV MMECAPBYTA)_72225945.md)** 或者 **[MOD MMECAPBYTA](../../S1接口管理/基于跟踪区的MME相对权重/修改基于跟踪区的MME相对权重配置(MOD MMECAPBYTA)_26146266.md)** 配置指定TA下，本MME的MME负荷能力在MME Pool区内的相对权重值为迁移前的权重值。期望抑制指定TA下的eNodeB的用户长时间不接入本MME时，需要保持MMECAPBYTA配置不变（指定TA下本MME的MME负荷能力在MME Pool区内的相对权重值为0）。

## 操作本对象的命令

- [STR OFFLOADBYTA](command/UNC/20.15.2/STR-OFFLOADBYTA.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/启动TA迁移任务（STR-OFFLOADBYTA）_02884717.md`
