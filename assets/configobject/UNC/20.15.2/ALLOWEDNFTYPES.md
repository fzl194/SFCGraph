---
id: UNC@20.15.2@ConfigObject@ALLOWEDNFTYPES
type: ConfigObject
name: ALLOWEDNFTYPES（允许访问的NF类型）
nf: UNC
version: 20.15.2
object_name: ALLOWEDNFTYPES
object_kind: entity
applicable_nf:
- NRF
status: active
---

# ALLOWEDNFTYPES（允许访问的NF类型）

## 说明

**适用NF：NRF**

该命令用于为NF对象新增允许访问的NF类型信息。

NF/NFS可以通过访问授权控制策略控制访问自己的NF/NFS范围：只允许特定PLMN内的NF访问、只允许特定NF类型访问、只允许特定NF Domain访问、只允许支持特定切片的NF访问。访问授权控制策略可以在NF/NFS向NRF注册或更新时通过属性控制，也可以在NRF上配置控制，本命令是在NRF上配置访问授权控制时使用。

## 操作本对象的命令

- [ADD ALLOWEDNFTYPES](command/UNC/20.15.2/ADD-ALLOWEDNFTYPES.md)
- [LST ALLOWEDNFTYPES](command/UNC/20.15.2/LST-ALLOWEDNFTYPES.md)
- [RMV ALLOWEDNFTYPES](command/UNC/20.15.2/RMV-ALLOWEDNFTYPES.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除允许访问的NF类型（RMV-ALLOWEDNFTYPES）_09653196.md`
- 原始手册：`evidence/UNC/20.15.2/增加允许访问的NF类型（ADD-ALLOWEDNFTYPES）_09652560.md`
- 原始手册：`evidence/UNC/20.15.2/查询允许访问的NF类型（LST-ALLOWEDNFTYPES）_09653307.md`
