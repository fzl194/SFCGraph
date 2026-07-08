---
id: UNC@20.15.2@ConfigObject@RUFAULTTOLERANCE
type: ConfigObject
name: RUFAULTTOLERANCE（资源单元故障容忍时间）
nf: UNC
version: 20.15.2
object_name: RUFAULTTOLERANCE
object_kind: global_setting
status: active
---

# RUFAULTTOLERANCE（资源单元故障容忍时间）

## 说明

该命令用于设置资源单元故障容忍时间，包括正向容忍时间、反向容忍时间、软仲裁选主时间和软仲裁停主时间。软仲裁是用来确定两个主控资源单元节点的主备身份。

正向容忍时间是指网络断开后主控资源单元节点经过多长时间认为业务资源单元节点出现故障。反向容忍时间是指网络断开后业务资源单元节点经过多长时间复位。软仲裁选主时间是指网络断开后主控资源单元备节点变成主控资源单元主节点所消耗的时间。软仲裁停主时间是指防脑裂模式下网络断开后主控资源单元主节点经过多长时间放弃主身份。

当需要更快的感知资源单元的故障时，可以适当缩短资源单元故障容忍时间。合理的资源单元故障容忍时间既能保证及时感知资源单元的故障，又能避免因为网络闪断而造成资源单元故障的误判。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-RUFAULTTOLERANCE]] · LST RUFAULTTOLERANCE
- [[command/UNC/20.15.2/SET-RUFAULTTOLERANCE]] · SET RUFAULTTOLERANCE

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询资源单元故障容忍时间（LST-RUFAULTTOLERANCE）_35925560.md`
- 原始手册：`evidence/UNC/20.15.2/设置资源单元故障容忍时间（SET-RUFAULTTOLERANCE）_20857597.md`
