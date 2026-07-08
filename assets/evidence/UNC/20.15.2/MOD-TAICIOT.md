# 修改CIoT能力配置(MOD TAICIOT)

- [命令功能](#ZH-CN_MMLREF_0000001126145782__1.3.1.1)
- [注意事项](#ZH-CN_MMLREF_0000001126145782__1.3.2.1)
- [本地用户权限](#ZH-CN_MMLREF_0000001126145782__1.3.3.1)
- [网管用户权限](#ZH-CN_MMLREF_0000001126145782__1.3.4.1)
- [参数说明](#ZH-CN_MMLREF_0000001126145782__1.3.5.1)
- [使用实例](#ZH-CN_MMLREF_0000001126145782__1.3.6.1)

#### [命令功能](#ZH-CN_MMLREF_0000001126145782)

**适用网元：MME**

该命令用于修改TAI范围内所有eNodeB的蜂窝物联网（CIoT）能力。

#### [注意事项](#ZH-CN_MMLREF_0000001126145782)

该命令执行后，在用户新的Attach/TAU流程中系统才会识别eNodeB的蜂窝物联网（CIoT）能力。

#### [本地用户权限](#ZH-CN_MMLREF_0000001126145782)

manage-ug；system-ug

#### [网管用户权限](#ZH-CN_MMLREF_0000001126145782)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_MMLREF_0000001126145782)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| BEGINTAI | 起始TAI | 可选必选说明：必选参数<br>参数含义：该参数用于指定跟踪区标识，标识一个起始跟踪区。<br>数据来源：全网规划<br>取值范围：9～10位的字符串。<br>默认值：无<br>配置原则：<br>- 起始TAI由MCC，MNC，TAC组成。<br>- MCC为3个BCD码字符，MNC为2个或者3个BCD码字符，填写时请遵循实际长度。<br>- TAC编码为16进制数，固定为4位，不足补0。 |
| NBDATATRANSSUPPORT | 窄带数据传输能力指示 | 可选必选说明：可选参数<br>参数含义：该参数用于指定所配置TAI范围内所有eNodeB支持窄带蜂窝物联网（NB CIoT）的能力。<br>数据来源：全网规划<br>取值范围：<br>- “SUPPORT_CP（支持CP CIoT）”<br>- “SUPPORT_UP（支持UP CIoT）”<br>- “SUPPORT_S1U（支持S1-U数据传输）”<br>默认值：无<br>配置原则：根据eNodeB能力配置此参数。如果勾选了<br>“SUPPORT_UP”<br>，则无论<br>“SUPPORT_S1U”<br>是否勾选，均按eNodeB支持S1–U数据传输进行处理。 |

#### [使用实例](#ZH-CN_MMLREF_0000001126145782)

当组网发生变化，eNodeB能力发生改变，需要将起始TAI为308015101的窄带CIoT能力指示修改为支持CP CIoT时：

MOD TAICIOT: BEGINTAI="308015101", NBDATATRANSSUPPORT=SUPPORT_CP-1&SUPPORT_UP-0&SUPPORT_S1U-0;
