---
id: UNC@20.15.2@ConfigObject@SCNDGWSELPLCY
type: ConfigObject
name: SCNDGWSELPLCY（相同APN建立多个PDP/PDN连接的网关选择策略）
nf: UNC
version: 20.15.2
object_name: SCNDGWSELPLCY
object_kind: entity
applicable_nf:
- SGSN
- MME
status: active
---

# SCNDGWSELPLCY（相同APN建立多个PDP/PDN连接的网关选择策略）

## 说明

**适用网元：SGSN、MME**

该命令用于根据用户范围及接入类型配置使用相同APN建立多个PDP/PDN连接场景下，系统选择GGSN/P-GW的策略。当指定用户建立第1个PDP/PDN连接时，系统通过相应APN到DNS解析获取GGSN/P-GW的IP地址（IP1），在发给GGSN/S-GW的Create PDP Context Request/Create Session Request消息中携带IP1（接口IP）。GGSN/S-GW回复给USN的Create PDP Context Response/Create Session Response消息中会携带IP2（业务IP），IP1和IP2可能相同，也可能不同，若不相同，当使用相同APN建立第二个或更多PDP/PDN连接时，根据本命令选择在Create PDP Context Request/Create Session Request消息中携带的IP类型。

## 操作本对象的命令

- [ADD SCNDGWSELPLCY](command/UNC/20.15.2/ADD-SCNDGWSELPLCY.md)
- [LST SCNDGWSELPLCY](command/UNC/20.15.2/LST-SCNDGWSELPLCY.md)
- [MOD SCNDGWSELPLCY](command/UNC/20.15.2/MOD-SCNDGWSELPLCY.md)
- [RMV SCNDGWSELPLCY](command/UNC/20.15.2/RMV-SCNDGWSELPLCY.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改相同APN建立多个PDP_PDN连接的网关选择策略(MOD-SCNDGWSELPLCY)_26305756.md`
- 原始手册：`evidence/UNC/20.15.2/删除相同APN建立多个PDP_PDN连接的网关选择策略(RMV-SCNDGWSELPLCY)_72225625.md`
- 原始手册：`evidence/UNC/20.15.2/增加相同APN建立多个PDP_PDN连接的网关选择策略(ADD-SCNDGWSELPLCY)_26145946.md`
- 原始手册：`evidence/UNC/20.15.2/查询相同APN建立多个PDP_PDN连接的网关选择策略(LST-SCNDGWSELPLCY)_72345547.md`
