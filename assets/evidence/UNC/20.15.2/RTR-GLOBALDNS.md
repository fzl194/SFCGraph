# 恢复系统默认DNS（RTR GLOBALDNS）

- [命令功能](#ZH-CN_MMLREF_0209652557__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0209652557__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0209652557__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0209652557__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0209652557)

**适用NF：SMF**

该命令用于恢复系统DNS地址配置信息，即将默认值设置成无效值。

## [注意事项](#ZH-CN_MMLREF_0209652557)

该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_MMLREF_0209652557)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0209652557)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DNSSERVERTYPE | DNS服务器类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定DNS服务器类型。<br>数据来源：本端规划<br>取值范围：<br>- DNS_IPV4（IPv4 DNS Server）<br>- DNS_IPV6（IPv6 DNS Server）<br>- DNS_64（DNS64 Server）<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0209652557)

在运营商网络中需要清除已经配置的系统的缺省的DNS配置信息，执行该命令：

```
RTR GLOBALDNS: DNSSERVERTYPE=DNS_IPV4;
```
