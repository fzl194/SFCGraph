# 复位S1AP连接(RST S1APLNK)

- [命令功能](#ZH-CN_MMLREF_0000001172225931__1.3.1.1)
- [注意事项](#ZH-CN_MMLREF_0000001172225931__1.3.2.1)
- [本地用户权限](#ZH-CN_MMLREF_0000001172225931__1.3.3.1)
- [网管用户权限](#ZH-CN_MMLREF_0000001172225931__1.3.4.1)
- [参数说明](#ZH-CN_MMLREF_0000001172225931__1.3.5.1)
- [使用实例](#ZH-CN_MMLREF_0000001172225931__1.3.6.1)

#### [命令功能](#ZH-CN_MMLREF_0000001172225931)

**适用网元：MME**

此命令用于复位S1AP连接。

#### [注意事项](#ZH-CN_MMLREF_0000001172225931)

- 此命令执行后立即生效。
- 执行此命令会导致S1AP链路连接中断，该eNodeB下所有的业务中断，请慎重使用。

#### [本地用户权限](#ZH-CN_MMLREF_0000001172225931)

manage-ug；system-ug

#### [网管用户权限](#ZH-CN_MMLREF_0000001172225931)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_MMLREF_0000001172225931)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RESETTYPE | 复位类型 | 可选必选说明:可选参数<br>参数含义：待复位的S1AP连接的类型。<br>取值范围：<br>- “ALL”：复位该eNodeB下的所有用户的S1AP连接信息。<br>- “PART”：随机选择该eNodeB下一部分用户的S1AP连接信息，进行复位。<br>默认值：<br>“ALL”<br>说明：用户的S1AP连接指的是每个用户在附着、路由更新等流程中建立的S1逻辑连接，当连接释放时，此用户状态就切换到EMM_IDLE态。 |
| MCC | 移动国家码 | 可选必选说明：必选参数<br>参数含义：待复位的S1AP连接的eNodeB的移动国家码。<br>取值范围：3位十进制数<br>默认值：无<br>说明：在“MML命令行-UNC”窗口上执行命令<br>[**DSP S1APLNK**](显示S1AP连接状态(DSP S1APLNK)_26146252.md)<br>查看当前系统里面已经存在的S1AP连接信息。 |
| MNC | 移动网号 | 可选必选说明：必选参数<br>参数含义：待复位的S1AP连接的eNodeB的移动网号。<br>取值范围：位数为2或3的十进制数字<br>默认值：无<br>说明：在“MML命令行-UNC”窗口上执行命令<br>[**DSP S1APLNK**](显示S1AP连接状态(DSP S1APLNK)_26146252.md)<br>查看当前系统里面已经存在的S1AP连接信息。 |
| ENODEBTYPE | eNodeB类型 | 可选必选说明：必选参数<br>参数含义：待复位的S1AP连接的eNodeB的类型。<br>取值范围：<br>- “HOME_ENB(HOME_ENB)”<br>- “MACRO_ENB(MACRO_ENB)”<br>默认值：无<br>说明：在“MML命令行-UNC”窗口上执行命令<br>[**DSP S1APLNK**](显示S1AP连接状态(DSP S1APLNK)_26146252.md)<br>查看当前系统里面已经存在的S1AP连接信息。 |
| ENODEBID | eNodeB标识 | 可选必选说明：必选参数<br>参数含义：待复位的S1AP连接的eNodeB的标识。<br>取值范围：0～268435455<br>默认值：无<br>说明：在“MML命令行-UNC”窗口上执行命令<br>[**DSP S1APLNK**](显示S1AP连接状态(DSP S1APLNK)_26146252.md)<br>查看当前系统里面已经存在的S1AP连接信息。 |

#### [使用实例](#ZH-CN_MMLREF_0000001172225931)

复位移动国家码为308，移动网号为07，id为2的home eNodeB的偶联上的部分用户的s1连接：

RST S1APLNK: RESETTYPE=PART, MCC="308", MNC="07", ENODEBTYPE=HOME_ENB, ENODEBID=2;
