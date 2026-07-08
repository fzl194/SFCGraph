---
id: UNC@20.15.2@ConfigObject@SMACTCTRL
type: ConfigObject
name: SMACTCTRL（激活过程控制参数）
nf: UNC
version: 20.15.2
object_name: SMACTCTRL
object_kind: entity
applicable_nf:
- SGSN
- MME
status: active
---

# SMACTCTRL（激活过程控制参数）

## 说明

**适用网元：SGSN、MME**

该命令用于增加在PDP激活流程（ UNC 作为SGSN网元）和PDN连接建立流程（ UNC 作为MME网元）中使用签约数据匹配的纠正功能涉及到的相关参数。PDP激活包括UE发起的PDP上下文激活过程和GGSN发起的网络侧PDP上下文激活过程，不包括二次激活过程。PDN连接建立包括UE发起的ATTACH流程和UE请求的PDN连接建立流程。

当纠正所有用户激活请求中错误的APN时，需要执行此命令。

## 操作本对象的命令

- [ADD SMACTCTRL](command/UNC/20.15.2/ADD-SMACTCTRL.md)
- [LST SMACTCTRL](command/UNC/20.15.2/LST-SMACTCTRL.md)
- [MOD SMACTCTRL](command/UNC/20.15.2/MOD-SMACTCTRL.md)
- [RMV SMACTCTRL](command/UNC/20.15.2/RMV-SMACTCTRL.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改激活过程控制参数（MOD-SMACTCTRL）_26145664.md`
- 原始手册：`evidence/UNC/20.15.2/删除激活过程控制参数（RMV-SMACTCTRL）_72345259.md`
- 原始手册：`evidence/UNC/20.15.2/增加激活过程控制参数（ADD-SMACTCTRL）_26305472.md`
- 原始手册：`evidence/UNC/20.15.2/查询激活过程控制参数（LST-SMACTCTRL）_72225343.md`
