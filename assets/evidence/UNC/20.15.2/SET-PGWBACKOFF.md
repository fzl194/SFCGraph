# 设置P-GW Back-off流控参数(SET PGWBACKOFF)

- [命令功能](#ZH-CN_MMLREF_0000001172345761__1.3.1.1)
- [注意事项](#ZH-CN_MMLREF_0000001172345761__1.3.2.1)
- [本地用户权限](#ZH-CN_MMLREF_0000001172345761__1.3.3.1)
- [网管用户权限](#ZH-CN_MMLREF_0000001172345761__1.3.4.1)
- [参数说明](#ZH-CN_MMLREF_0000001172345761__1.3.5.1)
- [使用实例](#ZH-CN_MMLREF_0000001172345761__1.3.6.1)

#### [命令功能](#ZH-CN_MMLREF_0000001172345761)

**适用网元：MME**

该命令用于设置P-GW Back-off流控功能的相关参数。MME支持基于P-GW Back-off timer的APN级流控功能会使用到本命令。

#### [注意事项](#ZH-CN_MMLREF_0000001172345761)

- 该命令执行后立即生效。
- 此配置涉及WSFD-215201基于延迟定时器的信令拥塞控制特性，license部件编码：LKV2LTCC01，请在设置参数前使用[**DSP LICENSE**](../../../../../../../../平台服务管理/操作维护/License管理/显示License(DSP LICENSE)_00360098.md)命令确认对应特性license是否得到授权，执行[**LST LICENSESWITCH**](../../../../../../../../平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md)命令确认特性开关状态为“ENABLE(打开)”。

#### [本地用户权限](#ZH-CN_MMLREF_0000001172345761)

manage-ug；system-ug

#### [网管用户权限](#ZH-CN_MMLREF_0000001172345761)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_MMLREF_0000001172345761)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FCSWITCH | 流控开关 | 可选必选说明：可选参数<br>参数含义：本参数用于指定是否开启P-GW Back-off流控功能。<br>数据来源：本端规划<br>取值范围：<br>- “OFF(关)”<br>- “ON(开)”<br>系统初始设置值：<br>“OFF(关)”<br>。<br>配置原则：基于延迟定时器的信令拥塞控制特性依赖于网关下发的P-GW Back-off Timer信元，需要MME和网关同时开启才能使用。 |
| APNNIGRPID | APNNI组号 | 可选必选说明：条件必选参数<br>参数含义：本参数用户设置支持P-GW Back-off APN流控的APNNI组号。<br>前提条件:本参数在“流控开关”参数配置为“ON(开)”后生效。<br>数据来源：本端规划<br>取值范围：0～15<br>系统初始设置值：无<br>配置原则：组号需要引用<br>[**ADD APNNIGROUP**](../../../../../业务安全管理/会话管理/APNNI信息管理/APNNI组管理/增加APNNI组(ADD APNNIGROUP)_26305508.md)<br>命令中已配置的组号。 |
| PGWGRPID | P-GW组号 | 可选必选说明：条件必选参数<br>参数含义：本参数用于表示用户设置支持P-GW Back-off APN流控的P-GW组号。<br>前提条件: 本参数在“流控开关”参数配置为“ON(开)”后生效。<br>数据来源：本端规划<br>取值范围：0～15<br>系统初始设置值：无<br>配置原则：组号需要引用<br>[**ADD PGWGROUP**](../../../../../业务安全管理/会话管理/P-GW信息管理/P-GW组管理/增加P-GW组(ADD PGWGROUP)_72225385.md)<br>命令中已配置的组号。 |

#### [使用实例](#ZH-CN_MMLREF_0000001172345761)

启用信令拥塞控制功能时，设置流控功能的相关参数。设置“流控开关”参数为“ON(开)”、“APNNI组号”参数为“2”，“P-GW组号”参数为“2”。运行如下命令：

SET PGWBACKOFF: FCSWITCH=ON, APNNIGRPID=2, PGWGRPID=2;
