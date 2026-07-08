# 删除IMEI库记录（RMV SMACTIMEILIB）

- [命令功能](#ZH-CN_MMLREF_0000001172345261__1.3.1.1)
- [注意事项](#ZH-CN_MMLREF_0000001172345261__1.3.2.1)
- [本地用户权限](#ZH-CN_MMLREF_0000001172345261__1.3.3.1)
- [网管用户权限](#ZH-CN_MMLREF_0000001172345261__1.3.4.1)
- [参数说明](#ZH-CN_MMLREF_0000001172345261__1.3.5.1)
- [使用实例](#ZH-CN_MMLREF_0000001172345261__1.3.6.1)

#### [命令功能](#ZH-CN_MMLREF_0000001172345261)

**适用网元：SGSN、MME**

此命令用于删除终端IMEI记录。终端IMEI记录为IMEI TAC和终端类型的对应关系表，用于按照IMEI识别智能终端。

#### [注意事项](#ZH-CN_MMLREF_0000001172345261)

此命令执行后立即生效。

#### [本地用户权限](#ZH-CN_MMLREF_0000001172345261)

manage-ug；system-ug

#### [网管用户权限](#ZH-CN_MMLREF_0000001172345261)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_MMLREF_0000001172345261)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SELMODE | 选择方式 | 可选必选说明：必选参数<br>参数含义：该参数用于选择删除终端IMEI记录的方式。<br>取值范围：<br>- “IMEI_TAC(设备型号核准号码)”<br>- “UE_TYPE(终端类型)”<br>- “ALL(所有)”<br>默认值：无 |
| IMEITAC | 设备型号核准号码 | 可选必选说明：条件必选参数<br>参数含义：该参数为用于删除终端IMEI记录的设备型号核准号码。<br>前提条件：当<br>“选择方式”<br>配置为<br>“IMEI_TAC(设备型号核准号码)”<br>时，此参数才生效。<br>取值范围：8位十进制数<br>默认值：无 |
| UETYPE | 终端类型 | 可选必选说明：条件必选参数<br>参数含义：该参数为用于删除终端IMEI记录的终端类型。<br>前提条件：当<br>“选择方式”<br>配置为<br>“UE_TYPE(终端类型)”<br>时，此参数才生效。<br>取值范围：<br>- “ANDROID(Android)”<br>- “BLACKBERRY(Black Berry)”<br>- “IOS(iOS)”<br>- “WINDOWS(Windows)”<br>- “CUSTOM_TYPE_1(自定义类型1)”<br>- “CUSTOM_TYPE_2(自定义类型2)”<br>- “CUSTOM_TYPE_3(自定义类型3)”<br>- “CUSTOM_TYPE_4(自定义类型4)”<br>- “CUSTOM_TYPE_5(自定义类型5)”<br>- “CUSTOM_TYPE_6(自定义类型6)”<br>- “CUSTOM_TYPE_7(自定义类型7)”<br>- “CUSTOM_TYPE_8(自定义类型8)”<br>- “CUSTOM_TYPE_9(自定义类型9)”<br>- “CUSTOM_TYPE_10(自定义类型10)”<br>- “CUSTOM_TYPE_11(自定义类型11)”<br>- “CUSTOM_TYPE_12(自定义类型12)”<br>默认值：无 |

#### [使用实例](#ZH-CN_MMLREF_0000001172345261)

删除IMEI TAC为12345670的终端IMEI记录：

RMV SMACTIMEILIB: SELMODE=IMEI_TAC, IMEITAC="12345670";
