---
id: UNC@20.15.2@MMLCommand@DSP SMFCONFLICTRULE
type: MMLCommand
name: DSP SMFCONFLICTRULE（显示冲突规则生效状态）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: SMFCONFLICTRULE
command_category: 查询类
applicable_nf:
- SGW-C
- PGW-C
- SMF
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 接入控制
- 业务功能灵活控制
- 冲突策略管理
status: active
---

# DSP SMFCONFLICTRULE（显示冲突规则生效状态）

## 功能

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用于显示冲突规则生效状态。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CSTYPE | 指定CS类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定CS类型。<br>数据来源：本端规划<br>取值范围：<br>- SMC_SM（会话管理控制cell服务的会话管理模块）<br>默认值：无<br>配置原则：无 |
| PROCTYPE | 流程内部标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定流程内部标识。<br>数据来源：本端规划<br>取值范围：任意类型，取值范围是1~128。<br>默认值：无<br>配置原则：无 |
| NEWINITPROCTYPE | 新流程内部标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定新流程内部标识。<br>数据来源：本端规划<br>取值范围：任意类型，取值范围是1~128。<br>默认值：无<br>配置原则：无 |
| RULE | 冲突流程规则 | 可选必选说明：可选参数<br>参数含义：该参数用于指定冲突流程规则。<br>数据来源：本端规划<br>取值范围：任意类型，取值范围是0~4096。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SMFCONFLICTRULE]] · 冲突规则（SMFCONFLICTRULE）

## 使用实例

查询该条规则是否生效，规则如下: HsmfN11形态N4DdnReport流程中，收到名为ProcedureTypeAmfIwkEpsIndChangeAsHsmfN11的流程首消息，执行丢弃策略生效：

```
%%DSP SMFCONFLICTRULE: CSTYPE=SMC_SM, PROCTYPE="ProcedureTypeN4DdnReportAsHsmfN11", NEWINITPROCTYPE="ProcedureTypeAmfIwkEpsIndChangeAsHsmfN11", RULE="{\"Name\":\"When\",\"Children\":[{\"Name\":\"Not\",\"Children\":[{\"Name\":\"TransLabelContainImpl\",\"LabelCheck\":\"LabelNotifyRmvSess\"}]},{\"Name\":\"DiscardImpl\",\"AnyWay\":\"false\",\"NeedRespond\":\"false\",\"RespondCause\":\"SmcCauseConflictBegin\"}]}";%%
RETCODE = 0  操作成功

结果如下
--------
冲突流程生效规则  =  Enable
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-SMFCONFLICTRULE.md`
