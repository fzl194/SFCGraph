---
id: UNC@20.15.2@MMLCommand@RMV SUBCONDITION
type: MMLCommand
name: RMV SUBCONDITION（删除NF订阅条件）
nf: UNC
version: 20.15.2
verb: RMV
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

# RMV SUBCONDITION（删除NF订阅条件）

## 功能

**适用NF：AMF、SMF、NRF、NSSF、SMSF、NCG**

该命令用于删除订阅的目标NF类型的订阅条件等信息。

## 注意事项

- 该命令执行后立即生效。

- 该命令只删除订阅条件，对于已经生成的订阅无法生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFTYPE | NF类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定订阅的目标NF类型。<br>数据来源：本端规划<br>取值范围：<br>- “NfInvalid（NfInvalid）”：NfInvalid<br>- “NfNRF（NfNRF）”：NfNRF<br>- “NfUDM（NfUDM）”：NfUDM<br>- “NfAMF（NfAMF）”：NfAMF<br>- “NfSMF（NfSMF）”：NfSMF<br>- “NfAUSF（NfAUSF）”：NfAUSF<br>- “NfNEF（NfNEF）”：NfNEF<br>- “NfPCF（NfPCF）”：NfPCF<br>- “NfSMSF（NfSMSF）”：NfSMSF<br>- “NfNSSF（NfNSSF）”：NfNSSF<br>- “NfUDR（NfUDR）”：NfUDR<br>- “NfLMF（NfLMF）”：NfLMF<br>- “NfGMLC（NfGMLC）”：NfGMLC<br>- “Nf5G_EIR（Nf5G_EIR）”：Nf5G_EIR<br>- “NfSEPP（NfSEPP）”：NfSEPP<br>- “NfUPF（NfUPF）”：NfUPF<br>- “NfN3IWF（NfN3IWF）”：NfN3IWF<br>- “NfAF（NfAF）”：NfAF<br>- “NfUDSF（NfUDSF）”：NfUDSF<br>- “NfBSF（NfBSF）”：NfBSF<br>- “NfCHF（NfCHF）”：NfCHF<br>- “NfCUSTOM_OCS（NfCUSTOM_OCS）”：NfCUSTOM_OCS<br>- “NfSCP（NfSCP）”：NfSCP<br>- “NfPCSCF（NfPCSCF）”：NfPCSCF<br>- “NfMBSMF（NfMBSMF）”：NfMBSMF<br>- “NfUDN（NfUDN）”：NfUDN<br>- “NfNWDAF（NfNWDAF）”：NfNWDAF<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SUBCONDITION]] · NF订阅条件（SUBCONDITION）

## 使用实例

删除目标NF类型为NfAMF的订阅条件信息。

```
RMV SUBCONDITION: NFTYPE=NfAMF;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-SUBCONDITION.md`
