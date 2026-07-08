---
id: UNC@20.15.2@ConfigObject@CDRSTAT
type: ConfigObject
name: CDRSTAT（话单统计）
nf: UNC
version: 20.15.2
object_name: CDRSTAT
object_kind: entity
applicable_nf:
- NCG
status: active
---

# CDRSTAT（话单统计）

## 说明

**适用NF：NCG**

该命令根据配置添加一个话单统计器，并根据选择的过滤策略（按接入网元分组、按通道名称和按数据网络名称）提取每用户每会话各个RG的汇总流量信息，通过话单下载界面可获取汇总结果。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-CDRSTAT]] · ADD CDRSTAT
- [[command/UNC/20.15.2/DSP-CDRSTAT]] · DSP CDRSTAT
- [[command/UNC/20.15.2/LST-CDRSTAT]] · LST CDRSTAT
- [[command/UNC/20.15.2/MOD-CDRSTAT]] · MOD CDRSTAT
- [[command/UNC/20.15.2/RMV-CDRSTAT]] · RMV CDRSTAT

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改话单统计（MOD-CDRSTAT）_19253282.md`
- 原始手册：`evidence/UNC/20.15.2/删除话单统计（RMV-CDRSTAT）_48572281.md`
- 原始手册：`evidence/UNC/20.15.2/增加话单统计（ADD-CDRSTAT）_19093334.md`
- 原始手册：`evidence/UNC/20.15.2/显示话单统计信息（DSP-CDRSTAT）_48572277.md`
- 原始手册：`evidence/UNC/20.15.2/查询话单统计（LST-CDRSTAT）_19093338.md`
