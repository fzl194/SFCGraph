---
id: UNC@20.15.2@MMLCommand@MOD SUBCONDITION
type: MMLCommand
name: MOD SUBCONDITION（修改NF订阅条件）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: SUBCONDITION
command_category: 配置类
applicable_nf:
- AMF
- SMF
- NRF
- NSSF
- SMSF
- NCG
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 服务化接口管理
- 注册与服务发现
- NRF管理
- NRF参数管理
- 注册与订阅管理
status: active
---

# MOD SUBCONDITION（修改NF订阅条件）

## 功能

**适用NF：AMF、SMF、NRF、NSSF、SMSF、NCG**

该命令用于修改订阅的目标NF类型的订阅条件等信息。

## 注意事项

- 该命令执行后立即生效。

- 该命令只修改订阅条件，对于已经生成的订阅无法生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFTYPE | NF类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定订阅的目标NF类型。<br>数据来源：本端规划<br>取值范围：<br>- “NfInvalid（NfInvalid）”：NfInvalid<br>- “NfNRF（NfNRF）”：NfNRF<br>- “NfUDM（NfUDM）”：NfUDM<br>- “NfAMF（NfAMF）”：NfAMF<br>- “NfSMF（NfSMF）”：NfSMF<br>- “NfAUSF（NfAUSF）”：NfAUSF<br>- “NfNEF（NfNEF）”：NfNEF<br>- “NfPCF（NfPCF）”：NfPCF<br>- “NfSMSF（NfSMSF）”：NfSMSF<br>- “NfNSSF（NfNSSF）”：NfNSSF<br>- “NfUDR（NfUDR）”：NfUDR<br>- “NfLMF（NfLMF）”：NfLMF<br>- “NfGMLC（NfGMLC）”：NfGMLC<br>- “Nf5G_EIR（Nf5G_EIR）”：Nf5G_EIR<br>- “NfSEPP（NfSEPP）”：NfSEPP<br>- “NfUPF（NfUPF）”：NfUPF<br>- “NfN3IWF（NfN3IWF）”：NfN3IWF<br>- “NfAF（NfAF）”：NfAF<br>- “NfUDSF（NfUDSF）”：NfUDSF<br>- “NfBSF（NfBSF）”：NfBSF<br>- “NfCHF（NfCHF）”：NfCHF<br>- “NfCUSTOM_OCS（NfCUSTOM_OCS）”：NfCUSTOM_OCS<br>- “NfSCP（NfSCP）”：NfSCP<br>- “NfPCSCF（NfPCSCF）”：NfPCSCF<br>- “NfMBSMF（NfMBSMF）”：NfMBSMF<br>- “NfUDN（NfUDN）”：NfUDN<br>- “NfNWDAF（NfNWDAF）”：NfNWDAF<br>默认值：无<br>配置原则：无 |
| CONDITION | 订阅条件 | 可选必选说明：可选参数<br>参数含义：该参数用于指定订阅的条件类型。<br>数据来源：全网规划<br>取值范围：<br>- “NfInstanceId（NfInstanceId）”：NfInstanceId<br>- “NFType（NFType）”：NFType<br>- “ServiceName（ServiceName）”：ServiceName<br>- “AmfRegionId（AmfRegionId）”：AmfRegionId<br>- “AmfSetId（AmfSetId）”：AmfSetId<br>- “GuamiList（GuamiList）”：GuamiList<br>- “PlmnId（PlmnId）”：PlmnId<br>- “NetworkSlice（NetworkSlice）”：NetworkSlice<br>- “NfGroup（NfGroup）”：NfGroup<br>- “Rev1（Rev1）”：Rev1<br>- “Rev2（Rev2）”：Rev2<br>- “Rev3（Rev3）”：Rev3<br>默认值：无<br>配置原则：<br>- 推荐使用NfInstanceId-1或NFType-1。<br>- 同一条命令勾选不同的订阅条件会生成多条订阅。<br>- 不支持单独配置AmfSetId订阅，只支持AmfRegionId+AmfSetId组合或者单独AmfRegionId订阅。 |
| REQNOTIFEVENT | 通知事件 | 可选必选说明：可选参数<br>参数含义：该参数用于指定订阅的通知事件类型。<br>数据来源：对端协商<br>取值范围：<br>- “NF_REGISTERED（NF_REGISTERED）”：NF上线通知事件，当NF上线时，NRF会通知NF。<br>- “NF_DEREGISTERED（NF_DEREGISTERED）”：NF下线通知事件，当NF下线时，NRF会通知NF。<br>- “NF_PROFILE_CHANGED（NF_PROFILE_CHANGED）”：NF Profile变化通知事件，当NF Profile变化时，NRF会通知NF。<br>默认值：无<br>配置原则：<br>推荐使用NF_REGISTERED-1，NF_DEREGISTERED-1，NF_PROFILE_CHANGED-1。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SUBCONDITION]] · NF订阅条件（SUBCONDITION）

## 使用实例

修改目标NF类型为NFAMF的订阅条件等信息，订阅条件修改为NF_REGISTERED，通知事件修改为NfInstanceId。

```
MOD SUBCONDITION: NFTYPE=NfAMF, CONDITION=NfInstanceId-1&NFType-1&ServiceName-0&AmfRegionId-0&AmfSetId-0&GuamiList-0&PlmnId-0&NetworkSlice-0&NfGroup-0&Rev1-0&Rev2-0&Rev3-0, REQNOTIFEVENT=NF_REGISTERED-1&NF_DEREGISTERED-1&NF_PROFILE_CHANGED-1;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-SUBCONDITION.md`
