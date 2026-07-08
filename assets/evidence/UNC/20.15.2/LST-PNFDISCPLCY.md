# 查询对端NF的服务发现策略（LST PNFDISCPLCY）

- [命令功能](#ZH-CN_MMLREF_0000001921742349__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001921742349__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001921742349__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001921742349__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0000001921742349__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0000001921742349)

**适用NF：AMF、SMF、NRF、NSSF、NCG**

该命令用于查询对端NF的服务发现策略。

## [注意事项](#ZH-CN_MMLREF_0000001921742349)

无

#### [操作用户权限](#ZH-CN_MMLREF_0000001921742349)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001921742349)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFTYPE | NF类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定对端NF类型。<br>数据来源：本端规划<br>取值范围：<br>- “NfInvalid（NfInvalid）”：NfInvalid<br>- “NfNRF（NfNRF）”：NfNRF<br>- “NfUDM（NfUDM）”：NfUDM<br>- “NfAMF（NfAMF）”：NfAMF<br>- “NfSMF（NfSMF）”：NfSMF<br>- “NfAUSF（NfAUSF）”：NfAUSF<br>- “NfNEF（NfNEF）”：NfNEF<br>- “NfPCF（NfPCF）”：NfPCF<br>- “NfSMSF（NfSMSF）”：NfSMSF<br>- “NfNSSF（NfNSSF）”：NfNSSF<br>- “NfUDR（NfUDR）”：NfUDR<br>- “NfLMF（NfLMF）”：NfLMF<br>- “NfGMLC（NfGMLC）”：NfGMLC<br>- “Nf5G_EIR（Nf5G_EIR）”：Nf5G_EIR<br>- “NfSEPP（NfSEPP）”：NfSEPP<br>- “NfUPF（NfUPF）”：NfUPF<br>- “NfN3IWF（NfN3IWF）”：NfN3IWF<br>- “NfAF（NfAF）”：NfAF<br>- “NfUDSF（NfUDSF）”：NfUDSF<br>- “NfBSF（NfBSF）”：NfBSF<br>- “NfCHF（NfCHF）”：NfCHF<br>- “NfCUSTOM_OCS（NfCUSTOM_OCS）”：NfCUSTOM_OCS<br>- “NfSCP（NfSCP）”：NfSCP<br>- “NfPCSCF（NfPCSCF）”：NfPCSCF<br>- “NfMBSMF（NfMBSMF）”：NfMBSMF<br>- “NfUDN（NfUDN）”：NfUDN<br>- “NfNWDAF（NfNWDAF）”：NfNWDAF<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0000001921742349)

查询NFType为NfSMF的对端NF的服务发现策略。

```
%%LST PNFDISCPLCY: NFTYPE=NfSMF;%%
RETCODE = 0  Operation succeeded

The result is as follows
------------------------
NF类型  =  NfSMF
 服务发现策略  =  LOCAL_ONLY
(结果个数 = 1)

---    END
```

## [输出结果说明](#ZH-CN_MMLREF_0000001921742349)

| 输出项名称 | 输出项解释 |
| --- | --- |
| NF类型 | 该参数用于指定对端NF类型。 |
| 服务发现策略 | 该参数用于指定服务发现策略。 |
