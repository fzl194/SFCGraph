---
id: UNC@20.15.2@MMLCommand@DSP REGNFSUBINFO
type: MMLCommand
name: DSP REGNFSUBINFO（显示NF订阅信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: REGNFSUBINFO
command_category: 查询类
applicable_nf:
- NRF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- 对端NF管理
- NF信息管理
- NF订阅信息管理
status: active
---

# DSP REGNFSUBINFO（显示NF订阅信息）

## 功能

![](显示NF订阅信息（DSP REGNFSUBINFO）_09653819.assets/notice_3.0-zh-cn_2.png)

该命令可能返回的查询记录数较大，执行过程中会影响系统性能或查询超时，可通过增加查询参数减少返回结果的记录数。

**适用NF：NRF**

该命令用于查询NF在NRF上的订阅信息。

## 注意事项

- 在执行此命令，当“KEYTYPE”选择“SUBCOND”，“SUBCONDTYPE”选择任何取值条件时，如果出现查询结果显示不全且超时，或者提示“RETCODE=387操作失败”，或者响应时长超过10s且提示“RETCODE=20111无数据”的情况，则需要进一步选择细粒度的查询条件。
- 例如：执行DSP REGNFSUBINFO: KEYTYPE=SUBCOND, SUBCONDTYPE=NFTYPECOND，如果提示“RETCODE=387 操作失败”，则需要补充NFTYPE的选择，查询具体NF的订阅记录，如执行DSP REGNFSUBINFO: KEYTYPE=SUBCOND, SUBCONDTYPE=NFTYPECOND, NFTYPE=NRF;。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| KEYTYPE | 查询类型 | 可选必选说明：必选参数<br>参数含义：该字段表示订阅信息的查询类型。<br>数据来源：本端规划<br>取值范围：<br>- SUBID（基于订阅标识查询订阅信息）<br>- NTFURI（基于订阅消息通知的URI查询订阅信息）<br>- SUBCOND（基于订阅条件查询订阅信息）<br>- SRCIP（基于订阅请求方IP查询订阅信息）<br>- SRCFQDN（基于订阅请求方FQDN查询订阅信息）<br>- INNER（内部订阅记录）<br>默认值：无<br>配置原则：<br>INNER（内部订阅记录）该参数仅用于SCP和NRF联合部署场景。 |
| SUBID | 订阅标识 | 可选必选说明：该参数在"KEYTYPE"配置为"SUBID"时为条件必选参数。<br>参数含义：该字段表示本次订阅的订阅标识。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~48。<br>默认值：无<br>配置原则：无 |
| NTFURI | 通知URI | 可选必选说明：该参数在"KEYTYPE"配置为"NTFURI"时为条件必选参数。<br>参数含义：该字段表示订阅消息通知的URI。<br>数据来源：对端协商<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：无 |
| SUBCONDTYPE | 订阅条件类型 | 可选必选说明：该参数在"KEYTYPE"配置为"SUBCOND"时为条件必选参数。<br>参数含义：该参数表示订阅条件的类型。<br>数据来源：本端规划<br>取值范围：<br>- INSTANCEIDCOND（基于NF的实例标识查询订阅信息）<br>- NFTYPECOND（基于目标NF类型查询订阅信息）<br>- SRVNAMECOND（基于目标服务名称查询订阅信息）<br>- AMFCOND（基于AMF的集合标识和区域标识查询订阅信息）<br>- GUAMICOND（基于目标NF的MCC和MNC信息查询订阅信息）<br>- NSCOND（基于目标NF的切片信息查询订阅信息）<br>- NFGROUPCOND（基于NF实例组标识查询订阅信息）<br>- NFSETCOND（基于NF Set ID查询订阅信息）<br>默认值：无<br>配置原则：无 |
| NFINSTANCEID | NF实例标识 | 可选必选说明：该参数在"SUBCONDTYPE"配置为"INSTANCEIDCOND"时为条件可选参数。<br>参数含义：该参数表示目标NF实例的标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~40。该参数只能由字母（A-Z或者a-z）、数字（0-9）、中划线（-）组成。<br>默认值：无<br>配置原则：无 |
| NFTYPE | NF类型 | 可选必选说明：该参数在"SUBCONDTYPE"配置为"NFTYPECOND"、"NFGROUPCOND"时为条件可选参数。<br>参数含义：该参数表示订阅的目标NF类型。<br>该参数要和NFGROUPID同时配置或者同时不配置。<br>数据来源：全网规划<br>取值范围：<br>- NRF（NRF）<br>- UDM（UDM）<br>- AMF（AMF）<br>- SMF（SMF）<br>- AUSF（AUSF）<br>- NEF（NEF）<br>- PCF（PCF）<br>- SMSF（SMSF）<br>- NSSF（NSSF）<br>- UDR（UDR）<br>- LMF（LMF）<br>- GMLC（GMLC）<br>- EIR_5G（EIR_5G）<br>- SEPP（SEPP）<br>- UPF（UPF）<br>- N3IWF（N3IWF）<br>- AF（AF）<br>- UDSF（UDSF）<br>- BSF（BSF）<br>- CHF（CHF）<br>- NWDAF（NWDAF）<br>- CUSTOM_OCS（CUSTOM_OCS）<br>- DRA（DRA）<br>- SCP（SCP）<br>默认值：无<br>配置原则：无 |
| SERVICENAME | 服务名称 | 可选必选说明：该参数在"SUBCONDTYPE"配置为"SRVNAMECOND"时为条件可选参数。<br>参数含义：该参数表示订阅的目标NF服务名称。<br>该参数要和NFGROUPID同时配置或者同时不配置。<br>数据来源：全网规划<br>取值范围：<br>- nnrfNfm（nnrfNfm）<br>- nnrfDisc（nnrfDisc）<br>- nudmSdm（nudmSdm）<br>- nudmUecm（nudmUecm）<br>- nudmUeau（nudmUeau）<br>- nudmEe（nudmEe）<br>- nudmPp（nudmPp）<br>- namfComm（namfComm）<br>- namfEvts（namfEvts）<br>- namfMt（namfMt）<br>- namfLoc（namfLoc）<br>- nsmfPdusess（nsmfPdusess）<br>- nsmfEventExp（nsmfEventExp）<br>- nausfAuth（nausfAuth）<br>- nausfSorp（nausfSorp）<br>- nnefPfdmgmt（nnefPfdmgmt）<br>- npcfAmPlcCtrl（npcfAmPlcCtrl）<br>- npcfSmPlcCtrl（npcfSmPlcCtrl）<br>- npcfPlcauth（npcfPlcauth）<br>- npcfBdtPlcctrl（npcfBdtPlcctrl）<br>- npcfEventExp（npcfEventExp）<br>- npcfUePlcCtrl（npcfUePlcCtrl）<br>- nsmsfSms（nsmsfSms）<br>- nnssfNsselc（nnssfNsselc）<br>- nnssfNssaiavai（nnssfNssaiavai）<br>- nudrDr（nudrDr）<br>- nlmfLoc（nlmfLoc）<br>- n5gEirEic（n5gEirEic）<br>- nbsfMgmt（nbsfMgmt）<br>- nchfSpdlmtctrl（nchfSpdlmtctrl）<br>- nchfConvgcharg（nchfConvgcharg）<br>- nnwdafEventsub（nnwdafEventsub）<br>- nnwdafAnltinfo（nnwdafAnltinfo）<br>默认值：无<br>配置原则：无 |
| AMFSETID | AMF集合标识 | 可选必选说明：该参数在"SUBCONDTYPE"配置为"AMFCOND"时为条件可选参数。<br>参数含义：该参数表示订阅的目标NF的AMF集合标识。<br>该参数要和AMFREGID同时配置或者同时不配置。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是3。取值范围0~0x3ff。<br>默认值：无<br>配置原则：无 |
| AMFREGID | AMF区域标识 | 可选必选说明：该参数在"SUBCONDTYPE"配置为"AMFCOND"时为条件可选参数。<br>参数含义：该参数表示订阅的目标NF的AMF区域标识。<br>该参数要和AMFSETID同时配置或者同时不配置。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是2。取值范围0~0xff。<br>默认值：无<br>配置原则：无 |
| MCC | 移动国家代码 | 可选必选说明：该参数在"SUBCONDTYPE"配置为"GUAMICOND"时为条件可选参数。<br>参数含义：该参数表示目标NF的移动国家代码。<br>参数MNC、MCC和AMF ID需要同时配置或者同时不配置。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是3。3位十进制数。<br>默认值：无<br>配置原则：无 |
| MNC | 移动网号 | 可选必选说明：该参数在"SUBCONDTYPE"配置为"GUAMICOND"时为条件可选参数。<br>参数含义：该参数表示目标NF的移动网号。<br>参数MNC、MCC和AMF ID需要同时配置或者同时不配置。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是2~3。2位或者3位十进制数。<br>默认值：无<br>配置原则：无 |
| AMFID | AMF标识 | 可选必选说明：该参数在"SUBCONDTYPE"配置为"GUAMICOND"时为条件可选参数。<br>参数含义：该参数表示目标NF的AMF标识。<br>参数MNC、MCC和AMF ID需要同时配置或者同时不配置。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~6。<br>默认值：无<br>配置原则：无 |
| SST | 切片业务类型 | 可选必选说明：该参数在"SUBCONDTYPE"配置为"NSCOND"时为条件可选参数。<br>参数含义：该参数表示订阅的目标NF切片业务类型。<br>该参数要和NSCOND同时配置或者同时不配置。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~255。<br>默认值：无<br>配置原则：无 |
| SD | 切片细分标识 | 可选必选说明：该参数在"SUBCONDTYPE"配置为"NSCOND"时为条件可选参数。<br>参数含义：该参数表示订阅的目标NF切片细分标识。<br>该参数要和NSCOND同时配置或者同时不配置。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是6。该参数只能由字母（A-F或者a-f）、数字（0-9）组成。<br>默认值：无<br>配置原则：无 |
| NFGROUPID | NF实例组标识 | 可选必选说明：该参数在"SUBCONDTYPE"配置为"NFGROUPCOND"时为条件可选参数。<br>参数含义：该参数表示目标NF实例组标识。<br>该参数要和NFTYPE同时配置或者同时不配置。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~128。<br>默认值：无<br>配置原则：无 |
| IPTYPE | IP类型 | 可选必选说明：该参数在"KEYTYPE"配置为"SRCIP"时为条件必选参数。<br>参数含义：该参数用于表示订阅方的IP类型。<br>数据来源：本端规划<br>取值范围：<br>- IPV4（IPv4）<br>- IPV6（IPv6）<br>默认值：无<br>配置原则：无 |
| IPV4 | IPv4地址 | 可选必选说明：该参数在"IPTYPE"配置为"IPV4"时为条件必选参数。<br>参数含义：该参数用于表示订阅方的IPv4地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| IPV6 | IPv6地址 | 可选必选说明：该参数在"IPTYPE"配置为"IPV6"时为条件必选参数。<br>参数含义：该参数用于表示订阅方的IPv6地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |
| VALIDATTR | 订阅记录有效值属性 | 可选必选说明：该参数在"KEYTYPE"配置为"SUBCOND"时为条件可选参数。<br>参数含义：该参数用于表示是否查询有效记录，有效记录详见SET NRFSUBPARA命令配置说明，默认查询有效记录。<br>数据来源：本端规划<br>取值范围：<br>- Valid（有效记录）<br>- Invalid（无效记录）<br>- All（所有记录）<br>默认值：Valid<br>配置原则：无 |
| NFSETID | NF Set ID | 可选必选说明：该参数在"SUBCONDTYPE"配置为"NFSETCOND"时为条件可选参数。<br>参数含义：该参数用于表示NF Set ID。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。该参数只能由字母（A-Z或者a-z）、数字（0-9）、连字符（-）、下划线（_）和点（.）组成，大小写不敏感，不能以“.”开始，也不能以“.”结束。<br>默认值：无<br>配置原则：无 |
| FQDN | 域名 | 可选必选说明：该参数在"KEYTYPE"配置为"SRCFQDN"时为条件必选参数。<br>参数含义：该参数用于表示订阅请求方的域名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：无 |
| SUBSOURCETYPE | 订阅来源分类 | 可选必选说明：该参数在"KEYTYPE"配置为"SUBID"、"NTFURI"、"SRCIP"、"SUBCOND"、"SRCFQDN"时为条件可选参数。<br>参数含义：该参数表示被订阅的订阅来源分类。若不输入，则表示查询所有类型的记录。<br>数据来源：本端规划<br>取值范围：<br>- EXTERNAL（外部订阅记录）<br>- INNER（内部订阅记录）<br>- ALL（全部订阅记录）<br>默认值：无<br>配置原则：<br>INNER（内部订阅记录）该参数仅用于SCP和NRF联合部署场景。 |

## 操作的配置对象

- [订阅信息（REGNFSUBINFO）](configobject/UNC/20.15.2/REGNFSUBINFO.md)

## 使用实例

- 当运营商想要查询所有的NF在NRF上的订阅信息时，按照如下命令配置。
  ```
  DSP REGNFSUBINFO: KEYTYPE=SUBCOND, SUBCONDTYPE=AMFCOND;
  %%DSP REGNFSUBINFO: KEYTYPE=SUBCOND, SUBCONDTYPE=AMFCOND, VALIDATTR=Valid;%%
  RETCODE = 0  操作成功

  结果如下
  --------
  订阅标识                                  通知URI                                                  IP类型  IPv4地址     IPv6地址  订阅条件                                        订阅有效期            通知事件类型                      目标NF的PLMN   通知条件  请求的NF类型  请求NF的FQDN                               NF支持的NRF特性  请求NF的PLMN列表  UserAgent携带的NF类型  订阅生成的连接模式   订阅来源分类

  000100008a7c3e658d424dbda6cf32fc87a1924d  http://10.70.139.1:5898/nnrf-nfm/v1/nf-instances/ff02-2  IPV4    10.70.139.1  NULL      {"AmfCond":{"amfSetId":"0","amfRegionId":"0"}}  2019-09-19T08:30:37Z  NF_REGISTERED;NF_PROFILE_CHANGED  12303          null      AMF           tac-123.epc.mnc003.mcc123.3gppnetwork.org  0                460-00;           NRF                    NONPLMNDIRECT   EXTERNAL
  00020001469abb0e86df42c683f164f048290f23  http://10.70.139.1:5898/nnrf-nfm/v1/nf-instances/ff02-3  IPV4    10.70.139.1  NULL      {"AmfCond":{"amfSetId":"0","amfRegionId":"0"}}  2019-09-19T08:30:39Z  NF_REGISTERED;NF_PROFILE_CHANGED  12303          null      AMF           tac-123.epc.mnc003.mcc123.3gppnetwork.org  1                460-00;           NRF                    NONPLMNDIRECT   EXTERNAL
  (结果个数 = 2)

  ---    END
  ```
- 当运营商想要查询订阅标识为http://10.70.139.1:5898/nnrf-nfm/v1/nf-instances/ff02-2的特定订阅信息时，按照如下命令配置。
  ```
  DSP REGNFSUBINFO: KEYTYPE=NTFURI,NTFURI="http://10.70.139.1:5898/nnrf-nfm/v1/nf-instances/ff02-2";
  %%DSP REGNFSUBINFO: KEYTYPE=NTFURI,NTFURI="http://10.70.139.1:5898/nnrf-nfm/v1/nf-instances/ff02-2";%%
  RETCODE = 0  操作成功

  结果如下
  --------
               订阅标识  =  000100008a7c3e658d424dbda6cf32fc87a1924d
                通知URI  =  http://10.70.139.1:5898/nnrf-nfm/v1/nf-instances/ff02-2
                 IP类型  =  IPv4
               IPv4地址  =  10.70.139.1
               IPv6地址  =  NULL  
               订阅条件  =  {"AmfCond":{"amfSetId":"0","amfRegionId":"0"}}
             订阅有效期  =  2019-09-19T08:30:37Z
           通知事件类型  =  NF_REGISTERED;NF_PROFILE_CHANGED
           目标NF的PLMN  =  12303
               通知条件  =  null
           请求的NF类型  =  AMF
           请求NF的FQDN  =  tac-123.epc.mnc003.mcc123.3gppnetwork.org 
        NF支持的NRF特性  =  1
       请求NF的PLMN列表  =  460-00;
  UserAgent携带的NF类型  =  NRF
     订阅生成的连接模式  =  NONPLMNDIRECT
           订阅来源分类  =  EXTERNAL
  (结果个数 = 1)

  ---    END
  ```
- 当运营商想要查询域名为topon.pgw-s5.app-nf001-03a011.nm.nm.node.epc.mnc000.mcc123.3gppnetwork.org的特定订阅信息时，按照如下命令配置。
  ```
  DSP REGNFSUBINFO: KEYTYPE=SRCFQDN, FQDN="topon.pgw-s5.app-nf001-03a011.nm.nm.node.epc.mnc000.mcc123.3gppnetwork.org";
  %%DSP REGNFSUBINFO: KEYTYPE=SRCFQDN, FQDN="topon.pgw-s5.app-nf001-03a011.nm.nm.node.epc.mnc000.mcc123.3gppnetwork.org";%%
  RETCODE = 0  操作成功

  结果如下
  --------
               订阅标识  =  000100008a7c3e658d424dbda6cf32fc87a1924d
                通知URI  =  http://topon.pgw-s5.app-nf001-03a011.nm.nm.node.epc.mnc000.mcc123.3gppnetwork.org/nnrf-nfm/v1/nf-instances/ff02-2
                 IP类型  =  IPv4
               IPv4地址  =  10.70.139.1
               IPv6地址  =  NULL  
               订阅条件  =  {"AmfCond":{"amfSetId":"0","amfRegionId":"0"}}
             订阅有效期  =  2019-09-19T08:30:37Z
           通知事件类型  =  NF_REGISTERED;NF_PROFILE_CHANGED
           目标NF的PLMN  =  12303
               通知条件  =  null
           请求的NF类型  =  AMF
           请求NF的FQDN  =  tac-123.epc.mnc003.mcc123.3gppnetwork.org 
        NF支持的NRF特性  =  1
       请求NF的PLMN列表  =  460-00;
  UserAgent携带的NF类型  =  NRF
     订阅生成的连接模式  =  NONPLMNDIRECT
           订阅来源分类  =  EXTERNAL
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示NF订阅信息（DSP-REGNFSUBINFO）_09653819.md`
