# 查询服务发现自适应流控NF级配置（LST DISCADAPTFC）

- [命令功能](#ZH-CN_MMLREF_0000001363250257__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001363250257__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001363250257__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001363250257__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0000001363250257__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0000001363250257)

**适用NF：AMF、SMF、NSSF、SMSF、NCG**

该命令用于查询服务发现自适应流控NF级配置。

## [注意事项](#ZH-CN_MMLREF_0000001363250257)

无

#### [操作用户权限](#ZH-CN_MMLREF_0000001363250257)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001363250257)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFTYPE | NF类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定NF类型。<br>数据来源：本端规划<br>取值范围：仅支持可以被服务发现的NF类型。<br>- “NfInvalid（NfInvalid）”：NfInvalid<br>- “NfNRF（NfNRF）”：NfNRF<br>- “NfUDM（NfUDM）”：NfUDM<br>- “NfAMF（NfAMF）”：NfAMF<br>- “NfSMF（NfSMF）”：NfSMF<br>- “NfAUSF（NfAUSF）”：NfAUSF<br>- “NfNEF（NfNEF）”：NfNEF<br>- “NfPCF（NfPCF）”：NfPCF<br>- “NfSMSF（NfSMSF）”：NfSMSF<br>- “NfNSSF（NfNSSF）”：NfNSSF<br>- “NfUDR（NfUDR）”：NfUDR<br>- “NfLMF（NfLMF）”：NfLMF<br>- “NfGMLC（NfGMLC）”：NfGMLC<br>- “Nf5G_EIR（Nf5G_EIR）”：Nf5G_EIR<br>- “NfSEPP（NfSEPP）”：NfSEPP<br>- “NfUPF（NfUPF）”：NfUPF<br>- “NfN3IWF（NfN3IWF）”：NfN3IWF<br>- “NfAF（NfAF）”：NfAF<br>- “NfUDSF（NfUDSF）”：NfUDSF<br>- “NfBSF（NfBSF）”：NfBSF<br>- “NfCHF（NfCHF）”：NfCHF<br>- “NfCUSTOM_OCS（NfCUSTOM_OCS）”：NfCUSTOM_OCS<br>- “NfSCP（NfSCP）”：NfSCP<br>- “NfPCSCF（NfPCSCF）”：NfPCSCF<br>- “NfMBSMF（NfMBSMF）”：NfMBSMF<br>- “NfUDN（NfUDN）”：NfUDN<br>- “NfNWDAF（NfNWDAF）”：NfNWDAF<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0000001363250257)

查询用于发现AMF的配置

```
%%LST DISCADAPTFC:;%%
RETCODE = 0  操作成功

结果如下
--------
                            NF类型  =  NfAMF
启动流控最低服务发现速率阈值(次/s)  =  10
      自适应流控速率变化步长(次/s)  =  5
              流控状态变更周期(秒)  =  10
         启动流控服务发现成功率(%)  =  80
         停止流控服务发现成功率(%)  =  95
(结果个数 = 1)

---    END
```

## [输出结果说明](#ZH-CN_MMLREF_0000001363250257)

| 输出项名称 | 输出项解释 |
| --- | --- |
| NF类型 | 该参数用于指定NF类型。 |
| 启动流控最低服务发现速率阈值(次/s) | 该参数用于指定启动自适应流控的服务发现速率最低阈值，低于该值不启动也没必要启动流控。 |
| 自适应流控速率变化步长(次/s) | 该参数用于指定自适应流控速率变化步长。 |
| 流控状态变更周期(秒) | 该参数用于指定流控状态变化周期。可以理解为最少需要INTERVAL秒，该NFType才可从正常状态变为过载状态(或者从过载状态变为正常状态)。 |
| 启动流控服务发现成功率(%) | 该参数用于指定启控成功率。当一个周期内服务发现的平均成功率低于该值时，才可能启动流控。 |
| 停止流控服务发现成功率(%) | 该参数用于指定解控成功率。当一个周期内服务发现的平均成功率高于该值时，才可能解除流控。 |
