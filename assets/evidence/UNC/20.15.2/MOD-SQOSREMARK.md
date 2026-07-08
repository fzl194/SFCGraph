# 修改重标记配置（MOD SQOSREMARK）

- [命令功能](#ZH-CN_CONCEPT_0000001600600285__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000001600600285__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000001600600285__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000001600600285__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000001600600285__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0000001600600285)

该命令用来修改重标记。

#### [注意事项](#ZH-CN_CONCEPT_0000001600600285)

- V4DSCPVALUE和V4TOSVALUE、V4PRECEDENCE互斥，不能同时配置。
- V6DSCPVALUE和V6TOSVALUE、V6PRECEDENCE互斥，不能同时配置。
- 该命令仅适用于非NP卡场景和NP卡非加速模式场景。

#### [操作用户权限](#ZH-CN_CONCEPT_0000001600600285)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000001600600285)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| BEHAVIORNAME | 流行为名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定流行为名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：区分大小写，不支持空格。 |
| V4DSCPVALUE | IPv4的DSCP值 | 可选必选说明：可选参数<br>参数含义：该参数用于指定配置IPv4的DSCP（差分服务码点）值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～255。其中有效值为0～63，255为无效值，表示没有配置。<br>默认值：无<br>配置原则：至少选择一个有效的参数（V4DSCPValue，V6DSCPValue，DFValue，V4TOSVALUE，V4PRECEDENCE，V6TOSVALUE，V6PRECEDENCE，VLAN8021P）。 |
| V6DSCPVALUE | IPv6的DSCP值 | 可选必选说明：可选参数<br>参数含义：该参数用于指定配置IPv6的DSCP（差分服务码点）值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～255。其中有效值为0～63，255为无效值，表示没有配置。<br>默认值：无<br>配置原则：至少选择一个有效的参数（V4DSCPValue，V6DSCPValue，DFValue，V4TOSVALUE，V4PRECEDENCE，V6TOSVALUE，V6PRECEDENCE，VLAN8021P）。 |
| DFVALUE | DF值 | 可选必选说明：可选参数<br>参数含义：该参数用于指定配置DF（不分片标记）值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～255。其中有效值为0～1，255为无效值，表示没有配置。<br>默认值：无<br>配置原则：至少选择一个有效的参数（V4DSCPValue，V6DSCPValue，DFValue，V4TOSVALUE，V4PRECEDENCE，V6TOSVALUE，V6PRECEDENCE，VLAN8021P）。 |
| V4TOSVALUE | IPv4的TOS值 | 可选必选说明：可选参数<br>参数含义：该参数用于指定配置IPv4的TOS（服务类型）值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～255。其中有效值为0～15，255为无效值，表示没有配置。<br>默认值：无<br>配置原则：至少选择一个有效的参数（V4DSCPValue，V6DSCPValue，DFValue，V4TOSVALUE，V4PRECEDENCE，V6TOSVALUE，V6PRECEDENCE，VLAN8021P）。 |
| V4PRECEDENCE | IPv4的优先级 | 可选必选说明：可选参数<br>参数含义：该参数用于指定配置IPv4的优先级。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～255。其中有效值为0～7，255为无效值，表示没有配置。<br>默认值：无<br>配置原则：至少选择一个有效的参数（V4DSCPValue，V6DSCPValue，DFValue，V4TOSVALUE，V4PRECEDENCE，V6TOSVALUE，V6PRECEDENCE，VLAN8021P）。 |
| V6TOSVALUE | IPv6的TOS值 | 可选必选说明：可选参数<br>参数含义：该参数用于指定配置IPv6的TOS（服务类型）值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～255。其中有效值为0～15，255为无效值，表示没有配置。<br>默认值：无<br>配置原则：至少选择一个有效的参数（V4DSCPValue，V6DSCPValue，DFValue，V4TOSVALUE，V4PRECEDENCE，V6TOSVALUE，V6PRECEDENCE，VLAN8021P）。 |
| V6PRECEDENCE | IPv6的优先级 | 可选必选说明：可选参数<br>参数含义：该参数用于指定配置IPv6的优先级。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～255。其中有效值为0～7，255为无效值，表示没有配置。<br>默认值：无<br>配置原则：至少选择一个有效的参数（V4DSCPValue，V6DSCPValue，DFValue，V4TOSVALUE，V4PRECEDENCE，V6TOSVALUE，V6PRECEDENCE，VLAN8021P）。 |
| VLAN8021P | 802.1p值 | 可选必选说明：可选参数<br>参数含义：该参数用于指定VLAN报文的802.1p值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～255。其中有效值为0～7，255为无效值，表示没有配置。<br>默认值：无<br>配置原则：至少选择一个有效的参数（V4DSCPValue，V6DSCPValue，DFValue，V4TOSVALUE，V4PRECEDENCE，V6TOSVALUE，V6PRECEDENCE，VLAN8021P）。 |

#### [使用实例](#ZH-CN_CONCEPT_0000001600600285)

修改重标记配置：

```
MOD SQOSREMARK:BEHAVIORNAME="b1",DFVALUE=0,V6TOSVALUE=3,V6PRECEDENCE=3,VLAN8021P=3;
```
