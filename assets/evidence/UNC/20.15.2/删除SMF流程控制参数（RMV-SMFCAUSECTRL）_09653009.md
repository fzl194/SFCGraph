# 删除SMF流程控制参数（RMV SMFCAUSECTRL）

- [命令功能](#ZH-CN_MMLREF_0209653009__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0209653009__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0209653009__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0209653009__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0209653009)

![](删除SMF流程控制参数（RMV SMFCAUSECTRL）_09653009.assets/notice_3.0-zh-cn_2.png)

删除下发的原因值可能会对终端行为产生影响，对性能指标的统计值产生影响，在配置前请联系华为技术支持工程师评估影响。

**适用NF：SMF**

该命令用于删除SMF流程控制参数。

## [注意事项](#ZH-CN_MMLREF_0209653009)

该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_MMLREF_0209653009)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0209653009)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCEDURETYPE | 流程类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定流程类型，要根据场景来配置相应的流程。<br>数据来源：全网规划<br>取值范围：<br>- PDU_SESSION_EST_PROC（PDU Session创建流程）<br>- PDU_SESSION_MOD_PROC（PDU Session修改流程）<br>默认值：无<br>配置原则：<br>当需要针对会话创建流程配置控制规则时，该参数设置为PDU_SESSION_EST_PROC。<br>当需要针对会话修改流程配置控制规则时，该参数设置为PDU_SESSION_MOD_PROC。 |
| NFTYPE | 异常来源 | 可选必选说明：必选参数<br>参数含义：该参数用于描述发生异常的NF名称。<br>数据来源：全网规划<br>取值范围：<br>- UPF（UPF）<br>- CHG_3GPP（3GPP计费）<br>- POLICY_PCF（PCF策略）<br>- INNER（内部异常）<br>- RADIUS_AUTH（Radius鉴权）<br>- RADIUS_CHG（Radius计费）<br>- UDM（UDM）<br>- CHF_3GPP（3GPP CHF）<br>- INNER_EMG（紧急会话内部异常）<br>默认值：无<br>配置原则：<br>UDM网元类型仅在“流程类型”为“PDU Session创建流程”时生效。 |

## [使用实例](#ZH-CN_MMLREF_0209653009)

删除PDU Session Establishment流程相关的配置记录:

```
RMV SMFCAUSECTRL: PROCEDURETYPE=PDU_SESSION_EST_PROC, NFTYPE=UPF;
```
