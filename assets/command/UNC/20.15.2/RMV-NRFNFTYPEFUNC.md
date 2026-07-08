---
id: UNC@20.15.2@MMLCommand@RMV NRFNFTYPEFUNC
type: MMLCommand
name: RMV NRFNFTYPEFUNC（删除基于NFType设置NRF的各类功能开关）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: NRFNFTYPEFUNC
command_category: 配置类
applicable_nf:
- NRF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- NRF业务参数
- NRF功能开关
status: active
---

# RMV NRFNFTYPEFUNC（删除基于NFType设置NRF的各类功能开关）

## 功能

**适用NF：NRF**

删除NRF基于NFType设置NRF的各类功能开关。

## 注意事项

- 该命令执行后立即生效。

- 单独删除客户端类型时，服务端类型应配置为NULL。
- 单独删除服务端类型时，客户端类型应配置为NULL。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| REQUESTNFTYPE | 客户端NF类型 | 可选必选说明：必选参数<br>参数含义：该参数用于表示客户端NF类型。<br>数据来源：本端规划<br>取值范围：<br>- NULL（空值）<br>- NRF（NRF）<br>- UDM（UDM）<br>- AMF（AMF）<br>- SMF（SMF）<br>- AUSF（AUSF）<br>- NEF（NEF）<br>- PCF（PCF）<br>- SMSF（SMSF）<br>- NSSF（NSSF）<br>- UDR（UDR）<br>- LMF（LMF）<br>- GMLC（GMLC）<br>- EIR_5G（5G_EIR）<br>- SEPP（SEPP）<br>- UPF（UPF）<br>- N3IWF（N3IWF）<br>- AF（AF）<br>- UDSF（UDSF）<br>- BSF（BSF）<br>- CHF（CHF）<br>- NWDAF（NWDAF）<br>- PCSCF（PCSCF）<br>- CUSTOM_OCS（CUSTOM_OCS）<br>- SCP（SCP）<br>- DRA（DRA）<br>- CBCF（CBCF）<br>- HSS（HSS）<br>- UCMF（UCMF）<br>- SOR_AF（SOR_AF）<br>- SPAF（SPAF）<br>- MME（MME）<br>- SCSAS（SCSAS）<br>- SCEF（SCEF）<br>- NSSAAF（NSSAAF）<br>- ICSCF（ICSCF）<br>- SCSCF（SCSCF）<br>- IMS_AS（IMS_AS）<br>- AANF（AANF）<br>- DDNMF_5G（5G_DDNMF）<br>- NSACF（NSACF）<br>- MFAF（MFAF）<br>- EASDF（EASDF）<br>- DCCF（DCCF）<br>- MB_SMF（MB_SMF）<br>- TSCTSF（TSCTSF）<br>- ADRF（ADRF）<br>- GBA_BSF（GBA_BSF）<br>- CEF（CEF）<br>- MB_UPF（MB_UPF）<br>- NSWOF（NSWOF）<br>- PKMF（PKMF）<br>- MNPF（MNPF）<br>- SMS_GMSC（SMS_GMSC）<br>- SMS_IWMSC（SMS_IWMSC）<br>- MBSF（MBSF）<br>- MBSTF（MBSTF）<br>- UDN（UDN ）<br>- PANF（PANF）<br>- DCSF（DCSF）<br>- MRF（MRF）<br>- MRFP（MRFP ）<br>- DCMF（DCMF）<br>默认值：无<br>配置原则：<br>客户端类型和服务端类型不能同时配置为NULL。<br>多条配置冲突时优先级如下：服务端+客户端>服务端>客户端。 |
| TARGETNFTYPE | 服务端NF类型 | 可选必选说明：必选参数<br>参数含义：该参数用于表示服务端NF类型。<br>数据来源：本端规划<br>取值范围：<br>- NULL（空值）<br>- NRF（NRF）<br>- UDM（UDM）<br>- AMF（AMF）<br>- SMF（SMF）<br>- AUSF（AUSF）<br>- NEF（NEF）<br>- PCF（PCF）<br>- SMSF（SMSF）<br>- NSSF（NSSF）<br>- UDR（UDR）<br>- LMF（LMF）<br>- GMLC（GMLC）<br>- EIR_5G（5G_EIR）<br>- SEPP（SEPP）<br>- UPF（UPF）<br>- N3IWF（N3IWF）<br>- AF（AF）<br>- UDSF（UDSF）<br>- BSF（BSF）<br>- CHF（CHF）<br>- NWDAF（NWDAF）<br>- PCSCF（PCSCF）<br>- CUSTOM_OCS（CUSTOM_OCS）<br>- SCP（SCP）<br>- DRA（DRA）<br>- CBCF（CBCF）<br>- HSS（HSS）<br>- UCMF（UCMF）<br>- SOR_AF（SOR_AF）<br>- SPAF（SPAF）<br>- MME（MME）<br>- SCSAS（SCSAS）<br>- SCEF（SCEF）<br>- NSSAAF（NSSAAF）<br>- ICSCF（ICSCF）<br>- SCSCF（SCSCF）<br>- IMS_AS（IMS_AS）<br>- AANF（AANF）<br>- DDNMF_5G（5G_DDNMF）<br>- NSACF（NSACF）<br>- MFAF（MFAF）<br>- EASDF（EASDF）<br>- DCCF（DCCF）<br>- MB_SMF（MB_SMF）<br>- TSCTSF（TSCTSF）<br>- ADRF（ADRF）<br>- GBA_BSF（GBA_BSF）<br>- CEF（CEF）<br>- MB_UPF（MB_UPF）<br>- NSWOF（NSWOF）<br>- PKMF（PKMF）<br>- MNPF（MNPF）<br>- SMS_GMSC（SMS_GMSC）<br>- SMS_IWMSC（SMS_IWMSC）<br>- MBSF（MBSF）<br>- MBSTF（MBSTF）<br>- UDN（UDN ）<br>- PANF（PANF）<br>- DCSF（DCSF）<br>- MRF（MRF）<br>- MRFP（MRFP ）<br>- DCMF（DCMF）<br>默认值：无<br>配置原则：<br>客户端类型和服务端类型不能同时配置为NULL。<br>多条配置冲突时优先级如下：服务端+客户端>服务端>客户端。 |

## 操作的配置对象

- [基于NFType设置NRF的各类功能开关（NRFNFTYPEFUNC）](configobject/UNC/20.15.2/NRFNFTYPEFUNC.md)

## 使用实例

运营商通过此命令删除基于NFType设置NRF的各类功能：设置客户端NF类型为AMF；服务端NF类型为UDM。

```
RMV NRFNFTYPEFUNC: REQUESTNFTYPE=AMF, TARGETNFTYPE=UDM;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除基于NFType设置NRF的各类功能开关（RMV-NRFNFTYPEFUNC）_29158013.md`
