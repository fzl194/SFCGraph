# 修改本端重启次数(MOD RECOVERY)

- [命令功能](#ZH-CN_MMLREF_0000001172225609__1.3.1.1)
- [注意事项](#ZH-CN_MMLREF_0000001172225609__1.3.2.1)
- [本地用户权限](#ZH-CN_MMLREF_0000001172225609__1.3.3.1)
- [网管用户权限](#ZH-CN_MMLREF_0000001172225609__1.3.4.1)
- [参数说明](#ZH-CN_MMLREF_0000001172225609__1.3.5.1)
- [使用实例](#ZH-CN_MMLREF_0000001172225609__1.3.6.1)

#### [命令功能](#ZH-CN_MMLREF_0000001172225609)

![](修改本端重启次数(MOD RECOVERY)_72225609.assets/notice_3.0-zh-cn_2.png)

该命令可能导致对端网元无法正常处理GTPC消息。

**适用网元：SGSN、MME、AMF**

该命令用于修改本端Recovery值。本端Recovery值表示本端系统重启的次数。

#### [注意事项](#ZH-CN_MMLREF_0000001172225609)

- 此命令执行后立即生效。
- 如果本端Recovery值设置不合理，可能导致对端删除承载或者消息无法正常处理，请谨慎设置。
- 如果通过本命令修改Recovery值后，只影响当前Recovery值，后续当本端设备重启后，Recovery值会在本次修改值基础上继续增加。
- 当命令**[SET AMFN26PLCY](../../../../../接口管理/GTP-C接口配置管理/N26接口管理/N26策略管理/设置AMF N26接口策略（SET AMFN26PLCY）_62817114.md)**的参数“N26ITFMODE”取值为“COMBINE”时，该命令适用于SGSN、MME、AMF，否则，该命令仅适用于SGSN、MME。

#### [本地用户权限](#ZH-CN_MMLREF_0000001172225609)

manage-ug；system-ug

#### [网管用户权限](#ZH-CN_MMLREF_0000001172225609)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_MMLREF_0000001172225609)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RECOVERYVALUE | RECOVERY值 | 可选必选说明：必选。<br>参数含义：该参数用于指定本端Recovery值。<br>数据来源：整网规划<br>取值范围：0~255<br>默认值：无<br>配置原则：<br>请根据现网需要合理设置Recovery值。 |

#### [使用实例](#ZH-CN_MMLREF_0000001172225609)

将本端recovery值修改为9：

MOD RECOVERY: RECOVERYVALUE=9;
