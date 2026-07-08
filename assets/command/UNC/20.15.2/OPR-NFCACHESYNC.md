---
id: UNC@20.15.2@MMLCommand@OPR NFCACHESYNC
type: MMLCommand
name: OPR NFCACHESYNC（操作远端NF缓存同步）
nf: UNC
version: 20.15.2
verb: OPR
object_keyword: NFCACHESYNC
command_category: 动作类
applicable_nf:
- AMF
- SMF
- NCG
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 服务化接口管理
- 注册与服务发现
- NF Cache管理
status: active
---

# OPR NFCACHESYNC（操作远端NF缓存同步）

## 功能

![](操作远端NF缓存同步（OPR NFCACHESYNC）_24956644.assets/notice_3.0-zh-cn_2.png)

该命令会根据输入远端NF实例标识尝试构建缓存，新缓存构建成功可能会影响后续对应业务的网元选择。

**适用NF：AMF、SMF、NCG**

该命令用于从NRF获得指定的远端NF信息并构建到缓存数据中。如果本端缓存数据缺失或希望更新缓存中某一网元数据时可以执行该命令。

## 注意事项

- 该命令执行后立即生效。

- 该命令执行结果可利用DSP NFCACHE命令核查，若执行5分钟后未查询到结果，则该目标NF的缓存同步失败。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFID | 对端NF实例标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定目标NF实例标识，通过该NF实例标识向远端NRF进行服务发现，并根据返回结果构建对应的缓存。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度是36。<br>默认值：无<br>配置原则：<br>该处需以该目标NF在NRF上注册的实例标识为准。 |
| TARGETNFTYPE | 目标NF类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定目标NF类型，作为远端服务发现参数。<br>数据来源：本端规划<br>取值范围：<br>- “NfNRF（NfNRF）”：NfNRF<br>- “NfUDM（NfUDM）”：NfUDM<br>- “NfAMF（NfAMF）”：NfAMF<br>- “NfSMF（NfSMF）”：NfSMF<br>- “NfAUSF（NfAUSF）”：NfAUSF<br>- “NfNEF（NfNEF）”：NfNEF<br>- “NfPCF（NfPCF）”：NfPCF<br>- “NfSMSF（NfSMSF）”：NfSMSF<br>- “NfNSSF（NfNSSF）”：NfNSSF<br>- “NfUDR（NfUDR）”：NfUDR<br>- “NfLMF（NfLMF）”：NfLMF<br>- “NfGMLC（NfGMLC）”：NfGMLC<br>- “Nf5G_EIR（Nf5G_EIR）”：Nf5G_EIR<br>- “NfSEPP（NfSEPP）”：NfSEPP<br>- “NfUPF（NfUPF）”：NfUPF<br>- “NfN3IWF（NfN3IWF）”：NfN3IWF<br>- “NfAF（NfAF）”：NfAF<br>- “NfUDSF（NfUDSF）”：NfUDSF<br>- “NfBSF（NfBSF）”：NfBSF<br>- “NfCHF（NfCHF）”：NfCHF<br>- “NfCUSTOM_OCS（NfCUSTOM_OCS）”：NfCUSTOM_OCS<br>- “NfSCP（NfSCP）”：NfSCP<br>- “NfPCSCF（NfPCSCF）”：NfPCSCF<br>- “NfMBSMF（NfMBSMF）”：NfMBSMF<br>- “NWDAF（NWDAF）”：NWDAF<br>默认值：无<br>配置原则：无 |
| REQNFTYPE | 本端NF类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定本端NF类型，作为远端服务发现参数。<br>数据来源：本端规划<br>取值范围：<br>- “NfNRF（NfNRF）”：NfNRF<br>- “NfUDM（NfUDM）”：NfUDM<br>- “NfAMF（NfAMF）”：NfAMF<br>- “NfSMF（NfSMF）”：NfSMF<br>- “NfAUSF（NfAUSF）”：NfAUSF<br>- “NfNEF（NfNEF）”：NfNEF<br>- “NfPCF（NfPCF）”：NfPCF<br>- “NfSMSF（NfSMSF）”：NfSMSF<br>- “NfNSSF（NfNSSF）”：NfNSSF<br>- “NfUDR（NfUDR）”：NfUDR<br>- “NfLMF（NfLMF）”：NfLMF<br>- “NfGMLC（NfGMLC）”：NfGMLC<br>- “Nf5G_EIR（Nf5G_EIR）”：Nf5G_EIR<br>- “NfSEPP（NfSEPP）”：NfSEPP<br>- “NfUPF（NfUPF）”：NfUPF<br>- “NfN3IWF（NfN3IWF）”：NfN3IWF<br>- “NfAF（NfAF）”：NfAF<br>- “NfUDSF（NfUDSF）”：NfUDSF<br>- “NfBSF（NfBSF）”：NfBSF<br>- “NfCHF（NfCHF）”：NfCHF<br>- “NfCUSTOM_OCS（NfCUSTOM_OCS）”：NfCUSTOM_OCS<br>- “NfSCP（NfSCP）”：NfSCP<br>- “NfPCSCF（NfPCSCF）”：NfPCSCF<br>- “NfMBSMF（NfMBSMF）”：NfMBSMF<br>- “NWDAF（NWDAF）”：NWDAF<br>默认值：无<br>配置原则：无 |
| PLMN | 目标方PLMN | 可选必选说明：可选参数<br>参数含义：该参数用于指定待查询NF所在的PLMN。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是5~6。<br>默认值：无<br>配置原则：<br>PLMN由MCC和MNC组成，MCC为3个十进制数字，MNC为2~3个十进制数字。例如PLMN=“12345”，其中MCC=“123”， MNC=“45”。 |
| REQPLMN | 请求方PLMN | 可选必选说明：可选参数<br>参数含义：该参数用于指定查询NF所在的PLMN。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是5~6。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NFCACHESYNC]] · 操作远端NF缓存同步（NFCACHESYNC）

## 使用实例

如果本端缓存数据缺失或希望更新缓存中某一网元数据时，假设本端网元类型为SMF，目标网元类型为AMF，目标网元ID为“00000000-0000-0000-0000-000000000001”

```
OPR NFCACHESYNC:NFID="00000000-0000-0000-0000-000000000001",TARGETNFTYPE=NfAMF,REQNFTYPE=NfSMF;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/操作远端NF缓存同步（OPR-NFCACHESYNC）_24956644.md`
