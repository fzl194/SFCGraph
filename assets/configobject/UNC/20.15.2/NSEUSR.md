---
id: UNC@20.15.2@ConfigObject@NSEUSR
type: ConfigObject
name: NSEUSR（NSE列表下的用户）
nf: UNC
version: 20.15.2
object_name: NSEUSR
object_kind: entity
applicable_nf:
- SGSN
status: active
---

# NSEUSR（NSE列表下的用户）

## 说明

![](删除NSE列表下的用户(RMV NSEUSR)_26305832.assets/notice_3.0-zh-cn_2.png)

- 删除任务一旦启动后无法强行终止。
- 该操作会删除指定NSE列表下的所有用户，导致这些用户被强制下线，请谨慎操作。

**适用网元：SGSN**

启动删除任务，删除 [**ADD NSELST**](增加NSE列表(ADD NSELST)_72345621.md) NSE列表下所有的用户。该命令执行后，系统启动任务，逐个扫描NSE列表中的所有NSEI，分离系统中属于这些NSE的用户。

## 操作本对象的命令

- [[command/UNC/20.15.2/DSP-NSEUSR]] · DSP NSEUSR
- [[command/UNC/20.15.2/RMV-NSEUSR]] · RMV NSEUSR

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除NSE列表下的用户(RMV-NSEUSR)_26305832.md`
- 原始手册：`evidence/UNC/20.15.2/显示删除NSE列表下的用户任务运行状态(DSP-NSEUSR)_72345623.md`
