---
id: UNC@20.15.2@ConfigObject@DNSERRDN
type: ConfigObject
name: DNSERRDN（失败的DNS记录）
nf: UNC
version: 20.15.2
object_name: DNSERRDN
object_kind: query_target
applicable_nf:
- SGSN
- MME
status: active
---

# DNSERRDN（失败的DNS记录）

## 说明

**适用网元：SGSN、MME**

该命令用于查询 UNC 检查出的DNS错误域名信息。导致这些错误的原因包括DNS服务器配置错误、配置不完整等。当 UNC 检测出有DNS查询失败时，会将相关信息记录在系统中，使用该命令可以查询出相关错误信息；当 UNC 检测出DNS查询成功后，再将相关错误信息从系统中清除。

## 操作本对象的命令

- [DSP DNSERRDN](command/UNC/20.15.2/DSP-DNSERRDN.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询失败的DNS记录(DSP-DNSERRDN)_26305692.md`
