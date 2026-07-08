# 查询对端网元的通知抑制时间（LST PNFNTFPLCY）

- [命令功能](#ZH-CN_MMLREF_0296242392__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0296242392__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0296242392__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0296242392__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0296242392__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0296242392)

**适用NF：AMF、SMF、SMSF**

该命令用于查询对端网元的通知抑制时间。

## [注意事项](#ZH-CN_MMLREF_0296242392)

无

#### [操作用户权限](#ZH-CN_MMLREF_0296242392)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0296242392)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFTYPE | NF类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定NF类型。<br>数据来源：全网规划<br>取值范围：<br>- “NfInvalid（NfInvalid）”：NfInvalid<br>- “NfNRF（NfNRF）”：NfNRF<br>- “NfUDM（NfUDM）”：NfUDM<br>- “NfAMF（NfAMF）”：NfAMF<br>- “NfSMF（NfSMF）”：NfSMF<br>- “NfAUSF（NfAUSF）”：NfAUSF<br>- “NfNEF（NfNEF）”：NfNEF<br>- “NfPCF（NfPCF）”：NfPCF<br>- “NfSMSF（NfSMSF）”：NfSMSF<br>- “NfNSSF（NfNSSF）”：NfNSSF<br>- “NfUDR（NfUDR）”：NfUDR<br>- “NfLMF（NfLMF）”：NfLMF<br>- “NfGMLC（NfGMLC）”：NfGMLC<br>- “Nf5G_EIR（Nf5G_EIR）”：Nf5G_EIR<br>- “NfSEPP（NfSEPP）”：NfSEPP<br>- “NfUPF（NfUPF）”：NfUPF<br>- “NfN3IWF（NfN3IWF）”：NfN3IWF<br>- “NfAF（NfAF）”：NfAF<br>- “NfUDSF（NfUDSF）”：NfUDSF<br>- “NfBSF（NfBSF）”：NfBSF<br>- “NfCHF（NfCHF）”：NfCHF<br>- “NfCUSTOM_OCS（NfCUSTOM_OCS）”：NfCUSTOM_OCS<br>- “NfSCP（NfSCP）”：NfSCP<br>- “NfPCSCF（NfPCSCF）”：NfPCSCF<br>- “NfMBSMF（NfMBSMF）”：NfMBSMF<br>- “NfUDN（NfUDN）”：NfUDN<br>- “NfNWDAF（NfNWDAF）”：NfNWDAF<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0296242392)

查询对端网元SMF的通知抑制时间。

```
%%LST PNFNTFPLCY: NFTYPE=NfSMF;%%
RETCODE = 0 操作成功

结果如下
--------
              网元类型 = NfSMF
          通知抑制时间(分钟) = 10
（结果个数 = 1）

----  END
```

## [输出结果说明](#ZH-CN_MMLREF_0296242392)

| 输出项名称 | 输出项解释 |
| --- | --- |
| NF类型 | 该参数用于指定NF类型。 |
| 通知抑制时间(分钟) | 参数用于指定向本端NF通知对端NF状态变更的抑制时间(分钟)。 |
