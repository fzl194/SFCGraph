---
id: UNC@20.15.2@ConfigObject@FAILHANDLING
type: ConfigObject
name: FAILHANDLING（融合计费模板故障处理动作）
nf: UNC
version: 20.15.2
object_name: FAILHANDLING
object_kind: global_setting
applicable_nf:
- PGW-C
- SMF
status: active
---

# FAILHANDLING（融合计费模板故障处理动作）

## 说明

![](设置融合计费模板故障处理动作（SET FAILHANDLING）_09654177.assets/notice_3.0-zh-cn_2.png)

配置N40接口超时时长不合理可能导致在超时场景下，激活响应的总时长过长。在前期规划时，建议产品配置的等待右侧网元的最大时长小于产品ADD GTPCT3N3命令配置的T3N3时长及左侧（MME\SGSN\AMF等）的T3N3时长。

**适用NF：PGW-C、SMF**

该命令用于设置融合计费模板（Converged Charging Template）故障处理相关动作。

## 操作本对象的命令

- [SET FAILHANDLING](command/UNC/20.15.2/SET-FAILHANDLING.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置融合计费模板故障处理动作（SET-FAILHANDLING）_09654177.md`
