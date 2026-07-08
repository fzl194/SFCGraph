# 查询NF向NRF注册状态（DSP NFREGNRFSTATUS）

- [命令功能](#ZH-CN_MMLREF_0212701649__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0212701649__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0212701649__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0212701649__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0212701649__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0212701649)

**适用NF：AMF、SMF、NCG、NRF、NSSF、SMSF**

查询NF向NRF注册状态。

## [注意事项](#ZH-CN_MMLREF_0212701649)

无

#### [操作用户权限](#ZH-CN_MMLREF_0212701649)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0212701649)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFINSTANCENAME | NF实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于显示NF实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~36。<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0212701649)

查询NF向NRF注册状态。

```
%%DSP NFREGNRFSTATUS:;%%
RETCODE = 0  操作成功

结果如下
--------
  NF实例名称  =  AMF_Instance_0
      NF类型  =  NfAMF
 NRF实例名称  =  NRF_Instance_0
  NF注册状态  =  Success/Registered
注册成功时间  =  2024-08-25T04:53:07+08:00
注册失败原因  =  Normal
    失败次数  =  0
  重注册时间  =  NULL
(结果个数 = 1)

---    END
```

## [输出结果说明](#ZH-CN_MMLREF_0212701649)

| 输出项名称 | 输出项解释 |
| --- | --- |
| NF实例名称 | 该参数用于显示NF实例名称。 |
| NF类型 | 该参数用于显示NF类型。<br>取值说明：<br>- “NfInvalid（NfInvalid）”：NfInvalid<br>- “NfNRF（NfNRF）”：NfNRF<br>- “NfUDM（NfUDM）”：NfUDM<br>- “NfAMF（NfAMF）”：NfAMF<br>- “NfSMF（NfSMF）”：NfSMF<br>- “NfAUSF（NfAUSF）”：NfAUSF<br>- “NfNEF（NfNEF）”：NfNEF<br>- “NfPCF（NfPCF）”：NfPCF<br>- “NfSMSF（NfSMSF）”：NfSMSF<br>- “NfNSSF（NfNSSF）”：NfNSSF<br>- “NfUDR（NfUDR）”：NfUDR<br>- “NfLMF（NfLMF）”：NfLMF<br>- “NfGMLC（NfGMLC）”：NfGMLC<br>- “Nf5G_EIR（Nf5G_EIR）”：Nf5G_EIR<br>- “NfSEPP（NfSEPP）”：NfSEPP<br>- “NfUPF（NfUPF）”：NfUPF<br>- “NfN3IWF（NfN3IWF）”：NfN3IWF<br>- “NfAF（NfAF）”：NfAF<br>- “NfUDSF（NfUDSF）”：NfUDSF<br>- “NfBSF（NfBSF）”：NfBSF<br>- “NfCHF（NfCHF）”：NfCHF<br>- “NfCUSTOM_OCS（NfCUSTOM_OCS）”：NfCUSTOM_OCS<br>- “NfSCP（NfSCP）”：NfSCP<br>- “NfPCSCF（NfPCSCF）”：NfPCSCF<br>- “NfMBSMF（NfMBSMF）”：NfMBSMF<br>- “NfUDN（NfUDN）”：NfUDN<br>- “NfNWDAF（NfNWDAF）”：NfNWDAF |
| NRF实例名称 | 该参数用于显示当前注册的NRF实例名称。 |
| NF注册状态 | 该参数用于显示NF的注册状态。 |
| 注册成功时间 | 该参数用于显示NF成功的时间。 |
| 注册失败原因 | 该参数用于显示NF注册失败的原因。 |
| 失败次数 | 该参数用于显示向NRF连续注册失败的次数。 |
| 重注册时间 | 该参数用于显示下一次重新注册的时间。如果值为1970-01-01T08:00:00+08:00，则说明没有注册失败进行注册退避，可以忽略。 |
