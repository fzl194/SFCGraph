---
id: UNC@20.15.2@ConfigObject@PAECHECKTHD
type: ConfigObject
name: PAECHECKTHD（PAE寻呼反压流控检测阈值）
nf: UNC
version: 20.15.2
object_name: PAECHECKTHD
object_kind: global_setting
applicable_nf:
- MME
- AMF
status: active
---

# PAECHECKTHD（PAE寻呼反压流控检测阈值）

## 说明

**适用NF：MME、AMF**

该命令用于设置LINK节点相关资源过载检测阈值参数，包括link-pod内pBuf资源使用率过载、恢复门限，PAE与虚拟交换机间消息发送队列使用率过载、恢复门限等信息。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-PAECHECKTHD]] · LST PAECHECKTHD
- [[command/UNC/20.15.2/SET-PAECHECKTHD]] · SET PAECHECKTHD

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询PAE寻呼反压流控检测阈值(LST-PAECHECKTHD)_13911930.md`
- 原始手册：`evidence/UNC/20.15.2/设置PAE寻呼反压流控检测阈值(SET-PAECHECKTHD)_13751952.md`
