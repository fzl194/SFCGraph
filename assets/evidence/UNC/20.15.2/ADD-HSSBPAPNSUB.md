# 增加HSS BYPASS最小APN签约数据配置 (ADD HSSBPAPNSUB)

- [命令功能](#ZH-CN_CONCEPT_0000001311385437__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000001311385437__1.3.2.1)
- [本地用户权限](#ZH-CN_CONCEPT_0000001311385437__1.3.3.1)
- [网管用户权限](#ZH-CN_CONCEPT_0000001311385437__1.3.4.1)
- [参数说明](#ZH-CN_CONCEPT_0000001311385437__1.3.5.1)
- [使用实例](#ZH-CN_CONCEPT_0000001311385437__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0000001311385437)

**适用网元：MME**

此命令用于新增最小APN签约数据群组对应的最小APN签约数据。

用户处于HSS BYPASS状态之后，无法从HSS获取用户签约数据，如果系统内无用户历史签约数据，使用该命令手动配置用户最小APN签约数据，保证业务惯性运行。

#### [注意事项](#ZH-CN_CONCEPT_0000001311385437)

- 该命令执行后立即生效。
- 此命令最大记录数为256。

#### [本地用户权限](#ZH-CN_CONCEPT_0000001311385437)

manage-ug；system-ug

#### [网管用户权限](#ZH-CN_CONCEPT_0000001311385437)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000001311385437)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APNSUBIDX | APN本地签约索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN本地签约数据索引。<br>数据来源：全网规划<br>取值范围：0~255<br>默认值：无<br>配置原则：无 |
| APNNI | APNNI | 可选必选说明：必选参数<br>参数含义：该参数用来指定APNNI信息。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~62<br>默认值：无<br>配置原则：<br>- APN网络标识地址由一个或多个LABEL构成，各LABEL间用“.”间隔。<br>- 每个LABEL的构成字符只能是字母A～Z或a～z、数字0～9和中划线“-”或者配置为通配符“*”，字母不区分大小写。<br>- APN网络标识地址不能以“rac”、“lac”、“sgsn”或“rnc”开头，不能以“.gprs”结尾。 |
| PDNTYPE | PDN类型 | 可选必选说明：必选参数<br>参数含义：该参数用来指定PDN类型。<br>数据来源：全网规划<br>取值范围：<br>- IPV4（IPv4）<br>- IPV6（IPv6）<br>- IPV4_AND_IPV6（IPv4和IPv6）<br>- IPV4_OR_IPv6（IPv4或IPv6）<br>默认值：IPV4（IPv4）<br>配置原则：无 |
| APNAMBRULK | 上行APN AMBR （kbps） | 可选必选说明：必选参数<br>参数含义：该参数用于指定用户Non-GBR承载的上行APN最大速率。<br>数据来源：全网规划<br>取值范围：1kbps～65000000kbps。<br>默认值：无<br>配置原则：无 |
| APNAMBRDLK | 下行APN AMBR （kbps） | 可选必选说明：必选参数<br>参数含义：该参数用于指定用户Non-GBR承载的下行APN最大速率。<br>数据来源：整网规划<br>取值范围：1kbps～65000000kbps。<br>默认值：无<br>配置原则：无 |
| ISNRIWK | 4-5G互操作 | 可选必选说明：可选参数<br>参数含义：该参数用于指定该APN对应的承载是否支持4-5G互操作。<br>数据来源：全网规划<br>取值范围：<br>- SUPPORT（支持）<br>- NOT_SUPPORT（不支持）<br>默认值：SUPPORT（支持）<br>配置原则：无 |
| QCI | QCI | 可选必选说明：必选参数<br>参数含义：该参数用于指定该APN的QCI。<br>数据来源：全网规划<br>取值范围：0~254<br>默认值：无<br>配置原则：无 |
| PRIORITY | 控制优先级 | 可选必选说明：必选参数<br>参数含义：该参数用于指定该APN的QCI控制优先级。<br>数据来源：全网规划<br>取值范围：1~15<br>默认值：无<br>配置原则：参数值越小优先级越高 |
| CHARGINGCHAR | 计费属性 | 可选必选说明：可选参数<br>参数含义：该参数用于指定该APN的计费属性。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为0000~FFFF<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0000001311385437)

添加HSS BYPASS最小APN签约数据配置，可以用如下命令：

```
ADD HSSBPAPNSUB: APNSUBIDX=1, APNNI="1234", PDNTYPE=IPV4, APNAMBRULK=2, APNAMBRDLK=2, ISNRIWK=SUPPORT, QCI=0, PRIORITY=2;
```
