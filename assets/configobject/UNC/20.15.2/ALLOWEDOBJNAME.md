---
id: UNC@20.15.2@ConfigObject@ALLOWEDOBJNAME
type: ConfigObject
name: ALLOWEDOBJNAME（授权控制对象）
nf: UNC
version: 20.15.2
object_name: ALLOWEDOBJNAME
object_kind: entity
applicable_nf:
- NRF
status: active
---

# ALLOWEDOBJNAME（授权控制对象）

## 说明

**适用NF：NRF**

该命令用于新增授权控制对象。

NF/NFS可以通过授权控制策略控制访问自己的NF/NFS范围：只允许特定PLMN内的NF访问、只允许特定NF类型访问、只允许特定NF Domain访问、只允许支持特定切片的NF访问。访问授权控制策略可以在NF注册或更新时通过属性控制，也可以在NRF上配置控制。

本命令是在NRF上配置访问授权控制时使用，用于指定授权控制的NF。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-ALLOWEDOBJNAME]] · ADD ALLOWEDOBJNAME
- [[command/UNC/20.15.2/LST-ALLOWEDOBJNAME]] · LST ALLOWEDOBJNAME
- [[command/UNC/20.15.2/RMV-ALLOWEDOBJNAME]] · RMV ALLOWEDOBJNAME

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除授权控制对象（RMV-ALLOWEDOBJNAME）_40906679.md`
- 原始手册：`evidence/UNC/20.15.2/增加授权控制对象（ADD-ALLOWEDOBJNAME）_40386783.md`
- 原始手册：`evidence/UNC/20.15.2/查询授权控制对象（LST-ALLOWEDOBJNAME）_93466876.md`
