# 显示NF实例（DSP REGNFINSTANCE）

- [命令功能](#ZH-CN_MMLREF_0209653688__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0209653688__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0209653688__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0209653688__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0209653688__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0209653688)

**适用NF：NRF**

该命令用于查询NRF上已注册的NF实例。

## [注意事项](#ZH-CN_MMLREF_0209653688)

无

#### [操作用户权限](#ZH-CN_MMLREF_0209653688)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0209653688)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFTYPE | NF类型 | 可选必选说明：可选参数<br>参数含义：该参数表示NF实例的类型。<br>数据来源：全网规划<br>取值范围：<br>- NRF（NRF）<br>- UDM（UDM）<br>- AMF（AMF）<br>- SMF（SMF）<br>- AUSF（AUSF）<br>- NEF（NEF）<br>- PCF（PCF）<br>- SMSF（SMSF）<br>- NSSF（NSSF）<br>- UDR（UDR）<br>- LMF（LMF）<br>- GMLC（GMLC）<br>- EIR_5G（EIR_5G）<br>- SEPP（SEPP）<br>- UPF（UPF）<br>- N3IWF（N3IWF）<br>- AF（AF）<br>- UDSF（UDSF）<br>- BSF（BSF）<br>- CHF（CHF）<br>- NWDAF（NWDAF）<br>- CUSTOM_OCS（CUSTOM_OCS）<br>- DRA（DRA）<br>- SCP（SCP）<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0209653688)

查询NRF上已注册的NF实例：

```
DSP REGNFINSTANCE:;
%%DSP REGNFINSTANCE:;%%
RETCODE = 0  操作成功

操作结果如下：
------------------------
      NF实例标识  =  123e4567-e89b-12d3-a456-426655440000
       IPV4地址  =  IP1:10.29.7.108
       IPV6地址  =  IP1:2001:db8:0:1:1:1:1:1
         NF状态  =  暂停状态
          FQDN  =  tac-123.epc.mnc003.mcc123.3gppnetwork.org
         NF类型  =  AMF
        NF组标识 =  NULL
      NF更新时间  =  2020-08-20 19:59:50
    NF客户端地址  =  10.29.7.102
  从本NRF接入标识 =  YES
(结果个数 = 1)

---    END
```

## [输出结果说明](#ZH-CN_MMLREF_0209653688)

| 输出项名称 | 输出项解释 |
| --- | --- |
| NF类型 | 该参数表示NF实例的类型。<br>取值说明：<br>- NRF（NRF）<br>- UDM（UDM）<br>- AMF（AMF）<br>- SMF（SMF）<br>- AUSF（AUSF）<br>- NEF（NEF）<br>- PCF（PCF）<br>- SMSF（SMSF）<br>- NSSF（NSSF）<br>- UDR（UDR）<br>- LMF（LMF）<br>- GMLC（GMLC）<br>- EIR_5G（EIR_5G）<br>- SEPP（SEPP）<br>- UPF（UPF）<br>- N3IWF（N3IWF）<br>- AF（AF）<br>- UDSF（UDSF）<br>- BSF（BSF）<br>- CHF（CHF）<br>- NWDAF（NWDAF）<br>- CUSTOM_OCS（CUSTOM_OCS）<br>- DRA（DRA）<br>- SCP（SCP） |
| NF实例标识 | 该参数表示NF实例标识。 |
| IPv4地址 | 该参数表示NF的IPv4地址信息。IP地址显示格式为："IP1:XXX"（其中XXX表示具体的IPv4地址），当存在多个IP地址时，各IP地址间用分号（;）隔开。 |
| IPv6地址 | 该参数表示NF的IPv6地址信息。IP地址显示格式为："IP1:XXX"（其中XXX表示具体的IPv6地址），当存在多个IP地址时，各IP地址间用分号（;）隔开。 |
| NF状态 | 该参数表示NF实例的状态，NF状态包括INVALID、REGISTERED、SUSPENDED、UNDISCOVERABLE。<br>取值说明：<br>- INVALID（无效状态）<br>- REGISTERED（注册状态）<br>- SUSPENDED（暂停状态）<br>- UNDISCOVERABLE（不可被服务发现状态） |
| FQDN | 该参数表示NF实例的FQDN。 |
| NF组标识 | 该参数表示号段配置的NF组标识。 |
| NF更新时间 | 该参数表示NF实例的最近一次更新时间，更新包含注册、全量更新、部分更新、心跳丢失（status字段变化）、心跳恢复（status字段变化）。 |
| NF客户端地址 | 该参数表示NF最近一次与NRF交互使用的客户端地址。 |
| 从本NRF接入标识 | 该参数表示NF最近一次与NRF交互是否从本NRF接入。（YES表示从本NRF接入，NO表示从容灾的另一个NRF接入，结果为空表示不确定是否从本地接入）。 |
