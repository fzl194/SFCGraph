---
id: UNC@20.15.2@ConfigObject@ISSUDIALTEST
type: ConfigObject
name: ISSUDIALTEST（拨测用户配置）
nf: UNC
version: 20.15.2
object_name: ISSUDIALTEST
object_kind: entity
applicable_nf:
- SGSN
- MME
status: active
---

# ISSUDIALTEST（拨测用户配置）

## 说明

**适用网元：SGSN、MME**

- 该命令用于新增拨测用户列表，通过起始IMSI/MSISDN和终止IMSI/MSISDN的方式，配置一组拨测用户。
- 在灰度升级场景下，符合拨测条件的用户，在附着过程中会被接入新版本的USN_VNFC，以便对新版本的USN_VNFC功能进行测试。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-ISSUDIALTEST]] · ADD ISSUDIALTEST
- [[command/UNC/20.15.2/LST-ISSUDIALTEST]] · LST ISSUDIALTEST
- [[command/UNC/20.15.2/RMV-ISSUDIALTEST]] · RMV ISSUDIALTEST

## 证据

- 原始手册：`evidence/UNC/20.15.2/ISSUDIALTEST.md`
- 原始手册：`evidence/UNC/20.15.2/ISSUDIALTEST.md`
- 原始手册：`evidence/UNC/20.15.2/ISSUDIALTEST.md`
