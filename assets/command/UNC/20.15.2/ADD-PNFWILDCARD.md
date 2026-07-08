---
id: UNC@20.15.2@MMLCommand@ADD PNFWILDCARD
type: MMLCommand
name: ADD PNFWILDCARD（增加对端NF的通配策略）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: PNFWILDCARD
command_category: 配置类
applicable_nf:
- AMF
- SMF
- NRF
- NSSF
- SMSF
- NCG
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 服务化接口管理
- 注册与服务发现
- 本地NRF功能管理
- 对端NF通配策略管理
status: active
---

# ADD PNFWILDCARD（增加对端NF的通配策略）

## 功能

**适用NF：AMF、SMF、NRF、NSSF、SMSF、NCG**

该命令用于增加对端NF的通配策略。用于指示当本地配置中没有配置或缓存中不包含对端NF支持的特定属性信息时，用户携带该属性查询，此对端NF是否允许被服务发现。

## 注意事项

- 该命令执行后立即生效。

- 该命令对于缓存和本地配置分别生效。参数SUPICFGSWITCH，GPSICFGSWITCH，TAICFGSWITCH等针对本地配置生效，SUPICACHESWITCH，GPSICACHESWITCH，TAISWITCH等针对缓存生效。
- UPF、PCSCF等非标准化查询不受该命令控制。
- 本命令中涉及漫游场景通配的开关配置，仅在发现条件中携带非ADD NGHPLMN配置的目标PLMN时生效。

- 最多可输入26条记录。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| NFTYPE | SUPICFGSWITCH | SUPICACHESWITCH | ROAMSUPICFGSW | ROAMSUPICACHESW | GPSICFGSWITCH | GPSICACHESWITCH | ROAMGPSICFGSW | ROAMGPSICACHESW | TAICFGSWITCH | TAISWITCH | ROAMTAICFGSW | ROAMTAICACHESW | PLMNCFGSWITCH | PLMNSWITCH | ROAMPLMNCFGSW | ROAMPLMNCACHESW | DNNCFGSWITCH | DNNSWITCH | ROAMDNNCFGSW | ROAMDNNCACHESW | WDNNCFGSW | WDNNCACHESW | ROAMWDNNCFGSW | ROAMWDNNCACHESW | NSCFGSWITCH | NSSWITCH | ROAMNSCFGSW | ROAMNSCACHESW | ROUTEINDCFGSW | ROUTEINDSWITCH | ROAMRTIDCFGSW | ROAMRTIDCACHESW | CLIENTTYPCFGSW | CLIENTTYPSWITCH | GROUPIDCFGSW | GROUPIDSWITCH | ROAMGPIDCFGSW | ROAMGPIDCACHESW | SRVSPCFGSW | ROAMSRVSPCFGSW |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NfAMF | OFF | ON | OFF | ON | OFF | ON | OFF | ON | OFF | ON | OFF | ON | OFF | ON | OFF | ON | OFF | ON | OFF | ON | OFF | OFF | OFF | OFF | OFF | ON | OFF | ON | OFF | ON | OFF | ON | OFF | ON | OFF | OFF | OFF | OFF | ON | ON |
| NfSMF | OFF | ON | OFF | ON | OFF | ON | OFF | ON | OFF | ON | OFF | ON | OFF | ON | OFF | ON | OFF | ON | OFF | ON | OFF | OFF | OFF | OFF | OFF | ON | OFF | OFF | OFF | ON | OFF | ON | OFF | ON | OFF | OFF | OFF | OFF | ON | ON |
| NfUDM | OFF | ON | OFF | ON | OFF | ON | OFF | ON | OFF | ON | OFF | ON | OFF | ON | OFF | ON | OFF | ON | OFF | ON | OFF | OFF | OFF | OFF | OFF | ON | OFF | ON | OFF | ON | OFF | ON | OFF | ON | OFF | OFF | OFF | OFF | ON | ON |
| NfAUSF | OFF | ON | OFF | ON | OFF | ON | OFF | ON | OFF | ON | OFF | ON | OFF | ON | OFF | ON | OFF | ON | OFF | ON | OFF | OFF | OFF | OFF | OFF | ON | OFF | ON | OFF | ON | OFF | ON | OFF | ON | OFF | OFF | OFF | OFF | ON | ON |
| NfPCF | OFF | ON | OFF | ON | OFF | ON | OFF | ON | OFF | ON | OFF | ON | OFF | ON | OFF | ON | OFF | ON | OFF | ON | OFF | OFF | OFF | OFF | OFF | ON | OFF | ON | OFF | ON | OFF | ON | OFF | ON | OFF | OFF | OFF | OFF | ON | ON |
| NfCUSTOM_OCS | OFF | ON | OFF | ON | OFF | ON | OFF | ON | OFF | ON | OFF | ON | OFF | ON | OFF | ON | OFF | ON | OFF | ON | OFF | OFF | OFF | OFF | OFF | ON | OFF | ON | OFF | ON | OFF | ON | OFF | ON | OFF | OFF | OFF | OFF | ON | ON |
| NfCHF | OFF | ON | OFF | ON | OFF | ON | OFF | ON | OFF | ON | OFF | ON | OFF | ON | OFF | ON | OFF | ON | OFF | ON | OFF | OFF | OFF | OFF | OFF | ON | OFF | ON | OFF | ON | OFF | ON | OFF | ON | OFF | OFF | OFF | OFF | ON | ON |
| NfSMSF | OFF | OFF | OFF | ON | OFF | OFF | OFF | ON | OFF | ON | OFF | ON | OFF | ON | OFF | ON | OFF | ON | OFF | ON | OFF | OFF | OFF | OFF | OFF | ON | OFF | ON | OFF | ON | OFF | ON | OFF | ON | OFF | OFF | OFF | OFF | ON | ON |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFTYPE | NF类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定对端NF类型。<br>数据来源：本端规划<br>取值范围：<br>- “NfInvalid（NfInvalid）”：NfInvalid<br>- “NfNRF（NfNRF）”：NfNRF<br>- “NfUDM（NfUDM）”：NfUDM<br>- “NfAMF（NfAMF）”：NfAMF<br>- “NfSMF（NfSMF）”：NfSMF<br>- “NfAUSF（NfAUSF）”：NfAUSF<br>- “NfNEF（NfNEF）”：NfNEF<br>- “NfPCF（NfPCF）”：NfPCF<br>- “NfSMSF（NfSMSF）”：NfSMSF<br>- “NfNSSF（NfNSSF）”：NfNSSF<br>- “NfUDR（NfUDR）”：NfUDR<br>- “NfLMF（NfLMF）”：NfLMF<br>- “NfGMLC（NfGMLC）”：NfGMLC<br>- “Nf5G_EIR（Nf5G_EIR）”：Nf5G_EIR<br>- “NfSEPP（NfSEPP）”：NfSEPP<br>- “NfUPF（NfUPF）”：NfUPF<br>- “NfN3IWF（NfN3IWF）”：NfN3IWF<br>- “NfAF（NfAF）”：NfAF<br>- “NfUDSF（NfUDSF）”：NfUDSF<br>- “NfBSF（NfBSF）”：NfBSF<br>- “NfCHF（NfCHF）”：NfCHF<br>- “NfCUSTOM_OCS（NfCUSTOM_OCS）”：NfCUSTOM_OCS<br>- “NfSCP（NfSCP）”：NfSCP<br>- “NfPCSCF（NfPCSCF）”：NfPCSCF<br>- “NfMBSMF（NfMBSMF）”：NfMBSMF<br>- “NfUDN（NfUDN）”：NfUDN<br>- “NfNWDAF（NfNWDAF）”：NfNWDAF<br>默认值：无<br>配置原则：无 |
| SUPICFGSWITCH | 非漫游SUPI配置通配开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定非漫游场景本地配置查询中对端NF的SUPI通配开关。当本地配置中此NF没有配置SUPI时，用户携带SUPI来服务发现，取值为ON时，此NF允许被服务发现；取值为OFF时，此NF不允许被服务发现。<br>数据来源：本端规划<br>取值范围：<br>- “OFF（OFF）”：功能关闭<br>- “ON（ON）”：功能开启<br>默认值：OFF<br>配置原则：无 |
| SUPICACHESWITCH | 非漫游SUPI缓存通配开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定非漫游场景缓存查询中对端NF的SUPI通配开关。当缓存中此NF没有SUPI时，用户携带SUPI来服务发现，取值为ON时，此NF允许被服务发现；取值为OFF时，此NF不允许被服务发现。对NRF返回的服务发现结果不生效。<br>数据来源：本端规划<br>取值范围：<br>- “OFF（OFF）”：功能关闭<br>- “ON（ON）”：功能开启<br>默认值：ON<br>配置原则：无 |
| ROAMSUPICFGSW | 漫游SUPI配置通配开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定漫游场景本地配置查询中对端NF的SUPI通配开关。当本地配置中此NF没有配置SUPI时，用户携带SUPI来服务发现，取值为ON时，此NF允许被服务发现；取值为OFF时，此NF不允许被服务发现。<br>数据来源：本端规划<br>取值范围：<br>- “OFF（OFF）”：功能关闭<br>- “ON（ON）”：功能开启<br>默认值：OFF<br>配置原则：无 |
| ROAMSUPICACHESW | 漫游SUPI缓存通配开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定漫游场景缓存查询中对端NF的SUPI通配开关。当缓存中此NF没有SUPI时，用户携带SUPI来服务发现，取值为ON时，此NF允许被服务发现；取值为OFF时，此NF不允许被服务发现。对NRF返回的服务发现结果不生效。<br>数据来源：本端规划<br>取值范围：<br>- “OFF（OFF）”：功能关闭<br>- “ON（ON）”：功能开启<br>默认值：ON<br>配置原则：无 |
| GPSICFGSWITCH | 非漫游GPSI配置通配开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定非漫游场景本地配置查询中对端NF的GPSI通配开关。当本地配置中此NF没有配置GPSI时，用户携带GPSI来服务发现，取值为ON时，此NF允许被服务发现；取值为OFF时，此NF不允许被服务发现。<br>数据来源：本端规划<br>取值范围：<br>- “OFF（OFF）”：功能关闭<br>- “ON（ON）”：功能开启<br>默认值：OFF<br>配置原则：无 |
| GPSICACHESWITCH | 非漫游GPSI缓存通配开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定非漫游场景缓存查询中对端NF的GPSI通配开关。当缓存中此NF没有GPSI时，用户携带GPSI来服务发现，取值为ON时，此NF允许被服务发现；取值为OFF时，此NF不允许被服务发现。对NRF返回的服务发现结果不生效。<br>数据来源：本端规划<br>取值范围：<br>- “OFF（OFF）”：功能关闭<br>- “ON（ON）”：功能开启<br>默认值：ON<br>配置原则：无 |
| ROAMGPSICFGSW | 漫游GPSI配置通配开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定漫游场景本地配置查询中对端NF的GPSI通配开关。当本地配置中此NF没有配置GPSI时，用户携带GPSI来服务发现，取值为ON时，此NF允许被服务发现；取值为OFF时，此NF不允许被服务发现。<br>数据来源：本端规划<br>取值范围：<br>- “OFF（OFF）”：功能关闭<br>- “ON（ON）”：功能开启<br>默认值：OFF<br>配置原则：无 |
| ROAMGPSICACHESW | 漫游GPSI缓存通配开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定漫游场景缓存查询中对端NF的GPSI通配开关。当缓存中此NF没有GPSI时，用户携带GPSI来服务发现，取值为ON时，此NF允许被服务发现；取值为OFF时，此NF不允许被服务发现。对NRF返回的服务发现结果不生效。<br>数据来源：本端规划<br>取值范围：<br>- “OFF（OFF）”：功能关闭<br>- “ON（ON）”：功能开启<br>默认值：ON<br>配置原则：无 |
| TAICFGSWITCH | 非漫游TAI配置通配开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定非漫游场景本地配置中对端NF的TAI通配开关。本地配置没有配置对端NF的TAI时，当用户携带TAI来服务发现，取值为ON时，此NF允许被服务发现；取值为OFF时，此NF不允许被服务发现。<br>数据来源：本端规划<br>取值范围：<br>- “OFF（OFF）”：功能关闭<br>- “ON（ON）”：功能开启<br>默认值：OFF<br>配置原则：无 |
| TAISWITCH | 非漫游TAI缓存通配开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定非漫游场景缓存查询中对端NF的TAI通配开关。缓存中此NF没有TAI时，当用户携带TAI来服务发现，取值为ON时，此NF允许被服务发现；取值为OFF时，此NF不允许被服务发现。对NRF返回的服务发现结果不生效。<br>数据来源：本端规划<br>取值范围：<br>- “OFF（OFF）”：功能关闭<br>- “ON（ON）”：功能开启<br>默认值：ON<br>配置原则：无 |
| ROAMTAICFGSW | 漫游TAI配置通配开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定漫游场景本地配置中对端NF的TAI通配开关。本地配置没有配置对端NF的TAI时，当用户携带TAI来服务发现，取值为ON时，此NF允许被服务发现；取值为OFF时，此NF不允许被服务发现。<br>数据来源：本端规划<br>取值范围：<br>- “OFF（OFF）”：功能关闭<br>- “ON（ON）”：功能开启<br>默认值：OFF<br>配置原则：无 |
| ROAMTAICACHESW | 漫游TAI缓存通配开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定漫游场景缓存查询中对端NF的TAI通配开关。缓存中此NF没有TAI时，当用户携带TAI来服务发现，取值为ON时，此NF允许被服务发现；取值为OFF时，此NF不允许被服务发现。对NRF返回的服务发现结果不生效。<br>数据来源：本端规划<br>取值范围：<br>- “OFF（OFF）”：功能关闭<br>- “ON（ON）”：功能开启<br>默认值：ON<br>配置原则：无 |
| PLMNCFGSWITCH | 非漫游PLMN配置通配开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定非漫游场景本地配置中对端NF的PLMN通配开关。本地配置没有配置对端NF的PLMN时，当用户携带PLMN来服务发现，取值为ON时，此NF允许被服务发现；取值为OFF时，此NF不允许被服务发现。<br>数据来源：本端规划<br>取值范围：<br>- “OFF（OFF）”：功能关闭<br>- “ON（ON）”：功能开启<br>默认值：OFF<br>配置原则：无 |
| PLMNSWITCH | 非漫游PLMN缓存通配开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定非漫游场景缓存查询中对端NF的PLMN通配开关。缓存中此NF没有PLMN时，当用户携带PLMN来服务发现，取值为ON时，此NF允许被服务发现；取值为OFF时，此NF不允许被服务发现。对NRF返回的服务发现结果不生效。<br>数据来源：本端规划<br>取值范围：<br>- “OFF（OFF）”：功能关闭<br>- “ON（ON）”：功能开启<br>默认值：ON<br>配置原则：无 |
| ROAMPLMNCFGSW | 漫游PLMN配置通配开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定漫游场景本地配置中对端NF的PLMN通配开关。本地配置没有配置对端NF的PLMN时，当用户携带PLMN来服务发现，取值为ON时，此NF允许被服务发现；取值为OFF时，此NF不允许被服务发现。<br>数据来源：本端规划<br>取值范围：<br>- “OFF（OFF）”：功能关闭<br>- “ON（ON）”：功能开启<br>默认值：OFF<br>配置原则：无 |
| ROAMPLMNCACHESW | 漫游PLMN缓存通配开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定漫游场景缓存查询中对端NF的PLMN通配开关。缓存中此NF没有PLMN时，当用户携带PLMN来服务发现，取值为ON时，此NF允许被服务发现；取值为OFF时，此NF不允许被服务发现。对NRF返回的服务发现结果不生效。<br>数据来源：本端规划<br>取值范围：<br>- “OFF（OFF）”：功能关闭<br>- “ON（ON）”：功能开启<br>默认值：ON<br>配置原则：无 |
| DNNCFGSWITCH | 非漫游DNN配置通配开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定非漫游场景本地配置中对端NF的DNN通配开关。本地配置没有配置对端NF的DNN时，当用户携带DNN来服务发现，取值为ON时，此NF允许被服务发现；取值为OFF时，此NF不允许被服务发现。<br>数据来源：本端规划<br>取值范围：<br>- “OFF（OFF）”：功能关闭<br>- “ON（ON）”：功能开启<br>默认值：OFF<br>配置原则：无 |
| DNNSWITCH | 非漫游DNN缓存通配开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定非漫游场景缓存查询中对端NF的DNN通配开关。缓存中此NF没有DNN时，当用户携带DNN来服务发现，取值为ON时，此NF允许被服务发现；取值为OFF时，此NF不允许被服务发现。对NRF返回的服务发现结果不生效。<br>数据来源：本端规划<br>取值范围：<br>- “OFF（OFF）”：功能关闭<br>- “ON（ON）”：功能开启<br>默认值：ON<br>配置原则：<br>当本端NF为SMF且对端NF为语音PCF时，缓存查询中DNN是否通配由SMF软参DWORD519 BIT6控制。 |
| ROAMDNNCFGSW | 漫游DNN配置通配开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定漫游场景本地配置中对端NF的DNN通配开关。本地配置没有配置对端NF的DNN时，当用户携带DNN来服务发现，取值为ON时，此NF允许被服务发现；取值为OFF时，此NF不允许被服务发现。<br>数据来源：本端规划<br>取值范围：<br>- “OFF（OFF）”：功能关闭<br>- “ON（ON）”：功能开启<br>默认值：OFF<br>配置原则：<br>当AMF发现语音漫游网关时，配置查询中DNN是否通配由公共软参DWORD219 BIT8控制。 |
| ROAMDNNCACHESW | 漫游DNN缓存通配开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定漫游场景缓存查询中对端NF的DNN通配开关。缓存中此NF没有DNN时，当用户携带DNN来服务发现，取值为ON时，此NF允许被服务发现；取值为OFF时，此NF不允许被服务发现。对NRF返回的服务发现结果不生效。<br>数据来源：本端规划<br>取值范围：<br>- “OFF（OFF）”：功能关闭<br>- “ON（ON）”：功能开启<br>默认值：ON<br>配置原则：<br>当AMF发现语音漫游网关时，缓存查询中DNN是否通配由公共软参DWORD219 BIT8控制。 |
| WDNNCFGSW | 非漫游WildcardDnn配置通配开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定非漫游场景本地配置中对端NF的WildcardDnn通配开关。本地配置了对端NF的WildcarDnn（即"*"）时，当用户携带DNN来服务发现，取值为ON时，此NF允许被服务发现；取值为OFF且未配置请求的DNN时，此NF不允许被服务发现。<br>数据来源：本端规划<br>取值范围：<br>- “OFF（OFF）”：功能关闭<br>- “ON（ON）”：功能开启<br>默认值：OFF<br>配置原则：<br>仅在对端NF为SMF时，本参数可以取值为ON。 |
| WDNNCACHESW | 非漫游WildcardDnn缓存通配开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定非漫游场景缓存查询中对端NF的WildcarDnn通配开关。缓存中此NF有WildcardDnn（即"*"）时，当用户携带DNN来服务发现，取值为ON时，此NF允许被服务发现；取值为OFF且此NF没有用户请求的DNN时，此NF不允许被服务发现。对NRF返回的服务发现结果不生效。<br>数据来源：本端规划<br>取值范围：<br>- “OFF（OFF）”：功能关闭<br>- “ON（ON）”：功能开启<br>默认值：OFF<br>配置原则：<br>仅在对端NF为SMF时，本参数可以取值为ON。 |
| ROAMWDNNCFGSW | 漫游WildcardDnn配置通配开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定漫游场景本地配置中对端NF的WildcardDnn通配开关。本地配置了对端NF的WildcardDnn（即"*"）时，当用户携带DNN来服务发现，取值为ON时，此NF允许被服务发现；取值为OFF且未配置请求的DNN时，此NF不允许被服务发现。<br>数据来源：本端规划<br>取值范围：<br>- “OFF（OFF）”：功能关闭<br>- “ON（ON）”：功能开启<br>默认值：OFF<br>配置原则：<br>仅在对端NF为SMF时，本参数可以取值为ON。<br>当AMF发现语音漫游网关时，配置查询中WildcardDnn是否通配由公共软参DWORD219 BIT8控制。 |
| ROAMWDNNCACHESW | 漫游WildcardDnn缓存通配开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定漫游场景缓存查询中对端NF的WildcarDnn通配开关。缓存中此NF有WildcardDnn（即"*"）时，当用户携带DNN来服务发现，取值为ON时，此NF允许被服务发现；取值为OFF且此NF没有用户请求的DNN时，此NF不允许被服务发现。对NRF返回的服务发现结果不生效。<br>数据来源：本端规划<br>取值范围：<br>- “OFF（OFF）”：功能关闭<br>- “ON（ON）”：功能开启<br>默认值：OFF<br>配置原则：<br>仅在对端NF为SMF时，本参数可以取值为ON。<br>当AMF发现语音漫游网关时，缓存查询中WildcardDnn是否通配由公共软参DWORD219 BIT8控制。 |
| NSCFGSWITCH | 非漫游NS配置通配开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定非漫游场景本地配置中对端NF的NS通配开关。本地配置没有配置对端NF的NS时，当用户携带NS来服务发现，取值为ON时，此NF允许被服务发现；取值为OFF时，此NF不允许被服务发现。<br>数据来源：本端规划<br>取值范围：<br>- “OFF（OFF）”：功能关闭<br>- “ON（ON）”：功能开启<br>默认值：OFF<br>配置原则：无 |
| NSSWITCH | 非漫游NS缓存通配开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定非漫游场景缓存查询中对端NF的NS通配开关。缓存中此NF没有NS时，当用户携带NS来服务发现，取值为ON时，此NF允许被服务发现；取值为OFF时，此NF不允许被服务发现。对NRF返回的服务发现结果不生效。<br>数据来源：本端规划<br>取值范围：<br>- “OFF（OFF）”：功能关闭<br>- “ON（ON）”：功能开启<br>默认值：ON<br>配置原则：无 |
| ROAMNSCFGSW | 漫游NS配置通配开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定漫游场景本地配置中对端NF的NS通配开关。本地配置没有配置对端NF的NS时，当用户携带NS来服务发现，取值为ON时，此NF允许被服务发现；取值为OFF时，此NF不允许被服务发现。<br>数据来源：本端规划<br>取值范围：<br>- “OFF（OFF）”：功能关闭<br>- “ON（ON）”：功能开启<br>默认值：OFF<br>配置原则：无 |
| ROAMNSCACHESW | 漫游NS缓存通配开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定漫游场景缓存查询中对端NF的NS通配开关。缓存中此NF没有NS时，当用户携带NS来服务发现，取值为ON时，此NF允许被服务发现；取值为OFF时，此NF不允许被服务发现。对NRF返回的服务发现结果不生效。<br>数据来源：本端规划<br>取值范围：<br>- “OFF（OFF）”：功能关闭<br>- “ON（ON）”：功能开启<br>默认值：ON<br>配置原则：无 |
| ROUTEINDCFGSW | 非漫游Routing Indicator配置通配开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定非漫游场景本地配置中对端NF的Routing Indicators通配开关。本地配置没有配置对端NF的Routing Indicators时，当用户携带Routing Indicators来服务发现，取值为ON时，此NF允许被服务发现；取值为OFF时，此NF不允许被服务发现。<br>数据来源：本端规划<br>取值范围：<br>- “OFF（OFF）”：功能关闭<br>- “ON（ON）”：功能开启<br>默认值：OFF<br>配置原则：无 |
| ROUTEINDSWITCH | 非漫游Routing Indicator缓存通配开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定非漫游场景缓存查询中对端NF的Routing Indicators通配开关。缓存中此NF没有Routing Indicators时，当用户携带Routing Indicators来服务发现，取值为ON时，此NF允许被服务发现；取值为OFF时，此NF不允许被服务发现。对NRF返回的服务发现结果不生效。<br>数据来源：本端规划<br>取值范围：<br>- “OFF（OFF）”：功能关闭<br>- “ON（ON）”：功能开启<br>默认值：ON<br>配置原则：无 |
| ROAMRTIDCFGSW | 漫游Routing Indicator配置通配开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定漫游场景本地配置中对端NF的Routing Indicators通配开关。本地配置没有配置对端NF的Routing Indicators时，当用户携带Routing Indicators来服务发现，取值为ON时，此NF允许被服务发现；取值为OFF时，此NF不允许被服务发现。<br>数据来源：本端规划<br>取值范围：<br>- “OFF（OFF）”：功能关闭<br>- “ON（ON）”：功能开启<br>默认值：OFF<br>配置原则：无 |
| ROAMRTIDCACHESW | 漫游Routing Indicator缓存通配开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定漫游场景缓存查询中对端NF的Routing Indicators通配开关。缓存中此NF没有Routing Indicators时，当用户携带Routing Indicators来服务发现，取值为ON时，此NF允许被服务发现；取值为OFF时，此NF不允许被服务发现。对NRF返回的服务发现结果不生效。<br>数据来源：本端规划<br>取值范围：<br>- “OFF（OFF）”：功能关闭<br>- “ON（ON）”：功能开启<br>默认值：ON<br>配置原则：无 |
| CLIENTTYPCFGSW | CLIENTTYPE配置通配开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定本地配置中对端NF的ClientTypes通配开关。本地配置通过ADD PNFLMFINFO/ADD PNFGMLCINFO命令配置LMFINFO/GMLCINFO并且没有配置ClientTypes时，当用户携带ClientType来服务发现，取值为ON时，此NF允许被服务发现；取值为OFF时，此NF不允许被服务发现。<br>数据来源：本端规划<br>取值范围：<br>- “OFF（OFF）”：功能关闭<br>- “ON（ON）”：功能开启<br>默认值：OFF<br>配置原则：无 |
| CLIENTTYPSWITCH | CLIENTTYPE缓存通配开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定缓存查询中对端NF的ClientTypes通配开关。缓存中此NF包含LMFINFO或者GMLCINFO并且没有ClientTypes时，当用户携带ClientType来服务发现，取值为ON时，此NF允许被服务发现；取值为OFF时，此NF不允许被服务发现。对NRF返回的服务发现结果不生效。<br>数据来源：本端规划<br>取值范围：<br>- “OFF（OFF）”：功能关闭<br>- “ON（ON）”：功能开启<br>默认值：ON<br>配置原则：无 |
| GROUPIDCFGSW | 非漫游GROUPID配置通配开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定非漫游场景本地配置中对端NF的GROUPID通配开关。本地配置没有配置对端NF的GROUPID时，当用户携带GROUPID来服务发现，取值为ON时，此NF允许被服务发现；取值为OFF时，此NF不允许被服务发现。<br>数据来源：本端规划<br>取值范围：<br>- “OFF（OFF）”：功能关闭<br>- “ON（ON）”：功能开启<br>默认值：OFF<br>配置原则：无 |
| GROUPIDSWITCH | 非漫游GROUPID缓存通配开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定非漫游场景缓存查询中对端NF的GROUPID通配开关。缓存中此NF没有GROUPID时，当用户携带GROUPID来服务发现，取值为ON时，此NF允许被服务发现；取值为OFF时，此NF不允许被服务发现。对NRF返回的服务发现结果不生效。<br>数据来源：本端规划<br>取值范围：<br>- “OFF（OFF）”：功能关闭<br>- “ON（ON）”：功能开启<br>默认值：ON<br>配置原则：无 |
| ROAMGPIDCFGSW | 漫游GROUPID配置通配开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定漫游场景本地配置中对端NF的GROUPID通配开关。本地配置没有配置对端NF的GROUPID时，当用户携带GROUPID来服务发现，取值为ON时，此NF允许被服务发现；取值为OFF时，此NF不允许被服务发现。<br>数据来源：本端规划<br>取值范围：<br>- “OFF（OFF）”：功能关闭<br>- “ON（ON）”：功能开启<br>默认值：OFF<br>配置原则：无 |
| ROAMGPIDCACHESW | 漫游GROUPID缓存通配开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定漫游场景缓存查询中对端NF的GROUPID通配开关。缓存中此NF没有GROUPID时，当用户携带GROUPID来服务发现，取值为ON时，此NF允许被服务发现；取值为OFF时，此NF不允许被服务发现。对NRF返回的服务发现结果不生效。<br>数据来源：本端规划<br>取值范围：<br>- “OFF（OFF）”：功能关闭<br>- “ON（ON）”：功能开启<br>默认值：ON<br>配置原则：无 |
| SRVSPCFGSW | 非漫游服务区配置通配开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定本地配置查询中对端NF的服务区通配开关。当本地配置中此NF没有配置服务区时，用户携带服务区来服务发现，取值为ON时，此NF允许被服务发现；取值为OFF时，此NF不允许被服务发现。<br>数据来源：本端规划<br>取值范围：<br>- “OFF（OFF）”：功能关闭<br>- “ON（ON）”：功能开启<br>默认值：ON<br>配置原则：无 |
| ROAMSRVSPCFGSW | 漫游服务区配置通配开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定漫游场景本地配置查询中对端NF的服务区通配开关。当本地配置中此NF没有配置服务区时，用户携带服务区来服务发现，取值为ON时，此NF允许被服务发现；取值为OFF时，此NF不允许被服务发现。<br>数据来源：本端规划<br>取值范围：<br>- “OFF（OFF）”：功能关闭<br>- “ON（ON）”：功能开启<br>默认值：ON<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PNFWILDCARD]] · 对端NF的通配策略（PNFWILDCARD）

## 使用实例

运营商A需要添加对端NF的通配策略：NF类型为NfSMSF，SUPI配置通配开关为ON，SUPI缓存通配开关为ON，TAI缓存通配开关为ON，Routing Indicator缓存通配开关为ON。

```
ADD PNFWILDCARD: NFTYPE=NfSMSF, SUPICFGSWITCH=ON, SUPICACHESWITCH=ON, TAISWITCH=ON, ROUTEINDSWITCH=ON;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加对端NF的通配策略（ADD-PNFWILDCARD）_35374733.md`
