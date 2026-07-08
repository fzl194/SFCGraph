---
id: UNC@20.15.2@ConfigObject@NFROUTINGIND
type: ConfigObject
name: NFROUTINGIND（选路指示器）
nf: UNC
version: 20.15.2
object_name: NFROUTINGIND
object_kind: entity
applicable_nf:
- NRF
status: active
---

# NFROUTINGIND（选路指示器）

## 说明

**适用NF：NRF**

该命令用于在NRF上新增选路指示器。选路指示器是SUCI组成的一部分，用于使用SUCI进行AUSF和UDM的选择。

在NRF可以为NF组配置支持的选路指示器。此配置对NF组内所有NF实例生效。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-NFROUTINGIND]] · ADD NFROUTINGIND
- [[command/UNC/20.15.2/LST-NFROUTINGIND]] · LST NFROUTINGIND
- [[command/UNC/20.15.2/RMV-NFROUTINGIND]] · RMV NFROUTINGIND

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除选路指示器（RMV-NFROUTINGIND）_09654372.md`
- 原始手册：`evidence/UNC/20.15.2/增加选路指示器（ADD-NFROUTINGIND）_09653295.md`
- 原始手册：`evidence/UNC/20.15.2/查询选路指示器（LST-NFROUTINGIND）_09653212.md`
