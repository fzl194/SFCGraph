# 增加HSS BYPASS最小用户签约数据配置 (ADD HSSBPUSRSUB)

- [命令功能](#ZH-CN_CONCEPT_0000001311529413__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000001311529413__1.3.2.1)
- [本地用户权限](#ZH-CN_CONCEPT_0000001311529413__1.3.3.1)
- [网管用户权限](#ZH-CN_CONCEPT_0000001311529413__1.3.4.1)
- [参数说明](#ZH-CN_CONCEPT_0000001311529413__1.3.5.1)
- [使用实例](#ZH-CN_CONCEPT_0000001311529413__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0000001311529413)

**适用网元：MME**

此命令用于新增HSS BYPASS最小用户签约数据配置。

用户处于HSS BYPASS状态之后，无法从HSS获取用户签约数据，如果系统内无用户历史签约数据，使用该命令手动配置用户最小签约数据，保证业务惯性运行。

#### [注意事项](#ZH-CN_CONCEPT_0000001311529413)

- 该命令执行后立即生效。
- 此命令最大记录数为1024。

#### [本地用户权限](#ZH-CN_CONCEPT_0000001311529413)

manage-ug；system-ug

#### [网管用户权限](#ZH-CN_CONCEPT_0000001311529413)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000001311529413)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定配置HSS BYPASS最小签约数据集的用户范围。<br>数据来源：本端规划<br>取值范围：<br>- “ALL_USER(所有用户)”<br>- “FOREIGN_USER(外网用户)”<br>- “HOME_USER(本网用户)”<br>- “IMSI_PREFIX(指定IMSI前缀)”<br>默认值：无<br>配置原则：对于指定的用户（群），HSS Bypass最小签约数据集的匹配优先级从高到低依次为：<br>“IMSI_PREFIX(指定IMSI前缀)”<br>，“FOREIGN_USER(外网用户)”或“HOME_USER(本网用户)”，“ALL_USER(所有用户)”。 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定IMSI前缀以区分不同的用户群。<br>前提条件：该参数在<br>“用户范围”<br>参数配置为<br>“IMSI_PREFIX(指定IMSI前缀)”<br>后生效。<br>数据来源：本端规划<br>取值范围：5～15位十进制数字字符串<br>默认值：无<br>配置原则：无 |
| STNSR | STN-SR | 可选必选说明：可选参数<br>参数含义：该参数用于指定用户的STN-SR。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1-16位的十六进制数<br>默认值：无<br>配置原则：无<br>说明：该参数会覆盖Forward Relocation Request消息携带的STN-SR信元。 |
| NETACCMODE | 网络接入模式 | 可选必选说明：可选参数<br>参数含义：该参数用于指定用户支持的Network-Access-Mode。<br>数据来源：本端规划<br>取值范围：<br>- PS_CS（PS和CS域）：PS和CS域<br>- PS（仅PS域）：仅PS域<br>默认值：PS_CS（PS和CS域）<br>配置原则：无 |
| ODB | 运营商闭锁分组业务 | 可选必选说明：可选参数<br>参数含义：该参数表示用户的ODB业务类型。<br>数据来源：本端规划<br>取值范围：<br>- ALL_PACKET_SERVICES（禁止所有用户）：禁止用户所有分组域业务。<br>- ROAMER_ACCESS_HPLMN_AP（禁止漫游用户使用Home Routed方式）：禁止漫游用户使用Home Routed方式进行分组域业务。<br>- ROAMER_ACCESS_VPLMN_AP（禁止漫游用户使用Local Breakout方式）：禁止漫游用户使用Local Breakout方式进行分组域业务。<br>默认值：无<br>配置原则：无 |
| APNGRPID | APN群组ID | 可选必选说明：必选参数<br>参数含义：用于指定APN本地配置签约群组。<br>数据来源：本端规划<br>取值范围：0~511<br>默认值：无<br>配置原则：须先在<br>[ADD HSSBPAPNGRP](增加HSS BYPASS最小APN签约数据群组 (ADD HSSBPAPNGRP)_64181038.md)<br>中配置取值相同的<br>“APNGRPID”<br>参数。 |

#### [使用实例](#ZH-CN_CONCEPT_0000001311529413)

添加HSS BYPASS最小用户签约数据配置，可以用如下命令：

```
ADD HSSBPUSRSUB: SUBRANGE=IMSI_PREFIX, IMSIPRE="12134567", STNSR="FF123", NETACCMODE=PS_CS, ODB=ALL_PACKET_SERVICES-1&ROAMER_ACCESS_HPLMN_AP-1&ROAMER_ACCESS_VPLMN_AP-1, APNGRPID=0;
```
