---
id: UDG@20.15.2@ConfigObject@CPUECOPOLICY
type: ConfigObject
name: CPUECOPOLICY（全局的CPU调频和休眠策略）
nf: UDG
version: 20.15.2
object_name: CPUECOPOLICY
object_kind: global_setting
status: active
---

# CPUECOPOLICY（全局的CPU调频和休眠策略）

## 说明

使用虚拟机CPU节能功能时，通过此命令可以设置全局的虚拟机CPU调频和休眠策略：

- 虚拟机的CPU调频策略，是指允许虚拟机根据CPU核的负载状态自动地调节CPU核的运行频率，达到在低负载时节约能源的目的。
- 虚拟机的CPU休眠策略，是指当CPU核在较长时间（秒级）没有中断请求时，允许虚拟机进入休眠状态，以获得更多的节能效果。
  CPU休眠的深浅程度，表示CPU核参与休眠的部件范围大小，影响节能效果。是否支持休眠和参与休眠的部件范围与CPU类型和BIOS设置有关，休眠部件一般包括软件时钟、频率、缓存等。例如，ARM CPU不支持CPU休眠；X86 CPU支持浅休眠、深休眠；X86浅休眠主要包括软件时钟挂起/待机、降低倍频和电压，深休眠还包括清除L1/L2缓存等。一般来说，深休眠的节能效果比浅休眠好，不过CPU核从深休眠状态唤醒的所需时间要比浅休眠略长。

> **说明**
> 该命令仅在Full-stack虚机场景下支持。

## 操作本对象的命令

- [[command/UDG/20.15.2/LST-CPUECOPOLICY]] · LST CPUECOPOLICY
- [[command/UDG/20.15.2/SET-CPUECOPOLICY]] · SET CPUECOPOLICY

## 证据

- 原始手册：`evidence/UDG/20.15.2/CPUECOPOLICY.md`
- 原始手册：`evidence/UDG/20.15.2/CPUECOPOLICY.md`
