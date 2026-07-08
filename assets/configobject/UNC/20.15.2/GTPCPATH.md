---
id: UNC@20.15.2@ConfigObject@GTPCPATH
type: ConfigObject
name: GTPCPATH（GTP-C路径）
nf: UNC
version: 20.15.2
object_name: GTPCPATH
object_kind: entity
applicable_nf:
- SGSN
- MME
status: active
---

# GTPCPATH（GTP-C路径）

## 说明

**适用网元：SGSN、MME**

该命令用于删除GTP-C信令面路径。

通常在当前路径的GTP版本与对端GSN实际支持的最高GTP版本不一致，希望重新创建GTP路径时会执行删除GTP路径的动作，比如对端GSN实际最高支持GTP V1版本，但由于通讯等原因，本端GSN在探测对端支持的GTP版本时，有可能误判为GTP V0版本，则以后所有由本端GSN发起的信令流程，都会使用GTP V0版本与对端进行通讯，尽管本端GSN有路径版本定时核查机制，但如果想立刻重新探测对端GSN支持的最高GTP协议版本，需要删除GTP-C路径。

## 操作本对象的命令

- [DSP GTPCPATH](command/UNC/20.15.2/DSP-GTPCPATH.md)
- [RMV GTPCPATH](command/UNC/20.15.2/RMV-GTPCPATH.md)
- [TST GTPCPATH](command/UNC/20.15.2/TST-GTPCPATH.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除GTP-C路径(RMV-GTPCPATH)_72345511.md`
- 原始手册：`evidence/UNC/20.15.2/显示GTP-C路径(DSP-GTPCPATH)_72225591.md`
- 原始手册：`evidence/UNC/20.15.2/测试GTP-C路径(TST-GTPCPATH)_26145912.md`
