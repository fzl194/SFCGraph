---
id: UNC@20.15.2@ConfigObject@DISKCHKPARA
type: ConfigObject
name: DISKCHKPARA（存储检测参数）
nf: UNC
version: 20.15.2
object_name: DISKCHKPARA
object_kind: global_setting
status: active
---

# DISKCHKPARA（存储检测参数）

## 说明

![](设置存储检测参数（SET DISKCHKPARA）_80543423.assets/notice_3.0-zh-cn_2.png)

该命令为高危命令，须由运维人员设置，另外，dd读写速率，IO时延需根据环境的实际情况进行填写。

本命令用于手动设置部署的节点当前磁盘检测的参数。

- 若需要设置所有节点的磁盘检测参数，需要输入“网元ID”并选择“设置存储检测类型”。
- 若需要设置指定节点的磁盘检测参数，需要输入“网元ID”和“节点名称”，并选择“设置存储检测类型”。

> **说明**
> 该命令仅在Full-stack虚机场景下支持。

## 操作本对象的命令

- [[command/UNC/20.15.2/DSP-DISKCHKPARA]] · DSP DISKCHKPARA
- [[command/UNC/20.15.2/SET-DISKCHKPARA]] · SET DISKCHKPARA

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询存储检测参数（DSP-DISKCHKPARA）_80543422.md`
- 原始手册：`evidence/UNC/20.15.2/设置存储检测参数（SET-DISKCHKPARA）_80543423.md`
