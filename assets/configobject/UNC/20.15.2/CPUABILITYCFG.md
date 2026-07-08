---
id: UNC@20.15.2@ConfigObject@CPUABILITYCFG
type: ConfigObject
name: CPUABILITYCFG（不同CPU类型的能力系数和基础消耗。）
nf: UNC
version: 20.15.2
object_name: CPUABILITYCFG
object_kind: entity
applicable_nf:
- GGSN
- SGW-C
- SMF
- PGW-C
status: active
---

# CPUABILITYCFG（不同CPU类型的能力系数和基础消耗。）

## 说明

![](增加不同CPU类型的能力系数和基础消耗。（ADD CPUABILITYCFG）_23736532.assets/notice_3.0-zh-cn_2.png)

如果配置不合理会导致会动态权重失效以及token迁移不能处于稳态。

**适用NF：GGSN、SGW-C、SMF、PGW-C**

该命令用于增加不同CPU类型的能力系数和基础消耗。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-CPUABILITYCFG]] · ADD CPUABILITYCFG
- [[command/UNC/20.15.2/LST-CPUABILITYCFG]] · LST CPUABILITYCFG
- [[command/UNC/20.15.2/MOD-CPUABILITYCFG]] · MOD CPUABILITYCFG
- [[command/UNC/20.15.2/RMV-CPUABILITYCFG]] · RMV CPUABILITYCFG

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改不同CPU类型的能力系数和基础消耗。（MOD-CPUABILITYCFG）_51335397.md`
- 原始手册：`evidence/UNC/20.15.2/删除不同CPU类型的能力系数和基础消耗。（RMV-CPUABILITYCFG）_23736560.md`
- 原始手册：`evidence/UNC/20.15.2/增加不同CPU类型的能力系数和基础消耗。（ADD-CPUABILITYCFG）_23736532.md`
- 原始手册：`evidence/UNC/20.15.2/查询不同CPU类型的能力系数和基础消耗。（LST-CPUABILITYCFG）_24015932.md`
