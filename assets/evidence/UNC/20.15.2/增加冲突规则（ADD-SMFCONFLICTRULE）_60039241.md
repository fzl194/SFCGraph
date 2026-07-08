# 增加冲突规则（ADD SMFCONFLICTRULE）

- [命令功能](#ZH-CN_MMLREF_0000001360039241__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001360039241__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001360039241__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001360039241__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0000001360039241)

![](增加冲突规则（ADD SMFCONFLICTRULE）_60039241.assets/notice_3.0-zh-cn_2.png)

本命令属于高危命令，增加冲突规则可能影响现有业务对冲突场景的判断和解决策略。

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用于增加冲突规则。

## [注意事项](#ZH-CN_MMLREF_0000001360039241)

- 该命令执行后立即生效。

- 最多可输入1024条记录。

#### [操作用户权限](#ZH-CN_MMLREF_0000001360039241)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001360039241)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CSTYPE | 指定CS类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定CS的类型。<br>数据来源：本端规划<br>取值范围：<br>- SMC_SM（会话管理控制cell服务的会话管理模块）<br>默认值：无<br>配置原则：无 |
| PROCTYPE | 流程内部标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定流程内部标识。<br>数据来源：本端规划<br>取值范围：任意类型，取值范围是1~128。<br>默认值：无<br>配置原则：无 |
| NEWINITPROCTYPE | 新流程内部标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定新流程内部标识。<br>数据来源：本端规划<br>取值范围：任意类型，取值范围是1~128。<br>默认值：无<br>配置原则：无 |
| RULE | 冲突流程规则 | 可选必选说明：必选参数<br>参数含义：该参数用于指定冲突流程规则。<br>数据来源：本端规划<br>取值范围：任意类型，取值范围是0~4096。<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0000001360039241)

HsmfN11形态N4DdnReport流程中，收到名为ProcedureTypeAmfIwkEpsIndChangeAsHsmfN11的流程首消息时，执行缓存策略：

```
ADD SMFCONFLICTRULE: CSTYPE=SMC_SM, PROCTYPE="ProcedureTypeN4DdnReportAsHsmfN11", NEWINITPROCTYPE="ProcedureTypeAmfIwkEpsIndChangeAsHsmfN11", RULE="{\"Name\":\"When\",\"Children\":[{\"Name\":\"Not\",\"Children\":[{\"Name\":\"TransLabelContainImpl\",\"LabelCheck\":\"LabelNotifyRmvSess\"}]},{\"Name\":\"StashImpl\",\"Cause\":\"SmcCauseConflictBegin\"}]}";
```
