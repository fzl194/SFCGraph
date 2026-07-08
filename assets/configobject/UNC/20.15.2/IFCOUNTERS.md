---
id: UNC@20.15.2@ConfigObject@IFCOUNTERS
type: ConfigObject
name: IFCOUNTERS（接口统计信息）
nf: UNC
version: 20.15.2
object_name: IFCOUNTERS
object_kind: action
status: active
---

# IFCOUNTERS（接口统计信息）

## 说明

在监控接口的状态或检查接口的故障原因时，可执行该命令获取接口的统计信息。用户可以根据这些信息进行流量统计和接口的故障诊断等。

若不指定IFNAME参数时，则显示所有接口的统计信息；若指定IFNAME参数时，则可以显示指定接口的统计信息。

## 操作本对象的命令

- [DSP IFCOUNTERS](command/UNC/20.15.2/DSP-IFCOUNTERS.md)
- [RTR IFCOUNTERS](command/UNC/20.15.2/RTR-IFCOUNTERS.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询接口统计信息（DSP-IFCOUNTERS）_00841557.md`
- 原始手册：`evidence/UNC/20.15.2/清除接口统计信息（RTR-IFCOUNTERS）_00866745.md`
