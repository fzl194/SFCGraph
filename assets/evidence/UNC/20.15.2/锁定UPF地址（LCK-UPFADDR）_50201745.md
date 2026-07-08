# 锁定UPF地址（LCK UPFADDR）

- [命令功能](#ZH-CN_MMLREF_0000001450201745__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001450201745__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001450201745__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001450201745__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0000001450201745)

**适用NF：SGW-C、GGSN、PGW-C、SMF**

该命令用于锁定UPF地址。锁定后新激活的用户不会选择该UPF地址建立PFCP会话。

## [注意事项](#ZH-CN_MMLREF_0000001450201745)

该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_MMLREF_0000001450201745)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001450201745)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| UPINSTANCEID | UPF实例标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定UPF实例名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~36。不区分大小写。<br>默认值：无<br>配置原则：<br>本参数取值与ADD PNFPROFILE命令中的“NF实例标识”参数取值保持一致。 |
| IPVERSION | UPF的IP版本 | 可选必选说明：必选参数<br>参数含义：该参数用于指定UPF的IP地址类型。<br>数据来源：全网规划<br>取值范围：<br>- IPV4（IPV4）<br>- IPV6（IPV6）<br>默认值：无<br>配置原则：无 |
| IPV4ADDR | UPF的IPv4地址 | 可选必选说明：该参数在"IPVERSION"配置为"IPV4"时为条件必选参数。<br>参数含义：该参数用于指定UPF的IPv4地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。IPv4只支持A，B，C类地址。<br>默认值：无<br>配置原则：无 |
| IPV6ADDR | UPF的IPv6地址 | 可选必选说明：该参数在"IPVERSION"配置为"IPV6"时为条件必选参数。<br>参数含义：该参数用于指定UPF的IPv6地址。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。IPv6必须是全球单播地址；不能为“FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF”、环回地址(“::1”)、链路本地地址(“FE80::/10”)和组播地址(“FF00::/8”)。<br>默认值：无<br>配置原则：无 |
| STARTTIMER | 是否开启定时器 | 可选必选说明：必选参数<br>参数含义：该参数用于指定是否开启定时器用于解锁UPF地址。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE（不使能）<br>- ENABLE（使能）<br>默认值：无<br>配置原则：无 |
| LCKDURATION | 加锁时长(小时) | 可选必选说明：该参数在"STARTTIMER"配置为"ENABLE"时为条件必选参数。<br>参数含义：该参数用于指定加锁定时器时长，单位为小时。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~240。<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0000001450201745)

为实例名称为“UP1”的UPF锁定其“10.0.0.2”的IPV4地址，并启动定时器。该地址将于2小时后自动解锁。

```
LCK UPFADDR: UPINSTANCEID="UP1", IPVERSION=IPV4, IPV4ADDR="10.0.0.2",STARTTIMER=ENABLE, LCKDURATION=2;
```
