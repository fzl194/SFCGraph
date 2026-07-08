---
id: UNC@20.15.2@MMLCommand@DSP NFCACHE
type: MMLCommand
name: DSP NFCACHE（查询NF缓存信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: NFCACHE
command_category: 查询类
applicable_nf:
- AMF
- SMF
- NRF
- NSSF
- NCG
- SMSF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 服务化接口管理
- 注册与服务发现
- NF Cache管理
status: active
---

# DSP NFCACHE（查询NF缓存信息）

## 功能

**适用NF：AMF、SMF、NRF、NSSF、NCG、SMSF**

该命令用于查询当前NF存储的对端NF信息。当前NF存储的对端NF信息包括如下两部分：

缓存数据：在通过NRF进行NF发现时，NRF向本端NF返回的对端NF信息。如果本端NF订阅了对端NF信息，NRF会在对端NF信息变化时向本端NF发送对端NF信息。这些对端NF信息会在本端NF上进行缓存。在缓存有效时长内，该系统中的NF实例再次服务发现相同NF实例时，可以直接使用缓存中的结果，不需要再去NRF上处理。超过缓存有效时间， 服务发现结果缓存数据将被清除。

本地数据：本地配置的对端NF信息。

## 注意事项

以SUPI和GPSI作为查询条件时，会根据通配开关，选择是否返回支持通配的NF。当通配开关打开时，会返回所有支持通配的NF。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QUERYTYPE | 查询类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定查询类型。<br>数据来源：本端规划<br>取值范围：<br>- “NFType（NFType）”：NF类型<br>- “NFID（NFInstanceId）”：NF实例标识<br>- SUPI（SUPI）<br>- GPSI（GPSI）<br>默认值：无<br>配置原则：无 |
| NFID | NF实例标识 | 可选必选说明：该参数在"QUERYTYPE"配置为"NFID"时为条件必选参数。<br>参数含义：本参数用于指定NF实例标识。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~50。<br>默认值：无<br>配置原则：无 |
| NFTYPE | NF类型 | 可选必选说明：该参数在"QUERYTYPE"配置为"NFType"、"SUPI"、"GPSI"时为条件可选参数。<br>参数含义：该参数用于指定NF类型。<br>数据来源：本端规划<br>取值范围：<br>- “NfInvalid（NfInvalid）”：NfInvalid<br>- “NfNRF（NfNRF）”：NfNRF<br>- “NfUDM（NfUDM）”：NfUDM<br>- “NfAMF（NfAMF）”：NfAMF<br>- “NfSMF（NfSMF）”：NfSMF<br>- “NfAUSF（NfAUSF）”：NfAUSF<br>- “NfNEF（NfNEF）”：NfNEF<br>- “NfPCF（NfPCF）”：NfPCF<br>- “NfSMSF（NfSMSF）”：NfSMSF<br>- “NfNSSF（NfNSSF）”：NfNSSF<br>- “NfUDR（NfUDR）”：NfUDR<br>- “NfLMF（NfLMF）”：NfLMF<br>- “NfGMLC（NfGMLC）”：NfGMLC<br>- “Nf5G_EIR（Nf5G_EIR）”：Nf5G_EIR<br>- “NfSEPP（NfSEPP）”：NfSEPP<br>- “NfUPF（NfUPF）”：NfUPF<br>- “NfN3IWF（NfN3IWF）”：NfN3IWF<br>- “NfAF（NfAF）”：NfAF<br>- “NfUDSF（NfUDSF）”：NfUDSF<br>- “NfBSF（NfBSF）”：NfBSF<br>- “NfCHF（NfCHF）”：NfCHF<br>- “NfCUSTOM_OCS（NfCUSTOM_OCS）”：NfCUSTOM_OCS<br>- “NfSCP（NfSCP）”：NfSCP<br>- “NfPCSCF（NfPCSCF）”：NfPCSCF<br>- “NfMBSMF（NfMBSMF）”：NfMBSMF<br>- “NfUDN（NfUDN）”：NfUDN<br>- “NfNWDAF（NfNWDAF）”：NfNWDAF<br>默认值：无<br>配置原则：无 |
| CACHETYPE | 缓存类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定缓存的类型。<br>数据来源：本端规划<br>取值范围：<br>- “E_ALL_CACHE（E_ALL_CACHE）”：缓存（从NRF查回的）和本地配置的NFProfile都会显示。<br>- “E_LOCAL_ONLY（E_LOCAL_ONLY）”：只显示本地配置的NFPROFILE。<br>- “E_REMOTE_ONLY（E_REMOTE_ONLY）”：只显示缓存（从NRF查回的）的NFProfile。<br>默认值：无<br>配置原则：无 |
| SUPI | SUPI | 可选必选说明：该参数在"QUERYTYPE"配置为"SUPI"时为条件必选参数。<br>参数含义：该参数用于指定SUPI。当QUERYTYPE参数设置为SUPI模式时有效。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是5~15。<br>默认值：无<br>配置原则：无 |
| GPSI | GPSI | 可选必选说明：该参数在"QUERYTYPE"配置为"GPSI"时为条件必选参数。<br>参数含义：该参数用于指定GPSI。当QUERYTYPE参数设置为GPSI模式时有效。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是5~15。<br>默认值：无<br>配置原则：无 |
| PODID | POD地址 | 可选必选说明：可选参数<br>参数含义：该参数用于指定POD的地址。如需显示指定POD的缓存，输入此参数即可。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~1024。作为输入参数时，来源于命令DSP POD的输出报文中的参数“Pod名称”。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NFCACHE]] · NF缓存信息（NFCACHE）

## 使用实例

查询当前NF存储的对端NF信息。

```
%%DSP NFCACHE: QUERYTYPE=NFType, NFTYPE=NfAMF, CACHETYPE=E_ALL_CACHE;%%
RETCODE = 0  操作成功

结果如下
--------
          NF实例标识  =  amf_instance_0
              NF类型  =  NfAMF
              NF状态  =  Registered
              优先级  =  0
                容量  =  100
                负载  =  0
                域名  =  NULL
            IPV4地址  =  192.168.0.1
            IPV6地址  =  NULL
            SUPI个数  =  0
            GPSI个数  =  0
             TAI个数  =  3
         TAI号段个数  =  0
             DNN个数  =  0
            PLMN列表  =  123_03
最近一次服务发现时间  =  NULL
        服务发现次数  =  0
             POD地址  =  gtp-pod-0
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-NFCACHE.md`
