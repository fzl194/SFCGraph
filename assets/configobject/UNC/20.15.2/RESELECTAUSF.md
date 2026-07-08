---
id: UNC@20.15.2@ConfigObject@RESELECTAUSF
type: ConfigObject
name: RESELECTAUSF（重选AUSF）
nf: UNC
version: 20.15.2
object_name: RESELECTAUSF
object_kind: action
applicable_nf:
- AMF
status: active
---

# RESELECTAUSF（重选AUSF）

## 说明

**适用NF：AMF**

该命令用于触发AUSF重选流程。AMF收到该命令后会启动扫描任务，对符合重选条件的用户在后续需要鉴权的流程中重选AUSF并进行鉴权。

该命令适用于特定的AUSF发生故障或升级等场景下，AMF通过本命令触发AUSF重选功能。

## 操作本对象的命令

- [STR RESELECTAUSF](command/UNC/20.15.2/STR-RESELECTAUSF.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/启动重选AUSF（STR-RESELECTAUSF）_96766645.md`
