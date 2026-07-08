---
id: UNC@20.15.2@ConfigObject@ACTRL
type: ConfigObject
name: ACTRL（接入控制）
nf: UNC
version: 20.15.2
object_name: ACTRL
object_kind: entity
applicable_nf:
- NCG
status: active
---

# ACTRL（接入控制）

## 说明

**适用NF：NCG**

该命令用于增加接入控制模块采用的IP地址和端口号。本网元的接入控制功能，由资源管理模块RCM（Resource Control Management）和全局控制模块GACM（Global Access Control Module）共同完成。它的功能是通过与话单产生网元协商，将其发送的话单分配到网元不同的接入网元分组上进行处理，平衡负载，提高可靠性。

PS域网元的IP和端口号要根据实际配置。

## 操作本对象的命令

- [ADD ACTRL](command/UNC/20.15.2/ADD-ACTRL.md)
- [CHK ACTRL](command/UNC/20.15.2/CHK-ACTRL.md)
- [DSP ACTRL](command/UNC/20.15.2/DSP-ACTRL.md)
- [LST ACTRL](command/UNC/20.15.2/LST-ACTRL.md)
- [MOD ACTRL](command/UNC/20.15.2/MOD-ACTRL.md)
- [RMV ACTRL](command/UNC/20.15.2/RMV-ACTRL.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改接入控制（MOD-ACTRL）_51174234.md`
- 原始手册：`evidence/UNC/20.15.2/删除接入控制（RMV-ACTRL）_51174233.md`
- 原始手册：`evidence/UNC/20.15.2/增加接入控制（ADD-ACTRL）_51174232.md`
- 原始手册：`evidence/UNC/20.15.2/显示CGF与对端网元链路状态（DSP-ACTRL）_51174236.md`
- 原始手册：`evidence/UNC/20.15.2/查询接入控制（LST-ACTRL）_51174235.md`
- 原始手册：`evidence/UNC/20.15.2/检查链路分配信息（CHK-ACTRL）_51174237.md`
