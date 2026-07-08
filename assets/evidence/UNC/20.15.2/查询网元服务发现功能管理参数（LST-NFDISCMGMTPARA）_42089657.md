# 查询网元服务发现功能管理参数（LST NFDISCMGMTPARA）

- [命令功能](#ZH-CN_MMLREF_0000001142089657__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001142089657__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001142089657__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001142089657__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0000001142089657__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0000001142089657)

**适用NF：AMF、SMF、NCG、SMSF**

该命令用于查询网元服务发现功能管理参数。

## [注意事项](#ZH-CN_MMLREF_0000001142089657)

无

#### [操作用户权限](#ZH-CN_MMLREF_0000001142089657)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001142089657)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFTYPE | 网元类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定目标NF类型。<br>数据来源：本端规划<br>取值范围：<br>- “NfNRF（NfNRF）”：NfNRF<br>- “NfUDM（NfUDM）”：NfUDM<br>- “NfAMF（NfAMF）”：NfAMF<br>- “NfSMF（NfSMF）”：NfSMF<br>- “NfAUSF（NfAUSF）”：NfAUSF<br>- “NfNEF（NfNEF）”：NfNEF<br>- “NfPCF（NfPCF）”：NfPCF<br>- “NfSMSF（NfSMSF）”：NfSMSF<br>- “NfNSSF（NfNSSF）”：NfNSSF<br>- “NfUDR（NfUDR）”：NfUDR<br>- “NfLMF（NfLMF）”：NfLMF<br>- “NfGMLC（NfGMLC）”：NfGMLC<br>- “Nf5G_EIR（Nf5G_EIR）”：Nf5G_EIR<br>- “NfSEPP（NfSEPP）”：NfSEPP<br>- “NfUPF（NfUPF）”：NfUPF<br>- “NfN3IWF（NfN3IWF）”：NfN3IWF<br>- “NfAF（NfAF）”：NfAF<br>- “NfUDSF（NfUDSF）”：NfUDSF<br>- “NfBSF（NfBSF）”：NfBSF<br>- “NfCHF（NfCHF）”：NfCHF<br>- “NfCUSTOM_OCS（NfCUSTOM_OCS）”：NfCUSTOM_OCS<br>- “NfSCP（NfSCP）”：NfSCP<br>- “NfPCSCF（NfPCSCF）”：NfPCSCF<br>- “NfMBSMF（NfMBSMF）”：NfMBSMF<br>- “NWDAF（NWDAF）”：NWDAF<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0000001142089657)

查询AMF相关的网元服务发现功能管理参数：

```
%%LST NFDISCMGMTPARA: NFTYPE=NfAMF;%%
RETCODE = 0  操作成功

结果如下
--------
          网元类型  =  NfAMF
 TAI精细化选择开关  =  ON
SUPI精细化选择开关  =  OFF
GPSI精细化选择开关  =  OFF
(结果个数 = 1)

---    END
```

## [输出结果说明](#ZH-CN_MMLREF_0000001142089657)

| 输出项名称 | 输出项解释 |
| --- | --- |
| 网元类型 | 该参数用于指定目标NF类型。 |
| TAI精细化选择开关 | 该参数用于指定服务发现过程中是否开启TAI精细化选择功能。若开关设置为ON时，服务发现会优选TAI区间更精细的网元。若开关设置为OFF时，服务发现不开启TAI精细化选择功能。精细化选择功能仅作用于本地配置命中或者缓存命中的服务发现结果。顺序在优先级选择功能在之后，在本大区locality优选之前。 |
| SUPI精细化选择开关 | 该参数用于指定服务发现过程中是否开启SUPI精细化选择功能。若开关设置为ON时，服务发现会优选SUPI区间更精细的网元。若开关设置为OFF时，服务发现不开启SUPI精细化选择功能。精细化选择功能仅作用于本地配置命中或者缓存命中的服务发现结果。顺序在优先级选择功能在之后，在本大区locality优选之前。 |
| GPSI精细化选择开关 | 该参数用于指定服务发现过程中是否开启GPSI精细化选择功能。若开关设置为ON时，服务发现会优选GPSI区间更精细的网元。若开关设置为OFF时，服务发现不开启GPSI精细化选择功能。精细化选择功能仅作用于本地配置命中或者缓存命中的服务发现结果。顺序在优先级选择功能在之后，在本大区locality优选之前。 |
