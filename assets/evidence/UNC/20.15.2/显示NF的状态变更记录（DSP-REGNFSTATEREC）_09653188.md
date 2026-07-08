# 显示NF的状态变更记录（DSP REGNFSTATEREC）

- [命令功能](#ZH-CN_MMLREF_0209653188__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0209653188__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0209653188__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0209653188__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0209653188__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0209653188)

**适用NF：NRF**

该命令用于查询NF状态变更过程记录，主要有NF的注册、去注册、心跳丢失以及执行DEL REGNFINSTANCE命令去注册过程记录。

## [注意事项](#ZH-CN_MMLREF_0209653188)

如果执行该命令未查询到相关NF状态变更过程记录，请等待十分钟后重试。

#### [操作用户权限](#ZH-CN_MMLREF_0209653188)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0209653188)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFTYPE | NF类型 | 可选必选说明：可选参数<br>参数含义：该参数用于表示在NRF上配置的NF类型。<br>数据来源：全网规划<br>取值范围：<br>- NRF（NRF）<br>- UDM（UDM）<br>- AMF（AMF）<br>- SMF（SMF）<br>- AUSF（AUSF）<br>- NEF（NEF）<br>- PCF（PCF）<br>- SMSF（SMSF）<br>- NSSF（NSSF）<br>- UDR（UDR）<br>- LMF（LMF）<br>- GMLC（GMLC）<br>- EIR_5G（EIR_5G）<br>- SEPP（SEPP）<br>- UPF（UPF）<br>- N3IWF（N3IWF）<br>- AF（AF）<br>- UDSF（UDSF）<br>- BSF（BSF）<br>- CHF（CHF）<br>- NWDAF（NWDAF）<br>- CUSTOM_OCS（CUSTOM_OCS）<br>- DRA（DRA）<br>- SCP（SCP）<br>默认值：无<br>配置原则：无 |
| NFINSTANCEID | NF实例标识 | 可选必选说明：可选参数<br>参数含义：该参数表示在NRF上配置的NF实例标识。可以通过DSP REGNFINSTANCE命令查询NF实例标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~255。该参数只能由字母（A-Z或者a-z）、数字（0-9）、中划线（-）组成。<br>默认值：无<br>配置原则：无 |
| TIMERANGE | 时间范围 | 可选必选说明：可选参数<br>参数含义：该参数表示查询NF状态变更记录的时间范围。如果不输入该参数，则查询所有NF状态变更记录。<br>数据来源：本端规划<br>取值范围：<br>- HOUR（一小时之内）<br>- DAY（一天之内）<br>- WEEK（一周之内）<br>默认值：无<br>配置原则：<br>当前版本不支持此参数。 |
| EVENTTYPE | 事件类型 | 可选必选说明：可选参数<br>参数含义：该参数表示在时间范围内发生的NF的操作记录类型。<br>数据来源：本端规划<br>取值范围：<br>- REGISTER（注册）<br>- DEREGISTER（去注册）<br>- HEARTBEATLOSS（心跳丢失）<br>- MANUALDEREGISTER（人工去注册）<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0209653188)

查询NF的状态变更记录：

```
DSP REGNFSTATEREC:;
%%DSP REGNFSTATEREC:;%%
RETCODE = 0  操作成功

结果如下
--------
NF类型  NF实例标识  事件类型    状态变化描述       时间戳               

AMF     ff02-002    注册        nf register        2019-10-12 05:52:38  
AMF     ff02-002    人工去注册  nf manual suspend  2019-10-12 05:52:38  
SMF     ff01-002    心跳丢失    nf heartbeat loss  2019-10-12 05:52:59   
AUSF    ff04-1      注册        nf register        2019-10-12 06:38:36  
AUSF    ff04-1      人工去注册  nf manual suspend  2019-10-12 06:38:36  
AUSF    ff04-1      人工去注册  nf manual suspend  2019-10-12 06:38:38  
AUSF    ff04-1      去注册      nf deregister      2019-10-12 06:38:38   
SMF     ff01-7      人工去注册  nf manual suspend  2019-10-12 06:48:45  
SMF     ff01-7      去注册      nf deregister      2019-10-12 06:48:45  
SMF     ff01-9      注册        nf register        2019-10-12 06:48:38  
SMF     ff01-9      人工去注册  nf manual suspend  2019-10-12 06:48:38  
SMF     ff01-9      人工去注册  nf manual suspend  2019-10-12 06:48:47   
UPF     ff08-001    人工去注册  nf manual suspend  2019-10-12 07:10:06  
UPF     ff08-001    去注册      nf deregister      2019-10-12 07:10:06  
UPF     ff08-001    注册        nf register        2019-10-12 07:10:31  
UPF     ff08-001    人工去注册  nf manual suspend  2019-10-12 07:10:31  
UPF     ff08-001    人工去注册  nf manual suspend  2019-10-12 07:10:51  
UPF     ff08-001    心跳丢失    nf heartbeat loss  2019-10-12 07:10:51  
(结果个数 = 18)
```

## [输出结果说明](#ZH-CN_MMLREF_0209653188)

| 输出项名称 | 输出项解释 |
| --- | --- |
| NF类型 | 该参数用于表示在NRF上配置的NF类型。<br>取值说明：<br>- NRF（NRF）<br>- UDM（UDM）<br>- AMF（AMF）<br>- SMF（SMF）<br>- AUSF（AUSF）<br>- NEF（NEF）<br>- PCF（PCF）<br>- SMSF（SMSF）<br>- NSSF（NSSF）<br>- UDR（UDR）<br>- LMF（LMF）<br>- GMLC（GMLC）<br>- EIR_5G（EIR_5G）<br>- SEPP（SEPP）<br>- UPF（UPF）<br>- N3IWF（N3IWF）<br>- AF（AF）<br>- UDSF（UDSF）<br>- BSF（BSF）<br>- CHF（CHF）<br>- NWDAF（NWDAF）<br>- CUSTOM_OCS（CUSTOM_OCS）<br>- DRA（DRA）<br>- SCP（SCP） |
| NF实例标识 | 该参数表示在NRF上配置的NF实例标识。可以通过DSP REGNFINSTANCE命令查询NF实例标识。 |
| 事件类型 | 该参数表示在时间范围内发生的NF的操作记录类型。<br>取值说明：<br>- REGISTER（注册）<br>- DEREGISTER（去注册）<br>- HEARTBEATLOSS（心跳丢失）<br>- MANUALDEREGISTER（人工去注册） |
| 状态变化描述 | 该参数表示NF在时间范围内发生的状态变化描述。 |
| 时间戳 | 该参数表示记录NF状态变化的时间戳。 |
