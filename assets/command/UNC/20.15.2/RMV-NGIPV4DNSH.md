---
id: UNC@20.15.2@MMLCommand@RMV NGIPV4DNSH
type: MMLCommand
name: RMV NGIPV4DNSH（删除IPv4 DNS Hostfile记录）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: NGIPV4DNSH
command_category: 配置类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- NRF业务参数
- DNS客户端管理
status: active
---

# RMV NGIPV4DNSH（删除IPv4 DNS Hostfile记录）

## 功能

![](删除IPv4 DNS Hostfile记录（RMV NGIPV4DNSH）_09653031.assets/notice_3.0-zh-cn_2.png)

如果一个主机名对应的所有IP地址都被删除，以Hostfile方式进行DNS查询时，该主机名将不能在本地被解析，请谨慎使用。

**适用NF：AMF**

该命令用于删除网元接口所对应的IP地址信息。当只输入主机名，会删除主机名对应的所有IP地址。当输入主机名+地址区间号，会删除主机名在输入地址区间号的所有IP地址。

## 注意事项

- 该命令执行后立即生效。

- 如果一个主机名对应的所有IP地址都被删除，以Hostfile方式进行DNS查询时，该主机名将不能被解析。
- 该命令执行后，可能导致HTTP的FQDN链路信息地址发生变更，建议通过执行CHK SBILINKFQDNIP，核查HTTP的链路信息。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| HOSTNAME | 主机名 | 可选必选说明：必选参数<br>参数含义：该参数用于配置主机名。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：<br>参见命令ADD NGIPV4DNSH。 |
| ADDRSECTION | 地址区间号 | 可选必选说明：可选参数<br>参数含义：该参数用于划分IP地址区间。一个域名最多可以配置64个IP地址，使用该参数将64个IP地址划分为8个区间，每个区间配置8个IP地址，减少了配置复杂度。所有区间的IP地址按照优先级和权重进行排序。<br>数据来源：全网规划<br>取值范围：<br>- SECTION1（SECTION1）<br>- SECTION2（SECTION2）<br>- SECTION3（SECTION3）<br>- SECTION4（SECTION4）<br>- SECTION5（SECTION5）<br>- SECTION6（SECTION6）<br>- SECTION7（SECTION7）<br>- SECTION8（SECTION8）<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [IPv4 DNS Hostfile记录（NGIPV4DNSH）](configobject/UNC/20.15.2/NGIPV4DNSH.md)

## 使用实例

网络改造过程中，某个网元不再使用，删除主机名为“HUAWEI3.COM.GTP.APN.EPC.MNC123.MCC456.3GPPNETWORK.ORG”所对应的所有IP地址记录。

```
RMV NGIPV4DNSH: HOSTNAME="HUAWEI3.COM.GTP.APN.EPC.MNC123.MCC456.3GPPNETWORK.ORG";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除IPv4-DNS-Hostfile记录（RMV-NGIPV4DNSH）_09653031.md`
