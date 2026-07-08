# 修改Token有效期（MOD TOKENEXP）

- [命令功能](#ZH-CN_MMLREF_0209651804__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0209651804__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0209651804__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0209651804__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0209651804)

**适用NF：NRF**

该命令用于修改NF的Token有效期。

安全层面考虑，NF请求提供某种服务时需要获取授权，以预防和降低权限提升风险。5GC网络的NF间的服务化接口采用Oauth2.0动态Token授权以保证安全，Token可以理解为NF请求访问某服务使用的短期令牌，当且仅当手持令牌时，才能获取所需服务。

## [注意事项](#ZH-CN_MMLREF_0209651804)

- 该命令执行后立即生效。

- 该命令执行后，已经申请了Token的NF不受影响，新修改的Token有效期在后续申请Token的对应NF上生效。
- 主备或双活组网的场景下，如果需要配置此命令，则两个NRF上均需执行此命令，且配置参数一致。

#### [操作用户权限](#ZH-CN_MMLREF_0209651804)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0209651804)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CFGTYPE | 生效范围 | 可选必选说明：必选参数<br>参数含义：该参数表示Token有效期的生效范围。<br>数据来源：本端规划<br>取值范围：<br>- “WHOLESYS（整系统）”：基于整系统配置Token有效期。<br>- “BYNFTYPE（NF类型）”：基于NF类型配置Token有效期。<br>- “BYFQDN（FQDN）”：基于FQDN配置Token有效期。<br>默认值：无<br>配置原则：无 |
| NFTYPE | NF类型 | 可选必选说明：该参数在"CFGTYPE"配置为"BYNFTYPE"时为条件必选参数。<br>参数含义：该参数表示Token有效期作用的NF类型。<br>数据来源：本端规划<br>取值范围：<br>- NRF（NRF）<br>- UDM（UDM）<br>- AMF（AMF）<br>- SMF（SMF）<br>- AUSF（AUSF）<br>- NEF（NEF）<br>- PCF（PCF）<br>- SMSF（SMSF）<br>- NSSF（NSSF）<br>- UDR（UDR）<br>- LMF（LMF）<br>- GMLC（GMLC）<br>- EIR_5G（EIR_5G）<br>- SEPP（SEPP）<br>- UPF（UPF）<br>- N3IWF（N3IWF）<br>- AF（AF）<br>- UDSF（UDSF）<br>- BSF（BSF）<br>- CHF（CHF）<br>- NWDAF（NWDAF）<br>- CUSTOM_OCS（CUSTOM_OCS）<br>- SCP（SCP）<br>默认值：无<br>配置原则：无 |
| FQDN | FQDN | 可选必选说明：该参数在"CFGTYPE"配置为"BYFQDN"时为条件必选参数。<br>参数含义：该参数表示Token有效期作用的FQDN。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。该参数只能由字母（A-Z或者a-z）、数字（0-9）、连字符（-）和点（.）组成。FQDN不能以“.”开始，也不能以“.”结束。<br>默认值：无<br>配置原则：无 |
| EXPTIME | 有效期时长(分钟) | 可选必选说明：必选参数<br>参数含义：该参数表示配置的Token有效期时长，单位为分钟。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~65535。<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0209651804)

- 运营商已经对AMF设置了单独的Token有效期，当运营商希望修改AMF对应的Token有效期时长，配置此命令。配置完成后，AMF新发起的Token请求都会按照新的有效期生效。
  ```
  MOD TOKENEXP:CFGTYPE=BYNFTYPE, NFTYPE=AMF, EXPTIME=30;
  ```
- 运营商已经对FQDN为mmec12.mmegi8001.mme.epc.mnc000.mcc123.3gppnetwork.org的NF设置了单独的Token有效期，当运营商希望修改FQDN为mmec12.mmegi8001.mme.epc.mnc000.mcc123.3gppnetwork.org的NF对应的Token有效期时长,配置此命令。配置完成后，该NF新发起的Token请求都会按照新的有效期生效。
  ```
  MOD TOKENEXP:CFGTYPE=BYFQDN, FQDN="mmec12.mmegi8001.mme.epc.mnc000.mcc123.3gppnetwork.org", EXPTIME=30;
  ```
- 当运营商希望修改整系统默认的Token有效期时长，配置此命令。
  ```
  MOD TOKENEXP:CFGTYPE=WHOLESYS, EXPTIME=30;
  ```
