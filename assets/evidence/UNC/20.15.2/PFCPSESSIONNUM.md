# 显示PFCP会话上下文数量（DSP PFCPSESSIONNUM）

- [命令功能](#ZH-CN_MMLREF_0000001587258857__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001587258857__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001587258857__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001587258857__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0000001587258857__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0000001587258857)

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用于查询PFCP会话上下文数量。

## [注意事项](#ZH-CN_MMLREF_0000001587258857)

查询所有UPF时，输出显示所有UPF的PFCP会话数，按照UPF、IP路径信息逐行显示，最多显示1000行。

#### [操作用户权限](#ZH-CN_MMLREF_0000001587258857)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001587258857)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QRYCLASS | 查询分类 | 可选必选说明：必选参数<br>参数含义：该参数用于指定查询PFCP会话上下文的类型。<br>数据来源：本端规划<br>取值范围：<br>- “IPADDR（IPADDR）”：查询指定IP路径的PFCP会话上下文数。<br>- “SPECIFIED_UPF（SPECIFIED_UPF）”：查询指定UPF的PFCP会话上下文数。<br>- “ALL_UPF（ALL_UPF）”：查询所有UPF的PFCP会话上下文数。<br>默认值：无<br>配置原则：无 |
| NFINSTANCENAME | UPF实例名称 | 可选必选说明：该参数在"QRYCLASS"配置为"IPADDR"、"SPECIFIED_UPF"时为条件必选参数。<br>参数含义：该参数用于指定UPF实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~36。不区分大小写。<br>默认值：无<br>配置原则：无 |
| IPADDRTYPE | IP地址类型 | 可选必选说明：该参数在"QRYCLASS"配置为"IPADDR"时为条件必选参数。<br>参数含义：该参数用于指定IP地址类型。<br>数据来源：全网规划<br>取值范围：<br>- IPV4（IPV4）<br>- IPV6（IPV6）<br>默认值：无<br>配置原则：无 |
| IPV4ADDR | 查询路径的IPv4地址 | 可选必选说明：该参数在"IPADDRTYPE"配置为"IPV4"时为条件必选参数。<br>参数含义：该参数用于指定查询路径的对端IPv4类型地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。IPv4支持A，B，C类地址及0.0.0.0。<br>默认值：无<br>配置原则：<br>本参数取值与<br>[**ADD PNFPROFILE**](../../../服务化接口管理/注册与服务发现/本地NRF功能管理/对端NF实例概述信息管理/增加对端NF实例概述信息（ADD PNFPROFILE）_09653772.md)<br>命令中的IPV4ADDRESS1、IPV4ADDRESS2、IPV4ADDRESS3、IPV4ADDRESS4其中一个相同。 |
| IPV6ADDR | 查询路径的IPv6地址 | 可选必选说明：该参数在"IPADDRTYPE"配置为"IPV6"时为条件必选参数。<br>参数含义：该参数用于指定查询路径的对端IPv6类型地址。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。IPv6必须是全球单播地址；不能为“FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF”、环回地址(“::1”)、链路本地地址(“FE80::/10”)和组播地址(“FF00::/8”)。<br>默认值：无<br>配置原则：<br>本参数取值与<br>[**ADD PNFPROFILE**](../../../服务化接口管理/注册与服务发现/本地NRF功能管理/对端NF实例概述信息管理/增加对端NF实例概述信息（ADD PNFPROFILE）_09653772.md)<br>命令中的IPV6ADDRESS1、IPV6ADDRESS2、IPV6ADDRESS3、IPV6ADDRESS4其中一个相同。 |

## [使用实例](#ZH-CN_MMLREF_0000001587258857)

当希望查询PFCP会话上下文数量时，使用如下命令：

```
%%DSP PFCPSESSIONNUM: QRYCLASS=IPADDR, NFINSTANCENAME="upf1", IPADDRTYPE=IPV4, IPV4ADDR="192.168.0.1";%%
RETCODE = 0  操作成功

结果如下
------------------------
      UPF实例名称  =  upf1
      UPF路径地址  =  192.168.0.1
       PFCP会话数  =  0
Radius PFCP会话数  =  0
     PFCP组会话数  =  0

(结果个数 = 1)
---    END
```

## [输出结果说明](#ZH-CN_MMLREF_0000001587258857)

| 输出项名称 | 输出项解释 |
| --- | --- |
| UPF实例名称 | 该参数用于指定UPF实例名称。 |
| UPF路径地址 | 该参数用于指定查询的UPF路径地址。 |
| PFCP会话数 | 该参数表示满足查询条件的PFCP会话数。 |
| Radius PFCP会话数 | 该参数表示满足查询条件的Radius PFCP会话数。 |
| PFCP组会话数 | 该参数表示满足查询条件的PFCP组会话数。 |
