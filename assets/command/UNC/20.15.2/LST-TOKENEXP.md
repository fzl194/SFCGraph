---
id: UNC@20.15.2@MMLCommand@LST TOKENEXP
type: MMLCommand
name: LST TOKENEXP（查询Token有效期）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: TOKENEXP
command_category: 查询类
applicable_nf:
- NRF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- 授权管理
- Token管理
- Token有效期管理
status: active
---

# LST TOKENEXP（查询Token有效期）

## 功能

**适用NF：NRF**

该命令用于查询NF的Token有效期时长。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CFGTYPE | 生效范围 | 可选必选说明：可选参数<br>参数含义：该参数表示Token有效期的生效范围。<br>数据来源：本端规划<br>取值范围：<br>- “WHOLESYS（整系统）”：基于整系统配置Token有效期。<br>- “BYNFTYPE（NF类型）”：基于NF类型配置Token有效期。<br>- “BYFQDN（FQDN）”：基于FQDN配置Token有效期。<br>默认值：无<br>配置原则：无 |
| NFTYPE | NF类型 | 可选必选说明：该参数在"CFGTYPE"配置为"BYNFTYPE"时为条件可选参数。<br>参数含义：该参数表示Token有效期作用的NF类型。<br>数据来源：本端规划<br>取值范围：<br>- NRF（NRF）<br>- UDM（UDM）<br>- AMF（AMF）<br>- SMF（SMF）<br>- AUSF（AUSF）<br>- NEF（NEF）<br>- PCF（PCF）<br>- SMSF（SMSF）<br>- NSSF（NSSF）<br>- UDR（UDR）<br>- LMF（LMF）<br>- GMLC（GMLC）<br>- EIR_5G（EIR_5G）<br>- SEPP（SEPP）<br>- UPF（UPF）<br>- N3IWF（N3IWF）<br>- AF（AF）<br>- UDSF（UDSF）<br>- BSF（BSF）<br>- CHF（CHF）<br>- NWDAF（NWDAF）<br>- CUSTOM_OCS（CUSTOM_OCS）<br>- SCP（SCP）<br>默认值：无<br>配置原则：无 |
| FQDN | FQDN | 可选必选说明：该参数在"CFGTYPE"配置为"BYFQDN"时为条件可选参数。<br>参数含义：该参数表示Token有效期作用的FQDN。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。该参数只能由字母（A-Z或者a-z）、数字（0-9）、连字符（-）和点（.）组成。FQDN不能以“.”开始，也不能以“.”结束。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@TOKENEXP]] · Token有效期（TOKENEXP）

## 使用实例

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

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-TOKENEXP.md`
