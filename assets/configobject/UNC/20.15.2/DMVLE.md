---
id: UNC@20.15.2@ConfigObject@DMVLE
type: ConfigObject
name: DMVLE（Diameter虚拟本地实体）
nf: UNC
version: 20.15.2
object_name: DMVLE
object_kind: entity
applicable_nf:
- MME
status: active
---

# DMVLE（Diameter虚拟本地实体）

## 说明

**适用网元：MME**

该命令用于增加Diameter虚拟本地实体信息。

本命令配置的虚拟本地实体只用于MME链式备份特性（特性编号：WSFD- 201201 ）开启时的S6a接口容灾，即用在容灾时接收并处理对端发送到本虚拟实体的请求消息，并回复响应消息。

除此之外，系统的正常业务流程不能使用本命令配置的虚拟本地实体进行Diameter层通信。

## 操作本对象的命令

- [ADD DMVLE](command/UNC/20.15.2/ADD-DMVLE.md)
- [LST DMVLE](command/UNC/20.15.2/LST-DMVLE.md)
- [MOD DMVLE](command/UNC/20.15.2/MOD-DMVLE.md)
- [RMV DMVLE](command/UNC/20.15.2/RMV-DMVLE.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改Diameter虚拟本地实体(MOD-DMVLE)_26306108.md`
- 原始手册：`evidence/UNC/20.15.2/删除Diameter虚拟本地实体(RMV-DMVLE)_72225975.md`
- 原始手册：`evidence/UNC/20.15.2/增加Diameter虚拟本地实体(ADD-DMVLE)_26146296.md`
- 原始手册：`evidence/UNC/20.15.2/查询Diameter虚拟本地实体(LST-DMVLE)_72345897.md`
