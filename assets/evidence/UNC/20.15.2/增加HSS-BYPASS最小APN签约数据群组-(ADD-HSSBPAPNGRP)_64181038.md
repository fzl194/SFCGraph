# 增加HSS BYPASS最小APN签约数据群组 (ADD HSSBPAPNGRP)

- [命令功能](#ZH-CN_CONCEPT_0000001264181038__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000001264181038__1.3.2.1)
- [本地用户权限](#ZH-CN_CONCEPT_0000001264181038__1.3.3.1)
- [网管用户权限](#ZH-CN_CONCEPT_0000001264181038__1.3.4.1)
- [参数说明](#ZH-CN_CONCEPT_0000001264181038__1.3.5.1)
- [使用实例](#ZH-CN_CONCEPT_0000001264181038__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0000001264181038)

**适用网元：MME**

此命令用于新增HSS BYPASS最小APN签约数据群组。

用户处于HSS BYPASS状态之后，无法从HSS获取用户签约数据，如果系统内无用户历史签约数据，使用该命令手动配置用户最小APN签约数据群组，保证业务惯性运行。

#### [注意事项](#ZH-CN_CONCEPT_0000001264181038)

- 该命令执行后立即生效。
- 此命令最大记录数为512。

#### [本地用户权限](#ZH-CN_CONCEPT_0000001264181038)

manage-ug；system-ug

#### [网管用户权限](#ZH-CN_CONCEPT_0000001264181038)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000001264181038)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APNGRPID | APN群组ID | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN本地配置签约群组ID。<br>数据来源：本端规划<br>取值范围：0~511<br>默认值：无<br>配置原则：无 |
| APNSUBIDX | APN本地签约索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN群组包含的APN本地签约数据索引。<br>数据来源：本端规划<br>取值范围：0~255<br>默认值：无<br>配置原则：须先在<br>[ADD HSSBPAPNSUB](增加HSS BYPASS最小APN签约数据配置 (ADD HSSBPAPNSUB)_11385437.md)<br>中配置取值相同的<br>“APNSUBIDX”<br>参数。 |
| DEFAULTAPN | 是否默认APN | 可选必选说明：必选参数<br>参数含义：该参数用于指示APN本地签约数据索引对应的APN，是否为本APN群组内的默认APN。<br>数据来源：本端规划<br>取值范围：<br>- NO（否）<br>- YES（是）<br>默认值：NO（否）<br>配置原则：<br>- 一个APN群组里最多只能有一个默认APN。<br>- 默认APN的APNNI不支持通配符。<br>- 当APN群组里有多条APN时，要指定其中一个为默认APN。 |

#### [使用实例](#ZH-CN_CONCEPT_0000001264181038)

添加HSS BYPASS最小APN签约数据群组，可以用如下命令：

```
ADD HSSBPAPNGRP: APNGRPID=1, APNSUBIDX=1, DEFAULTAPN=YES;
```
