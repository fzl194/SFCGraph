# 删除GGSN-C原因值控制参数（RMV GGSNCAUSECTRL）

- [命令功能](#ZH-CN_MMLREF_0225121201__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0225121201__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0225121201__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0225121201__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0225121201)

**适用NF：GGSN**

该命令用于删除GGSN-C的原因值控制参数。

## [注意事项](#ZH-CN_MMLREF_0225121201)

该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_MMLREF_0225121201)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0225121201)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCEDURETYPE | 流程类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定流程类型，要根据场景来配置相应的流程。<br>数据来源：本端规划<br>取值范围：<br>- CRT_PDP_PROC（创建PDP流程）<br>- UPD_PDP_PROC（更新PDP流程）<br>默认值：无<br>配置原则：无 |
| CAUSESOURCE | 异常来源 | 可选必选说明：必选参数<br>参数含义：该参数用于描述发生异常的来源。<br>数据来源：本端规划<br>取值范围：<br>- UPF（UPF）<br>- POLICY_PCRF（PCRF策略）<br>- CHG_3GPP（3GPP计费）<br>- RADIUS_AUTH（Radius鉴权）<br>- INNER（内部异常）<br>- RADIUS_CHG（Radius计费）<br>- POLICY_PCF（PCF策略）<br>- CHF_3GPP（3GPP CHF）<br>默认值：无<br>配置原则：<br>POLICY_PCF以及CHF_3GPP网元类型仅在2G用户下生效。 |

## [使用实例](#ZH-CN_MMLREF_0225121201)

删除创建PDP流程UPF异常的流程控制配置。

```
RMV GGSNCAUSECTRL: PROCEDURETYPE=CRT_PDP_PROC, CAUSESOURCE=UPF;
```
