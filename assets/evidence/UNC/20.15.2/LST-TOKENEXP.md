# 查询Token有效期（LST TOKENEXP）

- [命令功能](#ZH-CN_MMLREF_0209652435__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0209652435__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0209652435__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0209652435__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0209652435__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0209652435)

**适用NF：NRF**

该命令用于查询NF的Token有效期时长。

## [注意事项](#ZH-CN_MMLREF_0209652435)

无

#### [操作用户权限](#ZH-CN_MMLREF_0209652435)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0209652435)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CFGTYPE | 生效范围 | 可选必选说明：可选参数<br>参数含义：该参数表示Token有效期的生效范围。<br>数据来源：本端规划<br>取值范围：<br>- “WHOLESYS（整系统）”：基于整系统配置Token有效期。<br>- “BYNFTYPE（NF类型）”：基于NF类型配置Token有效期。<br>- “BYFQDN（FQDN）”：基于FQDN配置Token有效期。<br>默认值：无<br>配置原则：无 |
| NFTYPE | NF类型 | 可选必选说明：该参数在"CFGTYPE"配置为"BYNFTYPE"时为条件可选参数。<br>参数含义：该参数表示Token有效期作用的NF类型。<br>数据来源：本端规划<br>取值范围：<br>- NRF（NRF）<br>- UDM（UDM）<br>- AMF（AMF）<br>- SMF（SMF）<br>- AUSF（AUSF）<br>- NEF（NEF）<br>- PCF（PCF）<br>- SMSF（SMSF）<br>- NSSF（NSSF）<br>- UDR（UDR）<br>- LMF（LMF）<br>- GMLC（GMLC）<br>- EIR_5G（EIR_5G）<br>- SEPP（SEPP）<br>- UPF（UPF）<br>- N3IWF（N3IWF）<br>- AF（AF）<br>- UDSF（UDSF）<br>- BSF（BSF）<br>- CHF（CHF）<br>- NWDAF（NWDAF）<br>- CUSTOM_OCS（CUSTOM_OCS）<br>- SCP（SCP）<br>默认值：无<br>配置原则：无 |
| FQDN | FQDN | 可选必选说明：该参数在"CFGTYPE"配置为"BYFQDN"时为条件可选参数。<br>参数含义：该参数表示Token有效期作用的FQDN。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。该参数只能由字母（A-Z或者a-z）、数字（0-9）、连字符（-）和点（.）组成。FQDN不能以“.”开始，也不能以“.”结束。<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0209652435)

- 查询整系统的Token有效期时长：
  ```
  LST TOKENEXP: CFGTYPE=WHOLESYS;
  %%LST TOKENEXP: CFGTYPE=WHOLESYS;%%
  RETCODE = 0  操作成功

  结果如下
  --------
            NF类型  =  NULL
              FQDN  =  NULL
  有效期时长(分钟)  =  60
  (结果个数 = 1)
  ```
- 查询FQDN为mmec12.mmegi8001.mme.epc.mnc000.mcc123.3gppnetwork.org的NF的Token的有效期时长：
  ```
  LST TOKENEXP: CFGTYPE=BYFQDN, FQDN="mmec12.mmegi8001.mme.epc.mnc000.mcc123.3gppnetwork.org";
  %%LST TOKENEXP: CFGTYPE=BYFQDN, FQDN="mmec12.mmegi8001.mme.epc.mnc000.mcc123.3gppnetwork.org";%%
  RETCODE = 0 操作成功

  结果如下
  ------------------------
            NF类型  =  NULL
              FQDN  =  mmec12.mmegi8001.mme.epc.mnc000.mcc123.3gppnetwork.org
  有效期时长（分钟）= 30
  (结果个数 = 1)
  ```

## [输出结果说明](#ZH-CN_MMLREF_0209652435)

| 输出项名称 | 输出项解释 |
| --- | --- |
| NF类型 | 该参数表示Token有效期作用的NF类型。 |
| FQDN | 该参数表示Token有效期作用的FQDN。 |
| 有效期时长(分钟) | 该参数表示配置的Token有效期时长，单位为分钟。 |
