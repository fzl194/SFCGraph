# 测试NF和NRF上的网元信息是否一致（TST NFPROFILECHECK）

- [命令功能](#ZH-CN_MMLREF_0000001135803156__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001135803156__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001135803156__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001135803156__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0000001135803156)

**适用NF：AMF、SMF、NRF、NSSF、SMSF**

该命令用来手动触发NF本地配置的NFProfile信息和NRF上存储的该NF的NFProfile信息校验，如果两者不一致NF会自动触发一次注册，保证NRF上存储的NFProfile信息和本地配置的保持一致。

## [注意事项](#ZH-CN_MMLREF_0000001135803156)

- NF也可以通过SET NFNRFMGMTPARA中的TPROFILECHK参数实现周期性的自动校验。
- 如果同一类号段数存在多组参数不一致，只会输出其中一组的配置侧数据信息。
- 对于部分枚举类型信息将以数字显示，各数字对于关系如下：
- NfStatus:
- 0: "NFStatusINVALID"。
- 1: "NFStatusREGISTERED"。
- 2: "NFStatusSUSPENDED"。
- 3: "NFStatusUNDISCOVERABLE"。
- 4: "NFStatusMAX"。
- AccessType:
- 0: "AccessTypeINVALID"。
- 1: "AccessType3GPP_ACCESS"。
- 2: "AccessTypeNON_3GPP_ACCESS"。
- 3: "AccessTypeMAX"。
- NotificationType:
- 0: "NotificationTypeINVALID"。
- 1: "NotificationTypeN1_MESSAGES"。
- 2: "NotificationTypeN2_INFORMATION"。
- 3: "NotificationTypeLOCATION_NOTIFICATION"。
- 4: "NotificationTypeDATA_REMOVAL_NOTIFICATION"。
- 5: "NotificationTypeDATA_CHANGE_NOTIFICATION"。
- 6: "NotificationTypeMAX"。
- N1MessageClass:
- 0: "N1MessageClassINVALID"。
- 1: "N1MessageClass5GMM"。
- 2: "N1MessageClassSM"。
- 3: "N1MessageClassLPP"。
- 4: "N1MessageClassSMS"。
- 5: "N1MessageClassUPDP"。
- 6: "N1MessageClassMAX"。
- N2InformationClass。
- 0: "N2InformationClassINVALID"。
- 1: "N2InformationClassSM"。
- 2: "N2InformationClassNRPPa"。
- 3: "N2InformationClassPWS"。
- 4: "N2InformationClassPWSBCAL"。
- 5: "N2InformationClassPWSRF"。
- 6: "N2InformationClassRAN"。
- 7: "N2InformationClassMAX"。
- ServiceName:
- 1: "Nrf_NFManagement"。
- 2: "Nnrf_NFDiscovery"。
- 3: "Nudm_SubscriberDataManagement"。
- 4: "Nudm_UEContextManagement"。
- 5: "Nudm_UEAuthentication"。
- 6: "Nudm_EventExposure"。
- 7: "Nudm_ParameterProvision"。
- 8: "Namf_Communication"。
- 9: "Namf_EventExposure"。
- 10: "Namf_MT"。
- 11: "Namf_Location"。
- 12: "Nsmf_PDUSession"。
- 13: "Nsmf_EventExposure"。
- 14: "Nausf_UEAuthentication"。
- 15: "Nausf_SoRProtection"。
- 16: "Nausf_UPUProtection"。
- 17: "Nnef_PFDManagement"。
- 18: "Npcf_AMPolicyControl"。
- 19: "Npcf_SMPolicyControl"。
- 20: "Npcf_PolicyAuthorization"。
- 21: "Npcf_BDTPolicyControl"。
- 22: "Npcf_EventExposure"。
- 23: "Npcf_UEPolicyControl"。
- 24: "Nsmsf_SMService"。
- 25: "Nnssf_NSSelection"。
- 26: "Nnssf_NSSAIAvailability"。
- 27: "Nudr_DataRepository"。
- 28: "Nlmf_Location"。
- 29: "N5g-eir_EquipmentIdentityCheck"。
- 30: "Nbsf_Management"。
- 31: "Nchf_SpendingLimitControl"。
- 32: "Nchf_Converged_Charging"。
- 33: "Nnwdaf_EventsSubscription"。
- 34: "Nnwdaf_AnalyticsInfo"。
- 35: "Ncustom_ocs_SpendingLimitControl"。
- 36: "Ncustom_ocs_ConvergedCharging"。
- 37: "Ngmlc_Location"。
- 38: "Nnef_3gppAsSessionWithQos"。
- 39: "Nnef_3gppMonEvent"。
- NfType:
- 1: "Nrf"。
- 2: "Udm"。
- 3: "Amf"。
- 4: "Smf"。
- 5: "Ausf"。
- 6: "Pcf"。
- 7: "Udr"。
- 8: "Upf"。
- 9: "Bsf"。
- 10: "Chf"。
- 11:"Nef"。
- 12:"Nwdaf"。
- NfServiceStatus:
- 1: "NFServiceStatusREGISTERED"。
- 2: "NFServiceStatusSUSPENDED"。
- 3: "NFServiceStatusUNDISCOVERABLE"。

#### [操作用户权限](#ZH-CN_MMLREF_0000001135803156)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001135803156)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFINSTANCEID | 网元实例标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定NF实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度是36。<br>默认值：无<br>配置原则：<br>NFINSTANCEID值可通过LST NFUUID获得。 |
| DATACHKREGSW | 数据校验不一致重注册开关 | 可选必选说明：可选参数<br>参数含义：该参数用于控制数据校验不一致后NF是否发起重注册。<br>- 开关值为OFF时，数据校验不一致的NF不会向NRF发起重注册；<br>- 开关值为ON时，数据校验不一致的NF会向NRF发起重注册。<br>数据来源：本端规划<br>取值范围：<br>- “ON（ON）”：功能打开<br>- “OFF（OFF）”：功能关闭<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0000001135803156)

手动触发NFINSTANCEID为“639deb4b-b625-4fe8-bb64-d79c4d5a4aaa”的NF本地配置的NFProfile数据和NRF上存储的此NF的NFProfile数据一致性校验。

```
TST NFPROFILECHECK: NFINSTANCEID="639deb4b-b625-4fe8-bb64-d79c4d5a4aaa", DATACHKREGSW=ON;
```
