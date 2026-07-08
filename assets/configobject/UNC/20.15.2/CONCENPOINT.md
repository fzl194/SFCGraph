---
id: UNC@20.15.2@ConfigObject@CONCENPOINT
type: ConfigObject
name: CONCENPOINT（集中点部署模式）
nf: UNC
version: 20.15.2
object_name: CONCENPOINT
object_kind: global_setting
applicable_nf:
- PGW-C
- SMF
status: active
---

# CONCENPOINT（集中点部署模式）

## 说明

**适用NF：PGW-C、SMF**

![](设置集中点部署模式（SET CONCENPOINT）_09896704.assets/notice_3.0-zh-cn_2.png)

本命令属于高危命令，修改集中点模式可能导致Diameter链路重建或中断，进而影响用户使用业务，比如用户被去活等。涉及Diameter链路的接口为Gx、Gy、S6b接口。

此命令用于设置信令集中点的部署模式。

## 操作本对象的命令

- [LST CONCENPOINT](command/UNC/20.15.2/LST-CONCENPOINT.md)
- [SET CONCENPOINT](command/UNC/20.15.2/SET-CONCENPOINT.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询集中点部署模式（LST-CONCENPOINT）_09896705.md`
- 原始手册：`evidence/UNC/20.15.2/设置集中点部署模式（SET-CONCENPOINT）_09896704.md`
