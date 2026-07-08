---
id: UNC@20.15.2@ConfigObject@NGRANNEIBCFG
type: ConfigObject
name: NGRANNEIBCFG（NG-RAN基站邻接关系配置）
nf: UNC
version: 20.15.2
object_name: NGRANNEIBCFG
object_kind: entity
applicable_nf:
- AMF
status: active
---

# NGRANNEIBCFG（NG-RAN基站邻接关系配置）

## 说明

**适用NF：AMF**

此命令用于手动添加NG-RAN基站的邻接关系。当激活“精准寻呼”特性时，整网所有NG-RAN基站邻接关系的学习是一个漫长的过程，往往需要一周以上的时间，通过此命令可以避免等待系统自动学习邻接关系的大量时间消耗和切换流程的触发。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-NGRANNEIBCFG]] · ADD NGRANNEIBCFG
- [[command/UNC/20.15.2/LST-NGRANNEIBCFG]] · LST NGRANNEIBCFG
- [[command/UNC/20.15.2/RMV-NGRANNEIBCFG]] · RMV NGRANNEIBCFG

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除NG-RAN基站邻接关系配置（RMV-NGRANNEIBCFG）_09653236.md`
- 原始手册：`evidence/UNC/20.15.2/增加NG-RAN基站邻接关系配置（ADD-NGRANNEIBCFG）_09654363.md`
- 原始手册：`evidence/UNC/20.15.2/查询NG-RAN基站邻接关系配置（LST-NGRANNEIBCFG）_09652382.md`
