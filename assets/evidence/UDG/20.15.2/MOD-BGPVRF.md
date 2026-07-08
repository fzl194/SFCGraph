# 修改BGP VPN实例（MOD BGPVRF）

- [命令功能](#ZH-CN_CONCEPT_0000001600441417__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000001600441417__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000001600441417__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000001600441417__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000001600441417__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0000001600441417)

该命令用来修改已创建的BGP VPN实例。

![](修改BGP VPN实例（MOD BGPVRF）_00441417.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，如果修改路由器ID、VPN路由器ID自动选择、存活时间、保持时间会导致地址族下的对等体重连。

#### [注意事项](#ZH-CN_CONCEPT_0000001600441417)

- 该命令执行后立即生效。
- 修改路由器ID、VPN路由器ID自动选择、存活时间、保持时间会导致地址族下的对等体重连。

#### [操作用户权限](#ZH-CN_CONCEPT_0000001600441417)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000001600441417)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VRFNAME | VPN实例名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定BGP VPN实例。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：使用LST BGPVRF命令查看可用VPN。 |
| EBGPIFSENSITIVE | EBGP接口感知 | 可选必选说明：可选参数<br>参数含义：使能后，当某个接口状态变为Down时，立即清除建立在该接口上的直连EBGP邻居的BGP会话。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无<br>配置原则：只在公网下起作用。 |
| IBGPIFSENSITIVE | IBGP接口感知 | 可选必选说明：可选参数<br>参数含义：使能后，当某个接口状态变为Down时，立即清除建立在该接口上的直连IBGP邻居的BGP会话。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无<br>配置原则：只在公网下起作用。 |
| ROUTERID | 路由器ID | 可选必选说明：可选参数<br>参数含义：该参数用于指定BGP VPN实例的路由器ID。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～15。IPv4地址格式，但不允许输入0.0.0.0或255.255.255.255。<br>默认值：无<br>配置原则：<br>- 输入单空格将删除该参数已有配置项。<br>- ROUTERID和VRFRIDAUTOSEL的配置相互覆盖，且二者不可同时配置。 |
| VRFRIDAUTOSEL | VPN路由器ID自动选择 | 可选必选说明：可选参数<br>参数含义：该参数指定是否设置VPN实例自动选择Router ID。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无<br>配置原则：VRFRIDAUTOSEL只对私网起作用，公网下配置不起作用，ROUTERID和VRFRIDAUTOSEL的配置相互覆盖，且二者不可同时配置。 |
| KEEPALIVETIME | 存活时间（s） | 可选必选说明：可选参数<br>参数含义：该参数用于指定存活时间。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～21845，单位是秒。<br>默认值：无<br>配置原则：KEEPALIVETIME和HOLDTIME配合使用，且HOLDTIME至少为KEEPALIVETIME的3倍，默认值为60。该参数只支持在公网下配置，ADD命令不使用该参数。HOLDTIME和KEEPALIVETIME均取值为0会导致BGP定时器无效，无法检测链路故障，带来流量损失。HOLDTIME取值远大于KEEPALIVETIME时，这样网络中keepalive消息较多，而且即使长时间收不到keepalive消息，也会不认为连接已中断。 |
| HOLDTIME | 保持时间（s） | 可选必选说明：可选参数<br>参数含义：该参数用于指定BGP邻居建立后，未收到KEEPALIVE报文但邻居仍保持活跃状态的保持时间。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535，单位是秒。<br>默认值：无<br>配置原则：KEEPALIVETIME和HOLDTIME配合使用，且HOLDTIME至少为KEEPALIVETIME的3倍，默认值为180。该参数只支持在公网下配置，ADD命令不使用该参数。HOLDTIME和KEEPALIVETIME均取值为0会导致BGP定时器无效，无法检测链路故障，带来流量损失。HOLDTIME取值远大于KEEPALIVETIME时，这样网络中keepalive消息较多，而且即使长时间收不到keepalive消息，也会不认为连接已中断。 |
| CONNRETRYTIME | 重连时间（s） | 可选必选说明：可选参数<br>参数含义：该参数用于指定BGP邻居状态不活跃，尝试重新建立连接的等待时间。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～65535，单位是秒。<br>默认值：无<br>配置原则：该参数默认值为32。该参数只支持在公网下配置，ADD命令不使用该参数。 |

#### [使用实例](#ZH-CN_CONCEPT_0000001600441417)

修改名称为“vrf1”的BGP VPN实例：

```
MOD BGPVRF:VRFNAME="vrf1", ROUTERID="192.168.2.0";
```
