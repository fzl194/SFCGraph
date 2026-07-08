---
id: UNC@20.15.2@ConfigObject@PCFSSCOPEBIND
type: ConfigObject
name: PCFSSCOPEBIND（PCF业务服务区的绑定关系）
nf: UNC
version: 20.15.2
object_name: PCFSSCOPEBIND
object_kind: binding
applicable_nf:
- SMF
- PGW-C
- GGSN
status: active
---

# PCFSSCOPEBIND（PCF业务服务区的绑定关系）

## 说明

**适用NF：SMF、PGW-C、GGSN**

该命令用于增加PCF业务服务区与用户基本信息（如用户TAI区域）的绑定关系。其中，PCF业务服务区通过ADD PCFSSCOPE增加配置。当语音用户通过N7口发起会话建立请求时，可根据该绑定关系映射PCF业务服务区，从而选择可用PCF。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-PCFSSCOPEBIND]] · ADD PCFSSCOPEBIND
- [[command/UNC/20.15.2/LST-PCFSSCOPEBIND]] · LST PCFSSCOPEBIND
- [[command/UNC/20.15.2/MOD-PCFSSCOPEBIND]] · MOD PCFSSCOPEBIND
- [[command/UNC/20.15.2/RMV-PCFSSCOPEBIND]] · RMV PCFSSCOPEBIND

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改PCF业务服务区的绑定关系（MOD-PCFSSCOPEBIND）_88697036.md`
- 原始手册：`evidence/UNC/20.15.2/删除PCF业务服务区的绑定关系（RMV-PCFSSCOPEBIND）_88377450.md`
- 原始手册：`evidence/UNC/20.15.2/增加PCF业务服务区的绑定关系（ADD-PCFSSCOPEBIND）_88537090.md`
- 原始手册：`evidence/UNC/20.15.2/查询PCF业务服务区的绑定关系（LST-PCFSSCOPEBIND）_88377444.md`
