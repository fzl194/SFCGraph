---
id: UNC@20.15.2@MMLCommand@MOD DISCADAPTFC
type: MMLCommand
name: MOD DISCADAPTFC（修改服务发现自适应流控NF级配置）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: DISCADAPTFC
command_category: 配置类
applicable_nf:
- AMF
- SMF
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
- 服务发现自适应流控
status: active
---

# MOD DISCADAPTFC（修改服务发现自适应流控NF级配置）

## 功能

**适用NF：AMF、SMF、NSSF、SMSF、NCG**

该命令用于修改服务发现自适应流控NF级配置。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFTYPE | NF类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定NF类型。<br>数据来源：本端规划<br>取值范围：仅支持可以被服务发现的NF类型。<br>- “NfInvalid（NfInvalid）”：NfInvalid<br>- “NfNRF（NfNRF）”：NfNRF<br>- “NfUDM（NfUDM）”：NfUDM<br>- “NfAMF（NfAMF）”：NfAMF<br>- “NfSMF（NfSMF）”：NfSMF<br>- “NfAUSF（NfAUSF）”：NfAUSF<br>- “NfNEF（NfNEF）”：NfNEF<br>- “NfPCF（NfPCF）”：NfPCF<br>- “NfSMSF（NfSMSF）”：NfSMSF<br>- “NfNSSF（NfNSSF）”：NfNSSF<br>- “NfUDR（NfUDR）”：NfUDR<br>- “NfLMF（NfLMF）”：NfLMF<br>- “NfGMLC（NfGMLC）”：NfGMLC<br>- “Nf5G_EIR（Nf5G_EIR）”：Nf5G_EIR<br>- “NfSEPP（NfSEPP）”：NfSEPP<br>- “NfUPF（NfUPF）”：NfUPF<br>- “NfN3IWF（NfN3IWF）”：NfN3IWF<br>- “NfAF（NfAF）”：NfAF<br>- “NfUDSF（NfUDSF）”：NfUDSF<br>- “NfBSF（NfBSF）”：NfBSF<br>- “NfCHF（NfCHF）”：NfCHF<br>- “NfCUSTOM_OCS（NfCUSTOM_OCS）”：NfCUSTOM_OCS<br>- “NfSCP（NfSCP）”：NfSCP<br>- “NfPCSCF（NfPCSCF）”：NfPCSCF<br>- “NfMBSMF（NfMBSMF）”：NfMBSMF<br>- “NfUDN（NfUDN）”：NfUDN<br>- “NfNWDAF（NfNWDAF）”：NfNWDAF<br>默认值：无<br>配置原则：无 |
| WALMIN | 启动流控最低服务发现速率阈值(次/s) | 可选必选说明：可选参数<br>参数含义：该参数用于指定启动自适应流控的服务发现速率最低阈值，低于该值不启动也没必要启动流控。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是5~1000。默认值: 10次/s。<br>默认值：无<br>配置原则：无 |
| WALSTEP | 自适应流控速率变化步长(次/s) | 可选必选说明：可选参数<br>参数含义：该参数用于指定自适应流控速率变化步长。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~100。默认值: 5次/s。<br>默认值：无<br>配置原则：无 |
| INTERVAL | 流控状态变更周期(秒) | 可选必选说明：可选参数<br>参数含义：该参数用于指定流控状态变化周期。可以理解为最少需要INTERVAL秒，该NFType才可从正常状态变为过载状态(或者从过载状态变为正常状态)。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~600，单位是秒。默认: 10s。<br>默认值：无<br>配置原则：无 |
| STARTSUCCRATE | 启动流控服务发现成功率(%) | 可选必选说明：可选参数<br>参数含义：该参数用于指定启控成功率。当一个周期内服务发现的平均成功率低于该值时，才可能启动流控。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~100，单位是百分比。默认: 80%，需要比STOPSUCCRATE小。<br>默认值：无<br>配置原则：无 |
| STOPSUCCRATE | 停止流控服务发现成功率(%) | 可选必选说明：可选参数<br>参数含义：该参数用于指定解控成功率。当一个周期内服务发现的平均成功率高于该值时，才可能解除流控。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~100，单位是百分比。默认: 95%，需要比STARTSUCCRATE大。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/DISCADAPTFC]] · 服务发现自适应流控NF级配置（DISCADAPTFC）

## 使用实例

修改用于发现AMF的配置，把起控成功率改为79%

```
%%MOD DISCADAPTFC: NFTYPE=NfAMF, STARTSUCCRATE=79;%%
RETCODE = 0   操作成功
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改服务发现自适应流控NF级配置（MOD-DISCADAPTFC）_10850094.md`
