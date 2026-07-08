# 增加信元携带控制配置（ADD SMFIEADAPTER）

- [命令功能](#ZH-CN_MMLREF_0000001304057516__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001304057516__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001304057516__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001304057516__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0000001304057516)

![](增加信元携带控制配置（ADD SMFIEADAPTER）_04057516.assets/notice_3.0-zh-cn_2.png)

执行该命令，可能会导致SMF发送给周边网元的消息信元携带有误。

**适用NF：SMF**

该命令用于新增控制SMF与周边网元之间消息中的信元是否携带的配置。

## [注意事项](#ZH-CN_MMLREF_0000001304057516)

- 该命令执行后立即生效。

- 最多可输入1000条记录。

#### [操作用户权限](#ZH-CN_MMLREF_0000001304057516)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001304057516)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ITFNODEROLE | 接口和网元类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定需要控制的接口和网元类型。<br>数据来源：本端规划<br>取值范围：<br>- “N16_VSMF（N16_VSMF）”：N16接口上本端网元为V-SMF<br>- “N16_HSMF（N16_HSMF）”：N16接口上本端网元为H-SMF<br>- “N16a_ISMF（N16a_ISMF）”：N16a接口上本端网元为I-SMF<br>- “N16a_HSMF（N16a_HSMF）”：N16a接口上本端网元为H-SMF<br>- “N7（N7）”：N7接口<br>- “N40（N40）”：N40接口<br>- “N16_PROXYSMF（N16_PROXYSMF）”：N16接口上本端网元为PROXYSMF<br>默认值：无<br>配置原则：无 |
| PROCTYPE | 流程类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定需要控制的流程类型。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~128。<br>默认值：无<br>配置原则：无 |
| PROCMSGID | 流程消息标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定需要控制的流程消息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~128。<br>默认值：无<br>配置原则：无 |
| CTRLIE | 需要控制的信元 | 可选必选说明：必选参数<br>参数含义：该参数用于指定需要控制的信元。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：无 |
| IECTRLSW | 信元携带控制开关 | 可选必选说明：必选参数<br>参数含义：该参数用于指定是否携带控制的信元。<br>数据来源：本端规划<br>取值范围：<br>- “DISABLE（不使能）”：表示信元配置为不携带<br>- “ENABLE（使能）”：表示信元配置为携带<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0000001304057516)

新增一条配置控制VSMF会话创建流程中，VSMF发送给HSMFN16的创建消息中RequestType信元不携带，执行如下命令：

```
ADD SMFIEADAPTER: ITFNODEROLE=N16_VSMF, PROCTYPE="PduSessionEstAsVsmf", PROCMSGID="PostPduSessionsParameters", CTRLIE="PduSessionCreateData.RequestType", IECTRLSW=DISABLE;
```
