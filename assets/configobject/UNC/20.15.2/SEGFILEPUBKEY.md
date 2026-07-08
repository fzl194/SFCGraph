---
id: UNC@20.15.2@ConfigObject@SEGFILEPUBKEY
type: ConfigObject
name: SEGFILEPUBKEY（号段配置文件的签名验证公钥）
nf: UNC
version: 20.15.2
object_name: SEGFILEPUBKEY
object_kind: entity
applicable_nf:
- NRF
status: active
---

# SEGFILEPUBKEY（号段配置文件的签名验证公钥）

## 说明

**适用NF：NRF**

该命令用于在NRF上新增号段配置文件的签名验证公钥。

当使用号段文件导入到NRF这种方式来配置号段数据前，为了保证文件完整性安全，需要给号段文件配置签名验证公钥。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-SEGFILEPUBKEY]] · ADD SEGFILEPUBKEY
- [[command/UNC/20.15.2/LST-SEGFILEPUBKEY]] · LST SEGFILEPUBKEY
- [[command/UNC/20.15.2/RMV-SEGFILEPUBKEY]] · RMV SEGFILEPUBKEY

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除号段配置文件的签名验证公钥（RMV-SEGFILEPUBKEY）_09652232.md`
- 原始手册：`evidence/UNC/20.15.2/增加号段配置文件的签名验证公钥（ADD-SEGFILEPUBKEY）_09652608.md`
- 原始手册：`evidence/UNC/20.15.2/查询号段配置文件的签名验证公钥（LST-SEGFILEPUBKEY）_09653001.md`
