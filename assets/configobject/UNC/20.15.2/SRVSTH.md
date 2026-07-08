---
id: UNC@20.15.2@ConfigObject@SRVSTH
type: ConfigObject
name: SRVSTH（业务功能开关状态）
nf: UNC
version: 20.15.2
object_name: SRVSTH
object_kind: global_setting
applicable_nf:
- NCG
status: active
---

# SRVSTH（业务功能开关状态）

## 说明

![](设置业务功能开关（SET SRVSTH）_41302357.assets/notice_3.0-zh-cn_2.png)

此命令为高危命令，如果将“GACDRRESNDCHK”或“GAMDRESNDCHK”设置为开启，可能会导致POD的CPU使用率增加。

**适用NF：NCG**

该命令用于设置业务功能开关。包括自动链路负载均衡、检查无效链路和Ga无效链路老化时长。

> **说明**
> 负载均衡开关开启后，链路均衡调整需符合以下任一条件：
>
> - 检测到某一RU上无链路；
> - 检测到某一AP上话务量超过3000cdr/s;
> - 检测到某一RU磁盘使用率达到80%;
> - 检测到RU间前存盘和后存盘的使用率之和相差超过20%。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-SRVSTH]] · LST SRVSTH
- [[command/UNC/20.15.2/SET-SRVSTH]] · SET SRVSTH

## 证据

- 原始手册：`evidence/UNC/20.15.2/SRVSTH.md`
- 原始手册：`evidence/UNC/20.15.2/SRVSTH.md`
