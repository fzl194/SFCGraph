---
id: UNC@20.15.2@MMLCommand@LST SMFCONFLICTRULE
type: MMLCommand
name: LST SMFCONFLICTRULE（查询冲突规则）
nf: UNC
version: 20.15.2
verb: LST
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

# LST SMFCONFLICTRULE（查询冲突规则）

## 功能

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用于查询冲突规则。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CSTYPE | 指定CS类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定CS的类型。<br>数据来源：本端规划<br>取值范围：<br>- SMC_SM（会话管理控制cell服务的会话管理模块）<br>默认值：无<br>配置原则：无 |
| PROCTYPE | 流程内部标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定流程内部标识。<br>数据来源：本端规划<br>取值范围：任意类型，取值范围是1~128。<br>默认值：无<br>配置原则：无 |
| NEWINITPROCTYPE | 新流程内部标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定新流程内部标识。<br>数据来源：本端规划<br>取值范围：任意类型，取值范围是1~128。<br>默认值：无<br>配置原则：无 |
| RULE | 冲突流程规则 | 可选必选说明：可选参数<br>参数含义：该参数用于指定冲突流程规则。<br>数据来源：本端规划<br>取值范围：任意类型，取值范围是0~4096。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SMFCONFLICTRULE]] · 冲突规则（SMFCONFLICTRULE）

## 使用实例

查询指定场景的冲突流程，PROCTYPE=ProcedureTypeN4DdnReportAsHsmfN11和NEWINITPROCTYPE=ProcedureTypeAmfIwkEpsIndChangeAsHsmfN11的冲突规则：

```
%%LST SMFCONFLICTRULE: CSTYPE=SMC_SM, PROCTYPE="ProcedureTypeN4DdnReportAsHsmfN11", NEWINITPROCTYPE="ProcedureTypeAmfIwkEpsIndChangeAsHsmfN11";%%
RETCODE = 0  操作成功

结果如下
--------
    指定CS类型  =  SMC_SM
  流程内部标识  =  "ProcedureTypeN4DdnReportAsHsmfN11"
新流程内部标识  =  "InitialMsgTypeUpdateSmContextReq"
  冲突流程规则  =  {"Name":"When","Children":[{"Name":"Not","Children":[{"Name":"TransLabelContainImpl","LabelCheck":"LabelNotifyRmvSess"}]},{"Name":"DiscardImpl","AnyWay":"false","NeedRespond":"false","RespondCause":"SmcCauseConflictBegin"}]}
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询冲突规则（LST-SMFCONFLICTRULE）_59999565.md`
