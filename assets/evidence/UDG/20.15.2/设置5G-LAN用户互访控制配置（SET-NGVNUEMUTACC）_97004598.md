# 设置5G LAN用户互访控制配置（SET NGVNUEMUTACC）

- [命令功能](#ZH-CN_CONCEPT_0000206197004598__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000206197004598__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000206197004598__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000206197004598__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000206197004598__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0000206197004598)

**适用NF：UPF**

![](设置5G LAN用户互访控制配置（SET NGVNUEMUTACC）_97004598.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，5G LAN组下终端通过N9A接口互访策略配置为禁止转发时，组内终端通过N9A接口无法进行互访。

该命令用于配置指定5G LAN组下用户互访策略。

#### [注意事项](#ZH-CN_CONCEPT_0000206197004598)

- 该命令执行后立即生效。
- 该命令最大记录数为512。
- 5G LAN组实例存在。

#### [操作用户权限](#ZH-CN_CONCEPT_0000206197004598)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000206197004598)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VNINSTANCE | 5G LAN组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定5G LAN会话实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为18～37。VNINSTANCE以连字号分为4段，形式为GroupServiceID-MCC-MNC-LocalGroupID。其中，GroupServiceID长度为8，只能输入数字或者范围为A到F或a-f的字母；MCC长度为3，只能输入数字；MNC长度为2~3，只能输入数字；LocalGroupID长度为2~20的偶数，只能输入数字或者范围为A到F或a-f的字母。例如，A0000001-460-003-01，A0000001-460-003-A000000001。不区分大小写。<br>默认值：无<br>配置原则：无 |
| N9AUE2UEUNIPOL | N9A口单播互访控制策略 | 可选必选说明：可选参数<br>参数含义：该参数用于配置5G LAN N9A接口单播报文终端互访控制策略。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ALLOW_FWD：允许UE互访报文转发。<br>- FORBID_FWD：禁止UE互访报文转发。<br>- WHITELIST_FWD：UE互访报文转发根据白名单控制。<br>默认值：无<br>配置原则：无 |
| N9AUE2UEMULPOL | N9A口组播互访控制策略 | 可选必选说明：可选参数<br>参数含义：该参数用于配置5G LAN N9A接口组播报文终端互访控制策略。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ALLOW_FWD：允许UE互访报文转发。<br>- FORBID_FWD：禁止UE互访报文转发。<br>- WHITELIST_FWD：UE互访报文转发根据白名单控制。<br>默认值：无<br>配置原则：无 |
| N9AUE2UEBROPOL | N9A口广播互访控制策略 | 可选必选说明：可选参数<br>参数含义：该参数用于配置5G LAN N9A接口广播报文终端互访控制策略。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ALLOW_FWD：允许UE互访报文转发。<br>- FORBID_FWD：禁止UE互访报文转发。<br>- WHITELIST_FWD：UE互访报文转发根据白名单控制。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0000206197004598)

配置5GLAN会话实例"a0000001-460-01-01"的用户互访策略，N9A口单播、组播、广播互访控制策略均为白名单控制：

```
SET NGVNUEMUTACC: VNINSTANCE="a0000001-460-01-01", N9AUE2UEUNIPOL=WHITELIST_FWD, N9AUE2UEMULPOL=WHITELIST_FWD, N9AUE2UEBROPOL=WHITELIST_FWD;
```
