# 配置UDP报文中是否携带checksum（SET UDPCHECKSUM）

- [命令功能](#ZH-CN_CONCEPT_0182837687__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0182837687__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0182837687__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0182837687__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0182837687__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0182837687)

**适用NF：SGW-U、PGW-U、UPF**

![](配置UDP报文中是否携带checksum（SET UDPCHECKSUM）_82837687.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，执行该命令时，开启UDP checksum功能前，需要确认对端支持程度，否则影响整机信令转发

该命令用来配置系统发送的UDP报文是否携带checksum。

#### [注意事项](#ZH-CN_CONCEPT_0182837687)

- 该命令执行后立即生效。
- 该命令最大记录数为3。
- 在现网中与对端网元对接时，由于对端网元的处理方式不同，对接可能会失败。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | UDPTYPE | SWITCH |
| --- | --- | --- |
| 初始值 | L2TP_CTRL | DISABLE |
| 初始值 | L2TP_DATA | DISABLE |
| 初始值 | PFCP | DISABLE |

#### [操作用户权限](#ZH-CN_CONCEPT_0182837687)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0182837687)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| UDPTYPE | UDP Type | 可选必选说明：可选参数<br>参数含义：指定是何种类型的报文。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- L2TP_CTRL：表示L2TP控制报文。<br>- L2TP_DATA：表示L2TP数据报文。<br>- PFCP：表示PFCP报文。<br>默认值：无<br>配置原则：无 |
| SWITCH | Checksum 开关 | 可选必选说明：可选参数<br>参数含义：指定系统发送的系统报文中是否携带checksum。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：<br>- IPv6报文始终开启checksum，不受配置控制。<br>- IPv4报文可以配置为ENABLE或者DISABLE。 |

#### [使用实例](#ZH-CN_CONCEPT_0182837687)

配置L2TP信令报文携带checksum：

```
SET UDPCHECKSUM:UDPTYPE=L2TP_CTRL,SWITCH=ENABLE;
```
