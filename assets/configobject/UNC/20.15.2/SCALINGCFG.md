---
id: UNC@20.15.2@ConfigObject@SCALINGCFG
type: ConfigObject
name: SCALINGCFG（自动扩缩容配置）
nf: UNC
version: 20.15.2
object_name: SCALINGCFG
object_kind: global_setting
status: active
---

# SCALINGCFG（自动扩缩容配置）

## 说明

此命令用于设置扩缩容的各项参数，扩缩容方式、以及扩缩容步长、设置扩缩容阈值上下限，超过阈值上限，进行扩容，低于阈值下限进行缩容。扩缩容触发方式依赖 [**SET SCALINGSWITCH**](设置扩缩容开关（SET SCALINGSWITCH）_09587379.md) 命令。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-SCALINGCFG]] · LST SCALINGCFG
- [[command/UNC/20.15.2/SET-SCALINGCFG]] · SET SCALINGCFG

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询自动扩缩容配置（LST-SCALINGCFG）_09587906.md`
- 原始手册：`evidence/UNC/20.15.2/设置自动扩缩容配置（SET-SCALINGCFG）_09587850.md`
