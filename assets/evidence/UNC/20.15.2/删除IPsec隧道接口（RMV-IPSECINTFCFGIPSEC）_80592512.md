# 删除IPsec隧道接口（RMV IPSECINTFCFGIPSEC）

- [命令功能](#ZH-CN_MMLREF_0000001180592512__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001180592512__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001180592512__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001180592512__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0000001180592512)

![](删除IPsec隧道接口（RMV IPSECINTFCFGIPSEC）_80592512.assets/notice_3.0-zh-cn_2.png)

删除IPSEC隧道，该条链路会直接断连，导致业务流量掉底。

该命令用于删除IPsec隧道。

## [注意事项](#ZH-CN_MMLREF_0000001180592512)

该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_MMLREF_0000001180592512)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001180592512)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INTERFACENAME | 接口名称 | 可选必选说明：必选参数<br>参数含义：配置接口名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。<br>默认值：无<br>配置原则：无 |
| TNLTYPE | Tunnel口协议类型 | 可选必选说明：必选参数<br>参数含义：Tunnel口协议类型。<br>数据来源：本端规划<br>取值范围：<br>- “IPSEC（IPv4IP安全）”：IPv4IP安全<br>- “IPSEC6（IPv6IP安全）”：IPv6IP安全<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0000001180592512)

删除接口名为“Tunnel1/1/1”，协议类型为“IPv4IP安全”的隧道：

```
RMV IPSECINTFCFGIPSEC:INTERFACENAME="Tunnel 1/1/1",TNLTYPE=IPSEC;
```
