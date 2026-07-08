# 删除APN DNS域名策略(RMV APNDNS)

- [命令功能](#ZH-CN_MMLREF_0000001172225611__1.3.1.1)
- [注意事项](#ZH-CN_MMLREF_0000001172225611__1.3.2.1)
- [本地用户权限](#ZH-CN_MMLREF_0000001172225611__1.3.3.1)
- [网管用户权限](#ZH-CN_MMLREF_0000001172225611__1.3.4.1)
- [参数说明](#ZH-CN_MMLREF_0000001172225611__1.3.5.1)
- [使用实例](#ZH-CN_MMLREF_0000001172225611__1.3.6.1)

#### [命令功能](#ZH-CN_MMLREF_0000001172225611)

**适用网元：SGSN、MME**

该命令用于删除APN DNS域名策略。

#### [注意事项](#ZH-CN_MMLREF_0000001172225611)

- 该命令执行后立即生效。

#### [本地用户权限](#ZH-CN_MMLREF_0000001172225611)

manage-ug；system-ug

#### [网管用户权限](#ZH-CN_MMLREF_0000001172225611)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_MMLREF_0000001172225611)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APNNI | APN网络标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN网络标识。详见命令<br>[**ADD APNDNS**](增加APN DNS域名策略(ADD APNDNS)_26145932.md)<br>。<br>数据来源：整网规划<br>取值范围：1～62位字符串<br>默认值：无 |
| UEACCCAP | UE接入能力 | 可选必选说明：必选参数<br>参数含义：该参数用于指定UE接入2/3/4G网络的能力。<br>数据来源：整网规划<br>取值范围：<br>- “GERAN/UTRAN_UE(GERAN/UTRAN UE)”<br>- “EUTRAN_UE(EUTRAN UE)”<br>- “GERAN/UTRAN/EUTRAN_UE(GERAN/UTRAN/EUTRAN UE)”<br>- “ALL_UE(ALL UE)”<br>默认值 ：无 |

#### [使用实例](#ZH-CN_MMLREF_0000001172225611)

删除 “APN网络标识” 为“huawei.com”， “根据UE接入能力选择” 为 “EUTRAN_UE(EUTRAN UE)” 的DNS策略:

**RMV APNDNS: APNNI="huawei.com", UEACCCAP=EUTRAN_UE;**
