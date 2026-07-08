# 修改服务发现Service负载均衡功能（MOD NFDISCSRVLBSW）

- [命令功能](#ZH-CN_MMLREF_0000001304536948__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001304536948__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001304536948__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001304536948__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0000001304536948)

**适用NF：AMF、SMF、NSSF、SMSF、NCG**

该命令用于修改服务发现时的NF Service负载均衡功能。

## [注意事项](#ZH-CN_MMLREF_0000001304536948)

该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_MMLREF_0000001304536948)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001304536948)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TARGETNFTYPE | 对端NF类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定对端NF类型。<br>数据来源：本端规划<br>取值范围：<br>- “NfInvalid（NfInvalid）”：NfInvalid<br>- “NfNRF（NfNRF）”：NfNRF<br>- “NfUDM（NfUDM）”：NfUDM<br>- “NfAMF（NfAMF）”：NfAMF<br>- “NfSMF（NfSMF）”：NfSMF<br>- “NfAUSF（NfAUSF）”：NfAUSF<br>- “NfNEF（NfNEF）”：NfNEF<br>- “NfPCF（NfPCF）”：NfPCF<br>- “NfSMSF（NfSMSF）”：NfSMSF<br>- “NfNSSF（NfNSSF）”：NfNSSF<br>- “NfUDR（NfUDR）”：NfUDR<br>- “NfLMF（NfLMF）”：NfLMF<br>- “NfGMLC（NfGMLC）”：NfGMLC<br>- “Nf5G_EIR（Nf5G_EIR）”：Nf5G_EIR<br>- “NfSEPP（NfSEPP）”：NfSEPP<br>- “NfUPF（NfUPF）”：NfUPF<br>- “NfN3IWF（NfN3IWF）”：NfN3IWF<br>- “NfAF（NfAF）”：NfAF<br>- “NfUDSF（NfUDSF）”：NfUDSF<br>- “NfBSF（NfBSF）”：NfBSF<br>- “NfCHF（NfCHF）”：NfCHF<br>- “NfCUSTOM_OCS（NfCUSTOM_OCS）”：NfCUSTOM_OCS<br>- “NfSCP（NfSCP）”：NfSCP<br>- “NfPCSCF（NfPCSCF）”：NfPCSCF<br>- “NfMBSMF（NfMBSMF）”：NfMBSMF<br>- “NfUDN（NfUDN）”：NfUDN<br>- “NfNWDAF（NfNWDAF）”：NfNWDAF<br>默认值：无<br>配置原则：无 |
| LBSWITCH | 负载均衡开关 | 可选必选说明：必选参数<br>参数含义：该参数用于指定是否开启NF Service负载均衡功能。<br>数据来源：本端规划<br>取值范围：<br>- “OFF（OFF）”：功能关闭<br>- “ON（ON）”：功能开启<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0000001304536948)

修改服务发现UDM时的NF Service负载均衡功能。

```
MOD NFDISCSRVLBSW: TARGETNFTYPE=NfUDM, LBSWITCH=OFF;
```
