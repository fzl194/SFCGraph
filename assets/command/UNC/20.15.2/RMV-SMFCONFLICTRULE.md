---
id: UNC@20.15.2@MMLCommand@RMV SMFCONFLICTRULE
type: MMLCommand
name: RMV SMFCONFLICTRULE（删除冲突规则）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: SMFCONFLICTRULE
command_category: 配置类
applicable_nf:
- SGW-C
- PGW-C
- SMF
- GGSN
effect_mode: 立即生效
is_dangerous: true
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 接入控制
- 业务功能灵活控制
- 冲突策略管理
status: active
---

# RMV SMFCONFLICTRULE（删除冲突规则）

## 功能

![](删除冲突规则（RMV SMFCONFLICTRULE）_06639896.assets/notice_3.0-zh-cn_2.png)

本命令属于高危命令，删除冲突规则可能影响现有业务对冲突场景的判断和解决策略。

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用于删除冲突规则。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CSTYPE | 指定CS类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定CS的类型。<br>数据来源：本端规划<br>取值范围：<br>- SMC_SM（会话管理控制cell服务的会话管理模块）<br>默认值：无<br>配置原则：无 |
| PROCTYPE | 流程内部标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定流程内部标识。<br>数据来源：本端规划<br>取值范围：任意类型，取值范围是1~128。<br>默认值：无<br>配置原则：无 |
| NEWINITPROCTYPE | 新流程内部标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定新流程内部标识。<br>数据来源：本端规划<br>取值范围：任意类型，取值范围是1~128。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SMFCONFLICTRULE]] · 冲突规则（SMFCONFLICTRULE）

## 使用实例

删除该条冲突规则: HsmfN11形态N4DdnReport流程中，收到名为ProcedureTypeAmfIwkEpsIndChangeAsHsmfN11的流程首消息时，执行缓存策略，执行如下命令：

```
RMV SMFCONFLICTRULE: CSTYPE=SMC_SM, PROCTYPE="ProcedureTypeN4DdnReportAsHsmfN11", NEWINITPROCTYPE="ProcedureTypeAmfIwkEpsIndChangeAsHsmfN11";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-SMFCONFLICTRULE.md`
