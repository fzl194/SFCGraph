---
id: UNC@20.15.2@ConfigObject@NGTAGP
type: ConfigObject
name: NGTAGP（5G TA群组）
nf: UNC
version: 20.15.2
object_name: NGTAGP
object_kind: entity
applicable_nf:
- AMF
status: active
---

# NGTAGP（5G TA群组）

## 说明

**适用NF：AMF**

该命令用于增加跟踪区群组记录。跟踪区群组用于定义一组TA组成的区域，以该区域为粒度进行业务策略控制。需要结合ADD NGTAGPMEM命令为跟踪区群组添加成员。

## 操作本对象的命令

- [ADD NGTAGP](command/UNC/20.15.2/ADD-NGTAGP.md)
- [LST NGTAGP](command/UNC/20.15.2/LST-NGTAGP.md)
- [MOD NGTAGP](command/UNC/20.15.2/MOD-NGTAGP.md)
- [RMV NGTAGP](command/UNC/20.15.2/RMV-NGTAGP.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改5G-TA群组（MOD-NGTAGP）_58252981.md`
- 原始手册：`evidence/UNC/20.15.2/删除5G-TA群组（RMV-NGTAGP）_09732734.md`
- 原始手册：`evidence/UNC/20.15.2/增加5G-TA群组（ADD-NGTAGP）_09732730.md`
- 原始手册：`evidence/UNC/20.15.2/查询5G-TA群组（LST-NGTAGP）_09413038.md`
