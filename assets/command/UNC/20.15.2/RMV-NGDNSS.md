---
id: UNC@20.15.2@MMLCommand@RMV NGDNSS
type: MMLCommand
name: RMV NGDNSS（删除DNS服务器）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: NGDNSS
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

# RMV NGDNSS（删除DNS服务器）

## 功能

![](删除DNS服务器（RMV NGDNSS）_25121204.assets/notice_3.0-zh-cn_2.png)

该命令执行以后，网元将不会再向此DNS服务器发送域名解析请求，可能造成某些域名无法解析，请慎用此命令。

**适用NF：AMF**

该命令用于删除一个DNS服务器。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPTYPE | IP地址类型 | 可选必选说明：必选参数<br>参数含义：该参数用于表示IP地址类型。<br>数据来源：本端规划<br>取值范围：<br>- IPV4（IPv4）<br>- IPV6（IPv6）<br>默认值：无<br>配置原则：无 |
| IPV4 | IPv4地址 | 可选必选说明：该参数在"IPTYPE"配置为"IPV4"时为条件必选参数。<br>参数含义：该参数用于表示DNS服务器的IPv4地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：<br>IPv4地址不能为0.0.0.0。 |
| IPV6 | IPv6地址 | 可选必选说明：该参数在"IPTYPE"配置为"IPV6"时为条件必选参数。<br>参数含义：该参数用于表示DNS服务器的IPv6地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：<br>IPv6地址必须是全球单播地址，不能为::、FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址(::1)、链路本地地址(FE80::/10)和组播地址(FF00::/8)。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NGDNSS]] · DNS服务器（NGDNSS）

## 使用实例

删除一条IP类型为IPv4，IPv4地址为192.168.100.101的DNS服务器：

```
RMV NGDNSS: IPTYPE=IPV4, IPV4="192.168.100.101";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-NGDNSS.md`
