---
id: UNC@20.15.2@ConfigObject@CNTTMPDIR
type: ConfigObject
name: CNTTMPDIR（容器引擎临时目录）
nf: UNC
version: 20.15.2
object_name: CNTTMPDIR
object_kind: global_setting
status: active
---

# CNTTMPDIR（容器引擎临时目录）

## 说明

![](设置容器引擎临时目录（SET CNTTMPDIR）_89151642.assets/notice_3.0-zh-cn_2.png)

该命令为高危命令，此命令会修改容器引擎临时目录并复位容器引擎，可能出现容器引擎启动失败或容器引擎启动过程中业务中断，最终导致业务受损，请务必在华为技术支持人员的指导下使用该命令。

该命令用于设置节点的容器引擎临时目录。

> **说明**
> 该命令仅在 Full-stack 虚机场景下支持。

## 操作本对象的命令

- [DSP CNTTMPDIR](command/UNC/20.15.2/DSP-CNTTMPDIR.md)
- [SET CNTTMPDIR](command/UNC/20.15.2/SET-CNTTMPDIR.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询容器引擎临时目录（DSP-CNTTMPDIR）_88993080.md`
- 原始手册：`evidence/UNC/20.15.2/设置容器引擎临时目录（SET-CNTTMPDIR）_89151642.md`
