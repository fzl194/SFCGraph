---
id: UNC@20.15.2@ConfigObject@IFSTATUS
type: ConfigObject
name: IFSTATUS（接口状态信息）
nf: UNC
version: 20.15.2
object_name: IFSTATUS
object_kind: query_target
status: active
---

# IFSTATUS（接口状态信息）

## 说明

在监控接口的状态或检查接口的故障原因时，可执行该命令获取接口的状态信息。用户可以根据这些信息进行流量统计和接口的故障诊断等。

若不指定IFNAME参数时，则显示所有接口的状态信息；若指定IFNAME参数时，则可以显示指定接口的状态信息。

## 操作本对象的命令

- [[command/UNC/20.15.2/DSP-IFSTATUS]] · DSP IFSTATUS

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询接口状态信息（DSP-IFSTATUS）_49960906.md`
