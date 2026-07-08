---
id: UNC@20.15.2@ConfigObject@VLROFFLOADINF
type: ConfigObject
name: VLROFFLOADINF（VLR迁移配置信息）
nf: UNC
version: 20.15.2
object_name: VLROFFLOADINF
object_kind: global_setting
applicable_nf:
- SGSN
- MME
status: active
---

# VLROFFLOADINF（VLR迁移配置信息）

## 说明

**适用网元：SGSN、MME**

该命令用于设置与本局 UNC 相连的MSC POOL中VLR的迁移配置信息。

- 当MSC Pool中某个MSC/VLR不可用时（如发生故障、升级等），可以下发[**STR VLROFFLOAD**](../VLR迁移任务/启动VLR迁移任务(STR VLROFFLOAD)_26145420.md)启动迁移命令，UNC将该MSC/VLR的状态信息标识为不可用，系统将该MSC/VLR上的用户手动迁移到MSC Pool中的其他MSC/VLR上。
- 当BSC/RNC设备从一个MSC POOL下割接到另一个MSC POOL下时，执行[**STR VLROFFLOADBYLAI**](../基于LAI的IMSI分离业务/启动IMSI分离4G用户任务(STR VLROFFLOADBYLAI)_26305240.md)启动IMSI分离4G用户任务，系统根据本命令中的“第二阶段迁移速度(个/秒)”配置值对该LAI对应的TAI下面联合附着的4G用户执行IMSI分离操作，促使UE注册到新的MSC。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-VLROFFLOADINF]] · LST VLROFFLOADINF
- [[command/UNC/20.15.2/SET-VLROFFLOADINF]] · SET VLROFFLOADINF

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询VLR迁移配置信息(LST-VLROFFLOADINF)_26145422.md`
- 原始手册：`evidence/UNC/20.15.2/设置VLR迁移配置信息(SET-VLROFFLOADINF)_72345023.md`
