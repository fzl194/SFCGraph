---
id: UNC@20.15.2@MMLCommand@RMV FEATLOCREPORT
type: MMLCommand
name: RMV FEATLOCREPORT（删除基于特性的位置上报配置）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: FEATLOCREPORT
command_category: 配置类
applicable_nf:
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 位置上报管理
- 特性位置上报管理
status: active
---

# RMV FEATLOCREPORT（删除基于特性的位置上报配置）

## 功能

**适用NF：SMF**

该命令用于删除基于特性的位置上报配置。

## 注意事项

随流程生效

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FEATURE | 特性名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定特性名称。<br>数据来源：本端规划<br>取值范围：<br>- QOSANA（质差分析）<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@FEATLOCREPORT]] · 基于特性的位置上报配置（FEATLOCREPORT）

## 使用实例

删除“FEATURE”为“QOSANA”的位置上报配置：

```
RMV FEATLOCREPORT:FEATURE=QOSANA;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-FEATLOCREPORT.md`
