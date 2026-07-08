---
id: UDG@20.15.2@ConfigObject@DATAPLANEINFMODE
type: ConfigObject
name: DATAPLANEINFMODE（数据面接口模式）
nf: UDG
version: 20.15.2
object_name: DATAPLANEINFMODE
object_kind: global_setting
applicable_nf:
- SGW-U
- PGW-U
- UPF
status: active
---

# DATAPLANEINFMODE（数据面接口模式）

## 说明

**适用NF：SGW-U、PGW-U、UPF**

![](设置用户面接口模式（SET DATAPLANEINFMODE）_06677620.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，配置此命令时需要检查当前的POD Type是否是ISU/APU POD，如果不是，不能开启入不转板功能。

设置数据面接口模式，包含的接口类型有：s5-sif，s1-uif，saif，paif，n3if，n9cif，scif，n6。

## 操作本对象的命令

- [LST DATAPLANEINFMODE](command/UDG/20.15.2/LST-DATAPLANEINFMODE.md)
- [SET DATAPLANEINFMODE](command/UDG/20.15.2/SET-DATAPLANEINFMODE.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询数据面接口模式（LST-DATAPLANEINFMODE）_07148234.md`
- 原始手册：`evidence/UDG/20.15.2/设置用户面接口模式（SET-DATAPLANEINFMODE）_06677620.md`
