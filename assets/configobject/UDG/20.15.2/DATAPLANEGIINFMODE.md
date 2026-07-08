---
id: UDG@20.15.2@ConfigObject@DATAPLANEGIINFMODE
type: ConfigObject
name: DATAPLANEGIINFMODE（用户面下行模式配置）
nf: UDG
version: 20.15.2
object_name: DATAPLANEGIINFMODE
object_kind: global_setting
applicable_nf:
- PGW-U
- UPF
status: active
---

# DATAPLANEGIINFMODE（用户面下行模式配置）

## 说明

**适用NF：PGW-U、UPF**

![](设置用户面下行模式（SET DATAPLANEGIINFMODE）_76796630.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，配置此命令时需要检查当前的POD Type是否是ISU/APU POD， 如果不是，不能开启入不转板功能。

设置数据面接口模式，包含Gi、N6、SGi等接口的模式。

## 操作本对象的命令

- [[command/UDG/20.15.2/LST-DATAPLANEGIINFMODE]] · LST DATAPLANEGIINFMODE
- [[command/UDG/20.15.2/SET-DATAPLANEGIINFMODE]] · SET DATAPLANEGIINFMODE

## 证据

- 原始手册：`evidence/UDG/20.15.2/DATAPLANEGIINFMODE.md`
- 原始手册：`evidence/UDG/20.15.2/DATAPLANEGIINFMODE.md`
