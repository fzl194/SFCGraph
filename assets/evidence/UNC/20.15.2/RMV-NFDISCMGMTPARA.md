# 删除网元服务发现功能管理参数（RMV NFDISCMGMTPARA）

- [命令功能](#ZH-CN_MMLREF_0000001141969689__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001141969689__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001141969689__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001141969689__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0000001141969689)

**适用NF：AMF、SMF、NCG、SMSF**

该命令用于删除网元服务发现功能管理参数。

## [注意事项](#ZH-CN_MMLREF_0000001141969689)

该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_MMLREF_0000001141969689)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001141969689)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFTYPE | 网元类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定目标NF类型。<br>数据来源：本端规划<br>取值范围：<br>- “NfNRF（NfNRF）”：NfNRF<br>- “NfUDM（NfUDM）”：NfUDM<br>- “NfAMF（NfAMF）”：NfAMF<br>- “NfSMF（NfSMF）”：NfSMF<br>- “NfAUSF（NfAUSF）”：NfAUSF<br>- “NfNEF（NfNEF）”：NfNEF<br>- “NfPCF（NfPCF）”：NfPCF<br>- “NfSMSF（NfSMSF）”：NfSMSF<br>- “NfNSSF（NfNSSF）”：NfNSSF<br>- “NfUDR（NfUDR）”：NfUDR<br>- “NfLMF（NfLMF）”：NfLMF<br>- “NfGMLC（NfGMLC）”：NfGMLC<br>- “Nf5G_EIR（Nf5G_EIR）”：Nf5G_EIR<br>- “NfSEPP（NfSEPP）”：NfSEPP<br>- “NfUPF（NfUPF）”：NfUPF<br>- “NfN3IWF（NfN3IWF）”：NfN3IWF<br>- “NfAF（NfAF）”：NfAF<br>- “NfUDSF（NfUDSF）”：NfUDSF<br>- “NfBSF（NfBSF）”：NfBSF<br>- “NfCHF（NfCHF）”：NfCHF<br>- “NfCUSTOM_OCS（NfCUSTOM_OCS）”：NfCUSTOM_OCS<br>- “NfSCP（NfSCP）”：NfSCP<br>- “NfPCSCF（NfPCSCF）”：NfPCSCF<br>- “NfMBSMF（NfMBSMF）”：NfMBSMF<br>- “NWDAF（NWDAF）”：NWDAF<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0000001141969689)

删除AMF相关的网元服务发现功能管理参数，执行如下命令：

```
RMV NFDISCMGMTPARA:NFTYPE=NfAMF;
```
