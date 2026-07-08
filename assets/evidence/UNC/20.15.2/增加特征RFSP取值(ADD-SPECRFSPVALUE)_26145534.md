# 增加特征RFSP取值(ADD SPECRFSPVALUE)

- [命令功能](#ZH-CN_MMLREF_0000001126145534__1.3.1.1)
- [注意事项](#ZH-CN_MMLREF_0000001126145534__1.3.2.1)
- [本地用户权限](#ZH-CN_MMLREF_0000001126145534__1.3.3.1)
- [网管用户权限](#ZH-CN_MMLREF_0000001126145534__1.3.4.1)
- [参数说明](#ZH-CN_MMLREF_0000001126145534__1.3.5.1)
- [使用实例](#ZH-CN_MMLREF_0000001126145534__1.3.6.1)

#### [命令功能](#ZH-CN_MMLREF_0000001126145534)

**适用网元：SGSN、MME**

该命令用于增加一组RFSP(RAT/Frequency Selection Priority)。运营商为特定用户在HSS里签约特征RFSP(RAT/Frequency Selection Priority)作为标识， UNC 针对这些用户提供特殊处理，如：

通过 [**ADD S1ACCAREALST**](../../../区域漫游限制管理/S1模式区域漫游限制参数/增加S1模式接入控制配置（ADD S1ACCAREALST）_72345153.md) 命令禁止签约了特征RFSP的用户接入指定区域。

通过 [**ADD VOICEDEPLOY**](../../../../业务安全管理/语音业务管理/增加语音部署配置(ADD VOICEDEPLOY)_72345361.md) 命令禁止签约了特征RFSP的用户使用IMS VoPS业务。

#### [注意事项](#ZH-CN_MMLREF_0000001126145534)

- 此命令执行后立即生效。
- 此命令最大记录数为50。
- 同一索引下不能配置多个类型。
- 同一索引下的特征RFSP取值不能重叠。
- 当类型为“ENODEB_IND(eNodeB指示)”时，同一个索引下只能配置一条记录，且起始RFSP必须大于等于2。

#### [本地用户权限](#ZH-CN_MMLREF_0000001126145534)

manage-ug；system-ug

#### [网管用户权限](#ZH-CN_MMLREF_0000001126145534)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_MMLREF_0000001126145534)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RFSPIDX | 特征RFSP索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定特征RFSP索引，该索引标识了一组或多组RFSP取值。<br>数据来源：本端规划<br>取值范围：0~49<br>默认值：无 |
| TYPE | 特征RFSP索引类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定该特征RFSP索引的类型。<br>数据来源：整网规划<br>取值范围：<br>- “IMS_VOPS(IMS VoPS限制)”：表示该特征RFSP范围用于IMS VoPS限制。<br>- “ENODEB_IND(eNodeB指示)”：表示该特征RFSP范围用于将签约RFSP ID映射成SPID。<br>- “ACC_REJECT(区域接入控制)”：表示该特征RFSP范围用于区域接入控制。<br>默认值：无<br>配置原则：<br>- 当希望通过[**ADD VOICEDEPLOY**](../../../../业务安全管理/语音业务管理/增加语音部署配置(ADD VOICEDEPLOY)_72345361.md)命令禁止签约了特征RFSP的用户使用IMS VoPS业务则配置成“IMS_VOPS(IMS VoPS限制)”。<br>- 当[**ADD S1ACCAREALST**](../../../区域漫游限制管理/S1模式区域漫游限制参数/增加S1模式接入控制配置（ADD S1ACCAREALST）_72345153.md)命令“ENBIND(eNodeB指示方式)”参数配置为“RFSP_ID(RFSP ID)”，需要将用户签约RFSP ID映射成SPID时，该参数配置为“ENODEB_IND(eNodeB指示)”。<br>- 当希望通过[**ADD S1ACCAREALST**](../../../区域漫游限制管理/S1模式区域漫游限制参数/增加S1模式接入控制配置（ADD S1ACCAREALST）_72345153.md)命令禁止签约了特征RFSP的用户接入指定区域时则配置为“ACC_REJECT(区域接入控制)”。 |
| BEGRFSP | 起始RFSP | 可选必选说明：必选参数<br>参数含义：该参数用于指定一段连续特征RFSP的起始值。<br>数据来源：整网规划<br>取值范围：1~256<br>默认值：无 |
| ENDRFSP | 终止RFSP | 可选必选说明：必选参数<br>参数含义：该参数用于指定一段连续特征RFSP的终止值。<br>数据来源：整网规划<br>取值范围：1~256<br>默认值：无<br>配置原则：<br>“ENDRFSP(终止RFSP)”<br>必须大于或等于<br>“BEGRFSP(起始RFSP)”<br>。 |

#### [使用实例](#ZH-CN_MMLREF_0000001126145534)

增加一组RFSP从1到10的ACC_REJECT类型的RFSP，索引值为1：

ADD SPECRFSPVALUE: RFSPIDX=1, TYPE=ACC_REJECT, BEGRFSP=1, ENDRFSP=10;
