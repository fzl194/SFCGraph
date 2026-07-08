---
id: UNC@20.15.2@ConfigObject@CDRDELTASK
type: ConfigObject
name: CDRDELTASK（话单删除任务）
nf: UNC
version: 20.15.2
object_name: CDRDELTASK
object_kind: entity
applicable_nf:
- NCG
status: active
---

# CDRDELTASK（话单删除任务）

## 说明

![](增加话单删除任务（ADD CDRDELTASK）_51174264.assets/notice_3.0-zh-cn_2.png)

如果目录配置为系统文件目录将会造成误删系统文件，请确认配置的目录为话单目录。

**适用NF：NCG**

该命令用于配置话单删除任务，删除NCG上自定义目录下的过期话单文件，防止保存的话单数量过多导致磁盘空间不足。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-CDRDELTASK]] · ADD CDRDELTASK
- [[command/UNC/20.15.2/LST-CDRDELTASK]] · LST CDRDELTASK
- [[command/UNC/20.15.2/MOD-CDRDELTASK]] · MOD CDRDELTASK
- [[command/UNC/20.15.2/RMV-CDRDELTASK]] · RMV CDRDELTASK

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改话单删除任务（MOD-CDRDELTASK）_51174266.md`
- 原始手册：`evidence/UNC/20.15.2/删除话单删除任务（RMV-CDRDELTASK）_51174265.md`
- 原始手册：`evidence/UNC/20.15.2/增加话单删除任务（ADD-CDRDELTASK）_51174264.md`
- 原始手册：`evidence/UNC/20.15.2/查询话单删除任务（LST-CDRDELTASK）_51174267.md`
