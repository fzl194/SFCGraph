# 设置SMSF白名单开关（SET NRFSMSFWHLISTSW）

- [命令功能](#ZH-CN_MMLREF_0000001322223361__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001322223361__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001322223361__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001322223361__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0000001322223361)

![](设置SMSF白名单开关（SET NRFSMSFWHLISTSW）_22223361.assets/notice_3.0-zh-cn_2.png)

该命令与ADD NRFSMSFWHITELST配合使用，在白名单未设置完成时请勿打开SMSFWHLISTSW，否则未加入到白名单中的SMSF在发现参数仅携带TargetNftype时将无法被发现。

**适用NF：NRF**

该命令用于设置SMSF白名单功能是否打开。白名单用于配置现网存量SMSF，避免新升级的SMSF不能为存量用户提供业务，导致错误业务导流。

## [注意事项](#ZH-CN_MMLREF_0000001322223361)

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| SMSFWHLISTSW |
| --- |
| FUNC_OFF |

#### [操作用户权限](#ZH-CN_MMLREF_0000001322223361)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001322223361)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SMSFWHLISTSW | SMSF白名单开关 | 可选必选说明：必选参数<br>参数含义：该参数用于表示SMSF白名单功能是否打开。 当开关设置为FUNC_ON时，NF基于NFtype发现SMSF，NRF仅会与SMSF白名单中的网元进行匹配；当开关设置为FUNC_OFF时，NRF将会正常匹配SMSF。<br>数据来源：本端规划<br>取值范围：<br>- FUNC_ON（打开）<br>- FUNC_OFF（关闭）<br>默认值：无。<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0000001322223361)

打开SMSF白名单开关，执行如下命令：

```
SET NRFSMSFWHLISTSW: SMSFWHLISTSW=FUNC_ON;
```
