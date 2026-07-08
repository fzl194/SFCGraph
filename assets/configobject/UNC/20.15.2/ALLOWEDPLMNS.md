---
id: UNC@20.15.2@ConfigObject@ALLOWEDPLMNS
type: ConfigObject
name: ALLOWEDPLMNS（允许访问的PLMN）
nf: UNC
version: 20.15.2
object_name: ALLOWEDPLMNS
object_kind: entity
applicable_nf:
- NRF
status: active
---

# ALLOWEDPLMNS（允许访问的PLMN）

## 说明

**适用NF：NRF**

该命令用于为指定NF对象新增允许访问的PLMN信息。

NF/NFS可以通过访问授权控制策略控制访问自己的NF/NFS范围：只允许特定PLMN内的NF访问、只允许特定NF类型访问、只允许特定NF Domain访问、只允许支持特定切片的NF访问。访问授权控制策略可以在NF注册或更新时通过属性控制，也可以在NRF上配置控制，本命令是在NRF上配置访问授权控制时使用。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-ALLOWEDPLMNS]] · ADD ALLOWEDPLMNS
- [[command/UNC/20.15.2/LST-ALLOWEDPLMNS]] · LST ALLOWEDPLMNS
- [[command/UNC/20.15.2/RMV-ALLOWEDPLMNS]] · RMV ALLOWEDPLMNS

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除允许访问的PLMN（RMV-ALLOWEDPLMNS）_09653053.md`
- 原始手册：`evidence/UNC/20.15.2/增加允许访问的PLMN（ADD-ALLOWEDPLMNS）_09651372.md`
- 原始手册：`evidence/UNC/20.15.2/查询允许访问的PLMN（LST-ALLOWEDPLMNS）_09653100.md`
