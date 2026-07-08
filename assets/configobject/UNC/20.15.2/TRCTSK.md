---
id: UNC@20.15.2@ConfigObject@TRCTSK
type: ConfigObject
name: TRCTSK（跟踪任务）
nf: UNC
version: 20.15.2
object_name: TRCTSK
object_kind: entity
applicable_nf:
- SGW-C
- PGW-C
- SMF
- GGSN
- AMF
status: active
---

# TRCTSK（跟踪任务）

## 说明

![](删除跟踪任务（RMV TRCTSK）_86223168.assets/notice_3.0-zh-cn_2.png)

执行该命令会导致被删除的跟踪任务不可用，请谨慎使用并联系华为技术支持协助操作。

基于跟踪类型删除跟踪任务后，会导致该跟踪类型的任务不可用，需要重新创建该类型的所有跟踪。

基于用户信息删除跟踪任务后，仅影响该用户的跟踪任务不可用，需要重新创建该用户的跟踪任务。

删除信令面创建的E2E跟踪任务时，会同时反向删除CSP的跟踪任务，并且向下游网元传递跟踪任务删除标识，会导致下游网元的跟踪任务也会被删除。

删除除信令面创建的E2E跟踪任务之外的任务时，仅删除业务侧的跟踪任务，可能会导致业务侧跟踪任务和CSP的跟踪任务不一致，因此需要先在CSP界面上删除相应的跟踪任务。

**适用NF：SGW-C、PGW-C、SMF、GGSN、AMF**

该命令用于删除跟踪任务。

## 操作本对象的命令

- [[command/UNC/20.15.2/RMV-TRCTSK]] · RMV TRCTSK

## 证据

- 原始手册：`evidence/UNC/20.15.2/TRCTSK.md`
