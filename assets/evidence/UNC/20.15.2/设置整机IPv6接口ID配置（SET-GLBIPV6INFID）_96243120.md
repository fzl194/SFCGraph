# 设置整机IPv6接口ID配置（SET GLBIPV6INFID）

- [命令功能](#ZH-CN_MMLREF_0296243120__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0296243120__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0296243120__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0296243120__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0296243120)

**适用NF：PGW-C、GGSN、SMF**

该命令用于控制为用户分配IPv6地址时，是否开启IMSI作为用户的IPv6地址Interface ID功能。

## [注意事项](#ZH-CN_MMLREF_0296243120)

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| IMSI |
| --- |
| DISABLE |

#### [操作用户权限](#ZH-CN_MMLREF_0296243120)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0296243120)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IMSI | 配置IMSI作为IPv6 Interface ID | 可选必选说明：必选参数<br>参数含义：该参数用于控制开启和关闭IMSI作为用户的IPv6地址Interface ID功能。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE（不使能）<br>- ENABLE（使能）<br>默认值：无。<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0296243120)

配置IMSI作为用户的IPv6地址Interface ID功能使能：

```
SET GLBIPV6INFID: IMSI=ENABLE;
```
