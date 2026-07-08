---
id: UNC@20.15.2@ConfigObject@REGNFLOADUPDTHR
type: ConfigObject
name: REGNFLOADUPDTHR（NF负载更新阈值）
nf: UNC
version: 20.15.2
object_name: REGNFLOADUPDTHR
object_kind: global_setting
applicable_nf:
- NRF
status: active
---

# REGNFLOADUPDTHR（NF负载更新阈值）

## 说明

**适用NF：NRF**

当运营商希望设置不同于初始设置的NF负载更新阈值时，可使用此命令。

当NF相邻两次上报的负载差值超过负载更新阈值时，NRF会对NF的负载更新成最新上报的负载，并通知订阅该负载信息的NF实例。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-REGNFLOADUPDTHR]] · LST REGNFLOADUPDTHR
- [[command/UNC/20.15.2/SET-REGNFLOADUPDTHR]] · SET REGNFLOADUPDTHR

## 证据

- 原始手册：`evidence/UNC/20.15.2/REGNFLOADUPDTHR.md`
- 原始手册：`evidence/UNC/20.15.2/REGNFLOADUPDTHR.md`
