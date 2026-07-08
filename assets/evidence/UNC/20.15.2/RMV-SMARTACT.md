# 删除激活抑制规则（RMV SMARTACT）

- [命令功能](#ZH-CN_MMLREF_0000001126305552__1.3.1.1)
- [注意事项](#ZH-CN_MMLREF_0000001126305552__1.3.2.1)
- [本地用户权限](#ZH-CN_MMLREF_0000001126305552__1.3.3.1)
- [网管用户权限](#ZH-CN_MMLREF_0000001126305552__1.3.4.1)
- [参数说明](#ZH-CN_MMLREF_0000001126305552__1.3.5.1)
- [使用实例](#ZH-CN_MMLREF_0000001126305552__1.3.6.1)

#### [命令功能](#ZH-CN_MMLREF_0000001126305552)

**适用网元：SGSN**

此命令用于删除基于用户终端类型的激活抑制规则。当不需要对某种智能终端进行激活抑制时，需要执行此命令。

#### [注意事项](#ZH-CN_MMLREF_0000001126305552)

- 此命令执行后，当此终端类型的用户出现激活异常时，将不进行激活抑制，进行正常的激活流程。
- 此命令执行后立即生效。

#### [本地用户权限](#ZH-CN_MMLREF_0000001126305552)

manage-ug；system-ug

#### [网管用户权限](#ZH-CN_MMLREF_0000001126305552)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_MMLREF_0000001126305552)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| UETYPE | 终端类型 | 可选必选说明：必选参数<br>参数含义：待删除的用户的终端类型。<br>取值范围：<br>- “ANDROID(Android)”<br>- “BLACKBERRY(Black Berry)”<br>- “IOS(iOS)”<br>- “WINDOWS(Windows)”<br>- “CUSTOM_TYPE_1(自定义类型1)”<br>- “CUSTOM_TYPE_2(自定义类型2)”<br>- “CUSTOM_TYPE_3(自定义类型3)”<br>- “CUSTOM_TYPE_4(自定义类型4)”<br>- “CUSTOM_TYPE_5(自定义类型5)”<br>- “CUSTOM_TYPE_6(自定义类型6)”<br>- “CUSTOM_TYPE_7(自定义类型7)”<br>- “CUSTOM_TYPE_8(自定义类型8)”<br>- “CUSTOM_TYPE_9(自定义类型9)”<br>- “CUSTOM_TYPE_10(自定义类型10)”<br>- “CUSTOM_TYPE_11(自定义类型11)”<br>- “CUSTOM_TYPE_12(自定义类型12)”<br>- “UNKNOWN_TYPE(未知类型)”<br>默认值：无<br>说明：“UNKNOWN_TYPE(未知类型)”<br>是指没有对应的IMEILIB或APNNILIB配置的终端类型。除<br>“UNKNOWN_TYPE(未知类型)”<br>以外的终端类型，可通过<br>[**ADD IMEILIB**](../../终端类型识别/IMEI库管理/增加IMEI库记录（ADD IMEILIB）_26145734.md)<br>或<br>[**ADD APNNILIB**](../../终端类型识别/APNNI库管理/增加APNNI库记录（ADD APNNILIB）_26145736.md)<br>命令设置。 |

#### [使用实例](#ZH-CN_MMLREF_0000001126305552)

删除终端类型为黑莓的用户的激活抑制规则：

RMV SMARTACT: UETYPE=BLACKBERRY;
