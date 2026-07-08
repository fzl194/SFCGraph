# 增加振荡抑制路由（ADD DAMPROUTE）

- [命令功能](#ZH-CN_CONCEPT_0000001600841517__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000001600841517__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000001600841517__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000001600841517__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000001600841517__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0000001600841517)

该命令用于增加路由振荡抑制的配置参数。

#### [注意事项](#ZH-CN_CONCEPT_0000001600841517)

- 该命令执行后立即生效。
- 该命令最大记录数为65536。
- REUSE、SUPPRESS、CEILING三个阈值是依次增大的，即必须满足：REUSE < SUPPRESS < CEILING。
- 该命令中的各配置参数没有缺省值，必须显式配置。根据公式MaxSuppressTime=half-life-reach×60×(ln(ceiling/reuse)/ln(2))，如果MaxSuppressTime小于1就不能抑制。所以要保证MaxSuppressTime大于等于1，即必须满足：ceiling/reuse足够大。

#### [操作用户权限](#ZH-CN_CONCEPT_0000001600841517)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000001600841517)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：_public_<br>配置原则：使用LST L3VPNINST命令查看可用VPN。 |
| AFTYPE | 地址族类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定VRF的地址族类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4uni：IPv4地址族。<br>- ipv4vpn：VPNv4地址族。<br>- ipv6uni：IPv6地址族。<br>默认值：无 |
| PEERTYPE | 对等体类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定对等体类型是EBGP还是IBGP。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ebgp：EBGP。<br>- ibgp：IBGP。<br>默认值：ebgp<br>配置原则：只有在ipv4vpn地址族下，该参数才能配置为ibgp。 |
| HALFLIFEREACHTIME | 可达路由半衰期（min） | 可选必选说明：可选参数<br>参数含义：该参数用于指定可达路由的半衰期。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～45，单位是分钟。<br>默认值：15 |
| REUSE | 重用阈值 | 可选必选说明：可选参数<br>参数含义：该参数用于指定路由解除抑制状态的阈值。当惩罚降低到该值以下，路由就被再使用。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～20000。<br>默认值：750<br>配置原则：REUSE、SUPPRESS、CEILING三个阈值是依次增大的。 |
| SUPPRESS | 抑制阈值 | 可选必选说明：可选参数<br>参数含义：该参数用于指定路由进入抑制状态的阈值。当惩罚值超过该极限时，路由受到抑制。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～20000。<br>默认值：2000<br>配置原则：REUSE、SUPPRESS、CEILING三个阈值是依次增大的。 |
| CEILING | 惩罚上限值 | 可选必选说明：可选参数<br>参数含义：该参数用于指定路由的惩罚上限值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1001～20000。<br>默认值：16000<br>配置原则：REUSE、SUPPRESS、CEILING三个阈值是依次增大的。 |
| DAMPOLICYNAME | 衰减策略 | 可选必选说明：可选参数<br>参数含义：该参数用于指定对路由进行抑制的策略名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～200。<br>默认值：无<br>配置原则：在此之前应使用ADD ROUTEPOLICY命令配置对应策略。使用LST ROUTEPOLICY命令查看可用路由策略。 |
| UPDATESTANDARD | 收到Update报文时增加标准惩罚值 | 可选必选说明：可选参数<br>参数含义：该参数用于指定是否收到Update报文时增加标准惩罚值。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：FALSE |

#### [使用实例](#ZH-CN_CONCEPT_0000001600841517)

为公网IPv4单播地址族配置路由振荡抑制：

```
SET BGP:ASNUM="100",BGPENABLE=TRUE;
ADD DAMPROUTE:VRFNAME="_public_",AFTYPE=ipv4uni;
```
