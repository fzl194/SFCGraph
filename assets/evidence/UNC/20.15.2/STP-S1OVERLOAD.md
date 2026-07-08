# 停止S1接口过载控制(STP S1OVERLOAD)

- [命令功能](#ZH-CN_MMLREF_0000001126306062__1.3.1.1)
- [注意事项](#ZH-CN_MMLREF_0000001126306062__1.3.2.1)
- [本地用户权限](#ZH-CN_MMLREF_0000001126306062__1.3.3.1)
- [网管用户权限](#ZH-CN_MMLREF_0000001126306062__1.3.4.1)
- [参数说明](#ZH-CN_MMLREF_0000001126306062__1.3.5.1)
- [使用实例](#ZH-CN_MMLREF_0000001126306062__1.3.6.1)

#### [命令功能](#ZH-CN_MMLREF_0000001126306062)

**适用网元：MME**

此命令用于停止S1接口过载控制，用于发送overload stop消息给eNodeB。

#### [注意事项](#ZH-CN_MMLREF_0000001126306062)

无。

#### [本地用户权限](#ZH-CN_MMLREF_0000001126306062)

manage-ug；system-ug

#### [网管用户权限](#ZH-CN_MMLREF_0000001126306062)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_MMLREF_0000001126306062)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ENODERANGE | eNodeB范围 | 可选必选说明：可选参数<br>参数含义：该参数用于指定一个eNodeB范围。<br>取值范围：<br>- “ALL_ENODEB(所有eNodeB)”<br>- “SPECIFY_ENODEB(指定eNodeB)”<br>默认值：<br>“SPECIFY_ENODEB(指定eNodeB)”<br>说明：- ALL_ENODEB：用于所有eNodeB强制停止系统自动触发的过载控制流程。<br>- SPECIFY_ENODEB：设定停止S1接口过载控制的eNodeB范围。 |
| BGENODEBID | 起始eNodeB标识 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定起始eNodeB的ID。<br>前提条件：该参数在<br>“ENODERANGE”<br>参数配置为<br>“SPECIFY_ENODEB(指定eNodeB)”<br>时生效。<br>取值范围：0～268435455<br>默认值：无<br>说明：“EDENODEBID”<br>必须大于等于<br>“BGENODEBID”<br>。 |
| EDENODEBID | 终止eNodeB标识 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定终止eNodeB的ID。<br>前提条件：该参数在<br>“ENODERANGE”<br>参数配置为<br>“SPECIFY_ENODEB(指定eNodeB)”<br>时生效。<br>取值范围：0～268435455<br>默认值：无<br>说明：“EDENODEBID”<br>必须大于等于<br>“BGENODEBID”<br>。 |

#### [使用实例](#ZH-CN_MMLREF_0000001126306062)

停止一个eNodeB范围为SPECIFY_ENODEB(指定eNodeB)，起始eNodeB标识为100，终止eNodeB标识为1000的S1接口过载控制：

STP S1OVERLOAD: ENODERANGE=SPECIFY_ENODEB, BGENODEBID=100, EDENODEBID=1000;
