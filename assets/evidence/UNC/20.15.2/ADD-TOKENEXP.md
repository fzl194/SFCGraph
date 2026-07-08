# 增加Token有效期（ADD TOKENEXP）

- [命令功能](#ZH-CN_MMLREF_0209654165__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0209654165__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0209654165__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0209654165__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0209654165)

**适用NF：NRF**

该命令用于增加NF的Token有效期。当运营商希望新增对应NF类型/NF实例的Token有效期时长时可以使用此命令。

安全层面考虑，NF请求提供某种服务时需要获取授权，以预防和降低权限提升风险。5GC网络的NF间的服务化接口采用Oauth2.0动态Token授权以保证安全，Token可以理解为NF请求访问某服务使用的短期令牌，当且仅当手持令牌时，才能获取所需服务。

## [注意事项](#ZH-CN_MMLREF_0209654165)

- 该命令执行后立即生效。

- 最多可输入1088条记录。
- 当"SCFGTYPE"配置为"BYNFTYPE"时最多可以输入64条记录。
- 当"SCFGTYPE"配置为"BYFQDN"时最多可以输入1024条记录。
- 系统存在整系统默认的Token有效期，默认时长为60分钟，如果不配置此命令，所有的NF使用整系统默认的Token有效期。
- 整系统的Token有效期时长不能通过ADD TOKENEXP命令增加，只能通过MOD TOKENEXP命令修改。
- 根据NF类型/NF实例所配置的Token有效期优先级高于整系统的Token有效期。
- 该命令执行后，已经申请了Token的NF不受影响，新增加的Token有效期在后续申请Token的对应NF上生效。
- 主备或双活组网的场景下，如果需要配置此命令，则两个NRF上均需执行此命令，且配置参数一致。

#### [操作用户权限](#ZH-CN_MMLREF_0209654165)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0209654165)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SCFGTYPE | 生效范围 | 可选必选说明：必选参数<br>参数含义：该参数表示Token有效期的生效范围。<br>数据来源：本端规划<br>取值范围：<br>- “BYNFTYPE（NF类型）”：基于NF类型配置Token有效期。<br>- “BYFQDN（FQDN）”：基于FQDN配置Token有效期。<br>默认值：无<br>配置原则：无 |
| NFTYPE | NF类型 | 可选必选说明：该参数在"SCFGTYPE"配置为"BYNFTYPE"时为条件必选参数。<br>参数含义：该参数表示Token有效期作用的NF类型。<br>数据来源：本端规划<br>取值范围：<br>- NRF（NRF）<br>- UDM（UDM）<br>- AMF（AMF）<br>- SMF（SMF）<br>- AUSF（AUSF）<br>- NEF（NEF）<br>- PCF（PCF）<br>- SMSF（SMSF）<br>- NSSF（NSSF）<br>- UDR（UDR）<br>- LMF（LMF）<br>- GMLC（GMLC）<br>- EIR_5G（EIR_5G）<br>- SEPP（SEPP）<br>- UPF（UPF）<br>- N3IWF（N3IWF）<br>- AF（AF）<br>- UDSF（UDSF）<br>- BSF（BSF）<br>- CHF（CHF）<br>- NWDAF（NWDAF）<br>- CUSTOM_OCS（CUSTOM_OCS）<br>- SCP（SCP）<br>默认值：无<br>配置原则：无 |
| FQDN | FQDN | 可选必选说明：该参数在"SCFGTYPE"配置为"BYFQDN"时为条件必选参数。<br>参数含义：该参数表示Token有效期作用的FQDN。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。该参数只能由字母（A-Z或者a-z）、数字（0-9）、连字符（-）和点（.）组成。FQDN不能以“.”开始，也不能以“.”结束。<br>默认值：无<br>配置原则：无 |
| EXPTIME | 有效期时长(分钟) | 可选必选说明：必选参数<br>参数含义：该参数表示配置的Token有效期时长，单位为分钟。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~65535。<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0209654165)

- 运营商希望对AMF设置单独的Token有效期，不使用系统默认Token有效期时长，配置此命令。配置完成后，AMF新发起的Token请求都会按照新的有效期生效。
  ```
  ADD TOKENEXP: SCFGTYPE=BYNFTYPE, NFTYPE=AMF, EXPTIME=20;
  ```
- 运营商希望对FQDN为mmec12.mmegi8001.mme.epc.mnc000.mcc123.3gppnetwork.org的NF设置单独的Token有效期，不使用系统默认Token有效期时长，配置此命令。配置完成后，对应NF新发起的Token请求都会按照新的有效期生效。
  ```
  ADD TOKENEXP: SCFGTYPE=BYFQDN, FQDN="mmec12.mmegi8001.mme.epc.mnc000.mcc123.3gppnetwork.org", EXPTIME=20;
  ```
