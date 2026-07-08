# 删除HSS BYPASS最小用户签约数据配置 (RMV HSSBPUSRSUB)

- [命令功能](#ZH-CN_CONCEPT_0000001264009372__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000001264009372__1.3.2.1)
- [本地用户权限](#ZH-CN_CONCEPT_0000001264009372__1.3.3.1)
- [网管用户权限](#ZH-CN_CONCEPT_0000001264009372__1.3.4.1)
- [参数说明](#ZH-CN_CONCEPT_0000001264009372__1.3.5.1)
- [使用实例](#ZH-CN_CONCEPT_0000001264009372__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0000001264009372)

**适用网元：MME**

此命令用于删除HSS BYPASS最小用户签约数据配置。

#### [注意事项](#ZH-CN_CONCEPT_0000001264009372)

- 该命令执行后立即生效。

#### [本地用户权限](#ZH-CN_CONCEPT_0000001264009372)

manage-ug；system-ug

#### [网管用户权限](#ZH-CN_CONCEPT_0000001264009372)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000001264009372)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定配置HSS BYPASS最小签约数据集的用户范围。<br>数据来源：本端规划<br>取值范围：<br>- “ALL_USER(所有用户)”<br>- “FOREIGN_USER(外网用户)”<br>- “HOME_USER(本网用户)”<br>- “IMSI_PREFIX(指定IMSI前缀)”<br>默认值：无<br>配置原则：对于指定的用户（群），HSS Bypass最小签约数据集的匹配优先级从高到低依次为：<br>“IMSI_PREFIX(指定IMSI前缀)”<br>，“FOREIGN_USER(外网用户)”或“HOME_USER(本网用户)”，“ALL_USER(所有用户)”。 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定IMSI前缀以区分不同的用户群。<br>前提条件：该参数在<br>“用户范围”<br>参数配置为<br>“IMSI_PREFIX(指定IMSI前缀)”<br>后生效。<br>数据来源：本端规划<br>取值范围：5～15位十进制数字字符串<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0000001264009372)

删除HSS BYPASS最小用户签约数据配置，可以用如下命令：

```
RMV HSSBPUSRSUB: SUBRANGE=IMSI_PREFIX, IMSIPRE="12134567";
```
