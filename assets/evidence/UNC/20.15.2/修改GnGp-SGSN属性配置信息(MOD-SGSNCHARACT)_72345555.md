# 修改GnGp SGSN属性配置信息(MOD SGSNCHARACT)

- [命令功能](#ZH-CN_MMLREF_0000001172345555__1.3.1.1)
- [注意事项](#ZH-CN_MMLREF_0000001172345555__1.3.2.1)
- [本地用户权限](#ZH-CN_MMLREF_0000001172345555__1.3.3.1)
- [网管用户权限](#ZH-CN_MMLREF_0000001172345555__1.3.4.1)
- [参数说明](#ZH-CN_MMLREF_0000001172345555__1.3.5.1)
- [使用实例](#ZH-CN_MMLREF_0000001172345555__1.3.6.1)

#### [命令功能](#ZH-CN_MMLREF_0000001172345555)

**适用网元：SGSN**

- 该命令用于修改SGSN的QoS属性信息。
- 该命令主要用于修改“SGSN支持的QoS版本”，该参数标识本SGSN在与该对端SGSN进行Inter RAU或Relocation流程，发送消息时可以携带的QoS信元的最高协议版本。

#### [注意事项](#ZH-CN_MMLREF_0000001172345555)

- 该命令执行后立即生效。
- 只能配置一条“ALL_SGSN(所有SGSN)”的记录；可以配置多条“SPECIAL_SGSN(指定SGSN)”的记录，但是IP网段之间不能重复。
- 本SGSN的QoS版本不能高于对端能支持的最高版本。
- “是否支持在SGSN CONTEXT RSP消息中携带RAT信元”功能仅限于华为SGSN/USN设备对接所使用，与其他设备供应商设备对接时不可能开启。

#### [本地用户权限](#ZH-CN_MMLREF_0000001172345555)

manage-ug；system-ug

#### [网管用户权限](#ZH-CN_MMLREF_0000001172345555)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_MMLREF_0000001172345555)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RANGE | 对端设备范围 | 可选必选说明：可选参数<br>参数含义：该参数用于指定对端设备的范围。<br>数据来源：整网规划<br>取值范围：<br>“ALL_SGSN(所有SGSN)”<br>、<br>“SPECIAL_SGSN(指定SGSN)”<br>默认值： 无<br>说明：本参数不输入时，修改<br>“对端设备范围”<br>为<br>“ALL_SGSN(所有SGSN)”<br>的记录。 |
| IPT | IP地址类型 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定对端SGSN的信令面IP地址类型。<br>前提条件：当对端设备类型为<br>“SPECIAL_SGSN(指定SGSN)”<br>时显示。<br>数据来源：整网规划<br>取值范围：<br>“IPV4”<br>、<br>“IPV6”<br>默认值：无<br>配置原则：<br>- IPV4：表示对端SGSN的信令面IP地址为IPV4类型。<br>- IPV6：表示对端SGSN的信令面IP地址为IPV6类型。 |
| IPV4 | SGSN IPv4信令面地址 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定对端SGSN的信令面IPV4地址。<br>前提条件：当<br>“IPT（IP地址类型）”<br>为<br>“IPV4”<br>时显示。<br>数据来源：整网规划<br>取值范围：0.0.0.1～255.255.255.254<br>配置原则：<br>- 有效的IPV4地址不能为环回地址(127.x.y.z)。<br>- 有效的IPV4地址必须是A、B或者C类地址。<br>默认值： 无 |
| MASKV4 | 掩码 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定对端SGSN的信令面IPV4地址的掩码。<br>前提条件：当<br>“IPT（IP地址类型）”<br>为<br>“IPV4”<br>时显示。<br>数据来源：整网规划<br>取值范围：0.0.0.1～255.255.255.255<br>默认值： 无<br>说明：输入的掩码要求对应的二进制值1和1之间不允许存在0。例如：<br>“255.255.0.0”<br>是有效掩码；<br>“123.123.123.123”<br>是无效掩码。因为123对应的二进制为“1111011”，1之间存在0。 |
| IPV6 | SGSN IPv6信令面地址 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定SGSN配置的信令面IPV6地址。<br>前提条件：当<br>“IPT（IP地址类型）”<br>为<br>“IPV6”<br>时显示。<br>数据来源：整网规划<br>取值范围：::～FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值： 无<br>配置原则：IPV6地址必须是全球单播地址，不能为::、FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址(::1)、链路本地地址(FE80::/10)和组播地址(FF00::/8)。 |
| MASKV6 | 子网前缀长度 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定子网前缀的长度。<br>前提条件：当<br>“IPT（IP地址类型）”<br>为<br>“IPV6”<br>时显示。<br>数据来源：整网规划<br>取值范围：1～128（数值型）<br>默认值： 无 |
| QOSVER | SGSN支持的QoS版本 | 可选必选说明：可选参数<br>参数含义：该参数用于指定对端SGSN支持的QoS版本。该字段标识本端SGSN在向该对端SGSN发送消息时可以携带的QoS信元的最高协议版本。<br>数据来源：与对端SGSN协商<br>取值范围：<br>“R99QOS(R99QOS)”<br>、<br>“R5QOS(R5QOS)”<br>、<br>“R7QOS(R7QOS)”<br>默认值：无<br>配置原则：<br>- 本端SGSN的QoS版本不能高于对端能支持的最高版本。当设置某对端SGSN的属性为“R7QOS”时，要确保该SGSN支持R7QOS，以免因设备不兼容而导致流程失败。<br>- 本端SGSN和对端SGSN对接时，若对端SGSN只支持R99QOS，“SGSN支持的QoS版本”只能设置为“R99 QoS”。<br>- 若对端SGSN支持R5QOS，“SGSN支持的QoS版本”可以设置为“R5QOS”或者“R99QOS”。<br>- 若对端SGSN支持R7QOS，“SGSN支持的QoS版本”可以设置为“R7QOS”、“R5QOS”或者“R99QOS”。 |
| GNPATHVER | Gn接口的GTP-C路径版本规则 | 可选必选说明：可选参数<br>参数含义：该参数用于指定到SGSN的Gn接口GTP-C路径的版本规则。<br>数据来源：与对端SGSN网元协商<br>取值范围：<br>“Negotiated(协商)”<br>、<br>“V1(V1)”<br>默认值：无<br>说明：- 此参数选择“Negotiated(协商)”时，GTP-C路径版本规则通过协商决定。系统在发送请求消息第一次创建GTP-C路径时，会先发送V1 GTP-C消息。如果收到对端SGSN响应，则GTP-C路径版本为V1， 如果没有收到响应，再会发送V0 GTP-C消息。如果收到对端SGSN响应，则GTP-C路径版本为V0，如果没有收到响应，则GTP-C路径版本为未知。<br>- 此参数选择“V1(V1)”时，系统创建到对端SGSN的GTP-C路径版本为V1。<br>- 如果对端网元只支持V0版本的GTP-C消息，当将此参数设置为“V1(V1)”时，可能会出现到此对端的GTP-C路径版本在V1和V0之间切换。 |
| SUPPORTRATIE | 是否支持在SGSN CONTEXT RSP消息中携带RAT信元 | 可选必选说明：可选参数<br>参数含义：该参数用于指定是否支持在SGSN CONTEXT RSP消息中携带RAT信元。该字段功能仅限于华为SGSN/USN设备对接所使用，与其他设备供应商设备对接时不可能开启。<br>数据来源：整网规划<br>取值范围：<br>- “NO（否）”<br>- “YES（是）”<br>默认值：无 |
| ARD | 是否携带扩展接入限制数据 | 可选必选说明：可选参数<br>参数含义：该参数用于指定是否在SGSN Context Response、Forward Relocation Request消息中携带接入限制数据信元（Access Restriction Data）。<br>数据来源：全网规划<br>取值范围：<br>- “NO（否）”<br>- “YES（是）”<br>默认值：<br>“无”<br>配置原则：如果对端网元支持接入限制数据信元（Access Restriction Data），设置本参数为<br>“YES（是）”<br>；否则设置本参数为<br>“NO（否）”<br>。 |
| ALTER | 对端网元是否支持Alternative信元 | 可选必选说明：可选参数<br>参数含义：该参数用于指示对端网元是否支持SGSN Context Response、Forward Relocation Request消息中携带Alternative GGSN Address for control Plane和Alternative GGSN Address for user traffic信元。<br>数据来源：对端协商<br>取值范围：<br>- NO（不支持）：表示对端网元不支持Alternative GGSN Address for control Plane和Alternative GGSN Address for user traffic信元。<br>- YES（支持）：表示对端网元支持Alternative GGSN Address for control Plane和Alternative GGSN Address for user traffic信元。<br>默认值： 无 |
| GGSNCTLIPPLCY | GGSN Address for control plane信元携带策略 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定向对端网元发送SGSN Context Response或Forward Relocation Request消息中GGSN Address for control plane信元的地址类型携带策略。<br>前提条件：该参数在<br>“对端网元是否支持Alternative信元”<br>参数配置为<br>“NO（不支持）”<br>后生效。<br>数据来源：对端协商<br>取值范围：<br>- SGSNIPONLY（仅与对端网元控制面地址类型相同）：表示GGSN Address for control plane信元仅支持携带与对端网元控制面地址类型一致的地址。<br>- IPV4ONLY（仅支持携带IPv4地址）：表示GGSN Address for control plane信元仅支持携带IPv4类型地址。<br>- IPV6ONLY（仅支持携带IPv6地址）：表示GGSN Address for control plane信元仅支持携带IPv6类型地址。<br>- SGSNIPPRE（优先与对端网元控制面地址类型相同）：表示GGSN Address for control plane信元优先携带与对端网元地址类型一致的地址。<br>- IPV4PRE（优先携带IPv4地址）：表示GGSN Address for control plane信元优先携带IPv4类型地址。<br>- IPV6PRE（优先携带IPv6地址）：表示GGSN Address for control plane信元优先携带IPv6类型地址。<br>默认值：<br>“无” |
| GGSNUSRIPPLCY | GGSN Address for User Traffic信元携带策略 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定向对端网元发送SGSN Context Response或Forward Relocation Request消息中GGSN Address for User Traffic信元的地址类型携带策略。<br>前提条件：该参数在<br>“对端网元是否支持Alternative信元”<br>参数配置为<br>“NO（不支持）”<br>后生效。<br>数据来源：对端协商<br>取值范围：<br>- SGSNIPONLY（仅与对端网元控制面地址类型相同）：表示GGSN Address for control plane信元仅支持携带与对端网元控制面地址类型一致的地址。<br>- IPV4ONLY（仅支持携带IPv4地址）：表示GGSN Address for control plane信元仅支持携带IPv4类型地址。<br>- IPV6ONLY（仅支持携带IPv6地址）：表示GGSN Address for control plane信元仅支持携带IPv6类型地址。<br>- SGSNIPPRE（优先与对端网元控制面地址类型相同）：表示GGSN Address for control plane信元优先携带与对端网元地址类型一致的地址。<br>- IPV4PRE（优先携带IPv4地址）：表示GGSN Address for control plane信元优先携带IPv4类型地址。<br>- IPV6PRE（优先携带IPv6地址）：表示GGSN Address for control plane信元优先携带IPv6类型地址。<br>默认值：<br>“无” |
| ALTERCARRY | 特定场景是否携带Alternative信元 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定PDP控制面和用户面地址不同时为双栈时是否携带Alternative GGSN Address for control Plane和Alternative GGSN Address for user traffic信元。<br>前提条件：该参数在<br>“对端网元是否支持Alternative信元”<br>参数配置为<br>“YES（支持）”<br>后生效。<br>数据来源：对端协商<br>取值范围：<br>- “NO（不携带）”<br>- “YES（携带）”<br>默认值：<br>“无” |
| ALTERPLCY | Alternative信元携带策略 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定Alternative GGSN Address for control Plane和Alternative GGSN Address for user traffic信元携带策略。<br>前提条件：该参数在<br>“对端网元是否支持Alternative信元”<br>参数配置为<br>“YES（支持）”<br>后生效。<br>数据来源：对端协商<br>取值范围：<br>- CTRLPLANE（根据控制面地址类型决定）：表示当对端地址是IPv4时，GGSN Address for control Plane和GGSN Address for user traffic信元填写IPv4地址，Alternative GGSN Address for control Plane和Alternative GGSN Address for user traffic信元填写IPv6地址；当对端地址是IPv6时，GGSN Address for control Plane和GGSN Address for user traffic信元填写IPv6地址，Alternative GGSN Address for control Plane和Alternative GGSN Address for user traffic信元填写IPv4地址。<br>- IPV4FIRST（IPv4在前）：表示GGSN Address for control Plane和GGSN Address for user traffic信元填写IPv4地址，Alternative GGSN Address for control Plane和Alternative GGSN Address for user traffic信元填写IPv6地址。<br>- IPV6FIRST（IPv6在前）：表示GGSN Address for control Plane和GGSN Address for user traffic信元填写IPv6地址，Alternative GGSN Address for control Plane和Alternative GGSN Address for user traffic信元填写IPv4地址。<br>默认值：<br>“无” |
| DESC | 描述 | 可选必选说明：可选参数<br>参数含义：该参数用于增加配置命令的描述信息。<br>数据来源：整网规划<br>取值范围：0～32位字符串<br>默认值：无 |

#### [使用实例](#ZH-CN_MMLREF_0000001172345555)

修改信令面IP地址为 “192.168.168.12” ，掩码为 “255.255.255.0” 的SGSN的属性为支持R7协议版本的QoS：

MOD SGSNCHARACT: RANGE=SPECIAL_SGSN, IPT=IPV4, IPV4="192.168.168.12", MASKV4="255.255.255.0", QOSVER=R7QOS;
