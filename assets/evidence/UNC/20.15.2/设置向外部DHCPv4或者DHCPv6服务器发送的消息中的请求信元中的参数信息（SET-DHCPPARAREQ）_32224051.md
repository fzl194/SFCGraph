# 设置向外部DHCPv4或者DHCPv6服务器发送的消息中的请求信元中的参数信息（SET DHCPPARAREQ）

- [命令功能](#ZH-CN_MMLREF_0000001232224051__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001232224051__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001232224051__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001232224051__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0000001232224051)

**适用NF：PGW-C、SMF、GGSN**

该命令用来配置向外部DHCPv4或者DHCPv6服务器发送的消息中的请求信元中的参数信息。

## [注意事项](#ZH-CN_MMLREF_0000001232224051)

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| V4DNSSERVER | V4PCSCFSERVER | V6DNSSERVER | V6PCSCFSERVER |
| --- | --- | --- | --- |
| ENABLE | DISABLE | ENABLE | DISABLE |

#### [操作用户权限](#ZH-CN_MMLREF_0000001232224051)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001232224051)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| V4DNSSERVER | 指定DHCPv4消息中是否请求DNS服务器地址 | 可选必选说明：可选参数<br>参数含义：指定DHCPv4消息中是否请求DNS服务器地址。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE（不使能）<br>- ENABLE（使能）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST DHCPPARAREQ查询当前参数配置值。<br>配置原则：无 |
| V4PCSCFSERVER | 指定DHCPv4消息中是否请求P-CSCF服务器地址 | 可选必选说明：可选参数<br>参数含义：指定DHCPv4消息中是否请求P-CSCF服务器地址。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE（不使能）<br>- ENABLE（使能）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST DHCPPARAREQ查询当前参数配置值。<br>配置原则：无 |
| V6DNSSERVER | 指定DHCPv6消息中是否请求DNS服务器地址 | 可选必选说明：可选参数<br>参数含义：指定DHCPv6消息中是否请求DNS服务器地址。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE（不使能）<br>- ENABLE（使能）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST DHCPPARAREQ查询当前参数配置值。<br>配置原则：无 |
| V6PCSCFSERVER | 指定DHCPv6消息中是否请求P-CSCF服务器地址 | 可选必选说明：可选参数<br>参数含义：指定DHCPv6消息中是否请求P-CSCF服务器地址。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE（不使能）<br>- ENABLE（使能）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST DHCPPARAREQ查询当前参数配置值。<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0000001232224051)

指定DHCPv4消息中，DNS服务器地址、P-CSCF服务器地址是使能的。指定DHCPv6消息中，DNS服务器地址、P-CSCF服务器地址是使能的：

```
SET DHCPPARAREQ:V4DNSSERVER=ENABLE,V4PCSCFSERVER=ENABLE,V6DNSSERVER=ENABLE,V6PCSCFSERVER=ENABLE;
```
