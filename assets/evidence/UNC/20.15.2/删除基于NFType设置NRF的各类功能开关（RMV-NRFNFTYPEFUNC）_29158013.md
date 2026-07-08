# 删除基于NFType设置NRF的各类功能开关（RMV NRFNFTYPEFUNC）

- [命令功能](#ZH-CN_MMLREF_0000001929158013__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001929158013__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001929158013__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001929158013__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0000001929158013)

**适用NF：NRF**

删除NRF基于NFType设置NRF的各类功能开关。

## [注意事项](#ZH-CN_MMLREF_0000001929158013)

- 该命令执行后立即生效。

- 单独删除客户端类型时，服务端类型应配置为NULL。
- 单独删除服务端类型时，客户端类型应配置为NULL。

#### [操作用户权限](#ZH-CN_MMLREF_0000001929158013)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001929158013)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| REQUESTNFTYPE | 客户端NF类型 | 可选必选说明：必选参数<br>参数含义：该参数用于表示客户端NF类型。<br>数据来源：本端规划<br>取值范围：<br>- NULL（空值）<br>- NRF（NRF）<br>- UDM（UDM）<br>- AMF（AMF）<br>- SMF（SMF）<br>- AUSF（AUSF）<br>- NEF（NEF）<br>- PCF（PCF）<br>- SMSF（SMSF）<br>- NSSF（NSSF）<br>- UDR（UDR）<br>- LMF（LMF）<br>- GMLC（GMLC）<br>- EIR_5G（5G_EIR）<br>- SEPP（SEPP）<br>- UPF（UPF）<br>- N3IWF（N3IWF）<br>- AF（AF）<br>- UDSF（UDSF）<br>- BSF（BSF）<br>- CHF（CHF）<br>- NWDAF（NWDAF）<br>- PCSCF（PCSCF）<br>- CUSTOM_OCS（CUSTOM_OCS）<br>- SCP（SCP）<br>- DRA（DRA）<br>- CBCF（CBCF）<br>- HSS（HSS）<br>- UCMF（UCMF）<br>- SOR_AF（SOR_AF）<br>- SPAF（SPAF）<br>- MME（MME）<br>- SCSAS（SCSAS）<br>- SCEF（SCEF）<br>- NSSAAF（NSSAAF）<br>- ICSCF（ICSCF）<br>- SCSCF（SCSCF）<br>- IMS_AS（IMS_AS）<br>- AANF（AANF）<br>- DDNMF_5G（5G_DDNMF）<br>- NSACF（NSACF）<br>- MFAF（MFAF）<br>- EASDF（EASDF）<br>- DCCF（DCCF）<br>- MB_SMF（MB_SMF）<br>- TSCTSF（TSCTSF）<br>- ADRF（ADRF）<br>- GBA_BSF（GBA_BSF）<br>- CEF（CEF）<br>- MB_UPF（MB_UPF）<br>- NSWOF（NSWOF）<br>- PKMF（PKMF）<br>- MNPF（MNPF）<br>- SMS_GMSC（SMS_GMSC）<br>- SMS_IWMSC（SMS_IWMSC）<br>- MBSF（MBSF）<br>- MBSTF（MBSTF）<br>- UDN（UDN ）<br>- PANF（PANF）<br>- DCSF（DCSF）<br>- MRF（MRF）<br>- MRFP（MRFP ）<br>- DCMF（DCMF）<br>默认值：无<br>配置原则：<br>客户端类型和服务端类型不能同时配置为NULL。<br>多条配置冲突时优先级如下：服务端+客户端>服务端>客户端。 |
| TARGETNFTYPE | 服务端NF类型 | 可选必选说明：必选参数<br>参数含义：该参数用于表示服务端NF类型。<br>数据来源：本端规划<br>取值范围：<br>- NULL（空值）<br>- NRF（NRF）<br>- UDM（UDM）<br>- AMF（AMF）<br>- SMF（SMF）<br>- AUSF（AUSF）<br>- NEF（NEF）<br>- PCF（PCF）<br>- SMSF（SMSF）<br>- NSSF（NSSF）<br>- UDR（UDR）<br>- LMF（LMF）<br>- GMLC（GMLC）<br>- EIR_5G（5G_EIR）<br>- SEPP（SEPP）<br>- UPF（UPF）<br>- N3IWF（N3IWF）<br>- AF（AF）<br>- UDSF（UDSF）<br>- BSF（BSF）<br>- CHF（CHF）<br>- NWDAF（NWDAF）<br>- PCSCF（PCSCF）<br>- CUSTOM_OCS（CUSTOM_OCS）<br>- SCP（SCP）<br>- DRA（DRA）<br>- CBCF（CBCF）<br>- HSS（HSS）<br>- UCMF（UCMF）<br>- SOR_AF（SOR_AF）<br>- SPAF（SPAF）<br>- MME（MME）<br>- SCSAS（SCSAS）<br>- SCEF（SCEF）<br>- NSSAAF（NSSAAF）<br>- ICSCF（ICSCF）<br>- SCSCF（SCSCF）<br>- IMS_AS（IMS_AS）<br>- AANF（AANF）<br>- DDNMF_5G（5G_DDNMF）<br>- NSACF（NSACF）<br>- MFAF（MFAF）<br>- EASDF（EASDF）<br>- DCCF（DCCF）<br>- MB_SMF（MB_SMF）<br>- TSCTSF（TSCTSF）<br>- ADRF（ADRF）<br>- GBA_BSF（GBA_BSF）<br>- CEF（CEF）<br>- MB_UPF（MB_UPF）<br>- NSWOF（NSWOF）<br>- PKMF（PKMF）<br>- MNPF（MNPF）<br>- SMS_GMSC（SMS_GMSC）<br>- SMS_IWMSC（SMS_IWMSC）<br>- MBSF（MBSF）<br>- MBSTF（MBSTF）<br>- UDN（UDN ）<br>- PANF（PANF）<br>- DCSF（DCSF）<br>- MRF（MRF）<br>- MRFP（MRFP ）<br>- DCMF（DCMF）<br>默认值：无<br>配置原则：<br>客户端类型和服务端类型不能同时配置为NULL。<br>多条配置冲突时优先级如下：服务端+客户端>服务端>客户端。 |

## [使用实例](#ZH-CN_MMLREF_0000001929158013)

运营商通过此命令删除基于NFType设置NRF的各类功能：设置客户端NF类型为AMF；服务端NF类型为UDM。

```
RMV NRFNFTYPEFUNC: REQUESTNFTYPE=AMF, TARGETNFTYPE=UDM;
```
