# 增加M2M服务器组（ADD M2MSERVERGRP）

- [命令功能](#ZH-CN_MMLREF_0273321226__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0273321226__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0273321226__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0273321226__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0273321226)

**适用NF：PGW-C、SMF**

该命令用于添加一个M2M服务器组。

## [注意事项](#ZH-CN_MMLREF_0273321226)

- 该命令执行后立即生效。

- 通过ADD M2MSERVER可以设置M2M服务器具体信息。
- 通过ADD M2MSVRGRPBIND可以设置M2M服务器组绑定关系。UNC通过绑定关系选择对应M2M服务器组。

- 最多可输入1000条记录。

#### [操作用户权限](#ZH-CN_MMLREF_0273321226)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0273321226)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GROUPNAME | M2M服务器组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定M2M服务器组的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~31。字符串类型，输入长度范围为1～31。不区分大小写，不支持空格。<br>默认值：无<br>配置原则：无 |
| SERVERIPTYPE | M2M服务器IP地址类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定M2M服务器的IP地址类型。<br>数据来源：本端规划<br>取值范围：<br>- IPV4（IPv4）<br>- IPV6（IPv6）<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0273321226)

配置组名为m2msrvgroup01，服务器IP类型为IPV4的M2M服务器组：

```
ADD M2MSERVERGRP: GROUPNAME="m2msrvgroup01", SERVERIPTYPE=IPV4;
```
