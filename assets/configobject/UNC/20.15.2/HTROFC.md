---
id: UNC@20.15.2@ConfigObject@HTROFC
type: ConfigObject
name: HTROFC（HTR局向）
nf: UNC
version: 20.15.2
object_name: HTROFC
object_kind: entity
applicable_nf:
- SGSN
status: active
---

# HTROFC（HTR局向）

## 说明

**适用网元：SGSN**

此命令用于添加HTR局向配置信息。在GT转发的组网配置下，只有STP对SGSN逻辑上可见，HLR目的实体对SGSN是不可见的，所以需要用户手动配置具体的HTR局向进行区分，以保证准确的流控对象，避免误控。详细功能说明可参见 [**SET HTR**](../流控功能管理/设置HTR功能(SET HTR)_72345749.md) 。

## 操作本对象的命令

- [ADD HTROFC](command/UNC/20.15.2/ADD-HTROFC.md)
- [LST HTROFC](command/UNC/20.15.2/LST-HTROFC.md)
- [MOD HTROFC](command/UNC/20.15.2/MOD-HTROFC.md)
- [RMV HTROFC](command/UNC/20.15.2/RMV-HTROFC.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改HTR局向(MOD-HTROFC)_72225833.md`
- 原始手册：`evidence/UNC/20.15.2/删除HTR局向(RMV-HTROFC)_26146154.md`
- 原始手册：`evidence/UNC/20.15.2/增加HTR局向(ADD-HTROFC)_72345753.md`
- 原始手册：`evidence/UNC/20.15.2/查询HTR局向(LST-HTROFC)_26305964.md`
