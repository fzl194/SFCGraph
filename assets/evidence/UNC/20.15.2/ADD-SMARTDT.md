# 增加基于终端类型的DT限制(ADD SMARTDT)

- [命令功能](#ZH-CN_MMLREF_0000001126145738__1.3.1.1)
- [注意事项](#ZH-CN_MMLREF_0000001126145738__1.3.2.1)
- [本地用户权限](#ZH-CN_MMLREF_0000001126145738__1.3.3.1)
- [网管用户权限](#ZH-CN_MMLREF_0000001126145738__1.3.4.1)
- [参数说明](#ZH-CN_MMLREF_0000001126145738__1.3.5.1)
- [使用实例](#ZH-CN_MMLREF_0000001126145738__1.3.6.1)

#### [命令功能](#ZH-CN_MMLREF_0000001126145738)

**适用网元：SGSN**

此命令用于增加基于终端类型的Direct Tunnel限制的配置。

#### [注意事项](#ZH-CN_MMLREF_0000001126145738)

- 此命令最大记录数为17条（每种终端类型最多1条）。
- 此特性为可选特性，需要加载支持该特性的License，对应的License项为“Smartphone控制基础功能”。
- 当添加了某种终端类型的SMARTDT配置后，对该终端类型，基于Service Request频率的DT限制功能不再生效。基于Service Request频率的DT限制功能，是由SET SMARTCFG命令的DTSW参数控制的。当SGSN启用了基于Service Request频率的DT限制功能时，又需要针对某种终端类型例外，可执行该命令。
- 执行此命令，可能会导致Direct Tunnel相关的性能指标变化。

#### [本地用户权限](#ZH-CN_MMLREF_0000001126145738)

manage-ug；system-ug

#### [网管用户权限](#ZH-CN_MMLREF_0000001126145738)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_MMLREF_0000001126145738)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| UETYPE | 终端类型 | 可选必选说明：必选参数<br>参数含义：该参数用于设置用户的终端类型。<br>数据来源：本端规划<br>取值范围:<br>- “ANDROID(Android)”<br>- “BLACKBERRY(Black Berry)”<br>- “IOS(iOS)”<br>- “WINDOWS(Windows)”<br>- “CUSTOM_TYPE_1(自定义类型1)”<br>- “CUSTOM_TYPE_2(自定义类型2)”<br>- “CUSTOM_TYPE_3(自定义类型3)”<br>- “CUSTOM_TYPE_4(自定义类型4)”<br>- “CUSTOM_TYPE_5(自定义类型5)”<br>- “CUSTOM_TYPE_6(自定义类型6)”<br>- “CUSTOM_TYPE_7(自定义类型7)”<br>- “CUSTOM_TYPE_8(自定义类型8)”<br>- “CUSTOM_TYPE_9(自定义类型9)”<br>- “CUSTOM_TYPE_10(自定义类型10)”<br>- “CUSTOM_TYPE_11(自定义类型11)”<br>- “CUSTOM_TYPE_12(自定义类型12)”<br>- “UNKNOWN_TYPE(未知类型)”<br>默认值：无<br>说明：- “UNKNOWN_TYPE(未知类型)”是指没有对应的IMEILIB或APNNILIB配置的终端类型。除“UNKNOWN_TYPE(未知类型)”以外的终端类型，可通过[**ADD IMEILIB**](../终端类型识别/IMEI库管理/增加IMEI库记录（ADD IMEILIB）_26145734.md)或[**ADD APNNILIB**](../终端类型识别/APNNI库管理/增加APNNI库记录（ADD APNNILIB）_26145736.md)命令设置。 |
| DTLIMIT | DT限制开关 | 可选必选说明：可选参数<br>参数含义：该参数用于设置Direct Tunnel限制开关，控制是否进行DT限制。<br>数据来源：本端规划<br>取值范围:<br>- “OFF(关闭)”<br>- “ON(开启)”<br>默认值：无 |
| DESC | 描述 | 可选必选说明：可选参数<br>参数含义：该参数用于增加配置命令的描述信息。<br>数据来源：整网规划<br>取值范围：0~32位字符串<br>默认值：无 |

#### [使用实例](#ZH-CN_MMLREF_0000001126145738)

增加终端类型为微软的DT限制记录，对终端类型为微软的用户进行DT限制:

ADD SMARTDT: UETYPE=WINDOWS, DTLIMIT=ON;
