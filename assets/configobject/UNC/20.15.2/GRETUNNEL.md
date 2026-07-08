---
id: UNC@20.15.2@ConfigObject@GRETUNNEL
type: ConfigObject
name: GRETUNNEL（GRE隧道）
nf: UNC
version: 20.15.2
object_name: GRETUNNEL
object_kind: entity
status: active
---

# GRETUNNEL（GRE隧道）

## 说明

该命令用于创建GRE隧道。

通用路由封装GRE（Generic Routing Encapsulation）是对某些网络层协议的报文进行封装，使这些被封装的报文能够在另一网络层协议（如IP）中传输。GRE可以作为VPN的第三层隧道协议，为VPN数据提供透明传输通道。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-GRETUNNEL]] · ADD GRETUNNEL
- [[command/UNC/20.15.2/LST-GRETUNNEL]] · LST GRETUNNEL
- [[command/UNC/20.15.2/MOD-GRETUNNEL]] · MOD GRETUNNEL
- [[command/UNC/20.15.2/RMV-GRETUNNEL]] · RMV GRETUNNEL

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改GRE隧道（MOD-GRETUNNEL）_50121682.md`
- 原始手册：`evidence/UNC/20.15.2/删除GRE隧道（RMV-GRETUNNEL）_00600977.md`
- 原始手册：`evidence/UNC/20.15.2/增加GRE隧道（ADD-GRETUNNEL）_00841729.md`
- 原始手册：`evidence/UNC/20.15.2/查询GRE隧道（LST-GRETUNNEL）_49802638.md`
