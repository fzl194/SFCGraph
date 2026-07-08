---
id: UNC@20.15.2@ConfigObject@SECPOLICYPRIO
type: ConfigObject
name: SECPOLICYPRIO（报文上送优先级）
nf: UNC
version: 20.15.2
object_name: SECPOLICYPRIO
object_kind: global_setting
status: active
---

# SECPOLICYPRIO（报文上送优先级）

## 说明

该命令用来配置报文上送优先级。

当上送CPU的报文队列满时，为保护CPU，可以设置报文上送CPU的优先级，优先上送高优先级的报文。

缺省情况下，上送报文的优先级各不相同，可以使用DSP SECCARINFO命令查看。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-SECPOLICYPRIO]] · LST SECPOLICYPRIO
- [[command/UNC/20.15.2/SET-SECPOLICYPRIO]] · SET SECPOLICYPRIO

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询报文上送优先级（LST-SECPOLICYPRIO）_49960882.md`
- 原始手册：`evidence/UNC/20.15.2/设置报文上送优先级（SET-SECPOLICYPRIO）_00601093.md`
