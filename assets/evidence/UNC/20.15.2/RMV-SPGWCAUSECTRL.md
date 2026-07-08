# 删除SGW-C/PGW-C原因值控制参数（RMV SPGWCAUSECTRL）

- [命令功能](#ZH-CN_MMLREF_0209652355__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0209652355__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0209652355__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0209652355__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0209652355)

**适用NF：PGW-C、SGW-C**

该命令用于删除PGW-C或融合的SGW-C/PGW-C的原因值控制参数。

## [注意事项](#ZH-CN_MMLREF_0209652355)

该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_MMLREF_0209652355)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0209652355)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCEDURETYPE | 流程类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定流程类型。<br>数据来源：本端规划<br>取值范围：<br>- CRT_SES_PROC（初始会话创建流程）<br>- MOD_BR_PROC（承载修改流程）<br>默认值：无<br>配置原则：无 |
| CAUSESOURCE | 异常来源 | 可选必选说明：必选参数<br>参数含义：该参数用于指定发生异常的来源。<br>数据来源：本端规划<br>取值范围：<br>- UPF（UPF）<br>- POLICY_PCF（PCF策略）<br>- CHG_3GPP（3GPP计费）<br>- POLICY_PCRF（PCRF策略）<br>- RADIUS_AUTH（Radius鉴权）<br>- INNER（内部异常）<br>- RADIUS_CHG（Radius计费）<br>- DIAMETER_AAA（Diameter AAA）<br>- CHF_3GPP（3GPP CHF）<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0209652355)

删除会话创建流程中UPF异常的流程控制配置，执行如下命令：

```
RMV SPGWCAUSECTRL: PROCEDURETYPE=CRT_SES_PROC, CAUSESOURCE=UPF;
```
