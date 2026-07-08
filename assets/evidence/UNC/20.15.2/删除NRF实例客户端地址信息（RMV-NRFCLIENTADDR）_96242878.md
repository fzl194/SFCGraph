# 删除NRF实例客户端地址信息（RMV NRFCLIENTADDR）

- [命令功能](#ZH-CN_MMLREF_0296242878__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0296242878__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0296242878__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0296242878__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0296242878)

**适用NF：NRF**

该命令用于删除NRF实例客户端地址信息。

## [注意事项](#ZH-CN_MMLREF_0296242878)

- 该命令执行后立即生效。

- 主备或双活组网的场景下，如果需要配置此命令，则两个NRF上均需执行此命令，且配置参数一致。

#### [操作用户权限](#ZH-CN_MMLREF_0296242878)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0296242878)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NRFINSTANCENAME | NRF实例名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定NRF的实例名称。当参数值为“SEPP”时，NRF会将该命令配置的IP地址识别为SEPP的客户端地址。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~38。<br>默认值：无<br>配置原则：<br>该参数构成字符只能是字母A～Z或a～z、数字0～9和下划线“-”和中划线“_”。现网配置要求把容灾的SEPP客户端IP均配置上，保证SEPP和关口局NRF之间消息互转时，关口局NRF可以提前拦截消息。 |
| IPADDRESSTYPE | IP地址类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定NRF的IP地址类型。<br>数据来源：全网规划<br>取值范围：<br>- IPTypeV4（IPTypeV4）<br>- IPTypeV6（IPTypeV6）<br>默认值：无<br>配置原则：无 |
| IPV4ADDRESS | IPV4地址 | 可选必选说明：该参数在"IPADDRESSTYPE"配置为"IPTypeV4"时为条件必选参数。<br>参数含义：该参数用于指定IPV4类型地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。取值范围：1.0.0.0~255.255.255.254。Pv4地址不能为组播地址（224.x.y.z）和环回地址(127.x.y.z)。IPv4地址必须是A、B或者C类地址。<br>默认值：无<br>配置原则：无 |
| IPV6ADDRESS | IPV6地址 | 可选必选说明：该参数在"IPADDRESSTYPE"配置为"IPTypeV6"时为条件必选参数。<br>参数含义：该参数用于指定IPV6类型地址。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。取值范围：::～FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF。IPv6地址必须是全球单播地址，不能为::、FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址（::1）、链路本地地址（FE80::/10）、组播地址（FF00::/8）和IPv4映射地址（::FFFF:XXXX:XXXX），若为IPv4兼容地址时，需判断是否符合IPv4地址要求。<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0296242878)

删除NRF实例客户端地址信息，NRF实例名称为NRF_Instance_0，IP地址类型为IPV4类型，IPV4地址为192.168.0.1。

```
RMV NRFCLIENTADDR: NRFINSTANCENAME="NRF_Instance_0", IPADDRESSTYPE=IPTypeV4, IPV4ADDRESS="192.168.0.1";
```
