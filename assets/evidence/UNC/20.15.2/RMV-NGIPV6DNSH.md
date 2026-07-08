# 删除IPv6 DNS Hostfile记录（RMV NGIPV6DNSH）

- [命令功能](#ZH-CN_MMLREF_0209653120__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0209653120__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0209653120__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0209653120__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0209653120)

![](删除IPv6 DNS Hostfile记录（RMV NGIPV6DNSH）_09653120.assets/notice_3.0-zh-cn_2.png)

如果一个主机名对应的所有IP地址都被删除，以Hostfile方式进行DNS查询时，该主机名将不能在本地被解析，请谨慎使用。

**适用NF：AMF**

该命令用于删除网元接口所对应的IPv6地址信息。

## [注意事项](#ZH-CN_MMLREF_0209653120)

- 该命令执行后立即生效。

- 如果一个主机名对应的所有IP地址都被删除，以Hostfile方式进行DNS查询时，该主机名将不能被解析。
- 该命令执行后，可能导致HTTP的FQDN链路信息地址发生变更，建议通过执行CHK SBILINKFQDNIP，核查HTTP的链路信息。

#### [操作用户权限](#ZH-CN_MMLREF_0209653120)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0209653120)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| HOSTNAME | 主机名 | 可选必选说明：必选参数<br>参数含义：该参数用于配置主机名。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~255。该参数只能由字母（A-Z或者a-z）、数字（0-9）、连字符（-）和点（.）组成，大小写不敏感，主机名不能以“.”开始，也不能以“.”结束。<br>默认值：无<br>配置原则：无 |
| ADDRSECTION | 地址区间号 | 可选必选说明：可选参数<br>参数含义：该参数用于划分IP地址区间。一个域名最多可以配置64个IP地址，使用该参数将64个IP地址划分为8个区间，每个区间配置8个IP地址，减少了配置复杂度。所有区间的IP地址按照优先级和权重进行排序。<br>数据来源：全网规划<br>取值范围：<br>- SECTION1（SECTION1）<br>- SECTION2（SECTION2）<br>- SECTION3（SECTION3）<br>- SECTION4（SECTION4）<br>- SECTION5（SECTION5）<br>- SECTION6（SECTION6）<br>- SECTION7（SECTION7）<br>- SECTION8（SECTION8）<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0209653120)

网络改造过程中，某个网元不再使用，删除该“主机名”为“HUAWEI4.COM.GTP.APN.EPC.MNC123.MCC456.3GPPNETWORK.ORG”的HOSTFILE记录：

```
RMV NGIPV6DNSH: HOSTNAME="HUAWEI4.COM.GTP.APN.EPC.MNC123.MCC456.3GPPNETWORK.ORG";
```
