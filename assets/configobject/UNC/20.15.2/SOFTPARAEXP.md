---
id: UNC@20.15.2@ConfigObject@SOFTPARAEXP
type: ConfigObject
name: SOFTPARAEXP（软件参数配置导出模式）
nf: UNC
version: 20.15.2
object_name: SOFTPARAEXP
object_kind: global_setting
applicable_nf:
- SGSN
- MME
status: active
---

# SOFTPARAEXP（软件参数配置导出模式）

## 说明

**适用网元：SGSN、MME**

该命令用于控制软件参数导出。控制执行导出命令后，导出的MML配置文件中 [**SET SOFTPARA**](../软件参数/设置软件参数表(SET SOFTPARA)_26146182.md) 命令是包括全部软件参数值，还是只包括与系统初始默认值不一致的软件参数值。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-SOFTPARAEXP]] · LST SOFTPARAEXP
- [[command/UNC/20.15.2/SET-SOFTPARAEXP]] · SET SOFTPARAEXP

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询软件参数配置导出模式(LST-SOFTPARAEXP)_72345785.md`
- 原始手册：`evidence/UNC/20.15.2/设置软件参数配置导出模式(SET-SOFTPARAEXP)_26305996.md`
