# 删除语音部署配置(RMV VOICEDEPLOY)

- [命令功能](#ZH-CN_MMLREF_0000001172225441__1.3.1.1)
- [注意事项](#ZH-CN_MMLREF_0000001172225441__1.3.2.1)
- [本地用户权限](#ZH-CN_MMLREF_0000001172225441__1.3.3.1)
- [网管用户权限](#ZH-CN_MMLREF_0000001172225441__1.3.4.1)
- [参数说明](#ZH-CN_MMLREF_0000001172225441__1.3.5.1)
- [使用实例](#ZH-CN_MMLREF_0000001172225441__1.3.6.1)

#### [命令功能](#ZH-CN_MMLREF_0000001172225441)

**适用网元：MME**

该命令用于删除UE使用E-UTRAN网络接入时的IMS VoPS语音部署方案配置。UE使用E-UTRAN网络接入时可以选择两种语音部署方案：

- IMS VoPS（IMS Voice over PS session），即基于IMS网络提供语音业务。PS网络上部署专门的IMS APNNI，用于承载IMS业务相关的信令和数据。
- CSFB（Circuit Switched Fallback），利用现有的GSM /UMTS网络实现语音通话的一种语音解决方案。用户进行语音业务时，由EPS（Evolved Packet System）网络指示用户回落到目标GSM/UMTS电路域（CS）网络之后，再发起语音呼叫。

#### [注意事项](#ZH-CN_MMLREF_0000001172225441)

对于该命令执行后新接入的UE，该命令立即生效。该命令执行时已经在系统中注册过的UE，系统会在UE下一次进行Attach/TAU业务流程时，根据最新的配置对UE进行业务指示。

#### [本地用户权限](#ZH-CN_MMLREF_0000001172225441)

manage-ug；system-ug

#### [网管用户权限](#ZH-CN_MMLREF_0000001172225441)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_MMLREF_0000001172225441)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定所包含的用户范围。<br>数据来源：全网规划<br>取值范围：<br>- “ALL_USER（所有用户）”<br>- “HOME_USER（本网用户）”<br>- “FOREIGN_USER（外网用户）”<br>- “IMSI_PREFIX（指定IMSI前缀）”<br>默认值：无 |
| NOID | 运营商标识 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定运营商标识。<br>前提条件：该参数在<br>“SUBRANGE（用户范围）”<br>配置为<br>“FOREIGN_USER（外网用户）”<br>或<br>“HOME_USER（本网用户）”<br>后生效。<br>数据来源：全网规划<br>取值范围：0～64，128～254<br>默认值：无 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定被删除记录的IMSI前缀。<br>前提条件：此参数在<br>“SUBRANGE（用户范围）”<br>设置为<br>“IMSI_PREFIX（指定IMSI前缀）”<br>时有效。<br>数据来源：全网规划<br>取值范围：1～15位十进制数字字符串<br>默认值：无 |

#### [使用实例](#ZH-CN_MMLREF_0000001172225441)

场景参见 [**ADD VOICEDEPLOY**](增加语音部署配置(ADD VOICEDEPLOY)_72345361.md) 的命令使用实例。

删除外网用户的语音部署配置：

RMV VOICEDEPLOY: SUBRANGE=FOREIGN_USER, NOID=0;
