# 设置计费控制配置（SET CHARGECTRL）

- [命令功能](#ZH-CN_CONCEPT_0209896792__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0209896792__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0209896792__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0209896792__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0209896792__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0209896792)

**适用NF：PGW-C、SMF**

![](设置计费控制配置（SET CHARGECTRL）_09896792.assets/notice_3.0-zh-cn_2.png)

本命令属于高危命令，此操作会影响新激活用户的计费方式(在线、离线、融合)，可能导致用户无法计费。

本命令用来控制是否基于用户漫游、拜访、本地属性来提供在线计费、离线计费和融合计费功能。

#### [注意事项](#ZH-CN_CONCEPT_0209896792)

- 该命令执行后只对新激活用户生效。
- 该命令最大记录数为1。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | HOMEONLINE | HOMECONVERGED | HOMEOFFLINE | VISITONLINE | VISITOFFLINE | VISITCONVERGED | ROAMONLINE | ROAMOFFLINE | ROAMCONVERGED | N40BKPTRAFFIC | GAGYBKPTRAFFIC |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 初始值 | ENABLE | ENABLE | ENABLE | ENABLE | ENABLE | ENABLE | ENABLE | ENABLE | ENABLE | ENABLE | ENABLE |

#### [操作用户权限](#ZH-CN_CONCEPT_0209896792)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0209896792)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| HOMEONLINE | 归属地在线用户计费控制 | 可选必选说明：可选参数<br>参数含义：归属地用户计费控制。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- DISABLE：否。<br>- ENABLE：是。<br>默认值：无<br>配置原则：无 |
| HOMECONVERGED | 归属地融合用户计费控制 | 可选必选说明：可选参数<br>参数含义：归属地融合计费用户计费控制。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- DISABLE：否。<br>- ENABLE：是。<br>默认值：无<br>配置原则：无 |
| HOMEOFFLINE | 归属地离线用户计费控制 | 可选必选说明：可选参数<br>参数含义：归属地离线用户计费控制。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- DISABLE：否。<br>- ENABLE：是。<br>默认值：无<br>配置原则：无 |
| VISITONLINE | 拜访地在线计费用户计费控制 | 可选必选说明：可选参数<br>参数含义：拜访地在线计费用户计费控制。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- DISABLE：否。<br>- ENABLE：是。<br>默认值：无<br>配置原则：无 |
| VISITOFFLINE | 拜访地离线计费用户计费控制 | 可选必选说明：可选参数<br>参数含义：拜访地离线计费用户计费控制。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- DISABLE：否。<br>- ENABLE：是。<br>默认值：无<br>配置原则：无 |
| VISITCONVERGED | 拜访地融合计费用户计费控制 | 可选必选说明：可选参数<br>参数含义：拜访地融合计费用户计费控制。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- DISABLE：否。<br>- ENABLE：是。<br>默认值：无<br>配置原则：无 |
| ROAMONLINE | 漫游在线计费用户计费控制 | 可选必选说明：可选参数<br>参数含义：漫游在线计费用户计费控制。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- DISABLE：否。<br>- ENABLE：是。<br>默认值：无<br>配置原则：无 |
| ROAMOFFLINE | 漫游离线计费用户计费控制 | 可选必选说明：可选参数<br>参数含义：漫游离线计费用户计费控制。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- DISABLE：否。<br>- ENABLE：是。<br>默认值：无<br>配置原则：无 |
| ROAMCONVERGED | 漫游融合计费用户计费控制 | 可选必选说明：可选参数<br>参数含义：漫游融合计费用户计费控制。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- DISABLE：否。<br>- ENABLE：是。<br>默认值：无<br>配置原则：无 |
| N40BKPTRAFFIC | 融合计费是否支持处理备份流量 | 可选必选说明：可选参数<br>参数含义：该参数用于控制融合计费是否支持处理UPF上报的备份流量。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |
| GAGYBKPTRAFFIC | 在线离线计费是否支持处理备份流量 | 可选必选说明：可选参数<br>参数含义：该参数用于控制在线离线计费是否支持处理UPF上报的备份流量。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0209896792)

配置计费控制配置，归属地融合计费为DISABLE，拜访地融合计费为DISABLE：

```
SET CHARGECTRL: HOMECONVERGED=DISABLE, VISITCONVERGED=DISABLE;
```
