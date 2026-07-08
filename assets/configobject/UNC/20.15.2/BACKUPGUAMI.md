---
id: UNC@20.15.2@ConfigObject@BACKUPGUAMI
type: ConfigObject
name: BACKUPGUAMI（供备GUAMI信息）
nf: UNC
version: 20.15.2
object_name: BACKUPGUAMI
object_kind: entity
applicable_nf:
- AMF
status: active
---

# BACKUPGUAMI（供备GUAMI信息）

## 说明

**适用NF：AMF**

在5G核心网中，一个AMF逻辑上可以划分为多个实体，分别通过不同的GUAMI进行标识，并且支持以GUAMI为粒度选择Pool内其它AMF作为备用AMF。所谓备用AMF，即当前正在使用的AMF发生故障或者从网络中计划性退服时，可以接续主用AMF当前承载业务的AMF。

每个GUAMI的备用AMF可通过ADD GUAMI进行指定。本AMF可被哪些GUAMI用作备用AMF，则通过本命令配置。将本AMF用作备用AMF的GUAMI列表需要在本AMF的注册流程中带给NRF。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-BACKUPGUAMI]] · ADD BACKUPGUAMI
- [[command/UNC/20.15.2/LST-BACKUPGUAMI]] · LST BACKUPGUAMI
- [[command/UNC/20.15.2/MOD-BACKUPGUAMI]] · MOD BACKUPGUAMI
- [[command/UNC/20.15.2/RMV-BACKUPGUAMI]] · RMV BACKUPGUAMI

## 证据

- 原始手册：`evidence/UNC/20.15.2/BACKUPGUAMI.md`
- 原始手册：`evidence/UNC/20.15.2/BACKUPGUAMI.md`
- 原始手册：`evidence/UNC/20.15.2/BACKUPGUAMI.md`
- 原始手册：`evidence/UNC/20.15.2/BACKUPGUAMI.md`
