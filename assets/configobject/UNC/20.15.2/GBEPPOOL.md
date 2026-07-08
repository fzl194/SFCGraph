---
id: UNC@20.15.2@ConfigObject@GBEPPOOL
type: ConfigObject
name: GBEPPOOL（地址池中IP地址）
nf: UNC
version: 20.15.2
object_name: GBEPPOOL
object_kind: entity
applicable_nf:
- SGSN
status: active
---

# GBEPPOOL（地址池中IP地址）

## 说明

**适用网元：SGSN**

此命令用于增加IP地址到Gb地址池，作为自动配置功能的Gb业务IP使用，地址池整系统唯一。

此地址池中的IP地址既可以作为NSE动态流程协商的地址，也可以作为NSE的本端端点进行业务传输。

此命令只适用于Gb over IP自动配置的场景。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-GBEPPOOL]] · ADD GBEPPOOL
- [[command/UNC/20.15.2/LST-GBEPPOOL]] · LST GBEPPOOL
- [[command/UNC/20.15.2/RMV-GBEPPOOL]] · RMV GBEPPOOL

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除地址池中IP地址(RMV-GBEPPOOL)_72225677.md`
- 原始手册：`evidence/UNC/20.15.2/增加IP地址到地址池(ADD-GBEPPOOL)_26145998.md`
- 原始手册：`evidence/UNC/20.15.2/查询地址池中信息(LST-GBEPPOOL)_26305808.md`
