---
id: UNC@20.15.2@ConfigObject@CANDIDATEAMF
type: ConfigObject
name: CANDIDATEAMF（候选AMF）
nf: UNC
version: 20.15.2
object_name: CANDIDATEAMF
object_kind: entity
applicable_nf:
- NSSF
status: active
---

# CANDIDATEAMF（候选AMF）

## 说明

**适用NF：NSSF**

本命令用于配置候选AMF，建立AMF与AMFSET的关联关系。通过SET NSSFFUNCPARA命令将切片选择流程中给NF返回的信元配置为CandidateAmfList时，需要配置此命令。

## 操作本对象的命令

- [ADD CANDIDATEAMF](command/UNC/20.15.2/ADD-CANDIDATEAMF.md)
- [LST CANDIDATEAMF](command/UNC/20.15.2/LST-CANDIDATEAMF.md)
- [MOD CANDIDATEAMF](command/UNC/20.15.2/MOD-CANDIDATEAMF.md)
- [RMV CANDIDATEAMF](command/UNC/20.15.2/RMV-CANDIDATEAMF.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改候选AMF（MOD-CANDIDATEAMF）_18715635.md`
- 原始手册：`evidence/UNC/20.15.2/删除候选AMF（RMV-CANDIDATEAMF）_18715637.md`
- 原始手册：`evidence/UNC/20.15.2/增加候选AMF（ADD-CANDIDATEAMF）_18715631.md`
- 原始手册：`evidence/UNC/20.15.2/查询候选AMF（LST-CANDIDATEAMF）_18715633.md`
