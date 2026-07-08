# 增加P-CSCF组配置（ADD PCSCFGROUP）

- [命令功能](#ZH-CN_MMLREF_0209653619__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0209653619__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0209653619__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0209653619__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0209653619)

**适用NF：PGW-C、SMF、GGSN**

该命令用于增加P-CSCF组配置。在规划IMS网络，配置P-CSCF服务器地址时，需要先执行该命令配置P-CSCF组。当P-CSCF服务器地址由DHCP服务器分配时，用户具体使用DHCP P-CSCF分组中的哪个P-CSCF地址由用户激活时外置DHCP服务器返回的响应消息决定。

## [注意事项](#ZH-CN_MMLREF_0209653619)

- 该命令执行后立即生效。

- 最多可输入256条记录。

#### [操作用户权限](#ZH-CN_MMLREF_0209653619)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0209653619)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GROUPNAME | P-CSCF组名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定P-CSCF组的名字，在系统内唯一。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。只允许输入字母、数字、“.”、“_”和“-”。字母会被转换为小写字母进行存储和处理。<br>默认值：无<br>配置原则：无 |
| IPVERSION | IP地址版本 | 可选必选说明：可选参数<br>参数含义：该参数用于指定IP地址类型。<br>数据来源：本端规划<br>取值范围：<br>- “IPV4（IPV4）”：IPv4地址类型<br>- “IPV6（IPV6）”：IPv6地址类型<br>默认值：IPV4<br>配置原则：无 |
| ALLOCTYPE | P-CSCF获取方式 | 可选必选说明：可选参数<br>参数含义：该参数用于P-CSCF服务器地址分配方式。<br>数据来源：本端规划<br>取值范围：<br>- “LOCAL（本地分配）”：在网络规划p-cscf服务器地址由UNC本地配置的时，配置分组类型为LOCAL。<br>- “DHCP（DHCP分配）”：在网络规划p-cscf服务器地址由DHCP服务器分配时，配置分组类型为DHCP。<br>默认值：LOCAL<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0209653619)

当运营商规划使用IMS网络，需要配置IPV4地址类型的P-CSCF组，举例：

```
ADD PCSCFGROUP: GROUPNAME="mygroup", ALLOCTYPE=LOCAL;
```
