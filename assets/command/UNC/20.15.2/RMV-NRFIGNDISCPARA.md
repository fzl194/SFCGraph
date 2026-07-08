---
id: UNC@20.15.2@MMLCommand@RMV NRFIGNDISCPARA
type: MMLCommand
name: RMV NRFIGNDISCPARA（删除NF服务发现忽略参数规则）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: NRFIGNDISCPARA
command_category: 配置类
applicable_nf:
- NRF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- NRF业务参数
- NF服务发现忽略参数处理规则
status: active
---

# RMV NRFIGNDISCPARA（删除NF服务发现忽略参数规则）

## 功能

**适用NF：NRF**

该命令用于删除NF服务发现忽略参数配置。忽略参数被删除后，对应目标NF发现时，NRF会将此参数重新作为发现参数进行目标NF选择。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFTYPE | 网元类型 | 可选必选说明：必选参数<br>参数含义：该参数用于表示忽略发现参数规则对应的目标NF类型。其中，ALL表示适用于所有目标NF类型。<br>数据来源：本端规划<br>取值范围：<br>- ALL（表示适用于所有NF类型）<br>- NRF（NRF）<br>- UDM（UDM）<br>- AMF（AMF）<br>- SMF（SMF）<br>- AUSF（AUSF）<br>- NEF（NEF）<br>- PCF（PCF）<br>- SMSF（SMSF）<br>- NSSF（NSSF）<br>- UDR（UDR）<br>- LMF（LMF）<br>- GMLC（GMLC）<br>- EIR_5G（EIR_5G）<br>- SEPP（SEPP）<br>- UPF（UPF）<br>- N3IWF（N3IWF）<br>- AF（AF）<br>- UDSF（UDSF）<br>- BSF（BSF）<br>- CHF（CHF）<br>- NWDAF（NWDAF）<br>- CUSTOM_OCS（CUSTOM_OCS）<br>- SCP（SCP）<br>默认值：无<br>配置原则：无 |
| IGNDISCPARA | 服务发现忽略参数 | 可选必选说明：必选参数<br>参数含义：该参数表示NRF忽略的服务发现参数。NRF在处理指定目标NF类型服务发现时，会忽略该发现参数，当做该参数没有携带，匹配其他条件进行服务发现。<br>数据来源：本端规划<br>取值范围：<br>- PreferredLocality（preferred-locality）<br>- ServingScope（serving-scope）<br>- PreferredTai（preferred-tai）<br>- Tai（tai）<br>- Dnn（dnn）<br>- Snssais（snssais）<br>- Supi（supi）<br>- Gpsi（gpsi）<br>- RoutingIndicator（routing-indicator）<br>- UeIpv4Address（ue-ipv4-address）<br>- UeIpv6Prefix（ue-ipv6-prefix）<br>- Ipdomain（ip-domain）<br>- GroupIdList（group-id-list）<br>- TargetPlmnList（target-plmn-list）<br>- SmfServingArea（smf-serving-area）<br>- MaxPayloadSize（max-payload-size）<br>- MaxPayloadSizeExt（max-payload-size-ext）<br>- Reserved1（字段预留，为热补丁预留）<br>- Reserved2（字段预留，为热补丁预留）<br>- Reserved3（字段预留，为热补丁预留）<br>- PlmnSpecificSnssaiList（plmn-specific-snssai-list）<br>- NwdafEventList（nwdaf-event-list）<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [NF服务发现忽略参数规则（NRFIGNDISCPARA）](configobject/UNC/20.15.2/NRFIGNDISCPARA.md)

## 使用实例

删除网元类型为NRF、服务发现忽略参数为Tai的NF服务发现忽略参数规则。

```
RMV NRFIGNDISCPARA: NFTYPE=NRF, IGNDISCPARA=Tai;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除NF服务发现忽略参数规则（RMV-NRFIGNDISCPARA）_45048573.md`
