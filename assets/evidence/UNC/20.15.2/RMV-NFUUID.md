# 删除NF UUID信息（RMV NFUUID）

- [命令功能](#ZH-CN_MMLREF_0209652547__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0209652547__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0209652547__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0209652547__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0209652547)

![](删除NF UUID信息（RMV NFUUID）_09652547.assets/notice_3.0-zh-cn_2.png)

如果未执行ACT NFOFFLINE就执行该命令，可能导致不可预知的系统异常及重大业务影响。

**适用NF：AMF、SMF、NRF、NSSF、SMSF、NCG、CBCF、SPF**

该命令用于删除NF实例标识（UUID）。删除UUID可能导致NF无法和其他NF正常通信，请谨慎操作。

## [注意事项](#ZH-CN_MMLREF_0209652547)

- 该命令执行后立即生效。

- 当NFINSTANCENAME参数被AMFINFO，ALLOWEDNFDOMAIN，ALLOWEDNFNS，ALLOWEDPLMN，N2INFAMFINFO，NFPROFILE，NFSERVICE，NFSERVICEVER，NFSRVNTFSUBS，NFTAI，NSILIST，NFSRVSCOPE，TAIRANGELIST，BSFINFO，BSFIPRANGEBIND，SMFINFO命令关联时，不能执行此命令。
- 对于已经存在的NF实例，若要修改其NF实例标识，则必须在修改后通过RMV SBIAPLE和ADD SBIAPLE命令删除并重建链路集。重建链路集会导致所有链路短暂中断。

#### [操作用户权限](#ZH-CN_MMLREF_0209652547)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0209652547)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFTYPE | NF类型 | 可选必选说明：必选参数<br>参数含义：本参数用于指定NF类型。<br>数据来源：全网规划<br>取值范围：<br>- NfInvalid（NfInvalid）<br>- NfNRF（NfNRF）<br>- NfUDM（NfUDM）<br>- NfAMF（NfAMF）<br>- NfSMF（NfSMF）<br>- NfAUSF（NfAUSF）<br>- NfNEF（NfNEF）<br>- NfPCF（NfPCF）<br>- NfSMSF（NfSMSF）<br>- NfNSSF（NfNSSF）<br>- NfUDR（NfUDR）<br>- NfLMF（NfLMF）<br>- NfGMLC（NfGMLC）<br>- Nf5G_EIR（Nf5G_EIR）<br>- NfSEPP（NfSEPP）<br>- NfUPF（NfUPF）<br>- NfN3IWF（NfN3IWF）<br>- NfAF（NfAF）<br>- NfUDSF（NfUDSF）<br>- NfBSF（NfBSF）<br>- NfCHF（NfCHF）<br>- NfNWDAF（NfNWDAF）<br>- “NfTypeMAX（NfTypeMAX）”：已废弃。<br>- NfMBSMF（NfMBSMF）<br>- NfCBCF（NfCBCF）<br>- NfSCF（NfSCF）<br>- NfSPF（NfSPF）<br>默认值：无<br>配置原则：<br>仅可以选择网元支持的NF实例。 |

## [使用实例](#ZH-CN_MMLREF_0209652547)

运营商需要删除类型为NfAMF实例对应的NF实例标识。

```
RMV NFUUID: NFTYPE=NfAMF;
```
