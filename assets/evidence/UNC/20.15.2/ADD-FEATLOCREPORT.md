# 增加基于特性的位置上报配置（ADD FEATLOCREPORT）

- [命令功能](#ZH-CN_MMLREF_0000001870462505__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001870462505__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001870462505__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001870462505__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0000001870462505)

**适用NF：SMF**

该命令用于增加基于特性的位置上报配置。

## [注意事项](#ZH-CN_MMLREF_0000001870462505)

- 随流程生效

- 最多可输入1条记录。

#### [操作用户权限](#ZH-CN_MMLREF_0000001870462505)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001870462505)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FEATURE | 特性名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定特性名称。<br>数据来源：本端规划<br>取值范围：<br>- QOSANA（质差分析）<br>默认值：无<br>配置原则：无 |
| NCGITRIGGERFLG | 配置NR全球小区的trigger | 可选必选说明：该参数在"FEATURE"配置为"QOSANA"时为条件可选参数。<br>参数含义：该参数用于指定5G NR全球小区的trigger是否使能。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE（不使能）<br>- ENABLE（使能）<br>默认值：无<br>配置原则：<br>FEATURE配置为“QOSANA”时，需配置。配置为“ENABLE”时，会基于FEATURE中配置的特性上报NCGI信息。 |

## [使用实例](#ZH-CN_MMLREF_0000001870462505)

新增配置，使能特性为QOSANA的NCGI信息上报。

```
ADD FEATLOCREPORT:FEATURE=QOSANA,NCGITRIGGERFLG=ENABLE;
```
