---
id: UNC@20.15.2@ConfigObject@NRFREFRESHNF
type: ConfigObject
name: NRFREFRESHNF（操作执行网元信息刷新）
nf: UNC
version: 20.15.2
object_name: NRFREFRESHNF
object_kind: action
applicable_nf:
- NRF
status: active
---

# NRFREFRESHNF（操作执行网元信息刷新）

## 说明

**适用NF：NRF**

该命令用于对NF的心跳请求强制返回404响应，指示NF到NRF上进行全量更新，达到刷NF信息的目的。执行完该命令后NRF会对NF下一周期的心跳请求返回404，NF收到404响应后是否进行全量更新取决于NF的实现。此命令执行结果通过DSP NRFREFRESHNF查询。

## 操作本对象的命令

- [[command/UNC/20.15.2/CLR-NRFREFRESHNF]] · CLR NRFREFRESHNF
- [[command/UNC/20.15.2/DSP-NRFREFRESHNF]] · DSP NRFREFRESHNF
- [[command/UNC/20.15.2/OPR-NRFREFRESHNF]] · OPR NRFREFRESHNF

## 证据

- 原始手册：`evidence/UNC/20.15.2/NRFREFRESHNF.md`
- 原始手册：`evidence/UNC/20.15.2/NRFREFRESHNF.md`
- 原始手册：`evidence/UNC/20.15.2/NRFREFRESHNF.md`
