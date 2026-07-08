# 查询NF支持的网络切片（LST NFNS）

- [命令功能](#ZH-CN_MMLREF_0209651556__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0209651556__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0209651556__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0209651556__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0209651556__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0209651556)

**适用NF：AMF、SMF、NSSF**

该命令用以查询指定的NF所支持的网络切片。

## [注意事项](#ZH-CN_MMLREF_0209651556)

无

#### [操作用户权限](#ZH-CN_MMLREF_0209651556)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0209651556)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFTYPE | NF类型 | 可选必选说明：可选参数<br>参数含义：该参数用于表示NF类型。<br>数据来源：本端规划<br>取值范围：<br>- “NfInvalid（NfInvalid）”：无效的NF<br>- “NfNRF（NfNRF）”：NRF<br>- “NfUDM（NfUDM）”：UDM<br>- “NfAMF（NfAMF）”：AMF<br>- “NfSMF（NfSMF）”：SMF<br>- “NfAUSF（NfAUSF）”：AUSF<br>- “NfNEF（NfNEF）”：NEF<br>- “NfPCF（NfPCF）”：PCF<br>- “NfSMSF（NfSMSF）”：SMSF<br>- “NfNSSF（NfNSSF）”：NSSF<br>- “NfUDR（NfUDR）”：UDR<br>- “NfLMF（NfLMF）”：LMF<br>- “NfGMLC（NfGMLC）”：GMLC<br>- “Nf5G_EIR（Nf5G_EIR）”：5G_EIR<br>- “NfSEPP（NfSEPP）”：SEPP<br>- “NfUPF（NfUPF）”：UPF<br>- “NfN3IWF（NfN3IWF）”：N3IWF<br>- “NfAF（NfAF）”：AF<br>- “NfUDSF（NfUDSF）”：UDSF<br>- “NfBSF（NfBSF）”：BSF<br>- “NfCHF（NfCHF）”：CHF<br>- “NfNWDAF（NfNWDAF）”：NWDAF<br>- “NfTypeMAX（NfTypeMAX）”：NfTypeMAX<br>- “NfMBSMF（NfMBSMF）”：MBSMF<br>- “NfCBCF（NfCBCF）”：NfCBCF<br>- “NfSCF（NfSCF）”：NfSCF<br>- “NfSPF（NfSPF）”：NfSPF<br>默认值：无<br>配置原则：无 |
| NSIDX | 网络切片索引 | 可选必选说明：可选参数<br>参数含义：该参数在系统中唯一标识某个网络切片。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~4294967295。本参数通过ADD PLMNNS命令进行配置。<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0209651556)

- 查询AMF支持的网络切片列表，执行如下命令：
  ```
  %%LST NFNS: NFTYPE=NfAMF;%%
  RETCODE = 0  操作成功

  结果如下
  --------
        NF类型  =  NfAMF
  网络切片索引  =  0
      描述信息  =  NULL
  (结果个数 = 1)

  ---    END
  ```
- 查询所有NF支持的网络切片列表，执行如下命令：
  ```
  %%LST NFNS:;%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
  NF类型   网络切片索引         描述信息  

  NfAMF    0                    NULL         
  NfSMF    0                    NULL         
  (结果个数 = 2)

  ---    END
  ```

## [输出结果说明](#ZH-CN_MMLREF_0209651556)

| 输出项名称 | 输出项解释 |
| --- | --- |
| NF类型 | 该参数用于表示NF类型。 |
| 网络切片索引 | 该参数在系统中唯一标识某个网络切片。 |
| 描述信息 | 该参数表示对网络切片的描述信息。 |
