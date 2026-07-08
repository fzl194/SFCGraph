# 增加本省OCS的IP号段（ADD LOCALOCSIP）

- [命令功能](#ZH-CN_MMLREF_0245110910__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0245110910__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0245110910__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0245110910__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0245110910)

**适用NF：NCG**

该命令用于增加本省OCS的IP号段。

## [注意事项](#ZH-CN_MMLREF_0245110910)

- 该命令执行后立即生效。

- 最多可输入1024条记录。

#### [操作用户权限](#ZH-CN_MMLREF_0245110910)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0245110910)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| OCSID | OCS标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定OCS标识。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~40。只允许输入字母，数字和中划线。<br>默认值：无<br>配置原则：无 |
| IPADDRESSTYPE | IP地址类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定IP地址类型。<br>数据来源：本端规划<br>取值范围：<br>- IPV4（IPv4地址）<br>- IPV6（IPv6地址）<br>默认值：无<br>配置原则：无 |
| IPV4ADDRESS | IPv4地址 | 可选必选说明：该参数在"IPADDRESSTYPE"配置为"IPV4"时为条件必选参数。<br>参数含义：该参数用于指定IPv4地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| IPV6ADDRESS | IPv6地址 | 可选必选说明：该参数在"IPADDRESSTYPE"配置为"IPV6"时为条件必选参数。<br>参数含义：该参数用于指定IPv6地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0245110910)

增加OCS标识为ocsid001，IP类型为IPV4，IP地址为192.168.100.1的本省OCS的IP号段：

```
ADD LOCALOCSIP:OCSID="ocsid001",IPADDRESSTYPE=IPV4,IPV4ADDRESS="192.168.100.1";
```
