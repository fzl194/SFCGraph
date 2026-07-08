---
id: UDG@20.15.2@ConfigObject@SUPPRESSALM
type: ConfigObject
name: SUPPRESSALM（被抑制告警）
nf: UDG
version: 20.15.2
object_name: SUPPRESSALM
object_kind: query_target
status: active
---

# SUPPRESSALM（被抑制告警）

## 说明

本命令用于查询系统内闪断振荡被抑制告警，查询结果为最新产生的被抑制告警。

> **说明**
> 如果需要修改闪断或振荡参数，可在OM Portal中依次单击 “ 监控分析 > 告警管理 > 告警配置 ” ，然后在 “操作” 列单击 “修改” 按钮，按照需要进行修改。

> **说明**
> 不支持查询VNFC类型服务的闪断振荡被抑制的告警，VNFC类型服务可通过执行业务网元命令 **DSP VNFC** 查询。默认查询64条，最大支持1000条告警。

## 操作本对象的命令

- [LST SUPPRESSALM](command/UDG/20.15.2/LST-SUPPRESSALM.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询被抑制告警（LST-SUPPRESSALM）_39192239.md`
