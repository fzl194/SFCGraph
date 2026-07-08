# 设置CP Data流控参数(SET CPDATAFLOWCTRL)

- [命令功能](#ZH-CN_CONCEPT_0000001172345769__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000001172345769__1.3.2.1)
- [本地用户权限](#ZH-CN_CONCEPT_0000001172345769__1.3.3.1)
- [网管用户权限](#ZH-CN_CONCEPT_0000001172345769__1.3.4.1)
- [参数说明](#ZH-CN_CONCEPT_0000001172345769__1.3.5.1)
- [使用实例](#ZH-CN_CONCEPT_0000001172345769__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0000001172345769)

**适用网元：MME**

此命令用于设置CP Data流控参数。

#### [注意事项](#ZH-CN_CONCEPT_0000001172345769)

无。

#### [本地用户权限](#ZH-CN_CONCEPT_0000001172345769)

manage-ug；system-ug。

#### [网管用户权限](#ZH-CN_CONCEPT_0000001172345769)

G_1，管理员级别命令组；G_2，操作员级别命令组。

#### [参数说明](#ZH-CN_CONCEPT_0000001172345769)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CPDATACPUFLOWSW | CP Data CPU过载流控功能开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定MME CPU过载时，是否开启CP Data的流控功能。功能开启后，如果MME的CPU过载，MME将对使用WSFD-<br>215101<br>基于信令面的数据传输特性的终端进行流控，在Attach Accept、Tau Accept、Service Accept、Service Reject消息中携带Control Plane data back-off timer T3448，通知终端延迟发送数据，缓解MME的系统过载状况。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- OFF（关闭）。<br>- ON （打开）。<br>系统初始设置值：OFF（关闭）<br>配置原则：<br>- 系统目前暂不支持。 |
| MINT3448 | T3448最小值（秒） | 可选必选说明：可选参数<br>参数含义：本参数用于设置Control Plane data back-off timer T3448的最小值，用于计算发给终端的Attach Accept、Tau Accept、Service Accept、Service Reject消息中的T3448时长。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～11160。<br>系统初始设置值：900。<br>配置原则：<br>- 该参数的取值必须小于等于“T3448最大值”的取值。<br>- 系统目前暂不支持。 |
| MAXT3448 | T3448最大值（秒） | 可选必选说明：可选参数<br>参数含义：本参数用于设置Control Plane data back-off timer T3448的最大值，用于计算发给终端的Attach Accept、Tau Accept、Service Accept、Service Reject消息中的T3448时长。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～11160。<br>系统初始设置值：1800。<br>配置原则：<br>- 该参数的取值必须大于等于“T3448最小值”的取值。<br>- 系统目前暂不支持。 |

#### [使用实例](#ZH-CN_CONCEPT_0000001172345769)

设置 “CP Data CPU过载流控功能开关” 为 “ON” ， “T3448最小值（秒）” 为 “500” 和 “T3448最大值（秒）” 为 “800” ：

SET CPDATAFLOWCTRL:CPDATACPUFLOWSW=ON,MINT3448 = 500,MAXT3448 = 800;
