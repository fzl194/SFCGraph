---
id: UNC@20.15.2@ConfigObject@ALLOWEDNSSAIS
type: ConfigObject
name: ALLOWEDNSSAIS（允许访问的切片）
nf: UNC
version: 20.15.2
object_name: ALLOWEDNSSAIS
object_kind: entity
applicable_nf:
- NRF
status: active
---

# ALLOWEDNSSAIS（允许访问的切片）

## 说明

**适用NF：NRF**

该命令用于新增指定NF对象所允许访问的切片信息。

NF/NFS可以通过访问授权控制策略控制访问自己的NF/NFS范围：只允许特定PLMN内的NF访问、只允许特定NF类型访问、只允许特定NF Domain访问、只允许支持特定切片的NF访问。访问授权控制策略可以在NF/NFS向NRF注册或更新时通过属性控制，也可以在NRF上配置控制，本命令是在NRF上配置访问授权控制时使用。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-ALLOWEDNSSAIS]] · ADD ALLOWEDNSSAIS
- [[command/UNC/20.15.2/LST-ALLOWEDNSSAIS]] · LST ALLOWEDNSSAIS
- [[command/UNC/20.15.2/RMV-ALLOWEDNSSAIS]] · RMV ALLOWEDNSSAIS

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除允许访问的切片（RMV-ALLOWEDNSSAIS）_09651820.md`
- 原始手册：`evidence/UNC/20.15.2/增加允许访问的切片（ADD-ALLOWEDNSSAIS）_09653298.md`
- 原始手册：`evidence/UNC/20.15.2/查询允许访问的切片（LST-ALLOWEDNSSAIS）_09654198.md`
