# 删除静态ASN（RMV STATICASN）

- [命令功能](#ZH-CN_MMLREF_0000001139850025__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001139850025__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001139850025__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001139850025__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0000001139850025)

**适用NF：SGW-C、PGW-C、GGSN**

该命令用来删除SGSN、SGW-C信令地址和ASN映射的本地表项。

## [注意事项](#ZH-CN_MMLREF_0000001139850025)

该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_MMLREF_0000001139850025)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001139850025)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RANGE | 范围 | 可选必选说明：可选参数<br>参数含义：该参数用于设置删除静态ASN配置时的范围。<br>数据来源：本端规划<br>取值范围：<br>- “SPECIFIC_IP（指定IP）”：删除指定IP记录<br>- “ALL（所有）”：删除所有记录<br>默认值：SPECIFIC_IP<br>配置原则：无 |
| SRVNODEIP | Service Node信令IP地址 | 可选必选说明：该参数在"RANGE"配置为"SPECIFIC_IP"时为条件必选参数。<br>参数含义：该参数用于设置SGSN、SGW-C的信令IP。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| MASK | IP掩码 | 可选必选说明：该参数在"RANGE"配置为"SPECIFIC_IP"时为条件必选参数。<br>参数含义：该参数用于设置SGSN、SGW-C信令IP的掩码。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0000001139850025)

删除一个sgsn-ip为10.13.13.0，掩码类型为掩码长度的ASN配置：

```
RMV STATICASN: RANGE=SPECIFIC_IP, SRVNODEIP="10.13.13.0", MASK="255.255.255.0";
```
