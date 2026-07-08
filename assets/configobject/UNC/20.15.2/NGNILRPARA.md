---
id: UNC@20.15.2@ConfigObject@NGNILRPARA
type: ConfigObject
name: NGNILRPARA（NI-LR功能参数）
nf: UNC
version: 20.15.2
object_name: NGNILRPARA
object_kind: entity
applicable_nf:
- AMF
status: active
---

# NGNILRPARA（NI-LR功能参数）

## 说明

**适用NF：AMF**

该命令用于基于运营商新增NI-LR功能的参数。

Non-UE辅助定位流程中，AMF是否支持Namf_Communication_NonUeN2InfoSubscribe Request消息不携带globalRanNodeList信元受软参DWORD71 BIT7控制。

## 操作本对象的命令

- [ADD NGNILRPARA](command/UNC/20.15.2/ADD-NGNILRPARA.md)
- [LST NGNILRPARA](command/UNC/20.15.2/LST-NGNILRPARA.md)
- [MOD NGNILRPARA](command/UNC/20.15.2/MOD-NGNILRPARA.md)
- [RMV NGNILRPARA](command/UNC/20.15.2/RMV-NGNILRPARA.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改NI-LR功能参数（MOD-NGNILRPARA）_44007390.md`
- 原始手册：`evidence/UNC/20.15.2/删除NI-LR功能参数（RMV-NGNILRPARA）_44007658.md`
- 原始手册：`evidence/UNC/20.15.2/增加NI-LR功能参数（ADD-NGNILRPARA）_44006465.md`
- 原始手册：`evidence/UNC/20.15.2/查询NI-LR功能参数（LST-NGNILRPARA）_44007010.md`
