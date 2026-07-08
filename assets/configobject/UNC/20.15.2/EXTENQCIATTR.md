---
id: UNC@20.15.2@ConfigObject@EXTENQCIATTR
type: ConfigObject
name: EXTENQCIATTR（应用扩展QCI参数属性）
nf: UNC
version: 20.15.2
object_name: EXTENQCIATTR
object_kind: global_setting
applicable_nf:
- SGW-C
- PGW-C
- SMF
status: active
---

# EXTENQCIATTR（应用扩展QCI参数属性）

## 说明

**适用NF：SGW-C、PGW-C、SMF**

该命令可用来控制网关对扩展QCI的资源的管理。包括：是否允许非漫游用户发起non-GBR资源申请流程和漫游用户使用扩展QCI进行接入网络、控制Ga接口话单中QCI参数的取值范围、控制Gy接口CCR消息中QCI信元的取值范围、控制RADIUS Access Request和Accounting Request消息中QCI参数的取值范围和控制N40接口的消息中QCI信元的取值范围。当运营商需要控制扩展QCI相关的参数时，可使用SET EXTENQCIATTR命令对扩展QCI参数进行配置。

## 操作本对象的命令

- [LST EXTENQCIATTR](command/UNC/20.15.2/LST-EXTENQCIATTR.md)
- [SET EXTENQCIATTR](command/UNC/20.15.2/SET-EXTENQCIATTR.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询应用扩展QCI参数属性（LST-EXTENQCIATTR）_09652237.md`
- 原始手册：`evidence/UNC/20.15.2/设置应用扩展QCI参数属性（SET-EXTENQCIATTR）_09653201.md`
