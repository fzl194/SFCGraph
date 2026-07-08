# 修改Pre-R8 QoS到TOS/DSCP的映射规则（MOD PRER8REMARK）

- [命令功能](#ZH-CN_MMLREF_0209652464__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0209652464__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0209652464__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0209652464__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0209652464)

**适用NF：GGSN**

该命令用于修改QoS参数映射到IP报文头中的TOS（服务类型）或者DSCP（区别服务编码点）的映射配置。

## [注意事项](#ZH-CN_MMLREF_0209652464)

- 该命令执行后立即生效。

- 该命令执行后只对新激活用户生效。
- RFC2597推荐的BE编码点：000000；RFC2598推荐的EF编码点：101110。

#### [操作用户权限](#ZH-CN_MMLREF_0209652464)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0209652464)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QOSPROFILENAME | QoS Profile名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定QosProfile的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。不区分大小写。<br>默认值：无<br>配置原则：<br>该参数需要先通过ADD QOSPROFILE或者SET QOSGLOBAL命令配置。 |
| SERVICELEVEL | 业务级别 | 可选必选说明：必选参数<br>参数含义：该参数用于指定业务级别。<br>数据来源：本端规划<br>取值范围：<br>- “CONVERSATIONAL（会话业务）”：会话业务。<br>- “STM_GBR_MORE25K（下行保证带宽大于等于25kbit/s的流类业务）”：下行保证带宽大于等于25kbit/s的流类业务。<br>- “STM_GBR_LESS25K（下行保证带宽小于25kbit/s的流类业务）”：下行保证带宽小于25kbit/s的流类业务。<br>- “INT_TC_PRI1（发送控制优先级为1的交互类业务）”：发送控制优先级为1的交互类业务。<br>- “INT_TC_PRI2（发送控制优先级为2的交互类业务）”：发送控制优先级为2的交互类业务。<br>- “INT_TC_PRI3（发送控制优先级为3的交互类业务）”：发送控制优先级为3的交互类业务。<br>- “BACKGROUND（背景业务）”：背景业务。<br>- “GENERAL（通用业务）”：通用业务。<br>默认值：无<br>配置原则：无 |
| USERPRIORITY | 用户级别 | 可选必选说明：必选参数<br>参数含义：该参数用于指定用户级别。<br>数据来源：本端规划<br>取值范围：<br>- “GENERAL（通用用户）”：通用用户。<br>- “HIGH（高端用户）”：高端用户。<br>- “NORMAL（普通用户）”：普通用户。<br>- “LOW（低端用户）”：低端用户。<br>默认值：无<br>配置原则：无 |
| REMARKTYPE | 标记类型 | 可选必选说明：必选参数<br>参数含义：该参数用于设置映射到DSCP或者TOS。<br>数据来源：全网规划<br>取值范围：<br>- “DSCP（DSCP）”：映射到DSCP。<br>- “TOS（TOS）”：映射到TOS<br>默认值：无<br>配置原则：无 |
| DSCP | DSCP | 可选必选说明：该参数在"REMARKTYPE"配置为"DSCP"时为条件必选参数。<br>参数含义：该参数用于设置映射到DSCP的值。<br>数据来源：全网规划<br>取值范围：<br>- “EF（EF）”：对应的DSCP的值为46。<br>- “AF（AF）”：对应的DSCP的值由参数AF级别和AF丢弃优先级界定。<br>- “BE（BE）”：对应的DSCP的值为0。<br>- “CS6（CS6）”：对应的DSCP的值为48。<br>- “CS7（CS7）”：对应的DSCP的值为56。<br>- “DSCP_VALUE（DSCP_VALUE）”：映射的DSCP值。<br>默认值：无<br>配置原则：无 |
| AFCLASS | AF级别 | 可选必选说明：该参数在"DSCP"配置为"AF"时为条件必选参数。<br>参数含义：该参数用于设置AF队列序号。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~4。<br>默认值：无<br>配置原则：无 |
| AFDROPPREC | AF丢弃优先级 | 可选必选说明：该参数在"DSCP"配置为"AF"时为条件必选参数。<br>参数含义：该参数用于设置AF丢弃优先级。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~3。<br>默认值：无<br>配置原则：无 |
| TOSVALUE | TOS值 | 可选必选说明：该参数在"REMARKTYPE"配置为"TOS"时为条件必选参数。<br>参数含义：该参数用于设置映射到TOS的值。分别对应IP优先级的8个队列ID，优先级高的报文先于优先级低的报文发送。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~7。<br>默认值：无<br>配置原则：无 |
| DSCPVALUE | DSCP值 | 可选必选说明：该参数在"DSCP"配置为"DSCP_VALUE"时为条件必选参数。<br>参数含义：该参数用于设置DSCP。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~63。<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0209652464)

修改QoS Profile名称为“profile”，会话级别为“CONVERSATIONAL”，用户级别为“HIGH”的QoS的DSCP的映射信息，修改标记类型为“DSCP”,参数“DSCP”为“EF”：

```
MOD PRER8REMARK: QOSPROFILENAME="profile", SERVICELEVEL=CONVERSATIONAL, USERPRIORITY=HIGH, REMARKTYPE=DSCP, DSCP=EF;
```
