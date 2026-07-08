---
id: UDG@20.15.2@ConfigObject@TLSPSK
type: ConfigObject
name: TLSPSK（预共享密钥）
nf: UDG
version: 20.15.2
object_name: TLSPSK
object_kind: entity
status: active
---

# TLSPSK（预共享密钥）

## 说明

该命令用于增加预共享密钥信息。

> **说明**
> - 该命令执行后立即生效。
>
> - 该命令参数“预共享密钥值”的内容是密钥信息，执行“[**EXP MML**](../../../../操作维护/配置管理/配置导出管理/导出MML文件（EXP MML）_47200033.md):;”命令导出配置时，“预共享密钥值”参数的值是匿名化后的内容，因而该命令不支持MML导出后直接导入，必须手动下发。
>
> - 最多可输入128条记录。

## 操作本对象的命令

- [ADD TLSPSK](command/UDG/20.15.2/ADD-TLSPSK.md)
- [LST TLSPSK](command/UDG/20.15.2/LST-TLSPSK.md)
- [RMV TLSPSK](command/UDG/20.15.2/RMV-TLSPSK.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除预共享密钥（RMV-TLSPSK）_57029816.md`
- 原始手册：`evidence/UDG/20.15.2/增加预共享密钥（ADD-TLSPSK）_07669721.md`
- 原始手册：`evidence/UDG/20.15.2/查询预共享密钥信息（LST-TLSPSK）_56870528.md`
