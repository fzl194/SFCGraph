---
id: UNC@20.15.2@ConfigObject@GUAMI
type: ConfigObject
name: GUAMI（AMF全局标识）
nf: UNC
version: 20.15.2
object_name: GUAMI
object_kind: entity
applicable_nf:
- AMF
status: active
---

# GUAMI（AMF全局标识）

## 说明

**适用NF：AMF**

该命令用于为AMF实例配置全局AMF标识符（GUAMI）。GUAMI的组成是[MCC] + [MNC] + [AMF Region ID] + [AMF Set ID] + [AMF Pointer]。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-GUAMI]] · ADD GUAMI
- [[command/UNC/20.15.2/LST-GUAMI]] · LST GUAMI
- [[command/UNC/20.15.2/MOD-GUAMI]] · MOD GUAMI
- [[command/UNC/20.15.2/RMV-GUAMI]] · RMV GUAMI

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改AMF全局标识（MOD-GUAMI）_09652503.md`
- 原始手册：`evidence/UNC/20.15.2/删除AMF全局标识（RMV-GUAMI）_09652172.md`
- 原始手册：`evidence/UNC/20.15.2/增加AMF全局标识（ADD-GUAMI）_09653726.md`
- 原始手册：`evidence/UNC/20.15.2/查询AMF全局标识（LST-GUAMI）_09652365.md`
