---
id: UDG@20.15.2@ConfigObject@MEASMU
type: ConfigObject
name: MEASMU（话统测量单元模型）
nf: UDG
version: 20.15.2
object_name: MEASMU
object_kind: global_setting
status: active
---

# MEASMU（话统测量单元模型）

## 说明

该命令用于设置话统测量单元模型参数。

![](设置话统测量单元模型(SET MEASMU)_32481237.assets/notice_3.0-zh-cn.png)

该命令为高危命令，执行将修改话统测量单元的参数，影响该话统指标的上报，请慎重执行。

> **说明**
> 该命令通过修改测量单元是否默认测量属性，可从网管侧关闭默认测量任务。升级、回退、补丁、补丁回退场景下会自动同步任务，任务最终状态由默认测量属性和网管侧任务状态共同决定。

## 操作本对象的命令

- [[command/UDG/20.15.2/LST-MEASMU]] · LST MEASMU
- [[command/UDG/20.15.2/SET-MEASMU]] · SET MEASMU

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询话统测量单元模型(LST-MEASMU)_32442313.md`
- 原始手册：`evidence/UDG/20.15.2/设置话统测量单元模型(SET-MEASMU)_32481237.md`
