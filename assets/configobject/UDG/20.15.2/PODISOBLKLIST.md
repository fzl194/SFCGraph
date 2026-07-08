---
id: UDG@20.15.2@ConfigObject@PODISOBLKLIST
type: ConfigObject
name: PODISOBLKLIST（Pod隔离黑名单）
nf: UDG
version: 20.15.2
object_name: PODISOBLKLIST
object_kind: entity
status: active
---

# PODISOBLKLIST（Pod隔离黑名单）

## 说明

![](增加Pod隔离黑名单（ADD PODISOBLKLIST）_60519725.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，该命令配置后对应类型的Pod出现Fabric平面通信亚健康或者通信故障场景将统一不进行隔离，可能会导致业务呼损，请谨慎使用并联系华为技术支持协助操作。

该命令用于增加指定Pod类型到Pod隔离黑名单中。

> **说明**
> - 该命令执行后立即生效。
>
> - 该命令执行后不会影响业务正常运行，但当环境上对应的Pod类型出现Fabric平面通信亚健康或者通信故障时，则可能会导致业务呼损。
>
> - 最多可输入1024条记录。

## 操作本对象的命令

- [ADD PODISOBLKLIST](command/UDG/20.15.2/ADD-PODISOBLKLIST.md)
- [LST PODISOBLKLIST](command/UDG/20.15.2/LST-PODISOBLKLIST.md)
- [RMV PODISOBLKLIST](command/UDG/20.15.2/RMV-PODISOBLKLIST.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除Pod隔离黑名单（RMV-PODISOBLKLIST）_25438180.md`
- 原始手册：`evidence/UDG/20.15.2/增加Pod隔离黑名单（ADD-PODISOBLKLIST）_60519725.md`
- 原始手册：`evidence/UDG/20.15.2/查询Pod隔离黑名单（LST-PODISOBLKLIST）_25280044.md`
