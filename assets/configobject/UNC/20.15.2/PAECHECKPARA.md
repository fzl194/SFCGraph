---
id: UNC@20.15.2@ConfigObject@PAECHECKPARA
type: ConfigObject
name: PAECHECKPARA（PAE寻呼反压流控检测参数）
nf: UNC
version: 20.15.2
object_name: PAECHECKPARA
object_kind: global_setting
applicable_nf:
- MME
- AMF
status: active
---

# PAECHECKPARA（PAE寻呼反压流控检测参数）

## 说明

**适用NF：MME、AMF**

该命令用于设置LINK节点相关资源过载检测参数，包括link-pod内pBuf资源和PAE与虚拟交换机间消息发送队列所使用的检测周期、检测次数等信息。

## 操作本对象的命令

- [LST PAECHECKPARA](command/UNC/20.15.2/LST-PAECHECKPARA.md)
- [SET PAECHECKPARA](command/UNC/20.15.2/SET-PAECHECKPARA.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询PAE寻呼反压流控检测参数(LST-PAECHECKPARA)_58391837.md`
- 原始手册：`evidence/UNC/20.15.2/设置PAE寻呼反压流控检测参数(SET-PAECHECKPARA)_14231878.md`
