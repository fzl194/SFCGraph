# 增加安全策略告警配置（ADD SECPOLICYALARM）

- [命令功能](#ZH-CN_CONCEPT_0000001550121370__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000001550121370__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000001550121370__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000001550121370__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000001550121370__1.3.5.1)
- [参考信息](#ZH-CN_CONCEPT_0000001550121370__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0000001550121370)

该命令用来添加上送CPU报文产生告警参数的配置。

CPU防攻击丢弃的报文数目超出配置的告警产生阈值，产生告警。CPU防攻击丢弃的报文数目低于配置的告警清除阈值，告警恢复。

#### [注意事项](#ZH-CN_CONCEPT_0000001550121370)

- 该命令执行后立即生效。
- 该命令最大记录数为512。
- 该命令仅适用于非NP卡场景和NP卡非加速模式场景。

#### [操作用户权限](#ZH-CN_CONCEPT_0000001550121370)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000001550121370)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SECPOLICYID | 安全策略编号 | 可选必选说明：必选参数<br>参数含义：安全策略编号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～30。<br>默认值：无<br>配置原则：需要先添加安全策略，下发本MML命令前可使用LST SECPOLICY查看已添加的安全策略。 |
| SECPOLICYTYPE | 安全策略类型 | 可选必选说明：必选参数<br>参数含义：策略类型，如应用层联动、TCP/IP防攻击、黑白名单等。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- Tcpip：TCP/IP策略。<br>- TotalPkt：所有报文。<br>- WhiteList：白名单策略。<br>- BlackList：黑名单策略。<br>- Index：索引策略。<br>- UserFlow：用户自定义流策略。<br>- APP：APP应用策略。<br>- Urpf：URPF策略。<br>- WhiteListV6：IPv6白名单。<br>默认值：无 |
| SECPOLICYTYPEID | 安全策略类型编号 | 可选必选说明：条件必选参数<br>前提条件：该参数在“SECPOLICYTYPE”配置为“Index” 或 “UserFlow”时为必选参数。<br>参数含义：安全策略类型编号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535。<br>默认值：无<br>配置原则：<br>- 如果SECPOLICYTYPE选择Tcpip/Protocol/WhiteList/BlackList/WhiteListV6，则本项不选。如果SECPOLICYTYPE选择Index/UserFlow则本项必选。<br>- 如果SECPOLICYTYPE选择Index，需要根据DSP SECCARINFO查看安全CAR系统ID并在[35，1658]区间，48、95及[125，158]区间除外。如果SECPOLICYTYPE选择UserFlow，本参数在[1，32]之间。 |
| SECALARMFLAG | 安全告警使能 | 可选必选说明：必选参数<br>参数含义：策略告警是否使能。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无 |
| SECALARMTHLD | 安全告警阈值 | 可选必选说明：必选参数<br>参数含义：告警阈值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～1000000。<br>默认值：无 |
| SECALARMINT | 安全告警时间间隔（秒） | 可选必选说明：必选参数<br>参数含义：告警时间间隔。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为60～3600，单位是秒。<br>默认值：无 |

#### [使用实例](#ZH-CN_CONCEPT_0000001550121370)

添加上送CPU报文产生告警参数的配置：

```
ADD SECPOLICYALARM:SECPOLICYID=1,SECPOLICYTYPE=WhiteList,SECALARMFLAG=TRUE,SECALARMTHLD=1,SECALARMINT=60;
```

#### [参考信息](#ZH-CN_CONCEPT_0000001550121370)

需要先添加安全策略。
