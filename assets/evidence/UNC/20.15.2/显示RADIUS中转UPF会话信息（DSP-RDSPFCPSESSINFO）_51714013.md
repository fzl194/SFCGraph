# 显示RADIUS中转UPF会话信息（DSP RDSPFCPSESSINFO）

- [命令功能](#ZH-CN_MMLREF_0000001151714013__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001151714013__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001151714013__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001151714013__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0000001151714013__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0000001151714013)

**适用NF：SMF、PGW-C、GGSN**

该命令用于显示RADIUS中转UPF，UPC创建的会话信息。

## [注意事项](#ZH-CN_MMLREF_0000001151714013)

无

#### [操作用户权限](#ZH-CN_MMLREF_0000001151714013)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001151714013)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QUERYTYPE | 查询类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定查询类型。<br>数据来源：本端规划<br>取值范围：<br>- IPTYPE（Radius客户端IP类型）<br>- PEERTEID（RADIUS中转UPF会话中UPF分配的N4口TEID）<br>默认值：无<br>配置原则：无 |
| IPTYPE | IP类型 | 可选必选说明：该参数在"QUERYTYPE"配置为"IPTYPE"时为条件必选参数。<br>参数含义：表示Radius客户端的IP类型。<br>数据来源：本端规划<br>取值范围：<br>- IPV4（IPv4类型的地址）<br>- IPV6（IPv6类型的地址）<br>默认值：无<br>配置原则：无 |
| PEERTEID | 对端TEID | 可选必选说明：该参数在"QUERYTYPE"配置为"PEERTEID"时为条件必选参数。<br>参数含义：表示Radius中转UPF会话中UPF分配的N4口TEID。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~4294967295。<br>默认值：无<br>配置原则：无 |
| CLIENTIPV4 | Radius客户端IPv4地址 | 可选必选说明：该参数在"IPTYPE"配置为"IPV4"时为条件必选参数。<br>参数含义：表示Radius客户端的IPv4地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| CLIENTIPV6 | Radius客户端IPv6地址 | 可选必选说明：该参数在"IPTYPE"配置为"IPV6"时为条件必选参数。<br>参数含义：表示Radius客户端的IPv6地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |
| PEERIPTYPE | 对端IP类型 | 可选必选说明：该参数在"QUERYTYPE"配置为"PEERTEID"时为条件可选参数。<br>参数含义：表示对端IP类型。<br>数据来源：本端规划<br>取值范围：<br>- IPV4（IPv4类型的地址）<br>- IPV6（IPv6类型的地址）<br>默认值：无<br>配置原则：无 |
| PEERIPV4ADDR | 对端IPv4地址 | 可选必选说明：该参数在"PEERIPTYPE"配置为"IPV4"时为条件必选参数。<br>参数含义：表示Radius中转Upf会话中Upf分配的IPv4地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| PEERIPV6ADDR | 对端IPV6地址 | 可选必选说明：该参数在"PEERIPTYPE"配置为"IPV6"时为条件必选参数。<br>参数含义：表示Radius中转Upf会话中Upf分配的IPv6地址。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0000001151714013)

查询PeerTEID为“2148532224”的RADIUS中转UPF的会话信息。 DSP RDSPFCPSESSINFO: QUERYTYPE=PEERTEID, PEERTEID=2148532224;

```
%%DSP RDSPFCPSESSINFO:QUERYTYPE=PEERTEID,PEERTEID=2148532224;%%
RETCODE = 0  操作成功。

结果如下
------------------------
            查询类型  =  PEERTEID
              IP类型  =  IPv4 Address
Radius客户端IPv4地址  =  10.2.102.17
Radius客户端IPv6地址  =  ::
          UP实例标识  =  upf_instance_1
            本端TEID  =  8348532224
            对端TEID  =  2148532224
        本端IPv4地址  =  192.168.208.11
        本端IPv6地址  =  ::
        对端IPv4地址  =  192.168.48.11
        对端IPv6地址  =  ::
(结果个数 = 1)

---    END
```

## [输出结果说明](#ZH-CN_MMLREF_0000001151714013)

| 输出项名称 | 输出项解释 |
| --- | --- |
| Radius客户端IPv4地址 | 表示Radius客户端的IPv4地址。 |
| Radius客户端IPv6地址 | 表示Radius客户端的IPv6地址。 |
| UP实例标识 | 该参数用于指定UP实例标识。 |
| 对端TEID | 表示Radius中转UPF会话中UPF分配的N4口TEID。 |
| 本端TEID | 表示Radius中转UPF会话中SMF分配的N4口TEID。 |
| 本端IPv4地址 | 表示本端分配的IPv4地址（ADD CPGTPUADDR中配置的IPv4地址）。 |
| 本端IPv6地址 | 表示Radius中转UPF会话中SMF分配的IPv6地址（ADD CPGTPUADDR中配置的IPv6地址）。 |
| 对端IPv4地址 | 表示Radius中转Upf会话中Upf分配的IPv4地址。 |
| 对端IPV6地址 | 表示Radius中转Upf会话中Upf分配的IPv6地址。 |
| 查询类型 | 该参数用于指定查询类型。<br>取值说明：<br>- IPTYPE（Radius客户端IP类型）<br>- PEERTEID（RADIUS中转UPF会话中UPF分配的N4口TEID） |
| IP类型 | 表示Radius客户端的IP类型。<br>取值说明：<br>- IPV4（IPv4类型的地址）<br>- IPV6（IPv6类型的地址） |
