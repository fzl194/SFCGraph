---
id: UNC@20.15.2@ConfigObject@PCFSSCOPE
type: ConfigObject
name: PCFSSCOPE（PCF的业务服务区）
nf: UNC
version: 20.15.2
object_name: PCFSSCOPE
object_kind: entity
applicable_nf:
- SMF
- PGW-C
- GGSN
status: active
---

# PCFSSCOPE（PCF的业务服务区）

## 说明

**适用NF：SMF、PGW-C、GGSN**

该命令用于增加PCF的业务服务区配置。语音用户通过N7口向PCF请求策略时，可通过服务区名称选择可用PCF。具体过程如下：PCF向NRF注册时携带其服务区名称。会话建立阶段，SMF通过语音用户TAI区域查询配置PCFSSCOPEBIND得到对应的服务区标识，再通过本配置匹配到对应的服务区名称，并携带该服务区名称向NRF查询可用PCF，从而发起会话建立请求。

## 操作本对象的命令

- [ADD PCFSSCOPE](command/UNC/20.15.2/ADD-PCFSSCOPE.md)
- [LST PCFSSCOPE](command/UNC/20.15.2/LST-PCFSSCOPE.md)
- [MOD PCFSSCOPE](command/UNC/20.15.2/MOD-PCFSSCOPE.md)
- [RMV PCFSSCOPE](command/UNC/20.15.2/RMV-PCFSSCOPE.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改PCF的业务服务区（MOD-PCFSSCOPE）_88537102.md`
- 原始手册：`evidence/UNC/20.15.2/删除PCF的业务服务区（RMV-PCFSSCOPE）_35273629.md`
- 原始手册：`evidence/UNC/20.15.2/增加PCF的业务服务区（ADD-PCFSSCOPE）_35636447.md`
- 原始手册：`evidence/UNC/20.15.2/查询PCF的业务服务区（LST-PCFSSCOPE）_35273623.md`
